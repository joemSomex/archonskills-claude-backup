#!/usr/bin/env bash
# Restore the Archon workflows, Claude Code skills and Hermes skills captured in
# this repo onto a fresh host. Safe to re-run: anything it would overwrite is
# moved aside to a timestamped .bak-<UTC> sibling first.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GALATEA_REPO="${GALATEA_REPO:-/root/galatea-system-stagin}"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"

DRY=0 ALL_HERMES=0 SKIP_VENDOR=0
while [ $# -gt 0 ]; do
  case "$1" in
    --dry-run)            DRY=1 ;;
    --all-hermes-skills)  ALL_HERMES=1 ;;
    --skip-vendor)        SKIP_VENDOR=1 ;;
    -h|--help)
      sed -n '2,5p' "${BASH_SOURCE[0]}"
      echo "Flags: --dry-run  --all-hermes-skills  --skip-vendor"
      exit 0 ;;
    *) echo "install.sh: unknown flag $1" >&2; exit 1 ;;
  esac
  shift
done

say()  { printf '  %s\n' "$*"; }
head_() { printf '\n== %s\n' "$*"; }
run()  { if [ "$DRY" = 1 ]; then say "would: $*"; else "$@"; fi; }

# Move an existing path aside before we replace it, so a re-run is never lossy.
preserve() {
  local target="$1"
  [ -e "$target" ] || [ -L "$target" ] || return 0
  say "backing up existing $target -> $target.bak-$STAMP"
  run mv "$target" "$target.bak-$STAMP"
}

# Copy a tree from the repo to its home, preserving whatever was there.
restore_tree() {
  local src="$1" dest="$2"
  [ -e "$src" ] || { say "skip (not in backup): $src"; return 0; }
  preserve "$dest"
  run mkdir -p "$(dirname "$dest")"
  run cp -a "$src" "$dest"
  say "restored $dest"
}

head_ "Archon"
restore_tree "$REPO/archon/workflows" "$GALATEA_REPO/.archon/workflows"
restore_tree "$REPO/archon/config.yaml" "$HOME/.archon/config.yaml"
if [ -d "$GALATEA_REPO/.git" ]; then
  restore_tree "$REPO/archon/factory-consumer.json" "$GALATEA_REPO/.factory/consumer.json"
else
  say "no Galatea checkout at $GALATEA_REPO -- clone it, then re-run with GALATEA_REPO set"
fi
restore_tree "$REPO/archon/bin/galatea-archon" "$HOME/.local/bin/galatea-archon"
run chmod +x "$HOME/.local/bin/galatea-archon" 2>/dev/null || true

head_ "Claude Code skills"
run mkdir -p "$HOME/.claude/skills" "$HOME/.agents"
restore_tree "$REPO/claude/skills/galatea-archon" "$HOME/.claude/skills/galatea-archon"
restore_tree "$REPO/claude/agents-skills" "$HOME/.agents/skills"
restore_tree "$REPO/claude/agents-skill-lock.json" "$HOME/.agents/.skill-lock.json"
restore_tree "$REPO/claude/settings.json" "$HOME/.claude/settings.json"

# ~/.claude/skills/<name> -> ~/.agents/skills/<name> is how Claude Code picks the
# Cole Medin skills up; the lock file records them but does not create the links.
say "linking Cole Medin skills into ~/.claude/skills"
for d in "$REPO"/claude/agents-skills/*/; do
  name="$(basename "$d")"
  link="$HOME/.claude/skills/$name"
  [ -L "$link" ] && continue
  preserve "$link"
  run ln -s "../../.agents/skills/$name" "$link"
done

head_ "Hermes skills"
run mkdir -p "$HOME/.hermes/skills"
if [ "$ALL_HERMES" = 1 ]; then
  say "restoring the entire Hermes skill tree (vendor bundles included)"
  run rsync -a "$REPO/hermes/skills/" "$HOME/.hermes/skills/"
else
  say "restoring hand-authored Hermes skills only (--all-hermes-skills for everything)"
  while read -r rel; do
    [ -n "$rel" ] || continue
    restore_tree "$REPO/hermes/skills/$rel" "$HOME/.hermes/skills/$rel"
  done < "$REPO/meta/hermes-custom-skills.txt"
fi

run mkdir -p "$HOME/.hermes/bin"
for s in coleskills-hermes-sync gstack-hermes-sync hermes-wrap-response-patch; do
  restore_tree "$REPO/hermes/bin/$s" "$HOME/.hermes/bin/$s"
  run chmod +x "$HOME/.hermes/bin/$s" 2>/dev/null || true
done

if [ "$SKIP_VENDOR" = 1 ]; then
  head_ "Vendor installs skipped (--skip-vendor)"
else
  head_ "Vendor installs"
  # gstack is a git install (~1.7GB of node_modules and binaries once `./setup`
  # runs), which is why it is cloned here rather than committed to this repo.
  GSTACK_DIR="$HOME/.claude/skills/gstack"
  if [ -d "$GSTACK_DIR" ]; then
    say "gstack already present at $GSTACK_DIR -- leaving it alone"
  else
    say "cloning gstack from https://github.com/garrytan/gstack.git"
    run git clone --depth 1 https://github.com/garrytan/gstack.git "$GSTACK_DIR"
    say "running gstack setup (this pulls node_modules and browser binaries)"
    run bash -c "cd '$GSTACK_DIR' && ./setup"
  fi
  say "refreshing the Cole Medin skills against the committed lock file"
  run npx -y skills update
fi

head_ "Mirrors"
# Both sync scripts regenerate the gstack-*/piv-*/plan-* mirrors under
# ~/.hermes/skills, which is why those are not committed to this repo.
for s in gstack-hermes-sync coleskills-hermes-sync; do
  if [ -x "$HOME/.hermes/bin/$s" ]; then
    say "running $s"
    run "$HOME/.hermes/bin/$s" || say "$s failed -- re-run it once Hermes is configured"
  fi
done

head_ "Done"
cat <<'NEXT'
  Files are restored. Still to do by hand:
    1. Install Hermes, sign in, restore ~/.hermes/.env, auth.json and config.yaml.
    2. claude            -- sign in to Claude Code.
    3. gh auth login     -- the workflow scope is required for factory workflows.
    4. Running as root? Archon needs IS_SANDBOX=1 or every run dies at
       triage__triage. The galatea-archon wrapper exports it for you.
    5. After `hermes update`, re-run ~/.hermes/bin/hermes-wrap-response-patch --
       the raw-delivery patch is a vendor patch and updates revert it.
    6. Hermes cron is UTC: 10 AM Manila is `0 2 * * *`.
NEXT

# archonskills-claude-backup

Portable backup of the Archon workflows, Claude Code skills and Hermes skills
running on this VPS, plus a restore script that rebuilds the same setup on a
new host.

Captured from `srv1975204` — see [`meta/versions.txt`](meta/versions.txt) for
the exact versions this snapshot was taken against.

## What is in here

| Path | What it holds |
|---|---|
| `archon/workflows/` | The Galatea project workflows (`galatea-implementation-audit`) — YAML, commands and scripts. These live in `.archon/workflows/` and are invisible to `factory run` by design. |
| `archon/config.yaml` | Global Archon config: default assistant, model tiers. |
| `archon/factory-consumer.json` | The pinned Archon revision the factory consumer builds against. |
| `archon/bin/galatea-archon` | The wrapper that runs both engines (pinned SDLC pack via the factory consumer, project workflows via the pinned CLI) and reaps spent worktrees. |
| `claude/skills/` | Hand-authored Claude Code skills (`galatea-archon`). |
| `claude/agents-skills/` | The Cole Medin skill set from `~/.agents/skills`, which `~/.claude/skills` symlinks into. |
| `claude/agents-skill-lock.json` | Source + commit hash for every Cole Medin skill. |
| `claude/settings.json` | Claude Code settings. |
| `hermes/skills/` | The full Hermes skill tree, vendor and custom alike. |
| `hermes/bin/` | The three sync/patch scripts that must be re-run after upgrades. |
| `meta/hermes-custom-skills.txt` | The 19 Hermes skills that are hand-authored — everything else in `hermes/skills/` is a vendor bundle or a mirror. |

## What is deliberately *not* in here

**gstack itself** (`~/.claude/skills/gstack`, 1.7 GB). It is a vendor install —
964 MB of `node_modules` and 158 MB of binaries — and single files in it exceed
GitHub's 100 MB limit, so it cannot live in a git repo. `install.sh` reinstalls
it from the official installer instead, which is also how you get security
updates. The same applies to the `gstack-*` skill directories under
`~/.claude/skills` and `~/.hermes/skills`: they are generated mirrors, rebuilt
by `gstack-hermes-sync`.

**Secrets.** No `~/.hermes/.env`, `auth.json`, `config.yaml`, `.credentials.json`
or SSH keys. You must supply those yourself on the new host — see *After
restoring* below.

## Restoring on a new VPS

```bash
git clone https://github.com/joemSomex/archonskills-claude-backup.git
cd archonskills-claude-backup
./install.sh              # restore custom skills + Archon, reinstall vendors
```

Useful flags:

- `./install.sh --dry-run` — print every action without touching the filesystem.
- `./install.sh --all-hermes-skills` — also restore the vendor-bundled Hermes
  skills. Off by default: Hermes ships its own copies and they are usually
  newer than this snapshot.
- `./install.sh --skip-vendor` — do not reinstall gstack or the Cole Medin
  skills, just lay down the files from this repo.
- `GALATEA_REPO=/path/to/repo ./install.sh` — restore the Archon workflows into
  a Galatea checkout somewhere other than `/root/galatea-system-stagin`.

The script never overwrites without saying so: anything it replaces is moved to
a timestamped `.bak-<UTC>` sibling first.

## After restoring

`install.sh` covers files. These need you:

1. **Hermes credentials** — install Hermes, sign in, and restore `~/.hermes/.env`,
   `auth.json` and `config.yaml` from your own secret store.
2. **Claude Code auth** — `claude` and sign in.
3. **GitHub auth** — `gh auth login`. The `workflow` scope is required for the
   factory workflows.
4. **`IS_SANDBOX=1` when running as root** — Archon's Claude provider refuses
   `bypassPermissions` under UID 0 without it and every run dies at
   `triage__triage`. The `galatea-archon` wrapper exports it for you; set it
   yourself if you call the Archon CLI directly.
5. **Re-run the sync scripts after any upgrade.** `gstack-hermes-sync` after a
   gstack upgrade, `coleskills-hermes-sync` after `npx skills update`, and
   `hermes-wrap-response-patch` after `hermes update` — the per-job raw
   delivery patch is a vendor patch and every Hermes update reverts it.
6. **Cron times are UTC.** Manila is UTC+8, so 10 AM PH is `0 2 * * *`.

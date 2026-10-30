---
name: bilingual-skill-authoring
description: "Use when creating bilingual English-Chinese skills."
version: 0.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [skills, bilingual, English, Chinese]
    related_skills: []
---

# Bilingual Skill Authoring

Create one durable skill that can be discovered and invoked in English or Chinese without duplicating its procedure.

## Procedure

1. Choose one stable lowercase ASCII slug for the technical `name` and slash command, such as `clothing-tryon-render`. Keep it language-neutral enough to remain useful when display wording changes.
2. Give the skill an English display name and a Chinese display name in its main heading, for example `# Clothing Try-On Render / 服装上身效果图`.
3. Make the frontmatter description concise and bilingual enough for discovery, with the English capability and the primary Chinese trigger in the same sentence.
4. Add natural-language trigger phrases for both languages under `## When to Use`. Include common English variants and the Chinese terms users are likely to type; do not require an exact phrase match.
5. Add a language rule to the always-on body: answer in English when the request is primarily English and in Chinese when it is primarily Chinese. Preserve canonical proper nouns, filenames, IDs, and locked source terminology unless an approved translation exists.
6. Keep one shared procedure and verification section for both languages. Translate presentation, not operational logic, so fixes cannot drift between duplicate copies.
7. Verify activation with one English natural-language request, one Chinese natural-language request, and the canonical slash command. Confirm all three load the same skill and follow the same workflow.
8. When the user asks to cross-reference, review, or consider additions from another skill, first present a change proposal that separates recommended additions, conflicts, and exclusions. Do not modify the active skill until the user explicitly approves applying the proposal. If the user directly asks to apply specific edits, make only those requested edits and verify preserved locked content.

## Always-On Rules

- Use a single skill for both languages; never create separate English and Chinese copies of the same workflow because their procedures will drift.
- Keep the slash command in ASCII. Messaging-platform command syntaxes may reject Chinese characters even though natural-language activation supports them.
- Display the skill name in the language used by the requester, or show `English / 中文` when presenting an inventory intended for both audiences.
- Treat a mandatory verbatim prompt, template, camera block, or other user-locked content as immutable during unrelated refinements. Do not translate or rewrite it merely because the invocation language changed; translate only surrounding instructions and reporting.
- Treat review-only requests as non-mutating: show the proposed additions and wait for approval before patching the live skill.
- Ask which Chinese variant is required only when the distinction matters; otherwise preserve the variant already used by the requester.

## Example

```yaml
---
name: clothing-tryon-render
description: "Use for clothing try-on renders / 服装上身效果图."
---
```

```markdown
# Clothing Try-On Render / 服装上身效果图

## When to Use
- Clothing Try-On Render
- Clothing-on-model render
- 服装上身效果图
- 服装试穿效果图
```

## Portable Backup Export

When exporting bilingual skills for external safekeeping:

1. Copy each complete skill directory into a staging tree; include `SKILL.md` plus its `references/`, `templates/`, `scripts/`, and `assets/` so the backup remains executable rather than becoming a prose-only snapshot.
2. Never edit the active skill merely to make the export bilingual. Add or normalize English and Chinese display names only in the staged copy unless the user separately asked to update the live skill.
3. Preserve the canonical ASCII skill ID and one shared procedure. Put the bilingual names in the heading or a clearly labeled bilingual-name block; do not create parallel English and Chinese skill copies.
4. Exclude runtime junk such as `.git`, `node_modules`, `__pycache__`, and compiled bytecode. Never include `.env`, authentication files, tokens, or credential stores.
5. Add one bilingual index mapping canonical ID → English name → Chinese name. Add a machine-readable manifest containing every exported file's relative path, byte size, and SHA-256 checksum.
6. Build one archive, test its integrity, verify the number of archived `SKILL.md` files equals the source count, and scan for credential-shaped strings before delivery.
7. Report the archive size, SHA-256 checksum, verified skill count, and any exclusions. Keep the source skills unchanged.

## Verification

- One canonical skill directory and technical name exist.
- English and Chinese display names are visible in the skill.
- Both languages have natural trigger phrases.
- Output language follows the request language.
- English, Chinese, and slash-command tests invoke the same procedure.
- A portable export preserves support files, contains a bilingual index and checksum manifest, passes archive integrity checks, and contains no credential files.

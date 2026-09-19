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

## Always-On Rules

- Use a single skill for both languages; never create separate English and Chinese copies of the same workflow because their procedures will drift.
- Keep the slash command in ASCII. Messaging-platform command syntaxes may reject Chinese characters even though natural-language activation supports them.
- Display the skill name in the language used by the requester, or show `English / 中文` when presenting an inventory intended for both audiences.
- Treat a mandatory verbatim prompt or template as locked content. Do not translate it merely because the invocation language changed; translate only surrounding instructions and reporting.
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

## Verification

- One canonical skill directory and technical name exist.
- English and Chinese display names are visible in the skill.
- Both languages have natural trigger phrases.
- Output language follows the request language.
- English, Chinese, and slash-command tests invoke the same procedure.

# Backup Scope and Delivery

Use this reference only when the user asks what to back up, how large it will be, how to restore it, or whether it can be delivered through a messaging platform.

## Decision table

| Need | Artifact | Contains secrets | Coverage | Delivery |
|---|---|---:|---|---|
| Portable agent settings | Start with `hermes profile export <profile> -o <temporary>.tar.gz`, then inspect and repackage to the requested whitelist | Built-in credential stores should be absent, but user-authored scripts, memories, skills, and cron prompts still require a credential scan | Scope varies by version and installation; explicitly select persona, config, memories, skills, scripts, and `cron/jobs.json`, and exclude runtime databases, sessions, knowledge/project data, caches, and external stores unless requested | Suitable for private chat only after verification, measurement, and a current platform-limit check |
| Full Hermes recovery | `hermes backup -o <archive>.zip -k 0` | Yes: `.env`, auth state, vault and platform credentials | Hermes home, sessions, profiles, skills and durable Hermes data, subject to documented runtime/cache exclusions | Never deliver through chat; encrypt and store privately off-host |
| GBrain recovery | `gbrain backup create --output <absolute-archive>` using the recorded launcher/home | Full database can contain private facts | Local PGLite plus installer-managed files | Private encrypted storage; coordinate with the owning `gbrain serve` process and never remove its live lock |
| Knowledge source recovery | Archive or sync the configured Obsidian/notes source | Usually private | Editable source documents; does not replace the database snapshot | Private storage or version control appropriate to content |
| Application recovery | Native logical database dumps plus pushed Git repositories and durable uploads | Usually yes | Transaction-consistent application data and source | Private storage; host snapshot alone is not the logical backup |

## Procedure

1. Resolve the active Hermes profile and the exact paths in use. Never assume the default profile owns every bot or memory store.
2. Choose the artifact from the table. Do not call a credential-free profile export a full backup.
3. Write the test or retained archive to a private path outside any source repository. Ensure it is owner-readable only when it contains credentials.
4. Measure the resulting file with `stat` or the file tool. Report both decimal MB/GB and binary MiB/GiB when useful.
5. If the archive was created only to measure size, remove that exact temporary file immediately after recording the size.
6. For chat delivery, verify the platform's current attachment limit and compare it with the measured archive. Do not split or transmit a secret-bearing full backup merely to fit the transport.
7. State exclusions explicitly. Common external surfaces are GBrain, Obsidian, application databases, Git work not pushed, generated outputs, and project uploads.
8. Verify restoration periodically in an isolated environment. Archive creation without a tested restore is incomplete disaster recovery.

## Portable scheduled-export recipe

1. Run `hermes profile export <profile> -o <private-temporary-archive>` every cycle. Treat this as the source snapshot, not as proof that the result matches the requested transport scope.
2. Open the source archive and inspect member names before repackaging. Whitelist the requested classes—normally `config.yaml`, `SOUL.md`, `memories/`, `skills/`, `scripts/`, and only `cron/jobs.json`—instead of trying to maintain an ever-growing blacklist.
3. Exclude `.env`, auth and credential files, `state.db`, session/request dumps, cron execution databases and output, caches, `.git`, knowledge or project repositories, GBrain, Obsidian vault data, and any other external datastore unless explicitly requested.
4. Materialize linked skill files into the new archive so it is portable. Follow only topical skill directories such as `references/`, `scripts/`, and `templates/`; omit linked build/dependency trees such as `node_modules`, `dist`, and compiled browser bundles because dereferencing them can inflate a small profile export beyond messaging limits.
5. Scan profile-owned text for high-confidence credential signatures and reject credential-bearing filenames everywhere. Do not flag skill documentation merely for containing example key shapes; bundled skills often include redaction fixtures and setup examples.
6. Write a candidate archive in a temporary directory. Reopen it, read every regular member to force decompression, reject forbidden paths, and assert required persona, settings, memories, skills, scripts, and cron-definition members are present.
7. Calculate SHA-256 from the verified candidate, atomically move it to a date-stamped final name, then reopen and hash the final path. A mismatch fails the cycle.
8. Only after final verification succeeds, sort the exports and remove entries beyond the retention count. Leave every prior successful backup untouched on export, scan, integrity, or publication failure.
9. For a deterministic scheduled Telegram delivery, use a `no_agent` cron script that prints the size, SHA-256, verification result, retention result, and `MEDIA:/absolute/path/to/archive`. Empty output sends nothing; a non-zero exit surfaces a failure notice.
10. Express the requested local schedule in the scheduler's timezone explicitly. When the host scheduler uses UTC, convert the requested offset before writing the cron expression and verify `next_run_at` after creation.

## Pitfalls

- Measure the generated archive, not `du` output — compressed media and databases make ratios unreliable.
- Keep OAuth reauthentication in the restore plan — copied refresh state can expire or be invalidated even when the files restore correctly.
- Preserve active databases through their native snapshot/dump path — crash-consistent host images and file copies can capture live write state.
- Keep at least one backup outside the VPS — a backup beside the original does not survive total disk or host loss.
- Name retained exports with the backup date in the user's requested timezone; the host date can differ around midnight.
- If the archive must include its own newly created cron definition, create and verify the job before producing the final test archive; an earlier snapshot cannot contain a later schedule.

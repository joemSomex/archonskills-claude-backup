# Shared application and Supabase Vault secrets

Use this recipe when one random value must be present both in an application runtime and in Supabase Vault, for example to authenticate an internal synchronization request.

## Preconditions

1. Search the application and migrations for both names before provisioning:
   - the server environment variable, conventionally uppercase;
   - the Vault secret name, conventionally lowercase.
2. Confirm which component signs/sends the value and which component verifies it.
3. Treat a missing code reference as a blocker to claiming the integration works. Storing an unused secret is safe preparation only.
4. Never request, accept, or repeat the plaintext in chat. Never put it in a repository, screenshot, issue, PR, application log, build argument, or `NEXT_PUBLIC_*` variable.

## Generate a 48-character secret on Windows PowerShell

Use the instance RNG API for broad Windows PowerShell/.NET compatibility. Thirty-six random bytes encode to exactly 48 Base64 characters with no padding.

```powershell
$bytes = New-Object byte[] 36
$rng = [System.Security.Cryptography.RandomNumberGenerator]::Create()
$rng.GetBytes($bytes)
$secret = [Convert]::ToBase64String($bytes)
if ($secret.Length -ne 48) { throw "Unexpected secret length" }
$secret | Set-Clipboard
$rng.Dispose()
[Array]::Clear($bytes, 0, $bytes.Length)
Remove-Variable bytes, rng
```

Do not print `$secret`. A length-only check is safe. Keep the shell variable and clipboard only until both destinations are updated.

## Store the application copy

- Use the exact environment-variable name the server reads.
- Mark it masked/secret and runtime-only.
- Do not make it a public or build-time variable unless the code contract explicitly requires that; shared authentication secrets normally never enter browser bundles.
- Save the value but coordinate restart/redeploy with the Vault update so the two sides do not remain mismatched.
- On ECS, store the value in Secrets Manager or SSM Parameter Store and reference its ARN from the task definition; do not paste it into task-definition JSON.

## Store the Vault copy

Prefer the Supabase Vault UI when available, because a SQL literal can remain in local editor history. When SQL is required, use a private editor session and never save or share the query text.

Create one uniquely named secret:

```sql
select vault.create_secret(
  'PASTE_FROM_PRIVATE_CLIPBOARD',
  'shared_secret_name',
  'Purpose and owning integration'
);
```

The result is the secret UUID. Verify only metadata:

```sql
select id, name, description, created_at, updated_at
from vault.secrets
where name = 'shared_secret_name';
```

Require exactly one row. Do not query or screenshot `vault.decrypted_secrets`; it exposes plaintext to anyone who can read the result.

If the name already exists, do not create a duplicate. Read its UUID from `vault.secrets`, then update it:

```sql
select vault.update_secret(
  'EXISTING_SECRET_UUID',
  'PASTE_NEW_VALUE_FROM_PRIVATE_CLIPBOARD',
  'shared_secret_name',
  'Purpose and owning integration'
);
```

## Rotation order

- If the protocol supports current and next secrets, deploy dual-read verification first, add the next secret to both destinations, switch writers, verify, then retire the old secret.
- If only one value is supported, schedule a brief maintenance window and update both destinations back-to-back. Do not claim zero downtime because one side becomes active before the other.
- Restart/redeploy only after both stores have the intended value.

## Verify the integration

1. Confirm the application dashboard shows the variable name as present and masked.
2. Confirm `vault.secrets` returns exactly one metadata row with the expected name.
3. Run one focused request through the real synchronization path and require an authenticated success.
4. Confirm a deliberately wrong value fails closed without leaking either value.
5. Inspect logs for status and correlation IDs only; the secret must never appear.

## Cleanup

After both destinations and the integration are verified:

```powershell
Set-Clipboard -Value ""
Remove-Variable secret -ErrorAction SilentlyContinue
```

If a value was ever printed, screenshotted, pasted into chat, or committed, treat it as compromised and rotate both destinations. Changing only one copy breaks synchronization.
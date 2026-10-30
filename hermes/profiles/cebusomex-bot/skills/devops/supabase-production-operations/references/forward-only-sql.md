# Forward-only SQL patterns

## Decision table

- **Historical migration never applied:** apply the original migration only after verifying every prerequisite and its place in the dependency chain.
- **Historical migration already applied, definition changed later:** create a new forward-only patch; do not rerun the historical file.
- **Duplicate column/table/function error:** inspect the live object. If the script is wrapped in `BEGIN`, the failed transaction normally applied none of that attempt; still read back before proceeding.
- **View-only behavior change:** prefer `CREATE OR REPLACE VIEW` when the output column names, order, and types remain compatible.
- **Function behavior change:** use `CREATE OR REPLACE FUNCTION` with the complete intended body, preserving language, volatility, `SECURITY DEFINER`, and `search_path`.
- **Missing additive object:** use a new migration. Add `IF NOT EXISTS` only when accepting any pre-existing object with that name is semantically safe.

## Patch skeleton

```sql
begin;

-- Replace only the object whose behavior changed.
create or replace view private.example_view as
select ...;

-- Reassert the intended boundary when relevant.
revoke all on private.example_view from public, anon, authenticated;

commit;
```

Do not make a patch "idempotent" by swallowing every exception. A prerequisite mismatch should fail visibly rather than leave a partially compatible production schema.

## Local verification

1. Build the smallest fixture containing the real column types and dependent functions.
2. Apply the patch once and assert the changed behavior.
3. Apply it a second time and rerun the assertions.
4. Include a negative assertion proving hidden or forbidden data cannot leak.
5. Run the repository's focused database verifier; disclose unrelated failures that prevent the full verifier from reaching the new assertions.

## Production read-back

After execution, verify both structure and behavior:

```sql
select pg_get_viewdef('private.example_view'::regclass, true);
```

Confirm grants separately when the object is an authorization boundary:

```sql
select
  has_table_privilege('anon', 'private.example_view', 'SELECT') as anon_can_select,
  has_table_privilege('authenticated', 'private.example_view', 'SELECT') as authenticated_can_select;
```

Do not treat `list_tables` as authoritative for private views; inspect them with `to_regclass(...)` and `pg_get_viewdef(...)`.

## Rollback-only behavior probe

When no safe existing row exercises the changed behavior, use one explicit transaction that creates or modifies a uniquely marked fixture, reads the affected projection, and ends with `ROLLBACK`. Uncommitted changes remain invisible to other sessions while still exercising the hosted schema.

```sql
begin;
create temporary table probe(id uuid primary key) on commit drop;
-- Insert or update only the minimum fixture needed.
select ...; -- assert the user-visible behavior
rollback;
```

After the transaction, run a separate read-only query for the unique marker and require a zero count. This second read proves cleanup instead of merely trusting the presence of `ROLLBACK` in the submitted SQL. Never use a rollback probe for non-transactional side effects or external calls.

## Hermes MCP connection sequence

1. Install: `hermes mcp install supabase`.
2. Authenticate interactively: `hermes mcp login supabase`; keep OAuth redirects and codes in that terminal, never chat.
3. Verify: `hermes mcp test supabase` must connect and discover tools.
4. If the MCP was installed after the current conversation started, use a new Hermes session before invoking it; tool catalogs are session-stable.
5. List projects first, then identify the target by expected schema objects before applying SQL.

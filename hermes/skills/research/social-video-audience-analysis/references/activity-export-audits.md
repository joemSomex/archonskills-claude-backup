# Activity export audits

Use this workflow for date-filtered creator comment/reply counts from Google My Activity or similar account exports.

## Procedure

1. Define the date range, timezone, exact included video IDs/titles, whether replies and top-level comments both count, and which destinations are excluded.
2. Extract records using semantic activity markers such as `Replied to a comment on` and `Commented on`. Never split solely on presentation headings such as `### YouTube`: document extraction can render identical cards as headings, bold text, or plain text, silently merging records.
3. Normalize every record into `{date, activity_type, destination_title, text}`. Preserve destination titles exactly and filter through an explicit allowlist; do not use fuzzy episode-name matching.
4. Count all records in the requested date sections before filtering. Then compute included and excluded totals by destination class. This separates an all-channel activity count from an episode-only count.
5. Verify all invariants programmatically:
   - `raw_total = included_total + excluded_total`;
   - daily subtotals sum to the filtered total;
   - per-video subtotals sum to the filtered total;
   - top-level comments plus replies sum to the filtered total.
6. Cross-check with a second record boundary or source when available. Public relative labels such as “5 days ago” are not reliable for exact daily allocation.
7. If another count differs, compare scope first. Community posts, compilations, trailers, Shorts, music videos, and alternate uploads commonly explain large discrepancies.
8. Do not invent a missing `Today` section or reassign a record across dates from its clock time alone. If an external result claims an extra row absent from the export, request or identify that row before incorporating it.

## Reporting

Report the filtered total, comment/reply split, daily counts, per-video counts, timezone, export cutoff, and a one-line scope statement. When correcting a prior result, name the parsing mechanism that caused the error and show the reconciliation instead of presenting only a replacement number.

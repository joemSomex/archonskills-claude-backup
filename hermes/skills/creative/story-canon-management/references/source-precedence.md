# Source Precedence and Versioning

Use this table after preserving every source intact.

| Situation | Archive action | Canon action |
|---|---|---|
| New chapter or installment | Add a new sequence-specific source | Append to chronology; do not alter earlier installments |
| Revised text without explicit replacement language | Add a new versioned source beside the earlier draft | Mark both versions and ask which governs only when a task requires a single choice |
| Explicit replacement of an earlier draft | Preserve both; mark the older source superseded with a pointer | Use the named replacement for future canon work |
| Produced episode plus written source | Preserve both with medium/type labels and a timestamped comparison ledger | Treat both as parallel canonical adaptation records; cross-reference rather than inventing precedence |
| Episode contains material absent from written source | Preserve the episode timestamp and written-source absence | Record an episode-only version without deleting or downgrading the written record |
| Episode directly differs from written source | Preserve the timestamp, exact SRT dialogue, and exact written passage | Record both versions side by side; only an explicit author ruling resolves the difference |
| Episode does not depict a written detail | Preserve the written passage and mark the episode entry `not depicted` | Keep the written detail in its source record; omission is not deletion or lower canon status |
| World bible versus narrative scene | Preserve both and cite exact sections/passages | Apply the project’s declared primary-canon rule; distinguish general rules from deliberately exceptional story events |
| Direct contradiction with no declared precedence | Preserve both and record the conflict | Mark unresolved; ask the author before relying on either claim |
| Filename/version label disagrees with internal heading | Preserve both labels exactly | Keep discrepancy unresolved until the author clarifies |

## Canon Extraction Boundaries

- **Direct canon:** explicitly depicted or stated facts.
- **Continuity implication:** necessary ordering or state carried between direct events; label it as implication.
- **Interpretation:** thematic or aesthetic reading; never store as canon without confirmation.
- **Restricted knowledge:** true in the world but unavailable to named characters or the public.
- **Generated proposal:** assistant-created material; keep outside canon until explicitly approved.

## Verification Checklist

- Earlier source still exists.
- New source has provenance and a body-only SHA-256.
- Exact-body comparison passes.
- Index names every active and superseded version.
- Chronology points to the intended version.
- Adaptation comparisons distinguish `episode-version`, `written-version`, `aligned`, `difference`, and `uncertain/not depicted`, without implying automatic precedence.
- Every adaptation claim cites a timestamp or exact source segment; metadata-only retrieval is labeled incomplete.
- Contradictions and restricted-knowledge boundaries are visible.
- Durable recall returns a compact pointer, not the full manuscript.

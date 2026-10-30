# PDF structured extraction

Use this recipe when a PDF contains dense tables whose fields must remain exact.

## Native-text coverage

Inspect metadata and page coverage first. A usable text layer on every page means OCR is unnecessary; do not OCR clean native text because OCR can alter punctuation, symbols, and numbers. Record page-level character/word counts and image counts, then flag only empty or suspicious pages for raster review/OCR.

## Per-page source extraction

Extract each page separately and store it under an explicit `PDF page N` heading. Preserve visible text and page boundaries. This page-labeled extraction is the provenance layer; curated wiki pages may normalize whitespace but must cite the original page.

## Tables

Use `pdfplumber` table extraction (or the existing PDF helper's `--tables` mode) and retain the extractor's page number with every row. For each row:

1. Require the expected column count and validate its stable identifier format.
2. Collapse internal layout newlines/spaces only: `" ".join(cell.split())`.
3. Preserve punctuation, Unicode stars/dashes, capitalization, costs, stats, copy limits, and effect wording exactly.
4. Reject malformed rows for review instead of guessing missing cells.

For a card/catalog compendium, generate focused pages from the structured rows and include the page number in each record.

## Independent verification

Do not validate with the same rendering loop alone. Parse the generated Markdown back into structured fields and compare it to the extracted table JSON:

- expected total and unique IDs
- per-category totals
- every field value
- every page citation
- zero extras, omissions, duplicates, or mismatches

Split oversized pages only after exact extraction, then rerun the comparison across all split pages so records cannot be lost or duplicated during restructuring.

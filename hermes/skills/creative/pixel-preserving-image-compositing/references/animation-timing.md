# Lossless GIF timing revisions

Use when only frame delays change and decoded artwork must remain identical.

## Procedure

1. Open the exact user-supplied GIF with Pillow. Record its frame count, dimensions, per-frame durations, loop flag, and decoded RGBA arrays before writing. Do not substitute an earlier PNG set: the supplied GIF may have a different palette or frame selection.
2. Choose new durations in multiples of 10 milliseconds, GIF's stored timing unit. Use shorter transition frames and longer holds at readable opening/peak poses. If the user requires an unchanged loop length while adding drawn poses, allocate delays against the measured source total and verify their sum before assembly.
3. Prefer editing only Graphics Control Extension delay fields for an existing GIF. Walk the GIF block structure; do not search-and-replace arbitrary byte patterns, since compressed image data can contain the same bytes.
4. Write a new file. Reopen source and result and require equal frame counts, dimensions, loop behavior, and pixel-identical decoded RGBA arrays for every frame. Verify every requested duration and compute the loop total from the reopened result.
5. Deliver the revised GIF and a concise timing summary. Do not describe a timing-only change as a redraw or a smoothing pass.

## GIF block traversal

- Read the six-byte signature and seven-byte Logical Screen Descriptor. Start at byte 13; if the global color-table flag is set in descriptor byte 10, skip `3 * 2 ** ((packed & 7) + 1)` bytes.
- For extension introducer `0x21`, read its label. A Graphics Control Extension has label `0xF9`, a four-byte payload, and a zero terminator. With the cursor at the payload-size byte, the little-endian two-byte delay occupies offsets `+2:+4`. Replace only those bytes with `duration_ms // 10`; leave flags, transparent index, and disposal unchanged. Skip all extension payloads using their length-prefixed sub-blocks through the zero terminator.
- For image separator `0x2C`, read the nine-byte Image Descriptor. If its packed byte has a local color-table flag, skip the local table using the same size formula. Skip the LZW minimum code-size byte, then skip length-prefixed image-data sub-blocks through their zero terminator.
- Stop at trailer `0x3B`. Reject unexpected block markers, truncated data, durations outside the two-byte range, or a mismatch between control extensions and the expected frames rather than silently corrupting the file.

This preserves the original compressed image payloads and palette byte-for-byte while changing timing. Verification of decoded frames remains mandatory because correct file writing alone does not establish playback preservation.

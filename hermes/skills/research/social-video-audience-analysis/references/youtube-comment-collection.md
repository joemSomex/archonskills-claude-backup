# YouTube comment collection

## Primary route

Try the inexpensive extractor first:

```bash
uvx --from yt-dlp yt-dlp --skip-download --write-comments --write-info-json \
  --extractor-args 'youtube:comment_sort=new' -o 'episode.%(ext)s' URL
```

If playback or `yt-dlp` is bot-blocked, inspect the public comments in a browser. YouTube can expose comments even when the player requires sign-in.

## DOM route

1. Scroll below the description and switch comments to **Newest** when completeness matters.
2. Load top-level continuations under `ytd-comments`, excluding those nested in `ytd-comment-replies-renderer`.
3. Expand visible `#more-replies-sub-thread button` controls. Scroll every top-level thread into view because replies are lazy-loaded. Click visible reply continuations such as “Show more replies.”
4. Extract each `ytd-comment-view-model`:
   - author: `#author-text`
   - text: `#content-text`
   - relative time and permalink: `#published-time-text` / its anchor
   - likes: `#vote-count-middle`
   - reply status: ancestry under `ytd-comment-replies-renderer`
5. Clone comment text and replace inline emoji images with their `alt` text before reading `textContent`, or emoji-only comments appear blank.
6. Deduplicate by the `lc` permalink/comment ID. Expanded replies can create nested or duplicate thread renderers, so DOM thread counts are not reliable totals.
7. Confirm that no top-level or reply continuations remain, and compare unique IDs with YouTube’s displayed count.

## Direct Innertube fallback

When DOM lazy loading stalls or is expensive, use the watch page’s public endpoint from page JavaScript:

- API key: `ytcfg.get('INNERTUBE_API_KEY')`
- context: `ytcfg.get('INNERTUBE_CONTEXT')`
- endpoint: `/youtubei/v1/next?key=...`
- initial comment continuation: dynamically find `continuationItemRenderer.continuationEndpoint` within `ytInitialData.contents.twoColumnWatchNextResults.results.results.contents`; do not hard-code an array index because live-chat panels shift it.
- POST `{context, continuation: token}`.
- Parse `frameworkUpdates.entityBatchUpdate.mutations[].payload.commentEntityPayload` for:
  - `author.displayName`
  - `properties.commentId`
  - `properties.publishedTime`
  - `properties.replyLevel`
  - `properties.content.content`

Breadth-first traverse subsequent `continuationCommand.token` values for top-level pages and replies. Exclude tokens under `sortFilterSubMenuRenderer`, which represent alternate sorts and duplicate work. Deduplicate by `commentId` and cap traversal defensively.

Long async page JavaScript can exceed the browser evaluator’s short timeout. Start the collector without awaiting it, store progress/result on `window`, then read the stored result in a later browser call. Compare API totals with the displayed or DOM total because hidden/deleted comments can remain inaccessible.

## Date-bounded counting

YouTube commonly exposes relative labels (`3 days ago`) rather than exact public timestamps.

- Check the current UTC date before mapping labels.
- Map `N days ago` only as an approximation; posts near midnight can shift by one calendar day depending on posting hour and viewer timezone.
- Never assign `1 week ago` to one exact date; it spans a range.
- Split owner output into top-level posts and replies using `replyLevel` or DOM ancestry.
- Aggregate totals in code and verify that daily totals equal episode totals and the final grand total.

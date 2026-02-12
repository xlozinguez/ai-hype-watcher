# YouTube Transcriber — Reference Material

## Playwright Selectors

### Transcript Extraction
The primary selectors for YouTube's transcript panel:

| Selector | Purpose | Notes |
|----------|---------|-------|
| `ytd-transcript-segment-renderer` | Individual transcript segment container | Contains timestamp + text |
| `.segment-timestamp` | Timestamp within a segment | Format: `M:SS` or `H:MM:SS` |
| `.segment-text` | Text content within a segment | May contain auto-caption artifacts |

### Page Navigation
| Element | How to Find | Notes |
|---------|------------|-------|
| Description expand | Look for "...more" button in snapshot | Located below video title |
| Transcript button | "Show transcript" text after expanding description | May not exist if no captions |
| Transcript loaded | "Search in video" text appears | Indicates transcript panel is ready |
| Consent dialog | Cookie banner at page load | Click "Accept all" or "Reject all" |

### Alternative Selectors (Fallbacks)
YouTube's frontend changes periodically. If primary selectors fail, try:
- `ytd-transcript-segment-list-renderer` — parent container for all segments
- `[class*="segment-timestamp"]` — partial class match
- `[class*="segment-text"]` — partial class match
- Direct text extraction: `document.querySelector('#segments-container')?.textContent`

## Known Failure Modes

### No Transcript Available
- **Symptom**: "Show transcript" button doesn't appear after expanding description
- **Cause**: Video has no captions (auto-generated or manual)
- **Workaround**: Use yt-dlp or manual transcript services

### Consent/Cookie Dialog
- **Symptom**: Page loads but main content is hidden behind a consent dialog
- **Cause**: YouTube's GDPR/privacy consent requirement (especially for non-logged-in users)
- **Fix**: Check snapshot for consent dialog after navigation, click "Accept all" before proceeding

### Age-Restricted Content
- **Symptom**: Page loads but requires sign-in
- **Cause**: Video is age-restricted
- **Workaround**: Not supported via automated extraction — use manual methods

### Transcript Panel Doesn't Load
- **Symptom**: "Show transcript" button exists but clicking it doesn't populate segments
- **Cause**: YouTube's lazy loading or network issues
- **Fix**: Add a `browser_wait_for` with a timeout, retry once, then fall back to manual

### Empty Segments Array
- **Symptom**: `browser_evaluate` returns `{ segments: [], count: 0 }`
- **Cause**: Selectors changed or transcript panel didn't fully render
- **Fix**: Take a screenshot, try alternative selectors, report failure

## noembed API

The noembed API (`https://noembed.com/embed?url=<youtube-url>`) is a free, unauthenticated oEmbed proxy. It returns:
- `title` — video title
- `author_name` — channel display name
- `author_url` — channel URL
- `thumbnail_url` — video thumbnail
- `provider_name` — "YouTube"

It does NOT return: publication date, duration, view count, description. Use WebSearch for these.

## _drafts Directory

Raw transcripts are stored in `sources/_drafts/` to keep the `sources/` directory clean. This directory:
- Is for working files only
- Can be cleaned up after synthesis is complete
- Should not be referenced in the sources index
- Files use the pattern: `NNN-raw-transcript.md` (matching the source ID)

## Content Pipeline

The full pipeline from video to indexed source:

```
1. /scan-channels          → discover new relevant videos
2. /youtube-transcriber    → extract transcript via Playwright + metadata
3. /synthesize-source      → synthesize into structured source note
4. /compile-curriculum     → integrate into curriculum modules
```

Or use `/ingest <url>` to run steps 2-3 automatically.

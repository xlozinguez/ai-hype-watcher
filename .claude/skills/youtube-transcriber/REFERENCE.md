# YouTube Transcriber — Reference Material

## Transcript Quality

### Auto-generated transcripts
YouTube's auto-generated transcripts are typically 90-95% accurate but commonly have issues with:
- Technical terms (e.g., "Claude" → "clod", "Anthropic" → "anthropic")
- Proper nouns and names
- Acronyms (e.g., "LLM" → "elm", "API" → "a p i")
- Sentence boundaries and punctuation (auto-transcripts have none)

The synthesis step should interpret meaning rather than relying on exact transcript wording. Don't quote auto-transcript text directly — paraphrase and verify key claims.

### Manual/corrected transcripts
If the video has community-contributed captions, these are significantly more accurate. Check for "(English)" vs "(English - auto-generated)" in YouTube's transcript panel.

## noembed API

The noembed API (`https://noembed.com/embed?url=<youtube-url>`) is a free, unauthenticated oEmbed proxy. It returns:
- `title` — video title
- `author_name` — channel display name
- `author_url` — channel URL (useful for verifying the channel)
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
2. /youtube-transcriber    → capture transcript + metadata
3. /synthesize-source      → synthesize into structured source note
4. /compile-curriculum     → integrate into curriculum modules
```

Each step is independent — you can enter the pipeline at any point. For example, you can skip `/scan-channels` if you already have a URL, or skip `/youtube-transcriber` if you already have a transcript.

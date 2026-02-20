# Playlist — Reference Material

## VTT-to-Transcript Conversion Script

Use this Python one-liner to convert VTT subtitle files to clean timestamped transcripts:

```python
import re, sys

content = sys.stdin.read()
# Strip VTT header
content = re.sub(r'^WEBVTT\n.*?\n\n', '', content, flags=re.DOTALL)
# Parse cue blocks
lines = []
seen = set()
for block in re.split(r'\n\n+', content):
    block = block.strip()
    if not block:
        continue
    # Extract timestamp from first line (format: HH:MM:SS.mmm --> HH:MM:SS.mmm)
    ts_match = re.match(r'(\d{2}):(\d{2}):(\d{2})\.\d{3}\s*-->', block)
    if not ts_match:
        continue
    h, m, s = int(ts_match.group(1)), int(ts_match.group(2)), int(ts_match.group(3))
    timestamp = f"[{h*60+m:02d}:{s:02d}]"
    # Get text lines (skip timestamp line and any position/alignment lines)
    text_lines = []
    for line in block.split('\n')[1:]:
        line = line.strip()
        if not line or re.match(r'^(position|align|line|size):', line):
            continue
        # Strip VTT tags like <c> </c> <00:00:00.000>
        line = re.sub(r'<[^>]+>', '', line)
        line = line.strip()
        if line and line not in seen:
            text_lines.append(line)
            seen.add(line)
    if text_lines:
        text = ' '.join(text_lines)
        lines.append(f"{timestamp} {text}")

print('\n'.join(lines))
```

### Usage

```bash
python3 -c "
import re, sys
content = sys.stdin.read()
content = re.sub(r'^WEBVTT\n.*?\n\n', '', content, flags=re.DOTALL)
lines = []
seen = set()
for block in re.split(r'\n\n+', content):
    block = block.strip()
    if not block: continue
    ts_match = re.match(r'(\d{2}):(\d{2}):(\d{2})\.\d{3}\s*-->', block)
    if not ts_match: continue
    h, m, s = int(ts_match.group(1)), int(ts_match.group(2)), int(ts_match.group(3))
    timestamp = f'[{h*60+m:02d}:{s:02d}]'
    text_lines = []
    for line in block.split('\n')[1:]:
        line = line.strip()
        if not line or re.match(r'^(position|align|line|size):', line): continue
        line = re.sub(r'<[^>]+>', '', line).strip()
        if line and line not in seen:
            text_lines.append(line)
            seen.add(line)
    if text_lines:
        lines.append(f'{timestamp} {\" \".join(text_lines)}')
print('\n'.join(lines))
" < sources/_drafts/NNN-vtt.en.vtt > sources/_drafts/NNN-raw-transcript.md
```

## Team Structure Template

For N videos, divide into batches of 4-5:

```
batch_count = ceil(N / 5)  # minimum 2 agents, maximum 5
```

| Videos | Agents | Distribution |
|--------|--------|--------------|
| 1-5    | 1      | All to single agent (no team needed, use /ingest) |
| 6-10   | 2      | 5 + remainder |
| 11-15  | 3      | 5 + 5 + remainder |
| 16-20  | 4      | 5 + 5 + 5 + remainder |
| 21-25  | 5      | 5 + 5 + 5 + 5 + remainder |

## yt-dlp Playlist Commands

### Extract video URLs and titles
```bash
yt-dlp --flat-playlist --print url --print title "PLAYLIST_URL"
```

### Batch download subtitles
```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download \
  -o "sources/_drafts/playlist-%(playlist_index)03d" \
  "PLAYLIST_URL"
```

### Get metadata for all videos
```bash
yt-dlp --flat-playlist --print "%(url)s|%(title)s|%(duration)s|%(upload_date)s" "PLAYLIST_URL"
```

### With rate limiting protection
```bash
yt-dlp --write-auto-sub --sub-lang en --skip-download \
  --sleep-interval 2 --max-sleep-interval 5 \
  -o "sources/_drafts/playlist-%(playlist_index)03d" \
  "PLAYLIST_URL"
```

## Post-Ingest Checklist

After all source files are synthesized:

- [ ] `sources/README.md` — all new entries added to index table
- [ ] `synthesis/YYYY-MM-DD-*.md` — cross-source synthesis if 4+ sources share a theme
- [ ] `briefings/YYYY-MM-DD.md` — daily briefing covering the batch
- [ ] `briefings/README.md` — briefing index updated
- [ ] `curriculum/` — all 6 modules recompiled with new source content
- [ ] `curriculum/README.md` — module summaries and source counts current

## Error Handling

### No Captions Available

Some videos (courses, live streams, non-English content) may lack auto-generated English subtitles.

**Fallback sequence:**
1. Try `--sub-lang en` (English auto-subs)
2. Try `--sub-lang en --write-sub` (manual English subs)
3. Try Playwright transcript extraction (navigate to video, open transcript panel)
4. Report failure — offer to skip or use alternative URL

### Partial Playlist Failures

When some videos in a playlist fail:
- Continue processing successful videos
- Keep source IDs sequential (don't leave gaps)
- Report failures at the end with video titles and URLs
- Offer to retry failed videos individually via `/ingest`

### yt-dlp Rate Limiting

YouTube may throttle requests for large playlists:
- Add `--sleep-interval 2 --max-sleep-interval 5`
- If blocked, wait 30 seconds and retry
- For very large playlists (50+), split into sub-ranges with `--playlist-items`

## Relationship to Other Skills

| Skill | Relationship |
|-------|-------------|
| `/ingest` | Playlist uses the same synthesis pipeline as Ingest Mode D, but automates URL extraction and team orchestration |
| `/synthesize-source` | Each synthesis agent follows the synthesize-source workflow internally |
| `/compile-curriculum` | Playlist runs curriculum recompilation as the final phase |
| `/daily-briefing` | Playlist generates a briefing as part of the post-ingest pipeline |
| `/youtube-transcriber` | Playlist uses yt-dlp instead (faster for batch), falls back to Playwright |

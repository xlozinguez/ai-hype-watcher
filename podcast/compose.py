#!/usr/bin/env python3
"""
Podcast Audio Composition Pipeline

Parses a podcast script, renders each speaker segment via ElevenLabs TTS,
and composes the final episode using ffmpeg.

Usage:
    python3 podcast/compose.py podcast/scripts/EP001-2026-04-03.md
    python3 podcast/compose.py podcast/scripts/EP001-2026-04-03.md --dry-run  # count chars only
"""

import os
import re
import sys
import json
import time
import subprocess
import tempfile
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency: pip install PyYAML")

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv is optional — user can export ELEVENLABS_API_KEY directly


# ---------------------------------------------------------------------------
# Script Parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter from script."""
    match = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not match:
        return {}
    return yaml.safe_load(match.group(1)) or {}


def parse_script(text: str) -> list[dict]:
    """
    Parse a podcast script into ordered segments.

    Returns list of dicts with keys:
        speaker: 'A' | 'B' | None (for markers)
        text: str
        segment_type: 'dialogue' | 'cold_open' | 'intro' | 'outro' | 'segment' | 'rapid_fire'
    """
    # Strip frontmatter
    text = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)

    segments = []
    current_section = 'dialogue'

    for line in text.split('\n'):
        line = line.strip()
        if not line or line.startswith('<!--'):
            continue

        # Section markers
        marker_map = {
            '[COLD OPEN]': 'cold_open',
            '[INTRO]': 'intro',
            '[OUTRO]': 'outro',
            '[RAPID FIRE]': 'rapid_fire',
        }

        if line in marker_map:
            current_section = marker_map[line]
            continue

        if line.startswith('[SEGMENT:'):
            current_section = 'segment'
            continue

        # Speaker lines
        match = re.match(r'^\[([AB])\]\s*(.*)', line)
        if match:
            speaker = match.group(1)
            dialogue = match.group(2).strip()
            if dialogue:
                segments.append({
                    'speaker': speaker,
                    'text': dialogue,
                    'segment_type': current_section,
                })

    return segments


# ---------------------------------------------------------------------------
# TTS Rendering
# ---------------------------------------------------------------------------

def render_elevenlabs(segments: list[dict], config: dict, output_dir: Path) -> list[Path]:
    """Render each segment via ElevenLabs TTS API. Returns list of audio file paths."""
    import urllib.request
    import urllib.error

    api_key = os.environ.get('ELEVENLABS_API_KEY')
    if not api_key:
        sys.exit("ELEVENLABS_API_KEY not found in environment. Set it in .env or export it.")

    hosts = config.get('hosts', {})
    tts_config = config.get('tts', {})
    model_id = tts_config.get('model', 'eleven_multilingual_v2')
    output_format = tts_config.get('output_format', 'mp3_44100_128')

    voice_map = {
        'A': hosts.get('a', {}).get('voice_id', 'nPczCjzI2devNBz1zQrb'),
        'B': hosts.get('b', {}).get('voice_id', '9BWtsMINqrJLrRacOk9x'),
    }

    audio_files = []
    total = len(segments)

    for i, seg in enumerate(segments):
        speaker = seg['speaker']
        voice_id = voice_map[speaker]
        out_file = output_dir / f"host-{speaker.lower()}-{i:03d}.mp3"

        print(f"  [{i+1}/{total}] Rendering {speaker}: {seg['text'][:60]}...")

        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}?output_format={output_format}"
        payload = json.dumps({
            "text": seg['text'],
            "model_id": model_id,
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75,
                "style": 0.3,
                "use_speaker_boost": True,
            }
        }).encode('utf-8')

        req = urllib.request.Request(url, data=payload, headers={
            "xi-api-key": api_key,
            "Content-Type": "application/json",
        })

        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                out_file.write_bytes(resp.read())
                audio_files.append(out_file)
        except urllib.error.HTTPError as e:
            body = e.read().decode('utf-8', errors='replace')[:200]
            print(f"  WARNING: TTS failed for segment {i} (HTTP {e.code}): {body}")
            continue

        # Rate limiting
        if i < total - 1:
            time.sleep(0.5)

    return audio_files


# ---------------------------------------------------------------------------
# Audio Composition
# ---------------------------------------------------------------------------

def generate_silence(duration_ms: int, output_path: Path):
    """Generate a silent audio file of given duration."""
    subprocess.run([
        'ffmpeg', '-y', '-f', 'lavfi', '-i',
        f'anullsrc=r=44100:cl=mono',
        '-t', str(duration_ms / 1000),
        '-ar', '44100', '-ac', '1',
        str(output_path)
    ], capture_output=True, check=True)


def compose_audio(audio_files: list[Path], segments: list[dict], config: dict, output_dir: Path) -> Path:
    """Concatenate audio segments with silence gaps using ffmpeg."""
    audio_config = config.get('audio', {})
    turn_silence_ms = audio_config.get('silence_between_turns_ms', 400)
    segment_silence_ms = audio_config.get('silence_at_segment_ms', 800)
    target_lufs = audio_config.get('target_lufs', -16)

    # Build concat file list with silence gaps
    concat_list = output_dir / 'concat.txt'
    silence_short = output_dir / 'silence_short.mp3'
    silence_long = output_dir / 'silence_long.mp3'

    generate_silence(turn_silence_ms, silence_short)
    generate_silence(segment_silence_ms, silence_long)

    with open(concat_list, 'w') as f:
        for i, audio_file in enumerate(audio_files):
            f.write(f"file '{audio_file.resolve()}'\n")
            if i < len(audio_files) - 1:
                # Use longer silence at segment transitions
                is_segment_break = (
                    i < len(segments) - 1 and
                    segments[i].get('segment_type') != segments[i + 1].get('segment_type')
                )
                silence = silence_long if is_segment_break else silence_short
                f.write(f"file '{silence.resolve()}'\n")

    # Concatenate
    raw_output = output_dir / 'raw.mp3'
    subprocess.run([
        'ffmpeg', '-y', '-f', 'concat', '-safe', '0',
        '-i', str(concat_list),
        '-c', 'copy',
        str(raw_output)
    ], capture_output=True, check=True)

    # Normalize loudness
    final_output = output_dir / 'mixed.mp3'
    subprocess.run([
        'ffmpeg', '-y', '-i', str(raw_output),
        '-af', f'loudnorm=I={target_lufs}:TP=-1.5:LRA=11',
        '-ar', '44100', '-ac', '1',
        str(final_output)
    ], capture_output=True, check=True)

    # Clean up intermediates
    for f in [raw_output, concat_list, silence_short, silence_long]:
        f.unlink(missing_ok=True)

    return final_output


# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------

def get_duration(audio_path: Path) -> str:
    """Get audio duration as HH:MM:SS."""
    result = subprocess.run([
        'ffprobe', '-v', 'error', '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        str(audio_path)
    ], capture_output=True, text=True, check=True)
    seconds = float(result.stdout.strip())
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def write_episode_yaml(frontmatter: dict, audio_path: Path | None, config: dict, output_dir: Path):
    """Write episode metadata YAML."""
    episode_num = frontmatter.get('episode', 'EP001')
    episodes_dir = Path('podcast/episodes')
    episodes_dir.mkdir(parents=True, exist_ok=True)

    episode_data = {
        'episode': episode_num,
        'title': frontmatter.get('title', 'Untitled'),
        'date': frontmatter.get('date', ''),
        'sources': frontmatter.get('sources', []),
        'briefing': frontmatter.get('briefing', ''),
    }

    if audio_path and audio_path.exists():
        episode_data['duration'] = get_duration(audio_path)
        episode_data['audio_size'] = audio_path.stat().st_size

    yaml_path = episodes_dir / f"{episode_num}.yaml"
    with open(yaml_path, 'w') as f:
        yaml.dump(episode_data, f, default_flow_style=False, sort_keys=False)

    return yaml_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 podcast/compose.py <script-path> [--dry-run]")
        sys.exit(1)

    script_path = Path(sys.argv[1])
    dry_run = '--dry-run' in sys.argv

    if not script_path.exists():
        sys.exit(f"Script not found: {script_path}")

    # Load config
    config_path = Path('podcast/_config.yaml')
    if config_path.exists():
        with open(config_path) as f:
            config = yaml.safe_load(f)
    else:
        config = {}

    # Parse script
    text = script_path.read_text()
    frontmatter = parse_frontmatter(text)
    segments = parse_script(text)

    if not segments:
        sys.exit("No dialogue segments found in script.")

    # Stats
    total_chars = sum(len(s['text']) for s in segments)
    total_words = sum(len(s['text'].split()) for s in segments)
    est_duration = total_words / 150  # minutes at conversational pace

    print(f"\nScript: {script_path.name}")
    print(f"Segments: {len(segments)}")
    print(f"Words: {total_words:,}")
    print(f"Characters: {total_chars:,} (TTS billing)")
    print(f"Est. duration: {est_duration:.1f} min")
    print(f"Host A lines: {sum(1 for s in segments if s['speaker'] == 'A')}")
    print(f"Host B lines: {sum(1 for s in segments if s['speaker'] == 'B')}")

    if dry_run:
        print("\n--dry-run: skipping TTS and audio composition.")
        return

    # Check API key
    if not os.environ.get('ELEVENLABS_API_KEY'):
        print("\nNo ELEVENLABS_API_KEY found. Set it in .env or export it.")
        print("Skipping audio rendering. Run again with the key set, or use --dry-run for stats only.")
        return

    # Create output directory
    episode_id = frontmatter.get('episode', 'EP001')
    date = frontmatter.get('date', 'unknown')
    output_dir = Path(f"podcast/audio/{episode_id}-{date}")
    output_dir.mkdir(parents=True, exist_ok=True)

    # Render TTS
    print(f"\nRendering {len(segments)} segments via ElevenLabs...")
    audio_files = render_elevenlabs(segments, config, output_dir)

    if not audio_files:
        sys.exit("No audio files generated. Check API key and network.")

    print(f"\nRendered {len(audio_files)}/{len(segments)} segments.")

    # Compose final audio
    print("Composing final episode...")
    final = compose_audio(audio_files, segments, config, output_dir)
    duration = get_duration(final)

    # Write episode metadata
    yaml_path = write_episode_yaml(frontmatter, final, config, output_dir)

    # Clean up individual segment files
    for f in audio_files:
        f.unlink(missing_ok=True)

    print(f"\nDone!")
    print(f"Audio: {final}")
    print(f"Duration: {duration}")
    print(f"Metadata: {yaml_path}")
    print(f"Characters used: {total_chars:,}")


if __name__ == '__main__':
    main()

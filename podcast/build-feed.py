#!/usr/bin/env python3
"""
Podcast RSS Feed Generator

Reads episode YAML files and show config to generate a podcast-compliant
RSS 2.0 feed with iTunes namespace extensions.

Usage:
    python3 podcast/build-feed.py
"""

import sys
from datetime import datetime, timezone
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, ElementTree, indent

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency: pip install PyYAML")


REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = REPO_ROOT / 'podcast' / '_config.yaml'
EPISODES_DIR = REPO_ROOT / 'podcast' / 'episodes'
FEED_PATH = REPO_ROOT / 'podcast' / 'feed.xml'

ITUNES_NS = 'http://www.itunes.com/dtds/podcast-1.0.dtd'


def load_config() -> dict:
    with open(CONFIG_PATH) as f:
        return yaml.safe_load(f)


def load_episodes() -> list[dict]:
    if not EPISODES_DIR.exists():
        return []
    episodes = []
    for ep_file in sorted(EPISODES_DIR.glob('*.yaml'), reverse=True):
        with open(ep_file) as f:
            data = yaml.safe_load(f)
            if data:
                episodes.append(data)
    return episodes


def format_duration(duration_str: str) -> str:
    """Ensure duration is in HH:MM:SS format for iTunes."""
    parts = duration_str.split(':')
    if len(parts) == 2:
        return f"00:{duration_str}"
    return duration_str


def format_pub_date(date_str: str) -> str:
    """Convert YYYY-MM-DD to RFC 2822 format."""
    try:
        dt = datetime.strptime(date_str, '%Y-%m-%d').replace(tzinfo=timezone.utc)
        return dt.strftime('%a, %d %b %Y %H:%M:%S +0000')
    except (ValueError, TypeError):
        return datetime.now(timezone.utc).strftime('%a, %d %b %Y %H:%M:%S +0000')


def build_feed(config: dict, episodes: list[dict]) -> ElementTree:
    show = config.get('show', {})

    rss = Element('rss', {
        'version': '2.0',
        'xmlns:itunes': ITUNES_NS,
        'xmlns:content': 'http://purl.org/rss/1.0/modules/content/',
    })
    channel = SubElement(rss, 'channel')

    # Channel metadata
    SubElement(channel, 'title').text = show.get('title', 'Hype Watch')
    SubElement(channel, 'link').text = show.get('website', '')
    SubElement(channel, 'language').text = show.get('language', 'en-us')
    SubElement(channel, 'description').text = show.get('description', '')
    SubElement(channel, '{%s}subtitle' % ITUNES_NS).text = show.get('subtitle', '')
    SubElement(channel, '{%s}author' % ITUNES_NS).text = show.get('author', '')
    SubElement(channel, '{%s}explicit' % ITUNES_NS).text = 'no'

    owner = SubElement(channel, '{%s}owner' % ITUNES_NS)
    SubElement(owner, '{%s}name' % ITUNES_NS).text = show.get('author', '')
    SubElement(owner, '{%s}email' % ITUNES_NS).text = show.get('email', '')

    cat = SubElement(channel, '{%s}category' % ITUNES_NS, text=show.get('category', 'Technology'))
    if show.get('subcategory'):
        SubElement(cat, '{%s}category' % ITUNES_NS, text=show['subcategory'])

    artwork_url = show.get('artwork', '')
    if artwork_url:
        SubElement(channel, '{%s}image' % ITUNES_NS, href=artwork_url)

    # Episodes
    for ep in episodes:
        audio_url = ep.get('audio_url')
        if not audio_url:
            continue

        item = SubElement(channel, 'item')
        SubElement(item, 'title').text = f"{ep.get('episode', '')}: {ep.get('title', 'Untitled')}"
        SubElement(item, 'pubDate').text = format_pub_date(ep.get('date', ''))

        # Build description from sources
        source_count = len(ep.get('sources', []))
        desc = f"Episode covering {source_count} sources from the AI Hype Watcher project."
        SubElement(item, 'description').text = desc

        enclosure_attrs = {
            'url': audio_url,
            'type': 'audio/mpeg',
        }
        if ep.get('audio_size'):
            enclosure_attrs['length'] = str(ep['audio_size'])
        SubElement(item, 'enclosure', enclosure_attrs)

        if ep.get('duration'):
            SubElement(item, '{%s}duration' % ITUNES_NS).text = format_duration(ep['duration'])

        SubElement(item, '{%s}explicit' % ITUNES_NS).text = 'no'

        guid = SubElement(item, 'guid', isPermaLink='false')
        guid.text = f"hypewatch-{ep.get('episode', '').lower()}"

    tree = ElementTree(rss)
    indent(tree, space='  ')
    return tree


def main():
    config = load_config()
    episodes = load_episodes()

    if not episodes:
        print("No episodes found. Feed will be empty.")

    tree = build_feed(config, episodes)

    with open(FEED_PATH, 'wb') as f:
        tree.write(f, encoding='utf-8', xml_declaration=True)

    print(f"Feed written: {FEED_PATH}")
    print(f"Episodes: {len(episodes)}")


if __name__ == '__main__':
    main()

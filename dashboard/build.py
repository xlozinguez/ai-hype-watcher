#!/usr/bin/env python3
"""Build data.json for the AI Hype Watcher dashboard."""

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import frontmatter

ROOT = Path(__file__).resolve().parent.parent
SOURCES_DIR = ROOT / "sources"
CURRICULUM_DIR = ROOT / "curriculum"
SYNTHESIS_DIR = ROOT / "synthesis"
OUTPUT = Path(__file__).resolve().parent / "data.json"

SKIP_FILES = {"_template.md", "README.md"}


def parse_sources():
    """Parse all source markdown files, returning nodes and raw data for edges."""
    nodes = []
    source_data = {}  # id -> parsed info

    for path in sorted(SOURCES_DIR.glob("*.md")):
        if path.name in SKIP_FILES or path.name.startswith("_"):
            continue

        post = frontmatter.load(path)
        meta = post.metadata
        sid = meta.get("source_id", "")
        if not sid:
            continue

        # Extract first 2 sentences of ## Summary
        summary = ""
        in_summary = False
        summary_lines = []
        for line in post.content.split("\n"):
            if line.strip().startswith("## Summary"):
                in_summary = True
                continue
            if in_summary:
                if line.strip().startswith("## ") or line.strip().startswith("# "):
                    break
                summary_lines.append(line)

        summary_text = " ".join(summary_lines).strip()
        # Extract first 2 sentences
        sentences = re.split(r'(?<=[.!?])\s+', summary_text)
        summary = " ".join(sentences[:2]).strip()

        # Parse related sources
        related_ids = []
        in_related = False
        for line in post.content.split("\n"):
            if line.strip().startswith("## Related Sources"):
                in_related = True
                continue
            if in_related:
                if line.strip().startswith("## ") or line.strip().startswith("# "):
                    break
                matches = re.findall(r'\[(\d{3}):', line)
                related_ids.extend(matches)

        tags = meta.get("tags", []) or []
        modules = meta.get("curriculum_modules", []) or []

        nodes.append({
            "id": sid,
            "type": "source",
            "title": meta.get("title", ""),
            "creator": meta.get("creator", ""),
            "date": meta.get("date", ""),
            "tags": tags,
            "modules": modules,
            "summary": summary,
            "url": meta.get("url", ""),
        })

        source_data[sid] = {
            "tags": tags,
            "modules": modules,
            "related_ids": related_ids,
        }

    return nodes, source_data


def parse_curriculum():
    """Parse curriculum module READMEs for module nodes."""
    nodes = []
    for path in sorted(CURRICULUM_DIR.glob("*/README.md")):
        folder = path.parent.name
        match = re.match(r"(\d{2})-(.+)", folder)
        if not match:
            continue
        order = int(match.group(1))
        # Extract title from first heading
        text = path.read_text()
        title_match = re.search(r"^#\s+Module\s+\d+:\s+(.+)", text, re.MULTILINE)
        label = title_match.group(1).strip() if title_match else folder
        nodes.append({
            "id": f"mod:{folder}",
            "type": "module",
            "label": label,
            "order": order,
        })
    return nodes


def parse_synthesis():
    """Parse synthesis docs for themes and source references."""
    entries = []
    for path in sorted(SYNTHESIS_DIR.glob("*.md")):
        if path.name == "README.md":
            continue
        text = path.read_text()

        # Try YAML frontmatter first, then **Date**: line
        post = frontmatter.loads(text)
        fm_date = post.metadata.get("date", "")
        if fm_date:
            date = str(fm_date)
        else:
            date_match = re.search(r"\*\*Date\*\*:\s*(\d{4}-\d{2}-\d{2})", text)
            date = date_match.group(1) if date_match else ""

        # Title from frontmatter or first heading
        fm_title = post.metadata.get("title", "")
        if fm_title:
            title = fm_title
        else:
            title_match = re.search(r"^#\s+(?:Synthesis:\s*)?(.+)", text, re.MULTILINE)
            title = title_match.group(1).strip() if title_match else path.stem

        # Extract themes: ### headings under any theme-like ## section
        themes = []
        in_themes = False
        for line in text.split("\n"):
            if re.match(r"^##\s+.*(Theme|Cross-Cutting)", line):
                in_themes = True
                continue
            if in_themes:
                # Stop at next ## heading that isn't a theme heading
                if re.match(r"^##\s+", line) and not re.match(r"^##\s+Theme\s", line):
                    in_themes = False
                    continue
                # Capture ### subheadings as themes
                theme_match = re.match(r"^###\s+(?:\d+\.\s+)?(.+)", line)
                if theme_match:
                    themes.append(theme_match.group(1).strip())
                # Also capture ## Theme X: Title patterns
                theme_match2 = re.match(r"^##\s+Theme\s+\w+:\s*(.+)", line)
                if theme_match2:
                    themes.append(theme_match2.group(1).strip())

        # Extract source IDs: #NNN patterns and [NNN: patterns
        source_ids = sorted(set(
            re.findall(r'#(\d{3})\b', text) +
            re.findall(r'\[(\d{3}):', text) +
            re.findall(r'\[(\d{3})\]', text)
        ))

        entries.append({
            "id": path.stem,
            "date": date,
            "title": title,
            "themes": themes,
            "source_ids": source_ids,
        })

    return entries


def build():
    source_nodes, source_data = parse_sources()
    module_nodes = parse_curriculum()
    synthesis = parse_synthesis()

    # Build tag nodes with counts
    tag_counts = {}
    for data in source_data.values():
        for tag in data["tags"]:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    tag_nodes = [
        {"id": f"tag:{tag}", "type": "tag", "label": tag, "count": count}
        for tag, count in sorted(tag_counts.items())
    ]

    # Build edges
    edges = []
    for sid, data in source_data.items():
        for rid in data["related_ids"]:
            edges.append({"source": sid, "target": rid, "type": "related"})
        for tag in data["tags"]:
            edges.append({"source": sid, "target": f"tag:{tag}", "type": "tag"})
        for mod in data["modules"]:
            edges.append({"source": sid, "target": f"mod:{mod}", "type": "curriculum"})

    nodes = source_nodes + tag_nodes + module_nodes

    result = {
        "nodes": nodes,
        "edges": edges,
        "synthesis": synthesis,
        "meta": {
            "generated": datetime.now(timezone.utc).isoformat(),
            "source_count": len(source_nodes),
            "tag_count": len(tag_nodes),
        },
    }

    OUTPUT.write_text(json.dumps(result, indent=2, default=str))
    print(f"Wrote {OUTPUT}")
    print(f"  Sources: {len(source_nodes)}")
    print(f"  Tags: {len(tag_nodes)}")
    print(f"  Modules: {len(module_nodes)}")
    print(f"  Edges: {len(edges)}")
    print(f"  Synthesis: {len(synthesis)}")


if __name__ == "__main__":
    build()

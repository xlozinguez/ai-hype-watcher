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
BRIEFINGS_DIR = ROOT / "briefings"
RESEARCH_DIR = ROOT / "research"
OUTPUT = Path(__file__).resolve().parent / "data.json"
SRC_DIR = Path(__file__).resolve().parent / "src"

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

        # Build HTML body from source sections
        body_lines = []
        include = False
        for line in post.content.split("\n"):
            if re.match(r"^## (Summary|Key Concepts|Practical Takeaways|Notable Quotes)", line):
                include = True
            elif re.match(r"^## (Related|Curriculum)", line):
                include = False
            if include:
                body_lines.append(line)
        body_html = md_to_html("\n".join(body_lines))

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
            "body_html": body_html,
        })

        source_data[sid] = {
            "tags": tags,
            "modules": modules,
            "related_ids": related_ids,
        }

    return nodes, source_data


def parse_curriculum():
    """Parse curriculum module READMEs for module nodes with section structure."""
    nodes = []
    for path in sorted(CURRICULUM_DIR.glob("*/README.md")):
        folder = path.parent.name
        match = re.match(r"(\d{2})-(.+)", folder)
        if not match:
            continue
        order = int(match.group(1))
        text = path.read_text()
        lines = text.split("\n")

        # Extract title from first heading
        title_match = re.search(r"^#\s+Module\s+\d+:\s+(.+)", text, re.MULTILINE)
        label = title_match.group(1).strip() if title_match else folder

        # Extract overview (first paragraph after ## Overview)
        overview = ""
        in_overview = False
        overview_lines = []
        for line in lines:
            if re.match(r"^##\s+Overview", line):
                in_overview = True
                continue
            if in_overview:
                if line.strip().startswith("## ") or line.strip().startswith("# "):
                    break
                if line.strip():
                    overview_lines.append(line.strip())
                elif overview_lines:
                    break  # stop at first blank line after content
        overview = strip_markdown(first_n_sentences(" ".join(overview_lines), 2))

        # Parse sections by splitting on ## headings
        current_section = None
        sections = {
            "core-concepts": {"label": "Core Concepts", "items": []},
            "patterns": {"label": "Patterns & Practices", "items": []},
            "pitfalls": {"label": "Common Pitfalls", "items": []},
            "exercises": {"label": "Hands-On Exercises", "items": []},
        }

        # Track current item to collect its body text for citation extraction
        current_item = None
        current_item_lines = []

        def flush_item_citations():
            """Extract [#NNN] citations from accumulated body lines into the current item."""
            nonlocal current_item, current_item_lines
            if current_item and current_item_lines:
                body = "\n".join(current_item_lines)
                cited = set(re.findall(r'\[#?(\d{3})\b', body))
                cited.update(re.findall(r'\(#(\d{3})\b', body))
                cited.update(re.findall(r'#(\d{3})\b', body))
                current_item["cited_sources"] = sorted(cited)
            current_item = None
            current_item_lines = []

        for line in lines:
            # Track which ## section we're in
            h2 = re.match(r"^##\s+(.+)", line)
            if h2:
                flush_item_citations()
                heading = h2.group(1).strip()
                if "Core Concepts" in heading:
                    current_section = "core-concepts"
                elif "Patterns" in heading:
                    current_section = "patterns"
                elif "Common Pitfalls" in heading:
                    current_section = "pitfalls"
                elif "Hands-On Exercises" in heading:
                    current_section = "exercises"
                elif "Source Material" in heading or "Further Reading" in heading:
                    current_section = None
                continue

            if not current_section:
                continue

            # Concepts: ### Concept N: Title or ### Concept Na: Title
            if current_section == "core-concepts":
                cm = re.match(r"^###\s+Concept\s+(\S+):\s+(.+)", line)
                if cm:
                    flush_item_citations()
                    current_item = {
                        "id": f"c{cm.group(1)}",
                        "title": strip_markdown(cm.group(2).strip()),
                        "cited_sources": [],
                    }
                    sections["core-concepts"]["items"].append(current_item)
                    continue

            # Patterns: ### Pattern N: Title or ### Pattern: Title
            elif current_section == "patterns":
                pm = re.match(r"^###\s+Pattern(?:\s+\d+)?:\s+(.+)", line)
                if pm:
                    flush_item_citations()
                    current_item = {
                        "id": f"p{len(sections['patterns']['items']) + 1}",
                        "title": strip_markdown(pm.group(1).strip()),
                        "cited_sources": [],
                    }
                    sections["patterns"]["items"].append(current_item)
                    continue

            # Pitfalls: - **Description**: ... (first bold phrase is the title)
            elif current_section == "pitfalls":
                pit = re.match(r"^-\s+\*\*(.+?)\*\*", line)
                if pit:
                    flush_item_citations()
                    title = re.sub(r"^Pitfall:\s*", "", pit.group(1).strip()).rstrip(":")
                    if len(title) > 80:
                        title = title[:77] + "..."
                    current_item = {
                        "id": f"pit{len(sections['pitfalls']['items']) + 1}",
                        "title": strip_markdown(title),
                        "cited_sources": [],
                    }
                    sections["pitfalls"]["items"].append(current_item)

            # Exercises: N. **Title**: ...
            elif current_section == "exercises":
                ex = re.match(r"^\d+\.\s+\*\*(.+?)\*\*", line)
                if ex:
                    flush_item_citations()
                    current_item = {
                        "id": f"ex{len(sections['exercises']['items']) + 1}",
                        "title": strip_markdown(ex.group(1).strip().rstrip(":")),
                        "cited_sources": [],
                    }
                    sections["exercises"]["items"].append(current_item)

            # Accumulate body lines for citation extraction
            if current_item:
                current_item_lines.append(line)

        # Flush the last item
        flush_item_citations()

        # Build sections array (only include non-empty sections)
        sections_list = []
        for sid, sec in sections.items():
            if sec["items"]:
                sections_list.append({
                    "id": sid,
                    "label": sec["label"],
                    "count": len(sec["items"]),
                    "items": sec["items"],
                })

        nodes.append({
            "id": f"mod:{folder}",
            "type": "module",
            "label": label,
            "order": order,
            "overview": overview,
            "sections": sections_list,
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

        # Extract source IDs: frontmatter list, #NNN patterns, [NNN: patterns
        fm_source_ids = post.metadata.get("source_ids", []) or []
        source_ids = sorted(set(
            [str(s) for s in fm_source_ids] +
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


def parse_research():
    """Parse research docs for the reader."""
    entries = []
    if not RESEARCH_DIR.exists():
        return entries
    for path in sorted(RESEARCH_DIR.glob("*.md")):
        if path.name in SKIP_FILES or path.name.startswith("_"):
            continue
        text = path.read_text()

        # Date from filename (YYYY-MM-DD-slug.md)
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})", path.stem)
        date = date_match.group(1) if date_match else ""

        # Title from first heading
        title_match = re.search(r"^#\s+(?:Research:\s*)?(.+)", text, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else path.stem

        # Extract source IDs
        source_ids = sorted(set(
            re.findall(r'#(\d{3})\b', text) +
            re.findall(r'\[(\d{3}):', text) +
            re.findall(r'\[#(\d{3})\]', text)
        ))

        # Extract ## section headings as themes
        themes = []
        for line in text.split("\n"):
            h2 = re.match(r"^##\s+(.+)", line)
            if h2:
                heading = h2.group(1).strip()
                if heading not in ("Overview",):
                    themes.append(heading)

        entries.append({
            "id": path.stem,
            "date": date,
            "title": title,
            "themes": themes,
            "source_ids": source_ids,
        })

    return entries


def strip_markdown(text):
    """Strip markdown formatting for clean HTML display."""
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)  # bold
    text = re.sub(r'\*(.+?)\*', r'\1', text)        # italic
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)  # links
    text = re.sub(r'[`]', '', text)                  # inline code
    return text.strip()


def first_n_sentences(text, n=2):
    """Extract first n sentences from text."""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return " ".join(sentences[:n]).strip()


def parse_briefings():
    """Parse briefing markdown files for the reader."""
    entries = []
    for path in sorted(BRIEFINGS_DIR.glob("*.md")):
        if path.name in SKIP_FILES or path.name.startswith("_"):
            continue
        text = path.read_text()
        lines = text.split("\n")

        # Date from filename
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})", path.stem)
        date = date_match.group(1) if date_match else ""

        # Focus line: > **Focus**: ...
        focus = ""
        for line in lines:
            fm = re.match(r">\s*\*\*Focus\*\*:\s*(.+)", line)
            if fm:
                focus = fm.group(1).strip()
                break

        # Headlines: - **[category]** Title (possibly with **Title**)
        headlines = []
        in_headlines = False
        for line in lines:
            if line.strip().startswith("## Headlines"):
                in_headlines = True
                continue
            if in_headlines:
                if line.strip().startswith("## "):
                    break
                hm = re.match(
                    r"-\s*\*\*\[(\w+)\]\*\*\s*\*?\*?(.+?)(?:\*\*)?$", line.strip()
                )
                if hm:
                    headlines.append({
                        "category": hm.group(1),
                        "title": re.sub(r"\*\*", "", hm.group(2)).strip().rstrip("*"),
                    })

        # Detail summaries + source IDs per ### section under ## Details
        detail_data = {}  # heading -> {"summary": str, "source_ids": []}
        in_details = False
        current_heading = None
        detail_lines = []
        for line in lines:
            if line.strip().startswith("## Details"):
                in_details = True
                continue
            if in_details:
                if re.match(r"^## [^#]", line.strip()):
                    break
                heading_match = re.match(r"^###\s+(.+)", line)
                if heading_match:
                    if current_heading and detail_lines:
                        para = " ".join(detail_lines).strip()
                        sentences = re.split(r'(?<=[.!?])\s+', para)
                        src_ids = re.findall(r'#(\d{3})\b', para) + re.findall(r'\[(\d{3}):', para)
                        detail_data[current_heading] = {
                            "summary": sentences[0] if sentences else "",
                            "source_ids": list(dict.fromkeys(src_ids)),  # dedupe, preserve order
                        }
                    current_heading = heading_match.group(1).strip()
                    detail_lines = []
                elif current_heading and line.strip() and current_heading not in detail_data:
                    detail_lines.append(line.strip())
        # Last heading
        if current_heading and detail_lines and current_heading not in detail_data:
            para = " ".join(detail_lines).strip()
            sentences = re.split(r'(?<=[.!?])\s+', para)
            src_ids = re.findall(r'#(\d{3})\b', para) + re.findall(r'\[(\d{3}):', para)
            detail_data[current_heading] = {
                "summary": sentences[0] if sentences else "",
                "source_ids": list(dict.fromkeys(src_ids)),
            }

        # Attach summaries and source IDs to headlines by matching title substring
        detail_keys = list(detail_data.keys())
        used_headings = set()
        for h in headlines:
            h["summary"] = ""
            h["detail_source_ids"] = []
            best_match = None
            best_overlap = 0
            for heading, data in detail_data.items():
                if heading in used_headings:
                    continue
                title_words = set(re.findall(r'\w+', h["title"].lower()))
                heading_words = set(re.findall(r'\w+', heading.lower()))
                overlap = len(title_words & heading_words)
                if overlap > best_overlap:
                    best_overlap = overlap
                    best_match = heading
            # Accept match with 2+ word overlap, or fallback to positional
            if best_match and best_overlap >= 2:
                h["summary"] = detail_data[best_match]["summary"]
                h["detail_source_ids"] = detail_data[best_match]["source_ids"]
                used_headings.add(best_match)
            elif detail_keys:
                # Positional fallback: match by order
                idx = headlines.index(h)
                if idx < len(detail_keys):
                    key = detail_keys[idx]
                    if key not in used_headings:
                        h["summary"] = detail_data[key]["summary"]
                        h["detail_source_ids"] = detail_data[key]["source_ids"]
                        used_headings.add(key)

        # Source IDs
        source_ids = sorted(set(
            re.findall(r'#(\d{3})\b', text) +
            re.findall(r'\[(\d{3}):', text) +
            re.findall(r'\[#(\d{3})\]', text)
        ))

        # Related source IDs from Connections section
        related_source_ids = []
        in_connections = False
        for line in lines:
            if line.strip().startswith("## Connections"):
                in_connections = True
                continue
            if in_connections:
                if line.strip().startswith("## "):
                    break
                related_source_ids.extend(re.findall(r'#(\d{3})\b', line))
                related_source_ids.extend(re.findall(r'\[(\d{3}):', line))

        entries.append({
            "id": date,
            "type": "briefing",
            "date": date,
            "focus": focus,
            "headlines": headlines,
            "source_ids": source_ids,
            "related_source_ids": sorted(set(related_source_ids)),
        })

    return entries


def linkify_sources(html):
    """Convert #NNN references into tappable source links."""
    return re.sub(
        r'#(\d{3})\b',
        r'<a class="src-link" data-src="\1" href="#">#\1</a>',
        html,
    )


def build_reader_content(briefings, synthesis_entries, research_entries=None):
    """Build condensed reader documents with pre-rendered HTML."""
    documents = []
    research_entries = research_entries or []

    # Briefings — already structured, just add body_html
    for b in briefings:
        headlines_html = ""
        for h in b["headlines"]:
            summary = strip_markdown(first_n_sentences(h.get("summary", ""), 1))
            summary_html = f'<p class="headline-summary">{summary}</p>' if summary else ""
            # Source links for this headline
            src_links = " ".join(
                f'<a class="src-link" data-src="{sid}" href="#">#{sid}</a>'
                for sid in h.get("detail_source_ids", [])[:4]
            )
            src_html = f'<div class="headline-sources">{src_links}</div>' if src_links else ""
            headlines_html += (
                f'<div class="headline">'
                f'<span class="cat cat-{h["category"]}">{h["category"]}</span> '
                f'<strong>{strip_markdown(h["title"])}</strong>'
                f'{summary_html}'
                f'{src_html}'
                f'</div>'
            )

        sources_html = " ".join(f'#{s}' for s in b["source_ids"][:12])
        if len(b["source_ids"]) > 12:
            sources_html += f' +{len(b["source_ids"]) - 12} more'

        body_html = linkify_sources(
            f'<div class="card-focus">{b["focus"]}</div>'
            f'<div class="card-headlines">{headlines_html}</div>'
            f'<div class="card-sources">Sources: {sources_html}</div>'
        )

        documents.append({
            "id": b["id"],
            "type": "briefing",
            "date": b["date"],
            "title": "",
            "subtitle": "",
            "body_html": body_html,
        })

    # Synthesis — extract overview + theme insights
    for s in synthesis_entries:
        path = SYNTHESIS_DIR / f'{s["id"]}.md'
        if not path.exists():
            continue
        text = path.read_text()
        lines = text.split("\n")

        # Detect weekly synthesis format
        post = frontmatter.loads(text)
        is_weekly = post.metadata.get("type", "") in ("weekly-synthesis",)

        if is_weekly:
            # Weekly format: parse sections and render with briefing-style markup
            sections = {}  # section_name -> [lines]
            current_section = None
            for line in lines:
                section_match = re.match(r"^## (.+)", line)
                if section_match:
                    current_section = section_match.group(1).strip()
                    sections[current_section] = []
                    continue
                if current_section and line.strip() != "---":
                    sections[current_section].append(line)

            rendered = ""

            # Section config: name -> (css_class, accent_color)
            section_styles = {
                "What's Persisting": ("persisting", "cyan"),
                "What's New": ("new", "purple"),
                "What's New This Week": ("new", "purple"),
                "What to Watch": ("watch", "amber"),
                "Try This Week": ("try", "green"),
            }

            for section_name, section_lines in sections.items():
                if section_name == "Source Takeaways":
                    continue  # skip table — available via source taps

                style = section_styles.get(section_name)
                if not style:
                    continue
                css_class, accent = style

                # Render section content
                content_md = "\n".join(section_lines)
                content_html = md_to_html(content_md)

                rendered += (
                    f'<div class="weekly-section weekly-{css_class}">'
                    f'<div class="weekly-label weekly-label-{accent}">{section_name}</div>'
                    f'{content_html}'
                    f'</div>'
                )

            source_range = ""
            if s["source_ids"]:
                source_range = f'#{s["source_ids"][0]}–#{s["source_ids"][-1]} ({len(s["source_ids"])} sources)'

            body_html = linkify_sources(
                f'{rendered}'
                f'<div class="card-sources">Sources: {source_range}</div>'
            )
        else:
            # Standard synthesis format
            overview = ""
            in_overview = False
            overview_lines = []
            for line in lines:
                if re.match(r"^##\s+(Executive Summary|Overview)", line):
                    in_overview = True
                    continue
                if in_overview:
                    if line.strip().startswith("## ") or line.strip().startswith("# ") or line.strip() == "---":
                        if overview_lines:
                            break
                        continue
                    if line.strip():
                        overview_lines.append(line.strip())
            overview = " ".join(overview_lines).strip()
            overview_short = strip_markdown(first_n_sentences(overview, 2))

            # Extract theme insights
            theme_insights = []
            for theme_title in s.get("themes", []):
                theme_insights.append({"title": theme_title, "insight": ""})

            # Try to find **Key Insight:** or **Core Insight:** for each theme section
            current_theme_idx = -1
            for line in lines:
                theme_match = re.match(r"^##\s+(?:Theme\s+\w+:\s*)?(.+)", line)
                if not theme_match:
                    theme_match = re.match(r"^###\s+(?:Theme\s+\d+:\s*)?(?:\d+\.\s+)?(.+)", line)
                if theme_match:
                    title = theme_match.group(1).strip()
                    for i, t in enumerate(theme_insights):
                        if t["title"] in title or title in t["title"]:
                            current_theme_idx = i
                            break

                insight_match = re.match(
                    r"\*\*(?:Key Insight|Core Insight)\*?\*?:\*?\*?\s*(.+)", line.strip()
                )
                if insight_match and 0 <= current_theme_idx < len(theme_insights):
                    if not theme_insights[current_theme_idx]["insight"]:
                        raw = insight_match.group(1).strip()
                        insight = strip_markdown(first_n_sentences(raw, 1))
                        if len(insight) > 160:
                            insight = insight[:157] + "..."
                        theme_insights[current_theme_idx]["insight"] = insight

            themes_html = ""
            for i, t in enumerate(theme_insights[:5], 1):
                insight = t.get("insight", "")
                insight_html = f'<p class="theme-insight">{insight}</p>' if insight else ""
                title = re.sub(r'^Theme\s+\w+:\s*', '', strip_markdown(t["title"]))
                themes_html += (
                    f'<div class="theme">'
                    f'<strong>{i}. {title}</strong>'
                    f'{insight_html}'
                    f'</div>'
                )

            source_range = ""
            if s["source_ids"]:
                source_range = f'#{s["source_ids"][0]}–#{s["source_ids"][-1]} ({len(s["source_ids"])} sources)'

            body_html = linkify_sources(
                f'<div class="card-overview">{overview_short}</div>'
                f'<div class="card-themes">{themes_html}</div>'
                f'<div class="card-sources">Sources: {source_range}</div>'
            )

        # Subtitle from source range or date
        subtitle = source_range if source_range else s["date"]

        documents.append({
            "id": s["id"],
            "type": "synthesis",
            "date": s["date"],
            "title": s["title"],
            "subtitle": subtitle,
            "body_html": body_html,
        })

    # Research — long-form analysis with styled HTML components
    for r in research_entries:
        path = RESEARCH_DIR / f'{r["id"]}.md'
        if not path.exists():
            continue
        text = path.read_text()
        lines = text.split("\n")

        # Parse sections: collect ## headings with first 2 sentences of content
        sections = []
        current_heading = None
        current_lines = []
        in_mermaid = False

        for line in lines:
            if line.strip().startswith("```"):
                in_mermaid = not in_mermaid
                continue
            if in_mermaid:
                continue

            h2 = re.match(r"^##\s+(.+)", line)
            if h2:
                if current_heading:
                    para = " ".join(current_lines).strip()
                    sections.append({
                        "heading": current_heading,
                        "text": strip_markdown(first_n_sentences(para, 1)) if para else "",
                    })
                current_heading = h2.group(1).strip()
                current_lines = []
                continue

            if current_heading and line.strip() and not line.strip().startswith("#"):
                # Skip markdown table rows and horizontal rules
                if line.strip() == "---" or line.strip().startswith("|") or line.strip().startswith("> **"):
                    continue
                current_lines.append(line.strip())

        if current_heading:
            para = " ".join(current_lines).strip()
            sections.append({
                "heading": current_heading,
                "text": strip_markdown(first_n_sentences(para, 2)) if para else "",
            })

        # Section icon/color mapping
        section_icons = {
            "Overview": ("🔭", "green"),
            "The Autonomy Calibration Model": ("🎛️", "amber"),
            "Phase-by-Phase Breakdown": ("🔄", "cyan"),
            "Deep Dive: The Three-Agent Ticket Capture Pattern": ("🎯", "purple"),
            "Deep Dive: The Tester Agent": ("🧪", "green"),
            "The Episodic Feedback Meta-Loop": ("🔁", "amber"),
            "The Compound Effect": ("📈", "cyan"),
        }

        body_parts = []

        for sec in sections:
            heading = sec["heading"]
            if heading in ("Summary Table",):
                continue

            icon, color = section_icons.get(heading, ("📄", "cyan"))

            if heading == "Overview":
                # Shorter overview for the card
                overview_short = first_n_sentences(sec["text"], 2)
                body_parts.append(
                    f'<div class="research-overview">{overview_short}</div>'
                )
                continue

            if heading == "The Autonomy Calibration Model":
                body_parts.append(
                    f'<div class="research-section">'
                    f'<div class="research-section-head">'
                    f'<div class="rs-icon" style="background:rgba(245,158,11,0.1)">{icon}</div>'
                    f'<h3>Autonomy Levels</h3></div>'
                    f'<p>{sec["text"]}</p>'
                    f'<div class="autonomy-bar">'
                    f'<div class="autonomy-level al-0"><span class="al-tag">L0</span><span class="al-content"><span class="al-label">Assist</span><span class="al-desc">Autocomplete and inline suggestions. Human is the primary author, LLM fills in tokens.</span></span></div>'
                    f'<div class="autonomy-level al-1"><span class="al-tag">L1</span><span class="al-content"><span class="al-label">Draft</span><span class="al-desc">LLM produces a complete first draft. Human reviews everything before it moves forward.</span></span></div>'
                    f'<div class="autonomy-level al-2"><span class="al-tag">L2</span><span class="al-content"><span class="al-label">Gated</span><span class="al-desc">Research → Plan → Implement loop with human review gates between phases. Sweet spot for medium-risk work.</span></span></div>'
                    f'<div class="autonomy-level al-3"><span class="al-tag">L3</span><span class="al-content"><span class="al-label">Autonomous</span><span class="al-desc">LLM executes end-to-end. Human reviews only the final outcome. Requires strong test coverage as the completion signal.</span></span></div>'
                    f'<div class="autonomy-level al-4"><span class="al-tag">L4</span><span class="al-content"><span class="al-label">Delegated</span><span class="al-desc">One LLM implements, another LLM reviews. Human spot-checks batches of completed work.</span></span></div>'
                    f'<div class="autonomy-level al-5"><span class="al-tag">L5</span><span class="al-content"><span class="al-label">Overnight</span><span class="al-desc">Batch dispatch at end of day. Review N completed branches next morning. Requires months of L2-L4 trust-building.</span></span></div>'
                    f'</div></div>'
                )
                continue

            if heading == "Phase-by-Phase Breakdown":
                phases = [
                    ("1", "Discovery", "Agent synthesizes internal context and external evidence in minutes", "Catches: \"we already tried this\"", "L1", "blue"),
                    ("2", "Specification", "Three agents stress-test the spec: codebase reality, validation questions, vision alignment", "Catches: ambiguity and misalignment before sprint starts", "L2", "purple"),
                    ("3", "Planning", "Agent reads spec + codebase, proposes file-level plan with dependency order", "Catches: \"this touches 3 services we didn't expect\"", "L2", "purple"),
                    ("4", "Implementation", "Research → Plan → Implement loop per ticket with test validation", "Catches: spec drift and test failures before code review", "L2-4", "green"),
                    ("5", "Testing", "Tester Agent generates cases from spec (not implementation) to avoid confirmation bias", "Catches: missed edge cases and coverage gaps", "L3", "green"),
                    ("6", "Code Review", "Agent pre-review: anti-patterns, spec alignment, security scans", "Catches: mechanical issues so reviewer focuses on judgment", "L1-3", "blue"),
                    ("7", "Deployment", "Agent validates deployment checklist: CI, dependencies, feature flags, rollback", "Catches: missing config or dependency updates", "L2", "purple"),
                    ("8", "Monitoring", "Agent correlates error spikes with deployment changes within first hour", "Catches: anomalies before customers complain", "L3", "green"),
                ]
                flow_html = '<div class="research-flow">'
                for i, (num, name, desc, catches, level, clr) in enumerate(phases):
                    flow_html += (
                        f'<div class="flow-step">'
                        f'<span class="flow-num {clr}">{num}</span>'
                        f'<span class="flow-label"><strong>{name}</strong> <small class="flow-level">{level}</small>'
                        f'<small>{desc}</small>'
                        f'<small class="flow-catches">{catches}</small></span>'
                        f'</div>'
                    )
                flow_html += '</div>'
                body_parts.append(
                    f'<div class="research-section">'
                    f'<div class="research-section-head">'
                    f'<div class="rs-icon" style="background:rgba(6,182,212,0.1)">{icon}</div>'
                    f'<h3>SDLC Phases</h3></div>'
                    f'{flow_html}</div>'
                )
                continue

            if heading == "Deep Dive: The Three-Agent Ticket Capture Pattern":
                flow_html = (
                    '<div class="research-flow">'
                    '<div class="flow-step"><span class="flow-num blue">1</span>'
                    '<span class="flow-label"><strong>Codebase Agent</strong> <small class="flow-level">read-only</small>'
                    '<small>Explores the relevant codebase — CLAUDE.md, service files, DB schema, recent PRs — and produces an augmented problem outline with a "codebase context" appendix. Crucially, this agent does NOT propose solutions. It maps the terrain so subsequent agents have grounded context without premature implementation bias.</small>'
                    '</span></div>'
                    '<div class="flow-step"><span class="flow-num purple">2</span>'
                    '<span class="flow-label"><strong>Problem Definition Agent</strong> <small class="flow-level">fresh context</small>'
                    '<small>Works from Agent 1\'s markdown output only — deliberately has NO direct codebase access. Generates 10-20 validation questions ranked by ambiguity: scope, constraints, priorities, integration points. Fresh context is the feature — it asks the "dumb questions" insiders skip, surfacing ambiguities that would otherwise become bugs.</small>'
                    '</span></div>'
                    '<div class="flow-step"><span class="flow-num green">3</span>'
                    '<span class="flow-label"><strong>Validation Agent</strong> <small class="flow-level">vision check</small>'
                    '<small>Answers each question using product vision docs, ADRs, and team conventions. Flags questions that can\'t be answered — these become the highest-value items for the human review meeting. Produces a specification readiness score so the team knows exactly how much ambiguity remains.</small>'
                    '</span></div>'
                    '<div class="flow-step"><span class="flow-num amber">→</span>'
                    '<span class="flow-label"><strong>Human Review</strong>'
                    '<small>The spec arrives pre-validated with explicit remaining ambiguities, not unknown unknowns. The product review meeting starts from "here\'s what three independent LLM passes found" rather than raw text. Total time: 5-15 minutes.</small>'
                    '</span></div>'
                    '</div>'
                )
                body_parts.append(
                    f'<div class="research-section">'
                    f'<div class="research-section-head">'
                    f'<div class="rs-icon" style="background:rgba(139,92,246,0.1)">{icon}</div>'
                    f'<h3>Three-Agent Ticket Capture</h3></div>'
                    f'<p>{sec["text"]}</p>'
                    f'{flow_html}</div>'
                )
                continue

            if heading == "Deep Dive: The Tester Agent":
                flow_html = (
                    '<div class="research-flow">'
                    '<div class="flow-step"><span class="flow-num purple">📋</span>'
                    '<span class="flow-label"><strong>Read the specification</strong>'
                    '<small>Ingests the validated spec or acceptance criteria — NOT the implementation code. This is deliberate: tests generated from implementation confirm what the code does, not what it should do. Spec-derived tests catch the gap between intent and reality.</small>'
                    '</span></div>'
                    '<div class="flow-step"><span class="flow-num green">🧪</span>'
                    '<span class="flow-label"><strong>Generate test cases</strong>'
                    '<small>Covers four categories: happy path, edge cases derivable from spec constraints, error conditions implied by requirements, and integration scenarios with adjacent systems. Tests are "free to generate" with LLMs — the cost is a prompt, not an hour of manual work.</small>'
                    '</span></div>'
                    '<div class="flow-step"><span class="flow-num blue">▶️</span>'
                    '<span class="flow-label"><strong>Run tests + coverage report</strong>'
                    '<small>Executes tests against the implementation, identifies gaps where the spec implies behavior that no test covers, and produces a coverage map. QA reviews the report and adds judgment-intensive edge cases — race conditions, adversarial inputs, business-logic corners that require domain expertise.</small>'
                    '</span></div>'
                    '</div>'
                )
                body_parts.append(
                    f'<div class="research-section">'
                    f'<div class="research-section-head">'
                    f'<div class="rs-icon" style="background:rgba(16,185,129,0.1)">{icon}</div>'
                    f'<h3>Tester Agent</h3></div>'
                    f'<p>{sec["text"]}</p>'
                    f'{flow_html}</div>'
                )
                continue

            # Generic section fallback
            bg_colors = {"amber": "rgba(245,158,11,0.1)", "cyan": "rgba(6,182,212,0.1)",
                         "purple": "rgba(139,92,246,0.1)", "green": "rgba(16,185,129,0.1)"}
            body_parts.append(
                f'<div class="research-section">'
                f'<div class="research-section-head">'
                f'<div class="rs-icon" style="background:{bg_colors.get(color, bg_colors["cyan"])}">{icon}</div>'
                f'<h3>{strip_markdown(heading)}</h3></div>'
                f'<p>{sec["text"]}</p></div>'
            )

        source_range = ""
        if r["source_ids"]:
            source_range = f'#{r["source_ids"][0]}–#{r["source_ids"][-1]} ({len(r["source_ids"])} sources)'
        body_parts.append(f'<div class="card-sources">Sources: {source_range}</div>')

        body_html = linkify_sources("\n".join(body_parts))
        subtitle = source_range if source_range else r["date"]

        documents.append({
            "id": r["id"],
            "type": "research",
            "date": r["date"],
            "title": r["title"],
            "subtitle": subtitle,
            "body_html": body_html,
        })

    # Sort newest first
    documents.sort(key=lambda d: d["date"], reverse=True)
    return {"documents": documents}


def md_to_html(text):
    """Simple markdown-to-HTML for source note sections."""
    html_lines = []
    in_list = False
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            continue

        # Headings
        h3 = re.match(r"^###\s+(.+)", stripped)
        if h3:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f'<h4 class="src-h4">{strip_markdown(h3.group(1))}</h4>')
            continue
        h2 = re.match(r"^##\s+(.+)", stripped)
        if h2:
            if in_list:
                html_lines.append("</ul>")
                in_list = False
            html_lines.append(f'<h3 class="src-h3">{strip_markdown(h2.group(1))}</h3>')
            continue

        # Blockquotes
        bq = re.match(r"^>\s*(.*)", stripped)
        if bq:
            html_lines.append(f'<blockquote class="src-quote">{strip_markdown(bq.group(1))}</blockquote>')
            continue

        # List items
        li = re.match(r"^[-*]\s+(.+)", stripped)
        if li:
            if not in_list:
                html_lines.append('<ul class="src-list">')
                in_list = True
            html_lines.append(f"<li>{strip_markdown(li.group(1))}</li>")
            continue

        # Numbered list items
        nli = re.match(r"^\d+\.\s+(.+)", stripped)
        if nli:
            if not in_list:
                html_lines.append('<ul class="src-list">')
                in_list = True
            html_lines.append(f"<li>{strip_markdown(nli.group(1))}</li>")
            continue

        # Paragraph
        if in_list:
            html_lines.append("</ul>")
            in_list = False
        html_lines.append(f"<p>{strip_markdown(stripped)}</p>")

    if in_list:
        html_lines.append("</ul>")
    return "\n".join(html_lines)


def extract_keywords(title):
    """Extract meaningful keywords from a concept title for fuzzy matching."""
    stop = {
        "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
        "of", "with", "by", "from", "as", "is", "was", "are", "be", "been",
        "not", "no", "vs", "how", "why", "what", "when", "its", "it", "this",
        "that", "into", "over", "than", "your", "you", "do", "does",
    }
    words = re.findall(r'[a-z0-9]+', title.lower())
    return {w for w in words if w not in stop and len(w) > 2}


def score_concepts(module_nodes, source_nodes, source_data, edges):
    """Enrich curriculum concepts with strength scores based on source support.

    Formula: strength = support_count * decay_factor * diversity_bonus
    - support_count: distinct sources referencing the concept
    - decay_factor: freshness signal (1.0 if recent, lower if old)
    - diversity_bonus: 1.0 + 0.1*(unique_creators-1), capped at 1.5
    """
    today = datetime.now(timezone.utc).date()

    # Build source lookup: id -> {title_keywords, tags, creator, date, modules}
    source_lookup = {}
    for sn in source_nodes:
        sid = sn["id"]
        title_kw = extract_keywords(sn.get("title", ""))
        tag_kw = {t.replace("-", " ").lower() for t in sn.get("tags", [])}
        # Also extract keywords from tags
        tag_words = set()
        for t in sn.get("tags", []):
            tag_words.update(re.findall(r'[a-z0-9]+', t.lower()))
        source_lookup[sid] = {
            "title_kw": title_kw | tag_words,
            "tags": sn.get("tags", []),
            "creator": sn.get("creator", ""),
            "date": str(sn.get("date", "")),
            "modules": sn.get("modules", []),
        }

    # For each module, get its source IDs from edges
    mod_source_ids = {}
    for e in edges:
        if e["type"] == "curriculum":
            mod_id = e["target"]
            sid = e["source"]
            if mod_id not in mod_source_ids:
                mod_source_ids[mod_id] = set()
            mod_source_ids[mod_id].add(sid)

    for mod in module_nodes:
        if mod["type"] != "module":
            continue
        mod_id = mod["id"]
        mod_sources = mod_source_ids.get(mod_id, set())

        for section in mod.get("sections", []):
            for item in section.get("items", []):
                concept_kw = extract_keywords(item["title"])
                if not concept_kw:
                    item.update({"strength": 0, "classification": "emerging",
                                 "support_count": 0, "creator_count": 0, "last_supported": ""})
                    continue

                # Find supporting sources via two methods:
                # 1. Inline citations [#NNN] from curriculum text (high confidence)
                # 2. Keyword matching against source titles/tags (supplementary)
                cited_ids = set(item.get("cited_sources", []))
                supporting_ids = set()

                # Method 1: cited sources (always counted)
                for sid in cited_ids:
                    if sid in source_lookup:
                        supporting_ids.add(sid)

                # Method 2: keyword matching (supplementary, within module)
                for sid in mod_sources:
                    if sid in supporting_ids:
                        continue
                    sl = source_lookup.get(sid)
                    if not sl:
                        continue
                    overlap = concept_kw & sl["title_kw"]
                    threshold = 1 if len(concept_kw) <= 3 else 2
                    if len(overlap) >= threshold:
                        supporting_ids.add(sid)

                supporting = [source_lookup[sid] for sid in supporting_ids if sid in source_lookup]

                support_count = len(supporting)
                if support_count == 0:
                    item.update({"strength": 0, "classification": "emerging",
                                 "support_count": 0, "creator_count": 0, "last_supported": ""})
                    continue

                # Decay factor based on most recent supporting source
                dates = []
                for sl in supporting:
                    try:
                        d = datetime.strptime(sl["date"][:10], "%Y-%m-%d").date()
                        dates.append(d)
                    except (ValueError, IndexError):
                        pass

                if dates:
                    most_recent = max(dates)
                    age_days = (today - most_recent).days
                    if age_days < 90:
                        decay = 1.0
                    elif age_days < 180:
                        decay = 0.85
                    elif age_days < 365:
                        decay = 0.7
                    else:
                        decay = 0.5
                    last_supported = most_recent.isoformat()
                else:
                    decay = 0.5
                    last_supported = ""

                # Diversity bonus
                creators = {sl["creator"] for sl in supporting if sl["creator"]}
                creator_count = len(creators)
                diversity = min(1.0 + 0.1 * (creator_count - 1), 1.5)

                strength = round(support_count * decay * diversity, 2)

                if strength >= 5.0:
                    classification = "evergreen"
                elif strength >= 2.0:
                    classification = "established"
                elif strength >= 1.0:
                    classification = "emerging"
                else:
                    classification = "stale"

                item.update({
                    "strength": strength,
                    "classification": classification,
                    "support_count": support_count,
                    "creator_count": creator_count,
                    "last_supported": last_supported,
                })


def build():
    source_nodes, source_data = parse_sources()
    module_nodes = parse_curriculum()
    synthesis = parse_synthesis()
    briefings = parse_briefings()
    research = parse_research()
    reader = build_reader_content(briefings, synthesis, research)

    # Build tag nodes with counts
    tag_counts = {}
    for data in source_data.values():
        for tag in data["tags"]:
            tag_counts[tag] = tag_counts.get(tag, 0) + 1

    tag_nodes = [
        {"id": f"tag:{tag}", "type": "tag", "label": tag, "count": count}
        for tag, count in sorted(tag_counts.items())
    ]

    nodes = source_nodes + tag_nodes + module_nodes
    node_ids = {n["id"] for n in nodes}

    # Build edges (skip any that reference non-existent nodes)
    edges = []
    for sid, data in source_data.items():
        for rid in data["related_ids"]:
            if rid in node_ids:
                edges.append({"source": sid, "target": rid, "type": "related"})
        for tag in data["tags"]:
            edges.append({"source": sid, "target": f"tag:{tag}", "type": "tag"})
        for mod in data["modules"]:
            target = f"mod:{mod}"
            if target in node_ids:
                edges.append({"source": sid, "target": target, "type": "curriculum"})
            else:
                print(f"  Warning: source {sid} references unknown module '{mod}'")

    # Score curriculum concepts by source support
    score_concepts(module_nodes, source_nodes, source_data, edges)

    result = {
        "nodes": nodes,
        "edges": edges,
        "synthesis": synthesis,
        "briefings": briefings,
        "reader": reader,
        "meta": {
            "generated": datetime.now(timezone.utc).isoformat(),
            "source_count": len(source_nodes),
            "tag_count": len(tag_nodes),
            "briefing_count": len(briefings),
        },
    }

    OUTPUT.write_text(json.dumps(result, indent=2, default=str))
    print(f"Wrote {OUTPUT}")
    print(f"  Sources: {len(source_nodes)}")
    print(f"  Tags: {len(tag_nodes)}")
    print(f"  Modules: {len(module_nodes)}")
    print(f"  Edges: {len(edges)}")
    print(f"  Synthesis: {len(synthesis)}")
    print(f"  Briefings: {len(briefings)}")
    print(f"  Research: {len(research)}")
    print(f"  Reader docs: {len(reader['documents'])}")


if __name__ == "__main__":
    build()

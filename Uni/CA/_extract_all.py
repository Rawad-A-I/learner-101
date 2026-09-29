"""Extract CA lecture PDFs into chapter-separated workable artifacts."""
from __future__ import annotations

import json
import re
from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "artifacts"

PDFS = [
    {
        "path": ROOT / "Chapter 1 - Basic Concepts & Computer Evolution (1).pdf",
        "slug": "chapter-01-basic-concepts-computer-evolution",
        "number": 1,
        "title": "Basic Concepts & Computer Evolution",
    },
    {
        "path": ROOT / "Chapter 2 - Performance Issues (1).pdf",
        "slug": "chapter-02-performance-issues",
        "number": 2,
        "title": "Performance Issues",
    },
    {
        "path": ROOT
        / "Chapter 3 - Top Level View of Function and Interconnnection.pdf",
        "slug": "chapter-03-top-level-view-function-interconnection",
        "number": 3,
        "title": "A Top-Level View of Computer Function and Interconnection",
    },
]

# Common PowerPoint / Wingdings bullet and whitespace cleanup
BULLET_CHARS = "\uf0a7\uf0b7\u2022\u25cf\u25a0\u25aa\u25e6\u2043•▪●○■□–—"
WS_RE = re.compile(r"[ \t]+")
MULTI_NL = re.compile(r"\n{3,}")


def clean_text(text: str) -> str:
    for ch in BULLET_CHARS:
        text = text.replace(ch, "-")
    # normalize weird dashes / quotes
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    text = text.replace("\u2013", "-").replace("\u2014", "-")
    text = text.replace("\xa0", " ")
    lines = []
    for ln in text.splitlines():
        ln = WS_RE.sub(" ", ln).strip()
        if ln:
            lines.append(ln)
    return "\n".join(lines)


def slide_title(lines: list[str], page_num: int) -> str:
    if not lines:
        return f"Slide {page_num} (figure)"
    for ln in lines[:6]:
        if re.fullmatch(r"\d{1,3}", ln):
            continue
        if re.fullmatch(r"Chapter\s+\d+", ln, re.I):
            continue
        if len(ln) >= 2:
            return ln[:120]
    return f"Slide {page_num} (figure)"


def lines_to_markdown_body(lines: list[str], title: str) -> str:
    """Turn slide lines into markdown bullets / paragraphs."""
    remaining = list(lines)
    # Drop leading page number
    if remaining and re.fullmatch(r"\d{1,3}", remaining[0]):
        remaining = remaining[1:]
    # Drop first occurrence of the slide title
    if remaining and remaining[0] == title:
        remaining = remaining[1:]
    elif title in remaining:
        remaining.remove(title)

    body_lines: list[str] = []
    for ln in remaining:
        if not ln or re.fullmatch(r"\d{1,3}", ln):
            continue
        if ln in ("-", "•"):
            continue
        if ln.startswith("-"):
            content = ln.lstrip("- ").strip()
            if not content:
                continue
            body_lines.append(f"- {content}")
        elif ln.endswith(":") and len(ln) < 80:
            body_lines.append(f"\n**{ln}**")
        else:
            body_lines.append(f"- {ln}")
    text = "\n".join(body_lines).strip()
    text = MULTI_NL.sub("\n\n", text)
    return text

def extract_chapter(meta: dict) -> dict:
    pdf_path: Path = meta["path"]
    slug = meta["slug"]
    chap_dir = OUT / slug
    slides_dir = chap_dir / "slides"
    images_dir = chap_dir / "images"
    slides_dir.mkdir(parents=True, exist_ok=True)
    images_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)
    slides = []
    image_manifest = []

    chapter_md_parts = [
        f"# Chapter {meta['number']}: {meta['title']}",
        "",
        f"**Source:** `{pdf_path.name}`  ",
        f"**Pages / slides:** {doc.page_count}  ",
        f"**Based on:** William Stallings, *Computer Organization and Architecture*",
        "",
        "---",
        "",
        "## Slide index",
        "",
    ]

    index_rows = []

    for i, page in enumerate(doc):
        page_num = i + 1
        raw = page.get_text()
        cleaned = clean_text(raw)
        lines = cleaned.splitlines() if cleaned else []
        title = slide_title(lines, page_num)
        body = lines_to_markdown_body(lines, title)

        # Images on this page
        page_images = []
        for img_idx, img in enumerate(page.get_images(full=True), start=1):
            xref = img[0]
            try:
                pix = fitz.Pixmap(doc, xref)
                if pix.n - pix.alpha > 3:  # CMYK
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                # Skip tiny decorative icons
                if pix.width < 40 or pix.height < 40:
                    continue
                img_name = f"slide-{page_num:02d}-img-{img_idx:02d}.png"
                img_path = images_dir / img_name
                pix.save(img_path.as_posix())
                rel = f"images/{img_name}"
                page_images.append(
                    {
                        "file": rel,
                        "width": pix.width,
                        "height": pix.height,
                    }
                )
                image_manifest.append(
                    {
                        "slide": page_num,
                        "file": rel,
                        "width": pix.width,
                        "height": pix.height,
                    }
                )
            except Exception as e:
                image_manifest.append(
                    {"slide": page_num, "error": str(e), "xref": xref}
                )

        slide_md = [
            f"# Slide {page_num}: {title}",
            "",
            f"*Chapter {meta['number']} — {meta['title']}*",
            "",
        ]
        if body:
            slide_md.append(body)
            slide_md.append("")
        if page_images:
            slide_md.append("### Figures")
            slide_md.append("")
            for im in page_images:
                slide_md.append(f"![slide {page_num} figure](../{im['file']})")
                slide_md.append("")

        slide_file = slides_dir / f"slide-{page_num:02d}.md"
        slide_file.write_text("\n".join(slide_md).strip() + "\n", encoding="utf-8")

        slides.append(
            {
                "page": page_num,
                "title": title,
                "text": cleaned,
                "body_markdown": body,
                "images": page_images,
                "slide_file": f"slides/slide-{page_num:02d}.md",
            }
        )

        # Anchor-safe slug for index
        anchor = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60]
        index_rows.append(f"{page_num}. [{title}](#{page_num:02d}-{anchor})")

        chapter_md_parts.append(f"### {page_num:02d}. {title} {{#{page_num:02d}-{anchor}}}")
        chapter_md_parts.append("")
        if body:
            chapter_md_parts.append(body)
            chapter_md_parts.append("")
        if page_images:
            for im in page_images:
                chapter_md_parts.append(f"![slide {page_num} figure]({im['file']})")
                chapter_md_parts.append("")
        chapter_md_parts.append(f"*Per-slide file:* [`slides/slide-{page_num:02d}.md`](slides/slide-{page_num:02d}.md)")
        chapter_md_parts.append("")
        chapter_md_parts.append("---")
        chapter_md_parts.append("")

    # Insert index after the "## Slide index" header
    # Rebuild with index in the right place
    header = [
        f"# Chapter {meta['number']}: {meta['title']}",
        "",
        f"**Source:** `{pdf_path.name}`  ",
        f"**Pages / slides:** {doc.page_count}  ",
        f"**Based on:** William Stallings, *Computer Organization and Architecture*",
        "",
        "---",
        "",
        "## Slide index",
        "",
        *index_rows,
        "",
        "---",
        "",
    ]
    # body starts after first "---" block in chapter_md_parts — easier to rebuild from slides
    body_parts = []
    for s in slides:
        title = s["title"]
        page_num = s["page"]
        anchor = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60]
        body_parts.append(f"## {page_num:02d}. {title} {{#{page_num:02d}-{anchor}}}")
        body_parts.append("")
        if s["body_markdown"]:
            body_parts.append(s["body_markdown"])
            body_parts.append("")
        if s["images"]:
            for im in s["images"]:
                body_parts.append(f"![slide {page_num} figure]({im['file']})")
                body_parts.append("")
        body_parts.append(
            f"*Per-slide:* [`{s['slide_file']}`]({s['slide_file']})"
        )
        body_parts.append("")
        body_parts.append("---")
        body_parts.append("")

    chapter_md = "\n".join(header + body_parts).strip() + "\n"
    (chap_dir / "CHAPTER.md").write_text(chapter_md, encoding="utf-8")

    # Plain text dump (searchable / pasteable)
    plain_parts = [f"CHAPTER {meta['number']}: {meta['title']}", "=" * 60, ""]
    for s in slides:
        plain_parts.append(f"--- SLIDE {s['page']}: {s['title']} ---")
        plain_parts.append(s["text"])
        plain_parts.append("")
    (chap_dir / "CHAPTER.txt").write_text("\n".join(plain_parts), encoding="utf-8")

    # Structured JSON
    payload = {
        "chapter": meta["number"],
        "title": meta["title"],
        "slug": slug,
        "source_pdf": pdf_path.name,
        "page_count": doc.page_count,
        "slides": slides,
        "images": image_manifest,
    }
    (chap_dir / "chapter.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # Key-terms / headings list for study
    terms = []
    for s in slides:
        terms.append({"slide": s["page"], "heading": s["title"]})
    (chap_dir / "outline.json").write_text(
        json.dumps(terms, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    doc.close()
    return {
        "chapter": meta["number"],
        "title": meta["title"],
        "slug": slug,
        "pages": len(slides),
        "images": len(image_manifest),
        "dir": str(chap_dir.relative_to(ROOT)),
    }


def main() -> None:
    OUT.mkdir(exist_ok=True)
    summaries = []
    for meta in PDFS:
        if not meta["path"].exists():
            raise SystemExit(f"Missing PDF: {meta['path']}")
        print(f"Extracting: {meta['path'].name}")
        summaries.append(extract_chapter(meta))

    # Root index
    index_lines = [
        "# Computer Architecture — Extracted Artifacts",
        "",
        "Lecture slides extracted from course PDFs (Stallings-based), separated by chapter.",
        "",
        "## Chapters",
        "",
    ]
    for s in summaries:
        rel = Path(s["dir"]).name  # chapter folder only; README lives in artifacts/
        index_lines.append(
            f"- **Chapter {s['chapter']}: {s['title']}** — "
            f"[{rel}/CHAPTER.md]({rel}/CHAPTER.md) "
            f"({s['pages']} slides, {s['images']} images)"
        )
    index_lines += [
        "",
        "## Per-chapter layout",
        "",
        "```",
        "artifacts/chapter-XX-.../",
        "  CHAPTER.md      # full chapter notes (all slides)",
        "  CHAPTER.txt     # plain-text dump",
        "  chapter.json    # structured slide data",
        "  outline.json    # slide headings only",
        "  slides/         # one markdown file per slide",
        "  images/         # extracted figures",
        "```",
        "",
    ]
    (OUT / "README.md").write_text("\n".join(index_lines), encoding="utf-8")

    summary_path = OUT / "_extraction_summary.json"
    summary_path.write_text(
        json.dumps(summaries, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(summaries, indent=2))


if __name__ == "__main__":
    main()

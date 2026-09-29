#!/usr/bin/env python3
"""Extract ELE442 PPTX decks into agentic-parsable JSONL/YAML artifacts via OOXML."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
M_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"

NS = {"a": A_NS, "p": P_NS, "r": R_NS, "pr": REL_NS, "m": M_NS}

ROOT = Path(__file__).resolve().parents[2]
ARTIFACTS = ROOT / "artifacts"

TOPIC_MAP = {
    "ELE442_Topic1_Introduction.pptx": {
        "topic": 1,
        "slug": "01-ELE442_Topic1_Introduction",
        "title": "Introduction",
    },
    "ELE442_Topic2_Mathematical_Models_Laplace_Transform (2).pptx": {
        "topic": 2,
        "slug": "02-ELE442_Topic2_Mathematical_Models_Laplace",
        "title": "Mathematical Models & Laplace Transform",
    },
    "ELE442_Topic3_Transfer_Functions_and_Block_Diagrams (1).pptx": {
        "topic": 3,
        "slug": "03-ELE442_Topic3_Transfer_Functions_Block_Diagrams",
        "title": "Transfer Functions & Block Diagrams",
    },
}

DECKS_ROOT = ARTIFACTS / "decks"


def q(tag: str, ns: str) -> str:
    return f"{{{ns}}}{tag}"


def local(tag: str) -> str:
    return tag.split("}")[-1] if "}" in tag else tag


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def slide_num(name: str) -> int:
    m = re.search(r"slide(\d+)\.xml$", name)
    return int(m.group(1)) if m else 0


def notes_num(name: str) -> int:
    m = re.search(r"notesSlide(\d+)\.xml$", name)
    return int(m.group(1)) if m else 0


def text_runs(root: ET.Element) -> list[str]:
    out: list[str] = []
    for t in root.iter(q("t", A_NS)):
        if t.text is not None and t.text != "":
            out.append(t.text)
        if t.tail and t.tail.strip():
            out.append(t.tail)
    return out


def join_runs(runs: list[str]) -> str:
    if not runs:
        return ""
    s = runs[0]
    for r in runs[1:]:
        if not r:
            continue
        if s and r and (s[-1].isalnum() and r[0].isalnum()):
            s += " " + r
        else:
            s += r
    return re.sub(r"[ \t]+", " ", s).strip()


def _omml_child(el: ET.Element, name: str) -> ET.Element | None:
    return el.find(q(name, M_NS))


def omml_to_text(el: ET.Element) -> str:
    """Best-effort linearization of Office Math ML into readable text."""
    tag = local(el.tag)

    if tag == "t":
        return el.text or ""

    if tag == "f":  # fraction
        num = _omml_child(el, "num")
        den = _omml_child(el, "den")
        return f"({omml_to_text(num) if num is not None else ''})/({omml_to_text(den) if den is not None else ''})"

    if tag in {"sSup", "sSubSup"}:
        base = _omml_child(el, "e")
        sup = _omml_child(el, "sup")
        sub = _omml_child(el, "sub")
        s = omml_to_text(base) if base is not None else ""
        if sub is not None:
            s += f"_{{{omml_to_text(sub)}}}"
        if sup is not None:
            s += f"^{{{omml_to_text(sup)}}}"
        return s

    if tag == "sSub":
        base = _omml_child(el, "e")
        sub = _omml_child(el, "sub")
        s = omml_to_text(base) if base is not None else ""
        if sub is not None:
            s += f"_{{{omml_to_text(sub)}}}"
        return s

    if tag == "rad":  # radical
        deg = _omml_child(el, "deg")
        e = _omml_child(el, "e")
        body = omml_to_text(e) if e is not None else ""
        if deg is not None and omml_to_text(deg).strip():
            return f"root[{omml_to_text(deg)}]({body})"
        return f"sqrt({body})"

    if tag == "nary":
        narypr = _omml_child(el, "naryPr")
        ch = "∫"
        if narypr is not None:
            ch_el = _omml_child(narypr, "chr")
            if ch_el is not None and ch_el.get(q("val", M_NS)):
                ch = ch_el.get(q("val", M_NS))
        sub = _omml_child(el, "sub")
        sup = _omml_child(el, "sup")
        e = _omml_child(el, "e")
        s = ch
        if sub is not None:
            s += f"_{{{omml_to_text(sub)}}}"
        if sup is not None:
            s += f"^{{{omml_to_text(sup)}}}"
        s += f"({omml_to_text(e) if e is not None else ''})"
        return s

    if tag == "d":  # delimiter
        e = _omml_child(el, "e")
        return f"({omml_to_text(e) if e is not None else ''})"

    if tag == "func":
        fname = _omml_child(el, "fName")
        e = _omml_child(el, "e")
        return f"{omml_to_text(fname) if fname is not None else ''}({omml_to_text(e) if e is not None else ''})"

    if tag in {"acc", "bar", "groupChr", "borderBox", "box"}:
        e = _omml_child(el, "e")
        return omml_to_text(e) if e is not None else ""

    if tag == "eqArr":
        parts = [_omml_to_text_children(c) for c in el if local(c.tag) == "e"]
        return " ; ".join(p for p in parts if p)

    # Generic: concatenate math children / text
    return _omml_to_text_children(el)


def _omml_to_text_children(el: ET.Element | None) -> str:
    if el is None:
        return ""
    parts: list[str] = []
    if el.text and el.text.strip() and local(el.tag) != "t":
        # structural nodes rarely have meaningful direct text
        pass
    for child in list(el):
        parts.append(omml_to_text(child))
        if child.tail and child.tail.strip():
            parts.append(child.tail)
    if local(el.tag) == "t":
        return el.text or ""
    return "".join(parts)


def extract_omml_equations(root: ET.Element) -> list[str]:
    eqs: list[str] = []
    for node in root.iter():
        if local(node.tag) != "oMath":
            continue
        text = omml_to_text(node)
        text = re.sub(r"\s+", " ", text).strip()
        text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        if text and text not in eqs:
            eqs.append(text)
    return eqs


def is_page_number(line: str) -> bool:
    return bool(re.fullmatch(r"\d{1,3}", line.strip()))


def paragraph_texts(root: ET.Element) -> list[str]:
    paras: list[str] = []
    for p in root.iter(q("p", A_NS)):
        # Include OMML embedded in the paragraph inline
        chunks: list[str] = []
        for node in p:
            lname = local(node.tag)
            if lname == "r":
                for t in node.iter(q("t", A_NS)):
                    if t.text is not None:
                        chunks.append(t.text)
            elif lname in {"oMath", "oMathPara"} or node.tag.startswith("{" + M_NS):
                # math run inside paragraph — handled via extract_omml separately;
                # also splice a readable form into body flow
                mt = omml_to_text(node)
                if mt.strip():
                    chunks.append(mt.strip())
            else:
                for t in node.iter(q("t", A_NS)):
                    if t.text is not None:
                        chunks.append(t.text)
                for m in node.iter():
                    if local(m.tag) in {"oMath", "oMathPara"}:
                        mt = omml_to_text(m)
                        if mt.strip():
                            chunks.append(mt.strip())
        # Fallback: classic a:t only if nothing gathered
        if not chunks:
            for t in p.iter(q("t", A_NS)):
                if t.text is not None:
                    chunks.append(t.text)
        line = join_runs(chunks)
        if line and not is_page_number(line):
            paras.append(line)
    return paras


def extract_tables(root: ET.Element) -> list[dict]:
    tables = []
    for tbl in root.iter(q("tbl", A_NS)):
        rows = []
        for tr in tbl.findall(f".//{q('tr', A_NS)}"):
            cells = []
            for tc in tr.findall(f"./{q('tc', A_NS)}"):
                cells.append(join_runs(text_runs(tc)))
            if any(c.strip() for c in cells):
                rows.append(cells)
        if rows:
            tables.append({"rows": rows})
    return tables


def classify_tags(title: str, body: list[str], has_media: bool, has_table: bool) -> list[str]:
    blob = " ".join([title] + body).lower()
    tags: list[str] = []
    rules = [
        ("definition", r"\b(definition|defined as|is defined|what is)\b"),
        ("example", r"\b(example|e\.g\.|for instance|illustration)\b"),
        ("derivation", r"\b(derive|derivation|proof|obtain|taking laplace)\b"),
        ("formula", r"\b(equation|transfer function|laplace|g\(s\)|tf)\b|[/=].*[sS]\b"),
        ("procedure", r"\b(steps?|procedure|algorithm|how to|method)\b"),
        ("property", r"\b(propert|theorem|identity|linearity|final value)\b"),
        ("diagram", r"\b(block diagram|signal flow|schematic|figure)\b"),
        ("comparison", r"\b(open[- ]loop|closed[- ]loop|vs\.|versus|compare)\b"),
        ("history", r"\b(history|historical|century|invent)\b"),
        ("objectives", r"\b(objective|learning outcome|outline|agenda)\b"),
    ]
    for tag, pat in rules:
        if re.search(pat, blob, re.I):
            tags.append(tag)
    if has_media and "diagram" not in tags:
        tags.append("figure")
    if has_table:
        tags.append("table")
    if not tags:
        tags.append("content")
    return tags


def equationish(lines: list[str]) -> list[str]:
    eqs = []
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if re.search(
            r"(=|≈|≤|≥|∝|→|⇒|∫|∑|√|∂|ℒ|L\{|G\(s\)|H\(s\)|C\(s\)|R\(s\)|Y\(s\)|U\(s\)|"
            r"\\frac|s\^|e\^\{|/s\b|\bs\b.*\b[a-zA-Z]\()",
            s,
        ):
            eqs.append(s)
        elif re.search(r"[A-Za-z]\([st]\)\s*=", s):
            eqs.append(s)
        elif re.search(r"\d+\s*/\s*\([^)]*s", s):
            eqs.append(s)
    return eqs


def parse_rels(z: ZipFile, rels_path: str) -> dict[str, str]:
    if rels_path not in z.namelist():
        return {}
    root = ET.fromstring(z.read(rels_path))
    out = {}
    for rel in root:
        if local(rel.tag) != "Relationship":
            continue
        rid = rel.attrib.get("Id")
        target = rel.attrib.get("Target", "")
        if rid:
            out[rid] = target
    return out


def resolve_target(slide_path: str, target: str) -> str:
    # slide_path like ppt/slides/slide1.xml ; targets are relative
    base = Path(slide_path).parent  # ppt/slides
    # normalize ../media/foo.png
    parts = list(base.parts)
    for part in Path(target).parts:
        if part == "..":
            if parts:
                parts.pop()
        else:
            parts.append(part)
    return "/".join(parts).replace("\\", "/")


def extract_media_refs(root: ET.Element, rels: dict[str, str], slide_path: str) -> list[str]:
    refs = []
    for el in root.iter():
        rid = el.attrib.get(q("embed", R_NS)) or el.attrib.get(q("link", R_NS))
        if not rid:
            continue
        target = rels.get(rid)
        if not target:
            continue
        full = resolve_target(slide_path, target)
        if "/media/" in full or full.startswith("ppt/media/"):
            refs.append(full)
    # unique preserve order
    seen = set()
    out = []
    for r in refs:
        if r not in seen:
            seen.add(r)
            out.append(r)
    return out


def notes_body_paras(root: ET.Element) -> list[str]:
    """Speaker notes live in the notes body shape; fall back to all paragraphs."""
    paras = paragraph_texts(root)
    # Drop common placeholders that are just slide titles duplicated briefly
    return [p for p in paras if p.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def write_yaml_simple(path: Path, data: dict) -> None:
    """Minimal YAML writer (no pyyaml dependency)."""

    def dump(obj, indent=0):
        sp = "  " * indent
        lines = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    lines.append(f"{sp}{k}:")
                    lines.append(dump(v, indent + 1))
                else:
                    lines.append(f"{sp}{k}: {json.dumps(v, ensure_ascii=False)}")
        elif isinstance(obj, list):
            for item in obj:
                if isinstance(item, (dict, list)):
                    lines.append(f"{sp}-")
                    # indent dict keys under list item
                    sub = dump(item, indent + 1)
                    # convert first-level keys to list-item style
                    lines.append(sub)
                else:
                    lines.append(f"{sp}- {json.dumps(item, ensure_ascii=False)}")
        else:
            lines.append(f"{sp}{json.dumps(obj, ensure_ascii=False)}")
        return "\n".join(lines)

    path.write_text(dump(data) + "\n", encoding="utf-8")


def extract_deck(pptx_path: Path, meta: dict) -> dict:
    topic = meta["topic"]
    slug = meta["slug"]
    out_dir = DECKS_ROOT / slug
    media_dir = out_dir / "media"
    media_dir.mkdir(parents=True, exist_ok=True)

    slides_out: list[dict] = []
    notes_out: list[dict] = []
    media_inv: list[dict] = []
    completeness = {
        "empty_text_slides": [],
        "figure_only_slides": [],
        "notes_without_slide_match": [],
        "slides_with_notes": [],
        "slides_without_notes": [],
    }

    with ZipFile(pptx_path) as z:
        names = z.namelist()
        slide_files = sorted(
            [n for n in names if re.match(r"ppt/slides/slide\d+\.xml$", n)],
            key=slide_num,
        )
        # Extract all media binaries once
        media_files = [n for n in names if n.startswith("ppt/media/")]
        media_local = {}
        for mf in media_files:
            dest_name = Path(mf).name
            dest = media_dir / dest_name
            with z.open(mf) as src, dest.open("wb") as dst:
                shutil.copyfileobj(src, dst)
            media_local[mf] = f"media/{dest_name}"

        # Build slide -> notes via relationships
        slide_to_notes: dict[int, str] = {}
        for sf in slide_files:
            sn = slide_num(sf)
            rels_path = f"ppt/slides/_rels/slide{sn}.xml.rels"
            rels = parse_rels(z, rels_path)
            for target in rels.values():
                if "notesSlide" in target:
                    # target like ../notesSlides/notesSlide3.xml
                    nn = notes_num(target.replace("\\", "/"))
                    notes_xml = f"ppt/notesSlides/notesSlide{nn}.xml"
                    if notes_xml in names:
                        slide_to_notes[sn] = notes_xml

        for sf in slide_files:
            sn = slide_num(sf)
            sid = f"t{topic:02d}-s{sn:03d}"
            root = ET.fromstring(z.read(sf))
            paras = paragraph_texts(root)
            tables = extract_tables(root)
            omml_eqs = extract_omml_equations(root)
            rels = parse_rels(z, f"ppt/slides/_rels/slide{sn}.xml.rels")
            media_refs_full = extract_media_refs(root, rels, sf)
            media_refs = [media_local.get(m, m) for m in media_refs_full]

            title = paras[0] if paras else ""
            body = paras[1:] if len(paras) > 1 else []
            # Prefer short title: if first para very long, keep as body lead
            if len(title) > 120 and body:
                body = [title] + body
                title = f"(untitled slide {sn})"

            notes_id = None
            notes_paras: list[str] = []
            if sn in slide_to_notes:
                nxml = slide_to_notes[sn]
                nroot = ET.fromstring(z.read(nxml))
                notes_paras = [p for p in notes_body_paras(nroot) if not is_page_number(p)]
                # Drop notes that are empty / only whitespace after filter
                notes_paras = [p for p in notes_paras if p.strip()]
                notes_id = f"t{topic:02d}-n{sn:03d}"
                notes_out.append(
                    {
                        "id": notes_id,
                        "slide_id": sid,
                        "topic": topic,
                        "slide": sn,
                        "paras": notes_paras,
                        "text": "\n".join(notes_paras),
                        "omml_equations": extract_omml_equations(nroot),
                        "source": {"file": pptx_path.name, "notes_xml": nxml},
                    }
                )
                completeness["slides_with_notes"].append(sid)
            else:
                completeness["slides_without_notes"].append(sid)

            tags = classify_tags(title, body + notes_paras + omml_eqs, bool(media_refs), bool(tables))
            eqs = omml_eqs + [e for e in equationish(paras + notes_paras) if e not in omml_eqs]

            record = {
                "id": sid,
                "topic": topic,
                "slide": sn,
                "title": title,
                "bullets": body,
                "body_text": paras,
                "tables": tables,
                "equations_raw": eqs,
                "omml_equations": omml_eqs,
                "media_refs": media_refs,
                "notes_id": notes_id,
                "has_notes": notes_id is not None,
                "tags": tags,
                "source": {
                    "file": pptx_path.name,
                    "slide_xml": sf,
                },
            }
            slides_out.append(record)

            if not paras:
                completeness["empty_text_slides"].append(sid)
                if media_refs:
                    completeness["figure_only_slides"].append(sid)
            elif not paras and not media_refs and not tables:
                completeness["empty_text_slides"].append(sid)

            for mref, mfull in zip(media_refs, media_refs_full):
                media_inv.append(
                    {
                        "slide_id": sid,
                        "topic": topic,
                        "slide": sn,
                        "path": mref,
                        "pptx_path": mfull,
                        "role": "figure",
                        "ext": Path(mref).suffix.lower(),
                    }
                )

        # notes slides that exist but weren't linked
        all_notes = {
            n
            for n in names
            if re.match(r"ppt/notesSlides/notesSlide\d+\.xml$", n)
        }
        linked = set(slide_to_notes.values())
        for orphan in sorted(all_notes - linked, key=notes_num):
            completeness["notes_without_slide_match"].append(orphan)

    write_jsonl(out_dir / "slides.jsonl", slides_out)
    write_jsonl(out_dir / "notes.jsonl", notes_out)
    write_jsonl(out_dir / "media" / "inventory.jsonl", media_inv)

    deck_meta = {
        "topic": topic,
        "slug": slug,
        "title": meta["title"],
        "source_file": pptx_path.name,
        "artifact_path": f"decks/{slug}",
        "source_sha256": sha256_file(pptx_path),
        "source_bytes": pptx_path.stat().st_size,
        "slide_count": len(slides_out),
        "notes_count": len(notes_out),
        "media_count": len(media_inv),
        "unique_media_files": len({m["path"] for m in media_inv}),
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "completeness": {
            "empty_text_slides": completeness["empty_text_slides"],
            "figure_only_slides": completeness["figure_only_slides"],
            "notes_without_slide_match": completeness["notes_without_slide_match"],
            "slides_with_notes_count": len(completeness["slides_with_notes"]),
            "slides_without_notes_count": len(completeness["slides_without_notes"]),
        },
    }
    write_yaml_simple(out_dir / "deck.meta.yaml", deck_meta)
    return {
        "meta": deck_meta,
        "slides": slides_out,
        "notes": notes_out,
        "media": media_inv,
        "completeness_detail": completeness,
    }


def synthesize_knowledge(topic_data: dict) -> str:
    meta = topic_data["meta"]
    slides = topic_data["slides"]
    notes_by_slide = {n["slide_id"]: n for n in topic_data["notes"]}

    lines = [
        f"# Topic {meta['topic']}: {meta['title']}",
        "",
        f"Source: `{meta['source_file']}`",
        f"Slides: {meta['slide_count']} · Notes: {meta['notes_count']} · Media refs: {meta['media_count']}",
        "",
        "## Learning map",
        "",
    ]

    # Group by first meaningful tag
    by_tag: dict[str, list] = defaultdict(list)
    for s in slides:
        primary = s["tags"][0] if s["tags"] else "content"
        by_tag[primary].append(s["id"])
    for tag, ids in sorted(by_tag.items(), key=lambda x: -len(x[1])):
        lines.append(f"- **{tag}**: {len(ids)} slides")
    lines.append("")

    lines.append("## Slide knowledge cards")
    lines.append("")

    for s in slides:
        lines.append(f"### {s['id']} — {s['title']}")
        lines.append("")
        if s["tags"]:
            lines.append(f"Tags: {', '.join(s['tags'])}")
            lines.append("")
        if s["body_text"]:
            lines.append("Content:")
            for p in s["body_text"]:
                lines.append(f"- {p}")
            lines.append("")
        if s["tables"]:
            lines.append("Tables:")
            for ti, tbl in enumerate(s["tables"], 1):
                lines.append(f"- Table {ti}:")
                for row in tbl["rows"]:
                    lines.append(f"  - {' | '.join(row)}")
            lines.append("")
        if s["equations_raw"]:
            lines.append("Equations / relations:")
            for eq in s["equations_raw"]:
                lines.append(f"- `{eq}`")
            lines.append("")
        elif s.get("omml_equations"):
            lines.append("OMML equations:")
            for eq in s["omml_equations"]:
                lines.append(f"- `{eq}`")
            lines.append("")
        if s["media_refs"]:
            lines.append("Media:")
            for m in s["media_refs"]:
                lines.append(f"- `{m}`")
            lines.append("")
        note = notes_by_slide.get(s["id"])
        if note and note["paras"]:
            lines.append("Speaker notes:")
            for p in note["paras"]:
                lines.append(f"- {p}")
            lines.append("")
        lines.append("---")
        lines.append("")

    # Compact formula index for this topic
    lines.append("## Formula index (this topic)")
    lines.append("")
    seen = set()
    for s in slides:
        for eq in s["equations_raw"]:
            key = eq.strip()
            if key in seen:
                continue
            seen.add(key)
            lines.append(f"- `{key}` ← {s['id']}")
    if not seen:
        lines.append("- _(none detected)_")
    lines.append("")
    return "\n".join(lines)


def build_indexes_for_deck(topic_data: dict, out_dir: Path) -> None:
    concepts = []
    formulas = []
    glossary = []

    concept_patterns = [
        (r"\bopen[- ]loop\b", "open-loop control"),
        (r"\bclosed[- ]loop\b", "closed-loop control"),
        (r"\bfeedback\b", "feedback"),
        (r"\bplant\b|\bprocess\b", "plant/process"),
        (r"\bactuator\b", "actuator"),
        (r"\bsensor\b|\btransducer\b", "sensor/transducer"),
        (r"\bcontroller\b", "controller"),
        (r"\breference\b|\bset[- ]?point\b", "reference/setpoint"),
        (r"\bdisturbance\b", "disturbance"),
        (r"\berror\b", "error signal"),
        (r"\blaplace\b", "Laplace transform"),
        (r"\btransfer function\b|\b\bTF\b", "transfer function"),
        (r"\bblock diagram\b", "block diagram"),
        (r"\bpole\b", "poles"),
        (r"\bzero\b", "zeros"),
        (r"\bstability\b", "stability"),
        (r"\btransient\b", "transient response"),
        (r"\bsteady[- ]state\b", "steady-state"),
        (r"\bconvolution\b", "convolution"),
        (r"\bimpulse response\b", "impulse response"),
        (r"\bstep response\b", "step response"),
        (r"\blinearity\b|\blinear\b", "linearity / LTI"),
        (r"\btime[- ]invariant\b|\bLTI\b", "time-invariance / LTI"),
        (r"\bpartial fraction\b", "partial fractions"),
        (r"\bfinal value theorem\b", "final value theorem"),
        (r"\binitial value theorem\b", "initial value theorem"),
        (r"\bsignal flow\b", "signal flow graph"),
        (r"\bMason\b", "Mason's rule"),
        (r"\breduction\b", "block diagram reduction"),
        (r"\bmechanical\b|\bmass[- ]spring\b|\bdamper\b", "mechanical systems"),
        (r"\belectrical\b|\bRLC\b|\bcircuit\b", "electrical systems"),
        (r"\bdifferential equation\b", "differential equations"),
    ]

    concept_hits: dict[str, list[str]] = defaultdict(list)
    notes_by_slide = {n["slide_id"]: n for n in topic_data["notes"]}

    for s in topic_data["slides"]:
        blob = " ".join(s["body_text"])
        note = notes_by_slide.get(s["id"])
        if note:
            blob += " " + note["text"]
        for pat, name in concept_patterns:
            if re.search(pat, blob, re.I):
                if s["id"] not in concept_hits[name]:
                    concept_hits[name].append(s["id"])

        for eq in s["equations_raw"]:
            formulas.append(
                {
                    "id": f"f-{s['id']}-{len(formulas)+1:04d}",
                    "expression": eq,
                    "slide_id": s["id"],
                    "topic": s["topic"],
                    "title_context": s["title"],
                }
            )

        for p in s["body_text"]:
            if re.search(r"\bis defined as\b|\bdefinition\b|:.*\bis\b", p, re.I) or (
                len(p) < 160 and re.search(r"\bis\b", p) and p[0].isupper()
            ):
                glossary.append(
                    {
                        "term_guess": s["title"][:80],
                        "definition": p,
                        "slide_id": s["id"],
                        "topic": s["topic"],
                    }
                )

    for name, ids in sorted(concept_hits.items()):
        concepts.append(
            {
                "concept": name,
                "slide_ids": ids,
                "count": len(ids),
            }
        )

    idx = out_dir / "index"
    write_jsonl(idx / "concepts.jsonl", concepts)
    write_jsonl(idx / "formulas.jsonl", formulas)
    write_jsonl(idx / "glossary.jsonl", glossary)


def write_completeness_for_deck(topic_data: dict, out_dir: Path) -> None:
    m = topic_data["meta"]
    c = m["completeness"]
    lines = [
        f"# Completeness — {m['title']}",
        "",
        f"Source PowerPoint: `{m['source_file']}`",
        f"Deck folder: `{out_dir.name}`",
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        "",
        f"- Slides: {m['slide_count']}",
        f"- Notes: {m['notes_count']}",
        f"- Media refs: {m['media_count']}",
        f"- SHA256: `{m['source_sha256']}`",
        f"- Slides with notes: {c['slides_with_notes_count']}",
        f"- Slides without notes: {c['slides_without_notes_count']}",
        f"- Empty-text slides: {len(c['empty_text_slides'])}",
        f"- Figure-only slides: {len(c['figure_only_slides'])}",
        f"- Orphan notes XMLs: {len(c['notes_without_slide_match'])}",
        "",
    ]
    if c["empty_text_slides"]:
        lines.append("Empty text: " + ", ".join(c["empty_text_slides"]))
        lines.append("")
    if c["figure_only_slides"]:
        lines.append("Figure-only: " + ", ".join(c["figure_only_slides"]))
        lines.append("")
    if c["notes_without_slide_match"]:
        lines.append("Orphan notes: " + ", ".join(c["notes_without_slide_match"]))
        lines.append("")
    chars = sum(len(" ".join(s["body_text"])) for s in topic_data["slides"])
    note_chars = sum(len(n["text"]) for n in topic_data["notes"])
    omml_count = sum(len(s.get("omml_equations") or []) for s in topic_data["slides"])
    lines += [
        f"- Body character count: {chars}",
        f"- Notes character count: {note_chars}",
        f"- OMML equation blocks: {omml_count}",
        "",
    ]
    (out_dir / "completeness.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ARTIFACTS.mkdir(parents=True, exist_ok=True)
    DECKS_ROOT.mkdir(parents=True, exist_ok=True)
    deck_summaries = []

    # Remove previous shared/mixed layouts so only per-deck folders remain
    for stale in ("topics", "index"):
        stale_path = ARTIFACTS / stale
        if stale_path.exists():
            shutil.rmtree(stale_path)
    old_report = ARTIFACTS / "extraction" / "completeness_report.md"
    if old_report.exists():
        old_report.unlink()

    for fname, meta in TOPIC_MAP.items():
        pptx = ROOT / fname
        if not pptx.exists():
            raise FileNotFoundError(pptx)
        deck_dir = DECKS_ROOT / meta["slug"]
        if deck_dir.exists():
            shutil.rmtree(deck_dir)

        print(f"Extracting {fname} -> decks/{meta['slug']}/ ...")
        td = extract_deck(pptx, meta)
        out_dir = DECKS_ROOT / meta["slug"]
        (out_dir / "knowledge.md").write_text(synthesize_knowledge(td), encoding="utf-8")
        build_indexes_for_deck(td, out_dir)
        write_completeness_for_deck(td, out_dir)

        deck_summaries.append(
            {
                "topic": meta["topic"],
                "slug": meta["slug"],
                "title": meta["title"],
                "source_file": fname,
                "artifact_path": f"decks/{meta['slug']}",
                "sha256": td["meta"]["source_sha256"],
                "slides": td["meta"]["slide_count"],
                "notes": td["meta"]["notes_count"],
                "media_refs": td["meta"]["media_count"],
            }
        )
        print(
            f"  -> {td['meta']['slide_count']} slides, "
            f"{td['meta']['notes_count']} notes, "
            f"{td['meta']['media_count']} media refs"
        )

    manifest = {
        "course": "ELE 442 — Control Systems",
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "layout": "one folder per PowerPoint under artifacts/decks/",
        "artifact_root": "artifacts",
        "schema": {
            "per_deck_files": [
                "deck.meta.yaml",
                "slides.jsonl",
                "notes.jsonl",
                "knowledge.md",
                "completeness.md",
                "index/concepts.jsonl",
                "index/formulas.jsonl",
                "index/glossary.jsonl",
                "media/",
            ],
            "slides_jsonl": [
                "id",
                "topic",
                "slide",
                "title",
                "bullets",
                "body_text",
                "tables",
                "equations_raw",
                "omml_equations",
                "media_refs",
                "notes_id",
                "tags",
                "source",
            ],
        },
        "decks": deck_summaries,
        "totals": {
            "decks": len(deck_summaries),
            "slides": sum(d["slides"] for d in deck_summaries),
            "notes": sum(d["notes"] for d in deck_summaries),
            "media_refs": sum(d["media_refs"] for d in deck_summaries),
        },
    }
    write_yaml_simple(ARTIFACTS / "manifest.yaml", manifest)
    print("Done.")
    print(json.dumps(manifest["totals"], indent=2))


if __name__ == "__main__":
    main()

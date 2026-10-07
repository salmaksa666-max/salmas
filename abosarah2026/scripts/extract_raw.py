import sqlite3
import json
import re
import zipfile
import tempfile
import os

APKG_PATH = "/tmp/claude-0/-home-user-salmas/a5458d62-c397-540f-8afd-07d9eb2a5edf/scratchpad/inspect_apkg/deck.apkg"

tmp = tempfile.mkdtemp()
with zipfile.ZipFile(APKG_PATH) as z:
    z.extractall(tmp)

con = sqlite3.connect(os.path.join(tmp, "collection.anki2"))
cur = con.cursor()
cur.execute("select models from col")
models = json.loads(cur.fetchone()[0])
mid = list(models.keys())[0]
flds = [f["name"] for f in models[mid]["flds"]]
idx = {n: i for i, n in enumerate(flds)}

OPT_RE = re.compile(r'<div class="source-option" data-letter="([A-D])">([A-D])[\.\)]?\s*(.*?)</div>', re.S)
KW_RE = re.compile(r'<span class="kw">(.*?)</span>', re.S)


def strip_tags(html):
    if not html:
        return ""
    text = re.sub(r"<[^>]+>", "", html)
    text = text.replace("&amp;", "&").replace("&#39;", "'").replace("&quot;", '"')
    text = text.replace("&lt;", "<").replace("&gt;", ">")
    return text.strip()


def parse_study_note(html):
    """Returns dict: {label: text} for each <div class="study-item"> block,
    across BOTH study-note-v8 blocks (AI explanation + compiler/source notes)."""
    items = {}
    for m in re.finditer(
        r'<span class="study-label">(.*?)</span><div class="study-value">(.*?)</div></div>',
        html, re.S,
    ):
        label = strip_tags(m.group(1))
        value = m.group(2)
        items[label] = value
    return items


def parse_options(html):
    opts = {}
    for m in OPT_RE.finditer(html):
        letter = m.group(1)
        text = strip_tags(m.group(3))
        opts[letter] = text
    return opts


def extract_highlight_terms(html):
    terms = []
    for m in KW_RE.finditer(html):
        term = strip_tags(m.group(1))
        if term and term not in terms:
            terms.append(term)
    return terms


cur.execute("select id, flds from notes order by id")
rows = cur.fetchall()

questions = []
for nid, flds_raw in rows:
    parts = flds_raw.split("\x1f")

    def f(name):
        return parts[idx[name]]

    qno = f("QNo")
    section = f("Section")
    stem_html = f("OriginalQuestionHTML")
    stem_text_block = re.search(r'<div class="question-stem-text">(.*?)</div>', stem_html, re.S)
    stem = strip_tags(stem_text_block.group(1)) if stem_text_block else strip_tags(f("OriginalQuestionText"))
    highlight_terms = extract_highlight_terms(stem_html)

    opts_block = re.search(r'<div class="question-options">(.*)', stem_html, re.S)
    opts = parse_options(opts_block.group(1)) if opts_block else {}

    source_answer = strip_tags(f("SourceAnswer"))
    if source_answer.strip() == "zzz_no_source_answer":
        answer_letter = None
    else:
        m = re.match(r'^([A-D])[\.\)]?\s*(.*)$', source_answer.strip())
        answer_letter = m.group(1) if m else None

    answer_state = f("AnswerState")
    status_label = strip_tags(f("StatusLabel"))

    study = parse_study_note(f("StudyNote"))
    source_page = strip_tags(f("SourcePage"))

    questions.append({
        "qno": qno,
        "section": section,
        "stem": stem,
        "OptA": opts.get("A"),
        "OptB": opts.get("B"),
        "OptC": opts.get("C"),
        "OptD": opts.get("D"),
        "answer_letter": answer_letter,
        "answer_state": answer_state,
        "status_label": status_label,
        "highlight_terms_source": highlight_terms,
        "why_right": study.get("Why the answer is right", ""),
        "why_wrong_block": study.get("Why the others are wrong", ""),
        "key_concept": study.get("Key concept", ""),
        "exam_pearl": study.get("Exam pearl", ""),
        "compiler_note": study.get("Source notes", "") or study.get("Compiler note", ""),
        "source_page": source_page,
    })

with open("abosarah2026/data/raw_questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=1)

print("total:", len(questions))
print("has 4 options:", sum(1 for q in questions if q["OptA"] and q["OptB"] and q["OptC"] and q["OptD"]))
print("has 3 options only:", sum(1 for q in questions if q["OptA"] and q["OptB"] and q["OptC"] and not q["OptD"]))
print("has answer_letter:", sum(1 for q in questions if q["answer_letter"]))
from collections import Counter
print("answer_state:", Counter(q["answer_state"] for q in questions))
print("has why_right:", sum(1 for q in questions if q["why_right"]))
print("has why_wrong_block:", sum(1 for q in questions if q["why_wrong_block"]))
sections = Counter(q["section"] for q in questions)
for k, v in sorted(sections.items()):
    print(k, v)

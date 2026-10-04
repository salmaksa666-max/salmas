import re
import json

with open("smle2026/data/full_text.txt", encoding="utf-8") as f:
    lines = f.readlines()
lines = [l.rstrip("\n") for l in lines]

with open("smle2026/data/final_markers.txt", encoding="utf-8") as f:
    markers = []
    for line in f:
        i, num, rest = line.rstrip("\n").split("\t", 2)
        markers.append((int(i), int(num), rest))

OPT_RE = re.compile(r'^([A-Da-d])[\.\)\-]\s*(.*)$')
ANSWER_RE = re.compile(r'^\(?(answer|ans|correct answer)\)?\s*[:\-]?\s*([A-Da-d])\b(.*)$', re.IGNORECASE)
CHECK_CHARS = "✅✔"  # checkmark emoji / heavy check mark

# source text sometimes has contributor commentary glued onto the last
# option or the stem with no line break (e.g. "...prior to surgery
# AboSarah: (Patient safety...)"). Truncate at the first such marker.
COMMENTARY_RE = re.compile(
    r'\b([A-Z][a-zA-Z]{2,15}:\s|According to\b|Reference[s]?:\s|'
    r'https?://\S+|●|\bConfirmed\b|\bQ:\s)'
)

MAX_OPTION_LEN = 100


def strip_commentary(text):
    if not text:
        return text
    m = COMMENTARY_RE.search(text)
    if m:
        text = text[:m.start()].strip()
    if len(text) > MAX_OPTION_LEN:
        cut = text.rfind(" ", 0, MAX_OPTION_LEN)
        if cut == -1:
            cut = MAX_OPTION_LEN
        text = text[:cut].strip()
    return text

questions = []
for idx in range(len(markers)):
    start_line, num, first_rest = markers[idx]
    end_line = markers[idx + 1][0] if idx + 1 < len(markers) else len(lines)
    block_lines = [first_rest] + lines[start_line + 1:end_line]
    while block_lines and not block_lines[-1].strip():
        block_lines.pop()

    opts = {}
    opt_order = []
    closed_opts = set()
    answer_letter = None
    answer_source = None  # "text" | "check"
    stem_lines = []
    opt_started = False
    for bl in block_lines:
        raw = bl.strip()
        am = ANSWER_RE.match(raw)
        if am:
            answer_letter = am.group(2).upper()
            answer_source = "text"
            continue
        om = OPT_RE.match(raw)
        if om:
            letter = om.group(1).upper()
            text = om.group(2).strip()
            has_check = any(c in text for c in CHECK_CHARS)
            text_clean = "".join(c for c in text if c not in CHECK_CHARS).strip()
            stripped = strip_commentary(text_clean)
            if stripped != text_clean:
                closed_opts.add(letter)
            opts[letter] = stripped
            opt_order.append(letter)
            opt_started = True
            # NOTE: checkmark-based answer detection was tried and dropped —
            # PDF text-extraction order doesn't reliably match visual
            # position in this file (a checkmark meant for option A ended
            # up attributed to option D in testing), so a ✅/✔ found near
            # an option is NOT treated as a confirmed source answer. Only
            # an explicit "Answer: X" line counts as source-confirmed.
            continue
        if any(c in raw for c in CHECK_CHARS):
            continue
        if not opt_started:
            stem_lines.append(bl)
        else:
            if opts:
                last_letter = opt_order[-1]
                if last_letter in closed_opts:
                    continue
                cleaned = "".join(c for c in bl.strip() if c not in CHECK_CHARS).strip()
                if cleaned and not COMMENTARY_RE.match(cleaned):
                    combined = (opts[last_letter] + " " + cleaned).strip()
                    stripped = strip_commentary(combined)
                    if stripped != combined:
                        closed_opts.add(last_letter)
                    opts[last_letter] = stripped
                elif cleaned:
                    closed_opts.add(last_letter)

    stem = " ".join(s.strip() for s in stem_lines if s.strip())
    stem = "".join(c for c in stem if c not in CHECK_CHARS).strip()
    qm = re.search(r'\bQ:\s*', stem)
    if qm and qm.start() > 15:
        after = stem[qm.end():].strip()
        if len(after) > 30:
            stem = after

    questions.append({
        "num": num,
        "stem": stem,
        "OptA": opts.get("A"),
        "OptB": opts.get("B"),
        "OptC": opts.get("C"),
        "OptD": opts.get("D"),
        "answer_letter": answer_letter,
        "answer_source": answer_source,
    })

# detect exact-duplicate stems (keep both per "never merge or skip", just tag them)
seen = {}
for q in questions:
    key = q["stem"]
    if key and key in seen:
        q["duplicate_of"] = seen[key]
    else:
        if key:
            seen[key] = q["num"]

with open("smle2026/data/raw_questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=1)

total = len(questions)
empty = sum(1 for q in questions if not q["stem"] and not q["OptA"])
has_stem = sum(1 for q in questions if q["stem"])
has_4opts = sum(1 for q in questions if q["OptA"] and q["OptB"] and q["OptC"] and q["OptD"])
has_3opts_only = sum(1 for q in questions if q["OptA"] and q["OptB"] and q["OptC"] and not q["OptD"])
has_answer = sum(1 for q in questions if q["answer_letter"])
has_answer_text = sum(1 for q in questions if q["answer_source"] == "text")
has_answer_check = sum(1 for q in questions if q["answer_source"] == "check")
usable = sum(1 for q in questions if q["stem"] and q["OptA"] and q["OptB"])
dupes = sum(1 for q in questions if q.get("duplicate_of"))

print("total:", total)
print("completely empty (no stem, no options):", empty)
print("has stem:", has_stem)
print("usable (stem + >=2 options):", usable)
print("has 4 options:", has_4opts)
print("has exactly 3 options:", has_3opts_only)
print("has answer (any source):", has_answer, "(text:", has_answer_text, ", check-mark:", has_answer_check, ")")
print("exact duplicate stems:", dupes)

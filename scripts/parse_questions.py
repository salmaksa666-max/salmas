import json
import re

with open("data/raw_questions.json", encoding="utf-8") as f:
    raw = json.load(f)

OPT_RE = re.compile(r'^([A-D])[.\)]?\s*(.*)$', re.S)


def split_front(front_raw):
    lines = front_raw.split("<br>")
    opt_idx = {}
    for i, ln in enumerate(lines):
        m = OPT_RE.match(ln.strip())
        if m:
            opt_idx[m.group(1)] = (i, m.group(2).strip())
    # need at least A, B, C present (some source questions have only 3 options)
    if not all(k in opt_idx for k in "ABC"):
        return None
    keys = [k for k in "ABCD" if k in opt_idx]
    idxs = [opt_idx[k][0] for k in keys]
    if idxs != sorted(idxs):
        return None
    stem_lines = lines[:idxs[0]]
    stem = "<br>".join(stem_lines).strip()
    opts = {k: opt_idx[k][1] for k in keys}
    if "D" not in opts:
        opts["D"] = None
    return stem, opts


ok = 0
fail = []
parsed = []
for q in raw:
    r = split_front(q["front_raw"])
    if r is None:
        fail.append(q["num"])
        continue
    stem, opts = r
    ok += 1
    parsed.append({
        "seq": q["seq"],
        "num": q["num"],
        "nid": q["nid"],
        "stem": stem,
        "OptA": opts["A"],
        "OptB": opts["B"],
        "OptC": opts["C"],
        "OptD": opts["D"],
        "answer_letter": q["answer_letter"],
        "extra_note": q["extra_note"],
    })

print("ok:", ok, "fail:", len(fail))
print("failed nums (first 30):", fail[:30])

with open("data/parsed_questions.json", "w", encoding="utf-8") as f:
    json.dump(parsed, f, ensure_ascii=False, indent=2)

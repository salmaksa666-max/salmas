import json

with open("abosarah2026/data/raw_questions.json", encoding="utf-8") as f:
    raw = json.load(f)

parsed = []
skipped = 0
for q in raw:
    n_opts = sum(1 for L in "ABCD" if q.get(f"Opt{L}"))
    if n_opts < 2 or not q["stem"]:
        skipped += 1
        continue
    ans = q["answer_letter"]
    if ans and not q.get(f"Opt{ans}"):
        ans = None
    parsed.append({
        "qno": q["qno"],
        "section": q["section"],
        "stem": q["stem"],
        "OptA": q["OptA"], "OptB": q["OptB"], "OptC": q["OptC"], "OptD": q["OptD"],
        "answer_letter": ans,
        "answer_state": q["answer_state"],
        "status_label": q["status_label"],
        "highlight_terms_source": q["highlight_terms_source"],
        "why_right": q["why_right"],
        "why_wrong_block": q["why_wrong_block"],
        "key_concept": q["key_concept"],
        "exam_pearl": q["exam_pearl"],
        "compiler_note": q["compiler_note"],
        "source_page": q["source_page"],
    })

with open("abosarah2026/data/parsed_questions.json", "w", encoding="utf-8") as f:
    json.dump(parsed, f, ensure_ascii=False, indent=1)

print("total parsed/usable:", len(parsed))
print("skipped (no stem or <2 options):", skipped)
print("with confirmed source answer:", sum(1 for q in parsed if q["answer_letter"]))
print("WITHOUT source answer:", sum(1 for q in parsed if not q["answer_letter"]))

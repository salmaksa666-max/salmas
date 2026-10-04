import json

with open("smle2026/data/raw_questions.json", encoding="utf-8") as f:
    raw = json.load(f)

parsed = []
skipped_no_content = 0
skipped_dup = 0
for q in raw:
    if not q["stem"] or not q["OptA"] or not q["OptB"]:
        skipped_no_content += 1
        continue
    # keep duplicates per "never merge or skip" — just carry the flag through
    ans = q["answer_letter"]
    if ans and not q.get(f"Opt{ans}"):
        # answer references a letter with no option text -> treat as no answer
        ans = None
        q["answer_source"] = None
    parsed.append({
        "num": q["num"],
        "stem": q["stem"],
        "OptA": q["OptA"],
        "OptB": q["OptB"],
        "OptC": q.get("OptC"),
        "OptD": q.get("OptD"),
        "answer_letter": ans,
        "answer_source": q.get("answer_source"),
        "duplicate_of": q.get("duplicate_of"),
    })

with open("smle2026/data/parsed_questions.json", "w", encoding="utf-8") as f:
    json.dump(parsed, f, ensure_ascii=False, indent=1)

print("total parsed/usable:", len(parsed))
print("skipped (no stem or <2 options):", skipped_no_content)
print("with confirmed source answer:", sum(1 for q in parsed if q["answer_letter"]))
print("WITHOUT source answer (need own judgment):", sum(1 for q in parsed if not q["answer_letter"]))

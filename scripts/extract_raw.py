import sqlite3
import json
import re

DB_PATH = "/tmp/claude-0/-home-user-salmas/a5458d62-c397-540f-8afd-07d9eb2a5edf/scratchpad/apkg_extract/extracted/collection.anki21"

con = sqlite3.connect(DB_PATH)
cur = con.cursor()
cur.execute("select id, flds from notes order by id")
rows = cur.fetchall()

out = []
for nid, flds in rows:
    front, back = flds.split("\x1f")[0], flds.split("\x1f")[1]
    m = re.match(r'^(\d{3,4})\s*-\s*(.*)$', front.strip(), re.S)
    if not m:
        continue
    num = int(m.group(1))
    body = m.group(2)
    back = back.strip()
    bm = re.match(r'^([A-D])\s*;?\s*(.*)$', back, re.S)
    if not bm:
        # not a real MCQ note (e.g. the promo/announcement card)
        continue
    ans = bm.group(1)
    note = bm.group(2).strip()
    out.append({
        "num": num,
        "nid": nid,
        "front_raw": body,
        "answer_letter": ans,
        "extra_note": note,
    })

out.sort(key=lambda q: q["nid"])
for i, q in enumerate(out, start=1):
    q["seq"] = i

print("total:", len(out))
with open("data/raw_questions.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

# -*- coding: utf-8 -*-
"""Split an MKJ apkg (old-format collection.anki21) into System::Topic subdecks from a qid -> [system, topic] map
(written by build_dense_merged.py MAP=...).  Cards keep ids, notes, scheduling and revlog; topic tags added.
usage: split_by_map.py SRC.apkg MAP.json OUT.apkg"""
import json
import os
import re
import sqlite3
import sys
import tempfile
import time
import zipfile

SRC, MAP, OUT = sys.argv[1:4]
where = json.load(open(MAP, encoding="utf-8"))
SYSTEMS = ["Cardiology", "Pulmonology", "GI & Hepatology", "Nephrology & Electrolytes", "Endocrinology",
           "Hematology & Oncology", "Neurology", "Infectious disease", "Rheumatology", "Other"]
num = {s: f"{i + 1:02d} {s}" for i, s in enumerate(SYSTEMS)}

work = tempfile.mkdtemp()
zipfile.ZipFile(SRC).extractall(work)
c = sqlite3.connect(os.path.join(work, "collection.anki21"))
decks = json.loads(c.execute("select decks from col").fetchone()[0])
names = [f["name"] for f in list(json.loads(c.execute("select models from col").fetchone()[0]).values())[0]["flds"]]
used = {d for (d,) in c.execute("select distinct did from cards")}
parent = decks[str(next(iter(used)))]
now, base = int(time.time()), int(time.time() * 1000)
ids = {}


def deck(name):
    if name not in ids:
        d = json.loads(json.dumps(parent))
        d["id"] = base + len(ids)
        d["name"], d["mod"], d["usn"] = name, now, -1
        decks[str(d["id"])] = d
        ids[name] = d["id"]
    return ids[name]


moved, other = 0, []
for nid, flds, tags in c.execute("select id, flds, tags from notes").fetchall():
    qno = flds.split("\x1f")[names.index("QNo")]
    s, t = where.get(qno, ["Other", "Other"])
    if qno not in where:
        other.append(qno)
    sub = parent["name"] + "::" + num[s] + ("" if t == s or t == "Other" else "::" + t.replace("/", "-"))
    did = deck(parent["name"] + "::" + num[s]) if sub.endswith(num[s]) else (deck(parent["name"] + "::" + num[s]), deck(sub))[1]
    tag = "Medicine::" + re.sub(r"[^A-Za-z0-9]+", "_", s) + "::" + re.sub(r"[^A-Za-z0-9]+", "_", t).strip("_")
    c.execute("update cards set did=?, mod=?, usn=-1 where nid=?", (did, now, nid))
    c.execute("update notes set tags=?, mod=?, usn=-1 where id=?", (" " + " ".join(sorted(set(tags.split()) | {tag})) + " ", now, nid))
    moved += 1
c.execute("update col set decks=?, mod=?", (json.dumps(decks), now * 1000))
c.commit()
print(moved, "notes moved;", len(other), "not in map (to Other):", other[:10])
print(c.execute("select count(*) from revlog").fetchone()[0], "reviews kept")
c.execute("vacuum")
c.close()
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for f in os.listdir(work):
        z.write(os.path.join(work, f), f)

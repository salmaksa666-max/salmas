# -*- coding: utf-8 -*-
"""Split the September Medicine deck into system subdecks (same grouping as the topic tables), keeping all
review history.  Every card keeps its id, note, scheduling and revlog; only its deck changes.  Topic tags added.
usage: split_sept_deck.py SRC.apkg OUT.apkg"""
import glob
import json
import os
import re
import shutil
import sqlite3
import sys
import tempfile
import time
import zipfile

SRC, OUT = sys.argv[1], sys.argv[2]
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "review")
FILES = [("01 Hematology & Oncology", "heme"), ("02 Cardiology", "cardio"), ("03 Pulmonology", "pulm"), ("04 GI & Hepatology", "gi"),
         ("05 Infectious disease", "id"), ("06 Rheumatology & TLS", "rheum"), ("07 Endocrinology", "endo"),
         ("08 Nephrology & Electrolytes", "neph"), ("09 Neurology", "neuro"), ("10 Other", "other")]
where = {}
for sub, key in FILES:
    topic = ""
    for ln in open(os.path.join(ROOT, f"sept_tables_{key}.txt"), encoding="utf-8"):
        if ln.startswith("== "):
            topic = re.sub(r"[^A-Za-z0-9]+", "_", re.sub(r"[؀-ۿ]+", " ", ln[3:])).strip("_")[:40] or "topic"
        ids = re.findall(r"\b\d{4}\b", ln.strip().strip("|").split("|")[-1]) if ln.startswith("|") else []
        for b in re.findall(r"\[([0-9 ]+)\]", ln):
            ids += b.split()
        for q in ids:
            where.setdefault("SWR-" + q, (sub, topic))

work = tempfile.mkdtemp()
zipfile.ZipFile(SRC).extractall(work)
db = os.path.join(work, "collection.anki21")
c = sqlite3.connect(db)
decks = json.loads(c.execute("select decks from col").fetchone()[0])
parent = next(d for d in decks.values() if d["name"].endswith("01- Medicine"))
now = int(time.time())
ids = {}
base = int(time.time() * 1000)
for i, (sub, _) in enumerate(FILES + [("99 Duplicates (safe to delete)", None)]):
    d = json.loads(json.dumps(parent))
    d["id"] = base + i
    d["name"] = parent["name"] + "::" + sub
    d["mod"], d["usn"] = now, -1
    decks[str(d["id"])] = d
    ids[sub] = d["id"]
c.execute("update col set decks=?, mod=?", (json.dumps(decks), now * 1000))
names = [f["name"] for f in list(json.loads(c.execute("select models from col").fetchone()[0]).values())[0]["flds"]]
moved, dup, missing = 0, 0, []
for nid, flds, tags in c.execute("select id, flds, tags from notes").fetchall():
    qno = flds.split("\x1f")[names.index("QNo")]
    if qno in where:
        sub, topic = where[qno]
        tag = "Sept::" + re.sub(r"[^A-Za-z0-9]+", "_", sub) + "::" + topic
    elif "zz_Duplicate_DELETE" in tags:
        sub, tag = "99 Duplicates (safe to delete)", None
        dup += 1
    else:
        missing.append(qno)
        continue
    c.execute("update cards set did=?, mod=?, usn=-1 where nid=?", (ids[sub], now, nid))
    if tag:
        c.execute("update notes set tags=?, mod=?, usn=-1 where id=?", (" " + " ".join(sorted(set(tags.split()) | {tag})) + " ", now, nid))
    moved += 1
c.commit()
print("cards moved for", moved, "notes; duplicates", dup, "; unmapped", missing)
print(c.execute("select count(*) from revlog").fetchone()[0], "reviews kept;",
      c.execute("select count(*) from cards where ivl>0").fetchone()[0], "cards with intervals kept")
c.close()
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for f in os.listdir(work):
        z.write(os.path.join(work, f), f)

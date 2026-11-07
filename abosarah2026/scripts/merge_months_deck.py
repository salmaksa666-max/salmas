# -*- coding: utf-8 -*-
"""Re-deck the 'SMLE MKJ Months Combined' apkg so September and October sit together:
Medicine and Pediatrics by System::Topic (from build_dense_merged.py MAP=... files, same order as the PDFs),
the other specialties as one deck each.  New cards get due = position in the PDF, so Anki shows them in paper order.
Notes get fresh guids/ids so the import never collides with the older single-month decks.
usage: merge_months_deck.py SRC.apkg MED_MAP.json PEDS_MAP.json SURGERY_MAP.json OBGYN_MAP.json OUT.apkg"""
import json
import os
import random
import re
import sqlite3
import string
import sys
import tempfile
import time
import zipfile

SRC, MED, PEDS, SUR, OBG, OUT = sys.argv[1:7]
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
import peds_systems  # noqa: E402
import surgery_obgyn_systems as so  # noqa: E402

MED_ORDER = ["Hematology & Oncology", "Neurology", "Cardiology", "Pulmonology", "GI & Hepatology", "Infectious disease",
             "Rheumatology", "Endocrinology", "Nephrology & Electrolytes", "Other"]
PEDS_ORDER = peds_systems.SYSORDER + ["Other"]
ROOT = "SMLE MKJ · Sept + Oct"
SPEC = [("Medicine", "01 Medicine"), ("Pediatrics", "02 Pediatrics"), ("OBGYN", "03 OBGYN"), ("Surgery", "04 Surgery"),
        ("Psychiatry", "05 Psychiatry"), ("Other / Mixed", "06 Other - Mixed")]


def clean(t):
    return re.sub(r"[/:]+", "-", t).strip()


def tree(mp, order):
    """qid -> (deck suffix, position) with numbered systems and topics in map (= PDF) order"""
    out, topics = {}, {}
    for pos, (q, (s, t)) in enumerate(mp.items()):
        si = order.index(s) + 1 if s in order else 99
        tl = topics.setdefault(s, [])
        if t not in tl:
            tl.append(t)
        name = f"{si:02d} {clean(s)}"
        if t not in (s, "Other"):
            name += f"::{tl.index(t) + 1:02d} {clean(t)}"
        out[q] = (name, pos)
    return out


med = tree(json.load(open(MED, encoding="utf-8")), MED_ORDER)
peds = tree(json.load(open(PEDS, encoding="utf-8")), PEDS_ORDER)
MAPS = {"01 Medicine": med, "02 Pediatrics": peds,
        "03 OBGYN": tree(json.load(open(OBG, encoding="utf-8")), so.OBGYN_ORDER + ["Other"]),
        "04 Surgery": tree(json.load(open(SUR, encoding="utf-8")), so.SURGERY_ORDER + ["Other"])}

work = tempfile.mkdtemp()
zipfile.ZipFile(SRC).extractall(work)
c = sqlite3.connect(os.path.join(work, "collection.anki21"))
decks = json.loads(c.execute("select decks from col").fetchone()[0])
names = [f["name"] for f in list(json.loads(c.execute("select models from col").fetchone()[0]).values())[0]["flds"]]
qi = names.index("QNo")
tmpl = next(d for d in decks.values() if d["name"] != "Default" and not d.get("dyn"))
now, base = int(time.time()), int(time.time() * 1000)
new_decks = {k: v for k, v in decks.items() if v["name"] == "Default"}
ids = {}


def deck(name):
    parts = name.split("::")
    for i in range(1, len(parts) + 1):
        nm = "::".join(parts[:i])
        if nm not in ids:
            d = json.loads(json.dumps(tmpl))
            d["id"] = base + len(ids)
            d["name"], d["mod"], d["usn"] = nm, now, -1
            new_decks[str(d["id"])] = d
            ids[nm] = d["id"]
    return ids[name]


rows = c.execute("select c.id, c.nid, c.did, n.flds from cards c join notes n on n.id = c.nid").fetchall()
count, extra = {}, 10 ** 6
for cid, nid, did, flds in rows:
    q = flds.split("\x1f")[qi]
    dn = decks[str(did)]["name"]
    spec = next((lab for key, lab in SPEC if f"- {key}" in dn), "07 Unsorted")
    if q in MAPS.get(spec, {}):
        sub, pos = MAPS[spec][q]
        name = f"{ROOT}::{spec}::{sub}"
    elif "Duplicates" in dn or spec in MAPS:  # not in the maps = StatusLabel Duplicate
        name, pos = f"{ROOT}::{spec}::99 Duplicates (safe to delete)", extra
    else:  # September first, then October, original order
        name, pos = f"{ROOT}::{spec}", (0 if "September" in dn else 50000) + cid % 100000
    count[name.split("::")[1]] = count.get(name.split("::")[1], 0) + 1
    c.execute("update cards set did=?, due=?, mod=?, usn=-1 where id=?", (deck(name), pos, now, cid))

# fresh guids / ids so this never merges into the older single-month decks
chars = string.ascii_letters + string.digits + "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
rnd = random.Random(2026)
for (nid,) in c.execute("select id from notes").fetchall():
    c.execute("update notes set guid=?, mod=?, usn=-1 where id=?", ("".join(rnd.choice(chars) for _ in range(10)), now, nid))
c.execute("update notes set id = id + 7")
c.execute("update cards set nid = nid + 7, id = id + 7")
c.execute("update col set decks=?, mod=?", (json.dumps(new_decks), now * 1000))
c.commit()
c.execute("vacuum")
c.close()
for k in sorted(count):
    print(f"{count[k]:6d}  {k}")
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for f in os.listdir(work):
        z.write(os.path.join(work, f), f)
print("->", OUT, round(os.path.getsize(OUT) / 1e6, 1), "MB")

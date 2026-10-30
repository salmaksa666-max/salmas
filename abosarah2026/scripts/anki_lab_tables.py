# -*- coding: utf-8 -*-
"""Add a sorted lab/vitals table with normal ranges under the stem of every question that has values.

The deck marks values as <span class="refrange">…</span>; the label is read from the words just before each span.
Only notes whose deck name contains DECK_PART are touched; the stem itself, options and answers are left as is.
usage: anki_lab_tables.py SRC.apkg OUT.apkg [DECK_PART]   (needs: pip install zstandard)
"""
import html
import os
import re
import shutil
import sqlite3
import sys
import tempfile
import time
import zipfile

import zstandard

SRC, OUT = sys.argv[1], sys.argv[2]
PART = sys.argv[3] if len(sys.argv) > 3 else "Part 2"


def rng(lo, hi, text):
    return dict(lo=lo, hi=hi, text=text)


def by_unit(cut, small, big):
    """pick a range by the size of the number (SI vs conventional units)"""
    return lambda v: small if v is None or v < cut else big


CATS = ["Vitals", "CBC", "Glucose & endocrine", "Electrolytes & renal", "ABG", "Lipids", "Liver & pancreas", "Cardiac"]
# (label regex, shown name, category, range picker)
LABS = [
    (r"\bBP\b|blood pressure", "BP", "Vitals", lambda v: rng(None, None, "<120/80 · HTN ≥130/80 (AHA) or ≥140/90 (JNC)")),
    (r"\bHR\b|heart rate|pulse", "HR", "Vitals", lambda v: rng(60, 100, "60–100 /min")),
    (r"\bRR\b|resp\w* rate", "RR", "Vitals", lambda v: rng(12, 20, "12–20 /min")),
    (r"\btemp\w*", "Temp", "Vitals", lambda v: rng(36.1, 37.5, "36.1–37.5 °C")),
    (r"SpO2|O2 sat\w*|saturation", "SpO2", "Vitals", lambda v: rng(95, 100, "95–100%")),
    (r"\bBMI\b", "BMI", "Vitals", lambda v: rng(18.5, 24.9, "18.5–24.9 · obese ≥30")),
    (r"waist circumference", "Waist", "Vitals", lambda v: rng(None, 102, "men <102 · women <88 cm")),
    (r"hip circumference", "Hip", "Vitals", lambda v: rng(None, None, "waist:hip ratio — men <0.9 · women <0.85")),
    (r"\bheight\b", "Height", "Vitals", lambda v: rng(None, None, "percentile")),
    (r"\bweight\b", "Weight", "Vitals", lambda v: rng(None, None, "percentile")),
    (r"\bRBCs?\b", "RBC", "CBC", lambda v: rng(4.2, 5.9, "4.2–5.9 ×10¹²/L")),
    (r"\bHb\b|\bHgb\b|ha?emoglobin", "Hb", "CBC", by_unit(25, rng(12, 17, "women 12–16 · men 13–17 g/dL"), rng(120, 170, "women 120–160 · men 130–170 g/L"))),
    (r"\bMCV\b", "MCV", "CBC", lambda v: rng(80, 100, "80–100 fL")),
    (r"\bMCH\b", "MCH", "CBC", lambda v: rng(27, 33, "27–33 pg")),
    (r"platelets?|\bPLTs?\b", "Platelets", "CBC", lambda v: rng(150, 400, "150–400 ×10⁹/L")),
    (r"\bWBCs?\b", "WBC", "CBC", lambda v: rng(4, 11, "4–11 ×10⁹/L")),
    (r"fasting (?:blood )?glucose|\bFBS\b|\bFBG\b", "Fasting glucose", "Glucose & endocrine",
     by_unit(30, rng(3.9, 5.5, "3.9–5.5 mmol/L · pre-DM 5.6–6.9 · DM ≥7.0"), rng(70, 100, "70–100 mg/dL · DM ≥126"))),
    (r"random (?:blood )?glucose|\bRBS\b|\bRBG\b", "Random glucose", "Glucose & endocrine",
     by_unit(30, rng(None, 7.8, "<7.8 mmol/L · DM ≥11.1 with symptoms"), rng(None, 140, "<140 mg/dL · DM ≥200"))),
    (r"glucose", "Glucose", "Glucose & endocrine",
     by_unit(30, rng(3.9, 7.8, "3.9–7.8 mmol/L · DM: fasting ≥7.0, random ≥11.1"), rng(70, 140, "70–140 mg/dL · DM: fasting ≥126, random ≥200"))),
    (r"HbA1c|\bA1c\b", "HbA1c", "Glucose & endocrine", lambda v: rng(None, 5.6, "<5.7% · pre-DM 5.7–6.4 · DM ≥6.5")),
    (r"C-peptide", "C-peptide", "Glucose & endocrine", lambda v: rng(0.5, 2.0, "0.5–2.0 ng/mL (low = type 1)")),
    (r"urine na\+?|urine sodium", "Urine Na", "Electrolytes & renal", lambda v: rng(None, None, "<20 prerenal/hypovolemic · >40 SIADH or ATN")),
    (r"urine osm\w*", "Urine osm", "Electrolytes & renal", lambda v: rng(None, None, ">100 with low serum osm = inappropriate ADH")),
    (r"serum osm\w*|\bosm\w*", "Serum osm", "Electrolytes & renal", lambda v: rng(275, 295, "275–295 mOsm/kg")),
    (r"\bNa\+?|sodium", "Na", "Electrolytes & renal", lambda v: rng(135, 145, "135–145 mmol/L")),
    (r"\bK\+?|potassium", "K", "Electrolytes & renal", lambda v: rng(3.5, 5.0, "3.5–5.0 mmol/L")),
    (r"\bCl-?|chloride", "Cl", "Electrolytes & renal", lambda v: rng(98, 106, "98–106 mmol/L")),
    (r"HCO3-?|bicarbonate|bicarb", "HCO3", "Electrolytes & renal", lambda v: rng(22, 26, "22–26 mmol/L")),
    (r"\bCa(?:2\+)?|calcium", "Ca", "Electrolytes & renal", by_unit(5, rng(2.15, 2.6, "2.15–2.6 mmol/L"), rng(8.5, 10.5, "8.5–10.5 mg/dL"))),
    (r"albumin", "Albumin", "Electrolytes & renal", by_unit(10, rng(3.5, 5, "3.5–5 g/dL"), rng(35, 50, "35–50 g/L"))),
    (r"\burea\b|\bBUN\b", "Urea", "Electrolytes & renal", lambda v: rng(2.5, 7.5, "2.5–7.5 mmol/L")),
    (r"creatinine|\bCr\b", "Creatinine", "Electrolytes & renal", by_unit(20, rng(0.6, 1.2, "0.6–1.2 mg/dL"), rng(60, 110, "60–110 µmol/L"))),
    (r"e?GFR", "eGFR", "Electrolytes & renal", lambda v: rng(90, None, ">90 · CKD3 30–59 · CKD4 15–29")),
    (r"\bpH\b", "pH", "ABG", lambda v: rng(7.35, 7.45, "7.35–7.45")),
    (r"PCO2|PaCO2", "PCO2", "ABG", lambda v: rng(35, 45, "35–45 mmHg")),
    (r"\bPO2|PaO2", "PO2", "ABG", lambda v: rng(80, 100, "80–100 mmHg")),
    (r"\bLDL\b", "LDL", "Lipids", by_unit(20, rng(None, 3.0, "<3.0 mmol/L · target <2.5, <2.0 if ASCVD · ≥4.9 = high statin"), rng(None, 116, "<116 mg/dL · target <100, <70 if ASCVD · ≥190 = high statin"))),
    (r"\bHDL\b", "HDL", "Lipids", by_unit(10, rng(1.0, None, ">1.0 men · >1.3 women mmol/L"), rng(40, None, ">40 men · >50 women mg/dL"))),
    (r"\bTG\b|triglycerides?", "TG", "Lipids", by_unit(20, rng(None, 1.7, "<1.7 mmol/L (150 mg/dL)"), rng(None, 150, "<150 mg/dL"))),
    (r"(?:total )?cholesterol", "Total cholesterol", "Lipids", by_unit(20, rng(None, 5.2, "<5.2 mmol/L"), rng(None, 200, "<200 mg/dL"))),
    (r"direct bilirubin", "Direct bilirubin", "Liver & pancreas", by_unit(2, rng(None, 0.3, "<0.3 mg/dL"), rng(None, 5, "<5 µmol/L"))),
    (r"(?:total )?bilirubin", "Total bilirubin", "Liver & pancreas", by_unit(5, rng(None, 1.2, "<1.2 mg/dL"), rng(None, 21, "<21 µmol/L"))),
    (r"\bAST\b", "AST", "Liver & pancreas", lambda v: rng(None, 40, "10–40 U/L")),
    (r"\bALT\b", "ALT", "Liver & pancreas", lambda v: rng(None, 40, "7–40 U/L")),
    (r"\bALP\b|alkaline phosphatase", "ALP", "Liver & pancreas", lambda v: rng(40, 130, "40–130 U/L")),
    (r"\bGGT\b", "GGT", "Liver & pancreas", lambda v: rng(None, 50, "<50 U/L")),
    (r"globulin", "Globulin", "Liver & pancreas", lambda v: rng(20, 35, "20–35 g/L")),
    (r"amylase", "Amylase", "Liver & pancreas", lambda v: rng(30, 110, "30–110 U/L · pancreatitis >3× upper limit")),
    (r"\bANA\b", "ANA", "Liver & pancreas", lambda v: rng(None, None, "<1:80")),
    (r"troponin", "Troponin", "Cardiac", lambda v: rng(None, None, "below the lab's 99th-percentile cut-off")),
    (r"CK-?MB", "CK-MB", "Cardiac", lambda v: rng(None, 5, "<5 ng/mL")),
    (r"\bEF\b|ejection fraction", "EF", "Cardiac", lambda v: rng(55, 70, "55–70% · HFrEF ≤40%")),
    (r"valve gradient|gradient", "Aortic valve gradient", "Cardiac", lambda v: rng(None, 40, "severe AS: mean ≥40 mmHg · very severe ≥60")),
    (r"ASCVD risk|risk of", "10-yr ASCVD risk", "Cardiac", lambda v: rng(None, None, "<5% low · 5–7.4 borderline · 7.5–19.9 intermediate · ≥20 high")),
]
LABS = [(re.compile(rf"(?:{p})\s*[:=(~]*\s*$", re.I), name, cat, fn) for p, name, cat, fn in LABS]
SRC_RANGE = re.compile(r"(?:normal|nl|reference|ref|normal range)\s*[:=]?\s*$", re.I)
CHILD = re.compile(r"\b(\d{1,2})[- ]?(?:year|yr|y\.?o)|month|infant|newborn|neonate|toddler|\bboy\b|\bgirl\b|child", re.I)
SPAN = re.compile(r'<span class="refrange">(.*?)</span>', re.S)


SUP = str.maketrans("⁺⁻²³₂₃", "+-2323")


def plain(h):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", h))).strip().translate(SUP)


def first_num(s):
    m = re.search(r"-?\d+(?:\.\d+)?", s.replace(",", ""))
    return float(m.group(0)) if m else None


def flag(name, val, r):
    if name == "BP":
        m = re.search(r"(\d{2,3})\s*/\s*(\d{2,3})", val)
        if not m:
            return ""
        s, d = int(m.group(1)), int(m.group(2))
        return "↑" if s >= 130 or d >= 80 else ("↓" if s < 90 or d < 60 else "✓")
    v = first_num(val)
    if v is None or (r["lo"] is None and r["hi"] is None):
        return ""
    if r["hi"] is not None and v > r["hi"]:
        return "↑"
    if r["lo"] is not None and v < r["lo"]:
        return "↓"
    return "✓"


FILLER = re.compile(r"(?:\s*(?:\(|\)|:|,|is|was|now|this time|lower|higher|negative|positive|elevated|high|low|level|count|of|about|around|only|significantly|≈|~))+\s*$", re.I)
URINE = {"Na": "<20 = volume depletion (prerenal)", "K": "<20 = GI loss · >20–30 = renal loss",
         "Cl": "<15–20 = saline-responsive (vomiting / NG suction)"}


def rows_of(q):
    rows, last_end, urine = [], 0, False
    for m in SPAN.finditer(q):
        seg = q[last_end:m.start()]
        before = plain(seg)
        last_end = m.end()
        if re.search(r"urine\s*:", before, re.I):
            urine = True  # a "Urine: Na …, K …, Cl …" line
        elif "<br" in seg or re.search(r"serum\s*:", before, re.I):
            urine = False
        val = plain(m.group(1))
        if rows and SRC_RANGE.search(before[-25:]):
            rows[-1]["src"] = val  # the question gives its own normal range for the value before
            continue
        tail = before[-40:]
        for t in (tail, FILLER.sub("", tail)):
            hit = next(((name, cat, fn) for rx, name, cat, fn in LABS if rx.search(t)), None)
            if hit:
                break
        if hit:
            name, cat, fn = hit
            r = fn(first_num(val))
            if urine and name in URINE:
                name, r = "Urine " + name, rng(None, None, URINE[name])
            if not any(x["name"] == name and x["val"] == val for x in rows):  # the same value quoted twice
                rows.append(dict(name=name, cat=cat, val=val, r=r, src=None))
    return sorted(rows, key=lambda r: CATS.index(r["cat"]))  # stable: keeps the question's order inside a group


COLOR = {"↑": "#c0392b", "↓": "#1f6fb2", "✓": "#2e8b57", "": "inherit"}


def table(rows, child):
    out = ['<div class="labtbl" dir="ltr" style="margin-top:10px"><b>🧪 القيم مرتبة</b>',
           '<table class="lab" style="font-size:14px;width:100%;color:#1d2b36"><tr><th>Test</th><th>Value</th><th></th><th>Normal</th></tr>']
    prev = None
    for r in rows:
        if r["cat"] != prev:  # group name as its own row, so the table stays narrow on a phone
            out.append(f'<tr><td colspan="4" style="background:#eef3f6;font-weight:bold;font-size:13px">{html.escape(r["cat"])}</td></tr>')
        prev = r["cat"]
        normal = html.escape(r["src"]) + " <i>(from the question)</i>" if r["src"] else html.escape(r["r"]["text"])
        out.append(f'<tr><td><b>{html.escape(r["name"])}</b></td>'
                   f'<td><span class="refrange">{html.escape(r["val"])}</span></td>'
                   f'<td style="color:{COLOR[r["flag"]]};font-weight:bold;text-align:center">{r["flag"]}</td><td>{normal}</td></tr>')
    out.append("</table>")
    if child:
        out.append('<div style="font-size:12px;color:#8a6d1f">⚠ child: the normals above are adult values; HR, RR, BP and Hb differ by age, so vitals have no arrow.</div>')
    return "".join(out) + "</div>"


def main():
    work = tempfile.mkdtemp()
    with zipfile.ZipFile(SRC) as z:
        z.extractall(work)
        names = z.namelist()
    dbp = os.path.join(work, "col.db")
    with open(os.path.join(work, "collection.anki21b"), "rb") as f, open(dbp, "wb") as g:
        g.write(zstandard.ZstdDecompressor().stream_reader(f).read())
    c = sqlite3.connect(dbp)
    c.create_collation("unicase", lambda a, b: (a.lower() > b.lower()) - (a.lower() < b.lower()))  # Anki's own collation
    decks = {i: n for i, n in c.execute("select id, name from decks")}
    mcq = c.execute("select id from notetypes where name like '%MCQ%'").fetchone()[0]
    now = int(time.time())
    done = skipped = 0
    seen = set()
    for nid, flds, did in c.execute("select n.id, n.flds, c.did from notes n join cards c on c.nid = n.id where n.mid = ?", (mcq,)).fetchall():
        if nid in seen or f"\x1f{PART}\x1f" not in decks[did] + "\x1f":
            continue
        seen.add(nid)
        f = flds.split("\x1f")
        q = re.sub(r'<div class="labtbl".*?</table>.*?</div>', "", f[1], flags=re.S)  # re-runnable
        rows = rows_of(q)
        if not rows:
            skipped += 1 if SPAN.search(q) else 0
            continue
        child = bool(CHILD.search(plain(q))) and not re.search(r"\b(1[89]|[2-9]\d)[- ]?(?:year|yr)", plain(q))
        for r in rows:  # adult cut-offs would mislabel a child's vitals, so no arrow there
            r["flag"] = "" if r["src"] or (child and r["cat"] == "Vitals" and r["name"] != "BMI") else flag(r["name"], r["val"], r["r"])
        tbl = table(rows, child)
        cut = q.rfind("<br/><br/>")
        f[1] = (q[:cut] + tbl + q[cut:]) if cut > 0 else q + tbl
        c.execute("update notes set flds = ?, mod = ?, usn = -1 where id = ?", ("\x1f".join(f), now, nid))
        done += 1
    c.commit()
    c.close()
    with open(dbp, "rb") as g, open(os.path.join(work, "collection.anki21b"), "wb") as f:
        f.write(zstandard.ZstdCompressor(level=3).compress(g.read()))
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_STORED) as z:
        for n in names:
            z.write(os.path.join(work, n), n)
    shutil.rmtree(work)
    print(f"{PART}: tables added to {done} questions; {skipped} had values but no recognised label ->", OUT)


if __name__ == "__main__":
    main()

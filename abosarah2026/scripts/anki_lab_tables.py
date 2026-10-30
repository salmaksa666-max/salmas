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


CATS = ["Vitals", "CBC", "Coagulation", "Glucose & endocrine", "Electrolytes & renal", "ABG", "Lipids", "Liver & pancreas",
        "Cardiac", "Immunology & other"]
# (label regex, shown name, category, range picker)
LABS = [
    (r"\bBP\b|blood pressure", "BP", "Vitals", lambda v: rng(None, None, "<120/80 · HTN ≥130/80 (AHA) or ≥140/90 (JNC)")),
    (r"\bHR\b|heart rate|pulse", "HR", "Vitals", lambda v: rng(60, 100, "60–100 /min")),
    (r"\bRR\b|resp\w* rate", "RR", "Vitals", lambda v: rng(12, 20, "12–20 /min")),
    (r"\btemp\w*", "Temp", "Vitals", lambda v: rng(36.1, 37.5, "36.1–37.5 °C")),
    (r"SpO2|O2 sat\w*|oxygen sat\w*|saturation", "SpO2", "Vitals", lambda v: rng(95, 100, "95–100%")),
    (r"\bBMI\b", "BMI", "Vitals", lambda v: rng(18.5, 24.9, "18.5–24.9 · obese ≥30")),
    (r"waist circumference", "Waist", "Vitals", lambda v: rng(None, 102, "men <102 · women <88 cm")),
    (r"hip circumference", "Hip", "Vitals", lambda v: rng(None, None, "waist:hip ratio — men <0.9 · women <0.85")),
    (r"\bheight\b", "Height", "Vitals", lambda v: rng(None, None, "percentile")),
    (r"\bweight\b", "Weight", "Vitals", lambda v: rng(None, None, "percentile")),
    (r"PA pressure|pulmonary artery pressure", "PA pressure", "Cardiac", lambda v: rng(None, 25, "mean <20–25 mmHg (pulmonary HTN above)")),
    (r"\bRDW\b", "RDW", "CBC", lambda v: rng(11.5, 14.5, "11.5–14.5%")),
    (r"retic\w*", "Reticulocytes", "CBC", lambda v: rng(0.5, 2.5, "0.5–2.5%")),
    (r"haptoglobin", "Haptoglobin", "CBC", lambda v: rng(0.3, 2.0, "0.3–2.0 g/L (low = hemolysis)")),
    (r"\bLDH\b", "LDH", "CBC", lambda v: rng(None, 250, "140–250 U/L")),
    (r"ferritin", "Ferritin", "CBC", lambda v: rng(30, 300, "30–300 ng/mL (<30 = iron deficiency)")),
    (r"eosinophil\w*(?: count)?", "Eosinophils", "CBC", lambda v: rng(None, 5, "1–5%")),
    (r"neutrophil\w*|\bANC\b", "Neutrophils", "CBC", lambda v: rng(1.5, 7.5, "1.5–7.5 ×10⁹/L (neutropenia <1.5)")),
    (r"\bINR\b", "INR", "Coagulation", lambda v: rng(0.8, 1.2, "0.8–1.2 · on warfarin 2–3 (2.5–3.5 mechanical mitral)")),
    (r"\baPTT\b|\bPTT\b", "aPTT", "Coagulation", lambda v: rng(25, 35, "25–35 s")),
    (r"\bPT\b", "PT", "Coagulation", lambda v: rng(11, 13.5, "11–13.5 s")),
    (r"bleeding time", "Bleeding time", "Coagulation", lambda v: rng(2, 7, "2–7 min")),
    (r"fibrinogen", "Fibrinogen", "Coagulation", lambda v: rng(2, 4, "2–4 g/L")),
    (r"uric acid", "Uric acid", "Electrolytes & renal", by_unit(20, rng(3.5, 7, "3.5–7 mg/dL"), rng(200, 420, "200–420 µmol/L"))),
    (r"phosph\w*", "Phosphate", "Electrolytes & renal", by_unit(3, rng(0.8, 1.5, "0.8–1.5 mmol/L"), rng(2.5, 4.5, "2.5–4.5 mg/dL"))),
    (r"\bMg\b|magnesium", "Mg", "Electrolytes & renal", lambda v: rng(0.7, 1.0, "0.7–1.0 mmol/L")),
    (r"\bCrCl\b|creatinine clearance", "CrCl", "Electrolytes & renal", lambda v: rng(90, None, ">90 mL/min · <30 = dose-adjust LMWH")),
    (r"urine protein|proteinuria", "Proteinuria", "Electrolytes & renal", lambda v: rng(None, 0.15, "<0.15 g/24h · nephrotic >3.5 g/24h")),
    (r"urine pH", "Urine pH", "Electrolytes & renal", lambda v: rng(4.5, 8, "4.5–8 (≥6.5 = alkaline)")),
    (r"\bESR\b", "ESR", "Immunology & other", lambda v: rng(None, 20, "<20 mm/hr (Kocher: >40)")),
    (r"\bCRP\b", "CRP", "Immunology & other", lambda v: rng(None, 10, "<10 mg/L")),
    (r"\bANA(?: titer)?", "ANA", "Immunology & other", lambda v: rng(None, None, "<1:80")),
    (r"\bRF\b|rheumatoid factor", "RF", "Immunology & other", lambda v: rng(None, 14, "<14 IU/mL")),
    (r"\bTSH\b", "TSH", "Glucose & endocrine", lambda v: rng(0.4, 4.0, "0.4–4.0 mIU/L")),
    (r"\bRBCs?\b|erythrocytes", "RBC", "CBC", lambda v: rng(4.2, 5.9, "4.2–5.9 ×10¹²/L")),
    (r"\bHb\b|\bHgb\b|ha?emoglobin", "Hb", "CBC", by_unit(25, rng(12, 17, "women 12–16 · men 13–17 g/dL"), rng(120, 170, "women 120–160 · men 130–170 g/L"))),
    (r"\bMCV\b", "MCV", "CBC", lambda v: rng(80, 100, "80–100 fL")),
    (r"\bMCH\b", "MCH", "CBC", lambda v: rng(27, 33, "27–33 pg")),
    (r"platelets?(?: count)?|\bPLTs?\b", "Platelets", "CBC", by_unit(1000, rng(150, 400, "150–400 ×10⁹/L"), rng(150000, 400000, "150,000–400,000 /µL"))),
    (r"\bWBCs?\b", "WBC", "CBC", by_unit(200, rng(4, 11, "4–11 ×10⁹/L"), rng(4000, 11000, "4,000–11,000 /µL"))),
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
    (r"(?:blood )?\bpH\b", "pH", "ABG", lambda v: rng(7.35, 7.45, "7.35–7.45")),
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
    (r"troponin", "Troponin", "Cardiac", lambda v: rng(None, None, "below the lab's 99th-percentile cut-off")),
    (r"CK-?MB", "CK-MB", "Cardiac", lambda v: rng(None, 5, "<5 ng/mL")),
    (r"\bEF\b|ejection fraction", "EF", "Cardiac", lambda v: rng(55, 70, "55–70% · HFrEF ≤40%")),
    (r"valve gradient|gradient", "Aortic valve gradient", "Cardiac", lambda v: rng(None, 40, "severe AS: mean ≥40 mmHg · very severe ≥60")),
    (r"ASCVD risk|risk of", "10-yr ASCVD risk", "Cardiac", lambda v: rng(None, None, "<5% low · 5–7.4 borderline · 7.5–19.9 intermediate · ≥20 high")),
]
RAW = LABS
LABS = [(re.compile(rf"(?:{p})\s*[:=(~]*\s*$", re.I), name, cat, fn) for p, name, cat, fn in LABS]
UNIT = r"(?:%|mmol/L|µmol/L|umol/L|mg/dL|g/dL|g/L|mEq/L|mmHg|mL/min|mIU/L|IU/mL|x ?10\^?9/L|×10⁹/L|/min|°C|ng/mL|U/L|IU/L|fL|pg|mm/hr|g/24 ?h\w*|cm|kg|sec|s(?![a-z]))"
LEAD = r"(?:\s|:|=|\(|is|was|now|still|of|level|count|titer|at|~|≈|about|around|only|initially|negative|positive|elevated|high|low|lower|higher|this time|significantly)*"
VALUE = re.compile(rf"{LEAD}(?P<v>1:\d[\d,]*|[<>≤≥~≈]?\s?\d[\d.,]*\+*(?:\s?[–-]\s?\d[\d.,]*)?(?:\s?/\s?\d{{2,3}}(?:[–-]\d{{2,3}})?)?(?:\s?{UNIT})?)", re.I)
SRC_AFTER = re.compile(r"\s*[(\[]\s*(?:[a-z ,]*?\b(?:normal|nl|N|ref\w*)\b[a-z ]*[:=]?\s*(?P<r>[<>≤≥~]?\s?\d[^)\]]{0,25})"
                       r"|(?P<r2>[<>≤≥]?\s?\d[\d.,]*\s?[–-]\s?\d[\d.,]*\s?[^\s)\]]{0,10}))\s*[)\]]", re.I)  # "(normal 3.5–5.0)" or "[130-170 g/L]"
ARROW = re.compile(r"\s*(?:\([^)]{0,20}\))?\s*(?:→|->)\s*(?P<v>[<>~]?\d[\d.,]*\s?[a-zµ/%]*)", re.I)  # "60 (1 week ago) → 160"
URINE_LINE = re.compile(r"\burin(?:e|alysis)\s*:|\burine\b[^,.;]{0,12}$", re.I)
ANY_LABEL = re.compile("|".join(f"(?P<g{i}>(?<![A-Za-z0-9])(?:{p})(?![A-Za-z]))" for i, (p, *_) in enumerate(RAW)), re.I)
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
    v = first_num(val.split("→")[-1])
    if v is None or (r["lo"] is None and r["hi"] is None):
        return ""
    if r["hi"] is not None and v > r["hi"]:
        return "↑"
    if r["lo"] is not None and v < r["lo"]:
        return "↓"
    return "✓"


FILLER = re.compile(r"(?:\s*(?:\(|\)|:|,|is|was|now|this time|lower|higher|negative|positive|elevated|high|low|level|count|of|about|around|only|significantly|≈|~))+\s*$", re.I)
URINE = {"RBC": "<3 /HPF", "Na": "<20 = volume depletion (prerenal)", "K": "<20 = GI loss · >20–30 = renal loss",
         "Cl": "<15–20 = saline-responsive (vomiting / NG suction)"}


def rows_of(q):
    """find "LABEL value" pairs in the question text (highlighted or not), in reading order"""
    t = plain(re.sub(r"<br\s*/?>", " ¶ ", q))
    rows, pos = [], 0
    while True:
        m = ANY_LABEL.search(t, pos)
        if not m:
            break
        pos = m.end()
        i = int(next(k for k, v in m.groupdict().items() if v)[1:])
        v = VALUE.match(t, m.end())
        if not v or len(v.group(0)) - len(v.group("v")) > 22:
            continue  # label without a number right after it
        val = v.group("v").strip().rstrip(".,")
        pos = v.end()
        a = ARROW.match(t, pos)
        if a:  # keep the trend, the arrow uses the latest number
            val += " → " + a.group("v").strip().rstrip(".,")
            pos = a.end()
        _, name, cat, fn = RAW[i]
        r = fn(first_num(val))
        line = t[t.rfind("¶", 0, m.start()) + 1:m.start()]
        if URINE_LINE.search(line) and name in URINE:
            name, r = "Urine " + name, rng(None, None, URINE[name])
        if name == "WBC" and re.search(r"arthrocentesis|synovial|joint fluid|aspirat", line, re.I):
            name, r = "Synovial WBC", rng(None, None, "<200 normal · 2,000–50,000 inflammatory · >50,000 septic")
        sa = SRC_AFTER.match(t, pos)
        src = (sa.group("r") or sa.group("r2")).strip() if sa else None
        if not any(x["name"] == name and x["val"] == val for x in rows):  # the same value quoted twice
            rows.append(dict(name=name, cat=cat, val=val, r=r, src=src))
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
        if len(rows) == 1 and not SPAN.search(q) and rows[0]["cat"] == "Vitals" and rows[0]["name"] in ("Weight", "Height"):
            continue
        child = bool(CHILD.search(plain(q))) and not re.search(r"\b(1[89]|[2-9]\d)[- ]?(?:year|yr)", plain(q))
        for r in rows:  # adult cut-offs would mislabel a child's vitals, so no arrow there
            if r["src"]:  # judge against the range the question itself gives
                m = re.match(r"\s*(?:(?P<lt><)\s*(?P<u>\d[\d.]*)|(?P<a>\d[\d.]*)\s*[–-]\s*(?P<b>\d[\d.]*))", r["src"])
                r["r"] = rng(float(m["a"]) if m and m["a"] else None, float(m["b"] or m["u"]) if m and (m["b"] or m["u"]) else None, "")
            r["flag"] = "" if (r["src"] and r["r"]["lo"] is None and r["r"]["hi"] is None) or (child and r["cat"] == "Vitals" and r["name"] != "BMI") else flag(r["name"], r["val"], r["r"])
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

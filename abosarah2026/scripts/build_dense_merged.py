# -*- coding: utf-8 -*-
"""Merge several dump_mkj.py item sets into one very dense PDF grouped by system -> topic, similar questions side by side.
Each question: number, stem, options inline (answer ticked), Alhomrani / card notes.
usage: build_dense_merged.py OUT.pdf TITLE ITEMS1.json:EXPL1.json[:TAG] ITEMS2.json:EXPL2.json[:TAG] ...
env: FS (font pt, default 6.3), COLS (default 3), MAP=out.json (writes qid -> [system, topic])"""
import glob
import html
import json
import os
import re
import subprocess
import sys
import tempfile

OUT, TITLE = sys.argv[1], sys.argv[2]
CHROME = sorted(glob.glob("/opt/pw-browsers/chromium_headless_shell-*/*/chrome-headless-shell"))[-1]
FS = float(os.environ.get("FS", "6.3"))
COLS = int(os.environ.get("COLS", "3"))

# system -> [(topic, regex)] ; order matters (first match wins inside the chosen system)
SYS = [
 ("Cardiology", r"heart|cardi|chest pain|myocard|coronary|angina|\becg\b|murmur|valv|aort|atrial|arrhythm|syncope|hypertens|blood pressure|stemi|troponin|statin|ldl|cholesterol|lipid|endocarditis|pericard|tachycard|bradycard|warfarin.*valve", [
   ("Hypertension", r"hypertens|blood pressure|\bbp\b|amlodipine|lisinopril|ace inhibitor|losartan|thiazide|resistant"),
   ("Lipids", r"ldl|cholesterol|lipid|statin|triglycer|ezetimibe|pcsk9"),
   ("IHD / ACS", r"chest pain|myocard|coronary|angina|stemi|troponin|st elevation|st depression|thromboly|pci\b"),
   ("Arrhythmia", r"atrial|fibrillation|flutter|arrhythm|tachycard|bradycard|block|qt\b|wpw|palpitat|syncope|cardioversion|amiodarone|digoxin"),
   ("Heart failure", r"heart failure|\bhf\b|ejection fraction|edema|furosemide|cardiomyopathy|bnp"),
   ("Valves / endocarditis", r"murmur|valv|stenosis|regurgit|endocarditis|prophylaxis|rheumatic"),
   ("Other cardiology", r".")]),
 ("Pulmonology", r"asthma|copd|lung|pulmonary|pneumon|pleural|dyspnea|shortness of breath|cough|wheez|spirometr|inhaler|sarcoid|bronch|oxygen|intubat|ventilat|ards|tuberc|\btb\b|embolism|\bpe\b|smok", [
   ("Asthma", r"asthma|inhaler|salbutamol|ics\b|wheez"),
   ("COPD", r"copd|emphysema|chronic bronchitis|fev1/fvc"),
   ("Pneumonia / TB", r"pneumon|tuberc|\btb\b|consolidation|ppd|igra|isoniazid|sputum"),
   ("PE / pleural", r"embolism|\bpe\b|pleural|effusion|pneumothorax|d-dimer|ctpa"),
   ("Respiratory failure / ICU", r"intubat|ventilat|ards|abg|respiratory failure|niv|bipap"),
   ("Other pulmonology", r".")]),
 ("GI & Hepatology", r"liver|hepat|cirrho|ascites|jaundice|pancrea|bowel|colitis|crohn|celiac|diarrh|constipat|dysphagia|esophag|gastr|stomach|ulcer|reflux|gerd|dyspepsia|h\.? ?pylori|colon|rectal|melena|hematemesis|varice|bilirubin|gallstone|biliary|abdominal pain", [
   ("Liver", r"liver|hepat|cirrho|ascites|varice|bilirubin|alt\b|ast\b|encephalopathy|hbv|hcv|hbsag|paracetamol"),
   ("Pancreas / biliary", r"pancrea|gallstone|biliary|cholangit|cholecyst|lipase|amylase"),
   ("Upper GI", r"dysphagia|esophag|gastr|stomach|peptic|ulcer|reflux|gerd|dyspepsia|pylori|hematemesis|ppi|omeprazole"),
   ("IBD / celiac / IBS", r"colitis|crohn|celiac|ibs\b|irritable|inflammatory bowel|gluten|ttg"),
   ("Colon / screening", r"colon|colorectal|polyp|rectal|colonoscopy|screening|melena|bleeding per rectum"),
   ("Other GI", r".")]),
 ("Nephrology & Electrolytes", r"kidney|renal|creatinine|nephr|proteinuria|hematuria|dialysis|egfr|\baki\b|\bckd\b|sodium|potassium|hyponat|hypernat|hyperkal|hypokal|calcium|acidosis|alkalosis|urin|stone", [
   ("Potassium / acid-base", r"potassium|hyperkal|hypokal|\bk\b|acidosis|alkalosis|bicarbonate|anion gap|abg"),
   ("Sodium / water", r"sodium|hyponat|hypernat|siadh|\bna\b|insipidus"),
   ("Calcium", r"calcium|hypercalc|hypocalc|parathyroid|pth"),
   ("AKI / CKD", r"aki\b|ckd\b|creatinine|dialysis|egfr|acute kidney|chronic kidney"),
   ("Glomerular / stones / UTI", r"nephrotic|nephritic|proteinuria|hematuria|glomerul|stone|calculi|uti\b|pyelo|urinary"),
   ("Other nephrology", r".")]),
 ("Endocrinology", r"diabet|insulin|glucose|hba1c|metformin|thyroid|tsh|graves|adrenal|cortisol|cushing|addison|pituitar|prolactin|acromegal|osteopor|vitamin d|testosteron|obes|bmi|hypoglyc|dka", [
   ("Diabetes", r"diabet|insulin|glucose|hba1c|metformin|hypoglyc|dka|sglt|glp|sulfonylurea"),
   ("Thyroid", r"thyroid|tsh|graves|t4\b|levothyrox|goiter|nodule|methimazole"),
   ("Adrenal / pituitary", r"adrenal|cortisol|cushing|addison|pituitar|prolactin|acromegal|pheochrom|aldosteron"),
   ("Bone / obesity", r"osteopor|vitamin d|dexa|bisphosph|obes|bmi|weight"),
   ("Other endocrinology", r".")]),
 ("Hematology & Oncology", r"anemia|hemoglobin|\bhb\b|ferritin|iron|b12|folate|platelet|thrombocyt|bleeding|coagul|warfarin|heparin|dvt|thrombo|leukemia|lymphoma|myeloma|sickle|thalass|g6pd|transfusion|cancer|tumou?r|malignan|chemo|neutropeni|polycyth|hemophilia|willebrand|inr", [
   ("Anemia", r"anemia|iron|ferritin|b12|folate|mcv|thalass|sickle|g6pd|hemoly|pernicious"),
   ("Bleeding / clotting / VTE", r"bleeding|coagul|warfarin|heparin|dvt|thrombo|platelet|itp|ttp|hemophilia|willebrand|inr|anticoag|doac|apixaban|rivaroxaban"),
   ("Leukemia / lymphoma / myeloma", r"leukemia|lymphoma|myeloma|polycyth|myeloprolif|lymph node|neutropeni"),
   ("Cancer / screening / TLS", r"cancer|tumou?r|malignan|chemo|tumor lysis|screening|metasta|palliat"),
   ("Other hematology", r".")]),
 ("Neurology", r"stroke|seizure|epilep|headache|migraine|dementia|alzheimer|parkinson|tremor|multiple sclerosis|myasthenia|guillain|neuropath|weakness|numbness|vertigo|meningitis|encephal|bell|cranial|consciousness|gcs|spinal|nerve", [
   ("Stroke / TIA", r"stroke|tia\b|hemipar|thrombolys|tpa|carotid|infarct|hemorrhage"),
   ("Seizures", r"seizure|epilep|convuls|status|valpro|levetir|phenytoin"),
   ("Headache", r"headache|migraine|cluster|tension"),
   ("Dementia / movement", r"dementia|alzheimer|parkinson|tremor|lewy|huntington|confusion|delirium"),
   ("Neuromuscular / MS", r"multiple sclerosis|myasthenia|guillain|neuropath|als\b|motor neuron|weakness|bell|optic neuritis"),
   ("Other neurology", r".")]),
 ("Infectious disease", r"fever|infection|antibiotic|hiv|hepatitis b vaccine|malaria|brucell|sepsis|meningit|syphilis|herpes|zoster|influenza|vaccin|cellulitis|abscess|osteomyel|travel|typhoid|dengue|covid|fungal|candid", [
   ("Vaccines / travel / exposure", r"vaccin|travel|hajj|prophylaxis|exposure|rabies|tetanus|needle"),
   ("HIV / STI", r"hiv|syphilis|gonorr|chlamydia|herpes|sexual"),
   ("Fever / sepsis / zoonoses", r"fever|sepsis|brucell|malaria|typhoid|dengue|q fever"),
   ("Skin / bone / soft tissue", r"cellulitis|abscess|osteomyel|zoster|wound|diabetic foot"),
   ("Other infections", r".")]),
 ("Rheumatology", r"arthritis|joint|gout|lupus|\bsle\b|vasculit|spondyl|scleroderma|myositis|polymyalgia|sjogren|raynaud|behcet|fibromyalg|back pain|osteoarth|knee|shoulder|hip", [
   ("Gout / crystal / septic", r"gout|uric|pseudogout|crystal|septic|aspirat|monoarthritis"),
   ("RA / SLE / connective tissue", r"rheumatoid|lupus|\bsle\b|scleroderma|sjogren|myositis|raynaud|methotrexate|anti-?ccp|ana\b"),
   ("Spondyloarthritis / back", r"spondyl|back pain|sacroil|reactive|psoria|ankylos"),
   ("Vasculitis / PMR", r"vasculit|giant cell|temporal|polymyalgia|behcet|kawasaki|wegener|granulomatosis"),
   ("OA / soft tissue", r"osteoarth|knee|shoulder|hip|fibromyalg|tendon|carpal"),
   ("Other rheumatology", r".")]),
]
SYSORDER = ["Hematology & Oncology", "Neurology", "Cardiology", "Pulmonology", "GI & Hepatology", "Infectious disease",
            "Rheumatology", "Endocrinology", "Nephrology & Electrolytes"]
GUIDE_FILE = "guides_medicine.txt"
if os.environ.get("SPEC") == "peds":  # Pediatrics systems/topics and guides
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from peds_systems import SYS, SYSORDER
    GUIDE_FILE = "guides_peds.txt"
elif os.environ.get("SPEC") in ("surgery", "obgyn"):
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import surgery_obgyn_systems as _so
    SYS, SYSORDER = (_so.SURGERY, _so.SURGERY_ORDER) if os.environ["SPEC"] == "surgery" else (_so.OBGYN, _so.OBGYN_ORDER)
    GUIDE_FILE = f"guides_{os.environ['SPEC']}.txt"
_by = {s: tps for s, _, tps in SYS}
ALL_TOPICS = [(s, t) for s in SYSORDER for t, _ in _by[s]] + [("Other", "Other")]
def load_basics(path):
    out, cur = {}, None
    for ln in open(path, encoding="utf-8").read().splitlines():
        if ln.startswith("== "):
            cur = ln[3:].strip()
            out[cur] = []
        elif cur and ln.strip():
            out[cur].append(ln.rstrip())
    return out


GUIDES = load_basics(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "review", GUIDE_FILE)) if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "review", GUIDE_FILE)) else {}


def render_flow(spec):
    """flow chart in the 'Masters' look.  spec: top -> top2 | Label: box \\ sub -> box | Label: ..."""
    parts = [x.strip() for x in spec.split(" | ")]

    def box(t, cls):
        ti, _, sub = t.partition("\\")
        return f'<div class="fb {cls}" dir="auto"><b>{gb(ti.strip())}</b>' + (f'<small>{gb(sub.strip())}</small>' if sub.strip() else "") + "</div>"
    top = '<div class="fa">↓</div>'.join(box(x, "f0") for x in parts[0].split("->") if x.strip())
    brs = ""
    for i, br in enumerate(parts[1:]):
        lab, _, chain = br.partition(":")
        brs += (f'<div class="fbr"><div class="flab" dir="auto">{gb(lab.strip())}</div><div class="fa">↓</div>'
                + '<div class="fa">↓</div>'.join(box(x, f"f{i % 4 + 1}") for x in chain.split("->") if x.strip()) + "</div>")
    return f'<div class="flow"><div class="ftop">{top}</div>' + (f'<div class="fbrs">{brs}</div>' if brs else "") + "</div>"


def render_tree(lines):
    """decision tree: indentation (2 spaces) = level; 'Label :: text \\ sub'; [r] [g] [b] [y] colour the box"""
    root, stack = [], []
    for ln in lines:
        ind = (len(ln) - len(ln.lstrip(" "))) // 2
        txt = ln.strip()
        lab = ""
        if " :: " in txt:
            lab, txt = txt.split(" :: ", 1)
        m = re.match(r"\[([rgby])\]\s*", txt)
        col = {"r": "f1", "g": "f2", "b": "f3", "y": "f4"}[m.group(1)] if m else "f0"
        if m:
            txt = txt[m.end():]
        node = dict(lab=lab, txt=txt, col=col, kids=[])
        stack = stack[:ind]
        (stack[-1]["kids"] if stack else root).append(node)
        stack.append(node)

    def draw(n):
        ti, _, sub = n["txt"].partition("\\")
        h = f'<div class="fb {n["col"]}" dir="auto"><b>{gb(ti.strip())}</b>' + (f'<small>{gb(sub.strip())}</small>' if sub.strip() else "") + "</div>"
        ks = n["kids"]
        if len(ks) == 2 and (not ks[0]["kids"]) != (not ks[1]["kids"]):  # one exit + one continuing branch: keep the chain vertical
            leaf, cont = (ks[0], ks[1]) if not ks[0]["kids"] else (ks[1], ks[0])
            lt, _, ls = leaf["txt"].partition("\\")
            lbox = f'<div class="fb {leaf["col"]}" dir="auto"><b>{gb(lt.strip())}</b>' + (f'<small>{gb(ls.strip())}</small>' if ls.strip() else "") + "</div>"
            h = (f'<div class="tside">{h}<div class="flab" dir="auto">{gb(leaf["lab"])} →</div>{lbox}</div>'
                 f'<div class="fa">↓ <span class="flab" dir="auto">{gb(cont["lab"])}</span></div>' + draw(cont))
            return f'<div class="tn">{h}</div>'
        if n["kids"]:
            h += '<div class="fa">↓</div><div class="tk' + (" multi" if len(n["kids"]) > 1 else "") + '">' + "".join(
                '<div class="tc">' + (f'<div class="flab" dir="auto">{gb(k["lab"])}</div>' if k["lab"] else "") + draw(k) + "</div>" for k in n["kids"]) + "</div>"
        return f'<div class="tn">{h}</div>'
    return '<div class="flow">' + "".join(draw(n) for n in root) + "</div>"


def render_guide(name, lines):
    h, tbl = "", []
    wide, cell, in_wide = "", None, False  # full-width area above the columns: :wide / :cell N / :end

    def flush():
        nonlocal h, tbl
        if tbl:
            mt = tbl[0].startswith("|=")
            rows = [[c.strip() for c in r.lstrip("|=").strip().strip("|").split("|")] for r in tbl]
            h += (f'<table class="mt">' if mt else "<table>") + "".join("<tr>" + "".join((f"<th>{gb(c)}</th>" if (i == 0 or (mt and j == 0)) else f"<td>{gb(c)}</td>") for j, c in enumerate(r)) + "</tr>" for i, r in enumerate(rows)) + "</table>"
            tbl = []

    def close_cell():
        nonlocal h, wide, cell
        flush()
        if cell is not None:
            wide += f'<div class="wc" style="flex:{cell} 1 0">{h}</div>'
            h, cell = "", None
    gold, plan, main, tree = "", "", "", None
    for ln in lines:
        if tree is not None:
            if ln.strip() == "/tree":
                h += render_tree(tree)
                tree = None
            else:
                tree.append(ln)
            continue
        if ln.strip() == "tree:":
            flush()
            tree = []
            continue
        if ln.startswith("|"):
            tbl.append(ln)
            continue
        flush()
        if ln.startswith(":wide"):
            main, h, in_wide = h, "", True
            wide += f'<div class="wtitle">{gb(ln[5:].strip())}</div><div class="wrow">' if ln[5:].strip() else '<div class="wrow">'
        elif ln.startswith(":cell"):
            close_cell()
            cell = ln[5:].strip() or "1"
        elif ln.startswith(":end"):
            close_cell()
            wide += "</div>"
            h, in_wide = main, False
        elif ln.startswith("flow: "):
            h += render_flow(ln[6:])
        elif ln.startswith("* "):  # English note line (Masters style)
            h += f'<div class="mn">{gb(ln[2:])}</div>'
        elif ln.startswith("## "):
            h += f'<div class="mh">{gb(ln[3:])}</div>'
        elif ln.startswith("@@ "):
            gold = gold.replace("</div>", f'<div class="kw">{gb(ln[3:])}</div></div>', 1) if gold else gold
        elif ln.startswith("@ "):
            gold = f'<div class="gx gold"><b class="t">القاعدة الذهبية</b>{gb(ln[2:])}</div>'
        elif ln.startswith("^ "):
            plan = f'<div class="gx gold plan"><b class="t">خطة أي سؤال</b><span class="gxt" dir="auto">{gb(ln[2:])}</span></div>'
        elif ln.startswith("# "):
            n, _, t = ln[2:].partition(" ")
            h += f'<h3><i>{n}</i>{gb(t)}</h3>'
        elif ln.startswith("!"):
            kind, _, rest = ln[1:].partition(" ")
            lab, _, txt = rest.partition(":")
            h += f'<div class="gx {kind}"><b class="t">{gb(lab)}</b><span class="gxt" dir="auto">{gb(txt.strip())}</span></div>'
        elif ln.startswith("- "):
            h += f'<div class="gl">• {gb(ln[2:])}</div>'
        elif ln.startswith("> "):  # plain explanation paragraph
            h += f'<p class="gp">{gb(ln[2:])}</p>'
        elif ln.startswith("%% "):  # worked example: English question || Arabic why
            q, _, why = ln[3:].partition("||")
            h += f'<div class="gex"><div class="gq">{gb(q.strip())}</div><b>ليش؟</b> {gb(why.strip())}</div>'
    flush()
    return (f'<div class="guide"><div class="ghead"><span>شرح {e(name)}</span><span class="gsub">افهمي القاعدة، بعدين حلي الأسئلة تحت</span></div>'
            f'{gold}{wide}<div class="gcols">{h}</div>{plan}</div>')


def gb(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\[(ok|no):(.*?)\]", lambda m: f'<span class="tag {m.group(1)}">{m.group(2)}</span>', t)
    t = re.sub(r"\{(.*?)\}", lambda m: f'<span class="en">{m.group(1)}</span>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"==(.+?)==", r'<span class="hl">\1</span>', t)
    return t


BASICS = load_basics(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "review", "basics_medicine.txt"))


def render_basics(lines):
    h, tbl = "", []

    def flush():
        nonlocal h, tbl
        if tbl:
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in tbl]
            h += "<table>" + "".join("<tr>" + "".join((f"<th>{bidi(c)}</th>" if i == 0 else f"<td>{bidi(c)}</td>") for c in r) + "</tr>" for i, r in enumerate(rows)) + "</table>"
            tbl = []
    for ln in lines:
        if ln.startswith("|"):
            tbl.append(ln)
            continue
        flush()
        if ln.startswith("! "):
            h += f'<div class="bi">{bidi(ln[2:])}</div>'
        elif ln.startswith("? "):
            h += f'<div class="bi how"><b>كيف تحلين:</b> {bidi(ln[2:])}</div>'
        elif ln.startswith("## "):
            h += f'<div class="bh">{bidi(ln[3:])}</div>'
        elif ln.startswith("> "):
            h += '<div class="bc">' + '<span class="ar">←</span>'.join(f'<span class="nd">{bidi(x.strip())}</span>' for x in ln[2:].split("→") if x.strip()) + "</div>"
        elif ln.startswith("- "):
            h += f'<div class="bl">• {bidi(ln[2:])}</div>'
        else:
            h += f"<div>{bidi(ln)}</div>"
    flush()
    return f'<div class="basic"><div class="btitle">الأساس (بيسك)</div>{h}</div>'


BOXES = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "review", "merged_topic_boxes.json"), encoding="utf-8"))
AR = re.compile(r"[\u0600-\u06ff]")
LAT = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’\-/.+%±:&]*(?: (?:[A-Za-z0-9±][A-Za-z0-9'’\-/.+%±:&]*|\+|/|=|–))*")


def bidi(t):
    out, last = "", 0
    for m in LAT.finditer(t):
        out += html.escape(t[last:m.start()], quote=False) + f'<bdi dir="ltr">{html.escape(m.group(0), quote=False)}</bdi>'
        last = m.end()
    return out + html.escape(t[last:], quote=False)


HIST = re.compile(r"(known (case )?(of|with)|k/c|history of|hx of|with|has|on)\s+(type ?[12] )?(hypertension|htn|diabetes( mellitus)?|dm|dyslipidemia|hyperlipidemia|smok\w*)(\s*(and|,|&)\s*(type ?[12] )?(hypertension|htn|diabetes( mellitus)?|dm|dyslipidemia|hyperlipidemia))*", re.I)


def classify(stem, opts, ans):
    stem_l = HIST.sub(" ", stem.lower())
    sents = re.split(r"(?<=[.?!])\s+", stem_l)
    lead = sents[-1] if sents else ""
    parts = ((ans.lower(), 3.0), (lead, 2.0), (" ".join(opts).lower(), 1.2), (stem_l, 1.0))
    best = None
    for s, rx, tps in SYS:
        sc = sum(w * len(re.findall(rx, t)) for t, w in parts)
        if sc and (best is None or sc > best[0]):
            best = (sc, s, tps)
    if not best:
        return "Other", "Other"
    tbest = None
    for i, (tname, trx) in enumerate(best[2][:-1]):
        sc = sum(w * len(re.findall(trx, t)) for t, w in parts)
        if sc and (tbest is None or sc > tbest[0]):
            tbest = (sc, tname)
    return best[1], (tbest[1] if tbest else best[2][-1][0])


SKIP = re.compile(r"^(Other versions? of this recall|↻|Same question as|The same question reappears|Same-version)", re.I)
META = re.compile(r"^(Printed|Compiler|Recaller|Embedded|Inset|Answer (tagged|from|line|options?)|Handwritten|Source|Screenshot|Question-bank|October By Similar|MG |GB |Old recall|Slide|Image|Phone photo|Note options|Options? |Only |No (printed|answer|compiler)|Partial|Terse|Stem|Short|Long|Version|Same|Reference|The (compiler|recaller|stem|options?|printed)|Contributor|Highlighted|Circled|Red|Bold|Underlined|Arabic|\(|Literally|Text)", re.I)
DIFF = re.compile(r"different answer|gives a different|answer (differs|changes)|MODIFIED", re.I)
RULE = re.compile(r"\bif\b|→|->|rather than|instead of|\bnot\b|\bunless\b|= |\bbecause\b|\bpreferred\b|first[- ]line|contraindicat", re.I)
items = []
for spec in sys.argv[3:]:
    parts = spec.split(":")
    its, ex = json.load(open(parts[0], encoding="utf-8")), json.load(open(parts[1], encoding="utf-8"))
    tag = parts[2] if len(parts) > 2 else ""
    for it in its:
        s, tp = (it["sys"], it["topic"]) if "sys" in it else classify(it["stem"], [o for _, o in it["opts"]], it["ans"])
        exq = ex.get(it["qid"], {})
        sents = re.split(r"(?<=[.;])\s+(?=[A-Z↑↻])", exq.get("author", ""))
        keep = []
        for x in sents:
            x = x.strip()
            if not x or SKIP.match(x) or META.match(x):
                continue
            if DIFF.search(x) or RULE.search(x):
                keep.append(x)
        note = " ".join(keep)[:int(os.environ.get("NOTE_MAX", "230"))]
        if os.environ.get("NOANS_NOTES") and it["ans"].startswith("—"):  # no firm answer: keep Alhomrani's full words, they carry the conditional rule
            note = " ".join(x.strip() for x in sents if x.strip() and not SKIP.match(x.strip()))
        if os.environ.get("DROP_NOANS") and it["ans"].startswith("—"):
            continue
        items.append(dict(it, sys=s, topic=tp, note=note, tag=it.get("tag") or tag, key=exq.get("key", ""), rule=exq.get("rule", ""), decide=exq.get("decide", [])))

order = {k: i for i, k in enumerate(ALL_TOPICS)}
import numpy as np
from collections import Counter, defaultdict
TOK = re.compile(r"[a-z][a-z0-9\-]{2,}")
STOP = set("the and with for was has his her are this that which following most appropriate next step what patient presents presented year old years woman man male female history examination management diagnosis likely best initial".split())
docs = [[w for w in TOK.findall((it["ans"] + " ") * 3 + it["stem"].lower() + " " + " ".join(o for _, o in it["opts"]).lower()) if w not in STOP] for it in items]
df = Counter(w for d in docs for w in set(d))
N = len(docs)
vecs = []
vocab = {w: i for i, w in enumerate(df)}
for d in docs:
    c = Counter(d)
    v = {vocab[w]: (1 + np.log(n)) * np.log(N / df[w]) for w, n in c.items()}
    nrm = np.sqrt(sum(x * x for x in v.values())) or 1
    vecs.append({k: x / nrm for k, x in v.items()})
cos = lambda a, b: sum(x * b.get(k, 0) for k, x in a.items()) if len(a) < len(b) else sum(x * a.get(k, 0) for k, x in b.items())
groups = defaultdict(list)
for i, it in enumerate(items):
    groups[(it["sys"], it["topic"])].append(i)
ordered = list(range(len(items))) if os.environ.get("PRESET") else []
for g in ([] if os.environ.get("PRESET") else sorted(groups, key=lambda k: order.get(k, 999))):
    rest = groups[g][:]
    cur = rest.pop(0)
    chain = [cur]
    while rest:  # greedy nearest neighbour -> similar questions side by side
        j = max(range(len(rest)), key=lambda r: cos(vecs[cur], vecs[rest[r]]))
        cur = rest.pop(j)
        chain.append(cur)
    ordered += chain
# October questions that match a September one (same recall): badge, and flag when the answer differs
V = len(vocab)
Mx = np.zeros((N, V), dtype=np.float32)
for i, v in enumerate(vecs):
    for k, x in v.items():
        Mx[i, k] = x
tags_ = np.array([it["tag"] for it in items])
sep_i, oct_i = np.where(tags_ == "Sep")[0], np.where(tags_ == "Oct")[0]
if len(sep_i) and len(oct_i):
    sim = Mx[oct_i] @ Mx[sep_i].T
    na = lambda t: re.sub(r"[^a-z0-9]", "", re.sub(r"^[a-e][.)\-]\s*", "", t.lower()))[:14]
    for r, i in enumerate(oct_i):
        j = int(sim[r].argmax())
        if sim[r, j] >= 0.75:
            items[i]["same"] = "same" if na(items[i]["ans"]) == na(items[sep_i[j]]["ans"]) else "diff"
items = [items[i] for i in ordered]
if os.environ.get("DROP_SAME"):  # drop October copies of a September question with the same answer (keep the Sep one)
    print("dropped", sum(1 for it in items if it.get("same") == "same"), "October repeats with the same answer")
    items = [it for it in items if it.get("same") != "same"]
if os.environ.get("ONLY_SYS"):  # one system only (sample / single-topic file)
    items = [it for it in items if it["sys"] == os.environ["ONLY_SYS"]]
if os.environ.get("LIMIT"):
    items = items[int(os.environ.get("SKIP", "0")):int(os.environ.get("SKIP", "0")) + int(os.environ["LIMIT"])]
if os.environ.get("MAP"):
    json.dump({it["qid"]: [it["sys"], it["topic"]] for it in items}, open(os.environ["MAP"], "w"), ensure_ascii=False)
    if os.environ.get("MAP_ONLY"):
        sys.exit(0)

e = lambda t: html.escape(t, quote=False)
TOC = []
for i, it in enumerate(items):
    it["n"] = i + 1


def kvec(t):
    c = Counter(w for w in TOK.findall(t.lower()) if w not in STOP)
    v = {w: (1 + np.log(x)) * np.log(N / df.get(w, 1)) for w, x in c.items()}
    nr = np.sqrt(sum(a * a for a in v.values())) or 1
    return {w: a / nr for w, a in v.items()}


def summary(group):
    """one bubble line per idea (key concept), similar ideas merged, with the question numbers"""
    ideas = []
    for it in group:
        k = (it.get("key") or "").strip()
        if not k:
            continue
        kv = kvec(k)
        for idea in ideas:
            if cos(kv, idea["v"]) >= 0.5:
                idea["q"].append(it["n"])
                break
        else:
            ideas.append(dict(t=k, v=kv, q=[it["n"]]))
    ideas.sort(key=lambda d: (-len(d["q"]), d["q"][0]))
    out = ""
    for d in ideas:
        t = re.sub(r"\.$", "", d["t"])
        m = re.match(r"(.{6,120}?)(?::\s| = | -> | → )(.+)", t)
        nodes = [m.group(1), m.group(2)] if m else [t]
        qs = "، ".join(str(x) for x in d["q"][:12]) + ("…" if len(d["q"]) > 12 else "")
        out += ('<div class="ch">' + '<span class="ar">→</span>'.join(f'<span class="nd">{e(x.strip())}</span>' for x in nodes)
                + f'<span class="qn">Q {qs}</span></div>')
    return f'<div class="bx sum">{out}</div>' if out else ""


def ideas(group):
    """IDEAS=1: one line per idea (similar key concepts merged), most repeated first: ✔ answer — key ×N"""
    gs = []
    for it in group:
        k = (it.get("key") or it.get("rule") or it["stem"][:160]).strip()
        a = re.sub(r"^[A-Fa-f][.)\-]\s*", "", it["ans"].strip())
        if a.startswith("—"):
            continue
        v = kvec(k + " " + a)
        for g in gs:
            if cos(v, g["v"]) >= 0.45:
                g["items"].append((k, a, it))
                break
        else:
            gs.append(dict(v=v, items=[(k, a, it)]))
    gs.sort(key=lambda g: -len(g["items"]))
    out = ""
    for g in gs:
        ans = Counter(a.lower().rstrip(".") for _, a, _ in g["items"])
        top = [x for x, _ in ans.most_common(2)]
        shown = [next(a for _, a, _ in g["items"] if a.lower().rstrip(".") == t) for t in top]
        key = min((k for k, _, _ in g["items"]), key=len)
        key = key if len(key) <= 190 else key[:187] + "…"
        flag = (" ⚠" if any(i.get("filled") for _, _, i in g["items"]) else "") + (" ✏" if any(i.get("corrected") for _, _, i in g["items"]) else "")
        n = len(g["items"])
        out += (f'<div class="idl">' + (f'<span class="idn">×{n}</span>' if n > 1 else "") + f'<b>✔ {e(shown[0][:90])}</b>'
                + (f' <span class="ida">/ {e(shown[1][:60])}</span>' if len(shown) > 1 else "") + f'{flag} <span class="idk">{e(key)}</span></div>')
    return out


if os.environ.get("DEDUP"):  # merge near-identical questions (same topic, same answer text, very similar stem) into one with ×N
    th, kept, last = float(os.environ["DEDUP"]), [], {}
    for it in items:
        a = re.sub(r"^[A-Fa-f][.)\-]\s*", "", it["ans"].strip()).lower().rstrip(".")
        v = kvec(it["stem"])
        hit = None
        for k in last.get((it["sys"], it["topic"], a), []):
            if cos(v, k["_v"]) >= th:
                hit = k
                break
        if hit and not a.startswith("—"):
            hit["_n"] = hit.get("_n", 1) + 1
            if it.get("xnote") and not hit.get("xnote"):
                hit["xnote"] = it["xnote"]
            continue
        it["_v"] = v
        last.setdefault((it["sys"], it["topic"], a), []).append(it)
        kept.append(it)
    print("DEDUP merged", len(items) - len(kept), "near-identical questions")
    items = kept
    for i, it in enumerate(items):
        it["n"] = i + 1
by_topic = defaultdict(list)
for it in items:
    by_topic[(it["sys"], it["topic"])].append(it)
body, cur_s, cur_t = "", None, None
for it in items:
    if it["sys"] != cur_s:
        TOC.append([it["sys"], None, 0])
        body += f'<div class="sh">{e(it["sys"])}<span class="mk">@@M{len(TOC) - 1}@@</span></div>'
        if GUIDES.get(it["sys"]) and not os.environ.get("NOGUIDE"):
            body += render_guide(it["sys"], GUIDES[it["sys"]])
        cur_s, cur_t = it["sys"], None
    if it["topic"] != cur_t:
        TOC.append([it["sys"], it["topic"], 0])
        body += f'<div class="th">{e(it["topic"])}<span class="mk">@@M{len(TOC) - 1}@@</span></div>'
        if not os.environ.get("NOBASICS") and BASICS.get(it["topic"]):
            body += render_basics(BASICS[it["topic"]])
        elif False and BOXES.get(it["topic"]):
            body += '<div class="bx">' + "".join(
                '<div class="ch" dir="rtl">' + '<span class="ar">←</span>'.join(
                    f'<span class="nd" dir="{"rtl" if AR.search(nd) else "ltr"}">{bidi(nd.strip()) if AR.search(nd) else e(nd.strip())}</span>'
                    for nd in x.split("→") if nd.strip()) + "</div>" for x in BOXES[it["topic"]]) + "</div>"
        cur_t = it["topic"]
        if os.environ.get("IDEAS"):
            body += ideas(by_topic[(it["sys"], it["topic"])])
    n = it["n"]
    TOC[-1][2] += 1
    if os.environ.get("IDEAS"):
        continue
    ans = it["ans"].strip()
    o = ""
    hit = False
    for k, t in it["opts"]:
        ok = bool(re.match(rf"{k}[.)\-]", ans))
        hit = hit or ok
        if os.environ.get("ANSONLY") and not ok:
            continue
        o += f' <span class="{"ok" if ok else "op"}">{'<span class="ck">✔</span>' if ok else ""}{k}. {e(t)}</span>'
    if not hit:
        o += f' <span class="ok"><span class="ck">✔</span> {e(ans)}</span>'
    rp = f'<span class="rp">مكرر {e(it["rep"])}</span> ' if it.get("rep") else ""
    tg = f'<span class="tg">{e(it["tag"])}</span>' if it["tag"] else ""
    if it.get("same") == "same":
        tg += '<span class="sm">= Sep</span>'
    elif it.get("same") == "diff":
        tg += '<span class="sm df">≈ Sep: جواب مختلف ⚠</span>'
    if os.environ.get("NOANS_NOTES") and (ans.startswith("—") or it.get("filled")):
        def tidy(c):
            c = re.sub(r"^.{0,90}?\b(is|are|would be)\s+(?=(right|wrong|correct|incorrect|the answer|reserved|appropriate|indicated|only|not)\b)", "", c, 1)
            for a, b in (("right only when", "✔ only when"), ("right only for", "✔ only for"), ("right only if", "✔ only if"), ("right when", "✔ when"), ("right for", "✔ for"),
                         ("right if", "✔ if"), ("right in", "✔ in"), ("wrong", "✘"), ("incorrect", "✘"), ("correct when", "✔ when"), ("the answer when", "✔ when")):
                if c.lower().startswith(a):
                    return b + c[len(a):]
            return c
        rules = "".join(f'<div class="rl">• <b>{e(o)}</b> → <span dir="ltr">{e(tidy(c))}</span></div>' for o, c in it.get("decide", []))
        if not rules and it.get("key"):
            rules = "".join(f'<div class="rl">• {e(x.strip())}</div>' for x in re.split(r";\s*|(?<=\.)\s+(?=[A-Z])", it["key"]) if x.strip())
        nt = ('<div class="hbox"><div class="hh">' + ("⚠ ما كان له جواب بالمصدر ← الجواب فوق مني، وهذي القاعدة" if it.get("filled") else "⚠ ما فيه جواب أكيد ← احفظي القاعدة") + '</div>'
              + (f'<div class="hs">قاعدة الحمراني (متى يكون كل خيار صح):</div>{rules}' if rules else "")
              + (f'<div class="hq"><b>✍ الحمراني قال:</b> {e(it["note"][:260])}</div>' if it["note"] else "")
              + "</div>")
    else:
        nt = (f'<div class="nt">💡 {e(it["rule"])}</div>' if it.get("rule") else "") + (f'<div class="nt">✍ {e(it["note"])}</div>' if it["note"] else "")
    if it.get("set_first") and it.get("set"):
        st = it["set"]
        body += (f'<div class="lset"><div class="lsh">Look-alike set {st["n"]} · {e(st["title"])}</div>'
                 f'<b>How to tell them apart:</b> {e(st["how"])}</div>')
    if os.environ.get("NONOTES"):
        nt = ""
    nt = it.get("xnote", "") + nt
    if it.get("_n", 1) > 1:
        tg += f'<span class="rp">×{it["_n"]}</span> '
    body += f'<div class="q"><b>{n}.</b>{tg} {rp}{e(it["stem"])}{it["flag"]}{o}{nt}</div>'
n = len(items)

FONTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "fonts")
FONTS = os.path.abspath(FONTS)
CSS = f"""
@page {{ size: {os.environ.get('PAGE', 'A4')}; margin: 5mm 5mm 6mm; }}
* {{ box-sizing: border-box; }}
body {{ font-family: "DejaVu Sans", Arial, sans-serif; font-size: {FS}pt; line-height: {os.environ.get("LH", "1.13")}; margin: 0; color: #000; }}
.top {{ display: flex; justify-content: space-between; font-weight: bold; font-size: 9pt; border-bottom: 1.2pt solid #000; margin-bottom: .8mm; }}
.cols {{ column-count: {COLS}; column-gap: {os.environ.get("GAP", "2.6")}mm; column-rule: .3pt solid #888; }}
.sh {{ background: #000; color: #fff; font-weight: bold; font-size: 1.25em; padding: .3mm 1.2mm; margin: .8mm 0 .3mm; break-after: avoid; }}
.th {{ border-bottom: .8pt solid #000; font-weight: bold; margin: .6mm 0 .2mm; break-after: avoid; }}
.q {{ border-bottom: .25pt solid #999; padding: {os.environ.get('QP', '.25')}mm 0 {os.environ.get('QP', '.35')}mm; break-inside: avoid; }}
.op {{ color: #222; }}
.ok {{ font-weight: bold; text-decoration: underline; }}
.rp {{ border: .6pt solid #000; border-radius: .8mm; padding: 0 .6mm; font-weight: bold; direction: rtl; unicode-bidi: isolate; }}
.tg {{ font-size: .85em; border: .4pt solid #000; padding: 0 .4mm; margin-left: .6mm; }}
.bx {{ direction: rtl; text-align: right; border: 1pt solid #000; border-radius: 1.2mm; padding: .5mm 1mm; margin: .4mm 0 1mm; font-size: .98em; line-height: 1.2; break-inside: avoid; background: #eee; }}
.ch {{ display: flex; flex-wrap: wrap; align-items: center; gap: .5mm; margin: .5mm 0; padding-bottom: .5mm; border-bottom: .3pt dotted #888; }}
.ch:last-child {{ border-bottom: none; }}
.nd {{ border: .6pt solid #000; border-radius: .9mm; padding: .1mm .9mm; background: #fff; unicode-bidi: isolate; }}
.ar {{ font-weight: bold; }}
@font-face {{ font-family: Plex; font-weight: 400; src: url(file://{FONTS}/ibm-plex-sans-arabic-arabic-400-normal.woff2); unicode-range: U+0600-06FF, U+FB50-FDFF, U+FE70-FEFF; }}
@font-face {{ font-family: Plex; font-weight: 700; src: url(file://{FONTS}/ibm-plex-sans-arabic-arabic-700-normal.woff2); unicode-range: U+0600-06FF, U+FB50-FDFF, U+FE70-FEFF; }}
@font-face {{ font-family: Plex; font-weight: 400; src: url(file://{FONTS}/ibm-plex-sans-arabic-latin-400-normal.woff2); unicode-range: U+0000-024F, U+2000-22FF; }}
@font-face {{ font-family: Plex; font-weight: 700; src: url(file://{FONTS}/ibm-plex-sans-arabic-latin-700-normal.woff2); unicode-range: U+0000-024F, U+2000-22FF; }}
.guide {{ column-span: all; font-family: Plex, "DejaVu Sans", sans-serif; font-size: 8.3pt; line-height: 1.45; direction: rtl; text-align: right; color: #000; border: 1.4pt solid #000; border-radius: 2mm; padding: 2mm 3mm; margin: 1mm 0 2.5mm; background: #fff; }}
.ghead {{ display: flex; justify-content: space-between; align-items: flex-end; border-bottom: 2pt solid #000; padding-bottom: .6mm; margin-bottom: 1.5mm; font-size: 15pt; font-weight: 700; }}
.gsub {{ font-size: 8pt; font-weight: 400; color: #444; }}
.gcols {{ column-count: {os.environ.get("GCOLS", "2")}; column-gap: 4mm; }}
.guide h3 {{ font-size: 10pt; margin: 1.6mm 0 .8mm; display: flex; align-items: center; gap: 1.6mm; break-after: avoid; }}
.guide h3 i {{ font-style: normal; background: #000; color: #fff; width: 4.6mm; height: 4.6mm; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; font-size: 7.5pt; flex: none; }}
.guide table {{ width: 100%; border-collapse: separate; border-spacing: 0; border: 1px solid #555; border-radius: 1.6mm; overflow: hidden; margin: .5mm 0 1.2mm; break-inside: avoid; }}
.guide th {{ background: #e3e3e3; font-weight: 700; }}
.guide td, .guide th {{ padding: .55mm 1.6mm; border-bottom: 1px solid #bbb; vertical-align: top; text-align: right; }}
.guide tr:last-child td {{ border-bottom: none; }}
.wrow {{ display: flex; gap: 3mm; align-items: flex-start; margin: 1mm 0 2mm; direction: ltr; break-inside: avoid; }}
.tside {{ display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 1.2mm; max-width: 100%; }}
.gxt {{ display: block; unicode-bidi: plaintext; }}
.tside > .fb {{ min-width: 0; }}
.wtitle {{ break-after: avoid; }}
.wc {{ min-width: 0; }}
.wtitle {{ font-weight: 700; font-size: 10pt; margin: 1.5mm 0 .5mm; border-right: 4px solid #2b6f8f; padding-right: 2mm; }}
.guide table.mt {{ direction: ltr; border: 1px solid #5b6770; font-size: 7.6pt; line-height: 1.3; }}
.guide table.mt th, .guide table.mt td {{ text-align: left; padding: .7mm 1.4mm; border-right: 1px solid #c9ced2; }}
.guide table.mt tr:first-child th {{ background: #4a545c; color: #fff; text-align: center; }}
.guide table.mt tr:not(:first-child) th {{ background: #eef1f3; min-width: 15mm; }}
.guide table.mt tr:nth-child(odd) td {{ background: #fafbfc; }}
.guide .hl {{ background: #ffe89a; padding: 0 .6mm; border-radius: .6mm; }}
.mn {{ direction: ltr; text-align: left; font-size: 8pt; line-height: 1.35; margin: .5mm 0; padding: .6mm 1.6mm; border-left: 3px solid #2b6f8f; background: #f1f7fa; border-radius: 0 1.2mm 1.2mm 0; break-inside: avoid; }}
.mh {{ direction: ltr; text-align: left; font-weight: 700; font-size: 8.6pt; margin: 1.2mm 0 .4mm; color: #1d4e66; }}
.flow {{ direction: ltr; text-align: center; margin: 1mm 0 1.5mm; break-inside: avoid; font-size: 7.6pt; line-height: 1.25; }}
.ftop {{ display: flex; flex-direction: column; align-items: center; }}
.fbrs {{ display: flex; gap: 2mm; justify-content: center; align-items: flex-start; border-top: 1.2pt solid #666; margin-top: 1mm; padding-top: .6mm; }}
.fbr {{ flex: 1 1 0; display: flex; flex-direction: column; align-items: center; min-width: 0; }}
.flab {{ font-weight: 700; color: #444; font-size: 7.2pt; }}
.fa {{ line-height: 1; color: #555; font-size: 9pt; }}
.fb {{ border: 1.1pt solid #888; border-radius: 1.6mm; padding: .8mm 2mm; background: #eeeee8; max-width: 100%; }}
.fb small {{ display: block; font-size: 6.8pt; font-weight: 400; }}
.fb.f1 {{ background: #fbe9e4; border-color: #b96a55; color: #6a2a1a; }}
.fb.f2 {{ background: #e2f3ee; border-color: #4f9483; color: #17493d; }}
.fb.f3 {{ background: #e6eefb; border-color: #5b7fc0; color: #1e3a70; }}
.fb.f4 {{ background: #fdf3d3; border-color: #c2a03a; color: #5c4705; }}
.tn {{ display: flex; flex-direction: column; align-items: center; min-width: 0; }}
.tk {{ display: flex; gap: 1.6mm; justify-content: center; align-items: flex-start; }}
.tk.multi {{ border-top: 1.1pt solid #777; padding-top: .5mm; }}
.tc {{ flex: 1 1 0; display: flex; flex-direction: column; align-items: center; min-width: 0; }}
.idl {{ break-inside: avoid; padding: .35mm 0 .35mm 1mm; border-bottom: .5pt solid #ccc; }}
.idn {{ float: right; font-weight: 700; background: #000; color: #fff; border-radius: 1.2mm; padding: 0 1mm; margin-left: 1mm; font-size: .9em; }}
.ida {{ color: #333; }}
.idk {{ color: #222; }}
.gx {{ padding: 1.4mm 2.4mm; border-radius: 1.6mm; margin: 1mm 0; border: 1px solid #000; border-right-width: 3.5px; break-inside: avoid; }}
.gx .t {{ display: block; margin-bottom: .2mm; }}
.gx.gold {{ background: #ececec; }}
.gx.mem {{ background: #fff; border-style: solid; }}
.gx.warn {{ background: #fff; border-style: dashed; border-right-style: solid; }}
.gx.warn .t::before {{ content: "⚠ "; }}
.gx.mem .t::before {{ content: "✎ "; }}
.gl {{ margin: .4mm 0; }}
.gp {{ margin: .6mm 0 .9mm; }}
.gx.why {{ background: #f0f0f0; }}
.gx.why .t::before {{ content: "؟ "; }}
.gex {{ border: 1px dashed #000; border-radius: 1.6mm; padding: 1mm 2.2mm; margin: 1mm 0; break-inside: avoid; }}
.gq {{ direction: ltr; text-align: left; font-style: italic; font-size: .93em; border-bottom: 1px dotted #888; padding-bottom: .6mm; margin-bottom: .6mm; }}
.kw {{ margin-top: .6mm; padding-top: .5mm; border-top: .5pt dotted #000; }}
.guide .tag {{ display: inline-block; padding: 0 1.4mm; border-radius: 2mm; font-weight: 700; border: .8pt solid #000; }}
.guide .tag.ok {{ background: #fff; }}
.guide .tag.no {{ background: #000; color: #fff; }}
.guide .tag .en {{ color: inherit; }}
.guide .en {{ direction: ltr; unicode-bidi: isolate; font-weight: 700; }}
.basic {{ column-span: all; column-count: 2; column-gap: 6mm; direction: rtl; text-align: right; border: 1.2pt solid #000; border-radius: 2mm; padding: 1.5mm 2.5mm; margin: .8mm 0 1.6mm; font-size: 1.08em; line-height: 1.38; background: #fafafa; }}
.btitle {{ column-span: all; font-weight: bold; font-size: 1.1em; border-bottom: .8pt solid #000; margin-bottom: 1mm; }}
.bi {{ border: .9pt solid #000; border-radius: 1.5mm; padding: .8mm 1.8mm; background: #eee; margin: .8mm 0; break-inside: avoid; }}
.bi.how {{ background: #e4e4e4; }}
.bh {{ display: inline-block; background: #000; color: #fff; font-weight: bold; padding: .2mm 1.8mm; border-radius: 1mm; margin: 1.2mm 0 .4mm; break-after: avoid; }}
.bc {{ display: flex; flex-wrap: wrap; align-items: center; gap: .8mm; margin: .8mm 0; break-inside: avoid; }}
.bc .nd {{ border: .8pt solid #000; border-radius: 1.4mm; padding: .2mm 1.4mm; background: #fff; }}
.bl {{ margin: .4mm 0; }}
.basic table {{ border-collapse: collapse; width: 100%; margin: .8mm 0; break-inside: avoid; }}
.basic td, .basic th {{ border: .6pt solid #000; padding: .4mm 1.2mm; vertical-align: top; }}
.basic th {{ background: #ddd; }}
.bx.sum {{ direction: ltr; text-align: left; background: #f7f7f7; break-inside: auto; }}
.ch {{ break-inside: avoid; }}
.qn {{ font-size: .8em; color: #333; margin-left: .8mm; white-space: nowrap; }}
.slab {{ direction: rtl; text-align: right; font-weight: bold; font-size: .9em; margin-top: .5mm; }}
.sm {{ font-size: .82em; border: .4pt dashed #000; padding: 0 .4mm; margin-left: .5mm; }}
.sm.df {{ font-weight: bold; border-style: solid; }}
.mk {{ color: #fff; font-size: 1pt; }}
.hbox {{ border: 1.4pt solid #000; border-radius: 1.4mm; padding: .8mm 1.4mm; margin-top: .6mm; background: #f0f0f0; }}
.hh {{ direction: rtl; text-align: right; font-weight: bold; border-bottom: .6pt solid #000; margin-bottom: .4mm; }}
.hs {{ direction: rtl; text-align: right; font-weight: bold; font-size: .92em; }}
.rl {{ margin: .3mm 0 .3mm 1mm; direction: ltr; text-align: left; }}
.hq {{ font-size: .9em; font-style: italic; margin-top: .4mm; border-top: .4pt dotted #000; padding-top: .3mm; }}
.na {{ direction: rtl; text-align: right; font-weight: bold; margin-top: .3mm; }}
.nah {{ font-style: normal; border-left-width: 1.6pt; }}
.lset {{ border: 1.4pt solid #000; border-radius: 1.4mm; padding: .7mm 1.4mm; margin: .8mm 0 .4mm; background: #e9e9e9; break-inside: avoid; font-size: .96em; }}
.lsh {{ font-weight: bold; border-bottom: .6pt solid #000; margin-bottom: .3mm; }}
.nt.fx, .nt.ed {{ font-style: normal; border-left: none; border-right: 1.8pt solid #000; padding: 0 .8mm 0 0; direction: rtl; text-align: right; unicode-bidi: isolate; }}
.nt {{ font-size: .92em; font-style: italic; color: #111; border-left: .9pt solid #000; padding-left: .8mm; margin-top: .15mm; }}
"""
if os.environ.get("MASK"):  # same layout, answer areas painted pure red so their boxes can be found on each page
    CSS += """
.ok, .nt, .hbox, .na { background: #ff0000 !important; }
"""
if os.environ.get("HIDE_ANS"):  # same layout, answers blanked (space kept so pages match the answer copy)
    CSS += """
.ck, .nt, .hbox, .na { visibility: hidden; }
.ok { text-decoration: none; font-weight: normal; }
"""
doc = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
       f'<div class="top"><span>{e(TITLE)}</span><span>{n} سؤال</span></div><div class="cols">{body}</div></body></html>')
if os.environ.get("HTML_OUT"):
    import base64
    hb = re.sub(r'<span class="mk">@@M(\d+)@@</span>', lambda m: f'<a id="m{m.group(1)}"></a>', body)
    fcss = ""
    for w8 in ("400", "700"):
        for sub, rng in (("arabic", "U+0600-06FF, U+FB50-FDFF, U+FE70-FEFF"), ("latin", "U+0000-024F, U+2000-22FF")):
            b64 = base64.b64encode(open(os.path.join(FONTS, f"ibm-plex-sans-arabic-{sub}-{w8}-normal.woff2"), "rb").read()).decode()
            fcss += f"@font-face {{ font-family: Plex; font-weight: {w8}; src: url(data:font/woff2;base64,{b64}) format('woff2'); unicode-range: {rng}; }}\n"
    scss = re.sub(r"@font-face \{[^}]*\}", "", CSS).replace("@page", "@media print { @page") .replace("}\n* {", "} }\n* {", 1)
    sysq2 = {}
    for sy, tp, cnt in TOC:
        if tp:
            sysq2[sy] = sysq2.get(sy, 0) + cnt
    toc = "".join((f'<a class="ts" href="#m{i}">{e(sy)} <small>{sysq2.get(sy, 0)}</small></a>' if tp is None else f'<a class="tt" href="#m{i}">{e(tp)} <small>{cnt}</small></a>') for i, (sy, tp, cnt) in enumerate(TOC))
    extra = """
html { font-size: 15px; } body { font-size: 13.5px !important; line-height: 1.45 !important; padding: 10px; background: #fff; }
.cols { column-count: 1 !important; }
@media (min-width: 900px) { .cols { column-count: 2 !important; } }
@media (min-width: 1400px) { .cols { column-count: 3 !important; } }
.guide { font-size: 14px !important; } .gcols { column-count: 1 !important; }
@media (min-width: 900px) { .gcols { column-count: 2 !important; } }
.q { cursor: pointer; padding: 6px 0 !important; }
.q:not(.open) .ck, .q:not(.open) .nt, .q:not(.open) .hbox, .q:not(.open) .na { display: none; }
.q:not(.open) .ok { font-weight: normal; text-decoration: none; }
.q:not(.open)::after { content: "اضغطي لعرض الجواب"; display: block; text-align: right; direction: rtl; font-size: .8em; color: #888; }
.bar { position: sticky; top: 0; z-index: 9; background: #000; color: #fff; padding: 8px; display: flex; gap: 8px; flex-wrap: wrap; direction: rtl; }
.bar button, .bar a { background: #fff; color: #000; border: 0; border-radius: 6px; padding: 6px 10px; font: inherit; font-weight: bold; text-decoration: none; }
#toc { direction: rtl; columns: 2 220px; border: 1.5px solid #000; border-radius: 8px; padding: 8px; margin: 8px 0; }
#toc a { display: block; color: #000; text-decoration: none; padding: 3px 4px; border-bottom: 1px solid #ddd; break-inside: avoid; }
#toc a.ts { background: #000; color: #fff; font-weight: bold; margin-top: 6px; } #toc small { opacity: .7; }
"""
    js = """<script>
document.addEventListener('click',function(ev){var q=ev.target.closest('.q');if(q&&!ev.target.closest('a'))q.classList.toggle('open');});
function all(o){document.querySelectorAll('.q').forEach(function(q){q.classList.toggle('open',o);});}
</script>"""
    hdoc = (f'<!doctype html><html lang="ar"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            f'<title>{e(TITLE)}</title><style>{fcss}{scss}{extra}</style></head><body>'
            f'<div class="bar"><a href="#toc">الفهرس</a><button onclick="all(true)">إظهار كل الأجوبة</button><button onclick="all(false)">إخفاء كل الأجوبة</button></div>'
            f'<div class="top"><span>{e(TITLE)}</span><span>{n} سؤال</span></div><div id="toc"><b>الفهرس</b>{toc}</div><div class="cols">{hb}</div>{js}</body></html>')
    open(os.environ["HTML_OUT"], "w", encoding="utf-8").write(hdoc)
    print("html ->", os.environ["HTML_OUT"])
    if os.environ.get("HTML_ONLY"):
        sys.exit(0)
src = os.path.join(tempfile.mkdtemp(), "d.html")
open(src, "w", encoding="utf-8").write(doc)
if os.environ.get("SAVE_SRC"):
    open(os.environ["SAVE_SRC"], "w", encoding="utf-8").write(doc)
subprocess.run([CHROME, "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf={OUT}", "file://" + src], check=True, capture_output=True)
print(n, "questions ->", OUT)

# ---- index page (فهرس) + bookmarks
import pypdf
r = pypdf.PdfReader(OUT)
where = {}
for pi, pg in enumerate(r.pages):
    for m in re.findall(r"@@M(\d+)@@", (pg.extract_text() or "").replace(" ", "")):
        where.setdefault(int(m), pi)
rows, sysq = "", {}
for i, (sy, tp, cnt) in enumerate(TOC):
    if tp:
        sysq[sy] = sysq.get(sy, 0) + cnt
for i, (sy, tp, cnt) in enumerate(TOC):
    pg = where.get(i, -1) + 2
    if tp is None:
        rows += f'<tr class="s"><td><a href="http://go.page/{pg}">{e(sy)}</a></td><td class="c">{sysq.get(sy, 0)}</td><td class="p"><a href="http://go.page/{pg}">{pg}</a></td></tr>'
    else:
        rows += f'<tr><td class="t"><a href="http://go.page/{pg}">{e(tp)}</a></td><td class="c">{cnt}</td><td class="p"><a href="http://go.page/{pg}">{pg}</a></td></tr>'
idx = (f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: {os.environ.get('PAGE', 'A4')}; margin: 8mm; }} body {{ font-family: "DejaVu Sans", Arial; font-size: 8.6pt; margin: 0; }}
h1 {{ font-size: 15pt; margin: 0 0 1mm; border-bottom: 2pt solid #000; display: flex; justify-content: space-between; }}
.w {{ column-count: 2; column-gap: 8mm; }} table {{ width: 100%; border-collapse: collapse; }}
td {{ padding: .55mm 1.5mm; border-bottom: .3pt solid #999; }} tr.s td {{ background: #000; color: #fff; font-weight: bold; font-size: 1.1em; }}
td.t {{ padding-left: 5mm; }} td.c {{ text-align: center; width: 12mm; color: #333; }} td.p {{ text-align: right; font-weight: bold; width: 14mm; }}
tr {{ break-inside: avoid; }} a {{ color: inherit; text-decoration: none; display: block; }}
</style></head><body><h1><span>{e(TITLE)}</span><span>فهرس</span></h1>
<div class="w"><table><tr><td><b>الموضوع</b></td><td class="c"><b>أسئلة</b></td><td class="p"><b>صفحة</b></td></tr>{rows}</table></div></body></html>''')
isrc = os.path.join(tempfile.mkdtemp(), "i.html")
open(isrc, "w", encoding="utf-8").write(idx)
ipdf = isrc[:-4] + "pdf"
subprocess.run([CHROME, "--no-sandbox", "--no-pdf-header-footer", f"--print-to-pdf={ipdf}", "file://" + isrc], check=True, capture_output=True)
ir = pypdf.PdfReader(ipdf)
assert len(ir.pages) == 1, "index longer than one page"
w = pypdf.PdfWriter()
w.append(ir)
w.append(r)
par = None
for i, (sy, tp, cnt) in enumerate(TOC):
    pg = where.get(i, 0) + 1
    if tp is None:
        par = w.add_outline_item(sy, pg)
    else:
        w.add_outline_item(f"{tp} ({cnt})", pg, parent=par)
# turn the index links (http://go.page/N) into jumps inside this PDF
from pypdf.generic import ArrayObject, DictionaryObject, NameObject, NumberObject
for annot in w.pages[0].get("/Annots", []) or []:
    a = annot.get_object()
    uri = a.get("/A", {}).get("/URI", "")
    m = re.search(r"go\.page/(\d+)", str(uri))
    if m:
        tgt = min(int(m.group(1)) - 1, len(w.pages) - 1)
        a[NameObject("/A")] = DictionaryObject({NameObject("/S"): NameObject("/GoTo"),
                                                NameObject("/D"): ArrayObject([w.pages[tgt].indirect_reference, NameObject("/Fit")])})
w.page_mode = "/UseOutlines"
w.write(OUT)
print("index added;", len(where), "of", len(TOC), "headers located")

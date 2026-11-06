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


GUIDES = load_basics(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "review", "guides_medicine.txt"))


def render_guide(name, lines):
    h, tbl = "", []

    def flush():
        nonlocal h, tbl
        if tbl:
            rows = [[c.strip() for c in r.strip().strip("|").split("|")] for r in tbl]
            h += "<table>" + "".join("<tr>" + "".join((f"<th>{gb(c)}</th>" if i == 0 else f"<td>{gb(c)}</td>") for c in r) + "</tr>" for i, r in enumerate(rows)) + "</table>"
            tbl = []
    gold, plan = "", ""
    for ln in lines:
        if ln.startswith("|"):
            tbl.append(ln)
            continue
        flush()
        if ln.startswith("@@ "):
            gold = gold.replace("</div>", f'<div class="kw">{gb(ln[3:])}</div></div>', 1) if gold else gold
        elif ln.startswith("@ "):
            gold = f'<div class="gx gold"><b class="t">القاعدة الذهبية</b>{gb(ln[2:])}</div>'
        elif ln.startswith("^ "):
            plan = f'<div class="gx gold plan"><b class="t">خطة أي سؤال</b>{gb(ln[2:])}</div>'
        elif ln.startswith("# "):
            n, _, t = ln[2:].partition(" ")
            h += f'<h3><i>{n}</i>{gb(t)}</h3>'
        elif ln.startswith("!"):
            kind, _, rest = ln[1:].partition(" ")
            lab, _, txt = rest.partition(":")
            h += f'<div class="gx {kind}"><b class="t">{gb(lab)}</b>{gb(txt.strip())}</div>'
        elif ln.startswith("- "):
            h += f'<div class="gl">• {gb(ln[2:])}</div>'
    flush()
    return (f'<div class="guide"><div class="ghead"><span>شرح {e(name)}</span><span class="gsub">افهمي القاعدة، بعدين حلي الأسئلة تحت</span></div>'
            f'{gold}<div class="gcols">{h}</div>{plan}</div>')


def gb(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"\[(ok|no):(.*?)\]", lambda m: f'<span class="tag {m.group(1)}">{m.group(2)}</span>', t)
    t = re.sub(r"\{(.*?)\}", lambda m: f'<span class="en">{m.group(1)}</span>', t)
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
        s, tp = classify(it["stem"], [o for _, o in it["opts"]], it["ans"])
        exq = ex.get(it["qid"], {})
        sents = re.split(r"(?<=[.;])\s+(?=[A-Z↑↻])", exq.get("author", ""))
        keep = []
        for x in sents:
            x = x.strip()
            if not x or SKIP.match(x) or META.match(x):
                continue
            if DIFF.search(x) or RULE.search(x):
                keep.append(x)
        note = " ".join(keep)[:230]
        if os.environ.get("NOANS_NOTES") and it["ans"].startswith("—"):  # no firm answer: keep Alhomrani's full words, they carry the conditional rule
            note = " ".join(x.strip() for x in sents if x.strip() and not SKIP.match(x.strip()))
        if os.environ.get("DROP_NOANS") and it["ans"].startswith("—"):
            continue
        items.append(dict(it, sys=s, topic=tp, note=note, tag=tag, key=exq.get("key", ""), rule=exq.get("rule", "")))

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
ordered = []
for g in sorted(groups, key=lambda k: order.get(k, 999)):
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
if os.environ.get("MAP"):
    json.dump({it["qid"]: [it["sys"], it["topic"]] for it in items}, open(os.environ["MAP"], "w"), ensure_ascii=False)

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


by_topic = defaultdict(list)
for it in items:
    by_topic[(it["sys"], it["topic"])].append(it)
body, cur_s, cur_t = "", None, None
for it in items:
    if it["sys"] != cur_s:
        TOC.append([it["sys"], None, 0])
        body += f'<div class="sh">{e(it["sys"])}<span class="mk">@@M{len(TOC) - 1}@@</span></div>'
        if GUIDES.get(it["sys"]):
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
    n = it["n"]
    TOC[-1][2] += 1
    ans = it["ans"].strip()
    o = ""
    hit = False
    for k, t in it["opts"]:
        ok = bool(re.match(rf"{k}[.)\-]", ans))
        hit = hit or ok
        o += f' <span class="{"ok" if ok else "op"}">{"✔" if ok else ""}{k}. {e(t)}</span>'
    if not hit:
        o += f' <span class="ok">✔ {e(ans)}</span>'
    rp = f'<span class="rp">مكرر {e(it["rep"])}</span> ' if it.get("rep") else ""
    tg = f'<span class="tg">{e(it["tag"])}</span>' if it["tag"] else ""
    if it.get("same") == "same":
        tg += '<span class="sm">= Sep</span>'
    elif it.get("same") == "diff":
        tg += '<span class="sm df">≈ Sep: جواب مختلف ⚠</span>'
    if os.environ.get("NOANS_NOTES") and ans.startswith("—"):
        nt = ('<div class="na">⚠ ما فيه جواب أكيد بالمصدر ← احفظي القاعدة:</div>'
              + (f'<div class="nt nah"><b>✍ قاعدة الحمراني:</b> {e(it["note"])}</div>' if it["note"] else "")
              + (f'<div class="nt nah"><b>🔑 القاعدة:</b> {e(it["key"])}</div>' if it.get("key") else "")
              + (f'<div class="nt">💡 {e(it["rule"])}</div>' if it.get("rule") else ""))
    else:
        nt = (f'<div class="nt">💡 {e(it["rule"])}</div>' if it.get("rule") else "") + (f'<div class="nt">✍ {e(it["note"])}</div>' if it["note"] else "")
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
.gx {{ padding: 1.4mm 2.4mm; border-radius: 1.6mm; margin: 1mm 0; border: 1px solid #000; border-right-width: 3.5px; break-inside: avoid; }}
.gx .t {{ display: block; margin-bottom: .2mm; }}
.gx.gold {{ background: #ececec; }}
.gx.mem {{ background: #fff; border-style: solid; }}
.gx.warn {{ background: #fff; border-style: dashed; border-right-style: solid; }}
.gx.warn .t::before {{ content: "⚠ "; }}
.gx.mem .t::before {{ content: "✎ "; }}
.gl {{ margin: .4mm 0; }}
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
.na {{ direction: rtl; text-align: right; font-weight: bold; margin-top: .3mm; }}
.nah {{ font-style: normal; border-left-width: 1.6pt; }}
.nt {{ font-size: .92em; font-style: italic; color: #111; border-left: .9pt solid #000; padding-left: .8mm; margin-top: .15mm; }}
"""
doc = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>'
       f'<div class="top"><span>{e(TITLE)}</span><span>{n} سؤال</span></div><div class="cols">{body}</div></body></html>')
src = os.path.join(tempfile.mkdtemp(), "d.html")
open(src, "w", encoding="utf-8").write(doc)
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
        rows += f'<tr class="s"><td>{e(sy)}</td><td class="c">{sysq.get(sy, 0)}</td><td class="p">{pg}</td></tr>'
    else:
        rows += f'<tr><td class="t">{e(tp)}</td><td class="c">{cnt}</td><td class="p">{pg}</td></tr>'
idx = (f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: {os.environ.get('PAGE', 'A4')}; margin: 8mm; }} body {{ font-family: "DejaVu Sans", Arial; font-size: 8.6pt; margin: 0; }}
h1 {{ font-size: 15pt; margin: 0 0 1mm; border-bottom: 2pt solid #000; display: flex; justify-content: space-between; }}
.w {{ column-count: 2; column-gap: 8mm; }} table {{ width: 100%; border-collapse: collapse; }}
td {{ padding: .55mm 1.5mm; border-bottom: .3pt solid #999; }} tr.s td {{ background: #000; color: #fff; font-weight: bold; font-size: 1.1em; }}
td.t {{ padding-left: 5mm; }} td.c {{ text-align: center; width: 12mm; color: #333; }} td.p {{ text-align: right; font-weight: bold; width: 14mm; }}
tr {{ break-inside: avoid; }}
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
w.page_mode = "/UseOutlines"
w.write(OUT)
print("index added;", len(where), "of", len(TOC), "headers located")

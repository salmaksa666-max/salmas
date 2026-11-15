"""Pictures (Joe + Almakrami apkg) and Ethics (Athar's Code apkg + SMLE Brain/Rashed PDF) -> site banks."""
import sqlite3, json, os, re, html, sys
import numpy as np
from collections import Counter
from PIL import Image
S = "/tmp/claude-0/-home-user-salmas/a5458d62-c397-540f-8afd-07d9eb2a5edf/scratchpad/"
tx = lambda h: html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", re.sub(r"<br\s*/?>", " ", h)))).strip()
def notes(d):
    fs = os.listdir(S + d); db = S + d + "/" + ("collection.anki21" if "collection.anki21" in fs else "collection.anki2")
    m = json.load(open(S + d + "/media")); rev = {v: k for k, v in m.items()}
    return [r[0].split("\x1f") for r in sqlite3.connect(db).execute("select flds from notes")], rev
def parse_q(f):
    stem = tx(re.split(r'<div class="question-options"', f[3])[0])
    opts = [[m.group(1), tx(m.group(2))] for m in re.finditer(r'data-letter="([A-F])">\s*[A-F][.)]?\s*(.*?)</div>', f[3], re.S)]
    m = re.match(r"([A-F])[.)]", f[7].strip())
    return stem, [o for o in opts if o[1]], (m.group(1) if m else "")
def why(f):
    t = tx(f[10]); t = re.sub(r"^(Answer\s*:?\s*[A-F]\b[,.]?\s*)", "", t)
    t = re.sub(r"^Why the answer is right\s*", "", t)
    return t[:400]
# ---------------- pictures
os.makedirs("site/pimg", exist_ok=True)
pics = []
F, rev = notes("ap_joem")
for f in F:
    if f[19] not in ("sourced", "confirmed", "best"): continue
    stem, opts, a = parse_q(f)
    imgs = re.findall(r'src="([^"]+)"', f[11])
    if not a or len(opts) < 2 or not imgs: continue
    out_imgs = []
    for i in imgs:
        if i not in rev: continue
        name = os.path.splitext(i)[0] + ".webp"
        dst = "site/pimg/" + name
        if not os.path.exists(dst):
            im = Image.open(S + "ap_joem/" + rev[i]).convert("RGB"); im.thumbnail((900, 900)); im.save(dst, "WEBP", quality=62)
        out_imgs.append(name)
    sec = re.sub(r"^\d+-\s*", "", f[1])
    k = re.search(r'Key concept</span><div class="study-value">(.*?)</div>', f[10], re.S)
    r = re.search(r'Why the answer is right</span><div class="study-value">(.*?)</div>', f[10], re.S)
    pics.append(dict(i=f[0], b="Pictures", s=sec, t="كل الأسئلة", h="", q=stem, o=opts, a=a, k=tx(k.group(1))[:220] if k else "",
                     r=(tx(r.group(1)) if r else why(f))[:400], n="", f="", im=[], pi=out_imgs, kw=[]))
print("pictures:", len(pics), Counter(p["s"] for p in pics), "image KB", sum(os.path.getsize("site/pimg/" + x) for x in os.listdir("site/pimg")) // 1024)
# ---------------- ethics: Athar
eth = []
F, _ = notes("ap_athar")
for f in F:
    stem, opts, a = parse_q(f)
    if not a or len(opts) < 2: continue
    eth.append(dict(i=f[0], b="Ethics", s=re.sub(r"^\d+-\s*", "", f[1]), t="كل الأسئلة", h="", q=stem, o=opts, a=a, k="", r=why(f), n="Athar's Code", f="", im=[], kw=[]))
nA = len(eth)
# ---------------- ethics: SMLE Brain (Rashed) PDF
txt = open(S + "rashed.txt", encoding="utf-8").read()
txt = re.sub(r"^.*https://t\.me/smlebrain.*$", "", txt, flags=re.M)
sec = "Ethics"; cur = None; blocks = []
for line in txt.splitlines():
    ms = re.match(r"^\s*Section\s*\d+\)?\s*(.+?)\s*$", line)
    if ms and "Page" not in line: sec = re.sub(r"[–-].*", "", ms.group(1)).replace(":", "").strip() or sec
    mq = re.match(r"^\s{0,6}(\d{1,3})\)\s+(.*)$", line)
    if mq:
        cur = dict(n=int(mq.group(1)), sec=sec, lines=[mq.group(2)]); blocks.append(cur)
    elif cur is not None:
        cur["lines"].append(line)
for b in blocks:
    body = "\n".join(b["lines"])
    am = re.search(r"Answer\s*:\s*([A-F])\b[,.]?\s*(.*)", body, re.S)
    if not am: continue
    head = body[:am.start()]
    parts = re.split(r"(?m)^\s*([A-F])\)\s+", head)
    if len(parts) < 5: continue
    stem = " ".join(parts[0].split())
    opts = [[parts[i], " ".join(parts[i + 1].split())] for i in range(1, len(parts) - 1, 2)]
    expl = " ".join(am.group(2).split())
    expl = re.split(r"\s(?=\d{1,3}\)\s)", expl)[0][:400]
    if am.group(1) not in dict(opts): continue
    eth.append(dict(i=f"RSH-{b['n']:03d}", b="Ethics", s=b["sec"], t="كل الأسئلة", h="", q=stem, o=opts, a=am.group(1), k="", r=expl, n="SMLE Brain (Rashed)", f="", im=[], kw=[]))
print("ethics: athar", nA, "rashed", len(eth) - nA)
# drop Rashed questions that repeat an Athar one
T = re.compile(r"[a-z][a-z0-9\-]{2,}")
tk = lambda q: T.findall((q["q"] + " " + " ".join(t for _, t in q["o"])).lower())
docs = [tk(q) for q in eth]; df = Counter(w for d in docs for w in set(d)); N = len(docs)
voc = {w: i for i, w in enumerate(df)}; M = np.zeros((N, len(voc)), dtype=np.float32)
for r_, d in enumerate(docs):
    for w, c in Counter(d).items(): M[r_, voc[w]] = (1 + np.log(c)) * np.log(N / df[w])
M /= np.maximum(np.linalg.norm(M, axis=1, keepdims=True), 1e-9)
Sm = M[nA:] @ M[:nA].T
keep = eth[:nA]
for r_, q in enumerate(eth[nA:]):
    if Sm[r_].max() >= 0.8: continue
    top = np.argsort(-Sm[r_])[:5]
    q["s"] = Counter(eth[j]["s"] for j in top).most_common(1)[0][0]  # same topic names as Athar's
    keep.append(q)
print("ethics after removing repeats:", len(keep), Counter(q["s"] for q in keep).most_common(15))
json.dump(pics, open("site/pics.json", "w", encoding="utf-8"), ensure_ascii=False)
json.dump(keep, open("site/ethics.json", "w", encoding="utf-8"), ensure_ascii=False)

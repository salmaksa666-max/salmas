"""Parse the MKJ/Alhomrani November apkg and compare its answers with Yasir + our banks."""
import sqlite3, re, json, sys, html
import numpy as np
from collections import Counter
DB, OUT = sys.argv[1], sys.argv[2]
S = "/tmp/claude-0/-home-user-salmas/a5458d62-c397-540f-8afd-07d9eb2a5edf/scratchpad/"
c = sqlite3.connect(DB)
tx = lambda h: html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", h))).strip()
items = []
for (fl,) in c.execute("select flds from notes"):
    f = fl.split("\x1f")
    stem = tx(re.split(r'<div class="question-options"', f[3])[0])
    opts = [[m.group(1), tx(m.group(2))] for m in re.finditer(r'data-letter="([A-F])">\s*[A-F][.)]?\s*(.*?)</div>', f[3], re.S)]
    m = re.match(r"([A-F])[.)]", f[7].strip())
    sec = f[1].split("::")[-1]
    sec = re.sub(r"^\d+-\s*", "", sec)
    items.append(dict(i=f[0], b="Alhomrani Nov", s=sec, t="كل أسئلة النظام", h="", q=stem, o=opts, a=m.group(1) if m else "",
                      k="", r="", n=tx(f[10])[:260], f="", st=f[19], day=f[2],
                      im=re.findall(r'src="([^"]+)"', f[12]) if re.search(r"\b(picture|pic|image|photo|ECG|EKG|x-?ray|CXR|smear)\b", stem, re.I) else []))
print(len(items), Counter(i["st"] for i in items), "no letter:", sum(1 for i in items if not i["a"]), "no opts:", sum(1 for i in items if not i["o"]))
json.dump(items, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
# ---- compare with our banks
site = json.load(open("site/data.json", encoding="utf-8"))
TOK = re.compile(r"[a-z][a-z0-9\-]{2,}")
def toks(q): return TOK.findall((q["q"] + " " + " ".join(t for _, t in q["o"])).lower())
allq = items + site
docs = [toks(q) for q in allq]
from collections import defaultdict
df = Counter(w for d in docs for w in set(d)); N = len(docs)
keep = [w for w, c in df.most_common() if 2 <= c <= 400][:9000]
voc = {w: i for i, w in enumerate(keep)}
M = np.zeros((N, len(voc)), dtype=np.float32)
for r, d in enumerate(docs):
    for w, k in Counter(d).items():
        if w in voc: M[r, voc[w]] = (1 + np.log(k)) * np.log(N / df[w])
M /= np.maximum(np.linalg.norm(M, axis=1, keepdims=True), 1e-9)
n = len(items)
Sm = M[:n] @ M[n:].T
res = []
for r in range(n):
    j = int(Sm[r].argmax()); s = float(Sm[r, j])
    if s >= 0.75:
        o = site[j]
        # compare answer TEXT, since letters can differ
        ta = dict(items[r]["o"]).get(items[r]["a"], "").lower().strip()
        tb = dict(o["o"]).get(o["a"], "").lower().strip()
        res.append((round(float(s), 2), items[r]["i"], o["i"], o["b"], ta, tb, ta == tb or ta in tb or tb in ta))
print("matched to our banks:", len(res), "same answer:", sum(1 for x in res if x[-1]), "different:", sum(1 for x in res if not x[-1]))
json.dump(res, open(S + "mkj_cmp.json", "w", encoding="utf-8"), ensure_ascii=False)
for x in [x for x in res if not x[-1]][:25]: print(x[:6])

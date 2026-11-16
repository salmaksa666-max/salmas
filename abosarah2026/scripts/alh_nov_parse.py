"""Parse Alhomrani's November PDFs (one recall per page) exactly as written: stem, options, his answer line, his notes."""
import re, json, sys, os
SD = sys.argv[1]
FILES = [("N15f", "1-5 November"), ("N68", "6-8 November"), ("N9", "9 November"), ("P1", "10-14 November (Part 1)"), ("P2", "10-14 November (Part 2)")]
HDR = re.compile(r"https?://\S+|^\s*\d{1,2}\s*[–-]\s*\d{1,2}\s+November.*$|^\s*\d{1,2}\s+November\s*$|^\s*\d{1,2}[–-]\d{1,2} November.*$", re.M)
norm = lambda t: re.sub(r"[^a-z0-9]+", " ", t.lower()).strip()
out, stat = [], {}
for key, label in FILES:
    pages = open(os.path.join(SD, key + ".raw.txt"), encoding="utf-8", errors="ignore").read().split("\f")
    for _pi in range(len(pages)):
        _o = os.path.join(SD, "ocr", f"{key}_{_pi + 1}.txt")
        if os.path.exists(_o): pages[_pi] = open(_o, encoding="utf-8", errors="ignore").read()
    ok = bad = 0
    for pi, pg in enumerate(pages, 1):
        L = [HDR.sub("", l).strip() for l in pg.splitlines()]
        L = [l for l in L if l]
        st = next((i for i, l in enumerate(L) if re.match(r"^\d{1,4}\.\s*\S", l)), None)
        if st is None: continue
        oi = [i for i, l in enumerate(L) if i > st and re.match(r"^[A-F][\.\)]\s*\S", l)]
        run = []
        for i in oi:
            if not run: 
                if L[i][0] == "A": run = [i]
                continue
            if ord(L[i][0]) == ord(L[run[-1]][0]) + 1 and i - run[-1] <= 3: run.append(i)
            elif len(run) >= 2: break
        if len(run) < 2: bad += 1; out.append(dict(src=key, file=label, page=pi, n=int(re.match(r"^(\d+)", L[st]).group(1)), stem=" ".join(L[st:st+6]), opts=[], ans=None, notes="", fail="no options")); continue
        # options may wrap to a 2nd line: join continuation lines (not starting with a letter-option) up to next option
        opts = []
        for k, i in enumerate(run):
            j_end = run[k + 1] if k + 1 < len(run) else i + 1
            txt = " ".join(L[i:j_end]); opts.append(re.sub(r"^[A-F][\.\)]\s*", "", txt).strip())
        stem = re.sub(r"^\d{1,4}\.\s*", "", " ".join(L[st:run[0]]))
        rest = L[run[-1] + 1:]
        ans = None; ai = None
        for r_i, l in enumerate(rest[:12]):
            m = re.match(r"^([A-F])[\.\)]\s*(.+)", l); nl = norm(re.sub(r"^[A-F][\.\)]\s*", "", l))
            hits = [(len(norm(o)), j) for j, o in enumerate(opts) if norm(o) and (nl == norm(o) or nl.startswith(norm(o) + " ") or (len(norm(o)) > 12 and norm(o).startswith(nl) and len(nl) > 12))]
            if m and m.group(1) in "ABCDEF"[:len(opts)]:
                j = "ABCDEF".index(m.group(1))
                if norm(opts[j])[:10] and (norm(m.group(2))[:10] == norm(opts[j])[:10]): hits = [(999, j)]
            if hits: ans = max(hits)[1]; ai = r_i; break
        if ans is None:
            mm = re.findall(r"(?:Final\s+)?Answer\s*(?:is|:)?\s*[\"“”']?\s*([A-F])\b", " ".join(rest))
            if mm and mm[-1] in "ABCDEF"[:len(opts)]: ans = "ABCDEF".index(mm[-1]); ai = None
        notes = " · ".join(rest[(ai + 1) if ai is not None else 0:])[:900]
        if ans is None: bad += 1
        else: ok += 1
        out.append(dict(src=key, file=label, page=pi, n=int(re.match(r"^(\d+)", L[st]).group(1)), stem=stem, opts=opts, ans=ans, notes=notes, fail=None if ans is not None else "no answer"))
    stat[key] = (ok, bad)
json.dump(out, open(os.path.join(SD, "alh_nov_parsed.json"), "w"), ensure_ascii=False, indent=0)
print(stat, len(out))

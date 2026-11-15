"""GB (14 NOV).pdf -> GameBoy November bank + comparison with our GameBoy answers."""
import re, json, sys
t = open(sys.argv[1], encoding="utf-8").read()
t = re.sub(r"\n[ \t]*\d{1,2}[ \t]*(?=\n)", "\n", t.replace("\f", "\n"))
blocks = re.split(r"\n(?=[ \t]*\d{4}[ \t]*\n)", "\n" + t)
gb = {i["qid"]: i for i in json.load(open(sys.argv[2], encoding="utf-8"))}
out = []
for b in blocks:
    m = re.match(r"\s*(\d{4})\s*\n(.*)", b, re.S)
    if not m: continue
    num, body = m.group(1), m.group(2)
    main = body.split("Note:")[0]
    am = re.search(r"Answer:\s*([A-F])", main)
    opts = re.findall(r"^\s*([A-F])\.\s*(.+)$", main, re.M)
    stem = " ".join(main[:main.find(opts[0][0] + ". " + opts[0][1])].split()) if opts else ""
    if not am or not opts: continue
    note = " ".join(body.split("Note:")[1].split())[:300] if "Note:" in body else ""
    qid = f"GB-{num}"
    old = gb.get(qid, {})
    oa = (old.get("ans") or "")[:1]
    out.append(dict(i="GB14-" + num, gid=qid, q=stem, o=[[k, v.strip()] for k, v in opts], a=am.group(1), old=oa, n=note))
    if "Note:" in body:  # modified version of the same GameBoy question
        nb = body.split("Note:", 1)[1]
        vm = re.search(r"variant:?\s*(.*)", nb, re.S)
        if vm:
            vb = vm.group(1)
            vo = re.findall(r"^\s*([A-F])\.\s*(.+)$", vb, re.M)
            va = re.search(r"Answer:\s*([A-F])", vb)
            if vo and va:
                vs = " ".join(vb[:vb.find(vo[0][0] + ". " + vo[0][1])].split())
                out.append(dict(i="GB14-" + num + "v", gid=qid, q=vs, o=[[k, v.strip()] for k, v in vo], a=va.group(1), old="",
                                n="نسخة معدّلة من سؤال GameBoy " + num + " وجوابها يختلف عن الأصلي."))
print(len(out), "changed vs our GameBoy:", [(x["gid"], x["old"], x["a"]) for x in out if x["old"] and x["old"] != x["a"]])
json.dump(out, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False)

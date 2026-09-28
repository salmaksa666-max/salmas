import json, glob, html, re
L = "ABCDE"
def t(s):
    s = html.escape(s, quote=False)
    return re.sub(r"\{\{(.*?)\}\}", lambda m: f"<bdi>{m.group(1)}</bdi>", s)
def table(head, rows):
    h = "<table class=rx>"
    if head: h += "<tr>" + "".join(f"<th>{t(x)}</th>" for x in head) + "</tr>"
    return h + "".join("<tr>" + "".join(f"<td>{t(c)}</td>" for c in r) + "</tr>" for r in rows) + "</table>"
def ul(xs): return "<ul>" + "".join(f"<li>{t(x)}</li>" for x in xs) + "</ul>"
def render(e, q, file_expl):
    a = q["ans"]; ans_txt = html.unescape(re.sub("<[^>]+>", "", q["opts"][a]))
    h = ["<div class=rich dir=rtl>"]
    h.append(f"<h4>١. الجواب</h4><div><b>الخيار {'أبجده'[a]}: <bdi>{html.escape(ans_txt)}</bdi></b></div>")
    if file_expl and not file_expl.startswith("No written"):
        h.append(f"<div class=fx dir=ltr><b>From the file:</b> {file_expl}</div>")
    h.append("<h4>٢. وش الفكرة؟</h4>" + ul(e["idea"]))
    h.append("<h4>٣. كيف عرفنا؟</h4>" + table(["المعلومة في السؤال", "معناها"], e["clues"]))
    if e.get("check"):
        c = e["check"]; h.append(f"<div class=sub3>{t(c.get('title',''))}</div>" + table(["الشرط", "موجود؟", "تعليق"], c["rows"]))
    h.append("<h4>٤. ليش الجواب صح؟</h4>" + ul(e["why"]))
    if e.get("trap"): h.append("<h4>انتبهي للفخ</h4>" + ul([e["trap"]]))
    h.append("<h4>٥. متى يتغير الجواب؟</h4>" + ul(e["change"]))
    h.append(f"<h4>٦. القاعدة</h4><div class=rule><b>{t(e['rule'])}</b></div>")
    if e.get("compare"):
        c = e["compare"]; h.append("<h4>٧. مقارنة سريعة</h4>" + table(c.get("head"), c["rows"]))
    if e.get("note"): h.append(f"<h4>ملاحظة عن الإرشادات</h4><div class=gnote>{t(e['note'])}</div>")
    h.append("<div class=src2>الجواب من ملف الحمراني، والشرح الإضافي معلومات طبية عامة.</div></div>")
    for k, why in e["wrong"].items():
        h.append(f"<div data-why={int(k)}><b>ليش غلط؟</b> {t(why)}</div>")
    return "".join(h)
def load_all():
    R = {}
    for f in sorted(glob.glob("/home/claude/rich/out/*.json")): R.update(json.load(open(f)))
    return R

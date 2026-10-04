def clues_table(clues):
    if not clues:
        return ""
    rows = "".join(
        f"<tr><td dir=\"ltr\"><bdi>{term}</bdi></td><td>{meaning}</td></tr>"
        for term, meaning in clues
    )
    return (
        '<table class="clues"><tr><th>من السؤال</th><th>يعني وش</th></tr>'
        f"{rows}</table>"
    )


def bullets(items):
    if not items:
        return ""
    if isinstance(items, str):
        items = [items]
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def comparison_table(cmp):
    if not cmp:
        return ""
    headers = "".join(f"<th>{h}</th>" for h in cmp["headers"])
    rows = ""
    for row in cmp["rows"]:
        cells = "".join(f"<td>{c}</td>" for c in row)
        rows += f"<tr>{cells}</tr>"
    return f'<table class="cmp"><tr>{headers}</tr>{rows}</table>'


def render_explain(q, e, source_name):
    parts = []

    if e.get("self_judged"):
        parts.append(
            '<div class="star-badge">⭐ ما فيه جواب مذكور بالمصدر الأصلي لهذا السؤال '
            "— هذا اجتهادي الطبي الشخصي، مو من المصدر</div>"
        )

    ans_letter = e["correct_letter"]
    ans_text = q[f"Opt{ans_letter}"]
    parts.append(
        f'<p><b>الجواب:</b> <bdi dir="ltr">{ans_letter}. {ans_text}</bdi></p>'
    )

    parts.append(f'<p><b>وش الفكرة:</b> {e["idea"]}</p>')

    ct = clues_table(e.get("clues"))
    if ct:
        parts.append(f'<p><b>كيف عرفنا:</b></p>{ct}')

    parts.append(f'<p><b>ليش الجواب صح:</b></p>{bullets(e["why_correct"])}')

    parts.append(f'<p><b>متى يتغير الجواب:</b></p>{bullets(e["when_changes"])}')

    parts.append(f'<p><b>القاعدة:</b> {e["rule"]}</p>')

    cmp_html = comparison_table(e.get("comparison"))
    if cmp_html:
        parts.append(cmp_html)

    if e.get("guideline_note"):
        parts.append(f'<p class="note"><b>ملاحظة:</b> {e["guideline_note"]}</p>')

    note = "بدون جواب مذكور بالمصدر" if e.get("self_judged") else "جواب مذكور بالمصدر"
    parts.append(
        f'<p class="src">المصدر: {source_name}، السؤال رقم {q["num"]} ({note})</p>'
    )

    return "".join(parts)

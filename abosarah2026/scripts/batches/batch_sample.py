# -*- coding: utf-8 -*-
# Worked reference example for AS-0001. Study this before writing any real batch.

EXPLANATIONS = {
"AS-0001": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "هذا سيناريو <bdi>near-miss wrong-site surgery</bdi>، والسؤال يبي الإجراء الوقائي الصح حسب <bdi>Universal Protocol</bdi> و<bdi>WHO Surgical Safety Checklist</bdi>، مو بس اللي كشف الخطأ هالمرة بالصدفة.",
    "clues": [
        ("wrong leg", "خطأ وشيك بتحديد مكان الجراحة (<bdi>wrong-site surgery</bdi>)"),
        ("how to prevent", "السؤال يبي إجراء وقائي نظامي، مو بس وصف اللي صار بالسيناريو"),
    ],
    "why_correct": [
        "<bdi>proper site marking</bdi> قبل الجراحة هي خطوة الوقاية الأساسية حسب <bdi>Universal Protocol</bdi>: الجراح نفسه يحدد مكان الجراحة بعلامة واضحة قبل ما يدخل المريض غرفة العمليات، والأفضل والمريض واعي يأكد المكان.",
        "بعد التحديد تجي خطوة <bdi>time-out</bdi> قبل الشق مباشرة مع الفريق كامل، كتأكيد أخير.",
        "مراجعة الملف (الخيار B) فعلاً كشفت الخطأ بهالموقف، بس هي خطوة تحقق متأخرة وغير موثوقة لوحدها، مو الإجراء المعياري للوقاية من الأساس.",
    ],
    "when_changes": [
        "لو السؤال يبي الخطوة الفورية اللي تمنع الشق لحظة اكتشاف الخطأ (مو الوقاية الأصلية)، يصير الجواب وقف الإجراء فورًا والتحقق الجماعي (<bdi>time-out</bdi>).",
        "لو السؤال يركز على مين يتحمل مسؤولية الإبلاغ عن الشك، الجواب يصير إن أي عضو بالفريق (حتى الممرضة) لازم يتكلم فورًا بدون تردد.",
    ],
    "rule": "أي سؤال «كيف نمنع» خطأ بموقع الجراحة، الجواب المعياري دايمًا <bdi>site marking</bdi> قبل الجراحة ضمن <bdi>Universal Protocol</bdi>، مو خطوة الكشف اللي حصلت بالصدفة بالسيناريو.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
}

WHY_WRONG = {
"AS-0001": {
    "A": "تجاهل الشك وعدم التبليغ هو بالضبط السلوك اللي يسبب مثل هالخطأ، مو حل له.",
    "B": "مراجعة الملف خطوة تحقق مفيدة بس متأخرة وغير كافية لوحدها كإجراء وقائي معياري.",
},
}

HIGHLIGHT_TERMS = {
"AS-0001": ["wrong leg", "how to prevent"],
}

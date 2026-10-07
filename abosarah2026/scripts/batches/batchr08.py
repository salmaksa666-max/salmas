# -*- coding: utf-8 -*-
# Batch r08 — AS-0803 .. AS-1299 (Medicine). Built from the compiler's source
# explanations per AGENT_INSTRUCTIONS.md.

EXPLANATIONS = {

"AS-0803": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "سؤال يبي <bdi>screening test</bdi> لسبب ثانوي للـ<bdi>hypertension</bdi> عند <bdi>young patient</bdi> مع <bdi>hypokalemia</bdi> و<bdi>resistant HTN</bdi>.",
    "clues": [
        ("25 years old", "<bdi>young patient</bdi> بعمر صغير مع <bdi>hypertension</bdi> يدفعنا نفكر بسبب ثانوي، مو <bdi>essential HTN</bdi>"),
        ("hypokalemia", "<bdi>low potassium</bdi> مع <bdi>HTN</bdi> يوجه لـ<bdi>primary hyperaldosteronism</bdi> (<bdi>Conn syndrome</bdi>)"),
        ("blood pressure still uncontrolled", "<bdi>resistant hypertension</bdi> على دوائين يعني لازم نسبب الثانوي"),
    ],
    "why_correct": [
        "<bdi>young patient</bdi> مع <bdi>hypertension</bdi> <bdi>uncontrolled</bdi> على دوائين و<bdi>low potassium</bdi> لازم نسوي له <bdi>screening</bdi> لـ<bdi>primary hyperaldosteronism</bdi>، وهو أشهر سبب <bdi>endocrine</bdi> للـ<bdi>secondary hypertension</bdi>.",
        "التحليل المناسب هو <bdi>aldosterone to renin ratio</bdi>، وهذا هو المقصود بالخيار حتى لو صياغته \"<bdi>renin angiotensin ratio</bdi>\".",
        "وجود <bdi>family history</bdi> من <bdi>stroke</bdi> يدعم إمكانية <bdi>familial hyperaldosteronism</bdi> (<bdi>glucocorticoid remediable</bdi>) اللي مرتبط بـ<bdi>early hemorrhagic stroke</bdi>.",
    ],
    "when_changes": [
        "لو كان عند <bdi>patient</bdi> <bdi>paroxysmal headache</bdi> و<bdi>sweating</bdi> و<bdi>palpitations</bdi> بدل <bdi>hypokalemia</bdi>، الجواب يصير <bdi>metanephrines</bdi> (<bdi>pheochromocytoma</bdi>).",
        "لو كان عنده <bdi>AKI</bdi> بعد <bdi>ACE inhibitor</bdi>، نفكر بـ<bdi>renal artery stenosis</bdi> مو <bdi>Conn syndrome</bdi>.",
    ],
    "rule": "<bdi>hypertension</bdi> + <bdi>hypokalemia</bdi> (أو <bdi>young</bdi> أو <bdi>resistant</bdi>) = <bdi>screen</bdi> بـ<bdi>aldosterone:renin ratio</bdi>؛ <bdi>paroxysmal</bdi> symptoms توجه لـ<bdi>metanephrines</bdi>.",
    "comparison": {
        "headers": ["السبب", "الـ<bdi>clue</bdi>", "تحليل <bdi>screening</bdi>"],
        "rows": [
            ["<bdi>Conn syndrome</bdi>", "<bdi>hypokalemia</bdi>، <bdi>metabolic alkalosis</bdi>", "<bdi>aldosterone:renin ratio</bdi>"],
            ["<bdi>Pheochromocytoma</bdi>", "<bdi>paroxysms</bdi>, <bdi>headache</bdi>, <bdi>sweating</bdi>", "<bdi>plasma/urine metanephrines</bdi>"],
            ["<bdi>Renal artery stenosis</bdi>", "<bdi>AKI</bdi> بعد <bdi>ACEI</bdi>", "<bdi>renal duplex</bdi>"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},

"AS-0805": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "سؤال عن علاج <bdi>symptomatic MS</bdi> لما يكون <bdi>disease</bdi> نفسه <bdi>well controlled</bdi> بدون <bdi>relapse</bdi>، لازم نربط <bdi>symptom</bdi> بالعلاج الصح.",
    "clues": [
        ("Multiple Sclerosis", "<bdi>known case</bdi> و<bdi>well controlled</bdi>، يعني مافي <bdi>relapse</bdi> نشط"),
        ("generalized body pain", "<bdi>diffuse pain</bdi> مع عدم وجود <bdi>new neurological symptoms</bdi> يوجه لـ<bdi>spasticity</bdi>-related <bdi>pain</bdi>"),
    ],
    "why_correct": [
        "<bdi>MS</bdi> عندها <bdi>well controlled</bdi> على <bdi>Teriflunomide</bdi> وماعندها <bdi>new neurological symptoms</bdi>، فمو <bdi>relapse</bdi>.",
        "<bdi>diffuse body pain</bdi> بـ<bdi>MS</bdi> أغلبه <bdi>musculoskeletal pain</bdi> من <bdi>spasticity</bdi> و<bdi>stiffness</bdi>.",
        "العلاج هو <bdi>antispasticity agent</bdi> مثل <bdi>Tizanidine</bdi> (أو <bdi>baclofen</bdi>) مع <bdi>physiotherapy</bdi>.",
    ],
    "when_changes": [
        "لو كان الألم <bdi>paroxysmal</bdi> على شكل <bdi>electric shock</bdi> بالوجه، الجواب يصير <bdi>Carbamazepine</bdi> لـ<bdi>trigeminal neuralgia</bdi>.",
        "لو عندها <bdi>urgency</bdi> و<bdi>urge incontinence</bdi>، الجواب يصير <bdi>Oxybutynin</bdi> لعلاج <bdi>neurogenic bladder</bdi>.",
        "لو عندها <bdi>fever</bdi> و<bdi>urinary symptoms</bdi> توجه لـ<bdi>infection</bdi>، الجواب يصير <bdi>antibiotics</bdi>.",
    ],
    "rule": "علاج <bdi>MS</bdi> الـ<bdi>symptomatic</bdi> لازم يتطابق مع نوع <bdi>symptom</bdi>: <bdi>spasticity</bdi> يعني <bdi>baclofen/tizanidine</bdi>، <bdi>trigeminal neuralgia</bdi> يعني <bdi>carbamazepine</bdi>، <bdi>urge incontinence</bdi> يعني <bdi>oxybutynin</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-0811": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال عن علاج <bdi>IBS</bdi> بعد استبعاد <bdi>organic disease</bdi>؛ الخط الأول هو نصيحة غذائية وتجنب <bdi>trigger foods</bdi>.",
    "clues": [
        ("Symptoms increased with stress and after food", "نمط <bdi>functional</bdi> يتأثر بـ<bdi>stress</bdi> والأكل، يميل لـ<bdi>IBS</bdi>"),
        ("Normal blood lab, normal colonoscopy", "استبعاد <bdi>organic cause</bdi>، يدعم <bdi>diagnosis</bdi> الـ<bdi>IBS</bdi>"),
    ],
    "why_correct": [
        "الألم مع <bdi>intermittent diarrhea</bdi> يسوء مع <bdi>stress</bdi> وبعد الأكل، مع <bdi>normal labs</bdi> و<bdi>normal colonoscopy</bdi> ومافي <bdi>pathogen</bdi> = <bdi>irritable bowel syndrome</bdi> (<bdi>diarrhea predominant</bdi>).",
        "الخط الأول هو <bdi>reassurance</bdi> ونصيحة غذائية: وجبات منتظمة وتقليل <bdi>trigger foods</bdi> مثل <bdi>fatty</bdi> و<bdi>spicy food</bdi> والـ<bdi>caffeine</bdi> والكحول.",
        "هذا هو المقصود بالخيار D: تقليل <bdi>spicy food</bdi> و<bdi>fat</bdi> لتقليل <bdi>irritation</bdi>.",
    ],
    "when_changes": [
        "لو فشلت النصيحة الأولية، الخطوة الجاية تصير <bdi>low FODMAP diet</bdi>.",
        "لو كان النوع <bdi>constipation predominant</bdi>، الجواب يصير زيادة <bdi>soluble fiber</bdi> (<bdi>psyllium</bdi>) مو <bdi>insoluble fiber</bdi>.",
        "لو عنده <bdi>red flags</bdi> مثل <bdi>weight loss</bdi> أو <bdi>bleeding</bdi> أو <bdi>age</bdi> فوق 50 جديد، نحتاج <bdi>colonoscopy</bdi> أول.",
    ],
    "rule": "<bdi>IBS</bdi> يتشخّص بعد استبعاد <bdi>organic disease</bdi>، والعلاج يتبع نوع <bdi>symptom</bdi>: الأساس بكل الأنواع تقليل <bdi>fatty/spicy food</bdi> والـ<bdi>caffeine</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-0813": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "سؤال يربط <bdi>multiple myeloma</bdi> بسبب <bdi>renal failure</bdi> الأشهر وهو <bdi>cast nephropathy</bdi> من <bdi>light chains</bdi>.",
    "clues": [
        ("Persistent Back Pain", "<bdi>back pain</bdi> مستمر غير مستجيب لـ<bdi>NSAIDs</bdi> يوجه لـ<bdi>lytic bone lesion</bdi>"),
        ("Creatinine: Elevated", "<bdi>renal impairment</bdi> ضمن معايير <bdi>myeloma</bdi> CRAB"),
        ("Bone Marrow Biopsy: 20% Plasma Cells", "تأكيد <bdi>multiple myeloma</bdi> (≥10% <bdi>clonal plasma cells</bdi>)"),
    ],
    "why_correct": [
        "<bdi>patient</bdi> عمره 60 مع <bdi>persistent back pain</bdi> (<bdi>lytic bone disease</bdi>) و<bdi>20% clonal plasma cells</bdi> = <bdi>multiple myeloma</bdi>.",
        "أشهر سبب <bdi>renal failure</bdi> بالـ<bdi>myeloma</bdi> هو <bdi>cast nephropathy</bdi> (<bdi>myeloma kidney</bdi>): <bdi>monoclonal free light chains</bdi> تترسب بالـ<bdi>distal tubules</bdi> وتسبب ضرر.",
        "فتراكم <bdi>monoclonal light chains</bdi> هو اللي يفسر ارتفاع <bdi>creatinine</bdi>.",
    ],
    "when_changes": [
        "لو كان فيه <bdi>hypotension</bdi> أو <bdi>sepsis</bdi> أو <bdi>contrast exposure</bdi>، الجواب يصير <bdi>ATN</bdi>.",
        "لو كان فيه <bdi>colicky loin pain</bdi> و<bdi>hematuria</bdi> مع <bdi>hypercalcemia</bdi>، نفكر بـ<bdi>kidney stones</bdi>.",
    ],
    "rule": "<bdi>back pain</bdi> غير مستجيب لـ<bdi>NSAIDs</bdi> عند <bdi>older patient</bdi> مع ارتفاع <bdi>creatinine</bdi> = فكّر <bdi>myeloma</bdi>، وتجنب <bdi>NSAIDs</bdi> و<bdi>contrast</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-0825": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "سؤال وقاية من <bdi>ventilator associated pneumonia</bdi> (<bdi>VAP</bdi>)، والإجراء الأساسي هو <bdi>positioning</bdi> مو <bdi>antibiotics</bdi> أو إجراءات زيادة.",
    "clues": [
        ("mechanical ventilation", "<bdi>intubated patient</bdi> معرض لـ<bdi>aspiration</bdi>"),
        ("fever and purulent discharge from trachea", "علامات <bdi>VAP</bdi> فعلية، والسؤال يبي الوقاية المستقبلية"),
    ],
    "why_correct": [
        "<bdi>fever</bdi> و<bdi>purulent tracheal secretions</bdi> بعد أيام من <bdi>mechanical ventilation</bdi> = <bdi>ventilator associated pneumonia (VAP)</bdi>، سببها الأساسي <bdi>microaspiration</bdi> حول الـ<bdi>cuff</bdi>.",
        "الإجراء الوقائي الأساسي هو <bdi>elevating head of bed 30 to 45 degrees</bdi>، يقلل <bdi>aspiration risk</bdi>.",
    ],
    "when_changes": [
        "لو السؤال يسأل عن علاج <bdi>VAP</bdi> المثبت، الجواب يصير <bdi>antibiotics</bdi> حسب <bdi>cultures</bdi>، مو <bdi>prophylactic</bdi>.",
        "لو السؤال عن تقليل مدة <bdi>ventilation</bdi>، الجواب يصير <bdi>daily sedation hold</bdi> و<bdi>spontaneous breathing trial</bdi>.",
    ],
    "rule": "<bdi>VAP bundle</bdi>: <bdi>head of bed</bdi> مرفوع، <bdi>sedation hold</bdi> يومي، <bdi>oral care</bdi>، وتجنب <bdi>routine suctioning</bdi> و<bdi>prophylactic antibiotics</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-0830": {
    "correct_letter": "B",
    "self_judged": True,
    "idea": "سؤال يفرّق بين سببين لـ<bdi>HTN</bdi> مع <bdi>hypokalemia</bdi>: <bdi>hyperaldosteronism</bdi> أو <bdi>Cushing syndrome</bdi>، حسب وجود ملامح <bdi>Cushingoid</bdi>.",
    "clues": [
        ("Persistent HTN", "<bdi>resistant hypertension</bdi> يوجه لسبب ثانوي"),
        ("potassium 3,2", "<bdi>hypokalemia</bdi> واضح، يناسب <bdi>mineralocorticoid excess</bdi>"),
    ],
    "why_correct": [
        "<bdi>mustached</bdi> بلا <bdi>diabetes</bdi> ولا <bdi>obesity</bdi> (حسب <bdi>compiler note</bdi>) يعني مافي ملامح <bdi>Cushingoid</bdi> واضحة، فنرجّح <bdi>Conn syndrome</bdi> على <bdi>Cushing syndrome</bdi>.",
        "<bdi>family history</bdi> من <bdi>stroke</bdi> يدعم أكثر <bdi>familial hyperaldosteronism</bdi>.",
        "التحليل التشخيصي المناسب هنا هو <bdi>aldosterone renin ratio</bdi>، مو <bdi>24h urine cortisol</bdi> اللي يحتاج ملامح <bdi>Cushing</bdi> أول.",
        "هذا سؤال <bdi>self-judged</bdi> لأن المصدر نفسه ماحدد جواب؛ الاختيار هنا حسب أقوى <bdi>clue</bdi> متوفر.",
    ],
    "when_changes": [
        "لو ذكر السؤال <bdi>obesity</bdi>، <bdi>striae</bdi>، أو <bdi>diabetes</bdi>، الجواب يصير <bdi>24h urine cortisol</bdi> لتشخيص <bdi>Cushing syndrome</bdi>.",
        "<bdi>proximal weakness</bdi> ممكن تكون بس من <bdi>hypokalemia</bdi> نفسها، مو لازم تعني <bdi>Cushing</bdi>.",
    ],
    "rule": "<bdi>HTN</bdi> + <bdi>hypokalemia</bdi> بلا ملامح <bdi>Cushingoid</bdi> = <bdi>aldosterone:renin ratio</bdi>؛ وجود ملامح <bdi>Cushingoid</bdi> يحول الجواب لـ<bdi>cortisol</bdi> testing.",
    "comparison": None,
    "labs": [["Potassium", "3.2 mmol/L", "3.5-5.1 mmol/L"]],
    "guideline_note": None,
},

"AS-0831": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال <bdi>delirium</bdi> عند <bdi>elderly</bdi> مع عدة اضطرابات، والمصدر هنا يربط التحسن بتصحيح <bdi>calcium</bdi> المنخفض.",
    "clues": [
        ("elderly", "<bdi>elderly patient</bdi> معرّضة لـ<bdi>delirium</bdi> بأسباب متعددة"),
        ("urinary tract infection symptoms", "وجود <bdi>infection</bdi> ممكن يكون سبب، لكن هذا <bdi>distractor</bdi> بهذا النسخة"),
        ("calcium 1.9", "<bdi>hypocalcemia</bdi> واضح، هو المفتاح بهذا النسخة من السؤال"),
        ("sodium 134", "<bdi>mild hyponatremia</bdi> غير كافي لتفسير <bdi>confusion</bdi>"),
    ],
    "why_correct": [
        "المصدر بهذي النسخة قرأ <bdi>calcium</bdi> 1.9 (أقل من الطبيعي 2.2-2.6 mmol/L) كـ<bdi>symptomatic hypocalcemia</bdi> سبب <bdi>confusion</bdi>.",
        "علاج <bdi>acute symptomatic hypocalcemia</bdi> هو <bdi>IV calcium gluconate</bdi>، وهو اللي يرجع الحالة الذهنية.",
        "نسخ أخرى من هذا السؤال اختارت <bdi>antibiotics</bdi>، فهذا تضارب بالمصدر نفسه حسب <bdi>compiler note</bdi>.",
    ],
    "when_changes": [
        "لو كان <bdi>sodium</bdi> منخفض جدًا (أقل من 125) أو نازل بسرعة، الجواب يصير تصحيح <bdi>hyponatremia</bdi>.",
        "لو كان <bdi>UTI</bdi> هو السبب الأوضح بلا اضطراب <bdi>electrolyte</bdi> شديد، الجواب يصير <bdi>antibiotics</bdi>.",
    ],
    "rule": "<bdi>confusion</bdi> عند <bdi>elderly</bdi>: دوّر على السبب الأوضح إحصائيًا، لكن لازم نصحح <bdi>calcium</bdi> حسب <bdi>albumin</bdi> قبل اعتباره السبب.",
    "comparison": None,
    "labs": [["Calcium", "1.9 mmol/L", "2.2-2.6 mmol/L"], ["Sodium", "134 mmol/L", "135-145 mmol/L"]],
    "guideline_note": "هذا السؤال نسخة متضاربة بالمصدر نفسه (نسخ أخرى اختارت <bdi>antibiotics</bdi>)؛ احتفظنا بجواب المصدر المؤكد لهذه النسخة (<bdi>calcium gluconate</bdi>).",
},

"AS-0831B": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "<bdi>delirium</bdi> عند <bdi>elderly</bdi> بسبب <bdi>UTI</bdi> واضح، والمختبرات الأخرى خفيفة وغير كافية لتفسير <bdi>CNS symptoms</bdi>.",
    "clues": [
        ("elderly", "عمر متقدم يزيد خطر <bdi>delirium</bdi> من <bdi>infection</bdi>"),
        ("UTI symptoms and CNS symptoms", "علاقة سببية بين <bdi>infection</bdi> و<bdi>confusion</bdi>"),
        ("calcium 1.97 mmol/L", "<bdi>borderline hypocalcemia</bdi>، لازم تصحيح بـ<bdi>albumin</bdi>"),
        ("sodium 132 mmol/L", "<bdi>mild hyponatremia</bdi> نادرًا تسبب <bdi>confusion</bdi>"),
        ("mild cortical atrophy", "تغيّر <bdi>chronic</bdi> بالـ<bdi>MRI</bdi>، لا يفسر تغيّر حاد"),
    ],
    "why_correct": [
        "<bdi>elderly patient</bdi> مع <bdi>UTI symptoms</bdi> ثم <bdi>CNS symptoms</bdi> = <bdi>delirium</bdi> سببه <bdi>infection</bdi> إلى ما يثبت العكس.",
        "السؤال يسأل عن ما يرجّع الحالة الذهنية (<bdi>reverse CNS symptoms</bdi>)، يعني علاج السبب: <bdi>proper antibiotics</bdi> للـ<bdi>UTI</bdi>.",
        "باقي الاضطرابات (<bdi>Na</bdi> 132، <bdi>Ca</bdi> 1.97) خفيفة أو <bdi>chronic</bdi> (<bdi>cortical atrophy</bdi>) ولا تفسر <bdi>acute confusion</bdi>.",
    ],
    "when_changes": [
        "لو كان <bdi>Na</bdi> منخفض جدًا أو نازل بسرعة مع <bdi>seizures</bdi>، الجواب يصير تصحيح <bdi>hyponatremia</bdi>.",
        "لو كان فيه <bdi>tetany</bdi> أو <bdi>prolonged QT</bdi>، الجواب يصير <bdi>IV calcium gluconate</bdi>.",
    ],
    "rule": "<bdi>distractor labs</bdi> الخفيفة موجودة لتشتيت الانتباه؛ السبب الحاد الواضح (<bdi>infection</bdi>) هو اللي يرجّع <bdi>delirium</bdi>.",
    "comparison": None,
    "labs": [["Calcium", "1.97 mmol/L", "2.2-2.6 mmol/L"], ["Sodium", "132 mmol/L", "135-145 mmol/L"], ["Random glucose", "11 mmol/L", "4-7.8 mmol/L"]],
    "guideline_note": None,
},

"AS-0831C": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "نفس فكرة <bdi>UTI</bdi>-triggered <bdi>delirium</bdi> عند <bdi>elderly</bdi>، مع <bdi>hypertension</bdi> تستبعد <bdi>septic shock</bdi>.",
    "clues": [
        ("elderly", "عمر متقدم عامل خطر لـ<bdi>delirium</bdi>"),
        ("fever, dysuria, and confusion", "تسلسل واضح من <bdi>infection</bdi> إلى <bdi>confusion</bdi>"),
        ("Na+ = 132", "<bdi>mild hyponatremia</bdi> غير كافي لتفسير الحالة"),
        ("Ca2+ = 1.6", "<bdi>hypocalcemia</bdi> أوضح لكن لازم تصحيح بـ<bdi>albumin</bdi>"),
        ("leukocytes in urine", "تأكيد <bdi>UTI</bdi>"),
    ],
    "why_correct": [
        "<bdi>fever</bdi>، <bdi>dysuria</bdi>، و<bdi>confusion</bdi> مع <bdi>leukocytes in urine</bdi> = <bdi>UTI</bdi>-triggered <bdi>delirium</bdi>.",
        "السؤال يسأل عن علاج يرجّع <bdi>CNS symptoms</bdi>، فنعالج السبب: <bdi>proper antibiotics</bdi>.",
        "<bdi>hypertension</bdi> يستبعد <bdi>septic shock</bdi> كسبب للـ<bdi>confusion</bdi>، و<bdi>Na</bdi> 132 بسيط جدًا.",
    ],
    "when_changes": [
        "لو كان <bdi>Na</bdi> شديد الانخفاض مع <bdi>seizures</bdi>، الجواب يصير تصحيح <bdi>sodium</bdi>.",
        "لو كان فيه <bdi>tetany</bdi> أو <bdi>laryngospasm</bdi>، الجواب يصير <bdi>IV calcium gluconate</bdi> حتى بدون تصحيح <bdi>albumin</bdi> أول.",
        "لو كان <bdi>patient</bdi> <bdi>hypotensive</bdi> أو <bdi>dehydrated</bdi>، الجواب يصير <bdi>IV fluids</bdi> كجزء من الإنعاش.",
    ],
    "rule": "تحقق من <bdi>albumin</bdi> قبل ما تلوم <bdi>calcium</bdi> المنخفض؛ عند وجود <bdi>fever + dysuria + confusion</bdi>، الهدف هو علاج <bdi>infection</bdi>.",
    "comparison": None,
    "labs": [["Sodium", "132 mmol/L", "135-145 mmol/L"], ["Calcium", "1.6 mmol/L", "2.2-2.6 mmol/L"]],
    "guideline_note": None,
},

"AS-0831D": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نسخة ثالثة من نفس السيناريو: <bdi>elderly</bdi> مع <bdi>UTI</bdi> و<bdi>delirium</bdi>، وعلامات <bdi>hemodynamic stability</bdi> تستبعد الأسباب الأخرى.",
    "clues": [
        ("71 year old", "<bdi>elderly patient</bdi> عامل خطر لـ<bdi>delirium</bdi>"),
        ("S&S of UTI", "<bdi>infection source</bdi> واضح"),
        ("confused and unable to recall", "<bdi>acute confusion</bdi> بعد دخول المستشفى"),
        ("positive nitrites and leukocyte esterase", "تأكيد مخبري لـ<bdi>UTI</bdi>"),
    ],
    "why_correct": [
        "<bdi>71 year old</bdi> دخلت بـ<bdi>UTI</bdi> ثم صار عندها <bdi>confusion</bdi> = <bdi>delirium</bdi> من <bdi>infection</bdi>.",
        "<bdi>fever</bdi> مع <bdi>positive nitrites and leukocyte esterase</bdi> يأكد <bdi>UTI</bdi>، و<bdi>BP</bdi> 150 يأكد إنها مو <bdi>shocked</bdi>.",
        "لتصحيح <bdi>neurological symptoms</bdi> نعالج السبب: <bdi>give antibiotics</bdi>.",
    ],
    "when_changes": [
        "لو كانت <bdi>hypotensive</bdi> أو <bdi>dehydrated</bdi>، الجواب يصير <bdi>IV fluids</bdi> أول.",
        "لو كان <bdi>hyponatremia</bdi> شديد أو مع <bdi>seizures</bdi>، الجواب يصير تصحيح <bdi>sodium</bdi>.",
    ],
    "rule": "اضطرابات <bdi>labs</bdi> الخفيفة (<bdi>hyperglycemia</bdi>، <bdi>mild hyponatremia</bdi>، <bdi>borderline calcium</bdi>) جزء من المرض الحاد؛ علاج <bdi>infection</bdi> هو اللي يرجّع <bdi>delirium</bdi>.",
    "comparison": None,
    "labs": [["Sodium", "132 mmol/L", "134-145 mmol/L"], ["Calcium", "1.9 mmol/L", "2.2-2.6 mmol/L"]],
    "guideline_note": None,
},

"AS-0835": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "<bdi>pneumonia</bdi> مع <bdi>hemoptysis</bdi> فاشلة على <bdi>antibiotics</bdi> تياخذنا لمنظمة مسببة <bdi>destructive</bdi> و<bdi>cavitating</bdi>.",
    "clues": [
        ("pneumonia symptoms and hemoptysis", "<bdi>hemoptysis</bdi> مع <bdi>pneumonia</bdi> يوجه لـ<bdi>necrotising organism</bdi>"),
        ("Received 2 course of antibiotics but no improvement", "فشل <bdi>standard CAP treatment</bdi> يستبعد الأسباب المعتادة"),
    ],
    "why_correct": [
        "<bdi>pneumonia</bdi> مع <bdi>hemoptysis</bdi> لا تتحسن بعد <bdi>2 courses of antibiotics</bdi> توجه لعضو <bdi>destructive</bdi> و<bdi>cavitating</bdi> قد لا تغطيه <bdi>standard CAP antibiotics</bdi>.",
        "<bdi>Staphylococcus aureus</bdi> (شامل <bdi>MRSA</bdi>) يناسب هذا: يسبب <bdi>necrotising pneumonia</bdi> مع <bdi>hemoptysis</bdi>، غالبًا بعد <bdi>influenza</bdi>.",
        "المصدر وضع هذا الجواب كـ<bdi>uncertain</bdi>، فنتعلم الفكرة أكثر من الحرف.",
    ],
    "when_changes": [
        "لو كان فيه <bdi>travel</bdi> أو تعرض لمياه/فنادق مع <bdi>hyponatremia</bdi> و<bdi>confusion</bdi>، الجواب يصير <bdi>Legionella</bdi>.",
        "لو كان <bdi>patient</bdi> صغير بعمره مع <bdi>dry cough</bdi> خفيف، الجواب يصير <bdi>Mycoplasma</bdi>.",
        "لو كان <bdi>patient</bdi> <bdi>smoker</bdi> مع <bdi>infiltrate</bdi> غير متحسن، لازم نستبعد <bdi>malignancy</bdi>.",
    ],
    "rule": "<bdi>non-resolving pneumonia</bdi>: فكّر بعضو <bdi>resistant</bdi> أو <bdi>destructive</bdi>؛ \"<bdi>no travel</bdi>\" تستبعد <bdi>Legionella</bdi>، وفشل العلاج مع <bdi>hemoptysis</bdi> يوجه لـ<bdi>Staph aureus</bdi>.",
    "comparison": {
        "headers": ["المنظمة", "الـ<bdi>clue</bdi> المفتاح"],
        "rows": [
            ["<bdi>Strep pneumoniae</bdi>", "أشهر سبب <bdi>CAP</bdi>، يستجيب للعلاج المعتاد"],
            ["<bdi>Legionella</bdi>", "<bdi>travel</bdi>، <bdi>hyponatremia</bdi>، <bdi>GI upset</bdi>"],
            ["<bdi>Mycoplasma</bdi>", "<bdi>young</bdi>، <bdi>dry cough</bdi>، مرض خفيف"],
            ["<bdi>Staph aureus</bdi>", "بعد <bdi>influenza</bdi>، <bdi>cavitation</bdi>، <bdi>hemoptysis</bdi>، فشل العلاج"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},

"AS-0844": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "<bdi>parapneumonic effusion</bdi> كبيرة بما يكفي للتقييم يحتاج <bdi>diagnostic thoracentesis</bdi> قبل القرار بالـ<bdi>chest tube</bdi>.",
    "clues": [
        ("25 mm pleural effusion on decubitus film", "<bdi>effusion</bdi> أكبر من 10 mm يحتاج <bdi>sampling</bdi>"),
    ],
    "why_correct": [
        "<bdi>right lower lobe pneumonia</bdi> مع <bdi>effusion</bdi> 25 mm على <bdi>decubitus film</bdi> هو <bdi>parapneumonic effusion</bdi> كبير بما يكفي (أكثر من 10 mm).",
        "الخطوة الجاية هي <bdi>diagnostic thoracentesis</bdi>، لأن <bdi>pleural fluid pH</bdi> و<bdi>glucose</bdi> و<bdi>LDH</bdi> و<bdi>Gram stain</bdi> يحددون لو نحتاج <bdi>chest tube</bdi>.",
        "<bdi>antibiotics</bdi> تعطى كذلك لكن السؤال يختبر خطوة الـ<bdi>effusion</bdi>.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>effusion</bdi> أقل من 10 mm، الجواب يصير علاج <bdi>pneumonia</bdi> بالـ<bdi>antibiotics</bdi> فقط بدون تاب.",
        "لو كان فيه <bdi>weight loss</bdi> و<bdi>night sweats</bdi> مزمنة، نفكر بـ<bdi>TB pleurisy</bdi> ونأكد بـ<bdi>ADA</bdi> أو <bdi>pleural biopsy</bdi>.",
    ],
    "rule": "<bdi>parapneumonic effusion</bdi> أكبر من 10 mm = <bdi>tap it</bdi> أول؛ <bdi>pH</bdi> أقل من 7.2 أو <bdi>pus</bdi> أو <bdi>Gram stain</bdi> موجب = <bdi>chest tube</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-0845": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "<bdi>symptomatic bradycardia</bdi> مع <bdi>normal cardiac enzymes</bdi> تستبعد <bdi>ACS</bdi>، والعلاج الأول هو <bdi>atropine</bdi>.",
    "clues": [
        ("shortness of breath but no chest pain", "عرض من <bdi>rhythm problem</bdi> مو <bdi>ischemia</bdi>"),
        ("ECG show Bradycardia or heart block", "تأكيد <bdi>symptomatic bradycardia</bdi>"),
    ],
    "why_correct": [
        "<bdi>ECG</bdi> يبين <bdi>bradycardia</bdi> أو <bdi>heart block</bdi> مع <bdi>shortness of breath</bdi> = <bdi>symptomatic bradycardia</bdi>.",
        "<bdi>normal troponin</bdi> و<bdi>CK-MB</bdi> وعدم وجود <bdi>chest pain</bdi> يستبعدون <bdi>acute MI</bdi>.",
        "العلاج الأول للـ<bdi>symptomatic bradycardia</bdi> هو <bdi>IV atropine</bdi>، ولو فشل نروح لـ<bdi>pacing</bdi>.",
    ],
    "when_changes": [
        "لو فشل <bdi>atropine</bdi>، الجواب يصير <bdi>transcutaneous/transvenous pacing</bdi> أو <bdi>dopamine/epinephrine</bdi>.",
        "لو كان السؤال يبي علاج <bdi>unstable tachyarrhythmia</bdi>، الجواب يصير <bdi>cardioversion</bdi>.",
    ],
    "rule": "<bdi>symptomatic bradycardia</bdi>: <bdi>atropine</bdi> أول، ثم <bdi>pacing</bdi> لو فشل؛ وبعدين نعالج السبب.",
    "comparison": None,
    "labs": [["Troponin", "0.2", "دون الـ cutoff (<bdi>normal</bdi>)"], ["CK-MB", "3.5", "ضمن الطبيعي"]],
    "guideline_note": None,
},

"AS-0846": {
    "correct_letter": "B",
    "self_judged": True,
    "idea": "سؤال <bdi>serology</bdi> لـ<bdi>hepatitis B</bdi>؛ لازم نفرّق بين <bdi>acute</bdi> و<bdi>chronic</bdi> و<bdi>resolved infection</bdi> حسب نوع <bdi>antibody</bdi>.",
    "clues": [
        ("+ve HBsAg", "<bdi>current infection</bdi>، يستبعد <bdi>resolved infection</bdi> و<bdi>vaccination</bdi>"),
        ("Anti HBc IgG", "<bdi>past exposure</bdi>، و<bdi>IgG</bdi> (مو <bdi>IgM</bdi>) يعني مو <bdi>acute</bdi>"),
    ],
    "why_correct": [
        "<bdi>HBsAg</bdi> موجب يعني <bdi>current infection</bdi> (<bdi>acute</bdi> أو <bdi>chronic</bdi>)، يستبعد <bdi>resolved infection</bdi> و<bdi>vaccination</bdi> من الأساس.",
        "<bdi>Anti HBc IgG</bdi> (مو <bdi>IgM</bdi>) موجب مع <bdi>anti HBs</bdi> سالب يعني العدوى مستمرة من مدة، وهذا نمط <bdi>chronic hepatitis B</bdi>.",
        "هذا سؤال <bdi>self-judged</bdi> لأن المصدر ماحدد جواب؛ الاختيار هنا حسب نمط <bdi>serology</bdi> الكلاسيكي.",
    ],
    "when_changes": [
        "لو كان <bdi>Anti HBc</bdi> من نوع <bdi>IgM</bdi> بدل <bdi>IgG</bdi>، الجواب يصير <bdi>acute hepatitis B</bdi>.",
        "لو كان <bdi>HBsAg</bdi> سالب مع <bdi>anti HBs</bdi> و<bdi>anti HBc IgG</bdi> موجبين، الجواب يصير <bdi>resolved infection</bdi>.",
    ],
    "rule": "<bdi>HBsAg</bdi> موجب + <bdi>IgG anti-HBc</bdi> موجب (بدون <bdi>IgM</bdi>) = <bdi>chronic hepatitis B</bdi>؛ <bdi>IgM anti-HBc</bdi> هو اللي يفرّق <bdi>acute</bdi>.",
    "comparison": {
        "headers": ["الحالة", "<bdi>HBsAg</bdi>", "<bdi>Anti-HBc</bdi>", "<bdi>Anti-HBs</bdi>"],
        "rows": [
            ["<bdi>Acute</bdi>", "+", "<bdi>IgM</bdi> +", "−"],
            ["<bdi>Chronic</bdi>", "+ (>6 شهور)", "<bdi>IgG</bdi> +", "−"],
            ["<bdi>Resolved</bdi>", "−", "<bdi>IgG</bdi> +", "+"],
            ["<bdi>Vaccinated</bdi>", "−", "−", "+"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},

"AS-0846B": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "نمط <bdi>serology</bdi> لـ<bdi>hepatitis B</bdi>: <bdi>anti-HBs</bdi> لوحده بدون <bdi>anti-HBc</bdi> ما يصير إلا من <bdi>vaccination</bdi>.",
    "clues": [
        ("Negative", "<bdi>HBsAg</bdi> و<bdi>HBeAg</bdi> و<bdi>anti-HBc IgG</bdi> كلهم سالبين"),
        ("Anti-HBsAg Positive", "<bdi>immunity</bdi> موجودة"),
        ("Anti-HBc IgG Negative", "ما فيه دليل تعرّض حقيقي للفيروس"),
    ],
    "why_correct": [
        "<bdi>HBsAg</bdi> سالب يعني مافي <bdi>current infection</bdi>، و<bdi>anti-HBs</bdi> موجب يعني <bdi>immune</bdi>.",
        "<bdi>Anti-HBc IgG</bdi> سالب يبين إنه ما تعرّض للفيروس الحقيقي من الأساس.",
        "<bdi>immunity</bdi> بدون <bdi>anti-HBc</bdi> ما يجي إلا من <bdi>vaccination</bdi>، لأن اللقاح يحتوي <bdi>surface antigen</bdi> فقط.",
    ],
    "when_changes": [
        "لو كان <bdi>anti-HBc IgG</bdi> موجب مع <bdi>anti-HBs</bdi> موجب، الجواب يصير <bdi>previous (resolved) infection</bdi>.",
        "لو كان <bdi>HBsAg</bdi> موجب مع <bdi>IgM anti-HBc</bdi>، الجواب يصير <bdi>acute infection</bdi>.",
    ],
    "rule": "اللقاح يسبب <bdi>anti-HBs</bdi> فقط، أبدًا ما يسبب <bdi>anti-HBc</bdi>؛ هذا هو الفرق بين <bdi>vaccinated</bdi> و<bdi>recovered</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-0848": {
    "correct_letter": "A",
    "self_judged": True,
    "idea": "<bdi>weakness</bdi> مع <bdi>ECG</bdi> يبين <bdi>Afib</bdi> = <bdi>stroke</bdi> سببه <bdi>cardioembolic</bdi> من <bdi>left atrial thrombus</bdi>.",
    "clues": [
        ("weakness", "علامة <bdi>neurological deficit</bdi> من <bdi>stroke</bdi>"),
        ("image show Afib", "الصورة تحدد <bdi>rhythm</bdi> مباشرة بدون غموض"),
    ],
    "why_correct": [
        "الصورة توضح <bdi>ECG</bdi> فيه <bdi>Afib</bdi> (<bdi>irregularly irregular</bdi>، بدون <bdi>P waves</bdi>)، وهذا هو سبب الـ<bdi>stroke</bdi> المباشر بهذا السؤال.",
        "<bdi>Atrial fibrillation</bdi> تسبب تكوّن <bdi>thrombus</bdi> بالـ<bdi>left atrium</bdi>، وينفصل جزء ويسبب <bdi>cardioembolic stroke</bdi>.",
        "هذا سؤال <bdi>self-judged</bdi> لأن المصدر ماحدد جواب رسمي، لكن الصورة بالسؤال نفسه تحدد <bdi>Afib</bdi> بوضوح.",
    ],
    "when_changes": [
        "لو كانت الصورة تبين <bdi>sawtooth waves</bdi> منتظمة، الجواب يصير <bdi>Atrial flutter</bdi>.",
        "لو كان عنده <bdi>stroke</bdi> سابق، درجة <bdi>CHA2DS2-VASc</bdi> ترتفع وتأكد الحاجة لـ<bdi>anticoagulation</bdi>.",
    ],
    "rule": "<bdi>Afib</bdi> على الـ<bdi>ECG</bdi> مع <bdi>stroke</bdi> = سببه <bdi>cardioembolic</bdi>؛ الوقاية بـ<bdi>anticoagulation</bdi> مو <bdi>antiplatelets</bdi>.",
    "comparison": {
        "headers": ["النمط", "صفة الـ<bdi>ECG</bdi>"],
        "rows": [
            ["<bdi>Atrial fibrillation</bdi>", "<bdi>irregularly irregular</bdi>، بدون <bdi>P waves</bdi>"],
            ["<bdi>Atrial flutter</bdi>", "<bdi>sawtooth waves</bdi> منتظمة، معدل حوالي 150"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},

"AS-0850": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>symptomatic bradycardia</bdi> عند <bdi>patient</bdi> مستقر، والعلاج الأول من الخيارات هو <bdi>atropine</bdi>.",
    "clues": [
        ("SOB and fatigue", "أعراض من <bdi>poor perfusion</bdi> بسبب المعدل البطيء"),
        ("stable", "<bdi>stable patient</bdi> يعني مافي علامات <bdi>instability</bdi> شديدة"),
        ("bradycardia", "تأكيد <bdi>ECG</bdi> للمعدل البطيء"),
    ],
    "why_correct": [
        "الـ<bdi>ECG</bdi> يبين <bdi>bradycardia</bdi>، والمريض عنده <bdi>SOB and fatigue</bdi>، يعني المعدل البطيء هو سبب الأعراض.",
        "من بين الخيارات، <bdi>atropine</bdi> هو العلاج الوحيد اللي يرفع المعدل البطيء، وهو خط أول بخوارزمية <bdi>bradycardia</bdi>.",
        "لو فشل <bdi>atropine</bdi>، الخطوة الجاية <bdi>pacing</bdi> أو <bdi>dopamine/epinephrine</bdi>.",
    ],
    "when_changes": [
        "لو كان المريض <bdi>unstable</bdi> (<bdi>hypotension</bdi>، <bdi>altered mental status</bdi>)، يبقى <bdi>atropine</bdi> هو الخط الأول برضو، ثم <bdi>pacing</bdi> بسرعة لو فشل.",
        "لو كان السؤال عن <bdi>tachyarrhythmia</bdi> غير مستقرة، الجواب يصير <bdi>cardioversion</bdi>.",
    ],
    "rule": "<bdi>symptomatic bradycardia</bdi>: <bdi>atropine</bdi> أول دايمًا؛ <bdi>cardioversion</bdi> و<bdi>antiplatelets</bdi> لا علاقة لهم بمعدل بطيء.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-0853": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "<bdi>stable AFib</bdi> بلا عوامل خطر لـ<bdi>stroke</bdi>: الأساس <bdi>rate control</bdi>، والسؤال يستثني <bdi>rhythm control</bdi>.",
    "clues": [
        ("Incidentally Found To Have Atrial Fibrillation", "<bdi>asymptomatic</bdi>، اكتشاف عرضي، <bdi>medically free</bdi>"),
        ("HR: 110 bpm", "معدل سريع يحتاج <bdi>rate control</bdi>"),
        ("BP: 110/70 mmHg", "<bdi>hemodynamically stable</bdi>، يستبعد <bdi>cardioversion</bdi> الطارئ"),
    ],
    "why_correct": [
        "<bdi>patient</bdi> عنده <bdi>stable AFib</bdi> (<bdi>BP</bdi> 110/70) مع معدل سريع (<bdi>HR</bdi> 110)، والسؤال يستثني <bdi>rhythm control</bdi> صراحة، فالهدف هو <bdi>rate control</bdi>.",
        "<bdi>beta blocker</bdi> مثل <bdi>bisoprolol</bdi> ينزل المعدل تحت 100.",
        "كونه \"<bdi>medically free</bdi>\" يعني درجة <bdi>CHA2DS2-VA</bdi> منخفضة، فمافي حاجة ماسّة لـ<bdi>anticoagulation</bdi>؛ المصدر يربط <bdi>aspirin</bdi> مع الـ<bdi>beta blocker</bdi>.",
        "هذا الخيار يحقق <bdi>rate control</bdi> بلا الحاجة لـ<bdi>DOAC</bdi> حسب نقاط <bdi>CHA2DS2-VA</bdi>.",
    ],
    "when_changes": [
        "لو كانت درجة <bdi>CHA2DS2-VA</bdi> 2 أو أكثر (<bdi>hypertension</bdi>، <bdi>diabetes</bdi>، <bdi>prior stroke</bdi>)، الجواب يصير <bdi>DOAC + beta blocker</bdi>.",
        "لو كان <bdi>patient</bdi> <bdi>unstable</bdi> (<bdi>hypotension</bdi>، <bdi>shock</bdi>)، الجواب يصير <bdi>electrical cardioversion</bdi>.",
    ],
    "rule": "<bdi>stable AFib</bdi> = <bdi>rate control</bdi> أول، و<bdi>anticoagulation</bdi> تتحدد بدرجة <bdi>CHA2DS2-VA</bdi> مو بنوع <bdi>rhythm</bdi>.",
    "comparison": None,
    "labs": [["Heart rate", "110 bpm", "60-100 bpm"], ["Blood pressure", "110/70 mmHg", "90-120 / 60-80 mmHg"]],
    "guideline_note": None,
},

"AS-0854": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "سؤال يحفظ <bdi>LDL target</bdi> \"<bdi>optimal</bdi>\" بدون <bdi>ASCVD</bdi>، مقارنة بالهدف الأدق مع وجود مرض وعائي مثبت.",
    "clues": [
        ("LDL-cholesterol", "المقصود هو <bdi>target value</bdi> لا <bdi>current value</bdi>"),
        ("Optimal range", "يبي الهدف العام، مو هدف <bdi>established ASCVD</bdi>"),
    ],
    "why_correct": [
        "السؤال يبي الهدف العام \"<bdi>optimal</bdi>\" للـ<bdi>LDL</bdi>، والمصدر يحدده بـ<bdi>&lt;2.5 mmol/L</bdi> (يقابل تقريبًا أقل من 100 mg/dL) لشخص بلا <bdi>established atherosclerotic disease</bdi>.",
        "لو كان فيه <bdi>ASCVD</bdi> مثبت، الهدف ينزل لحوالي <bdi>2.0 mmol/L</bdi> أو أقل.",
    ],
    "when_changes": [
        "لو ذكر السؤال <bdi>MI</bdi> أو <bdi>stroke</bdi> أو <bdi>PAD</bdi>، الجواب يتحول للهدف الأدق (حوالي 2.0).",
        "لو كان <bdi>LDL</bdi> ≥190 mg/dL أو عنده <bdi>diabetes</bdi> بعمر 40-75، الجواب يصير البدء بـ<bdi>statin</bdi> عالي الكثافة بغض النظر عن الهدف.",
    ],
    "rule": "هدف <bdi>LDL</bdi> يعتمد على درجة الخطر: بلا <bdi>ASCVD</bdi> = &lt;2.5 mmol/L؛ مع <bdi>ASCVD</bdi> مثبت = هدف أدق وأقل.",
    "comparison": {
        "headers": ["الحالة", "هدف <bdi>LDL</bdi>"],
        "rows": [
            ["بلا <bdi>ASCVD</bdi>", "&lt;2.5 mmol/L"],
            ["مع <bdi>ASCVD</bdi> مثبت", "≈2.0 mmol/L أو أقل"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},

"AS-0868": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>adolescent</bdi> مع نتيجتين غير طبيعيتين يثبتان <bdi>diabetes</bdi>، فالخطوة هي البدء بالعلاج مو مزيد من التأكيد.",
    "clues": [
        ("family hx of diabetes", "عامل خطر لـ<bdi>type 2 DM</bdi> بعمر صغير"),
        ("thirst and polyuria", "<bdi>classic symptoms</bdi> لـ<bdi>hyperglycemia</bdi>"),
        ("Fasting glucose 8 to 10 mmol", "فوق عتبة <bdi>diabetes</bdi> (≥7.0 mmol/L)"),
        ("Hb a1c above 7 , 7.8 %", "نتيجة ثانية مؤكدة (≥6.5%)"),
    ],
    "why_correct": [
        "<bdi>diabetes</bdi> مثبت بهذا <bdi>13 to 15 year old</bdi>: <bdi>classic symptoms</bdi> مع نتيجتين غير طبيعيتين (<bdi>fasting glucose</bdi> فوق 7، <bdi>HbA1c</bdi> 7.8%).",
        "<bdi>family history</bdi> القوية توجه لـ<bdi>youth onset type 2 diabetes</bdi>.",
        "<bdi>patient</bdi> مستقر (بلا <bdi>ketosis</bdi>، <bdi>HbA1c</bdi> أقل من 8.5%)، فيبدأ بـ<bdi>lifestyle change</bdi> و<bdi>metformin</bdi>، أول علاج من عمر 10.",
    ],
    "when_changes": [
        "لو عنده <bdi>ketosis</bdi> أو <bdi>DKA</bdi> أو <bdi>HbA1c</bdi> ≥8.5% مع أعراض شديدة، الجواب يصير <bdi>insulin</bdi> أول.",
        "لو كانت نتيجة واحدة فقط غير طبيعية، الجواب يصير تأكيد بتحليل ثاني أول.",
    ],
    "rule": "نتيجتين غير طبيعيتين (تحليلين مختلفين أو نفس التحليل مكرر) تثبت <bdi>diabetes</bdi>؛ عند <bdi>stable youth T2DM</bdi> نبدأ <bdi>lifestyle + metformin</bdi> مباشرة.",
    "comparison": None,
    "labs": [["Fasting glucose", "8-10 mmol/L", "<5.6 mmol/L"], ["HbA1c", "7.8%", "<5.7%"]],
    "guideline_note": None,
},

"AS-0868B": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>typical type 2 diabetes</bdi> عند <bdi>young obese female</bdi>، والسؤال عن العلاج الأول (<bdi>first line</bdi>).",
    "clues": [
        ("BMI 31", "<bdi>obesity</bdi>، عامل خطر لـ<bdi>type 2 DM</bdi>"),
        ("HbA1C 7.8", "ضمن نطاق 7.5-10% عند التشخيص"),
        ("first line anti-diabetic", "السؤال يحدد إنه يبي الدواء الأول مباشرة"),
    ],
    "why_correct": [
        "<bdi>obese</bdi> (<bdi>BMI</bdi> 31) مع <bdi>HbA1c</bdi> 7.8% وبلا <bdi>comorbidities</bdi> أخرى = <bdi>typical type 2 diabetes</bdi>.",
        "<bdi>HbA1c</bdi> بين 7.5 و10% عند التشخيص يعني <bdi>lifestyle</bdi> مع <bdi>metformin</bdi>.",
        "<bdi>metformin</bdi> هو الخط الأول لأنه <bdi>weight neutral</bdi>، لا يسبب <bdi>hypoglycemia</bdi> لوحده، ورخيص.",
    ],
    "when_changes": [
        "لو كان <bdi>HbA1c</bdi> أكثر من 10% أو فيه <bdi>ketosis</bdi>، الجواب يصير <bdi>insulin</bdi>.",
        "لو كان <bdi>eGFR</bdi> أقل من 30، <bdi>metformin</bdi> ممنوع والجواب يتغير لعلاج آخر.",
        "لو كان فيه <bdi>established cardiovascular disease</bdi> مثبتة، <bdi>GLP-1 agonist</bdi> مثل <bdi>liraglutide</bdi> يضاف أولوية أكثر كـ<bdi>add-on</bdi>.",
    ],
    "rule": "<bdi>first line T2DM drug</bdi> = <bdi>metformin</bdi> مع <bdi>lifestyle</bdi> إلا لو فيه <bdi>contraindication</bdi> (<bdi>eGFR</bdi> أقل من 30) أو <bdi>HbA1c</bdi> أكثر من 10%.",
    "comparison": None,
    "labs": [["HbA1c", "7.8%", "<5.7%"], ["BMI", "31", "18.5-24.9"]],
    "guideline_note": None,
},

"AS-0869": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نتيجة واحدة غير طبيعية فقط بلا <bdi>HbA1c</bdi> لا تكفي لتشخيص <bdi>diabetes</bdi>؛ الخطوة الأولى هي التأكيد.",
    "clues": [
        ("strong family history of diabetes", "عامل خطر، لكن لا يثبت التشخيص لوحده"),
        ("occasionally thirst", "أعراض خفيفة وغير حاسمة"),
        ("fasting blood glucose (FBG ) is 7.5 mmol/L", "نتيجة واحدة فقط فوق العتبة"),
        ("No Mention Of A1c", "مافي نتيجة ثانية مؤكدة"),
    ],
    "why_correct": [
        "نتيجة <bdi>fasting glucose</bdi> واحدة فقط (7.5 mmol/L) بلا <bdi>HbA1c</bdi> وأعراض خفيفة فقط ما تؤكد <bdi>diabetes</bdi> بشكل قاطع.",
        "بدون <bdi>unequivocal hyperglycemia</bdi>، التشخيص يحتاج نتيجتين غير طبيعيتين.",
        "فالأولوية هي <bdi>repeat the test</bdi> (أو إضافة <bdi>HbA1c</bdi>) قبل تصنيفه وبدء الأدوية.",
    ],
    "when_changes": [
        "لو كانت نتيجة ثانية غير طبيعية موجودة (مثلاً <bdi>HbA1c</bdi> ≥6.5%)، الجواب يتحول مباشرة للعلاج بـ<bdi>metformin</bdi>.",
        "لو كان عنده <bdi>random glucose</bdi> ≥11.1 مع أعراض كلاسيكية واضحة، نتيجة واحدة تكفي للتشخيص.",
    ],
    "rule": "نتيجة غير طبيعية واحدة = أكّد أولًا؛ نتيجتين غير طبيعيتين = شخّص وعالج.",
    "comparison": None,
    "labs": [["Fasting glucose", "7.5 mmol/L", "<5.6 mmol/L (Normal), 5.6-6.9 (Prediabetes), ≥7.0 (Diabetes)"]],
    "guideline_note": None,
},

"AS-0875": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>young adult</bdi> مع <bdi>rectal bleeding</bdi> وتاريخ عائلي عمودي قوي يوجه لمتلازمة <bdi>polyposis</bdi> وراثية سائدة.",
    "clues": [
        ("25-year-old", "<bdi>young adult</bdi> يناسب بداية <bdi>inherited polyposis syndrome</bdi>"),
        ("bloody stools", "<bdi>GI bleeding</bdi> من عملية مخاطية"),
        ("mother and siblings", "نمط وراثي عمودي (<bdi>autosomal dominant</bdi>)"),
    ],
    "why_correct": [
        "<bdi>25-year-old</bdi> مع ألم و<bdi>weight loss</bdi> و<bdi>bloody stools</bdi>، وأمه وأخواته عندهم نفس الصورة، يناسب حالة <bdi>autosomal dominant</bdi> بالقولون.",
        "<bdi>familial adenomatous polyposis (FAP)</bdi> تظهر بعمر صغير مع نزيف وفقدان وزن من مئات <bdi>adenomas</bdi>، وتتطور لـ<bdi>colorectal cancer</bdi> لو مو علاج.",
        "<bdi>abdomen</bdi> الطبيعي بالفحص يناسب عملية <bdi>mucosal</bdi> مو كتلة واضحة.",
    ],
    "when_changes": [
        "لو كان فيه <bdi>pigmentation</bdi> بالشفاه أو الفم مع <bdi>intussusception</bdi>، الجواب يصير <bdi>Peutz-Jeghers syndrome</bdi>.",
        "لو كان النزيف مع <bdi>urgency</bdi> و<bdi>mucus</bdi> بلا تاريخ عائلي عمودي قوي، نفكر بـ<bdi>ulcerative colitis</bdi>.",
    ],
    "rule": "<bdi>young adult</bdi> + <bdi>rectal bleeding</bdi> + تاريخ عائلي عمودي قوي = فكّر <bdi>FAP</bdi>؛ <bdi>APC gene</bdi> على <bdi>chromosome 5q</bdi>.",
    "comparison": {
        "headers": ["المتلازمة", "الصفة المميزة"],
        "rows": [
            ["<bdi>FAP</bdi>", "مئات <bdi>adenomas</bdi>، نزيف، بلا <bdi>pigmentation</bdi>"],
            ["<bdi>Peutz-Jeghers</bdi>", "<bdi>hamartomas</bdi> + <bdi>mucocutaneous pigmentation</bdi>"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},

"AS-0876": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "<bdi>significant hyperkalemia</bdi> بلا تغيّرات <bdi>ECG</bdi> حادة: الخطوة الأولى هي <bdi>shift</bdi> البوتاسيوم للخلايا مو <bdi>stabilization</bdi> أو <bdi>removal</bdi>.",
    "clues": [
        ("lethargy", "عرض عام من اضطراب <bdi>electrolyte</bdi>"),
        ("ECG shows no acute changes", "يستبعد الحاجة لـ<bdi>calcium gluconate</bdi> الفوري"),
        ("Potassium 6.6", "<bdi>significant hyperkalemia</bdi>"),
        ("Bicarbonate 15", "<bdi>metabolic acidosis</bdi> مصاحب"),
    ],
    "why_correct": [
        "<bdi>K</bdi> 6.6 هو <bdi>significant hyperkalemia</bdi>، لكن الحيوية مستقرة والـ<bdi>ECG</bdi> بلا تغيّرات حادة، فـ<bdi>membrane stabilization</bdi> بـ<bdi>calcium</bdi> غير ضروري حتمًا.",
        "العلاج الأولي الأنسب هو تحريك البوتاسيوم للخلايا بـ<bdi>insulin plus dextrose</bdi>، يعمل خلال دقائق.",
    ],
    "when_changes": [
        "لو كان الـ<bdi>ECG</bdi> يبين <bdi>peaked T waves</bdi> أو <bdi>wide QRS</bdi>، الجواب يصير <bdi>IV calcium gluconate</bdi> أول.",
        "لو فشل العلاج الدوائي أو عنده <bdi>severe renal failure</bdi>، الجواب يصير <bdi>hemodialysis</bdi>.",
    ],
    "rule": "<bdi>hyperkalemia ladder</bdi>: <bdi>stabilize</bdi> (<bdi>calcium</bdi>) لو فيه تغيّر <bdi>ECG</bdi>، ثم <bdi>shift</bdi> (<bdi>insulin/dextrose</bdi>)، ثم <bdi>remove</bdi> (<bdi>dialysis</bdi>).",
    "comparison": None,
    "labs": [
        ["Sodium", "139 mmol/L", "134-146 mmol/L"],
        ["Potassium", "6.6 mmol/L", "3.5-5.1 mmol/L"],
        ["Bicarbonate", "15 mmol/L", "21-28 mmol/L"],
        ["BUN", "9 mmol/L", "2.8-8.9 mmol/L"],
        ["Creatinine", "118 µmol/L", "44-115 µmol/L"],
    ],
    "guideline_note": None,
},

"AS-0877": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "<bdi>drug-induced gout flare</bdi> بعد إضافة أدوية جديدة لعلاج <bdi>HTN</bdi> و<bdi>DM</bdi>، والمسبب الكلاسيكي من هذه الأدوية.",
    "clues": [
        ("severe pain, redness, and swelling of the first metatarsophalangeal (MTP) joint", "صورة كلاسيكية لـ<bdi>gout</bdi> (<bdi>podagra</bdi>)"),
    ],
    "why_correct": [
        "بعد أيام من بدء أدوية جديدة، ظهر <bdi>acute pain, redness and swelling</bdi> بالـ<bdi>first MTP joint</bdi>، صورة <bdi>gout flare</bdi> (<bdi>podagra</bdi>) الكلاسيكية.",
        "<bdi>hydrochlorothiazide</bdi> هو المسبب الكلاسيكي: <bdi>thiazides</bdi> تقلل إفراغ <bdi>urate</bdi> الكلوي وتسبب <bdi>hyperuricemia</bdi>.",
    ],
    "when_changes": [
        "لو كان القائمة فيها <bdi>loop diuretic</bdi> مثل <bdi>furosemide</bdi> بدل <bdi>thiazide</bdi>، هو يصير المسبب.",
        "لو ماكان فيه <bdi>diuretic</bdi> بالقائمة، الجواب يصير <bdi>low dose aspirin</bdi> كمسبب أضعف.",
    ],
    "rule": "<bdi>thiazide</bdi> و<bdi>loop diuretics</bdi> هم المسببات الكلاسيكية لـ<bdi>gout flare</bdi>؛ ابحث عنهم أول بقائمة الأدوية.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-0879": {
    "correct_letter": "A",
    "self_judged": True,
    "idea": "<bdi>PE</bdi> بدون تقرير <bdi>vitals</bdi> واضح: بغياب دليل على <bdi>instability</bdi>، العلاج الافتراضي هو <bdi>anticoagulation</bdi> لا <bdi>thrombolysis</bdi>.",
    "clues": [
        ("pulmonary embolism", "تشخيص مؤكد، لكن درجة الخطورة غير محددة"),
        ("no vital report", "بدون دليل على <bdi>instability</bdi>، نفترض <bdi>stable</bdi>"),
    ],
    "why_correct": [
        "علاج <bdi>PE</bdi> يعتمد على حالة الدورة الدموية: <bdi>unstable/massive</bdi> يحتاج <bdi>thrombolysis</bdi>، و<bdi>stable</bdi> يحتاج <bdi>LMWH</bdi>.",
        "بما إنه مافي <bdi>vital report</bdi> يثبت <bdi>instability</bdi>، الافتراض الأسلم هو إنه <bdi>stable</bdi>، فيكون العلاج الأول <bdi>enoxaparin</bdi>.",
        "هذا سؤال <bdi>self-judged</bdi> لأن المصدر ماحدد جواب، والمنطق هنا حسب غياب علامات <bdi>shock</bdi>.",
    ],
    "when_changes": [
        "لو ذكر السؤال \"<bdi>massive</bdi>\" أو <bdi>low BP</bdi>، الجواب يتحول لـ<bdi>thrombolysis</bdi>.",
        "لو كان <bdi>anticoagulation</bdi> ممنوع، الجواب يصير <bdi>IVC filter</bdi>.",
    ],
    "rule": "بدون دليل على <bdi>massive PE</bdi> أو <bdi>shock</bdi>، العلاج الافتراضي هو <bdi>LMWH (enoxaparin)</bdi>؛ <bdi>thrombolysis</bdi> فقط لو <bdi>unstable</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-0880": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>massive PE</bdi> = <bdi>high-risk unstable PE</bdi>، والعلاج الأولي هو <bdi>thrombolysis</bdi> بغياب <bdi>contraindications</bdi>.",
    "clues": [
        ("massive pulmonary embolism", "يعني <bdi>hemodynamically unstable</bdi>، درجة خطورة عالية"),
    ],
    "why_correct": [
        "\"<bdi>massive pulmonary embolism</bdi>\" بـ<bdi>ICU</bdi> يعني <bdi>high-risk (unstable) PE</bdi>.",
        "<bdi>young</bdi>، \"<bdi>medically free</bdi>\" رجل بلا <bdi>contraindication</bdi> لـ<bdi>fibrinolysis</bdi>، فالعلاج الأولي الأنسب هو <bdi>systemic thrombolysis</bdi>.",
        "بعد الـ<bdi>thrombolysis</bdi> يعطى <bdi>heparin</bdi> للمتابعة.",
    ],
    "when_changes": [
        "لو كان فيه <bdi>contraindication</bdi> لـ<bdi>thrombolysis</bdi> (مثل <bdi>recent surgery</bdi> أو <bdi>bleeding risk</bdi>)، الجواب يصير <bdi>embolectomy</bdi>.",
        "لو كان <bdi>stable</bdi>، الجواب يصير <bdi>LMWH</bdi>.",
    ],
    "rule": "\"<bdi>massive</bdi>\" أو <bdi>hypotension/shock</bdi> بسؤال <bdi>PE</bdi> = <bdi>thrombolysis</bdi>؛ <bdi>stable patient</bdi> يأخذ <bdi>LMWH</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-0881": {
    "correct_letter": "C",
    "self_judged": True,
    "idea": "علاج <bdi>post-MI</bdi> طويل المدى (<bdi>secondary prevention</bdi>): <bdi>aspirin</bdi> مع <bdi>high intensity statin</bdi> هو الهدف المعياري.",
    "clues": [
        ("stemi", "<bdi>established ASCVD</bdi> بعد <bdi>STEMI</bdi>، يحتاج علاج <bdi>secondary prevention</bdi>"),
        ("long term", "السؤال يبي العلاج طويل المدى مو الإدارة الحادة"),
    ],
    "why_correct": [
        "بعد <bdi>STEMI</bdi> مُدار بشكل صحيح، أدوية <bdi>long term survival</bdi> الأساسية هي <bdi>aspirin</bdi> مدى الحياة و<bdi>high intensity statin</bdi>.",
        "<bdi>clinical ASCVD</bdi> المثبت يستوجب <bdi>high intensity statin</bdi> بغض النظر عن قيمة <bdi>LDL</bdi> الأساسية.",
        "هذا سؤال <bdi>self-judged</bdi> لأن المصدر ماحدد جواب؛ الاختيار هنا حسب المبدأ المعياري لـ<bdi>post-MI secondary prevention</bdi>.",
    ],
    "when_changes": [
        "لو كان عنده <bdi>reduced EF</bdi>، يضاف <bdi>beta blocker</bdi> و<bdi>ACE inhibitor</bdi> كجزء من العلاج طويل المدى.",
        "<bdi>CCB</bdi> و<bdi>warfarin</bdi> ما لهم فايدة إضافية لـ<bdi>survival</bdi> بعد <bdi>MI</bdi> بدون سبب آخر.",
    ],
    "rule": "علاج <bdi>post-MI</bdi> طويل المدى الأساسي: <bdi>aspirin</bdi> + <bdi>high intensity statin</bdi>، مع <bdi>beta blocker</bdi> و<bdi>ACEI</bdi> لو فيه <bdi>reduced EF</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-0882": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "تعريف <bdi>significant bacteriuria</bdi> التشخيصي لـ<bdi>UTI</bdi> على <bdi>urine culture</bdi>.",
    "clues": [
        ("significant or diagnostic for uti", "يبي المعيار المخبري المحدد لتشخيص <bdi>UTI</bdi>"),
    ],
    "why_correct": [
        "<bdi>urine culture</bdi> تكون <bdi>significant</bdi> لما تنمو <bdi>a single organism</bdi> بعدد ≥10^5 <bdi>CFU/mL</bdi> من عينة <bdi>clean catch midstream</bdi>.",
        "منظمة واحدة بعدد مرتفع تعكس <bdi>true bladder infection</bdi> مو <bdi>contamination</bdi>.",
    ],
    "when_changes": [
        "لو كانت العينة من <bdi>suprapubic aspirate</bdi>، أي نمو يعتبر <bdi>significant</bdi> حتى بعدد أقل.",
        "لو كانت من <bdi>catheter sample</bdi>، العتبة المقبولة أقل من 10^5.",
    ],
    "rule": "<bdi>significant bacteriuria</bdi> = منظمة واحدة بعدد مرتفع؛ <bdi>mixed growth</bdi> يعني <bdi>contamination</bdi> ونعيد العينة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-0887": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "<bdi>acute hepatocellular hepatitis</bdi> عند <bdi>young healthy patient</bdi> بلا عوامل خطر: الخطوة التالية تأكيد <bdi>acute viral hepatitis</bdi> الأشيع.",
    "clues": [
        ("yellowish discolouration", "<bdi>jaundice</bdi>، يأكد <bdi>hepatic dysfunction</bdi>"),
        ("Alanine aminotransferase 990", "ارتفاع شديد بـ<bdi>ALT</bdi> يناسب <bdi>hepatocellular pattern</bdi>"),
        ("Aspartate aminotransferase 789", "ارتفاع شديد بـ<bdi>AST</bdi>، نفس النمط"),
    ],
    "why_correct": [
        "<bdi>previously healthy</bdi> عمره 28 مع ألم و<bdi>vomiting</bdi> ثم <bdi>jaundice</bdi>، و<bdi>ALT</bdi> 990 و<bdi>AST</bdi> 789 مع <bdi>ALP</bdi> طبيعي = <bdi>acute hepatocellular hepatitis</bdi> (مو <bdi>cholestatic</bdi>).",
        "بـ<bdi>young person</bdi> بلا <bdi>alcohol</bdi> أو <bdi>drug exposure</bdi>، أشهر سبب <bdi>acute viral hepatitis</bdi> هو <bdi>hepatitis A</bdi>.",
        "التأكيد يكون بـ<bdi>anti-HAV IgM</bdi>، الفحص المناسب التالي.",
    ],
    "when_changes": [
        "لو كان عنده عوامل خطر مثل <bdi>unprotected sex</bdi> أو <bdi>IV drug use</bdi>، الجواب يصير <bdi>HBsAg</bdi>.",
        "لو كان الصورة <bdi>cholestatic</bdi> (<bdi>ALP</bdi> مرتفع مع <bdi>jaundice</bdi>)، الخطوة التالية تصير <bdi>ultrasound</bdi> مو <bdi>serology</bdi>.",
    ],
    "rule": "<bdi>acute hepatocellular hepatitis</bdi> عند <bdi>young healthy patient</bdi> بلا عوامل خطر = اطلب <bdi>HAV IgM</bdi> أول؛ <bdi>IgM</bdi> يعني الآن، <bdi>IgG</bdi> يعني قبل.",
    "comparison": None,
    "labs": [["ALT", "990 IU/L", "5-40 IU/L"], ["AST", "789 IU/L", "12-40 IU/L"], ["ALP", "109 IU/L", "39-117 IU/L"]],
    "guideline_note": None,
},

}

WHY_WRONG = {

"AS-0803": {
    "B": "<bdi>urine metanephrine</bdi> يفحص <bdi>pheochromocytoma</bdi> اللي يعطي <bdi>paroxysmal headache</bdi> و<bdi>sweating</bdi> و<bdi>palpitations</bdi>، وعادة ما يسبب <bdi>hypokalemia</bdi>.",
    "C": "<bdi>serum catecholamine</bdi> غير موثوق (إفراز متقطع وتأثر بالـ<bdi>stress</bdi>) وليس تحليل <bdi>screening</bdi> حتى لو اشتبهنا بـ<bdi>pheochromocytoma</bdi>.",
    "D": "<bdi>plasma free metanephrines</bdi> تحليل جيد لـ<bdi>pheochromocytoma</bdi> لما يكون فيه نمط <bdi>adrenergic</bdi> متقطع؛ هنا الـ<bdi>clue</bdi> هو <bdi>hypokalemia</bdi> اللي يوجه لـ<bdi>aldosterone</bdi>.",
},

"AS-0805": {
    "B": "<bdi>antibiotics</bdi> تحتاج دليل <bdi>infection</bdi> (<bdi>fever</bdi>، <bdi>urinary symptoms</bdi>)؛ الألم لوحده بدون علامة <bdi>infection</bdi> لا يبرر إعطاءها.",
    "C": "<bdi>Oxybutynin</bdi> يعالج <bdi>MS bladder symptoms</bdi> (<bdi>urgency</bdi>، <bdi>urge incontinence</bdi> من <bdi>detrusor overactivity</bdi>)، وهي لا تشتكي من هذا.",
    "D": "<bdi>Carbamazepine</bdi> يعالج <bdi>paroxysmal neuropathic pain</bdi> بـ<bdi>MS</bdi> مثل <bdi>trigeminal neuralgia</bdi> (ألم كهربائي قصير بالوجه)؛ الألم العام بالجسم ليس هذا النمط.",
},

"AS-0811": {
    "A": "<bdi>high protein, low carbohydrate diet</bdi> ليس علاج معتمد لـ<bdi>IBS</bdi>؛ الخطوة المبنية على دليل بخصوص <bdi>carbohydrate</bdi> هي <bdi>low FODMAP diet</bdi>، وتستخدم لو فشل الخط الأول.",
    "B": "<bdi>gluten free diet</bdi> يعالج <bdi>celiac disease</bdi> اللي يحتاج <bdi>positive tTG serology</bdi> و<bdi>duodenal biopsy</bdi>؛ الفحوصات الطبيعية وعدم وجود <bdi>malabsorption</bdi> تستبعدها.",
    "C": "زيادة <bdi>fiber</bdi> بشكل عام تساعد بـ<bdi>IBS constipation predominant</bdi>، لكن زيادة <bdi>insoluble fiber</bdi> بالذات ممكن تسوّي <bdi>bloating</bdi> و<bdi>diarrhea</bdi> أسوأ، فمو الخيار المناسب هنا.",
},

"AS-0813": {
    "A": "<bdi>ATN</bdi> يجي بعد <bdi>hypotension</bdi> أو <bdi>sepsis</bdi> أو <bdi>nephrotoxins</bdi> مثل <bdi>contrast</bdi>؛ مافي بالسيناريو دليل على إهانة <bdi>ischemic</bdi> أو <bdi>toxic</bdi> واضحة.",
    "B": "<bdi>kidney stones</bdi> تسبب <bdi>colicky loin pain</bdi> و<bdi>hematuria</bdi>؛ <bdi>normal electrolytes</bdi> (بلا <bdi>hypercalcemia</bdi>) ونتائج <bdi>marrow</bdi> توجه لإصابة <bdi>light chain</bdi> بدل الحصوة.",
    "D": "<bdi>Waldenström macroglobulinemia</bdi> مرض مختلف (<bdi>IgM</bdi>، <bdi>lymphoplasmacytic cells</bdi>) مع <bdi>hyperviscosity</bdi> و<bdi>lymphadenopathy</bdi>، مو <bdi>lytic back pain</bdi> و<bdi>plasma cell infiltration</bdi>، وهو تشخيص مو <bdi>mechanism</bdi>.",
},

"AS-0825": {
    "B": "<bdi>suctioning</bdi> كل ساعة بشكل روتيني يسبب ضرر لـ<bdi>mucosa</bdi> وزيادة خطر <bdi>contamination</bdi>؛ <bdi>suctioning</bdi> يكون حسب الحاجة.",
    "C": "تغيير <bdi>plastic tube</bdi> يوميًا لا يقلل <bdi>VAP</bdi> ويزيد الخطر؛ تغيير الدوائر يكون فقط لو متسخة أو معيبة.",
    "D": "<bdi>prophylactic antibiotics</bdi> غير موصى بها لأنها تنتخب <bdi>resistant organisms</bdi>؛ الـ<bdi>antibiotics</bdi> تعطى لعلاج <bdi>VAP</bdi> المثبت حسب <bdi>cultures</bdi>.",
},

"AS-0830": {
    "A": "<bdi>24h urine cortisol</bdi> يُطلب لما يكون فيه ملامح <bdi>Cushingoid</bdi> واضحة مثل <bdi>obesity</bdi> أو <bdi>striae</bdi> أو <bdi>diabetes</bdi>، وهذا غير موجود هنا.",
},

"AS-0831": {
    "A": "<bdi>antibiotics</bdi> تعالج <bdi>UTI</bdi> اللي ممكن تسبب <bdi>delirium</bdi>، لكن هذه النسخة من المصدر تربط التحسن بتصحيح <bdi>calcium</bdi> بدل علاج <bdi>infection</bdi>.",
    "C": "<bdi>sodium</bdi> 134 منخفض خفيف فقط؛ <bdi>hyponatremia</bdi> عادة تسبب <bdi>confusion</bdi> لما تكون أقل من 125 أو تنزل بسرعة.",
},

"AS-0831B": {
    "A": "<bdi>Na</bdi> 132 منخفض خفيف جدًا ونادرًا يسبب <bdi>confusion</bdi>؛ تصحيح <bdi>sodium</bdi> يكون الجواب لما يكون <bdi>Na</bdi> منخفض جدًا أو مع <bdi>seizures</bdi>.",
    "B": "<bdi>calcium</bdi> 1.97 حدّي وممكن يرجع طبيعي بعد تصحيح <bdi>albumin</bdi>، ومافي <bdi>tetany</bdi> أو <bdi>seizure</bdi> أو تغيّر بـ<bdi>QT</bdi>؛ <bdi>IV calcium gluconate</bdi> يكون الجواب لحالة <bdi>symptomatic hypocalcemia</bdi> شديدة.",
    "C": "<bdi>fluids</bdi> و<bdi>monitoring</bdi> دعم فقط ولا تعالج <bdi>infection</bdi> اللي تسبب <bdi>delirium</bdi>؛ تكون الجواب لو السبب الأساسي <bdi>dehydration</bdi> أو <bdi>hypotension</bdi>.",
},

"AS-0831C": {
    "A": "<bdi>Na</bdi> 132 خفيف ونادرًا يسبب <bdi>confusion</bdi> لوحده؛ تصحيح <bdi>sodium</bdi> يكون الهدف لو كان شديد الانخفاض أو مع <bdi>seizures</bdi> واضحة.",
    "B": "<bdi>hypocalcemia</bdi> ممكن تساهم بـ<bdi>confusion</bdi>، لكن <bdi>total calcium</bdi> 1.6 لازم يصحح بـ<bdi>albumin</bdi> أول، والسبب الحاد الواضح هو <bdi>infection</bdi>؛ <bdi>IV calcium gluconate</bdi> يكون الجواب لحالة <bdi>symptomatic</bdi> مع <bdi>tetany</bdi> أو <bdi>seizures</bdi>.",
    "C": "<bdi>patient</bdi> مرتفع ضغطها، مو جافة أو بـ<bdi>shock</bdi>، فـ<bdi>fluids</bdi> لوحدها لا تعالج السبب؛ تكون الجواب لحالة <bdi>hypovolemia</bdi> أو <bdi>septic shock</bdi>.",
},

"AS-0831D": {
    "A": "ماهي <bdi>hypotensive</bdi>، فـ<bdi>fluids</bdi> لوحدها لن تصلح <bdi>confusion</bdi>؛ تكون أول خيار لو كانت <bdi>hypotensive</bdi> أو <bdi>dehydrated</bdi>.",
    "C": "<bdi>Na</bdi> 132 خفيف جدًا عشان يسبب <bdi>delirium</bdi>؛ تصحيح <bdi>sodium</bdi> يكون الجواب لو <bdi>hyponatremia</bdi> شديد أو مع <bdi>seizures</bdi> واضحة.",
    "D": "هذا الخيار غير معروف نصّه من المصدر (\"<bdi>missing</bdi>\")، فلا يمكن تقييمه؛ المنطق الطبي ثابت على علاج <bdi>infection</bdi>.",
},

"AS-0835": {
    "B": "<bdi>Legionella</bdi> يترافق مع <bdi>travel</bdi> أو تعرض لمياه/فنادق، <bdi>GI upset</bdi>، <bdi>hyponatremia</bdi>، و<bdi>confusion</bdi>؛ السؤال يحدد عدم وجود <bdi>travel history</bdi>.",
    "C": "<bdi>Mycoplasma</bdi> يسبب <bdi>pneumonia</bdi> خفيف <bdi>atypical</bdi> عند <bdi>young people</bdi>، مع <bdi>dry cough</bdi>، و<bdi>hemoptysis</bdi> غير معتاد فيه.",
    "D": "<bdi>Strep pneumoniae</bdi> هو أشهر سبب للـ<bdi>CAP</bdi> لكنه عادة يستجيب للـ<bdi>antibiotics</bdi> المعتادة؛ هو الجواب للعرض الأولي المعتاد، مو بعد فشل علاجين.",
},

"AS-0844": {
    "B": "مافي ما يوجه لـ<bdi>TB</bdi>: مرض حاد لمدة يومين فقط، بدون <bdi>weight loss</bdi> أو <bdi>night sweats</bdi> أو تعرض؛ <bdi>TB pleurisy</bdi> يأكد بـ<bdi>fluid ADA</bdi> أو <bdi>pleural biopsy</bdi>.",
    "C": "<bdi>bronchoalveolar lavage</bdi> يستخدم لـ<bdi>non-resolving pneumonia</bdi> أو <bdi>immunocompromised host</bdi> أو اشتباه <bdi>opportunistic infection</bdi>، ولا يقيّم الـ<bdi>effusion</bdi>.",
    "D": "<bdi>antibiotics</bdi> تعالج <bdi>pneumonia</bdi> لكن لا تخبرنا لو الـ<bdi>effusion</bdi> معقد؛ <bdi>effusion</bdi> أكبر من 10 mm لازم يتاب أول.",
},

"AS-0845": {
    "B": "<bdi>cardioversion</bdi> لعلاج <bdi>unstable tachyarrhythmias</bdi> مثل <bdi>VT</bdi> أو <bdi>SVT</bdi> أو <bdi>fast AF</bdi>، مو <bdi>slow rhythm</bdi>؛ الصدمة لا ترفع المعدل، <bdi>pacing</bdi> هو اللي يرفعه.",
    "C": "<bdi>dual antiplatelet therapy</bdi> لعلاج <bdi>ACS</bdi>، لكن <bdi>cardiac enzymes</bdi> طبيعية ومافي <bdi>chest pain</bdi>؛ تكون الجواب لـ<bdi>NSTEMI</bdi> أو بعد <bdi>stent</bdi>.",
    "D": "<bdi>anticoagulation</bdi> لا يفيد <bdi>slow heart rate</bdi>؛ تكون الجواب لـ<bdi>AF stroke prevention</bdi> أو <bdi>VTE</bdi> أو ضمن علاج <bdi>ACS</bdi>.",
},

"AS-0846": {
    "A": "<bdi>acute hepatitis B</bdi> يحتاج <bdi>IgM anti-HBc</bdi> موجب، وهنا الـ<bdi>anti-HBc</bdi> من نوع <bdi>IgG</bdi> يعني العدوى ليست حديثة.",
    "C": "<bdi>resolved infection</bdi> يحتاج <bdi>HBsAg</bdi> سالب مع <bdi>anti-HBs</bdi> موجب؛ هنا <bdi>HBsAg</bdi> موجب، يعني العدوى مستمرة.",
},

"AS-0846B": {
    "A": "<bdi>previous infection</bdi> تحتاج <bdi>anti-HBs</bdi> و<bdi>anti-HBc IgG</bdi> موجبين؛ هنا <bdi>anti-HBc IgG</bdi> سالب.",
    "B": "<bdi>acute infection</bdi> تحتاج <bdi>HBsAg</bdi> موجب و<bdi>IgM anti-HBc</bdi> موجب؛ كلاهما غائب هنا.",
    "C": "<bdi>chronic infection</bdi> تحتاج <bdi>HBsAg</bdi> يستمر أكثر من 6 أشهر مع <bdi>anti-HBc IgG</bdi> موجب و<bdi>anti-HBs</bdi> سالب، وهذا عكس النمط هنا تمامًا.",
},

"AS-0848": {
    "B": "<bdi>Atrial flutter</bdi> يبين <bdi>sawtooth waves</bdi> منتظمة، وهذا غير الصورة الموصوفة بالـ<bdi>ECG</bdi> هنا.",
},

"AS-0850": {
    "A": "<bdi>cardioversion</bdi> يستخدم لـ<bdi>unstable tachyarrhythmias</bdi>، ولا يرفع معدل <bdi>bradycardia</bdi>.",
    "C": "<bdi>aspirin</bdi> لعلاج <bdi>ACS</bdi>؛ مافي <bdi>chest pain</bdi> أو صورة <bdi>ischemic</bdi> هنا.",
    "D": "<bdi>aspirin and clopidogrel</bdi> لعلاج <bdi>ACS</bdi> مثبت أو بعد <bdi>PCI</bdi>، مو لـ<bdi>bradyarrhythmia</bdi> عرضي.",
},

"AS-0853": {
    "A": "<bdi>amiodarone</bdi> دواء <bdi>rhythm control</bdi>، والسؤال يستثني <bdi>rhythm control</bdi> صراحة، وهو مو خط أول لـ<bdi>rate control</bdi> بلا <bdi>heart failure</bdi>.",
    "B": "<bdi>dual antiplatelet therapy</bdi> لعلاج <bdi>coronary disease</bdi> (<bdi>ACS</bdi>، <bdi>stents</bdi>)، مو <bdi>AFib</bdi>؛ لا تفيد بـ<bdi>rate control</bdi> وتزيد خطر النزيف بلا حماية كافية من <bdi>stroke</bdi>.",
    "D": "<bdi>DOAC</bdi> مع <bdi>beta blocker</bdi> مناسب لو درجة <bdi>CHA2DS2-VA</bdi> ≥2؛ هذا المريض <bdi>medically free</bdi>، فـ<bdi>anticoagulation</bdi> غير مؤشر حسب الدرجة.",
},

"AS-0854": {
    "B": "&lt;2.2 mmol/L ليس عتبة معيارية بأي نظام أهداف معروف؛ يقع بين هدف الوقاية الأولية والثانوية.",
    "C": "&lt;2.0 mmol/L هو الهدف الأشد المستخدم لو فيه <bdi>established ASCVD</bdi> (<bdi>MI</bdi>، <bdi>stroke</bdi>، <bdi>PAD</bdi>)، ومافي تاريخ كذا بالسؤال.",
    "D": "&lt;3.0 mmol/L هدف أوسع يستخدم فقط للأشخاص قليلي الخطورة بأنظمة معتمدة على الخطورة، مو الهدف \"<bdi>optimal</bdi>\".",
},

"AS-0868": {
    "A": "لا حاجة لتحليل إضافي يفرّق <bdi>prediabetes</bdi> عن <bdi>diabetes</bdi>: يوجد تحليلان مختلفان بالفعل بالمدى السكري؛ <bdi>random glucose</bdi> يكون تشخيصي فقط مع أعراض و≥11.1 mmol/L.",
},

"AS-0868B": {
    "A": "<bdi>sitagliptin</bdi> (<bdi>DPP-4 inhibitor</bdi>) دواء إضافي من الخط الثاني لما يكون <bdi>metformin</bdi> غير كافٍ أو غير محتمل.",
    "C": "<bdi>liraglutide</bdi> (<bdi>GLP-1 agonist</bdi>) يفيد الوزن ويفضل كـ<bdi>add on</bdi> مع <bdi>established cardiovascular disease</bdi> أو حاجة إنقاص وزن إضافية، مو الدواء الأول هنا.",
    "D": "<bdi>glimepiride</bdi> (<bdi>sulfonylurea</bdi>) يسبب <bdi>hypoglycemia</bdi> و<bdi>weight gain</bdi>، خيار سيء عند <bdi>obese patient</bdi>؛ يضاف لاحقًا.",
},

"AS-0869": {
    "A": "<bdi>metformin</bdi> يبدأ بعد تأكيد <bdi>diabetes</bdi> (نتيجتين غير طبيعيتين، أو <bdi>random glucose</bdi> عرضي ≥11.1)؛ العلاج على نتيجة واحدة غير مؤكدة سابق لأوانه.",
},

"AS-0875": {
    "A": "<bdi>Peutz-Jeghers</bdi> وراثي سائد أيضًا، لكنه يسبب <bdi>hamartomatous small bowel polyps</bdi> مع <bdi>pigmentation</bdi> بالشفاه والفم وغالبًا <bdi>intussusception</bdi>؛ مافي <bdi>pigmentation</bdi> موصوفة هنا.",
    "C": "<bdi>ulcerative colitis</bdi> يعطي <bdi>bloody diarrhea</bdi> مع <bdi>urgency</bdi> و<bdi>mucus</bdi>؛ التجمع العائلي أضعف، والأم مع الأخوات كلهم مصابين يوجه لمتلازمة <bdi>polyposis</bdi> سائدة.",
    "D": "<bdi>Crohn disease</bdi> عادة يسبب <bdi>diarrhea</bdi> غير دموي، ألم بـ<bdi>RLQ</bdi> أو كتلة، مرض حول الشرج وتقرحات فموية؛ الوراثة العمودية هنا ليست نمطه.",
},

"AS-0876": {
    "A": "<bdi>hemodialysis</bdi> خطوة أخيرة لو فشل العلاج الدوائي أو فيه <bdi>severe renal failure</bdi> أو <bdi>fluid overload</bdi>؛ <bdi>creatinine</bdi> هنا مرتفع بشكل خفيف فقط.",
    "B": "<bdi>IV bicarbonate</bdi> مساعد فقط لو فيه <bdi>acidosis</bdi> شديد؛ رغم <bdi>HCO3</bdi> 15 هو أضعف وأبطأ من <bdi>insulin/dextrose</bdi> وليس الخط الأولي المعياري.",
    "D": "<bdi>normal saline</bdi> لا ينزل <bdi>potassium</bdi> بشكل فعال؛ يستخدم لـ<bdi>volume depletion</bdi>، وغير موجود هنا.",
},

"AS-0877": {
    "A": "<bdi>low dose aspirin</bdi> يرفع <bdi>urate</bdi> بشكل معتدل، لكن <bdi>thiazide</bdi> هو المسبب الكلاسيكي والأكثر احتمالًا؛ يكون الجواب فقط لو مافي <bdi>diuretic</bdi> بالقائمة.",
    "B": "<bdi>metformin</bdi> لا يسبب <bdi>hyperuricemia</bdi> أو <bdi>gout</bdi>؛ أعراضه الجانبية الأساسية <bdi>GI upset</bdi>، نقص <bdi>B12</bdi>، و<bdi>lactic acidosis</bdi>.",
    "C": "<bdi>lisinopril</bdi> (<bdi>ACE inhibitor</bdi>) ليس مسبب <bdi>gout</bdi>؛ أعراضه الجانبية الكلاسيكية <bdi>dry cough</bdi>، <bdi>angioedema</bdi>، و<bdi>hyperkalemia</bdi>.",
},

"AS-0879": {
    "B": "\"<bdi>Thrombosis</bdi>\" (ربما يقصد <bdi>thrombolysis</bdi>) تستخدم فقط لو كان <bdi>PE</bdi> <bdi>massive/unstable</bdi>، وهذا غير مؤكد هنا بسبب غياب تقرير <bdi>vitals</bdi>.",
},

"AS-0880": {
    "A": "<bdi>warfarin</bdi> لعلاج <bdi>long-term anticoagulation</bdi>؛ يحتاج أيام ليعمل وأبدًا ما يكون علاج أولي لـ<bdi>acute PE</bdi>.",
    "C": "<bdi>LMWH</bdi> خط أول لـ<bdi>stable PE</bdi>؛ <bdi>massive PE</bdi> حالة <bdi>unstable</bdi> تحتاج <bdi>thrombolysis</bdi>.",
    "D": "<bdi>dabigatran</bdi> دواء فموي لعلاج <bdi>stable</bdi> أو طويل المدى، مو لـ<bdi>massive PE</bdi>.",
},

"AS-0881": {
    "A": "<bdi>low aspirin with statin</bdi> لا يحدد شدة <bdi>statin</bdi>؛ بعد <bdi>STEMI</bdi> المعيار هو <bdi>high intensity statin</bdi> مو مجرد أي <bdi>statin</bdi>.",
    "B": "<bdi>beta blocker and aspirin</bdi> وحدهم بدون <bdi>statin</bdi> مرتفع الكثافة ناقصين؛ <bdi>statin</bdi> عالي الكثافة ضروري بـ<bdi>ASCVD</bdi> مثبت.",
    "D": "<bdi>CCBs</bdi> ما لها فايدة <bdi>survival</bdi> إضافية بعد <bdi>MI</bdi> بدون سبب آخر يستدعيها.",
},

"AS-0882": {
    "A": "<bdi>mixed bacteria</bdi> بـ<bdi>urine culture</bdi> غالبًا تعني <bdi>contamination</bdi> أثناء جمع العينة؛ الخطوة الصحيحة إعادة عينة بطريقة سليمة، مو تشخيص <bdi>UTI</bdi>.",
},

"AS-0887": {
    "A": "<bdi>Hepatitis A IgG</bdi> يدل على عدوى سابقة أو <bdi>immunity</bdi> من تطعيم؛ يبقى موجب مدى الحياة ولا يخبرنا عن المرض الحالي.",
    "C": "<bdi>HBsAg</bdi> جزء من فحص <bdi>acute hepatitis</bdi> الكامل، لكن <bdi>hepatitis B</bdi> له فترة حضانة طويلة (أسابيع لشهور) وأقل احتمالًا هنا بدون عوامل خطر؛ يكون الفحص الأول لو فيه <bdi>unprotected sex</bdi> أو <bdi>IV drug use</bdi>.",
    "D": "<bdi>hepatitis C</bdi> نادرًا يسبب <bdi>acute icteric hepatitis</bdi> واضح، وقد يكون <bdi>anti-HCV</bdi> سالب بالبداية؛ يفحص لو فيه عوامل خطر <bdi>parenteral</bdi> أو مرض كبد مزمن.",
},

}

HIGHLIGHT_TERMS = {

"AS-0803": ["25 years old", "hypokalemia", "blood pressure still uncontrolled"],
"AS-0805": ["Multiple Sclerosis", "generalized body pain"],
"AS-0811": ["Symptoms increased with stress and after food", "Normal blood lab, normal colonoscopy"],
"AS-0813": ["Persistent Back Pain", "Creatinine: Elevated", "Bone Marrow Biopsy: 20% Plasma Cells"],
"AS-0825": ["mechanical ventilation", "fever and purulent discharge from trachea"],
"AS-0830": ["Persistent HTN", "potassium 3,2"],
"AS-0831": ["elderly", "urinary tract infection symptoms", "sudden change in mental status", "calcium 1.9", "sodium 134"],
"AS-0831B": ["elderly", "UTI symptoms and CNS symptoms", "calcium 1.97 mmol/L", "sodium 132 mmol/L", "mild cortical atrophy"],
"AS-0831C": ["elderly", "fever, dysuria, and confusion", "Na+ = 132", "Ca2+ = 1.6", "leukocytes in urine"],
"AS-0831D": ["71 year old", "S&S of UTI", "confused and unable to recall", "positive nitrites and leukocyte esterase"],
"AS-0835": ["pneumonia symptoms and hemoptysis", "Received 2 course of antibiotics but no improvement"],
"AS-0844": ["25 mm pleural effusion on decubitus film"],
"AS-0845": ["shortness of breath but no chest pain", "ECG show Bradycardia or heart block"],
"AS-0846": ["+ve HBsAg", "Anti HBc IgG"],
"AS-0846B": ["Negative", "Anti-HBsAg Positive", "Anti-HBc IgG Negative"],

}

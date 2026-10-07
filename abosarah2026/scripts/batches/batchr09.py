# -*- coding: utf-8 -*-
# Batch r09 — covers all questions in data/slices/r09.json

EXPLANATIONS = {}
WHY_WRONG = {}
HIGHLIGHT_TERMS = {}

EXPLANATIONS["AS-1300"] = {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "السؤال عن <bdi>hepatocellular carcinoma</bdi> في <bdi>cirrhotic liver</bdi>، ويبي أقوى <bdi>risk factor</bdi> له.",
    "clues": [
        ("2 Liver lesion in the right lobe", "كتلتين بالفص الأيمن تدل على <bdi>HCC</bdi> حتى يثبت عكسه"),
        ("risk factor", "السؤال يبي السبب الأقوى إحصائيًا، مو أي سبب ممكن"),
    ],
    "why_correct": [
        "<bdi>jaundice</bdi> مع كتلتين بالفص الأيمن بكبد <bdi>nodular cirrhotic</bdi> يعني <bdi>HCC</bdi> لين يثبت العكس.",
        "<bdi>chronic hepatitis B</bdi> هو أقوى وأشهر <bdi>risk factor</bdi> لـ<bdi>HCC</bdi> بالعالم والسعودية، وممكن يسبب <bdi>HCC</bdi> حتى بدون <bdi>cirrhosis</bdi>.",
        "لذلك الجواب الصحيح هو <bdi>hepatitis B</bdi> مو الأسباب الأقل شيوعًا.",
    ],
    "when_changes": [
        "لو السؤال ذكر تاريخ أكل حبوب مخزنة بظروف رطبة (<bdi>moldy grain</bdi>)، الجواب يصير <bdi>aflatoxin</bdi>.",
        "لو السؤال ذكر مريض شاب مع أعراض نفسية وعصبية وحلقة <bdi>Kayser-Fleischer</bdi>، الجواب يصير <bdi>Wilson disease</bdi>.",
    ],
    "rule": "أي سؤال عن أقوى <bdi>risk factor</bdi> لـ<bdi>HCC</bdi>، الجواب الافتراضي هو <bdi>hepatitis B</bdi> مو <bdi>aflatoxin</bdi> أو <bdi>Wilson disease</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1300"] = {
    "A": "<bdi>aflatoxin</bdi> سبب حقيقي لـ<bdi>HCC</bdi> ويتعاون مع <bdi>HBV</bdi>، بس أقل شيوعًا بكثير كسبب أساسي، ويصير الجواب لو السؤال ركز على أكل حبوب متعفنة.",
    "B": "<bdi>lead toxicity</bdi> مش سبب معروف لـ<bdi>HCC</bdi>، هو يسبب <bdi>anemia</bdi> مع <bdi>basophilic stippling</bdi> و<bdi>neuropathy</bdi> وألم بطن.",
    "C": "<bdi>Wilson disease</bdi> تسبب <bdi>cirrhosis</bdi> بس خطر <bdi>HCC</bdi> فيها أقل من <bdi>viral hepatitis</bdi>، وتفكر فيها بمريض شاب مع أعراض عصبية نفسية وحلقة <bdi>Kayser-Fleischer</bdi>.",
}
HIGHLIGHT_TERMS["AS-1300"] = ["2 Liver lesion in the right lobe", "risk factor"]

EXPLANATIONS["AS-1301"] = {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "مريض على <bdi>methotrexate</bdi> لـ<bdi>rheumatoid arthritis</bdi> جاله <bdi>mouth ulcer</bdi> و<bdi>rigor</bdi>، والسؤال يبي السبب.",
    "clues": [
        ("methotrexate", "دواء يسبب <bdi>bone marrow suppression</bdi> و<bdi>mucosal toxicity</bdi>"),
        ("mouth ulcer and rigor", "<bdi>mucositis</bdi> مع علامات <bdi>infection</bdi> يدل على <bdi>neutropenia</bdi>"),
    ],
    "why_correct": [
        "<bdi>methotrexate</bdi> مضاد لـ<bdi>folate</bdi> يسبب <bdi>bone marrow suppression</bdi> و<bdi>mucosal toxicity</bdi>.",
        "لذلك ظهور <bdi>mouth ulcers</bdi> مع <bdi>rigor</bdi> (حمى شديدة) يدل على <bdi>neutropenia</bdi> ناتج من الدواء مع <bdi>infection</bdi> مصاحبة.",
        "<bdi>management</bdi> يشمل إيقاف <bdi>methotrexate</bdi>، فحص <bdi>CBC</bdi>، علاج <bdi>febrile neutropenia</bdi>، وإعطاء <bdi>folinic acid</bdi>.",
    ],
    "when_changes": [
        "لو السؤال ذكر <bdi>splenomegaly</bdi> مع <bdi>RA</bdi> قديمة <bdi>seropositive</bdi>، الجواب يصير <bdi>Felty syndrome</bdi>.",
    ],
    "rule": "<bdi>mouth ulcers</bdi> + حمى عند مريض على <bdi>methotrexate</bdi> = <bdi>marrow toxicity</bdi>، و<bdi>Felty</bdi> يحتاج <bdi>splenomegaly</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1301"] = {
    "A": "<bdi>Felty syndrome</bdi> يحتاج <bdi>RA</bdi> طويلة <bdi>seropositive</bdi> مع <bdi>splenomegaly</bdi> (<bdi>SANTA</bdi>)، ولا شي من هذا مذكور هنا.",
}
HIGHLIGHT_TERMS["AS-1301"] = ["methotrexate", "mouth ulcer and rigor"]

EXPLANATIONS["AS-1302"] = {
    "correct_letter": "A",
    "self_judged": True,
    "idea": "امرأة عندها <bdi>MVP</bdi> و<bdi>severe MR</bdi> بدون تاريخ <bdi>endocarditis</bdi>، تبي تسوي إجراء أسنان، والسؤال عن <bdi>IE prophylaxis</bdi>.",
    "clues": [
        ("MVP and sever MR", "<bdi>native valve disease</bdi> بدون <bdi>prosthetic material</bdi>"),
        ("without endocarditis", "ما عندها تاريخ سابق لـ<bdi>infective endocarditis</bdi>"),
        ("dentist procedure", "إجراء أسنان قد يحتاج <bdi>IE prophylaxis</bdi> بحالات معينة فقط"),
    ],
    "why_correct": [
        "<bdi>IE prophylaxis</bdi> قبل إجراء الأسنان مقصورة على فئات عالية الخطورة: <bdi>prosthetic valve</bdi>، تاريخ سابق لـ<bdi>endocarditis</bdi>، أمراض قلب خلقية معينة، أو زراعة قلب مع مشكلة بالصمام.",
        "<bdi>MVP</bdi> مع <bdi>MR</bdi> حتى لو <bdi>severe</bdi> هو <bdi>native valve disease</bdi> ولا يدخل بهذي الفئات، فلا يحتاج <bdi>prophylaxis</bdi> حسب القاعدة الحديثة.",
        "درجة شدة <bdi>MR</bdi> لا تغيّر القاعدة؛ القرار يعتمد على نوع الصمام (<bdi>native</bdi> مقابل <bdi>prosthetic</bdi>) وتاريخ <bdi>endocarditis</bdi>، مو على شدة التسريب.",
    ],
    "when_changes": [
        "لو كان عندها صمام صناعي (<bdi>prosthetic valve</bdi>) أو تاريخ سابق لـ<bdi>infective endocarditis</bdi>، الجواب يصير إعطاء <bdi>amoxicillin</bdi> قبل الإجراء.",
    ],
    "rule": "شدة <bdi>MR</bdi> ما تغيّر القاعدة: <bdi>native MVP/MR</bdi> لوحدها أبدًا لا تستحق <bdi>IE prophylaxis</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": "المصدر نفسه غير متأكد من هذا السؤال (توجد نسخة أخرى بخيارات مختلفة)، لكن حسب القاعدة الحديثة لـ<bdi>IE prophylaxis</bdi> فإن <bdi>native MVP/MR</bdi> بدون تاريخ <bdi>endocarditis</bdi> لا تحتاج <bdi>prophylaxis</bdi>.",
}
WHY_WRONG["AS-1302"] = {
    "B": "<bdi>amoxicillin</bdi> هو دواء <bdi>IE prophylaxis</bdi> الصحيح، بس فقط للفئات عالية الخطورة؛ هذي المريضة <bdi>native valve disease</bdi> فقط فلا تحتاجه.",
}
HIGHLIGHT_TERMS["AS-1302"] = ["MVP and sever MR", "without endocarditis", "dentist procedure"]

EXPLANATIONS["AS-1304"] = {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "مدخن كبير بالسن مع <bdi>weight loss</bdi> و<bdi>pleural effusion</bdi> دموي <bdi>exudative</bdi>، يبي الخطوة التالية.",
    "clues": [
        ("40-pack-year smoking history", "عامل خطورة قوي لسرطان الرئة"),
        ("bloody fluid", "<bdi>effusion</bdi> دموي يرفع الشك بـ<bdi>malignancy</bdi>"),
        ("strongly exudative", "يثبت أنه <bdi>exudate</bdi> لا <bdi>transudate</bdi>"),
    ],
    "why_correct": [
        "مريض بعمر 69 سنة مدخن بشدة مع <bdi>6 months</bdi> من <bdi>weight loss</bdi> و<bdi>effusion</bdi> دموي <bdi>exudative</bdi> أكبر الاحتمالات أنه <bdi>lung cancer</bdi> أو <bdi>pleural malignancy</bdi>.",
        "الخطوة التالية هي <bdi>CT chest with contrast</bdi> لإظهار الكتلة والعقد اللمفاوية وسماكة الغشاء الجنبي.",
        "بعد ذلك يتم التخطيط لـ<bdi>biopsy</bdi> موجه بالتصوير.",
    ],
    "when_changes": [
        "لو كان المريض يشكو من حمى وكحة مع ارتفاع <bdi>inflammatory markers</bdi>، الجواب يصير <bdi>empirical antibiotics</bdi> لـ<bdi>parapneumonic effusion</bdi>.",
    ],
    "rule": "مدخن + <bdi>weight loss</bdi> + <bdi>bloody exudate</bdi> = <bdi>malignancy</bdi> لين يثبت العكس؛ صوّر قبل لا تخز (<bdi>biopsy</bdi>).",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1304"] = {
    "A": "<bdi>empirical antibiotics</bdi> تناسب <bdi>parapneumonic effusion</bdi> مع حمى وكحة وارتفاع مؤشرات الالتهاب، مو <bdi>effusion</bdi> دموي مع <bdi>weight loss</bdi> لأشهر.",
    "C": "<bdi>blind pleural biopsy</bdi> حساسيتها منخفضة؛ عند الاشتباه بـ<bdi>malignancy</bdi> يجب أن تكون موجهة بالتصوير (<bdi>CT-guided</bdi> أو <bdi>thoracoscopic</bdi>) بعد <bdi>CT</bdi>.",
}
HIGHLIGHT_TERMS["AS-1304"] = ["40-pack-year smoking history", "bloody fluid", "strongly exudative"]

EXPLANATIONS["AS-1305"] = {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نفس سيناريو السؤال السابق (مدخن كبير مع <bdi>bloody exudative effusion</bdi>)، بخيار C مختلف قليلًا.",
    "clues": [
        ("40-pack-year smoking history", "عامل خطورة قوي لسرطان الرئة"),
        ("bloody fluid", "يرفع الشك بـ<bdi>malignancy</bdi>"),
        ("strongly exudative", "يثبت أنه <bdi>exudate</bdi>"),
    ],
    "why_correct": [
        "<bdi>69 years</bdi> مدخن بشدة مع <bdi>6 months weight loss</bdi> و<bdi>effusion</bdi> دموي <bdi>exudative</bdi> كبير = <bdi>malignancy</bdi> (سرطان رئة أو <bdi>mesothelioma</bdi>) لين يثبت العكس.",
        "بعد سحب العينة، الخطوة التالية <bdi>contrast CT chest</bdi> لإظهار الكتلة وسماكة الغشاء والعقد اللمفاوية وتخطيط أفضل مكان لـ<bdi>biopsy</bdi>.",
        "<bdi>biopsy</bdi> النسيجي يجي بعد التصوير، وليس قبله.",
    ],
    "when_changes": [
        "لو وُجدت حمى وأعراض حادة مع ارتفاع المؤشرات الالتهابية، الجواب يصير <bdi>empirical antibiotics</bdi>.",
    ],
    "rule": "مدخن + <bdi>weight loss</bdi> + <bdi>bloody exudate</bdi> → <bdi>CT chest with contrast</bdi> قبل أي <bdi>biopsy</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1305"] = {
    "A": "<bdi>empirical antibiotics</bdi> تناسب <bdi>parapneumonic effusion</bdi> أو <bdi>empyema</bdi> بصورة حادة، مو <bdi>6 months weight loss</bdi> مع <bdi>bloody effusion</bdi>.",
    "C": "<bdi>tissue</bdi> لازم بالنهاية، بس <bdi>pleural biopsy</bdi> يجب أن تكون موجهة بالتصوير بعد <bdi>CT</bdi>؛ <bdi>blind biopsy</bdi> قبل التصوير حساسيتها أقل.",
}
HIGHLIGHT_TERMS["AS-1305"] = ["40-pack-year smoking history", "bloody fluid", "strongly exudative"]

EXPLANATIONS["AS-1321"] = {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "مريض <bdi>severe CAP</bdi> مع <bdi>sepsis</bdi> وانخفاض ضغط ولاكتات مرتفع، والسؤال عن الخطوة الأولى بالعلاج.",
    "clues": [
        ("fever chils", "صورة <bdi>infection</bdi> حادة"),
        ("Bp90/50", "<bdi>hypotension</bdi> واضح"),
        ("MAP is 63", "أقل من 65 يدل على <bdi>hypoperfusion</bdi>"),
        ("Lactic acid venous 4", "<bdi>lactate</bdi> مرتفع يدل على نقص تروية بالأنسجة"),
    ],
    "why_correct": [
        "هذه صورة <bdi>severe community acquired pneumonia</bdi> مع <bdi>sepsis-induced hypoperfusion</bdi>: حمى، بلغم قيحي، <bdi>BP 90/50 (MAP 63)</bdi>، <bdi>HR 128</bdi>، <bdi>lactate 4</bdi>، ارتفاع <bdi>creatinine</bdi>، و<bdi>GCS 12</bdi>.",
        "السؤال يوضح أنه لم يُعطَ <bdi>fluid</bdi> بعد، فالخطوة الأولى لاستعادة التروية هي <bdi>IV crystalloid resuscitation</bdi>.",
        "<bdi>antibiotics</bdi> تبدأ بنفس الساعة الأولى، لكن التهديد الفوري هنا هو الدوران (<bdi>circulation</bdi>).",
    ],
    "when_changes": [
        "لو استمر انخفاض الضغط بعد إعطاء <bdi>fluids</bdi> كافية، الجواب يصير <bdi>vasopressor</bdi> (<bdi>norepinephrine</bdi>).",
        "لو كان <bdi>Hb</bdi> أقل من 7 بدون نزيف نشط، الجواب يصير <bdi>blood transfusion</bdi>.",
    ],
    "rule": "بأول ساعة من <bdi>sepsis</bdi> مع <bdi>hypotension</bdi> أو <bdi>lactate ≥ 4</bdi> ولم تُعطَ <bdi>fluids</bdi> بعد، الجواب هو <bdi>fluid resuscitation</bdi> أولًا.",
    "comparison": None,
    "labs": [
        ["BP", "90/50 mmHg", "≥ 90/60 mmHg"],
        ["MAP", "63 mmHg", "≥ 65 mmHg"],
        ["Lactic acid (venous)", "4 mmol/L", "up to 2 mmol/L"],
        ["WBC", "18 ×10⁹/L", "4-11 ×10⁹/L"],
        ["Creatinine", "190 µmol/L", "up to 115 µmol/L"],
        ["Hemoglobin", "10.1 g/dL", "13.5-17.5 g/dL (male)"],
    ],
    "guideline_note": None,
}
WHY_WRONG["AS-1321"] = {
    "B": "<bdi>vasopressor</bdi> يكون صحيح لو استمر انخفاض الضغط بعد إعطاء <bdi>fluids</bdi> كافية (<bdi>septic shock</bdi>)؛ هنا لم تُعطَ <bdi>fluids</bdi> بعد فهذا سابق لأوانه.",
    "C": "<bdi>Hb 10.1</bdi> أعلى من حد نقل الدم المعتاد (7 g/dL) بـ<bdi>sepsis</bdi> بدون نزيف نشط أو إقفار قلبي، فلا يوجد مؤشر لـ<bdi>transfusion</bdi>.",
    "D": "<bdi>antibiotics</bdi> ضرورية بأول ساعة مع <bdi>fluids</bdi>، لكن عند سؤال عن الخطوة الوحيدة الأولى بمريض منخفض الضغط ونقص تروية، الأولوية للدوران (<bdi>fluids</bdi>)؛ لو كان المريض مستقر همودينامكيًا كان الجواب يصير <bdi>antibiotics</bdi>.",
}
HIGHLIGHT_TERMS["AS-1321"] = ["fever chils", "Bp90/50", "MAP is 63", "Lactic acid venous 4"]

EXPLANATIONS["AS-1323"] = {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "مريض <bdi>COPD</bdi> عنده <bdi>acidosis</bdi> (معروفة من غاز الدم)، والسؤال عن أول <bdi>investigation</bdi> يسوّى.",
    "clues": [
        ("COPD", "خلفية مرضية مزمنة"),
        ("ACIDOSIS", "<bdi>respiratory acidosis</bdi> موجودة بالفعل من غاز الدم"),
        ("INITIAL INVESTIGATION", "يبي الفحص الأول، مو العلاج"),
    ],
    "why_correct": [
        "مريض <bdi>COPD</bdi> مع <bdi>acidosis</bdi> يعني <bdi>exacerbation</bdi> حادة مع <bdi>ventilatory failure</bdi>.",
        "أول فحص يُسوّى هو <bdi>chest X-ray</bdi> لإيجاد السبب المحرّض أو المضاعفة اللي تغيّر العلاج: <bdi>pneumonia</bdi>, <bdi>pneumothorax</bdi>, <bdi>pulmonary edema</bdi>, أو <bdi>effusion</bdi>.",
        "هو فحص سريع وعند السرير ويُسوّى لكل مريض مُنوّم بـ<bdi>exacerbation</bdi>.",
    ],
    "when_changes": [
        "لو كان السؤال يبي فحص لتشخيص <bdi>PE</bdi> مشتبه فيه، الجواب يصير <bdi>CT pulmonary angiography</bdi>.",
    ],
    "rule": "<bdi>acidosis</bdi> معروفة مسبقًا → أول/initial investigation هو <bdi>CXR</bdi> لإيجاد المحرّض.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1323"] = {
    "A": "<bdi>CT with contrast</bdi> ليس فحص أولي بـ<bdi>COPD exacerbation</bdi>؛ يُحجز لـ<bdi>CT pulmonary angiography</bdi> عند الاشتباه بـ<bdi>PE</bdi> بعد التقييم الأولي.",
    "C": "<bdi>CBC</bdi> جزء من فحوصات القبول الروتينية، لكنها داعمة ولا تحدد المحرّض مثل <bdi>CXR</bdi>.",
    "D": "<bdi>sputum culture</bdi> يُطلب عند وجود بلغم قيحي أو عند التنويم لتوجيه المضادات، لكن نتائجه متأخرة وليس هو الفحص الأولي.",
}
HIGHLIGHT_TERMS["AS-1323"] = ["COPD", "ACIDOSIS", "INITIAL INVESTIGATION"]

EXPLANATIONS["AS-1334"] = {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "امرأة بتاريخ <bdi>rheumatic fever</bdi> قديم مع نفخة قلبية جديدة، والسؤال عن أفضل خطوة وقائية مستقبلية.",
    "clues": [
        ("Rheumatic fever 15 years ago", "خلفية تؤهب لأمراض الصمامات الروماتيزمية"),
        ("blowing Diastolic decrescendo murmur at aortic area", "نفخة <bdi>aortic regurgitation</bdi> الكلاسيكية"),
        ("BP 154/56", "<bdi>wide pulse pressure</bdi> يدعم <bdi>AR</bdi>"),
    ],
    "why_correct": [
        "النفخة الانبساطية <bdi>blowing decrescendo</bdi> بمنطقة الأبهر مع <bdi>wide pulse pressure</bdi> بعد <bdi>rheumatic fever</bdi> تشير إلى <bdi>rheumatic aortic regurgitation</bdi>.",
        "أي نفخة قلبية جديدة لازم تُقيَّم أولًا بـ<bdi>transthoracic echo</bdi> لمعرفة الشدة وحجم ووظيفة البطين الأيسر.",
        "قرار المراقبة أو التوقيت الجراحي يعتمد كليًا على نتيجة هذا <bdi>echo</bdi>، فهو الخطوة الأهم هنا.",
    ],
    "when_changes": [
        "لو كان لديها صمام صناعي أو تاريخ سابق لـ<bdi>endocarditis</bdi>، الجواب يصير <bdi>prophylactic antibiotics</bdi> قبل إجراء الأسنان.",
    ],
    "rule": "نفخة قلبية جديدة = <bdi>echo</bdi> أولًا؛ <bdi>rheumatic valve disease</bdi> لوحدها لا تستحق <bdi>dental prophylaxis</bdi>.",
    "comparison": None,
    "labs": [["Blood pressure", "154/56 mmHg", "~120/80 mmHg"]],
    "guideline_note": None,
}
WHY_WRONG["AS-1334"] = {
    "A": "<bdi>annual chest X-ray</bdi> ليس أداة مراقبة لأمراض الصمامات أو للتدخين؛ لا يقيّم شدة <bdi>regurgitation</bdi> أو وظيفة البطين.",
    "B": "<bdi>colorectal screening</bdi> ليست القضية المطروحة، ولا يوجد فاصل زمني موصى به لـ<bdi>annual sigmoidoscopy</bdi>.",
    "D": "<bdi>native valve disease</bdi> من <bdi>rheumatic heart disease</bdi> بدون تاريخ <bdi>endocarditis</bdi> ليست من مؤشرات <bdi>dental prophylaxis</bdi> حسب التوجيهات الحديثة.",
}
HIGHLIGHT_TERMS["AS-1334"] = ["Rheumatic fever 15 years ago", "blowing Diastolic decrescendo murmur at aortic area", "BP 154/56"]

EXPLANATIONS["AS-1345"] = {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "شاب مع <bdi>bloody diarrhea</bdi> و<bdi>tenesmus</bdi> لأسبوعين، والسؤال عن الفحص المثبت للتشخيص.",
    "clues": [
        ("2-week history of bloody diarrhea", "<bdi>subacute colitis</bdi> نمطية لـ<bdi>ulcerative colitis</bdi>"),
        ("tenesmus", "يدل على التهاب يشمل المستقيم"),
    ],
    "why_correct": [
        "<bdi>28 years</bdi> مع أسبوعين من <bdi>bloody diarrhea</bdi> وتقلصات و<bdi>tenesmus</bdi> يوافق صورة <bdi>ulcerative colitis</bdi>.",
        "السؤال يبي الفحص اللي <bdi>establishes the diagnosis</bdi>: <bdi>colonoscopy</bdi> مع <bdi>biopsy</bdi> تُظهر الالتهاب المستمر من المستقيم وتعطي <bdi>histology</bdi> مؤكدة.",
    ],
    "when_changes": [
        "لو كانت هناك علامات <bdi>toxic megacolon</bdi> (حمى، تسرع قلب، توسع كبير بالقولون)، الجواب يصير تجنب <bdi>full colonoscopy</bdi> واستخدام <bdi>flexible sigmoidoscopy</bdi> مع تصوير.",
    ],
    "rule": "اشتباه <bdi>IBD</bdi>: فحوصات البراز تستثني العدوى، و<bdi>colonoscopy with biopsy</bdi> هي اللي تثبت التشخيص.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1345"] = {
    "B": "<bdi>abdominal CT</bdi> تُظهر سماكة جدار الأمعاء ومضاعفات مثل الانثقاب أو <bdi>toxic megacolon</bdi>، لكن لا تثبت المرض بالغشاء المخاطي ولا تعطي <bdi>histology</bdi>.",
    "C": "<bdi>C. difficile toxin</bdi> يُطلب بعد التعرض للمضادات أو التنويم أو بحالة <bdi>IBD</bdi> معروفة؛ لا يوجد تعرض كذا هنا، ولا يشخص <bdi>UC</bdi>.",
    "D": "<bdi>stool culture</bdi> يستثني العدوى فقط، ونتيجته السلبية لا تثبت التشخيص.",
}
HIGHLIGHT_TERMS["AS-1345"] = ["2-week history of bloody diarrhea", "tenesmus"]

EXPLANATIONS["AS-1346"] = {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "شاب مع <bdi>DVT</bdi> كبير بالساق مع أعراض اشتباه <bdi>PE</bdi>، والسؤال عن العلاج الفوري.",
    "clues": [
        ("left leg swelling and pain", "<bdi>whole leg</bdi> يدل على <bdi>proximal DVT</bdi>"),
        ("chest tightness and shortness of breath", "علامات احتمال <bdi>embolization</bdi> لـ<bdi>PE</bdi>"),
    ],
    "why_correct": [
        "تورم كامل الساق إلى الفخذ يدل على <bdi>proximal DVT</bdi>، وظهور ضيق تنفس وألم صدر مع <bdi>sinus tachycardia</bdi> يدل أنه انتقل لـ<bdi>PE</bdi>.",
        "بمريض مستقر، الخطوة الفورية هي <bdi>parenteral anticoagulation</bdi>؛ <bdi>LMWH</bdi> هو الخط الأول، وإذا لم يُعرض فـ<bdi>unfractionated heparin</bdi> هو الصحيح 'بهذا الوقت'.",
    ],
    "when_changes": [
        "لو كان المريض غير مستقر (<bdi>hypotension</bdi>) بسبب <bdi>PE</bdi>، الجواب يصير <bdi>thrombolysis</bdi>.",
    ],
    "rule": "'At this time' تعني العلاج الحاد: <bdi>heparin</bdi> أبدًا مو <bdi>warfarin</bdi> لوحده ولا مضاد صفائح.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1346"] = {
    "A": "<bdi>aspirin</bdi> مضاد صفائح، ولا دور له بعلاج <bdi>VTE</bdi> الذي يحتاج تجلط غني بالفيبرين يُعالَج بمضادات التجلط.",
    "B": "<bdi>clopidogrel</bdi> أيضًا مضاد صفائح يُستخدم لأمراض الشرايين، مو <bdi>DVT</bdi> أو <bdi>PE</bdi>.",
    "C": "<bdi>warfarin</bdi> يُستخدم لمضاد تجلط طويل الأمد ولازم يتداخل مع <bdi>heparin</bdi> حتى يصل <bdi>INR</bdi> للعلاج؛ لوحده بالبداية بطيء وقد يسبب حالة تخثرية مؤقتة.",
}
HIGHLIGHT_TERMS["AS-1346"] = ["left leg swelling and pain", "chest tightness and shortness of breath"]

EXPLANATIONS["AS-1359"] = {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "مريض خرج من المستشفى بعد علاج <bdi>pneumonia</bdi> ورجع بحمى وضيق تنفس مع <bdi>effusion</bdi>، والسؤال عن أفضل علاج.",
    "clues": [
        ("recent hospitalization 10 days ago for pneumonia", "خلفية <bdi>hospital-acquired</bdi> حديثة"),
        ("low-grade fever", "استمرار العدوى"),
        ("Moderate right-sided pleural effusion", "<bdi>parapneumonic effusion</bdi> محتمل"),
    ],
    "why_correct": [
        "تنويمه قبل 10 أيام بـ<bdi>pneumonia</bdi> مع حمى خفيفة وزيادة ضيق تنفس و<bdi>effusion</bdi> متوسط يعني عدوى مكتسبة من المستشفى مع <bdi>parapneumonic effusion</bdi> أو <bdi>empyema</bdi>.",
        "<bdi>piperacillin-tazobactam</bdi> يغطي <bdi>Pseudomonas</bdi> وغيره من جراثيم المستشفى، ولازم يتم <bdi>drain</bdi> للسائل المصاب للتحكم بالمصدر.",
    ],
    "when_changes": [
        "لو كانت العدوى مكتسبة من المجتمع بدون تنويم حديث، الجواب يصير <bdi>ceftriaxone and azithromycin</bdi>.",
    ],
    "rule": "<bdi>pneumonia</bdi> بعد المستشفى + <bdi>effusion</bdi> = <bdi>drain</bdi> + مضاد يغطي <bdi>Pseudomonas</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1359"] = {
    "A": "<bdi>ceftriaxone + azithromycin</bdi> نظام لـ<bdi>CAP</bdi> فقط، ولا يُصرّف السائل المصاب.",
    "B": "التصريف صحيح، لكن <bdi>levofloxacin</bdi> وحده تغطيته لللا هوائيات ضعيفة ومعرض للمقاومة بعد دورة مضادات حديثة.",
    "C": "الانتظار غير آمن مع حمى وضيق تنفس متزايد و<bdi>effusion</bdi> متوسط يشير لـ<bdi>complicated parapneumonic effusion</bdi>.",
}
HIGHLIGHT_TERMS["AS-1359"] = ["recent hospitalization 10 days ago for pneumonia", "low-grade fever", "Moderate right-sided pleural effusion"]

EXPLANATIONS["AS-1360"] = {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "نفس سيناريو السؤال السابق، بخيار D مختلف قليلاً (<bdi>small-bore</bdi> drain محدد).",
    "clues": [
        ("recent hospitalization 10 days ago for pneumonia", "خلفية مستشفى حديثة"),
        ("low-grade fever", "عدوى مستمرة"),
        ("Moderate right-sided pleural effusion", "<bdi>complicated effusion</bdi> محتمل"),
    ],
    "why_correct": [
        "حمى وضيق تنفس بعد أيام من الخروج من تنويم بـ<bdi>pneumonia</bdi> مع <bdi>effusion</bdi> متوسط = عدوى جنبية معقدة.",
        "السائل المصاب لازم يُصرّف، و<bdi>small-bore drain</bdi> كافٍ لمعظم الحالات، مع تغطية واسعة (<bdi>piperacillin-tazobactam</bdi>) لأنه كان بالمستشفى حديثًا وأخذ دورة مضادات كاملة.",
    ],
    "when_changes": [
        "لو كانت العدوى مكتسبة من المجتمع بدون تنويم حديث، الجواب يصير <bdi>ceftriaxone and azithromycin</bdi>.",
    ],
    "rule": "عدوى بعد المستشفى + <bdi>effusion</bdi> لا يتحسن = صرّف + مضاد يغطي <bdi>Pseudomonas</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1360"] = {
    "A": "<bdi>ceftriaxone + azithromycin</bdi> نظام <bdi>CAP</bdi>، تغطيته ضعيفة بعد تنويم حديث ولا يصرف السائل.",
    "B": "التصريف صحيح، لكن <bdi>levofloxacin</bdi> تغطيته لللاهوائيات ضعيفة هنا، و<bdi>chest tube</bdi> كبير ليس ضروريًا دائمًا.",
    "C": "الانتظار غير آمن مع استمرار الحمى و<bdi>effusion</bdi> متوسط بعد <bdi>pneumonia</bdi>.",
}
HIGHLIGHT_TERMS["AS-1360"] = ["recent hospitalization 10 days ago for pneumonia", "low-grade fever", "Moderate right-sided pleural effusion"]

EXPLANATIONS["AS-1362"] = {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "مريضة <bdi>COPD</bdi> مع علامات احتقان وريدي جهازي، والسؤال عن السبب.",
    "clues": [
        ("COPD", "خلفية <bdi>chronic hypoxic lung disease</bdi>"),
        ("LL edema", "احتقان وريدي جهازي"),
        ("raised JVP with giant 'a' wave", "يدل على <bdi>pulmonary hypertension</bdi> و<bdi>RV hypertrophy</bdi>"),
    ],
    "why_correct": [
        "مريضة <bdi>COPD</bdi> مع ارتفاع <bdi>JVP</bdi>، <bdi>hepatomegaly</bdi>، <bdi>ascites</bdi> وتورم الساقين هي صورة احتقان وريدي جهازي، أي <bdi>right heart failure</bdi>.",
        "مرض الرئة المزمن المصحوب بنقص أكسجين يسبب <bdi>pulmonary hypertension</bdi> ثم فشل البطين الأيمن (<bdi>cor pulmonale</bdi>).",
        "<bdi>giant a wave</bdi> يعكس البطين الأيمن المتضخم المتصلب اللي الأذين الأيمن يدفع ضده.",
    ],
    "when_changes": [
        "لو كانت العلامات الغالبة <bdi>orthopnea</bdi> و<bdi>PND</bdi> وخراخر قاعدية مع <bdi>S3</bdi>، الجواب يصير <bdi>Lt HF</bdi>.",
    ],
    "rule": "<bdi>ascites</bdi> مع <bdi>JVP</bdi> مرتفع = قلبي؛ <bdi>ascites</bdi> مع <bdi>JVP</bdi> طبيعي = كبدي.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1362"] = {
    "B": "<bdi>Lt HF</bdi> تُقدّم باحتقان رئوي: <bdi>orthopnea</bdi>، <bdi>PND</bdi>، خراخر قاعدية، <bdi>S3</bdi>؛ هنا الصورة احتقان جهازي بمريضة <bdi>COPD</bdi>.",
    "C": "<bdi>chronic liver disease</bdi> تعطي <bdi>ascites</bdi> وتورم لكن مع <bdi>JVP</bdi> طبيعي أو منخفض، وعلامات مرض كبدي؛ <bdi>JVP</bdi> المرتفع مع <bdi>giant a wave</bdi> يشير للقلب.",
}
HIGHLIGHT_TERMS["AS-1362"] = ["COPD", "LL edema", "raised JVP with giant 'a' wave"]

EXPLANATIONS["AS-1365"] = {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "امرأة بالثلاثينات مع ضيق تنفس وألم صدر مفاجئ و<bdi>D-dimer</bdi> مرتفع وعلامات <bdi>right heart strain</bdi> بالـ<bdi>ECG</bdi>، السؤال عن أفضل فحص.",
    "clues": [
        ("shortness of breath and chest pain for one day", "بداية مفاجئة بدون كحة أو حمى"),
        ("D dimer 800 high", "يرفع الشك بـ<bdi>PE</bdi>"),
        ("right deviation with right bundle branch block", "علامات <bdi>right heart strain</bdi> بسبب <bdi>PE</bdi>"),
    ],
    "why_correct": [
        "ضيق تنفس وألم صدر مفاجئ بدون كحة أو حمى، مع <bdi>D-dimer</bdi> مرتفع وعلامات <bdi>right heart strain</bdi> (<bdi>peaked P</bdi>, <bdi>right axis deviation</bdi>, <bdi>RBBB</bdi>) تجعل <bdi>pulmonary embolism</bdi> التشخيص المرجّح.",
        "المريضة 'مستقرة حيويًا' فتستطيع الذهاب لـ<bdi>CT</bdi>، و<bdi>CT pulmonary angiography</bdi> هو الفحص اللي يثبت التشخيص.",
    ],
    "when_changes": [
        "لو كانت المريضة غير مستقرة همودينامكيًا، الجواب يصير <bdi>bedside echo</bdi>.",
        "لو كان هناك فشل كلوي أو حمل أو حساسية صبغة، الجواب يصير <bdi>V/Q scan</bdi>.",
    ],
    "rule": "'مستقرة حيويًا' تذهب لـ<bdi>CTPA</bdi>؛ انخفاض الضغط يحوّل الجواب لـ<bdi>bedside echo</bdi>.",
    "comparison": None,
    "labs": [["D-dimer", "800 (high)", "typically < 500 ng/mL FEU"]],
    "guideline_note": None,
}
WHY_WRONG["AS-1365"] = {
    "A": "<bdi>echo</bdi> يُظهر علامات غير مباشرة فقط (<bdi>RV strain</bdi>) ولا يثبت <bdi>PE</bdi>؛ يُختار بمريض غير مستقر لا يمكن نقله لـ<bdi>CT</bdi>.",
    "B": "<bdi>V/Q scan</bdi> يُستخدم عند منع صبغة <bdi>CT</bdi> (فشل كلوي، حساسية)، بالحمل، أو عند <bdi>CTPA</bdi> غير حاسم؛ لا ينطبق هنا.",
    "D": "<bdi>MRA</bdi> ليس فحصًا معياريًا أوليًا لـ<bdi>PE</bdi>؛ حساسيته وتوافره أقل من <bdi>CTPA</bdi>.",
}
HIGHLIGHT_TERMS["AS-1365"] = ["shortness of breath and chest pain for one day", "D dimer 800 high", "right deviation with right bundle branch block"]

EXPLANATIONS["AS-1368"] = {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "مريض عنده <bdi>AF</bdi> جديدة مع <bdi>renal impairment stage 3</bdi>، والسؤال عن أفضل مضاد تجلط يُضاف.",
    "clues": [
        ("renal impairment 3", "يحدد اختيار <bdi>DOAC</bdi> الأقل اعتمادًا على الكلى"),
        ("AF", "يحتاج مضاد تجلط حسب <bdi>CHA2DS2-VA</bdi>"),
    ],
    "why_correct": [
        "بوجود <bdi>HTN</bdi> و<bdi>DM</bdi> هو بالفعل عنده نقطتان على الأقل بـ<bdi>CHA2DS2-VA</bdi>، فمضاد التجلط مطلوب، و<bdi>DOACs</bdi> خط أول.",
        "العلامة الحاسمة هي 'renal impairment 3': من بين <bdi>DOACs</bdi>، <bdi>apixaban</bdi> أقلها اعتمادًا على التصفية الكلوية وله أفضل بيانات أمان بـ<bdi>CKD</bdi>.",
    ],
    "when_changes": [
        "لو كان المريض يعاني من <bdi>mechanical valve</bdi> أو <bdi>moderate/severe mitral stenosis</bdi>، الجواب يصير <bdi>warfarin</bdi>.",
    ],
    "rule": "الكلى بالسؤال = تجنّب <bdi>dabigatran</bdi>، واختر <bdi>apixaban</bdi>.",
    "comparison": {
        "headers": ["الدواء", "الاعتماد الكلوي"],
        "rows": [
            ["<bdi>Apixaban</bdi>", "أقل اعتمادًا"],
            ["<bdi>Rivaroxaban</bdi>", "متوسط"],
            ["<bdi>Edoxaban</bdi>", "متوسط-عالي"],
            ["<bdi>Dabigatran</bdi>", "أعلى اعتمادًا"],
        ],
    },
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1368"] = {
    "B": "<bdi>rivaroxaban</bdi> خيار معقول لكن اعتماده الكلوي أعلى من <bdi>apixaban</bdi> ويحتاج تعديل جرعة بـ<bdi>CKD</bdi> متوسط.",
    "C": "<bdi>dabigatran</bdi> يُطرح كليًا بشكل كبير فيتراكم ويزيد خطر النزيف بـ<bdi>CKD</bdi>.",
    "D": "<bdi>edoxaban</bdi> يحتاج تعديل جرعة كلوي وفعاليته تقل بتصفية كرياتينين مرتفعة جدًا؛ ليس المفضل عندما تكون الكلى هي القضية.",
}
HIGHLIGHT_TERMS["AS-1368"] = ["renal impairment 3", "AF"]

EXPLANATIONS["AS-1370"] = {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "رجل بعمر 45 مع <bdi>HTN</bdi> غير مضبوط ويدخن مع <bdi>LDL</bdi> مرتفع، والسؤال عن أفضل وقاية.",
    "clues": [
        ("HTN", "<bdi>known hypertension</bdi>"),
        ("20 pack smoker", "عامل خطورة قلبي وعائي إضافي"),
        ("BP 150/95", "ضغط غير مضبوط"),
        ("LDL 4.5", "ارتفاع واضح بالكوليسترول الضار"),
    ],
    "why_correct": [
        "هو 'known case' من <bdi>HTN</bdi> وضغطه لازال <bdi>150/95</bdi>، ويدخن، وعنده <bdi>LDL 4.5 mmol/L</bdi> مرتفع، فخطره القلبي الوعائي مرتفع ويحتاج علاج دوائي للعاملين.",
        "<bdi>antihypertensive therapy</bdi> مع <bdi>statin</bdi> هي الخطوة الوقائية التي تخفض خطره، بالإضافة لإيقاف التدخين ونصائح نمط الحياة.",
    ],
    "when_changes": [
        "لو كان الضغط مكتشفًا حديثًا بدرجة خفيفة بدون عوامل خطورة أخرى، الجواب يصير <bdi>lifestyle modification</bdi> أولًا.",
    ],
    "rule": "'known case' من <bdi>HTN</bdi> مع ضغط لازال مرتفع ليس سؤال نمط حياة فقط.",
    "comparison": None,
    "labs": [
        ["Blood pressure", "150/95 mmHg", "< 140/90 mmHg"],
        ["LDL", "4.5 mmol/L", "< 3.0 mmol/L (general target)"],
        ["HDL", "1.1 mmol/L", "> 1.0 mmol/L (male), > 1.2 (female)"],
        ["Total cholesterol", "6.5 mmol/L", "< 5.2 mmol/L"],
        ["Triglycerides", "2.1 mmol/L", "< 1.7 mmol/L"],
    ],
    "guideline_note": None,
}
WHY_WRONG["AS-1370"] = {
    "A": "<bdi>stress test</bdi> ليس فحص فرز بمريض بلا أعراض؛ يُستخدم للتحقيق بألم صدر مع الجهد أو أعراض نقص تروية.",
    "D": "<bdi>lifestyle modification</bdi> لوحده يناسب ضغط خفيف مكتشف حديثًا بمريض منخفض الخطورة بدون عوامل خطورة أخرى؛ هنا هو مريض معروف بـ<bdi>HTN</bdi> غير مضبوط، مدخن، و<bdi>LDL</bdi> مرتفع، فتأخير الدواء غير كافٍ.",
}
HIGHLIGHT_TERMS["AS-1370"] = ["HTN", "20 pack smoker", "BP 150/95", "LDL 4.5"]

EXPLANATIONS["AS-1374"] = {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "مريضة <bdi>asthma</bdi> على <bdi>ICS</bdi> منتظم لكن مع نوبات متكررة ودخول للمستشفى، والسؤال عن الخطوة التالية بالعلاج.",
    "clues": [
        ("salbutamol inhaler 100 mcg prn", "<bdi>reliever</bdi> حسب الحاجة"),
        ("beclometasone dipropionate inhaler 400 mcg bd", "<bdi>regular ICS</bdi>"),
        ("frequent exacerbations", "دليل على عدم السيطرة على المرض"),
    ],
    "why_correct": [
        "هي بالفعل على <bdi>reliever</bdi> مع <bdi>ICS</bdi> منتظم (<bdi>beclometasone 400 mcg bd</bdi>)، ومع ذلك عندها نوبات متكررة ودخول للمستشفى 3 مرات بـ6 أشهر.",
        "<bdi>asthma</bdi> غير مضبوط على <bdi>ICS</bdi> يحتاج تصعيد العلاج، والخطوة التالية هي إضافة <bdi>LABA</bdi> مثل <bdi>salmeterol</bdi> للـ<bdi>ICS</bdi> (الأفضل كبخاخ مشترك)، بعد التأكد من الالتزام وتقنية الاستخدام.",
    ],
    "when_changes": [
        "لو كانت لا زالت غير مضبوطة بعد إضافة <bdi>LABA</bdi>، الجواب يصير زيادة جرعة <bdi>ICS</bdi> أو إضافة <bdi>LAMA</bdi> أو مضاد <bdi>leukotriene</bdi>.",
    ],
    "rule": "عدم ضبط المرض على <bdi>ICS</bdi> = أضف <bdi>LABA</bdi> قبل أي شيء آخر.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1374"] = {
    "A": "تبديل <bdi>beclometasone</bdi> لـ<bdi>fluticasone</bdi> يبدّل نوع <bdi>ICS</bdi> فقط وليس تصعيدًا؛ يفيد فقط عند عدم تحمل أو مشكلة بالجهاز.",
    "B": "استخدام <bdi>salbutamol</bdi> بشكل منتظم لا يعالج الالتهاب، وزيادة استخدام <bdi>reliever</bdi> نفسها علامة على ضعف الضبط لا علاج له.",
    "D": "<bdi>tiotropium (LAMA)</bdi> إضافة تُستخدم عندما لا يُضبط المرض على <bdi>ICS + LABA</bdi>، مو أول إضافة بعد <bdi>ICS</bdi> لوحده.",
}
HIGHLIGHT_TERMS["AS-1374"] = ["salbutamol inhaler 100 mcg prn", "beclometasone dipropionate inhaler 400 mcg bd", "frequent exacerbations"]

EXPLANATIONS["AS-1381"] = {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "مريض <bdi>COPD exacerbation</bdi> مع فشل تنفسي شديد مهدد للحياة بعد العلاج الدوائي الكامل، والسؤال عن الخطوة التالية.",
    "clues": [
        ("COPD exacerbation", "نوبة حادة"),
        ("O2 70%", "نقص أكسجين شديد"),
        ("CO2 high 9", "<bdi>hypercapnia</bdi> شديد"),
        ("pH 7.2", "<bdi>severe acidosis</bdi>"),
    ],
    "why_correct": [
        "رغم العلاج بـ<bdi>steroid</bdi> وموسعات الشعب، عنده فشل تنفسي مهدد للحياة: <bdi>O2 70%</bdi>, <bdi>CO2 9</bdi>, <bdi>pH 7.2</bdi>.",
        "القاعدة بهذه الامتحانات: بمريض <bdi>COPD</bdi> إذا كان <bdi>pH</bdi> أقل من 7.25 يجب <bdi>intubation</bdi>، والخيار الآخر هنا (<bdi>negative pressure</bdi>) ليس علاجًا معياريًا، فالجواب هو <bdi>mechanical intubation</bdi>.",
    ],
    "when_changes": [
        "لو كان <bdi>pH</bdi> أعلى من 7.25 والمريض واعٍ، الجواب يصير <bdi>positive pressure NIV</bdi> (انظر AS-1381B).",
    ],
    "rule": "بـ<bdi>COPD</bdi>: <bdi>pH</bdi> أقل من 7.25 = <bdi>intubate</bdi>؛ أعلى من 7.25 = <bdi>NIV</bdi>.",
    "comparison": None,
    "labs": [
        ["O2 saturation", "70%", "88-92% target in COPD"],
        ["CO2 (PaCO2)", "9 kPa (high)", "4.7-6.0 kPa"],
        ["pH", "7.2", "7.35-7.45"],
    ],
    "guideline_note": None,
}
WHY_WRONG["AS-1381"] = {
    "B": "<bdi>negative pressure ventilation</bdi> (مثل <bdi>iron lung</bdi>) لا تُستخدم بنوبات <bdi>COPD</bdi> الحادة؛ الخيار الصحيح بين التنفس غير الباضع هو <bdi>positive pressure (BiPAP)</bdi> بمريض واعٍ مع حموضة أقل شدة.",
}
HIGHLIGHT_TERMS["AS-1381"] = ["COPD exacerbation", "O2 70%", "CO2 high 9", "pH 7.2"]

EXPLANATIONS["AS-1381B"] = {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نفس سيناريو <bdi>COPD exacerbation</bdi> لكن مع <bdi>pH 7.27</bdi> وبدون أي مؤشر لـ<bdi>intubation</bdi>.",
    "clues": [
        ("acute exacerbation COPD", "فشل تنفسي حاد"),
        ("no O2 given", "لم يُعطَ أكسجين بعد"),
        ("not have confusion or any CNS symptoms or absent gag or any indication for intubation", "لا توجد مؤشرات لـ<bdi>intubation</bdi>"),
        ("pH 7.24", "<bdi>acidosis</bdi> صُحّح لـ7.27"),
    ],
    "why_correct": [
        "عنده <bdi>hypercapnic respiratory acidosis</bdi> (<bdi>pH 7.27</bdi>, <bdi>CO2</bdi> مرتفع) رغم العلاج الدوائي الكامل، لكن 'لا يوجد تشوش أو أعراض عصبية أو غياب منعكس البلع'.",
        "مريض واعٍ مع منعكسات مجرى هوائي سليمة وحموضة أعلى من حد <bdi>intubation</bdi> يستوفي معايير <bdi>non-invasive positive pressure ventilation (BiPAP)</bdi> مع أكسجين مضبوط.",
    ],
    "when_changes": [
        "لو كان <bdi>pH</bdi> أقل من 7.25 أو ظهر تشوش وعي أو فشل <bdi>NIV</bdi>، الجواب يصير <bdi>intubation</bdi>.",
    ],
    "rule": "مريض <bdi>COPD</bdi> واعٍ + حموضة تنفسية رغم العلاج = <bdi>NIV</bdi>.",
    "comparison": None,
    "labs": [
        ["pH", "7.27 (corrected from 7.24)", "7.35-7.45"],
        ["O2 saturation", "70%", "88-92% target in COPD"],
    ],
    "guideline_note": None,
}
WHY_WRONG["AS-1381B"] = {
    "A": "<bdi>high flow nasal cannula</bdi> يعالج نقص الأكسجين بشكل أساسي ولا يصحح الحموضة التنفسية الفرط-ثانية بشكل موثوق؛ يُستخدم إذا لم يتحمل المريض <bdi>NIV</bdi>.",
    "C": "<bdi>intubation</bdi> يحتاج سببًا: تشوش وعي، خطر استنشاق، فشل <bdi>NIV</bdi>، أو حموضة شديدة (<bdi>pH</bdi> أقل من 7.25 بهذه الامتحانات)؛ السؤال يستثني كل هذه صراحة.",
}
HIGHLIGHT_TERMS["AS-1381B"] = ["acute exacerbation COPD", "no O2 given", "not have confusion or any CNS symptoms or absent gag or any indication for intubation", "pH 7.24"]

EXPLANATIONS["AS-1383"] = {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "شابة مع صورة <bdi>meningococcal meningitis</bdi> وطفح <bdi>purpuric</bdi>، والسؤال عن الفحص المثبت للتشخيص.",
    "clues": [
        ("headache, fever, photosensitivity", "صورة <bdi>meningitis</bdi>"),
        ("neck rigidity", "علامة سحائية"),
        ("purpuric skin rash over her extremities", "مميز لـ<bdi>meningococcemia</bdi>"),
    ],
    "why_correct": [
        "الصداع والحمى والحساسية للضوء والخمول و<bdi>neck rigidity</bdi> مع طفح <bdi>purpuric</bdi> تشير لـ<bdi>meningococcal meningitis</bdi>.",
        "لا توجد 'علامات عصبية بؤرية'، والخمول وحده بدون <bdi>papilledema</bdi> أو انخفاض شديد بمستوى الوعي لا يحتاج <bdi>CT</bdi> أولًا، فـ<bdi>lumbar puncture</bdi> هو الفحص الذي يُثبت التشخيص عبر خلايا <bdi>CSF</bdi> والجلوكوز والبروتين و<bdi>Gram stain</bdi> والزرع.",
        "<bdi>blood cultures</bdi> والمضادات التجريبية تُعطى دون انتظار <bdi>LP</bdi>.",
    ],
    "when_changes": [
        "لو ظهرت علامة عصبية بؤرية أو <bdi>papilledema</bdi> أو نقص وعي شديد، الجواب يصير عمل <bdi>CT</bdi> قبل <bdi>LP</bdi>.",
    ],
    "rule": "اشتباه <bdi>bacterial meningitis</bdi>: خذ <bdi>blood cultures</bdi> ثم <bdi>LP</bdi>، ولا تؤخر المضادات.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1383"] = {
    "A": "<bdi>skin biopsy</bdi> للطفح قد يُظهر الجراثيم لكنه ليس الفحص المعياري لإثبات <bdi>meningitis</bdi>.",
    "B": "<bdi>blood culture</bdi> يجب أن يُسحب (قبل المضادات) لكنه يشخص <bdi>bacteremia</bdi> لا العدوى السحائية؛ <bdi>CSF</bdi> هو ما يؤكد <bdi>meningitis</bdi>.",
    "D": "<bdi>meningococcal serology</bdi> بطيء ولا دور له بالتشخيص الحاد.",
}
HIGHLIGHT_TERMS["AS-1383"] = ["headache, fever, photosensitivity", "neck rigidity", "purpuric skin rash over her extremities"]

EXPLANATIONS["AS-1384"] = {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "شاب عمره 30 مع عسر هضم بدون علامات خطر، والسؤال عن الخطوة التالية.",
    "clues": [
        ("30 years old", "عمر صغير"),
        ("epigastric pain worse after meal", "صورة عسر هضم"),
        ("No family history", "يستثني الحاجة لـ<bdi>endoscopy</bdi> المباشر"),
    ],
    "why_correct": [
        "شاب بعمر 30 مع عسر هضم بدون تاريخ عائلي لسرطان المعدة أو المريء وبدون علامات خطر (لا نزيف، لا نقص وزن، لا فقر دم، لا عسر بلع أو قيء) يُعالج بمبدأ <bdi>test and treat</bdi>.",
        "الفحص غير الباضع لـ<bdi>H. pylori</bdi> (<bdi>urea breath test</bdi> أو <bdi>stool antigen</bdi>) هو الخطوة التالية؛ <bdi>BMI 35</bdi> مجرد عامل مشوّش لا علامة خطر.",
    ],
    "when_changes": [
        "لو أُضيف فقر دم أو نقص وزن أو عسر بلع، الجواب يصير <bdi>endoscopy</bdi>.",
    ],
    "rule": "شاب مع عسر هضم بدون علامات خطر = <bdi>test and treat H. pylori</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1384"] = {
    "B": "<bdi>endoscopy</bdi> للعلامات التحذيرية، كبر السن، تاريخ عائلي لسرطان الجهاز الهضمي العلوي، أو فشل العلاج التجريبي.",
    "C": "<bdi>CT abdomen</bdi> لا يُظهر المرض بالغشاء المخاطي؛ يُستخدم عند الاشتباه بمضاعفات.",
    "D": "<bdi>barium studies</bdi> تُستخدم فقط عند تعذر أو منع <bdi>endoscopy</bdi>؛ ليست جزءًا من الفحص الأولي لعسر الهضم.",
}
HIGHLIGHT_TERMS["AS-1384"] = ["30 years old", "epigastric pain worse after meal", "No family history"]

EXPLANATIONS["AS-1387"] = {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "نفخة انبساطية بقاعدة القلب تزيد بالانحناء للأمام، والسؤال عن التشخيص الأرجح.",
    "clues": [
        ("diastolic murmur heard at the base of the heart", "نفخة انبساطية = <bdi>ARMS</bdi>"),
        ("increased when the patient leaned forward in full expiration", "علامة كلاسيكية لـ<bdi>aortic regurgitation</bdi>"),
    ],
    "why_correct": [
        "أول خطوة بتحليل أي نفخة هي توقيتها: هذه نفخة <bdi>diastolic</bdi>.",
        "نفخة انبساطية بقاعدة القلب تزيد بالانحناء للأمام مع الزفير الكامل هي النفخة الانبساطية المبكرة الكلاسيكية لـ<bdi>aortic regurgitation</bdi>، وهي الخيار الانبساطي الوحيد بين الاختيارات.",
    ],
    "when_changes": [
        "لو كانت النفخة بالقاعدة وتزيد بالشهيق، الجواب يصير <bdi>pulmonary regurgitation</bdi>.",
    ],
    "rule": "قرر <bdi>systolic</bdi> أو <bdi>diastolic</bdi> أولًا؛ النفخة الانبساطية (<bdi>ARMS</bdi>) تشمل <bdi>AR</bdi> و<bdi>MS</bdi> فقط.",
    "comparison": {
        "headers": ["النفخة", "التوقيت والموقع"],
        "rows": [
            ["<bdi>Aortic regurgitation</bdi>", "انبساطية مبكرة، قاعدة/حافة عظم القص اليسرى، تزيد بالانحناء بالزفير"],
            ["<bdi>Aortic stenosis</bdi>", "انقباضية طردية بالقاعدة، تمتد للسباتي"],
            ["<bdi>Mitral regurgitation</bdi>", "انقباضية مستمرة بالقمة، تمتد للإبط"],
            ["<bdi>Tricuspid regurgitation</bdi>", "انقباضية مستمرة بحافة عظم القص اليسرى السفلى، تزيد بالشهيق"],
        ],
    },
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1387"] = {
    "A": "<bdi>aortic stenosis</bdi> نفخة انقباضية طردية بحافة عظم القص اليمنى العلوية تمتد للسباتي.",
    "B": "<bdi>mitral regurgitation</bdi> نفخة انقباضية مستمرة بالقمة تمتد للإبط.",
    "D": "<bdi>tricuspid regurgitation</bdi> نفخة انقباضية مستمرة بحافة عظم القص اليسرى السفلى تزيد بالشهيق.",
}
HIGHLIGHT_TERMS["AS-1387"] = ["diastolic murmur heard at the base of the heart", "increased when the patient leaned forward in full expiration"]

EXPLANATIONS["AS-1388"] = {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "مريض بـ<bdi>ICU</bdi> نتائج الكبد طبيعية ثم أصبحت شاذة بعد نوبة <bdi>hypotension</bdi>، والسؤال عن التشخيص الأرجح.",
    "clues": [
        ("hypotension treated with hydration and inotropes", "نوبة نقص تروية شديدة"),
        ("repeated one is abnormal", "ارتفاع حاد بوظائف الكبد بعد النوبة"),
        ("Unremarkable", "<bdi>ultrasound</bdi> طبيعي يستثني انسداد قناة مرارية"),
    ],
    "why_correct": [
        "كانت وظائف الكبد طبيعية بالقبول، ثم حدثت نوبة <bdi>hypotension</bdi> احتاجت <bdi>inotropes</bdi> باليوم الثالث، وأصبحت وظائف الكبد شاذة مع <bdi>ultrasound</bdi> طبيعي.",
        "نقص تروية الكبد بمريض عنده <bdi>ischemic heart disease</bdi> يسبب <bdi>ischemic (shock) liver</bdi>: ارتفاع حاد وكبير بـ<bdi>AST</bdi> و<bdi>ALT</bdi> (غالبًا فوق 1000) بعد نوبة نقص الضغط بوقت قصير، وينخفض بسرعة بعد استعادة التروية.",
    ],
    "when_changes": [
        "لو كان الارتفاع تدريجيًا مع ارتفاع أساسي بالبيليروبين والـ<bdi>ALP</bdi> بدون نوبة حادة، الجواب يصير <bdi>ICU-related jaundice</bdi>.",
    ],
    "rule": "وظائف طبيعية ثم <bdi>hypotension</bdi> ثم ارتفاع حاد جدًا بـ<bdi>AST/ALT</bdi> = <bdi>ischemic hepatitis</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1388"] = {
    "B": "<bdi>ICU-related jaundice</bdi> (<bdi>cholestasis</bdi>) تعطي ارتفاع أساسي بالبيليروبين والـ<bdi>ALP</bdi> مع ارتفاع خفيف فقط بالـ<bdi>transaminases</bdi>، لا طفرة ضخمة بعد <bdi>hypotension</bdi> مباشرة.",
    "C": "<bdi>intravascular hemolysis</bdi> يرفع البيليروبين غير المباشر و<bdi>LDH</bdi> مع انخفاض <bdi>Hb</bdi>، لكن لا يسبب ارتفاعًا كبيرًا بـ<bdi>ALT</bdi>.",
    "D": "<bdi>acalculous cholecystitis</bdi> تحدث بمرضى العناية المركزة لكن تظهر حمى وألم بالربع العلوي الأيمن ومرارة متوسعة بجدار سميك؛ <bdi>ultrasound</bdi> هنا طبيعي.",
}
HIGHLIGHT_TERMS["AS-1388"] = ["hypotension treated with hydration and inotropes", "repeated one is abnormal", "Unremarkable"]

EXPLANATIONS["AS-1389"] = {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سيدة مسنة مع <bdi>pneumonia</bdi> لا تتحسن بعد دورتين مضادات، والسؤال عن التشخيص الأرجح.",
    "clues": [
        ("4-month history of progressive shortness of breath, dry cough", "صورة تدريجية طويلة"),
        ("showed no improvement", "فشل العلاج بالمضادات"),
        ("persistent dense area of consolidation", "صلابة مستمرة بالتصوير"),
        ("Atypical cells", "علامة خبيثة بـ<bdi>BAL</bdi>"),
    ],
    "why_correct": [
        "سيدة بعمر 65 مع 4 أشهر من ضيق تنفس تدريجي وكحة جافة وتعب، وصلابة مستمرة لم تتحسن بعد دورتين مضادات، تعني <bdi>non-resolving pneumonia</bdi> اللي بالكبار بالسن تعني <bdi>malignancy</bdi> (أو <bdi>TB</bdi>) لين يثبت العكس.",
        "'<bdi>atypical cells</bdi>' بـ<bdi>BAL</bdi> تؤكد عملية خبيثة، فالتشخيص هو <bdi>bronchogenic cancer</bdi>.",
    ],
    "when_changes": [
        "لو كان هناك تعرق ليلي ونفث دم وكهف بالفص العلوي، الجواب يصير <bdi>TB</bdi>.",
    ],
    "rule": "<bdi>pneumonia</bdi> لا تُحل بمريض كبير بالسن = فكر بسرطان أو <bdi>TB</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1389"] = {
    "A": "<bdi>sarcoidosis</bdi> تعطي تضخم غدد لمفاوية نقيرية ثنائي وحبيبومات غير متجبنة، غالبًا بمرضى أصغر مع <bdi>erythema nodosum</bdi>، لا كتلة فصية واحدة مع خلايا شاذة.",
    "B": "<bdi>atypical pneumonia</bdi> تعطي ارتشاح خلالي منتشر وتستجيب للـ<bdi>macrolides</bdi>؛ لا تعطي خلايا خبيثة أو كثافة فصية مستمرة لأشهر.",
    "C": "<bdi>allergic pneumonitis</bdi> تحتاج تعرض لمستضد (طيور، عفن، زراعة) وتُظهر زيادة بالخلايا اللمفاوية بـ<bdi>BAL</bdi>، لا خلايا شاذة.",
}
HIGHLIGHT_TERMS["AS-1389"] = ["4-month history of progressive shortness of breath, dry cough", "showed no improvement", "persistent dense area of consolidation", "Atypical cells"]

EXPLANATIONS["AS-1390"] = {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "شاب مع <bdi>HIV</bdi> ودخول للعناية المركزة بصورة <bdi>ARDS</bdi>، والسؤال عن العضو المسبب.",
    "clues": [
        ("HIV", "خلفية نقص مناعة"),
        ("cyanosed", "نقص أكسجين شديد"),
        ("Signs of ARDS", "ارتشاح ثنائي منتشر"),
    ],
    "why_correct": [
        "العلامات الحاسمة: <bdi>HIV</bdi> مع مسار تدريجي (تحت حاد) من ضيق تنفس وكحة وحمى، نقص أكسجين واضح (<bdi>cyanosed</bdi>)، وصورة <bdi>ARDS</bdi> منتشرة.",
        "هذه الصورة الكلاسيكية لـ<bdi>Pneumocystis jirovecii pneumonia</bdi>، أشهر عدوى انتهازية عندما يكون <bdi>CD4</bdi> أقل من 200.",
        "<bdi>PCP</bdi> تعطي ارتشاح خلالي ثنائي (<bdi>ground glass</bdi>) مع نقص أكسجين لا يتناسب مع الفحص السريري، بدلًا من كثافة فصية واحدة.",
    ],
    "when_changes": [
        "لو كان <bdi>CD4</bdi> أعلى من 200 والمرض حاد مع كثافة فصية، الجواب يصير <bdi>Strep pneumoniae</bdi>.",
    ],
    "rule": "<bdi>HIV</bdi> + ضيق تنفس تدريجي + صورة ثنائية منتشرة = <bdi>PCP</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1390"] = {
    "A": "<bdi>Staph aureus</bdi> غالبًا يتبع <bdi>influenza</bdi> أو عدوى فيروسية سابقة (أو تعاطي أدوية وريدية) ويميل لـ<bdi>necrotizing</bdi> أو <bdi>cavitating</bdi>؛ لا دليل على مرض فيروسي سابق هنا.",
    "C": "<bdi>Pseudomonas</bdi> هو الجرثوم النمطي لـ<bdi>pneumonia</bdi> المكتسبة من المستشفى أو جهاز التنفس أو مرضى <bdi>CF</bdi>/<bdi>bronchiectasis</bdi>؛ هذا المريض أتى من المجتمع.",
    "D": "<bdi>Strep pneumoniae</bdi> أشهر جرثوم بـ<bdi>CAP</bdi> عمومًا وبـ<bdi>HIV</bdi> مع <bdi>CD4</bdi> أعلى من 200، لكنه يُقدّم بشكل حاد وكثافة فصية، مو صورة <bdi>ARDS</bdi> تدريجية منتشرة بـ<bdi>HIV</bdi> متقدم.",
}
HIGHLIGHT_TERMS["AS-1390"] = ["HIV", "cyanosed", "Signs of ARDS"]

EXPLANATIONS["AS-P349"] = {
    "correct_letter": "A",
    "self_judged": True,
    "idea": "مريض سليم بعمر 51 مع حمى وكحة وصلابة رئوية وارتفاع <bdi>neutrophils</bdi>، والسؤال عن الجرثوم المسبب الأرجح.",
    "clues": [
        ("cough, fever, and lung consolidation", "صورة <bdi>CAP</bdi> نمطية"),
        ("neutrophilia", "استجابة جرثومية نمطية"),
        ("No other medical comorbidities", "يستثني العوامل الخاصة بمريض معين"),
    ],
    "why_correct": [
        "بالغ سليم بدون أمراض مصاحبة مع كثافة فصية وحمى وارتفاع <bdi>neutrophils</bdi> هي الصورة الكلاسيكية لـ<bdi>community acquired pneumonia</bdi> بالغ سليم.",
        "<bdi>Streptococcus pneumoniae</bdi> هو أشهر جرثوم مسبب لـ<bdi>CAP</bdi> بالبالغ السليم بدون عوامل خاصة.",
    ],
    "when_changes": [
        "لو كان هناك تاريخ عدوى فيروسية سابقة (<bdi>influenza</bdi>) أو تعاطي أدوية وريدية، الجواب يصير <bdi>Staph aureus</bdi>.",
        "لو كان المريض بمستشفى أو مريض <bdi>CF</bdi>، الجواب يصير <bdi>Pseudomonas</bdi>.",
    ],
    "rule": "'بدون أمراض مصاحبة' مع كثافة فصية يوجّه بعيدًا عن الجراثيم الخاصة؛ الجواب الافتراضي هو <bdi>Strep pneumoniae</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": "المصدر لم يحدد جوابًا مؤكدًا لهذا السؤال؛ الاختيار هنا مبني على القاعدة السريرية المعتادة لأشهر سبب لـ<bdi>CAP</bdi> بمريض سليم.",
}
WHY_WRONG["AS-P349"] = {
    "B": "<bdi>Staph aureus</bdi> يرتبط بعدوى فيروسية سابقة (<bdi>influenza</bdi>) أو تعاطي أدوية وريدية؛ لا ذِكر لذلك هنا.",
    "C": "<bdi>E. coli</bdi> سبب نادر لـ<bdi>CAP</bdi> ويرتبط أكثر بعدوى بالمستشفى أو شفط محتوى معوي.",
    "D": "<bdi>Listeria</bdi> يُفكر فيها بكبار السن ضعيفي المناعة أو الحوامل أو حديثي الولادة، لا ببالغ سليم بدون أمراض مصاحبة.",
}
HIGHLIGHT_TERMS["AS-P349"] = ["cough, fever, and lung consolidation", "neutrophilia", "No other medical comorbidities"]

EXPLANATIONS["AS-1394"] = {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "السؤال يبي دواء ينتمي لفئة <bdi>angiotensin II receptor blocker</bdi> موصوفة لعلاج ضغط الدم.",
    "clues": [
        ("angiotensin receptor II blocker", "يحدد الفئة الدوائية مباشرة"),
    ],
    "why_correct": [
        "السؤال يذكر الفئة مباشرة: <bdi>angiotensin II receptor blocker</bdi>.",
        "<bdi>Irbesartan</bdi> يحمل اللاحقة '-<bdi>sartan</bdi>' التي تحدد فئة <bdi>ARBs</bdi>، فهو الدواء الموصوف.",
    ],
    "when_changes": [
        "لو كان السؤال يبي دواء من فئة <bdi>ACE inhibitor</bdi>، الجواب يصير <bdi>perindopril</bdi>.",
    ],
    "rule": "ميّز فئة الدواء من اللاحقة: '-<bdi>sartan</bdi>' = <bdi>ARB</bdi>؛ '-<bdi>pril</bdi>' = <bdi>ACE inhibitor</bdi>.",
    "comparison": {
        "headers": ["اللاحقة", "الفئة"],
        "rows": [
            ["-sartan", "<bdi>ARB</bdi>"],
            ["-pril", "<bdi>ACE inhibitor</bdi>"],
            ["-olol / -ilol", "<bdi>Beta blocker</bdi>"],
            ["-dipine", "<bdi>Dihydropyridine CCB</bdi>"],
        ],
    },
    "labs": None,
    "guideline_note": None,
}
WHY_WRONG["AS-1394"] = {
    "A": "<bdi>carvedilol</bdi> هو <bdi>beta blocker</bdi> (مع تأثير <bdi>alpha blocking</bdi>)، مفيد بـ<bdi>heart failure</bdi>، وليس <bdi>ARB</bdi>.",
    "C": "<bdi>perindopril</bdi> هو <bdi>ACE inhibitor</bdi> ('-<bdi>pril</bdi>')، يعمل على نفس المنظومة لكن يمنع تكوّن <bdi>angiotensin II</bdi> لا مستقبله.",
    "D": "<bdi>amiodarone</bdi> مضاد اضطراب نظم من فئة III، وليس خافضًا لضغط الدم أو <bdi>ARB</bdi>.",
}
HIGHLIGHT_TERMS["AS-1394"] = ["angiotensin receptor II blocker"]

# -*- coding: utf-8 -*-
# Explanations for questions 001-013 (topic: Geriatric Medicine)

TOPIC = "Geriatric Medicine"

EXPLANATIONS = {
1: {
    "idea": "الـ<bdi>patient</bdi> عنده <bdi>hypercalcemia</bdi> <bdi>severe</bdi> وعرضية (لخبطة ذهنية)، ومعه <bdi>signs</bdi> جفاف واضحة، فالسؤال يبي أول <bdi>step</bdi> <bdi>treatment</bdi> قبل أي شي ثاني.",
    "clues": [
        ("acute confusional state", "لخبطة ذهنية <bdi>acute</bdi>، من <bdi>symptoms</bdi> ارتفاع الكالسيوم"),
        ("postural hypotension", "هبوط ضغط عند الوقوف، <bdi>sign</bdi> جفاف"),
        ("dry mucus membranes", "جفاف الأغشية المخاطية، <bdi>sign</bdi> جفاف"),
        ("Calcium 3.41 (2.15-2.62) mmol/L", "كالسيوم <bdi>elevated</bdi> جدًا، يعادل تقريبًا 13.6 مقابل الـ<bdi>normal</bdi> 8.6-10.5 mg/dL"),
    ],
    "why_correct": [
        "أول <bdi>step</bdi> في أي <bdi>hypercalcemia</bdi> عرضية هي تعويض الجفاف بـ <bdi>IV normal saline</bdi>، لأن الجفاف نفسه يرفع الكالسيوم أكثر (يقلل إفرازه بالكلى).",
        "الترطيب يرجع تروية الكلى ويخلّيها تطرح كالسيوم أكثر، وهذي أسرع <bdi>step</bdi> تنعمل فورًا في الطوارئ.",
        "باقي الخيارات علاجات ثانية بس مو الـ<bdi>step</bdi> الأولى: <bdi>pamidronate</bdi> يحتاج وقت (أيام) لين يبين مفعوله، والـ <bdi>steroids</bdi> تفيد بحالات معينة بس، والـ <bdi>furosemide</bdi> ممكن يزيد الجفاف لو الـ<bdi>patient</bdi> ناقص سوائل.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> عنده <bdi>congestion</bdi> سوائل أو قصور قلب مع الكالسيوم العالي، يصير <bdi>furosemide</bdi> مفيد بعد الترطيب، مو بديل عنه.",
        "لو الـ<bdi>cause</bdi> <bdi>sarcoidosis</bdi> أو زيادة فيتامين D، الـ<bdi>treatment</bdi> النوعي يصير <bdi>steroids</bdi>.",
        "لو الكالسيوم من ورم خبيث ومحتاج تحكم طويل المدى، يضاف <bdi>bisphosphonate</bdi> بعد ما يترطب الـ<bdi>patient</bdi>، مو قبل.",
    ],
    "rule": "في أي <bdi>hypercalcemia</bdi> <bdi>severe</bdi> وعرضية، الترطيب بـ <bdi>IV saline</bdi> أول <bdi>step</bdi> دايمًا قبل أي دواء ثاني.",
    "comparison": {
        "headers": ["الـ<bdi>treatment</bdi>", "دوره", "متى يستخدم"],
        "rows": [
            ["<bdi>IV normal saline</bdi>", "ترطيب وتحسين طرح الكالسيوم", "الـ<bdi>step</bdi> الأولى دايمًا"],
            ["<bdi>Pamidronate</bdi>", "تحكم طويل المدى بالكالسيوم", "بعد الترطيب، خصوصًا بالسرطان"],
            ["<bdi>Prednisolone</bdi>", "<bdi>treatment</bdi> نوعي", "<bdi>cause</bdi> حبيبي أو فيتامين D زايد"],
            ["<bdi>Furosemide</bdi>", "طرح سوائل زايدة", "لو صار <bdi>congestion</bdi> بعد الترطيب بس"],
        ],
    },
    "guideline_note": None,
},
2: {
    "idea": "الـ<bdi>patient</bdi> بصدمة (هبوط ضغط <bdi>severe</bdi> وتسرع قلب وأطراف باردة) والـ<bdi>cause</bdi> الأرجح فقدان سوائل من الإسهال وقلة الأكل، فالسؤال يبي أول <bdi>step</bdi> إنعاش.",
    "clues": [
        ("BP 83/45", "هبوط ضغط <bdi>severe</bdi>، يدل على صدمة"),
        ("cold extremities, feeble pulses", "ضعف تروية طرفية، من <bdi>signs</bdi> الصدمة"),
        ("JVP not visible", "الضغط الوريدي <bdi>low</bdi>، يدل على نقص سوائل مو <bdi>congestion</bdi>"),
        ("lungs clear", "ما فيه <bdi>congestion</bdi> رئوي يمنع إعطاء السوائل"),
        ("diarrhea, poor oral intake", "<bdi>cause</bdi> فقدان السوائل"),
    ],
    "why_correct": [
        "الصورة كلها صدمة نقص حجم (هبوط ضغط، تسرع قلب، أطراف باردة، JVP <bdi>low</bdi>)، والـ<bdi>step</bdi> الأولى بأي صدمة نقص حجم هي إعطاء سوائل وريدية بسرعة.",
        "الرئتين نظيفة والـ JVP <bdi>low</bdi>، يعني ما فيه <bdi>congestion</bdi> يمنعنا من إعطاء السوائل، فالخيار الآمن والصحيح هو الـ <bdi>IV saline boluses</bdi>.",
        "الـ <bdi>beta blockers</bdi> يزيدون الهبوط سوء، والـ <bdi>dopamine</bdi> يستخدم لو ما تحسن الضغط بعد سوائل كافية، مو ك<bdi>step</bdi> أولى.",
    ],
    "when_changes": [
        "لو كان الـ JVP <bdi>elevated</bdi> مع <bdi>crepitations</bdi> بالرئتين (يدل على قصور قلب)، الجواب يتغير ل<bdi>treatment</bdi> <bdi>heart failure</bdi> مو سوائل زيادة.",
        "لو ما تحسن الضغط بعد سوائل كافية، الـ<bdi>step</bdi> التالية تصير موسّعات وريدية مثل <bdi>dopamine</bdi> أو <bdi>norepinephrine</bdi>.",
    ],
    "rule": "أي صدمة بدون <bdi>signs</bdi> <bdi>congestion</bdi>، أول <bdi>step</bdi> سوائل وريدية بسرعة قبل أي دواء ثاني.",
    "comparison": None,
    "guideline_note": None,
},
3: {
    "idea": "<bdi>patient</bdi> كبيرة بالسن عندها قصور قلب، صارت تاخذ سوائل وريدية بعد عملية، وبعد يومين طلع عندها <bdi>congestion</bdi> رئوي. السؤال يبي أفضل طريقة تمنع هالمضاعفة من الأساس.",
    "clues": [
        ("history of heart failure", "<bdi>factor</bdi> <bdi>risk</bdi> لاحتباس السوائل"),
        ("kept on normal saline", "سوائل وريدية مستمرة بدون مراجعة قد تسبب الحمل الزائد"),
        ("dropping oxygen, crepitations", "<bdi>signs</bdi> <bdi>congestion</bdi> رئوي حصل فعلًا"),
    ],
    "why_correct": [
        "المشكلة صارت لأن السوائل الوريدية استمرت بدون إعادة <bdi>assessment</bdi> ل<bdi>case</bdi> الـ<bdi>patient</bdi> يوميًا رغم إنها قلبية.",
        "أفضل <bdi>procedure</bdi> وقائي هو <bdi>daily reassessment of fluid status</bdi>، يعني يعدّلون كمية السوائل حسب حالتها كل يوم بدل ما تكون ثابتة.",
        "باقي الخيارات <bdi>treatment</bdi> لل<bdi>complication</bdi> بعد ما تصير (أكسجين، <bdi>furosemide</bdi>، استشارة)، مو منع لها من البداية.",
    ],
    "when_changes": [
        "لو السؤال يبي <bdi>treatment</bdi> الـ<bdi>congestion</bdi> اللي صار فعلًا وليس الوقاية، الجواب يصير <bdi>furosemide</bdi> أو الأكسجين حسب شدة الـ<bdi>case</bdi>.",
        "لو ما فيه تاريخ قصور قلب من الأصل، <bdi>risk</bdi> الحمل الزائد أقل وما يحتاج نفس درجة الحذر.",
    ],
    "rule": "بمرضى <bdi>heart failure</bdi>، السوائل الوريدية تحتاج مراجعة يومية دايمًا، مو أوامر ثابتة لمدة طويلة.",
    "comparison": None,
    "guideline_note": None,
},
4: {
    "idea": "رجل كبير بالسن عنده ألم بطن مغصي مع تغيّر بالإخراج: كان إمساك وحبس براز، وبعدين صار إسهال مائي. هذي صورة كلاسيكية لإمساك <bdi>severe</bdi> مع إسهال فيضاني (تسريب حول الكتلة البرازية).",
    "clues": [
        ("hard stools once or twice a week", "إمساك <bdi>chronic</bdi> قبل الـ<bdi>symptoms</bdi> الحالية"),
        ("watery stools several times a day", "إسهال فيضاني حول الكتلة البرازية المحبوسة"),
        ("fullness in left lower quadrant", "كتلة براز محسوسة بمكان القولون النازل"),
        ("no fever, no guarding", "يبعد الالتهاب الـ<bdi>acute</bdi> مثل التهاب القولون"),
    ],
    "why_correct": [
        "تاريخ الإمساك الـ<bdi>chronic</bdi> مع كتلة محسوسة بالحفرة اليسرى وإسهال مائي فجأة يطابق تمامًا صورة الإمساك مع تسريب حول الكتلة البرازية.",
        "ما فيه حمى ولا <bdi>signs</bdi> التهاب <bdi>acute</bdi> (guarding)، وهذا يبعد التهاب القولون الـ<bdi>acute</bdi>.",
        "الفحص الـ<bdi>normal</bdi> للبول يبعد <bdi>cause</bdi> بولي مثل حصوة الحالب أو التهاب المسالك.",
    ],
    "when_changes": [
        "لو فيه حمى وارتفاع كريات الدم البيضاء مع الألم، الجواب يميل لالتهاب القولون الرتوجي (<bdi>diverticulitis</bdi>) بدل الإمساك.",
        "لو الألم انتقل لجانب واحد مع دم بالبول، يصير الـ<bdi>diagnosis</bdi> حصوة حالب (<bdi>ureteric stone</bdi>).",
    ],
    "rule": "إمساك <bdi>chronic</bdi> يتبعه إسهال مائي مفاجئ بكبار السن غالبًا يكون إسهال فيضاني حول كتلة براز محبوسة، مو التهاب حقيقي.",
    "comparison": None,
    "guideline_note": None,
},
5: {
    "idea": "السؤال يبي أفضل نوع تمرين يحسّن الوظيفة الجسدية (القدرة على الحركة والاعتماد على النفس) لامرأة كبيرة بالسن، مو بس اللياقة القلبية.",
    "clues": [
        ("improve the function", "يقصد قوة العضلات والقدرة الوظيفية اليومية، مو التحمل القلبي بس"),
    ],
    "why_correct": [
        "تمارين المقاومة (<bdi>resistance training</bdi>) هي اللي تبني كتلة العضلات وتقوّي القوة العضلية، وهذا اللي يحسّن الوظيفة (الوقوف، المشي، صعود الدرج) عند كبار السن.",
        "المشي والسباحة والدراجة الثابتة تمارين هوائية تحسّن اللياقة القلبية بس أقل تأثير على قوة العضلات مقارنة بتمارين المقاومة.",
        "بكبار السن، ضعف العضلات (<bdi>sarcopenia</bdi>) هو الـ<bdi>cause</bdi> الرئيسي لضعف الوظيفة، فتمارين المقاومة تستهدف الـ<bdi>cause</bdi> مباشرة.",
    ],
    "when_changes": [
        "لو السؤال يبي تحسين اللياقة القلبية التنفسية بدل الوظيفة العضلية، الجواب يصير مشي أو سباحة.",
        "لو الـ<bdi>patient</bdi> عندها مشاكل مفاصل تمنع تمارين المقاومة، يفضّل تمارين بأثر أقل مثل السباحة.",
    ],
    "rule": "تمارين المقاومة هي الأفضل لتحسين القوة والوظيفة الجسدية عند كبار السن.",
    "comparison": {
        "headers": ["نوع التمرين", "الفايدة الأساسية"],
        "rows": [
            ["<bdi>Resistance training</bdi>", "قوة عضلية ووظيفة يومية"],
            ["<bdi>Walking / Cycling</bdi>", "لياقة قلبية تنفسية"],
            ["<bdi>Swimming</bdi>", "لياقة قلبية بأثر أقل على المفاصل"],
        ],
    },
    "guideline_note": None,
},
6: {
    "idea": "رجل كبير بالسن يصعب عليه ينهض من الكرسي (ضعف عضلي قريب من الجذع)، والسؤال يبي أكثر نوع إصابة متوقع له ب<bdi>cause</bdi> هالضعف.",
    "clues": [
        ("difficulty getting up from the chair", "ضعف عضلي قريب (proximal)، <bdi>factor</bdi> <bdi>risk</bdi> رئيسي للسقوط"),
        ("72-year-old", "عمر متقدم، <bdi>factor</bdi> <bdi>risk</bdi> إضافي للسقوط"),
    ],
    "why_correct": [
        "ضعف العضلات القريبة وصعوبة النهوض من الكرسي من أهم <bdi>factors</bdi> <bdi>risk</bdi> السقوط عند كبار السن.",
        "السقوط (<bdi>falls</bdi>) هو أشيع نوع إصابة تصيب كبار السن أصلًا، ويزيد خطره أكثر مع ضعف عضلي زي اللي عند الـ<bdi>patient</bdi>.",
        "باقي الخيارات (حوادث سيارات، حريق، طلق ناري) ما لها علاقة مباشرة بضعف عضلات النهوض من الكرسي.",
    ],
    "when_changes": [
        "لو السؤال يذكر <bdi>factors</bdi> <bdi>risk</bdi> مختلفة زي قيادة سيارة أو مصدر حريق بالمنزل، ينتقل التركيز لنوع إصابة ثاني.",
        "لو الـ<bdi>patient</bdi> شاب وسليم عضليًا، <bdi>risk</bdi> السقوط ما يكون هو الأبرز.",
    ],
    "rule": "ضعف العضلات القريبة وصعوبة النهوض من الكرسي <bdi>sign</bdi> تحذيرية ل<bdi>risk</bdi> السقوط عند كبار السن.",
    "comparison": None,
    "guideline_note": None,
},
7: {
    "idea": "رجل 65 سنة سليم بدون <bdi>diseases</bdi> ولا حساسية، يبي تطعيم المكورات الرئوية (<bdi>pneumococcus</bdi>) لأول مرة، والسؤال عن أفضل خطة تطعيم.",
    "clues": [
        ("65-year-old", "السن اللي يبدأ فيه تطعيم المكورات الرئوية الروتيني"),
        ("asymptomatic, no known allergies", "ما فيه مانع من التطعيم"),
    ],
    "why_correct": [
        "الترتيب المعتمد بهالملف للشخص السليم اللي ما أخذ تطعيم من قبل هو <bdi>PCV13</bdi> أول، وبعدها <bdi>PPSV23</bdi> بعد فترة.",
        "إعطاء <bdi>PCV13</bdi> قبل <bdi>PPSV23</bdi> يعطي استجابة مناعية أقوى مقارنة بالعكس.",
        "ما فيه <bdi>cause</bdi> يمنع التطعيم عند هالمريض (سليم وما عنده حساسية)، فخيار عدم التطعيم غلط.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> أخذ <bdi>PPSV23</bdi> من قبل، الترتيب والتوقيت يختلف عن الشخص اللي ما أخذ شي.",
        "لو عنده كبت مناعي أو <bdi>disease</bdi> <bdi>chronic</bdi> معين، ممكن يتغيّر توقيت وترتيب الجرعات.",
    ],
    "rule": "بالشخص السليم اللي ما أخذ تطعيم مكورات رئوية من قبل، الترتيب <bdi>PCV13</bdi> ثم <bdi>PPSV23</bdi>.",
    "comparison": None,
    "guideline_note": "بعض الإرشادات الحديثة (بعد 2021) تغيّرت وصارت تعتمد لقاح واحد أحدث (<bdi>PCV15</bdi> أو <bdi>PCV20</bdi>) لبعض الفئات بدل هالترتيب القديم، بس جواب الملف هنا هو المعتمد.",
},
8: {
    "idea": "رجل كبير بالسن عنده ألم ركبة بسيط لأول مرة بدون إصابة، ومعه حرقان بالمعدة، والسؤال يبي أنسب مسكّن آمن له.",
    "clues": [
        ("epigastric burning", "<bdi>symptom</bdi> يدل على مشكلة بالمعدة، يزيد <bdi>risk</bdi> مسكنات معينة"),
        ("no history of injury, normal exam", "ألم بسيط ما يحتاج مسكن قوي"),
    ],
    "why_correct": [
        "الحرقان بالمعدة يخلّي مسكنات زي <bdi>aspirin</bdi> و<bdi>ibuprofen</bdi> <bdi>risk</bdi> لأنها تزيد تهيّج المعدة وممكن تسبب قرحة أو نزيف.",
        "<bdi>Paracetamol</bdi> ما يهيّج المعدة، فهو الخيار الأأمن لألم بسيط بدون التهاب واضح.",
        "<bdi>Codeine</bdi> مسكن أقوى من اللازم لألم بسيط، وله <bdi>symptoms</bdi> جانبية أكثر (إمساك، دوخة) خصوصًا بكبار السن.",
    ],
    "when_changes": [
        "لو الألم <bdi>severe</bdi> مع <bdi>signs</bdi> التهاب واضحة (تورم، احمرار)، ممكن يحتاج مسكن أقوى مع حذر من <bdi>complications</bdi> المعدة.",
        "لو ما فيه مشكلة بالمعدة أصلًا، الـ <bdi>ibuprofen</bdi> يصير خيار مقبول لألم عضلي هيكلي بسيط.",
    ],
    "rule": "عند وجود <bdi>symptoms</bdi> معدية، <bdi>paracetamol</bdi> هو المسكن الأول الآمن، ويُتجنّب <bdi>NSAIDs</bdi> و<bdi>aspirin</bdi>.",
    "comparison": None,
    "guideline_note": None,
},
9: {
    "idea": "<bdi>patient</bdi> كبيرة بالسن صار عندها كسر انضغاطي بالفقرات بعد كحة قوية ب<bdi>cause</bdi> <bdi>osteoporosis</bdi>، والسؤال يبي أول <bdi>step</bdi> بالـ<bdi>treatment</bdi>.",
    "clues": [
        ("low back pain after forceful coughing", "آلية كلاسيكية لكسر انضغاطي ب<bdi>patient</bdi> هشة العظام"),
        ("lumbar compression fracture on radiograph", "تأكيد الـ<bdi>diagnosis</bdi> بالأشعة"),
    ],
    "why_correct": [
        "أول <bdi>step</bdi> بأي كسر انضغاطي جديد هي التحكم بالألم، والـ <bdi>acetaminophen</bdi> هو البداية الآمنة قبل أي <bdi>procedure</bdi> تدخلي.",
        "الـ<bdi>procedures</bdi> التدخلية زي <bdi>vertebroplasty</bdi> تنحجز للحالات اللي ما تتحسن بالـ<bdi>treatment</bdi> المحافظ أو الألم الـ<bdi>severe</bdi> المستمر، مو ك<bdi>step</bdi> أولى.",
        "<bdi>Calcitonin</bdi> و<bdi>zoledronate</bdi> يفيدون ب<bdi>treatment</bdi> <bdi>osteoporosis</bdi> على المدى البعيد وتقليل <bdi>risk</bdi> الكسور الجاية، مو كمسكّن أولي فوري.",
    ],
    "when_changes": [
        "لو الألم ما تحسّن بعد أسابيع من الـ<bdi>treatment</bdi> المحافظ، يصير التفكير بـ <bdi>vertebroplasty</bdi> منطقي.",
        "بعد ما يتحسن الألم الـ<bdi>acute</bdi>، لازم تبدأ <bdi>treatment</bdi> <bdi>osteoporosis</bdi> نفسها (مثل <bdi>bisphosphonates</bdi>) لمنع كسور جديدة.",
    ],
    "rule": "بالكسر الانضغاطي الـ<bdi>acute</bdi>، التحكم بالألم بمسكن بسيط هو الـ<bdi>step</bdi> الأولى قبل أي <bdi>treatment</bdi> تدخلي أو <bdi>treatment</bdi> طويل المدى للعظم.",
    "comparison": None,
    "guideline_note": None,
},
10: {
    "idea": "<bdi>patient</bdi> عندها قصور كلوي <bdi>chronic</bdi> (مرحلة 3) وألم بمفصل قاعدة الإبهام ب<bdi>cause</bdi> خشونة، والسؤال يبي أفضل <bdi>treatment</bdi> أولي آمن لكليتها.",
    "clues": [
        ("stage 3 chronic kidney disease", "يحدد أي مسكنات خطرة عليها"),
        ("osteoarthritis of first carpometacarpal joint", "خشونة مفصل، مو التهاب <bdi>acute</bdi> يحتاج <bdi>treatment</bdi> قوي فورًا"),
    ],
    "why_correct": [
        "ب<bdi>osteoarthritis</bdi> الـ<bdi>mild</bdi>، الـ<bdi>treatment</bdi> المحافظ (تثبيت المفصل بجبيرة والـ<bdi>treatment</bdi> الوظيفي) هو الـ<bdi>step</bdi> الأولى قبل أي دواء.",
        "<bdi>NSAIDs</bdi> زي <bdi>ibuprofen 800mg</bdi> بجرعة عالية <bdi>risk</bdi> جدًا على كليتها لأنها بمرحلة 3 من <bdi>renal failure</bdi>، فيتجنّب.",
        "الحقن الستيرويدي أو الجراحة يحجزون لحالات أشد أو ما استجابت لل<bdi>treatment</bdi> المحافظ.",
    ],
    "when_changes": [
        "لو الألم <bdi>severe</bdi> جدًا وما استجاب لل<bdi>treatment</bdi> المحافظ، يصير التفكير بحقن الستيرويد موضعيًا.",
        "لو الكلى سليمة، ممكن نفكر بمسكن من نوع <bdi>NSAIDs</bdi> بحذر لفترة قصيرة.",
    ],
    "rule": "بمرضى <bdi>renal failure</bdi>، الـ<bdi>treatment</bdi> المحافظ (تثبيت و<bdi>treatment</bdi> وظيفي) هو الخيار الأول، وتجنّب <bdi>NSAIDs</bdi> قدر الإمكان.",
    "comparison": None,
    "guideline_note": None,
},
11: {
    "idea": "السؤال يبي أفضل فحص جسدي (حركي) يتوقع <bdi>risk</bdi> السقوط المستقبلي عند رجل كبير بالسن سليم.",
    "clues": [
        ("assist the risk of future falls", "يبي اختبار <bdi>assessment</bdi> <bdi>risk</bdi> السقوط تحديدًا"),
    ],
    "why_correct": [
        "اختبار <bdi>Get-up-and-go test</bdi> هو الفحص المعياري ل<bdi>assessment</bdi> التوازن والمشي و<bdi>risk</bdi> السقوط عند كبار السن.",
        "باقي الخيارات فحوصات ل<bdi>causes</bdi> ثانية (الـ<bdi>nystagmus</bdi> للدوخة الدهليزية، نبض متناقض للقلب والرئة، مرونة الظهر للألم)، مو مخصصة ل<bdi>assessment</bdi> السقوط.",
    ],
    "when_changes": [
        "لو السؤال يبي <bdi>assessment</bdi> دوخة دهليزية بدل <bdi>risk</bdi> السقوط عمومًا، يصير فحص الـ<bdi>nystagmus</bdi> هو المطلوب.",
    ],
    "rule": "اختبار <bdi>Get-up-and-go</bdi> هو الأداة الأساسية ل<bdi>assessment</bdi> <bdi>risk</bdi> السقوط بكبار السن.",
    "comparison": None,
    "guideline_note": None,
},
12: {
    "idea": "رجل كبير بالسن عنده ضعف بالساق اليسرى ب<bdi>cause</bdi> خشونة الورك، والسؤال يبي أي يد يستخدم فيها العصا صح.",
    "clues": [
        ("left-sided leg weakness", "الطرف الضعيف اللي يحتاج دعم"),
    ],
    "why_correct": [
        "العصا لازم تُستخدم باليد المقابلة للطرف الضعيف، يعني هنا اليد اليمنى لأن الضعف باليسار.",
        "استخدام العصا باليد المقابلة يوزّع الوزن بشكل صحيح ويقلل الحمل على المفصل المصاب أثناء المشي.",
        "لو استخدم العصا بنفس جهة الضعف (اليسار)، ما تعطي الدعم الميكانيكي الصحيح وممكن تزيد <bdi>risk</bdi> السقوط.",
    ],
    "when_changes": [
        "لو الضعف كان بالطرف اليمين بدل اليسار، تنعكس القاعدة وتصير العصا باليد اليسرى.",
    ],
    "rule": "العصا تُستخدم دايمًا باليد المقابلة للطرف أو المفصل الضعيف.",
    "comparison": None,
    "guideline_note": None,
},
13: {
    "idea": "رجل كبير بالسن ضغطه غير مضبوط رغم ثلاث أدوية ضغط، والسؤال يبي أكثر <bdi>cause</bdi> يفسر فشل الـ<bdi>treatment</bdi>.",
    "clues": [
        ("6 readings 188-216/03-112 mmHg", "ضغط غير مضبوط رغم <bdi>treatment</bdi> ثلاثي، يدل على مقاومة لل<bdi>treatment</bdi>"),
        ("ramipril, atenolol, amlodipine", "<bdi>treatment</bdi> ثلاثي كامل ومع كذا الضغط عالي"),
        ("Potassium 2.9 (3.5-5.1) mmol/L", "بوتاسيوم <bdi>low</bdi>، قيمة غير <bdi>normal</bdi> بالتحاليل"),
    ],
    "why_correct": [
        "<bdi>NSAIDs</bdi> من أشيع الـ<bdi>causes</bdi> المخفية لمقاومة <bdi>treatment</bdi> الضغط، لأنها تسبب احتباس ملح وسوائل وتقلل فعالية أدوية الضغط.",
        "الملف هنا يعتبر <bdi>NSAIDs</bdi> الـ<bdi>cause</bdi> الأرجح لفشل الـ<bdi>treatment</bdi> رغم ثلاث أدوية مختلفة الآلية.",
        "باقي الخيارات (مضادات الحموضة، ملح الطعام، السودوإيفيدرين) <bdi>causes</bdi> أضعف احتمالًا مقارنة بـ <bdi>NSAIDs</bdi> بهالسياق.",
    ],
    "when_changes": [
        "لو الـ<bdi>patient</bdi> يستخدم كمية ملح عالية موثقة بالتاريخ الغذائي، يصير احتمال الملح أقوى.",
        "لو يستخدم أدوية زكام تحتوي <bdi>pseudoephedrine</bdi> بانتظام، يصير هذا هو الـ<bdi>cause</bdi> الأرجح بدالها.",
    ],
    "rule": "أي ضغط مقاوم لل<bdi>treatment</bdi> رغم عدة أدوية، لازم نسأل عن استخدام <bdi>NSAIDs</bdi> ك<bdi>cause</bdi> مخفي شائع.",
    "comparison": {
        "headers": ["التحليل", "القيمة", "الـ<bdi>normal</bdi>"],
        "rows": [
            ["<bdi>Sodium</bdi>", "138", "134-146 mmol/L"],
            ["<bdi>Potassium</bdi>", "2.9", "3.5-5.1 mmol/L"],
            ["<bdi>Urea</bdi>", "8", "2.75-7.4 mmol/L"],
            ["<bdi>Creatinine</bdi>", "88", "44-115 µmol/L"],
        ],
    },
    "guideline_note": None,
},
}

# short reasons (1-2 lines) for each WRONG option; correct letter's key is omitted/empty
WHY_WRONG = {
1: {
    "B": "بيسفوسفونيت مفعوله يتأخر أيام، مو مناسب ك<bdi>step</bdi> أولى فورية.",
    "C": "الستيرويد يفيد ب<bdi>causes</bdi> معينة بس (زي الساركويدوز)، مو أول <bdi>step</bdi> هنا.",
    "D": "الـ<bdi>furosemide</bdi> ممكن يزيد الجفاف الموجود أصلًا ويسوي المشكلة أسوأ.",
},
2: {
    "B": "حاصرات بيتا تخفض الضغط أكثر وتزيد الصدمة سوء.",
    "C": "التغذية الأنفية المعوية ما تعالج الصدمة الـ<bdi>acute</bdi>، <bdi>procedure</bdi> غير عاجل.",
    "D": "الـ<bdi>dopamine</bdi> يستخدم لو ما تحسن الضغط بعد سوائل كافية، مو ك<bdi>step</bdi> أولى.",
},
3: {
    "A": "الاستشارة <bdi>procedure</bdi> تفاعلي بعد ما تصير المشكلة، مو وقاية منها.",
    "B": "الأكسجين يعالج نقص الأكسجين اللي صار، بس ما يمنع تكرار المشكلة.",
    "C": "الـ<bdi>furosemide</bdi> <bdi>treatment</bdi> لل<bdi>congestion</bdi> بعد حدوثه، مو منع له من الأساس.",
},
4: {
    "A": "التهاب القولون الـ<bdi>acute</bdi> يصاحبه حمى وألم موضعي أشد، مو موجودين هنا.",
    "C": "حصوة الحالب تسبب ألم جانبي <bdi>acute</bdi> وتغيّرات بالبول، والفحص هنا <bdi>normal</bdi>.",
    "D": "التهاب المسالك يعطي <bdi>symptoms</bdi> بولية وتحليل بول غير <bdi>normal</bdi>، وهذا مو موجود.",
},
5: {
    "A": "المشي يحسّن اللياقة القلبية أكثر من قوة العضلات نفسها.",
    "B": "السباحة تمرين هوائي، تأثيرها على قوة العضلات محدود مقارنة بالمقاومة.",
    "D": "الدراجة الثابتة زي المشي، تحسّن اللياقة القلبية مو القوة العضلية بشكل رئيسي.",
},
6: {
    "A": "حوادث السيارات ما لها علاقة مباشرة بضعف عضلات النهوض من الكرسي.",
    "B": "إصابات الحريق مو مرتبطة بالضعف العضلي المذكور بالسؤال.",
    "C": "إصابات الطلق الناري بعيدة تمامًا عن سياق ضعف كبار السن العضلي.",
},
7: {
    "A": "إعطاء PPSV23 قبل PCV13 يعطي استجابة مناعية أضعف من الترتيب الصحيح.",
    "C": "نفس الفكرة بالعكس؛ الترتيب الصحيح PCV13 أول ثم PPSV23.",
    "D": "الـ<bdi>patient</bdi> بعمر يستحق التطعيم الروتيني وما فيه مانع عنده.",
},
8: {
    "A": "الـ<bdi>aspirin</bdi> يهيّج المعدة ويزيد <bdi>risk</bdi> النزيف عند وجود حرقان معدي.",
    "B": "الكودايين مسكن أقوى من اللازم لألم بسيط وله <bdi>symptoms</bdi> جانبية أكثر.",
    "C": "الإيبوبروفين من مضادات الالتهاب اللي تزيد تهيّج المعدة الموجود أصلًا.",
},
9: {
    "A": "الكالسيتونين مفيد كمسكّن مساعد أحيانًا بس مو الـ<bdi>step</bdi> الأولى المعتمدة هنا.",
    "C": "التدخل الجراحي يحجز لو ما تحسن الألم بالـ<bdi>treatment</bdi> المحافظ، مو ك<bdi>step</bdi> أولى.",
    "D": "زوليدرونات يقلل <bdi>risk</bdi> الكسور القادمة على المدى البعيد، مو يعالج الألم الحالي.",
},
10: {
    "A": "الجراحة تحجز للحالات الـ<bdi>severe</bdi> اللي ما استجابت لل<bdi>treatment</bdi> المحافظ.",
    "C": "جرعة الإيبوبروفين العالية خطرة على الكلى المتضررة أصلًا (مرحلة 3).",
    "D": "حقن الستيرويد يستخدم لو ما تحسنت الـ<bdi>symptoms</bdi> بالـ<bdi>treatment</bdi> المحافظ الأولي.",
},
11: {
    "A": "فحص الـ<bdi>nystagmus</bdi> يقيّم مشاكل الدهليز والدوخة، مو <bdi>risk</bdi> السقوط عمومًا.",
    "C": "النبض المتناقض يفحص مشاكل قلبية رئوية معينة، ما له علاقة بالسقوط.",
    "D": "مرونة الظهر تخص مشاكل الظهر، مو أداة <bdi>assessment</bdi> <bdi>risk</bdi> السقوط المعتمدة.",
},
12: {
    "A": "استخدام العصا بنفس جهة الطرف الضعيف ما يعطي الدعم الميكانيكي الصحيح.",
    "C": "لازم تكون بيد محددة (المقابلة للضعف)، مو أي يد بشكل عشوائي.",
    "D": "استخدام العصا بيدين مو الطريقة الصحيحة ولا العملية أثناء المشي.",
},
13: {
    "A": "مضادات الحموضة العادية ما تسبب مقاومة ل<bdi>treatment</bdi> الضغط بهالشكل.",
    "C": "ملح الطعام يرفع الضغط لو موثق بكمية كبيرة، بس أقل احتمالًا هنا من NSAIDs.",
    "D": "السودوإيفيدرين يرفع الضغط لو مستخدم فعلًا، بس النقطة هنا NSAIDs.",
},
}

# exact substrings (verbatim from the stem) to wrap in <mark> on the front of the card.
# these must literally appear in the stem and must not span a <br> line break.
HIGHLIGHT_TERMS = {
1: ["acute confusional state", "postural hypotension", "dry mucus membranes", "Calcium 3.41"],
2: ["decreased level of consciousness", "diarrhea", "poor oral intake", "JVP", "lungs are clear", "cold and", "Blood pressure 83/45 mmHg"],
3: ["history of heart failure", "kept on normal saline", "pulse oxymetry was dropping", "bilateral basal crepitations"],
4: ["colicky abdominal pain", "hard stools once or", "watery stools", "fullness in his left lower quadrant", "urine dipstick is normal"],
5: ["improve the function"],
6: ["difficulty in getting up from the chair"],
7: ["asymptomatic", "no known allergies"],
8: ["epigastric burning", "no history of injury"],
9: ["forceful coughing episode", "lumbar compression fracture"],
10: ["chronic kidney disease", "carpometacarpal joint"],
11: ["risk of future falls"],
12: ["left-sided leg weaknesses"],
13: ["longstanding uncontrolled hypertension", "Potassium 2.9"],
}

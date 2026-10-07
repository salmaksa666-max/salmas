# -*- coding: utf-8 -*-
# AboSarah 2026 - batch05 (OBGYN slice, AS-1614 .. AS-2251, 145 questions)

EXPLANATIONS = {
"AS-1614": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "السؤال يبي أهم <bdi>investigation</bdi> لـ <bdi>intrahepatic cholestasis of pregnancy (ICP)</bdi>، مو بس وصف الأعراض.",
    "clues": [
        ("34 weeks'", "ثلث ثالث من <bdi>pregnancy</bdi>، وقت ظهور <bdi>ICP</bdi> المعتاد"),
        ("generalized pruritus", "حكة عامة بدون <bdi>rash</bdi> = أهم <bdi>clue</bdi> لـ <bdi>ICP</bdi>"),
        ("yellowish discoloration of the sclera", "<bdi>jaundice</bdi> خفيف يصاحب <bdi>ICP</bdi> أحيانًا"),
    ],
    "why_correct": [
        "حكة عامة بثلث ثالث مع يرقان خفيف صورة <bdi>classic</bdi> لـ <bdi>intrahepatic cholestasis of pregnancy</bdi>.",
        "الفحص التشخيصي والمراقبة هو <bdi>serum bile acids</bdi> مع <bdi>liver function tests</bdi>: ارتفاع الـ<bdi>bile acids</bdi> يأكد التشخيص، والـ<bdi>LFTs</bdi> يبين ارتفاع الإنزيمات ويستبعد أسباب كبدية ثانية.",
        "مستوى الـ<bdi>bile acids</bdi> كمان يوجه قرار توقيت <bdi>delivery</bdi> لتقليل خطر الجنين، فلذا هو أهم فحص بالموقف.",
    ],
    "when_changes": [
        "لو فيه <bdi>rash</bdi> واضح مع الحكة، الجواب يتحول لـ <bdi>dermatosis of pregnancy</bdi> مو <bdi>ICP</bdi>.",
        "لو الصورة فيها ارتفاع ضغط وتشوش ونزيف، فكر بـ <bdi>preeclampsia/HELLP</bdi> أو <bdi>AFLP</bdi> وتصير الفحوصات مختلفة.",
    ],
    "rule": "حكة بدون <bdi>rash</bdi> بالثلث الثالث = <bdi>ICP</bdi> لحد ما يثبت العكس، وفحصها <bdi>bile acids</bdi> مع <bdi>LFTs</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1615": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "السؤال يبي <bdi>initial therapy</bdi> لـ <bdi>stress urinary incontinence</bdi>، مو العلاج النهائي.",
    "clues": [
        ("urine leaks when she laughs, coughs, or sneezes", "تسرب مع زيادة الضغط داخل البطن = <bdi>stress incontinence</bdi>"),
        ("initial", "يبي الخطوة الأولى بالعلاج مو الجراحة"),
    ],
    "why_correct": [
        "تسرب البول مع الضحك أو السعال أو العطس، بدون <bdi>frequency</bdi> أو <bdi>dysuria</bdi> أو <bdi>nocturia</bdi> أو <bdi>urgency</bdi>، صورة <bdi>pure stress urinary incontinence</bdi>.",
        "السؤال يحدد «<bdi>initial therapy</bdi>»، والخط الأول لـ <bdi>stress incontinence</bdi> هو تعديل نمط الحياة مع تمارين <bdi>Kegel</bdi> (تقوية عضلات قاع الحوض).",
        "الجراحة تُحجز للحالات اللي ما استجابت للعلاج المحافظ.",
    ],
    "when_changes": [
        "لو السؤال يذكر إنها فشلت بالعلاج المحافظ، الجواب يتحول لـ <bdi>midurethral sling (TVT)</bdi> كعلاج نهائي.",
        "لو فيه <bdi>urgency</bdi> مع سماع صوت الماء، نفكر بـ <bdi>urge incontinence</bdi> وعلاجها <bdi>anticholinergics</bdi> مو <bdi>Kegel</bdi>.",
    ],
    "rule": "«<bdi>initial</bdi>» = <bdi>Kegel exercises</bdi>؛ «<bdi>definitive</bdi>» أو فشل التمارين = <bdi>sling/TVT</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1616": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "السؤال يختبر خطوة التصوير الأولى لـ <bdi>uterine fibroid</bdi> مشتبه فيه.",
    "clues": [
        ("heavy menstrual cycle", "نزيف دورة غزير = عرض شائع لـ <bdi>fibroids</bdi>"),
        ("firm fundal mass", "كتلة صلبة بقاع الرحم تدعم تشخيص <bdi>leiomyoma</bdi>"),
    ],
    "why_correct": [
        "امرأة بسن الإنجاب مع <bdi>heavy menstrual bleeding</bdi> وكتلة صلبة بقاع الرحم غالبًا <bdi>uterine fibroid</bdi>.",
        "<bdi>pelvic ultrasound</bdi> (ويفضل <bdi>transvaginal</bdi>) هو الفحص الأول والتشخيصي عادة: رخيص وآمن وبدون <bdi>radiation</bdi>، ويبين حجم وعدد ومكان الـ<bdi>fibroids</bdi>.",
    ],
    "when_changes": [
        "لو نتيجة الـ<bdi>ultrasound</bdi> غير واضحة أو نحتاج تخطيط قبل جراحة أو <bdi>embolization</bdi>، الجواب يصير <bdi>MRI</bdi>.",
        "لو فيه شك إن الكتلة ليست نموذجية (نمو سريع بعد سن اليأس مثلًا)، نفكر بأسباب أخرى غير <bdi>fibroid</bdi>.",
    ],
    "rule": "كتلة حوضية بسؤال نسائية: <bdi>ultrasound</bdi> أولًا قبل <bdi>MRI</bdi> أو <bdi>CT</bdi> إلا إذا ذكر السؤال إن الـ<bdi>ultrasound</bdi> غير حاسم.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1617": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "السؤال يبي علاج <bdi>dyspareunia</bdi> المعزول بعد سن اليأس، يعني اختيار طريق <bdi>estrogen</bdi> الصح.",
    "clues": [
        ("last menstrual period was 18 months ago", "توقف الدورة 18 شهر يعني <bdi>postmenopausal</bdi>"),
        ("dyspareunia", "عرض <bdi>genitourinary</bdi> معزول من <bdi>vaginal atrophy</bdi>"),
    ],
    "why_correct": [
        "توقف الدورة قبل 18 شهر بعمر 53 يعني <bdi>postmenopausal</bdi>، و<bdi>dyspareunia</bdi> لوحدها عرض <bdi>genitourinary</bdi> ناتج عن <bdi>vaginal atrophy</bdi>.",
        "الأعراض البولية التناسلية المعزولة تُعالج بـ <bdi>local (vaginal) estrogen</bdi> مثل <bdi>conjugated estrogen cream</bdi>، لأنه يشتغل على النسيج المستهدف بامتصاص جهازي قليل.",
    ],
    "when_changes": [
        "لو الشكوى الرئيسية <bdi>hot flashes</bdi> (أعراض <bdi>vasomotor</bdi>)، الجواب يتحول لـ <bdi>systemic HRT</bdi> بعد تعديل نمط الحياة.",
        "لو أعطينا <bdi>systemic estrogen</bdi> ومعها رحم سليم، لازم نضيف <bdi>progestogen</bdi>.",
    ],
    "rule": "<bdi>dyspareunia</bdi> لوحدها بعد سن اليأس = <bdi>cream</bdi> موضعي، مو حبوب؛ الحبوب الجهازية لـ <bdi>hot flashes</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1618": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "كتلة عنق رحم مرئية مع نزيف بعد الجماع = لازم تشخيص نسيجي قبل أي شيء ثاني.",
    "clues": [
        ("postcoital bleeding", "نزيف بعد الجماع = علامة تحذيرية لـ <bdi>cervical cancer</bdi>"),
        ("2*1 cm cervical mass", "كتلة مرئية بعنق الرحم تحتاج خزعة مباشرة"),
    ],
    "why_correct": [
        "<bdi>postcoital bleeding</bdi> مع كتلة عنق رحم مرئية يُفترض إنها <bdi>cervical cancer</bdi> لحد ما يثبت النسيج العكس.",
        "الكتلة المرئية تحتاج تشخيص نسيجي، فالخطوة التالية <bdi>punch biopsy</bdi> (ويفضل موجه بـ <bdi>colposcopy</bdi>).",
    ],
    "when_changes": [
        "لو عنق الرحم يبدو طبيعي بالفحص، الجواب يرجع لـ <bdi>Pap/HPV test</bdi> كفحص فرز.",
        "بعد ما يتأكد التشخيص بالخزعة، نستخدم <bdi>MRI</bdi> للامتداد الموضعي و<bdi>CT/PET</bdi> لانتشار المرض بعيد كجزء من <bdi>staging</bdi>.",
    ],
    "rule": "ما تجاوب <bdi>Pap smear</bdi> إذا فيه كتلة عنق رحم مرئية: روح على الخزعة مباشرة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1619": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "السؤال يختبر إدارة <bdi>SLE</bdi> المستقر بالحمل، وهل نكمل دواء آمن ولا نوقفه.",
    "clues": [
        ("20 weeks pregnant", "حامل بمنتصف الحمل"),
        ("SLE", "مرض مناعي مزمن محتاج ضبط مستمر"),
        ("symptom-free for the past 2 years", "مرض هادئ ومستقر حاليًا"),
        ("Plaquenil", "اسم تجاري لـ <bdi>hydroxychloroquine</bdi>"),
    ],
    "why_correct": [
        "<bdi>hydroxychloroquine (Plaquenil)</bdi> آمن بالحمل وهو العمود الأساسي لضبط <bdi>SLE</bdi>.",
        "المريضة <bdi>symptom-free</bdi> لمدة سنتين عليه، فالخطوة الصح إنها تكمل الدواء بدون تغيير.",
        "إيقافه يرفع خطر <bdi>flare</bdi> بالحمل، واللي خطره على الأم والجنين أكبر من خطر الدواء نفسه.",
    ],
    "when_changes": [
        "لو فيه <bdi>drug reaction</bdi> حقيقي زي <bdi>retinal toxicity</bdi>، حينها يصير الجواب إيقاف الدواء.",
        "لو فيه <bdi>active flare</bdi> بالحمل، نضيف <bdi>steroids</bdi> مع الدواء الأساسي، مو بدل منه.",
    ],
    "rule": "<bdi>hydroxychloroquine</bdi> هو دواء <bdi>SLE</bdi> اللي نكمله بالحمل؛ <bdi>mycophenolate</bdi> و<bdi>methotrexate</bdi> هم اللي نوقفهم.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1620": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "السؤال يبي عامل خطر <bdi>postpartum hemorrhage</bdi> المرتبط بسرعة الولادة.",
    "clues": [
        ("2 hours of labor, just making it to the hospital", "ولادة خلال ساعتين فقط = <bdi>precipitous labor</bdi>"),
    ],
    "why_correct": [
        "ولادة «بعد ساعتين فقط من المخاض، بالكاد وصلت المستشفى» هي تعريف <bdi>precipitous labor</bdi> (ولادة خلال حوالي 3 ساعات من بداية المخاض).",
        "المخاض السريع عامل خطر لـ <bdi>uterine atony</bdi> ولإصابات الجهاز التناسلي، وبالتالي لـ <bdi>postpartum hemorrhage</bdi>.",
        "الولادة الأولى (P1) والوزن 3000 غرام طبيعيان، فما يعتبرون عامل خطر هنا.",
    ],
    "when_changes": [
        "لو كانت الولادة طالت لساعات كثيرة (مثلًا 16 ساعة)، الجواب يتحول لـ <bdi>prolonged labor</bdi>.",
        "لو كان وزن الجنين أكبر من 4000 غرام، الجواب يصير <bdi>macrosomic baby</bdi>.",
    ],
    "rule": "عبارة «بالكاد وصلت المستشفى» برمز الامتحان تعني <bdi>precipitous labor</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1621": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "السؤال يبي تصنيف توقيت النزيف التوليدي حسب علاقته بالمخاض والولادة.",
    "clues": [
        ("32 weeks of gestation", "لسا حامل ومافي وصف لمخاض"),
    ],
    "why_correct": [
        "المريضة لسا حامل (<bdi>32 weeks of gestation</bdi>) وما فيه إشارة إنها بمخاض.",
        "نزيف أثناء الحمل وقبل بداية المخاض يُسمى <bdi>antepartum hemorrhage</bdi>.",
    ],
    "when_changes": [
        "لو ذكر السؤال إن عنق الرحم متوسع (مخاض فعلي)، الجواب يتحول لـ <bdi>intrapartum</bdi>.",
        "لو النزيف بعد الولادة بأقل من 24 ساعة، يصير <bdi>early postpartum</bdi>؛ وإذا بعد أكثر من 24 ساعة لين 12 أسبوع، يصير <bdi>late postpartum</bdi>.",
    ],
    "rule": "صنّف النزيف التوليدي حسب توقيته بالنسبة للمخاض والولادة: قبل المخاض = <bdi>antepartum</bdi>، أثناءه = <bdi>intrapartum</bdi>، وبعد الولادة = <bdi>postpartum</bdi> (مبكر أو متأخر).",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1621B": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نفس تصنيف توقيت النزيف التوليدي، بس هنا بعد الولادة بثلاث أسابيع.",
    "clues": [
        ("3 weeks after vaginal delivery", "بعد 24 ساعة من الولادة وقبل 12 أسبوع = <bdi>late (secondary) postpartum</bdi>"),
    ],
    "why_correct": [
        "<bdi>postpartum hemorrhage</bdi> يُصنف حسب التوقيت: <bdi>primary (early)</bdi> خلال أول 24 ساعة، و<bdi>secondary (late)</bdi> من 24 ساعة لين 12 أسبوع.",
        "النزيف هنا بعد 3 أسابيع من الولادة، فهو ضمن النافذة الثانية، يعني <bdi>late postpartum (secondary) hemorrhage</bdi>، وغالبًا سببه بقايا مشيمية أو <bdi>endometritis</bdi>.",
    ],
    "when_changes": [
        "لو النزيف صار خلال أول 24 ساعة بعد الولادة، الجواب يتحول لـ <bdi>early postpartum</bdi>، والسبب الأشيع <bdi>uterine atony</bdi>.",
        "لو النزيف قبل الولادة أصلًا، الجواب يصير <bdi>antepartum</bdi>.",
    ],
    "rule": "الحد الفاصل 24 ساعة: قبل كذا <bdi>early</bdi>، وبعده لين 12 أسبوع <bdi>late</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
}  # END_EXPL

WHY_WRONG = {
"AS-1614": {
    "A": "تقدير وزن الجنين بالـ<bdi>ultrasound</bdi> ما يشخص ولا يقيّم <bdi>ICP</bdi>؛ خطر الجنين فيها (موت مفاجئ) ما تتوقعه فحوصات النمو.",
    "C": "<bdi>coagulation profile</bdi> فحص ثانوي (سوء امتصاص فيتامين K من الـ<bdi>cholestasis</bdi> ممكن يطوّل PT)، يساعد بالإدارة بس ما يشخص.",
    "D": "الأعراض نفسها مذكورة بالسؤال ومو فحص؛ الحكة لوحدها ما تأكد <bdi>ICP</bdi> بدون تحاليل.",
},
"AS-1615": {
    "B": "<bdi>anticholinergics</bdi> علاج لـ <bdi>urge incontinence</bdi> (فرط نشاط العضلة الدافعة)، والمريضة تنفي أي <bdi>urgency</bdi>.",
    "C": "<bdi>bladder suspension</bdi> أو <bdi>sling (TVT)</bdi> علاج نهائي بعد فشل العلاج المحافظ، مو خطوة أولى.",
    "D": "<bdi>anterior colporrhaphy</bdi> يصلح <bdi>cystocele</bdi> وما له فعالية بـ <bdi>stress incontinence</bdi>، وما فيه وصف لـ <bdi>prolapse</bdi> أصلًا.",
},
"AS-1616": {
    "A": "<bdi>MRI</bdi> خط ثاني: يُستخدم لتخطيط الـ<bdi>fibroids</bdi> قبل جراحة أو <bdi>embolization</bdi>، مو الفحص الأول.",
    "B": "<bdi>CT</bdi> ضعيف بتمييز أنسجة الرحم اللينة ويضيف إشعاع؛ ما له دور بتشخيص <bdi>fibroids</bdi>.",
    "D": "<bdi>fibroid</bdi> يُشخص بالتصوير مو بالنسيج؛ الخزعة ليست جزء من تقييم كتلة قاعية نموذجية.",
},
"AS-1617": {
    "A": "<bdi>Depo-Provera</bdi> موانع حمل <bdi>progestin</bdi> تخفض الـ<bdi>estrogen</bdi> أكثر وتزيد الـ<bdi>atrophy</bdi>، وهي أصلًا ما تحتاج منع حمل.",
    "B": "حبوب منع الحمل المركبة غير مناسبة بعد سن اليأس وتزيد خطر الجلطات بعمرها.",
    "C": "<bdi>systemic estrogen</bdi> لأعراض <bdi>vasomotor</bdi> (الهبات الساخنة)؛ للأعراض المهبلية المعزولة يُفضل الموضعي، وإعطاء جهازي مع رحم سليم يحتاج <bdi>progestogen</bdi> إضافي.",
},
"AS-1618": {
    "A": "<bdi>Pap test</bdi> فحص فرز لعنق رحم بدون كتلة واضحة؛ ممكن يطلع سلبي كاذب مع ورم ظاهر.",
    "B": "<bdi>pelvic CT</bdi> يقيّم انتشار المرض للعقد والأعضاء البعيدة كجزء من <bdi>staging</bdi> بعد تأكيد التشخيص نسيجيًا.",
    "C": "<bdi>pelvic MRI</bdi> أفضل لتقييم الامتداد الموضعي بعد التشخيص، وما يعطي تشخيص نسيجي.",
},
"AS-1619": {
    "A": "إيقاف <bdi>hydroxychloroquine</bdi> يرفع خطر <bdi>flare</bdi> بالحمل؛ ما يوقف إلا لتفاعل دوائي حقيقي زي <bdi>retinal toxicity</bdi>.",
    "B": "<bdi>steroids</bdi> لعلاج <bdi>flare</bdi> نشط مو مرض هادئ، وتبديلها يضيف مخاطر زي <bdi>gestational diabetes</bdi> و<bdi>hypertension</bdi> بدون فايدة.",
    "D": "ما فيه سبب لإيقاف الدواء أصلًا، فالتحويل لهذا الغرض غلط؛ متابعة الروماتيزم مفيدة بس مو لإيقاف الدواء.",
},
"AS-1620": {
    "A": "<bdi>grand parity</bdi> يعني ولادة أكثر من 3، وهي P1 بعيدة عن هالحد.",
    "B": "ساعتين عكس <bdi>prolonged labor</bdi> تمامًا؛ المخاض المطول مثاله 16 ساعة.",
    "C": "3000 غرام وزن طبيعي (بين 2500 و3500 غرام)، مو <bdi>macrosomic</bdi>.",
},
"AS-1621": {
    "A": "<bdi>early postpartum</bdi> يحصل بعد الولادة خلال 24 ساعة؛ المريضة لسا ما ولدت.",
    "B": "<bdi>late postpartum</bdi> يحصل من 24 ساعة لين 12 أسبوع بعد الولادة؛ المريضة لسا حامل.",
    "C": "<bdi>intrapartum</bdi> يحتاج مخاض فعلي (مثل اتساع عنق الرحم)؛ ما فيه وصف مخاض هنا.",
},
"AS-1621B": {
    "A": "<bdi>early postpartum</bdi> خلال أول 24 ساعة بعد الولادة، أغلبها بسبب <bdi>uterine atony</bdi>؛ 3 أسابيع أبعد من هالنافذة بكثير.",
    "C": "<bdi>intrapartum</bdi> نزيف أثناء المخاض والولادة قبل خروج الجنين والمشيمة.",
    "D": "<bdi>antepartum</bdi> نزيف أثناء الحمل قبل المخاض (بعد 20 أسبوع) زي <bdi>previa</bdi> أو <bdi>abruption</bdi>؛ هذي المريضة ولدت أصلًا.",
},
}  # END_WW

HIGHLIGHT_TERMS = {
"AS-1614": ["34 weeks'", "generalized pruritus", "yellowish discoloration of the sclera"],
"AS-1615": ["urine leaks when she laughs, coughs, or sneezes", "initial"],
"AS-1616": ["heavy menstrual cycle", "firm fundal mass"],
"AS-1617": ["last menstrual period was 18 months ago", "dyspareunia"],
"AS-1618": ["postcoital bleeding", "2*1 cm cervical mass"],
"AS-1619": ["20 weeks pregnant", "SLE", "symptom-free for the past 2 years", "Plaquenil"],
"AS-1620": ["2 hours of labor", "just making it to the hospital"],
"AS-1621": ["32 weeks of gestation"],
"AS-1621B": ["3 weeks after vaginal delivery"],
}  # END_HL

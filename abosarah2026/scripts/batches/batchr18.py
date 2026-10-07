# -*- coding: utf-8 -*-
# Batch r18: Pediatrics / Psychiatry / Ophthalmology / Dermatology (137 questions)

EXPLANATIONS = {
"AS-2300": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "طفل <bdi>male</bdi> عنده مجموعة <bdi>dysmorphic features</bdi> تشبه <bdi>Turner syndrome</bdi>، والسؤال يبي الـ<bdi>differential diagnosis</bdi> الصحيح بوجود <bdi>normal karyotype</bdi> متوقع لأنه ذكر.",
    "clues": [
        ("cryptorchidism", "خصية غير نازلة، من علامات <bdi>Noonan syndrome</bdi>"),
        ("low lying epicanthal folds", "ملامح وجه تشبه <bdi>Turner</bdi>"),
        ("nuchal skin", "جلد زايد بالرقبة (<bdi>webbed neck</bdi>)"),
    ],
    "why_correct": [
        "ذكر فيه <bdi>cryptorchidism</bdi> و<bdi>epicanthal folds</bdi> و<bdi>excess nuchal skin</bdi> (<bdi>webbed neck</bdi>) هذا هو شكل <bdi>Noonan syndrome</bdi> اللي يشبه <bdi>Turner</bdi> بالمظهر.",
        "الفرق المهم إن <bdi>Noonan</bdi> يصير بالذكور والإناث مع <bdi>karyotype</bdi> طبيعي، عكس <bdi>Turner</bdi> اللي يحتاج <bdi>45,X</bdi> وتصير فقط بالبنات.",
        "من ملامح <bdi>Noonan</bdi> الإضافية: قصر القامة، <bdi>hypertelorism</bdi>، و<bdi>pulmonary valve stenosis</bdi> بالقلب (قلب يمين عكس <bdi>Turner</bdi> اللي فيها تضيّق بالقلب الشمال).",
    ],
    "when_changes": [
        "لو كانت الحالة بنت بدال ولد مع نفس الملامح، الجواب يصير <bdi>Turner syndrome</bdi> بدل <bdi>Noonan</bdi>.",
        "لو السؤال ذكر <bdi>coarctation of aorta</bdi> بدل <bdi>pulmonary stenosis</bdi>، هذا يرجّح <bdi>Turner</bdi> أكثر.",
    ],
    "rule": "ملامح <bdi>Turner-like</bdi> عند ذكر مع <bdi>karyotype</bdi> طبيعي = <bdi>Noonan syndrome</bdi>؛ قلب يمين (<bdi>pulmonary stenosis</bdi>) يميزها عن قلب شمال (<bdi>coarctation</bdi>) باللي بـ<bdi>Turner</bdi>.",
    "comparison": {
        "headers": ["الحالة", "الجنس", "القلب"],
        "rows": [
            ["Noonan syndrome", "ذكر أو أنثى، <bdi>karyotype</bdi> طبيعي", "<bdi>pulmonary stenosis</bdi>"],
            ["Turner syndrome", "أنثى فقط، <bdi>45,X</bdi>", "<bdi>coarctation of aorta</bdi>"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},
"AS-2310": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "طفل عنده <bdi>fecal soiling</bdi>، والسؤال يفرّق بين <bdi>functional constipation</bdi> و<bdi>Hirschsprung disease</bdi> كسبب للتسريب.",
    "clues": [
        ("Fecal soiling", "تسريب براز حول <bdi>impaction</bdi>، سمة <bdi>functional constipation</bdi>"),
    ],
    "why_correct": [
        "عند <bdi>child</bdi> (بعد مرحلة الرضاعة) مع <bdi>fecal soiling</bdi>، السبب الشائع هو <bdi>idiopathic constipation</bdi> مع <bdi>overflow incontinence</bdi>: البراز القاسي المحتجز يمدد <bdi>rectum</bdi> ويضعف الحس فيتسرب براز رخو حول الانحشار.",
        "<bdi>soiling</bdi> نفسه هي علامة مميزة لـ<bdi>functional constipation</bdi> وتبعد عن انسداد <bdi>organic</bdi>.",
    ],
    "when_changes": [
        "لو الأعراض من الولادة مباشرة مع تأخر خروج <bdi>meconium</bdi> وانتفاخ وبدون <bdi>soiling</bdi>، الجواب يصير <bdi>Hirschsprung disease</bdi>.",
    ],
    "rule": "<bdi>soiling</bdi> مع براز محسوس بـ<bdi>rectum</bdi> = <bdi>functional constipation</bdi>؛ أعراض من الولادة مع <bdi>rectum</bdi> فاضي ومشدود = <bdi>Hirschsprung</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2311": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "رضيع كان طبيعي مع <bdi>breastfeeding</bdi> وصارت عنده <bdi>vomiting</bdi> و<bdi>jaundice</bdi> بعد إدخال الفواكه، يعني السؤال يفحص معرفة <bdi>enzyme deficiency</bdi> المرتبط بالمحرض الغذائي.",
    "clues": [
        ("7-month-old", "عمر إدخال الأطعمة الصلبة والفواكه"),
        ("Symptoms began after the introduction of fruits and fruit juices", "المحرض هو <bdi>fructose</bdi>، يدل على <bdi>hereditary fructose intolerance</bdi>"),
    ],
    "why_correct": [
        "رضيع كان يتحمل <bdi>breastfeeding</bdi> كويس وصارت عنده <bdi>vomiting</bdi> و<bdi>jaundice</bdi> بعد دخول الفواكه وعصير الفواكه، هذا <bdi>hereditary fructose intolerance</bdi> (نقص إنزيم <bdi>aldolase B</bdi>).",
        "تراكم <bdi>fructose 1 phosphate</bdi> يسبب <bdi>vomiting</bdi> و<bdi>hypoglycemia</bdi> وإصابة الكبد، و<bdi>fructose</bdi> يظهر بالبول كـ<bdi>reducing substance</bdi> وهذا يفسر الـ<bdi>urine sediment test</bdi> الإيجابي.",
    ],
    "when_changes": [
        "لو الأعراض بدأت من أول أيام الحليب (رضاعة طبيعية أو صناعية) بدل الفواكه، الجواب يصير <bdi>Galactosemia</bdi>.",
        "لو السبب إدخال حبوب القمح مع <bdi>chronic diarrhea</bdi> و<bdi>failure to thrive</bdi>، الجواب يصير <bdi>gluten insensitivity</bdi>.",
    ],
    "rule": "طابق المحرض الغذائي بالإنزيم الناقص: الفاكهة والسكروز = <bdi>fructose intolerance</bdi> (<bdi>aldolase B</bdi>)، الحليب من أول الأسابيع = <bdi>galactosemia</bdi>، القمح = <bdi>celiac disease</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2319": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "طفل عنده أعراض <bdi>asthma</bdi> نمطية، والسؤال يبي الدليل <bdi>objective</bdi> الحقيقي مقابل عوامل التاريخ الداعمة فقط.",
    "clues": [
        ("objective evidence", "السؤال يبي نتيجة فحص، مو مجرد تاريخ مرضي"),
    ],
    "why_correct": [
        "السؤال يحدد <bdi>objective evidence</bdi>؛ <bdi>atopy</bdi> والتاريخ العائلي والسعال الليلي كلها تاريخ داعم، بس الدليل الموضوعي الوحيد هو <bdi>spirometry</bdi>: زيادة <bdi>FEV1</bdi> بنسبة 12% أو أكثر بعد <bdi>bronchodilator</bdi> يؤكد <bdi>reversible airflow obstruction</bdi> وهذا يثبت <bdi>asthma</bdi>.",
    ],
    "when_changes": [
        "لو الـ<bdi>spirometry</bdi> طبيعي بس الشك عالي، الدليل الموضوعي البديل يصير <bdi>methacholine challenge test</bdi> (انخفاض <bdi>FEV1</bdi> ≥20%).",
    ],
    "rule": "«<bdi>objective evidence</bdi>» بالسؤال يعني نتيجة فحص (<bdi>spirometry reversibility</bdi>)، مو عنصر من التاريخ المرضي.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2329": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "طفل صغير عنده <bdi>pica</bdi> وشرب حليب زايد وشحوب، والسؤال يبي الفحص الأول الصحيح لتأكيد <bdi>anemia</bdi> قبل أي فحص آخر.",
    "clues": [
        ("drinks 1 litter of milk daily", "حليب زايد يبعّد الحديد ويقلل الأطعمة الصلبة"),
        ("eats dirt", "<bdi>pica</bdi>، علامة شائعة بـ<bdi>iron deficiency</bdi>"),
        ("pale conjunctiva", "علامة سريرية على <bdi>anemia</bdi>"),
    ],
    "why_correct": [
        "طفل بعمر 18 شهر يشرب <bdi>1 litre</bdi> حليب يوميًا مع أكل صلب قليل، و<bdi>pica</bdi> (أكل التراب)، و<bdi>underweight</bdi> و<bdi>pale conjunctiva</bdi>، هذا <bdi>iron deficiency anemia</bdi> لحد يثبت العكس.",
        "الفحص الأول هو <bdi>CBC with blood smear</bdi>: يأكد وجود <bdi>anemia</bdi>، ويوضح الصفات <bdi>microcytic hypochromic</bdi> وشكل الخلايا، وبعدها يوجّه لفحوصات <bdi>iron studies</bdi> الإضافية.",
    ],
    "when_changes": [
        "لو كان السؤال يبي فحص يأكد نقص الحديد تحديدًا بعد تأكيد الـ<bdi>anemia</bdi>، الجواب يصير <bdi>Ferritin level</bdi>.",
        "لو السؤال ركّز على خطر التسمم المصاحب لـ<bdi>pica</bdi>، يُضاف <bdi>lead screening</bdi> كخطوة موازية.",
    ],
    "rule": "طفل صغير + حليب بقر زايد + <bdi>pica</bdi> + شحوب = <bdi>iron deficiency anemia</bdi>؛ الفحص الأول دايمًا <bdi>CBC with smear</bdi> قبل <bdi>ferritin</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2337": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "طفل عنده تورم حول العين صبحًا مع <bdi>hypoalbuminemia</bdi> و<bdi>proteinuria</bdi> شديد، والسؤال يفرّق <bdi>nephrotic</bdi> عن <bdi>nephritic</bdi> syndrome وأسباب أخرى للتورم.",
    "clues": [
        ("eye puffiness", "تورم حول العين، أسوأ بالصبح، علامة <bdi>nephrotic syndrome</bdi>"),
        ("Albumin 16", "<bdi>hypoalbuminemia</bdi> شديد"),
        ("Protein +4", "<bdi>proteinuria</bdi> بمستوى <bdi>nephrotic range</bdi>"),
    ],
    "why_correct": [
        "طفل بعمر 5 سنين مع تورم حول العين صبحًا، <bdi>blood pressure</bdi> طبيعي، <bdi>albumin</bdi> منخفض جدًا، و<bdi>proteinuria</bdi> 4+، هذا <bdi>nephrotic syndrome</bdi>: <bdi>proteinuria</bdi> شديد + <bdi>hypoalbuminemia</bdi> + <bdi>edema</bdi>.",
        "بهذا العمر السبب الأشيع <bdi>minimal change disease</bdi>، غالبًا بعد مرض فيروسي.",
    ],
    "when_changes": [
        "لو كان فيه <bdi>hematuria</bdi> و<bdi>hypertension</bdi> و<bdi>oliguria</bdi> مع <bdi>proteinuria</bdi> خفيف، الجواب يصير <bdi>nephritic syndrome</bdi>.",
        "لو الـ<bdi>urine</bdi> سليم من البروتين مع تورم وألبومين منخفض، فكّر بـ<bdi>protein losing enteropathy</bdi> بدل الكلى.",
    ],
    "rule": "<bdi>nephrotic syndrome</bdi> = <bdi>proteinuria</bdi> + <bdi>hypoalbuminemia</bdi> + <bdi>edema</bdi>؛ مرض فيروسي سابق مجرد مشتت وليس دليل على <bdi>post-infectious nephritis</bdi>.",
    "comparison": {
        "headers": ["الحالة", "BP", "Proteinuria"],
        "rows": [
            ["Nephrotic syndrome", "طبيعي", "شديد (3+ إلى 4+)"],
            ["Nephritic syndrome", "مرتفع", "خفيف مع <bdi>hematuria</bdi>"],
        ],
    },
    "labs": [
        ["Total Proteins", "35 g/L", "56-80 g/L"],
        ["Albumin", "16 g/L", "36-52 g/L"],
        ["Urine Protein", "+4", "Absent"],
        ["Blood Pressure", "100/70 mmHg", "طبيعي للعمر"],
    ],
    "guideline_note": None,
},
"AS-2344": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال وراثة <bdi>autosomal recessive</bdi> لـ<bdi>sickle cell disease</bdi>، والمطلوب تقييم خطر الطفل حسب حالة كل من الوالدين لا تاريخ العائلة البعيد.",
    "clues": [
        ("SC trait", "الأب حامل لجين واحد فقط من <bdi>sickle cell</bdi>"),
        ("woman didn't test yet", "حالة الأم الحاملة غير معروفة، لازم فحصها أولًا"),
    ],
    "why_correct": [
        "<bdi>sickle cell disease</bdi> وراثتها <bdi>autosomal recessive</bdi>: الطفل يصاب فقط لو الوالدين كلاهما حاملين للجين.",
        "الأب حامل (<bdi>SC trait</bdi>)، والأم من عائلة بدون <bdi>SCD</bdi> وغير مفحوصة، فالخطر منخفض ويصير معدوم لو فحص <bdi>hemoglobin electrophoresis</bdi> للأم جاء سلبي.",
        "الخطوة الصحيحة هي فحص الأم قبل إعطاء نسبة خطر نهائية.",
    ],
    "when_changes": [
        "لو ثبت إن الأم حاملة كذلك، يصير الخطر مرتفع (25% إصابة لكل حمل).",
        "لو الأم غير حاملة فعلًا بعد الفحص، الخطر يصير صفر على الإصابة بالمرض (الطفل ممكن يكون حامل فقط).",
    ],
    "rule": "بالأمراض <bdi>autosomal recessive</bdi> لازم تعرف حالة الوالدين الاثنين؛ حامل × غير مفحوص = خطر منخفض لحد الفحص، مو مرتفع ولا معدوم مباشرة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2351": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "طفل عنده <bdi>jaundice</bdi> تدريجي مع <bdi>tremor</bdi> و<bdi>hemolytic anemia</bdi> وعلامات <bdi>chronic liver disease</bdi>، هذا <bdi>Wilson disease</bdi>، والسؤال يبي الفحص <bdi>gold standard</bdi> تحديدًا.",
    "clues": [
        ("progressive jaundice and mild tremors", "يدل على <bdi>liver</bdi> + <bdi>neurological</bdi> involvement معًا، نموذجي لـ<bdi>Wilson disease</bdi>"),
        ("decreased school performance", "تدهور معرفي/عصبي خفي مصاحب"),
        ("gold standard", "السؤال يبي الفحص التأكيدي الحاسم، مو الفحص الأولي"),
    ],
    "why_correct": [
        "طفل بعمر 6 سنين مع <bdi>jaundice</bdi> تدريجي، <bdi>tremor</bdi>، تراجع بالتحصيل الدراسي، علامات <bdi>chronic liver disease</bdi>، و<bdi>hemolytic anemia</bdi> (Hb منخفض مع <bdi>retics</bdi> مرتفع) = <bdi>Wilson disease</bdi>.",
        "السؤال يحدد <bdi>gold standard</bdi>: <bdi>liver biopsy</bdi> مع قياس <bdi>hepatic copper content</bdi> هو الفحص التأكيدي النهائي، لأن <bdi>serum ceruloplasmin</bdi> و<bdi>urinary copper</bdi> ممكن يكونوا غير حاسمين.",
    ],
    "when_changes": [
        "لو السؤال صاغ اللفظ «<bdi>most appropriate investigation</bdi>» بدل <bdi>gold standard</bdi>، الجواب يصير <bdi>24h urine copper excretion</bdi> كفحص عملي أولي.",
    ],
    "rule": "«<bdi>gold standard</bdi>» في <bdi>Wilson disease</bdi> = <bdi>liver biopsy</bdi> بقياس النحاس؛ «<bdi>most appropriate investigation</bdi>» = <bdi>24h urine copper</bdi>.",
    "comparison": None,
    "labs": [
        ["Hb", "7", "طبيعي حسب العمر (أعلى من 7)"],
        ["Retics", "6%", "0.5-1.5%"],
        ["Direct bilirubin", "20", "مرتفع"],
        ["Total bilirubin", "25", "مرتفع"],
    ],
    "guideline_note": "نفس السيناريو يتكرر بسؤال <bdi>AS-2352</bdi> بصيغة لفظية مختلفة («<bdi>most appropriate investigation</bdi>») وجوابه <bdi>D</bdi>؛ هذا مو تعارض حقيقي، بل اختلاف بصيغة السؤال نفسه.",
},
"AS-2352": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "نفس سيناريو <bdi>Wilson disease</bdi> السابق، لكن هنا السؤال يبي الفحص العملي الأول (<bdi>most appropriate</bdi>) مو الفحص التأكيدي النهائي.",
    "clues": [
        ("progressive jaundice and mild tremors", "علامة <bdi>Wilson disease</bdi>"),
        ("decreased school performance", "تدهور عصبي خفي"),
        ("Most appropriate Investigation", "يبي الفحص العملي الأول، مو <bdi>gold standard</bdi>"),
    ],
    "why_correct": [
        "<bdi>jaundice</bdi> تدريجي، <bdi>tremor</bdi>، تراجع دراسي، علامات <bdi>chronic liver disease</bdi>، و<bdi>hemolysis</bdi> في طفل 6 سنين تدل على <bdi>Wilson disease</bdi>.",
        "السؤال يحدد <bdi>most appropriate investigation</bdi>، يعني الفحص غير التداخلي العملي: <bdi>24 hour urinary copper excretion</bdi> يرتفع في <bdi>Wilson disease</bdi> ويُستخدم مع <bdi>ceruloplasmin</bdi> وفحص العين بـ<bdi>slit lamp</bdi> للتشخيص.",
    ],
    "when_changes": [
        "لو السؤال طلب <bdi>gold standard</bdi> بدل الفحص العملي، الجواب يرجع إلى <bdi>liver biopsy</bdi>.",
    ],
    "rule": "نفس السيناريو، لكن تغيّر صياغة اللفظ («<bdi>gold standard</bdi>» مقابل «<bdi>most appropriate investigation</bdi>») يغيّر الجواب بين <bdi>liver biopsy</bdi> و<bdi>24h urine copper</bdi>.",
    "comparison": None,
    "labs": [
        ["Hb", "7", "طبيعي حسب العمر (أعلى من 7)"],
        ["Retics", "6%", "0.5-1.5%"],
        ["Direct bilirubin", "20", "مرتفع"],
        ["Total bilirubin", "25", "مرتفع"],
    ],
    "guideline_note": "هذا سؤال مطابق لـ<bdi>AS-2351</bdi> لكن بصياغة لفظ مختلفة؛ الجوابان صحيحان كل واحد بسياقه (<bdi>gold standard</bdi> مقابل <bdi>most appropriate investigation</bdi>) وليسوا تعارض حقيقي.",
},
"AS-2353": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "طفلة شاحبة مع <bdi>microcytic anemia</bdi> وتاريخ عائلي لإخوة مصابين، والمصدر هنا يختار <bdi>sickle cell disease</bdi> رغم إن ملامح التغذية تدعم <bdi>iron deficiency</bdi> أيضًا.",
    "clues": [
        ("drinking 3 glasses of cow's milk daily", "يدعم <bdi>iron deficiency</bdi>، بس المصدر هنا يرجّح السبب الوراثي"),
        ("MCV 62", "<bdi>microcytic anemia</bdi>"),
        ("Ferritin 9", "منخفض، يدعم <bdi>iron deficiency</bdi> عادةً"),
    ],
    "why_correct": [
        "هذا السجل مُفتاح على <bdi>sickle cell disease</bdi>؛ استدلال المصدر يعتمد على وجود <bdi>similar presentation</bdi> في أخوين، نمط عائلي يرجّح <bdi>hemoglobinopathy</bdi> وراثي (<bdi>autosomal recessive</bdi> تنتشر بين الإخوة)، و<bdi>reticulocytes 3%</bdi> أعلى من الطبيعي يدعم زيادة تكسّر الدم.",
        "عند الشك بـ<bdi>hemoglobinopathy</bdi> الفحص المؤكد هو <bdi>hemoglobin electrophoresis</bdi>.",
    ],
    "when_changes": [
        "لو حذفنا تاريخ الإخوة المصابين وبقيت فقط عادات الحليب والتغذية، الجواب العلمي الأرجح يصير <bdi>iron deficiency anemia</bdi> (كما بسؤال <bdi>AS-2354</bdi> المطابق تقريبًا).",
    ],
    "rule": "هذا السؤال من النوع المتنازع عليه بالمصدر نفسه: نفس السيناريو تقريبًا يُجاب هنا بـ<bdi>A</bdi> لكن بنسخ مشابهة (<bdi>AS-2354</bdi>، <bdi>AS-2355</bdi>) يُجاب بـ<bdi>C. Iron deficiency anemia</bdi>.",
    "comparison": {
        "headers": ["الحالة", "Ferritin", "Reticulocytes"],
        "rows": [
            ["Iron deficiency anemia", "منخفض", "طبيعي/منخفض"],
            ["Sickle cell disease", "طبيعي/مرتفع", "مرتفع (تكسّر دم)"],
        ],
    },
    "labs": [
        ["RBC", "3", "4.6-4.8 x10^12/L (child)"],
        ["Hb", "4", "112-165 g/L (child)"],
        ["MCH", "18", "28-33 pg/cell"],
        ["MCV", "62", "80-95 fL"],
        ["Reticulocyte", "3%", "0.2-1.2%"],
        ["Platelets", "480", "150-400 x10^9/L"],
        ["Ferritin", "9", "20-200 µg/L"],
    ],
    "guideline_note": "المصدر نفسه يسجّل تعارض: نفس السؤال تقريبًا (<bdi>AS-2354</bdi>, <bdi>AS-2355</bdi>) جوابه <bdi>C. Iron deficiency anemia</bdi>، والملاحظة التوضيحية بالمصدر تقول إن صفحة <bdi>AS-2353</bdi> تطبع الجواب <bdi>A</bdi> رغم تشابه الصورة السريرية مع النسخ الأخرى. نحتفظ بجواب المصدر المؤكد لهذه البطاقة تحديدًا (<bdi>A</bdi>) كما تنص القاعدة.",
},
"AS-2354": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "نفس صورة الطفلة الشاحبة، لكن هنا التركيز الأوضح على عادات التغذية (حليب زايد + أكل سيء) والمختبر يرجّح <bdi>iron deficiency anemia</bdi> بوضوح.",
    "clues": [
        ("drinking 3 pints of cow's milk daily", "حليب بقر زايد يبعّد الحديد"),
        ("MCV 62", "<bdi>microcytic anemia</bdi>"),
        ("Ferritin 9", "منخفض جدًا، تشخيصي لـ<bdi>iron deficiency</bdi>"),
    ],
    "why_correct": [
        "طفلة بعمر سنتين تشرب <bdi>3 pints</bdi> حليب بقر يوميًا وأكلها سيء، مع <bdi>MCV 62</bdi>، <bdi>MCH 18</bdi>، <bdi>ferritin 9</bdi> و<bdi>platelets 480</bdi>، هذا <bdi>iron deficiency anemia</bdi>.",
        "حليب البقر فقير بالحديد ويبعّد الأكل الصلب الغني بالحديد وممكن يسبب نزف هضمي خفي بهذا العمر؛ <bdi>ferritin</bdi> المنخفض تشخيصي و<bdi>thrombocytosis</bdi> التفاعلي نموذجي.",
    ],
    "when_changes": [
        "لو كان <bdi>ferritin</bdi> طبيعي أو مرتفع مع <bdi>RBC count</bdi> مرتفع نسبيًا، الجواب يصير <bdi>alpha thalassemia trait</bdi> بدل <bdi>iron deficiency</bdi>.",
    ],
    "rule": "<bdi>Hb</bdi> منخفض + <bdi>MCV</bdi> منخفض + <bdi>ferritin</bdi> منخفض (+ <bdi>platelets</bdi> مرتفع) = <bdi>iron deficiency anemia</bdi>؛ تاريخ العائلة بالإخوة هنا مجرد مشتت.",
    "comparison": None,
    "labs": [
        ["RBC", "3", "4.6-4.8 x10^12/L (child)"],
        ["Hb", "4", "112-165 g/L (child)"],
        ["MCH", "18", "28-33 pg/cell"],
        ["MCV", "62", "80-95 fL"],
        ["Reticulocyte", "3%", "0.2-1.2%"],
        ["Platelets", "480", "150-400 x10^9/L"],
        ["Ferritin", "9", "20-200 µg/L"],
    ],
    "guideline_note": "نفس السيناريو تقريبًا بـ<bdi>AS-2353</bdi> مُسجّل بجواب <bdi>A. Sickle cell disease</bdi> بسبب تفسير مختلف لتاريخ الإخوة؛ هنا نعتمد جواب المصدر المؤكد لهذه النسخة (<bdi>C</bdi>).",
},
"AS-2355": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "نسخة ثالثة من نفس السيناريو، تؤكد <bdi>iron deficiency anemia</bdi> كتشخيص الأرجح استنادًا للتغذية والمختبر.",
    "clues": [
        ("Drinking excessive amounts Of Milk", "سبب رئيسي لـ<bdi>iron deficiency</bdi> بهذا العمر"),
        ("MCV: 62", "<bdi>microcytic anemia</bdi>"),
        ("Ferritin: 9", "منخفض، تشخيصي"),
    ],
    "why_correct": [
        "طفلة عندها <bdi>excessive milk intake</bdi> ورفض الأكل الصلب واللحم، يعني غذاء فقير بالحديد، وحليب البقر بهذا العمر يسبب نزف هضمي خفي ويقلل امتصاص الحديد.",
        "المختبر يؤكد: <bdi>microcytosis</bdi> (<bdi>MCV 62</bdi>)، <bdi>MCH</bdi> منخفض، <bdi>ferritin 9</bdi> (تشخيصي لنقص الحديد)، و<bdi>platelets 480</bdi> (<bdi>reactive thrombocytosis</bdi>). نسبة <bdi>MCV/RBC</bdi> (62/3) أعلى من 13 وهذا يدعم <bdi>IDA</bdi> أكثر من <bdi>thalassemia</bdi>.",
    ],
    "when_changes": [
        "لو <bdi>reticulocytes</bdi> كانت مرتفعة بوضوح مع <bdi>jaundice</bdi> و<bdi>ferritin</bdi> طبيعي، الجواب يميل لـ<bdi>sickle cell disease</bdi>.",
    ],
    "rule": "بـ<bdi>microcytic anemia</bdi> عند طفل، <bdi>ferritin</bdi> هو الفاصل: منخفض = <bdi>iron deficiency</bdi>، طبيعي/مرتفع مع <bdi>RBC</bdi> مرتفع = <bdi>thalassemia trait</bdi>.",
    "comparison": {
        "headers": ["المؤشر", "IDA", "Thalassemia trait"],
        "rows": [
            ["Ferritin", "منخفض", "طبيعي/مرتفع"],
            ["RBC count", "منخفض", "مرتفع نسبيًا"],
        ],
    },
    "labs": [
        ["RBC", "3", "4.6-4.8 x10^12/L (child)"],
        ["Hb", "4", "112-165 g/L (child)"],
        ["MCH", "18", "28-33 pg/cell"],
        ["MCV", "62", "80-95 fL"],
        ["Reticulocyte", "3%", "0.2-1.2%"],
        ["Platelets", "480", "150-400 x10^9/L"],
        ["Ferritin", "9", "20-200 µg/L"],
    ],
    "guideline_note": None,
},
"AS-2356": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "بنت تناولت <bdi>acetaminophen</bdi> بجرعة كبيرة منذ يوم كامل وبدأ عندها ألم بالبطن العلوي الأيمن، والسؤال يبي تحديد <bdi>phase</bdi> التسمم حسب الوقت والعلامات.",
    "clues": [
        ("acetaminophen", "مادة التسمم"),
        ("1 day ago", "مرت تقريبًا 24 ساعة على الابتلاع"),
        ("right upper quadrant abdominal pain", "علامة إصابة الكبد، تحدد <bdi>phase 2</bdi>"),
    ],
    "why_correct": [
        "الابتلاع كان <bdi>1 day ago</bdi> وعندها الآن <bdi>RUQ abdominal pain</bdi>، يعني إصابة كبدية مبكرة.",
        "<bdi>Phase 2</bdi> (تقريبًا 24 إلى 72 ساعة) هي اللي يهدأ فيها الغثيان الأولي ويظهر ألم <bdi>RUQ</bdi> وحساسية الكبد مع ارتفاع <bdi>transaminases</bdi>. لا يوجد <bdi>jaundice</bdi> ولا <bdi>encephalopathy</bdi> ولا <bdi>anuria</bdi>، يعني لسه ما وصلت <bdi>phase 3</bdi>.",
        "هذا يبعد <bdi>phase 1</bdi> أيضًا لأنها كانت أول 24 ساعة فقط بأعراض غير محددة بدون ألم كبدي.",
    ],
    "when_changes": [
        "لو ظهر <bdi>jaundice</bdi> و<bdi>encephalopathy</bdi> و<bdi>coagulopathy</bdi> الجواب يصير <bdi>phase 3</bdi>.",
        "لو كان الابتلاع من ساعات قليلة فقط بدون ألم كبدي، الجواب يصير <bdi>phase 1</bdi>.",
    ],
    "rule": "تحديد <bdi>phase</bdi> تسمم <bdi>acetaminophen</bdi> يعتمد على الوقت + العلامة السريرية: ألم <bdi>RUQ</bdi> بدون <bdi>jaundice</bdi>/<bdi>encephalopathy</bdi> = <bdi>phase 2</bdi>.",
    "comparison": {
        "headers": ["Phase", "الوقت", "العلامات"],
        "rows": [
            ["Phase 1", "0-24h", "غثيان وتقيؤ فقط"],
            ["Phase 2", "24-72h", "ألم RUQ، ارتفاع إنزيمات الكبد"],
            ["Phase 3", "72-96h", "jaundice, encephalopathy, coagulopathy"],
        ],
    },
    "labs": [
        ["Blood pressure", "95/50 mmHg", "طبيعي للعمر"],
        ["Heart rate", "135 /min", "60-100 /min"],
        ["Respiratory rate", "25 /min", "طبيعي للعمر"],
        ["Temperature", "36.6°C", "36.5-37.5°C"],
        ["Oxygen saturation", "95%", "95-100%"],
    ],
    "guideline_note": None,
},
"AS-2357": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "طفل عنده <bdi>cystic fibrosis</bdi> بعمر 10 سنين، والسؤال يبي الطريقة الصحيحة لفحص <bdi>CF related diabetes</bdi> المبكّر.",
    "clues": [
        ("cystic fibrosis", "خطر <bdi>CF related diabetes</bdi> بسبب تلف البنكرياس التدريجي"),
    ],
    "why_correct": [
        "<bdi>CF related diabetes</bdi> ينتج عن تلف تدريجي بخلايا <bdi>pancreas</bdi> وغالبًا يكون صامت بالبداية مع <bdi>fasting glucose</bdi> طبيعي حتى مراحل متأخرة.",
        "الإرشادات توصي بـ<bdi>annual oral glucose tolerance test</bdi> من عمر 10 سنين لكل مرضى <bdi>CF</bdi>، وهذا يطابق عمر هذا الطفل تمامًا.",
        "<bdi>OGTT</bdi> يكشف ارتفاع السكر بعد الحمل الذي يفوته فحص <bdi>fasting</bdi> أو <bdi>random glucose</bdi>.",
    ],
    "when_changes": [
        "لو الطفل عنده أعراض <bdi>classic hyperglycemia</bdi> واضحة مع <bdi>random glucose</bdi> ≥200 mg/dL، يصير التشخيص مباشر بدون انتظار <bdi>OGTT</bdi>.",
    ],
    "rule": "متابعة <bdi>CF related diabetes</bdi> = <bdi>OGTT</bdi> سنوي من عمر 10 سنين، لأن <bdi>fasting glucose</bdi> يبقى طبيعي لمدة طويلة بعد بداية المرض.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2358": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "طفلة عندها حمى طويلة متكررة مع علامات متعددة مخصوصة بالعين والفم واليدين والجلد، نموذج كلاسيكي لتشخيص فيروسي/التهابي معروف يعتمد على معايير سريرية واضحة.",
    "clues": [
        ("fever of 9-day duration", "حمى أطول من 5 أيام، شرط أساسي بالمعيار التشخيصي"),
        ("non-purulent conjunctivitis", "أحد المعايير الأربعة الرئيسية"),
        ("red cracked lips", "علامة مخصوصة بالتشخيص"),
        ("swollen and erythematous hands and feet", "علامة مخصوصة بالتشخيص"),
    ],
    "why_correct": [
        "حمى لمدة <bdi>9 days</bdi> (أكثر من 5) مع أربع علامات رئيسية: <bdi>non-purulent conjunctivitis</bdi>، <bdi>red cracked lips</bdi>، تورم واحمرار اليدين والقدمين، و<bdi>rash</bdi> متعدد الأشكال، تحقق معايير <bdi>Kawasaki disease</bdi>.",
        "<bdi>irritability</bdi> الشديد الزائد عن الحمى نفسها علامة نموذجية أيضًا. الخطوة التالية <bdi>echocardiography</bdi> لتفقّد <bdi>coronary aneurysms</bdi> وعلاج بـ<bdi>IVIG</bdi> مع <bdi>aspirin</bdi>.",
    ],
    "when_changes": [
        "لو كان فيه <bdi>Koplik spots</bdi> مع <bdi>cough</bdi> و<bdi>coryza</bdi>، الجواب يصير <bdi>measles</bdi> بدل <bdi>Kawasaki</bdi>.",
    ],
    "rule": "<bdi>Kawasaki disease</bdi> = حمى ≥5 أيام + 4 من 5 معايير (<bdi>conjunctivitis</bdi>، <bdi>rash</bdi>، <bdi>adenopathy</bdi>، <bdi>cracked lips/strawberry tongue</bdi>، تورم اليدين والقدمين).",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2384": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "طفل بعد زيارة مزرعة عنده توكسيدروم <bdi>cholinergic</bdi> كامل، والسؤال يبي الـ<bdi>antidote</bdi> الصحيح.",
    "clues": [
        ("grandfather's farm", "تعرّض محتمل لمبيدات <bdi>organophosphate</bdi>"),
        ("miosis", "حدقة ضيقة، علامة <bdi>cholinergic toxicity</bdi>"),
        ("lacrimation, salivation", "إفرازات زايدة، جزء من <bdi>DUMBBELSS</bdi>"),
        ("garlic odor", "رائحة مميزة لتسمم <bdi>organophosphate</bdi>"),
    ],
    "why_correct": [
        "طفل من <bdi>farm</bdi> عنده <bdi>diarrhea</bdi>، <bdi>urination</bdi>، <bdi>miosis</bdi>، <bdi>vomiting</bdi>، <bdi>lacrimation</bdi> و<bdi>salivation</bdi>، هذا توكسيدروم <bdi>cholinergic</bdi> (<bdi>DUMBBELSS</bdi>)، و<bdi>garlic odor</bdi> يرجّح تسمم مبيد <bdi>organophosphate</bdi>.",
        "<bdi>organophosphates</bdi> تثبط <bdi>acetylcholinesterase</bdi>، فيُعطى <bdi>atropine</bdi> لإيقاف تأثيرات <bdi>muscarinic</bdi> (يُقاس التحسن بجفاف الإفرازات)، مع <bdi>pralidoxime</bdi> وإزالة التلوث.",
    ],
    "when_changes": [
        "لو كانت الحدقة ضيقة مع تنفس بطيء وجاف بدون إفرازات زايدة، الجواب يصير تسمم <bdi>opioid</bdi> والعلاج <bdi>naloxone</bdi>.",
    ],
    "rule": "حدقة ضيقة + إفرازات زايدة + رائحة ثوم = <bdi>organophosphate poisoning</bdi>؛ العلاج <bdi>atropine</bdi> مع <bdi>pralidoxime</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2387": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طفل عنده <bdi>Koplik spots</bdi> ورشّ بعد حفلة ميلاد، هذا <bdi>measles</bdi>، والسؤال يبي طريقة الانتقال الصحيحة.",
    "clues": [
        ("KOPLIK spots", "علامة مرضية مؤكدة لـ<bdi>measles</bdi>"),
    ],
    "why_correct": [
        "حمى مع <bdi>Koplik spots</bdi> بالفم ورشّ <bdi>maculopapular</bdi> بعد تجمع بـ<bdi>birthday party</bdi> هذا <bdi>measles</bdi>.",
        "فيروس <bdi>measles</bdi> ينتقل بطريقة <bdi>airborne</bdi>: إفرازات الجهاز التنفسي تتحول لجزيئات صغيرة تبقى معلّقة بالهواء، وهذا يفسر انتشاره السريع بالتجمعات.",
    ],
    "when_changes": [
        "لو كان المرض <bdi>rubella</bdi> بدل <bdi>measles</bdi>، طريقة الانتقال تصير <bdi>droplet</bdi> لا <bdi>airborne</bdi>.",
    ],
    "rule": "<bdi>measles</bdi> ينتقل <bdi>airborne</bdi> ويحتاج عزل خاص (غرفة ضغط سلبي، <bdi>N95</bdi>)، عكس أغلب فيروسات الرشّ الأخرى اللي تنتقل <bdi>droplet</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2387B": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "نفس تشخيص <bdi>measles</bdi> مع انتقاله لثلاثة إخوة بالبيت، والسؤال يبي طريقة الانتقال الصحيحة بالاختيارات الأربعة.",
    "clues": [
        ("measles", "فيروس ينتقل بطريقة <bdi>airborne</bdi>"),
    ],
    "why_correct": [
        "انتقال <bdi>measles</bdi> لثلاثة إخوة بنفس البيت يوضح شدة عدواه.",
        "<bdi>measles</bdi> ينتقل بطريقة <bdi>airborne</bdi>: جزيئات صغيرة من الإفرازات التنفسية تبقى معلّقة بالهواء وتصيب أشخاص بنفس الغرفة حتى بعد خروج المريض، وهذا سبب حاجته لعزل <bdi>airborne</bdi> مو فقط <bdi>droplet</bdi>.",
    ],
    "when_changes": [
        "لو كان المرض <bdi>mumps</bdi> أو <bdi>rubella</bdi> أو <bdi>pertussis</bdi>، طريقة الانتقال تصير <bdi>droplet</bdi>.",
    ],
    "rule": "عزل <bdi>airborne</bdi> يحتاجه: <bdi>measles</bdi>، <bdi>varicella</bdi>، <bdi>TB</bdi>؛ لا تخلط <bdi>rubella</bdi> (<bdi>droplet</bdi>) مع <bdi>measles</bdi> (<bdi>airborne</bdi>).",
    "comparison": {
        "headers": ["طريقة الانتقال", "أمثلة"],
        "rows": [
            ["Airborne", "measles, varicella, TB"],
            ["Droplet", "influenza, mumps, rubella, pertussis, meningococcus"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},
"AS-2388": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "صبي بدون أعراض عنده نبض غير منتظم بفحص روتيني، والسؤال يبي التوقع (<bdi>prognosis</bdi>) الصحيح لحالة قلبية حميدة شائعة بهذا العمر.",
    "clues": [
        ("routine paediatrics exam", "فحص روتيني بدون أعراض"),
        ("irregular pulse", "نبض غير منتظم، يحتاج تمييز حميد عن مرضي"),
    ],
    "why_correct": [
        "صبي عمره 14 سنة بدون أعراض بفحص روتيني عنده <bdi>irregular pulse</bdi> مع باقي العلامات الحيوية والفحص طبيعي، هذا على الأغلب <bdi>sinus arrhythmia</bdi>، حيث يزيد معدل القلب مع الشهيق وينخفض مع الزفير.",
        "هذا وضع فسيولوجي حميد بالأطفال والمراهقين، فالتوقع المتوقع هو <bdi>normal development</bdi> بدون علاج.",
    ],
    "when_changes": [
        "لو كان فيه تاريخ <bdi>syncope</bdi> أو علامات <bdi>heart block</bdi> بالـ<bdi>ECG</bdi>، الجواب يصير توقع يحتاج تقييم ومتابعة أعمق مثل <bdi>syncopal episodes</bdi> أو <bdi>pacemaker</bdi>.",
    ],
    "rule": "بدون أعراض + فحص طبيعي + نبض غير منتظم عند طفل = <bdi>sinus arrhythmia</bdi> فسيولوجي، التوقع <bdi>normal development</bdi>.",
    "comparison": None,
    "labs": [
        ["Blood pressure", "115/70 mmHg", "طبيعي للعمر"],
        ["Heart rate", "80 /min", "60-100 /min"],
        ["Respiratory rate", "20 /min", "طبيعي للعمر"],
        ["Oxygen saturation", "95%", "95-100%"],
    ],
    "guideline_note": None,
},
"AS-2390": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "مولود بملامح وجه كلاسيكية لمتلازمة كروموسومية، والسؤال يبي الخطوة التالية الصحيحة للتأكيد.",
    "clues": [
        ("depressed nasal bridge", "ملامح <bdi>Down syndrome</bdi>"),
        ("upward slanting palpebral fissures", "ملامح <bdi>Down syndrome</bdi>"),
        ("epicanthal fold", "ملامح <bdi>Down syndrome</bdi>"),
    ],
    "why_correct": [
        "<bdi>depressed nasal bridge</bdi> و<bdi>upward slanting palpebral fissures</bdi> و<bdi>epicanthal folds</bdi> هي ملامح <bdi>Down syndrome</bdi> الكلاسيكية.",
        "عند وجود ملامح متلازمة كروموسومية بمولود، الخطوة المناسبة التالية هي <bdi>chromosomal analysis</bdi> (<bdi>karyotype</bdi>)، تأكد <bdi>trisomy 21</bdi> وتحدد أشكال <bdi>translocation</bdi> المهمة لاستشارة الوالدين.",
    ],
    "when_changes": [
        "لو كان المولود <bdi>SGA</bdi> مع <bdi>microcephaly</bdi>، <bdi>cataracts</bdi>، <bdi>hepatosplenomegaly</bdi> أو <bdi>petechiae</bdi> بدل ملامح <bdi>Down</bdi>، الجواب يصير <bdi>TORCH screening</bdi>.",
    ],
    "rule": "ملامح وجه كروموسومية = <bdi>karyotype</bdi>؛ <bdi>SGA</bdi> مع إصابة أعضاء (كبد/عين/جلد) = <bdi>TORCH screen</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": "فيه ملاحظة بالمصدر عن سؤال مشابه (<bdi>AS-2235</bdi>) بجواب <bdi>TORCH</bdi>، لكن ذاك السيناريو يحتوي تفاصيل <bdi>SGA</bdi> إضافية تبرر التفرقة؛ هنا نعتمد جواب المصدر المؤكد لهذه النسخة (<bdi>A</bdi>).",
},
"AS-2394": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "طفل عنده ملامح <bdi>Marfan syndrome</bdi> مع ألم صدر متكرر، والسؤال يبي الفحص المناسب لنفي الأسباب القلبية الخطيرة.",
    "clues": [
        ("chest pain", "عرض يحتاج نفي سبب قلبي خطير"),
        ("high status", "قامة طويلة، ملامح <bdi>Marfan</bdi>"),
        ("joints are laxed", "ارتخاء مفاصل، ملامح <bdi>Marfan</bdi>"),
        ("arachnodactyly", "أصابع طويلة نحيفة، ملامح <bdi>Marfan</bdi>"),
    ],
    "why_correct": [
        "قامة طويلة، ارتخاء مفاصل، و<bdi>arachnodactyly</bdi> ترجّح <bdi>Marfan syndrome</bdi>.",
        "أخطر مشاكله القلبية <bdi>aortic root dilation</bdi>، <bdi>aortic dissection</bdi>، و<bdi>mitral valve prolapse</bdi>، فألم الصدر المتكرر يحتاج تقييم بـ<bdi>echocardiography</bdi>، اللي تقيس قطر الجذر الأبهري وتوضح الصمامات.",
    ],
    "when_changes": [
        "لو كانت الحالة غير مستقرة بشكوك <bdi>acute dissection</bdi>، الفحص الطارئ يصير <bdi>CT angiography</bdi> للصدر.",
    ],
    "rule": "<bdi>Marfan syndrome</bdi> + ألم صدر = خوف من <bdi>aortic root disease</bdi>؛ الفحص الأساسي <bdi>echocardiography</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2395": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "رضيع صغير عنده تقيؤ متكرر مع جوع فوري بعده، ومختبر يظهر اضطراب كهارل كلاسيكي، والسؤال يبي التشخيص الصحيح.",
    "clues": [
        ("5-week-old", "العمر النموذجي لـ<bdi>pyloric stenosis</bdi>"),
        ("becomes very hungry and wants to feed again", "تقيؤ غير صفراوي مع جوع، يميز عن أسباب أخرى"),
        ("Potassium 2.9", "<bdi>hypokalemia</bdi>"),
        ("Bicarbonate 32", "<bdi>metabolic alkalosis</bdi>"),
        ("Chloride 89", "<bdi>hypochloremia</bdi>"),
    ],
    "why_correct": [
        "رضيع بعمر <bdi>5 weeks</bdi> عنده تقيؤ متكرر، يصير جوعان فورًا بعد التقيؤ، مع فقدان وزن، ومختبر يظهر <bdi>hypochloremic hypokalemic metabolic alkalosis</bdi>، هذا <bdi>hypertrophic pyloric stenosis</bdi>.",
        "فقدان العصارة المعوية (<bdi>HCl</bdi>) المتكرر يسبب هذا النمط الكهرلي، والعمر النموذجي 2 إلى 8 أسابيع.",
    ],
    "when_changes": [
        "لو كان التقيؤ <bdi>bilious</bdi> مع طفل غير مستقر، الجواب يصير <bdi>intestinal malrotation with volvulus</bdi> كطارئ جراحي.",
    ],
    "rule": "تقيؤ غير صفراوي + جوع بعده + <bdi>hypochloremic hypokalemic alkalosis</bdi> = <bdi>pyloric stenosis</bdi>؛ تقيؤ صفراوي = <bdi>malrotation</bdi> طارئ.",
    "comparison": None,
    "labs": [
        ["Sodium", "147 mmol/L", "134-146 mmol/L"],
        ["Potassium", "2.9 mmol/L", "3.5-5.1 mmol/L"],
        ["Bicarbonate", "32 mmol/L", "21-28 mmol/L"],
        ["Chloride", "89 mmol/L", "97-108 mmol/L"],
    ],
    "guideline_note": None,
},
"AS-2396": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "طفل عنده نوبات قصيرة من فقدان الوعي مع حركات فم، ونتائج <bdi>EEG</bdi> مميزة جدًا، السؤال يبي نوع <bdi>seizure</bdi> الصحيح.",
    "clues": [
        ("sudden abrupt loss of environmental awareness", "فقدان وعي مفاجئ قصير"),
        ("sudden return to normal baseline", "بدون ارتباك بعد النوبة، يميز <bdi>absence</bdi>"),
        ("EEG 3-Hz spikes", "نمط <bdi>EEG</bdi> تشخيصي لـ<bdi>absence seizure</bdi>"),
    ],
    "why_correct": [
        "طفل بعمر 6 سنين مع فقدان وعي قصير مفاجئ، حركات فم (<bdi>lip smacking</bdi>)، وعودة فورية للطبيعي بدون ارتباك بعد النوبة، هذا <bdi>absence seizure</bdi>.",
        "نمط <bdi>3-Hz spike-and-wave</bdi> مع تصوير دماغ طبيعي يأكد <bdi>childhood absence epilepsy</bdi>.",
    ],
    "when_changes": [
        "لو كانت النوبة مرتبطة بحمى بعمر 6 أشهر إلى 5 سنين وطويلة أو بؤرية، الجواب يصير <bdi>complicated febrile seizure</bdi>.",
    ],
    "rule": "عودة فورية بدون ارتباك بعد النوبة + <bdi>EEG</bdi> بنمط <bdi>3-Hz spike-wave</bdi> = <bdi>absence seizure</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2401": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "مولود عنده <bdi>panhypopituitarism</bdi> بنقص عدة هرمونات، والسؤال يبي أولوية التعويض الهرموني الصحيحة.",
    "clues": [
        ("panhypopituitarism", "نقص متعدد بهرمونات الغدة النخامية"),
        ("Cortisol low", "نقص <bdi>cortisol</bdi> يحدد الأولوية العلاجية"),
    ],
    "why_correct": [
        "بحالة <bdi>panhypopituitarism</bdi> مع <bdi>cortisol</bdi> منخفض و<bdi>thyroid hormone</bdi> منخفض، يجب بدء <bdi>hydrocortisone</bdi> أولًا.",
        "<bdi>thyroxine</bdi> يزيد التمثيل الغذائي وإخلاء <bdi>cortisol</bdi>، فإعطاؤه قبل تعويض <bdi>cortisol</bdi> ممكن يسبب <bdi>adrenal crisis</bdi>. نقص <bdi>cortisol</bdi> هو الخطر المباشر على حياة المولود (<bdi>hypoglycemia</bdi>، <bdi>shock</bdi>).",
    ],
    "when_changes": [
        "لو كان <bdi>cortisol</bdi> طبيعي ونقص <bdi>thyroid</bdi> فقط، يصير الترتيب <bdi>thyroxine</bdi> مباشرة بدون قلق من <bdi>adrenal crisis</bdi>.",
    ],
    "rule": "ترتيب تعويض الهرمونات بـ<bdi>hypopituitarism</bdi>: <bdi>glucocorticoid</bdi> أولًا، ثم <bdi>thyroxine</bdi>، ثم <bdi>growth hormone</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2404": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "طفل بتاريخ نوبات <bdi>asthma</bdi> سابقة يحتاج دخول مستشفى، الآن بنوبة حادة شديدة بعد مرض فيروسي، والسؤال يبي العلاج الصحيح.",
    "clues": [
        ("Bilateral Wheeze And Prolonged Expiratory Phase", "علامة انسداد مجرى هوائي سفلي، نموذجي لـ<bdi>asthma</bdi>"),
        ("Similar Attacks Before", "تاريخ نوبات <bdi>asthma</bdi> متكررة"),
        ("Oxygen Saturation: 82 %", "<bdi>hypoxemia</bdi> شديد، يدل على نوبة حادة شديدة"),
    ],
    "why_correct": [
        "طفل بتاريخ نوبات سابقة تحتاج دخول مستشفى، الآن عنده <bdi>bilateral wheeze</bdi>، <bdi>prolonged expiration</bdi>، ضيق شديد، و<bdi>SpO2 82%</bdi> بعد محرض فيروسي، هذا نوبة <bdi>acute severe asthma</bdi>.",
        "العلاج الأساسي <bdi>Ventolin nebulization</bdi> (<bdi>salbutamol</bdi>) مع <bdi>systemic corticosteroid</bdi>، بالإضافة للأكسجين لتصحيح <bdi>hypoxemia</bdi>.",
    ],
    "when_changes": [
        "لو كان الطفل مصحوب بحمى واضحة وعلامات <bdi>pneumonia</bdi> بكتيرية مؤكدة، يُضاف <bdi>antibiotic</bdi> للعلاج.",
    ],
    "rule": "نوبة <bdi>asthma</bdi> حادة = <bdi>bronchodilator</bdi> + <bdi>systemic steroid</bdi>؛ <bdi>antibiotics</bdi> مو جزء من العلاج القياسي بدون دليل بكتيري.",
    "comparison": None,
    "labs": [
        ["Blood pressure", "100/65 mmHg", "طبيعي للعمر"],
        ["Heart rate", "124 /min", "80-120 /min"],
        ["Respiratory rate", "33 /min", "20-30 /min"],
        ["Oxygen saturation", "82%", "94-98%"],
    ],
    "guideline_note": None,
},
"AS-2405": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "طفل عنده أعراض فشل قلب بعد مرض فيروسي بأسابيع، والسؤال يبي الفحص التشخيصي الأهم لتقييم وظيفة القلب.",
    "clues": [
        ("new-onset exertional dyspnea and palpitations", "أعراض فشل قلب جديدة"),
        ("viral URI 3 weeks ago", "محرض سابق لـ<bdi>myocarditis</bdi>"),
        ("gallop rhythm", "علامة فشل قلب بالفحص"),
    ],
    "why_correct": [
        "ضيق تنفس جهدي جديد، خفقان، تسرع قلب، وتسرع تنفس مع <bdi>gallop rhythm</bdi> بعد <bdi>viral URI</bdi> قبل 3 أسابيع يرجّح <bdi>viral myocarditis</bdi> بفشل قلب.",
        "<bdi>echocardiography</bdi> هي الفحص الأهم: تُظهر توسّع البطين وضعف الوظيفة الانقباضية واضطراب حركة الجدار والانصباب، وتستبعد مرض قلب بنيوي.",
    ],
    "when_changes": [
        "لو كان الهدف تحديد الفيروس المسبب لا تقييم القلب، يُضاف <bdi>viral serology</bdi>، لكنه لا يؤكد <bdi>myocarditis</bdi> ولا يوجّه العلاج الفوري.",
    ],
    "rule": "طفل بعد مرض فيروسي مع <bdi>gallop</bdi> وتضخم قلب = <bdi>myocarditis</bdi>؛ الفحص الأول <bdi>echocardiography</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2406": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "مولود عمره يومين عنده نزف ومفاصل مصابة، والمختبر يحدد المسار الداخلي للتخثر، والسؤال يبي السبب الأرجح.",
    "clues": [
        ("2 days old", "عمر مبكر، يحتاج استبعاد نقص فيتامين K"),
        ("hemarthrosis", "علامة مميزة لنزف بالمفاصل بسبب نقص عامل تخثر"),
        ("Prolonged PTT, Normal PT", "يحدد الخلل بالمسار الداخلي (<bdi>intrinsic pathway</bdi>)"),
    ],
    "why_correct": [
        "<bdi>PTT</bdi> مطوّل مع <bdi>PT</bdi> طبيعي يحدد الخلل بالمسار الداخلي (<bdi>factors VIII, IX, XI, XII</bdi>)، و<bdi>hemarthrosis</bdi> هي علامة النزف المميزة لـ<bdi>hemophilia</bdi>. نقص <bdi>factor VIII</bdi> (<bdi>hemophilia A</bdi>) هو الأشيع.",
        "عدم وجود تاريخ عائلي لا يستبعد التشخيص لأن نسبة كبيرة من الحالات تنتج عن طفرة جديدة.",
    ],
    "when_changes": [
        "لو كان <bdi>PT</bdi> و<bdi>PTT</bdi> كلاهما مطوّلين، الجواب يصير سبب بالمسار المشترك مثل نقص فيتامين K أو مرض كبد.",
        "لو كانت الصفائح منخفضة مع <bdi>PT/PTT</bdi> طبيعي، الجواب يصير <bdi>ITP</bdi>.",
    ],
    "rule": "<bdi>PTT</bdi> مطوّل منفرد مع <bdi>PT</bdi> طبيعي + نزف مفاصل = <bdi>hemophilia</bdi>؛ غياب تاريخ عائلي لا يستبعده.",
    "comparison": {
        "headers": ["النمط", "السبب المرجّح"],
        "rows": [
            ["PTT مطوّل منفرد", "Factor VIII/IX/XI/XII deficiency"],
            ["PT و PTT مطوّلان معًا", "Vitamin K deficiency, liver disease, DIC"],
            ["صفائح منخفضة، PT/PTT طبيعي", "ITP"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},
"AS-2412": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "طفلة بـ<bdi>sickle cell</bdi> موجب عندها تضخم طحال مفاجئ وأنيميا شديدة وصدمة سريعة خلال ساعات، والسؤال يبي نوع الأزمة الصحيح.",
    "clues": [
        ("pale", "شحوب حاد، علامة أنيميا شديدة"),
        ("spleen is 6 cm below the costal margin", "تضخم طحال حاد، مفتاح تشخيص <bdi>sequestration crisis</bdi>"),
        ("Hb: 52 g/L", "أنيميا شديدة"),
        ("Sickle cell screen: Positive", "يؤكد خلفية <bdi>sickle cell disease</bdi>"),
    ],
    "why_correct": [
        "طفلة موجبة لـ<bdi>sickle cell</bdi> مع تضخم طحال حاد (6 سم) وأنيميا شديدة (<bdi>Hb 52</bdi>) وصدمة (<bdi>HR 169</bdi>, <bdi>BP 93/55</bdi>) خلال 10 ساعات فقط، هذا <bdi>splenic sequestration</bdi>: الدم يتجمع بسرعة بالطحال.",
        "نقص الصفائح الخفيف يعكس احتجاز الصفائح بالطحال أيضًا، وتضخم الطحال المفاجئ مع الشحوب هو المفتاح الحاسم.",
    ],
    "when_changes": [
        "لو كان الطحال بحجم طبيعي مع <bdi>reticulocytes</bdi> منخفض جدًا، الجواب يصير <bdi>aplastic crisis</bdi> (<bdi>parvovirus B19</bdi>).",
        "لو كانت الحمى مرتفعة وواضحة مع علامات صدمة إنتانية بدون تضخم طحال مفاجئ، الجواب يصير <bdi>bacterial sepsis</bdi>.",
    ],
    "rule": "طفل <bdi>sickle cell</bdi> شاحب مع طحال كبير = <bdi>sequestration crisis</bdi>؛ شاحب مع طحال طبيعي و<bdi>reticulocytes</bdi> منخفض = <bdi>aplastic crisis</bdi>.",
    "comparison": None,
    "labs": [
        ["Hb", "52 g/L", "112-165 g/L"],
        ["Platelets", "102 x10^9/L", "150-400 x10^9/L"],
        ["Blood pressure", "93/55 mmHg", "طبيعي للعمر"],
        ["Heart rate", "169 /min", "80-120 /min"],
    ],
    "guideline_note": None,
},
"AS-2416": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طفلة عندها ضعف تركيز وفرط حركة، لكن السبب الظاهر هو حرمان نوم شديد، والسؤال يبي الخطوة الأولى الصحيحة قبل التفكير بـ<bdi>ADHD</bdi>.",
    "clues": [
        ("poor concentration and hyperactivity at school", "عرض قد يكون نتيجة حرمان نوم، لا <bdi>ADHD</bdi> بالضرورة"),
        ("only sleeps 5 hours per night from 1 AM to 6 AM", "حرمان نوم شديد، السبب الأرجح للأعراض"),
    ],
    "why_correct": [
        "طفلة عمرها 8 سنين تنام فقط <bdi>5 hours</bdi> (من 1 صباحًا إلى 6 صباحًا) تعتبر محرومة من النوم بشدة، وبالأطفال الحرمان من النوم يظهر كـ<bdi>hyperactivity</bdi> وضعف تركيز بدل النعاس.",
        "الخطوة الأولى المناسبة هي تصحيح السبب بتدابير سلوكية: وقت نوم ثابت، روتين تهيئة قبل النوم، وتجنب الشاشات. لو استمرت الأعراض بعد تصحيح النوم، يُقيّم <bdi>ADHD</bdi> رسميًا.",
    ],
    "when_changes": [
        "لو استمرت الأعراض رغم روتين نوم منظّم لأشهر، الخطوة تصير تقييم <bdi>ADHD</bdi> رسمي.",
        "لو كان فيه شخير وانقطاع تنفس بالنوم، يُفكر بـ<bdi>obstructive sleep apnea</bdi>.",
    ],
    "rule": "ضعف تركيز وفرط حركة عند طفل: استبعد أسباب قابلة للإصلاح (مثل حرمان النوم) قبل تسميتها <bdi>ADHD</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2418": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "طفل عنده تاريخ اختناق بعد أكل بذور، وأصوات تنفس منخفضة بجهة واحدة، والسؤال يبي الخطوة التالية الحاسمة.",
    "clues": [
        ("hx of choking after he ingested some seed", "تاريخ اختناق يرجّح <bdi>foreign body aspiration</bdi>"),
        ("dec RT side breathing sound", "علامة انسداد موضعي بجهة واحدة"),
    ],
    "why_correct": [
        "نوبة اختناق أثناء أكل بذور متبوعة بانخفاض أصوات التنفس بالجهة اليمنى هي <bdi>foreign body aspiration</bdi> لحد يثبت العكس؛ الحمى والسعال يشيرون لعدوى تتطور خلف الانسداد.",
        "الخطوة التالية <bdi>bronchoscopy</bdi> (<bdi>rigid</bdi> بالأطفال)، تؤكد التشخيص وتزيل الجسم الغريب معًا. المضادات أو العلاج الداعم وحدها لن تنجح مع وجود البذرة.",
    ],
    "when_changes": [
        "لو كان الانسداد كامل مع ضيق شديد فوري، الخطوة الأولى تصير إسعافية (<bdi>back blows</bdi> أو <bdi>abdominal thrusts</bdi>) قبل <bdi>bronchoscopy</bdi>.",
    ],
    "rule": "تاريخ اختناق موثّق + علامات بجهة واحدة = <bdi>bronchoscopy</bdi>، حتى لو كانت صورة الصدر تبدو طبيعية.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
}

WHY_WRONG = {
"AS-2300": {
    "A": "<bdi>Marfan syndrome</bdi> يعطي قوام طويل نحيف مع <bdi>arachnodactyly</bdi> و<bdi>ectopia lentis</bdi> و<bdi>aortic root dilation</bdi>، ولا يسبب <bdi>webbed neck</bdi> ولا خصية غير نازلة.",
},
"AS-2310": {
    "B": "<bdi>Hirschsprung disease</bdi> تبدأ بالمرحلة الوليدية بتأخر خروج <bdi>meconium</bdi> (أكثر من 24-48 ساعة)، انتفاخ، تقيؤ صفراوي، و<bdi>rectum</bdi> فاضي مع <bdi>squirt sign</bdi>؛ <bdi>soiling</bdi> نادر لأن الجزء المصاب يحافظ على <bdi>rectum</bdi> فاضي.",
},
"AS-2311": {
    "B": "<bdi>Galactosemia</bdi> تظهر بالأيام الأولى من العمر بمجرد بدء الرضاعة لأن حليب الأم يحتوي <bdi>lactose</bdi>؛ طفل تحمّل الرضاعة الطبيعية كويس لأشهر مستبعد.",
    "C": "<bdi>Gluten sensitivity</bdi> (<bdi>celiac disease</bdi>) يتبع إدخال حبوب القمح ويسبب <bdi>chronic diarrhea</bdi> وانتفاخ و<bdi>failure to thrive</bdi>، مو تقيؤ حاد مع <bdi>jaundice</bdi> بعد الفاكهة.",
},
"AS-2319": {
    "A": "<bdi>atopic dermatitis</bdi> جزء من <bdi>atopic march</bdi> ويرفع احتمال <bdi>asthma</bdi>، لكنه عنصر تاريخ مرضي، مو دليل موضوعي.",
    "C": "التاريخ العائلي لـ<bdi>asthma</bdi> عامل خطر يدعم التشخيص؛ هو تاريخ شخصي ولا يثبت وجود مرض بالمجرى التنفسي بهذا الطفل.",
    "D": "السعال الليلي عرض نمطي لـ<bdi>asthma</bdi> (وضعف السيطرة)، لكن الأعراض ذاتية ومشتركة مع أسباب سعال مزمن أخرى.",
},
"AS-2329": {
    "A": "<bdi>lead screening</bdi> منطقي عند طفل عنده <bdi>pica</bdi>، وممكن يتزامن التسمم بالرصاص مع نقص الحديد، لكن الشحوب وزيادة الحليب يستدعون أولًا تأكيد وتوصيف <bdi>anemia</bdi>.",
    "C": "<bdi>ophthalmology consultation</bdi> ليس له دور؛ <bdi>pale conjunctiva</bdi> علامة على <bdi>anemia</bdi>، مو مرض بالعين.",
    "D": "<bdi>ferritin</bdi> فحص ثاني مفيد يأكد انخفاض مخزون الحديد، لكنه وحده لا يوضح وجود <bdi>anemia</bdi> أو شدته؛ الـ<bdi>CBC</bdi> يأتي أولًا.",
},
"AS-2337": {
    "A": "<bdi>nephritic syndrome</bdi> (مثل <bdi>post-infectious GN</bdi>) يعطي <bdi>hematuria</bdi> و<bdi>hypertension</bdi> و<bdi>oliguria</bdi> مع <bdi>proteinuria</bdi> خفيف فقط؛ هنا <bdi>BP</bdi> طبيعي والألبومين منخفض جدًا، وهذا يطابق <bdi>nephrotic</bdi>.",
    "C": "<bdi>hereditary angioedema</bdi> يسبب تورم غير حاكّ بالوجه أو الشفاه أو المجرى التنفسي بنوبات متقطعة مع <bdi>albumin</bdi> طبيعي وبدون <bdi>proteinuria</bdi>.",
    "D": "<bdi>protein losing enteropathy</bdi> يسبب أيضًا <bdi>hypoalbuminemia</bdi> وتورم، لكن فقدان البروتين من الأمعاء، فالبول يكون سليم من البروتين؛ <bdi>proteinuria</bdi> 4+ يشير للكلى.",
},
"AS-2344": {
    "A": "<bdi>high risk</bdi> ينطبق فقط لو كان الوالدين الاثنين حاملين مؤكدين (خطر 1 من 4 لكل حمل)؛ هنا فقط الأب مؤكد حامل.",
    "B": "<bdi>no risk</bdi> لا يمكن إثباته قبل فحص الأم؛ شريك غير مفحوص ممكن يكون حامل صامت للجين.",
    "C": "النصيحة بعدم إنجاب أطفال غير مناسبة بالاستشارة الوراثية، وحتى لو كان الوالدين حاملين، الدور هو تقديم المعلومات والخيارات، مو منع الحمل.",
},
"AS-2351": {
    "B": "<bdi>Liver HIDA scan</bdi> يقيّم إفراز العصارة الصفراوية (<bdi>biliary atresia</bdi>، <bdi>cholecystitis</bdi>) ولا يشخص مرض تخزين النحاس.",
    "C": "<bdi>bone marrow aspiration</bdi> يُستخدم للشك بـ<bdi>leukemia</bdi> أو فشل نقي العظم؛ ارتفاع <bdi>reticulocytes</bdi> هنا يدل على نقي عظم متفاعل بسبب التكسّر.",
    "D": "<bdi>24h urine copper</bdi> هو الفحص العملي والداعم الأشيع لـ<bdi>Wilson disease</bdi>، لكنه ليس <bdi>gold standard</bdi>؛ ذاك هو النحاس بـ<bdi>liver biopsy</bdi>.",
},
"AS-2352": {
    "A": "<bdi>liver biopsy</bdi> مع قياس النحاس هو <bdi>gold standard</bdi>، لكنه إجراء تداخلي يُحجز لما تكون الفحوصات غير التداخلية غير كافية؛ ليس الفحص الأول المناسب.",
    "B": "<bdi>HIDA scan</bdi> يقيّم تصريف العصارة الصفراوية (<bdi>biliary atresia</bdi>، <bdi>cholecystitis</bdi>) وليس له دور بمرض تخزين النحاس.",
    "C": "<bdi>bone marrow aspiration</bdi> يُستخدم لـ<bdi>leukemia</bdi> أو فشل نقي العظم؛ ارتفاع <bdi>reticulocytes</bdi> هنا يدل على نقي عظم متفاعل مع التكسّر.",
},
"AS-2353": {
    "B": "<bdi>alpha thalassemia trait</bdi> يعطي <bdi>anemia</bdi> خفيف فقط مع <bdi>RBC count</bdi> طبيعي أو مرتفع و<bdi>ferritin</bdi> طبيعي؛ <bdi>Hb</bdi> هذا المنخفض مع <bdi>ferritin 9</bdi> لا يطابق سمة <bdi>trait</bdi>.",
    "C": "<bdi>iron deficiency</bdi> يطابق عادات الحليب الزائد ورفض اللحم و<bdi>MCV 62</bdi> و<bdi>ferritin 9</bdi> و<bdi>platelets 480</bdi>، لكن مفتاح هذه النسخة بالمصدر يعطي أهمية أكبر لتاريخ الإخوة المصابين، نمط عائلي لا يفسره سبب غذائي.",
    "D": "<bdi>anemia of chronic disease</bdi> يحتاج مرض التهابي مزمن كامن، غير مذكور هنا، و<bdi>ferritin</bdi> فيها يكون طبيعي أو مرتفع بدل 9.",
},
"AS-2354": {
    "A": "<bdi>sickle cell disease</bdi> تسبب <bdi>normocytic hemolytic anemia</bdi> مع <bdi>ferritin</bdi> طبيعي أو مرتفع؛ تاريخ الإخوة هنا مجرد مشتت، والتشخيص يحتاج <bdi>Hb electrophoresis</bdi> لا تاريخ غذائي.",
    "B": "<bdi>alpha thalassemia trait</bdi> يعطي <bdi>anemia</bdi> خفيف مع <bdi>RBC count</bdi> مرتفع نسبيًا و<bdi>ferritin</bdi> طبيعي أو مرتفع؛ <bdi>ferritin 9</bdi> و<bdi>Hb</bdi> هذا المنخفض يرجّحان <bdi>iron deficiency</bdi> بدلًا.",
    "D": "<bdi>anemia of chronic disease</bdi> يحتاج مرض التهابي مزمن كامن مع <bdi>ferritin</bdi> طبيعي أو مرتفع، عادة بصفات <bdi>normocytic</bdi>.",
},
"AS-2355": {
    "A": "<bdi>sickle cell disease</bdi> تسبب <bdi>anemia</bdi> <bdi>normocytic</bdi> تكسّري مع <bdi>reticulocytes</bdi> مرتفع بوضوح و<bdi>jaundice</bdi> و<bdi>ferritin</bdi> طبيعي أو مرتفع؛ لا تعطي <bdi>MCV 62</bdi> مع <bdi>ferritin 9</bdi>. تاريخ الإخوة هنا مجرد مشتت نحو <bdi>hemoglobinopathy</bdi>.",
    "B": "<bdi>alpha thalassemia trait</bdi> <bdi>microcytic</bdi> لكن <bdi>anemia</bdi> خفيف، <bdi>RBC count</bdi> مرتفع، <bdi>ferritin</bdi> طبيعي؛ يطابق طفل <bdi>MCV</bdi> منخفض مع <bdi>Hb</bdi> قريب من الطبيعي وفحوصات حديد طبيعية.",
    "D": "<bdi>anemia of chronic disease</bdi> يحتاج مرض التهابي مزمن كامن، <bdi>ferritin</bdi> فيه طبيعي أو مرتفع مع <bdi>TIBC</bdi> منخفض عند طفل مريض مزمن.",
},
"AS-2356": {
    "A": "<bdi>phase 1</bdi> هي أول 24 ساعة فقط: غثيان وتقيؤ وتوعك مع تحاليل طبيعية؛ ظهور ألم <bdi>RUQ</bdi> يدل على الانتقال لـ<bdi>phase 2</bdi>.",
    "C": "<bdi>phase 3</bdi> (حوالي 72-96 ساعة) هي فشل كبدي حاد: <bdi>jaundice</bdi>، <bdi>encephalopathy</bdi>، <bdi>coagulopathy</bdi>، حموضة ميتابوليك، <bdi>anuria</bdi>؛ لا شيء من هذا موجود هنا.",
    "D": "<bdi>phase 4</bdi> (من يوم 4 تقريبًا إلى أسبوعين) إما تعافي مع تحسن التحاليل أو تطور لفشل أعضاء متعدد ووفاة.",
},
"AS-2357": {
    "B": "<bdi>fasting glucose</bdi> غير حساس بـ<bdi>CF</bdi> لأن المرحلة المبكرة من <bdi>CF related diabetes</bdi> تظهر بارتفاع السكر بعد الأكل مع <bdi>fasting</bdi> طبيعي؛ هو الفحص المعتاد بمجموعات خطر <bdi>type 2 diabetes</bdi>، مو <bdi>CF</bdi>.",
    "C": "الانتظار لعمر 18 يفوّت سنوات من <bdi>diabetes</bdi> غير مكشوف؛ الفحص يبدأ من عمر 10.",
    "D": "<bdi>random glucose</bdi> ليس فحص فرز؛ يشخص <bdi>diabetes</bdi> فقط إذا كان ≥200 mg/dL مع أعراض كلاسيكية.",
},
"AS-2358": {
    "A": "<bdi>EBV mononucleosis</bdi> يعطي <bdi>exudative pharyngitis</bdi> و<bdi>generalized lymphadenopathy</bdi> و<bdi>splenomegaly</bdi> و<bdi>atypical lymphocytes</bdi>، لا شفاه متشققة مع تورم احمرار اليدين والقدمين.",
    "C": "<bdi>rubella</bdi> خفيفة بحمى منخفضة ورشّ من الرأس للأسفل وعقد خلف الأذن تدوم تقريبًا 3 أيام، لا 9 أيام من حمى عالية.",
    "D": "<bdi>measles</bdi> فيها <bdi>cough</bdi> و<bdi>coryza</bdi> و<bdi>conjunctivitis</bdi> مع <bdi>Koplik spots</bdi> ورشّ من الرأس للأسفل؛ لا تسبب تورم الأطراف ولا شفاه متشققة.",
},
"AS-2384": {
    "B": "<bdi>N-acetylcysteine</bdi> هو ترياق تسمم <bdi>paracetamol</bdi>، اللي يسبب غثيان وألم <bdi>RUQ</bdi> مع إصابة كبدية، مو توكسيدروم <bdi>cholinergic</bdi>.",
    "C": "<bdi>flumazenil</bdi> يعكس تأثير <bdi>benzodiazepines</bdi> (نعاس، حدقة طبيعية، إفرازات قليلة)؛ يُتجنب بالتسمم المختلط لأنه يسبب تشنجات.",
    "D": "<bdi>sodium bicarbonate</bdi> يعالج تسمم <bdi>tricyclic antidepressant</bdi> (<bdi>wide QRS</bdi>، اضطراب نظم) وتسمم <bdi>salicylate</bdi>؛ لا دور له بفرط <bdi>cholinergic</bdi>.",
},
"AS-2387": {
    "A": "الأسطح الملوثة (<bdi>fomites</bdi>) مهمة بكائنات مثل <bdi>norovirus</bdi> أو <bdi>RSV</bdi> أو <bdi>MRSA</bdi>؛ ليست الطريقة الأساسية لـ<bdi>measles</bdi>.",
    "B": "الطعام والشراب الملوث هو مسار <bdi>fecal-oral</bdi> (<bdi>hepatitis A</bdi>، <bdi>typhoid</bdi>)، مو <bdi>measles</bdi>.",
    "D": "هذا الخيار لم يُسجّل بالمصدر؛ أي طريقة انتقال غير <bdi>airborne</bdi> لا تطابق <bdi>measles</bdi>.",
},
"AS-2387B": {
    "B": "انتقال <bdi>droplet</bdi> (جزيئات كبيرة، ضمن 1-2 متر) يطابق <bdi>influenza</bdi>، <bdi>mumps</bdi>، <bdi>rubella</bdi>، <bdi>pertussis</bdi>، <bdi>meningococcus</bdi>؛ <bdi>measles</bdi> كلاسيكيًا <bdi>airborne</bdi>.",
    "C": "<bdi>fecal-oral</bdi> يطابق <bdi>hepatitis A/E</bdi>، <bdi>enteroviruses</bdi>، <bdi>rotavirus</bdi>، مو <bdi>measles</bdi>.",
    "D": "<bdi>bloodborne</bdi> يطابق <bdi>hepatitis B/C</bdi> و<bdi>HIV</bdi>، لا تسبب تفشي رشّ بنفس البيت كهذا.",
},
"AS-2388": {
    "A": "<bdi>syncopal episodes</bdi> متوقعة مع اضطراب نظم مرضي (مثل <bdi>heart block</bdi> أو <bdi>long QT</bdi>)؛ هذا الصبي بدون تاريخ مرض أو أعراض.",
    "B": "<bdi>pacemaker</bdi> لحالات <bdi>bradyarrhythmia</bdi> عرضية مثل <bdi>complete heart block</bdi>، مو لتغيّر نبض فسيولوجي حميد بالتنفس.",
    "D": "<bdi>myocardial dysfunction</bdi> تأتي مع أعراض أو علامات فشل قلب أو <bdi>cardiomyopathy</bdi>، غير موجودة هنا.",
},
"AS-2390": {
    "B": "<bdi>metabolic screening</bdi> يطابق مولود يصبح مريض بعد الرضاعة (خمول، تقيؤ، حموضة، نقص سكر)؛ الملامح الوجهية هنا تشير لسبب كروموسومي.",
    "C": "<bdi>TORCH screening</bdi> يطابق <bdi>SGA</bdi> مع <bdi>microcephaly</bdi>، <bdi>cataracts</bdi>، <bdi>hepatosplenomegaly</bdi>، <bdi>petechiae</bdi> أو <bdi>chorioretinitis</bdi>؛ وزن <bdi>SGA</bdi> وحده لا يفسر هذا الوجه بالـ<bdi>Down syndrome</bdi>.",
    "D": "<bdi>skeletal survey</bdi> لحالات الشك بـ<bdi>skeletal dysplasia</bdi> أو إصابة غير حادثة، مو لملامح <bdi>Down syndrome</bdi>.",
},
"AS-2394": {
    "A": "<bdi>ECG</bdi> مفيد للنقص التروية أو اضطراب النظم لكنه لا يقيس الجذر الأبهري ولا يُظهر <bdi>dissection</bdi>، وهو الخطر بـ<bdi>Marfan syndrome</bdi>.",
    "B": "<bdi>MRI brain</bdi> غير مرتبط بألم الصدر؛ يُستخدم للصداع أو علامات عصبية.",
    "C": "<bdi>CT chest</bdi> (<bdi>CT angiography</bdi>) يُستخدم لشك <bdi>acute dissection</bdi> بمريض غير مستقر، لكن <bdi>echocardiography</bdi> هو الفحص القياسي الأول لمرض الجذر الأبهري بطفل بملامح <bdi>Marfan</bdi>.",
},
"AS-2395": {
    "A": "<bdi>gastric volvulus</bdi> يظهر بشكل حاد بتقيؤ شديد وانتفاخ معدة وعدم القدرة على إدخال أنبوب أنفي معدي، مو أسابيع تقيؤ برضيع جوعان طبيعي.",
    "B": "<bdi>cyclic vomiting syndrome</bdi> يصيب أطفال أكبر بنوبات نمطية وفواصل سليمة؛ لا يسبب هذا النمط الكهرلي برضيع عمره 5 أسابيع.",
    "D": "<bdi>malrotation with volvulus</bdi> يسبب تقيؤ <bdi>bilious</bdi> وهو طارئ جراحي برضيع غير طبيعي الحال، مو تقيؤ غير صفراوي برضيع جوعان.",
},
"AS-2396": {
    "A": "<bdi>complicated febrile seizure</bdi> يحتاج حمى (عمر 6 أشهر-5 سنين) وتكون بؤرية أو طويلة (أكثر من 15 دقيقة) أو تتكرر خلال 24 ساعة؛ لا توجد حمى هنا.",
    "C": "<bdi>infantile spasms</bdi> تحدث برضع (عادة أقل من سنة) كحركات انثناء أو بسط مع <bdi>hypsarrhythmia</bdi> بالـ<bdi>EEG</bdi>، مو <bdi>3-Hz spikes</bdi>.",
    "D": "<bdi>cerebral palsy</bdi> اضطراب حركي غير تقدمي مع تغيّر توتر وتأخر مراحل نمو، مو نوبات متقطعة من فقدان وعي.",
},
"AS-2401": {
    "B": "<bdi>thyroxine</bdi> مطلوب، لكن بعد بدء تعويض <bdi>glucocorticoid</bdi>؛ إعطاؤه أولًا ممكن يسبب <bdi>adrenal crisis</bdi>.",
    "C": "<bdi>growth hormone</bdi> مطلوب، لكنه ليس الأولوية الطارئة؛ نقص <bdi>cortisol</bdi> غير المعالج يقتل، نقص <bdi>GH</bdi> لا يقتل بالمدى القصير.",
    "D": "الانتظار شهر غير آمن: التشخيص مؤكد والمولود يحتاج تعويض الآن لتجنب نقص سكر و<bdi>adrenal crisis</bdi> وتلف دماغي من نقص الغدة الدرقية.",
},
"AS-2404": {
    "A": "<bdi>antibiotics</bdi> غير مناسبة: المحرض فيروسي والطفل بدون حمى؛ وهذا الخيار يحذف <bdi>bronchodilator</bdi> الدواء الأهم.",
    "B": "<bdi>antibiotics</bdi> لا تضيف شيء بنوبة <bdi>asthma</bdi> فيروسية و<bdi>systemic steroid</bdi> مفقود؛ المضادات فقط لعدوى بكتيرية مؤكدة.",
    "C": "<bdi>IV fluids</bdi> ليست جزء قياسي من علاج <bdi>asthma</bdi> إلا لو كان الطفل مجفف، وهذا الخيار يحذف <bdi>systemic steroid</bdi>.",
},
"AS-2405": {
    "B": "<bdi>ECG</bdi> مساعد (تسرع جيبي، <bdi>low voltage</bdi>، تغيرات <bdi>ST-T</bdi>) لكنه غير نوعي ولا يقيّم وظيفة البطين.",
    "C": "<bdi>viral serology</bdi> ممكن يحدد الفيروس لكنه لا يؤكد <bdi>myocarditis</bdi> ولا يوجّه العلاج الفوري؛ الفيروس كثيرًا لا يُكتشف.",
},
"AS-2406": {
    "B": "<bdi>ITP</bdi> مشكلة بالصفائح: تسبب <bdi>petechiae</bdi> و<bdi>purpura</bdi> ونزف الأغشية مع صفائح منخفضة و<bdi>PT/PTT</bdi> طبيعي؛ نزف المفاصل و<bdi>PTT</bdi> غير طبيعي لا يطابقان.",
    "C": "نص الخيار غير مكتمل بالمصدر؛ اضطرابات الصفائح المتلازمية تسبب نزف جلدي-غشائي مع زمن تخثر طبيعي، فلا تفسر <bdi>PTT</bdi> مطوّل منفرد مع نزف مفاصل.",
    "D": "مرض الكبد يخفض عدة عوامل من ضمنها <bdi>factor VII</bdi>، فيطوّل <bdi>PT</bdi> مبكرًا؛ <bdi>PT</bdi> الطبيعي هنا يستبعده بقوة، وهو غير متوقع عند مولود سليم عمره يومين.",
},
"AS-2412": {
    "B": "<bdi>Evans syndrome</bdi> هو أنيميا انحلالية مناعية مع نقص صفائح مناعي (<bdi>Coombs</bdi> موجب)؛ لا يسبب تضخم طحال ضخم مع صدمة نقص حجم عند طفل <bdi>sickle cell</bdi>.",
    "C": "<bdi>sepsis</bdi> خطر حقيقي بـ<bdi>sickle cell</bdi> (ضعف وظيفة الطحال)، لكن الحرارة هنا فقط 37.5°C، والإنتان لا يفسر تضخم طحال مفاجئ مع انخفاض حاد بالـ<bdi>Hb</bdi>.",
    "D": "<bdi>aplastic crisis</bdi> (<bdi>parvovirus B19</bdi>) يسبب أنيميا شديدة مع <bdi>reticulocytes</bdi> منخفض جدًا <b>بدون</b> تضخم طحال؛ يُختار عندما يكون الطحال بحجم طبيعي.",
},
"AS-2416": {
    "A": "<bdi>melatonin</bdi> ليس خط أول؛ يُنظر فيه فقط بعد فشل التدابير السلوكية بالنوم.",
    "B": "لا شيء بالتاريخ يرجّح اضطراب عصبي (لا تشنجات ولا تراجع ولا علامات بؤرية)؛ السبب الواضح القابل للإصلاح هو نمط النوم.",
    "D": "نقص الحديد ممكن يساهم بضعف تركيز أو نوم مضطرب، لكن لا شحوب ولا دليل آخر هنا؛ فحص الأنيميا ليس الخطوة الأولى الأنسب مع حرمان نوم واضح موثّق.",
},
"AS-2418": {
    "A": "<bdi>epinephrine</bdi> لعلاج <bdi>anaphylaxis</bdi> (<bdi>urticaria</bdi>، <bdi>angioedema</bdi>، انخفاض ضغط) أو <bdi>croup</bdi> الشديد بشكل مستنشق؛ لا يفيد انسداد مجرى هوائي ميكانيكي.",
    "C": "التعامل مع هذا كـ<bdi>URTI</bdi> بسيط يفوّت الجسم الغريب ويعرّض لـ<bdi>pneumonia</bdi> متكرر أو انخماص رئة أو <bdi>bronchiectasis</bdi>؛ تاريخ الاختناق والعلامات بجهة واحدة تحتم الإزالة.",
    "D": "الوصول الوريدي والسوائل والمضادات ممكن تكون جزء من الرعاية الداعمة، لكنها ليست الخطوة التالية الحاسمة؛ لازم إزالة الانسداد.",
},
}

HIGHLIGHT_TERMS = {
"AS-2300": ["cryptorchidism", "low lying epicanthal folds", "nuchal skin"],
"AS-2310": ["Fecal soiling"],
"AS-2311": ["7-month-old", "Symptoms began after the introduction of fruits and fruit juices"],
"AS-2319": ["objective evidence"],
"AS-2329": ["drinks 1 litter of milk daily", "eats dirt", "pale conjunctiva"],
"AS-2337": ["eye puffiness", "Albumin 16", "Protein +4"],
"AS-2344": ["SC trait", "woman didn't test yet"],
"AS-2351": ["progressive jaundice and mild tremors", "decreased school performance", "gold standard"],
"AS-2352": ["progressive jaundice and mild tremors", "decreased school performance", "Most appropriate Investigation"],
"AS-2353": ["drinking 3 glasses of cow's milk daily", "MCV 62", "Ferritin 9"],
"AS-2354": ["drinking 3 pints of cow's milk daily", "MCV 62", "Ferritin 9"],
"AS-2355": ["Drinking excessive amounts Of Milk", "MCV: 62", "Ferritin: 9"],
"AS-2356": ["acetaminophen", "1 day ago", "right upper quadrant abdominal pain"],
"AS-2357": ["cystic fibrosis"],
"AS-2358": ["fever of 9-day duration", "non-purulent conjunctivitis", "red cracked lips", "swollen and erythematous hands and feet"],
"AS-2384": ["grandfather's farm", "miosis", "lacrimation, salivation", "garlic odor"],
"AS-2387": ["KOPLIK spots"],
"AS-2387B": ["measles"],
"AS-2388": ["routine paediatrics exam", "irregular pulse"],
"AS-2390": ["depressed nasal bridge", "upward slanting palpebral fissures", "epicanthal fold"],
"AS-2394": ["chest pain", "high status", "joints are laxed", "arachnodactyly"],
"AS-2395": ["5-week-old", "becomes very hungry and wants to feed again", "Potassium 2.9", "Bicarbonate 32", "Chloride 89"],
"AS-2396": ["sudden abrupt loss of environmental awareness", "sudden return to normal baseline", "EEG 3-Hz spikes"],
"AS-2401": ["panhypopituitarism", "Cortisol low"],
"AS-2404": ["Bilateral Wheeze And Prolonged Expiratory Phase", "Similar Attacks Before", "Oxygen Saturation: 82 %"],
"AS-2405": ["new-onset exertional dyspnea and palpitations", "viral URI 3 weeks ago", "gallop rhythm"],
"AS-2406": ["2 days old", "hemarthrosis", "Prolonged PTT, Normal PT"],
"AS-2412": ["pale", "spleen is 6 cm below the costal margin", "Hb: 52 g/L", "Sickle cell screen: Positive"],
"AS-2416": ["poor concentration and hyperactivity at school", "only sleeps 5 hours per night from 1 AM to 6 AM"],
"AS-2418": ["hx of choking after he ingested some seed", "dec RT side breathing sound"],
}

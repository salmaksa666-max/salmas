# -*- coding: utf-8 -*-
# Batch r10 — AboSarah SMLE 2026 deck. 141 questions (01-Medicine + 04-Surgery).

EXPLANATIONS = {

"AS-1851": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "سؤال عن ترتيب <bdi>workup</bdi> لأول <bdi>seizure</bdi> عند بالغ ما له سبب واضح، والمطلوب الخطوة الأولى بعد التاريخ والتحاليل.",
    "clues": [
        ("first-time generalized tonic-clonic seizure", "أول <bdi>seizure</bdi> بدون سبب مُحفِّز واضح"),
        ("Neurological findings are unremarkable", "الفحص <bdi>neurological</bdi> طبيعي، يعني مافي عجز بؤري حالي يغيّر الأولوية"),
    ],
    "why_correct": [
        "بعد ما التاريخ والتحاليل (<bdi>CBC</bdi> و<bdi>metabolic panel</bdi>) استبعدوا الأسباب المُحفِّزة زي اضطراب السكر أو الكهارل، الخطوة الجاية هي <bdi>neuroimaging</bdi> لاستبعاد <bdi>structural lesion</bdi>.",
        "بالطوارئ أسرع وسيلة <bdi>imaging</bdi> متوفرة هي <bdi>head CT scan</bdi>، فهي الخطوة الأولية الأنسب.",
        "<bdi>EEG</bdi> يجي بعدها لتصنيف نوع <bdi>seizure</bdi> وتقدير خطر التكرار، مو لاستبعاد سبب عضوي عاجل.",
    ],
    "when_changes": [
        "لو كان فيه حمى أو علامات <bdi>meningism</bdi>، الجواب يتحول لاستبعاد <bdi>CNS infection</bdi> أولاً وقد تحتاج <bdi>lumbar puncture</bdi> بعد الصورة.",
        "لو السؤال يسأل عن الخطوة اللي تجي بعد <bdi>CT</bdi> الطبيعي لتصنيف النوبة، الجواب يصير <bdi>EEG</bdi>.",
    ],
    "rule": "أول <bdi>seizure</bdi> عند بالغ بدون سبب محفِّز: التحاليل الطبيعية تدفعك لـ <bdi>neuroimaging</bdi>، وبالطوارئ هذا يعني <bdi>head CT</bdi> أولاً ثم <bdi>EEG</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1852": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "سؤال عن تأكيد تشخيص <bdi>hypertension</bdi> قبل البدء بالعلاج، عند مريض بدون أي <bdi>end organ damage</bdi>.",
    "clues": [
        ("elevated blood pressure during a routine checkup", "قراءة وحيدة بالعيادة فقط، مو تشخيص مؤكد لـ <bdi>hypertension</bdi> بعد"),
    ],
    "why_correct": [
        "المريض <bdi>asymptomatic</bdi> والفحص والتحاليل (<bdi>ECG</bdi>، <bdi>CBC</bdi>، <bdi>electrolytes</bdi>، <bdi>renal function</bdi>، <bdi>urine analysis</bdi>) كلها طبيعية، يعني مافي دليل على <bdi>end organ damage</bdi> يستدعي علاج فوري.",
        "الخطوة الصحيحة قبل تثبيت التشخيص هي تأكيده بقياس خارج العيادة، يعني <bdi>ambulatory blood pressure measurement</bdi> (أو قياس بالمنزل)، وهذا يستبعد أيضًا <bdi>white coat hypertension</bdi>.",
        "بعد التأكيد فقط نقرر البدء بعلاج دوائي.",
    ],
    "when_changes": [
        "لو كان فيه <bdi>end organ damage</bdi> واضح (زي <bdi>retinopathy</bdi> أو ضعف كلوي حاد) أو الضغط مرتفع جدًا، الجواب يتحول للبدء بالعلاج فورًا بدون انتظار.",
        "لو السؤال يسأل عن الفحص الأساسي قبل تشخيص <bdi>hypertension</bdi>، الجواب يصير فحوصات الـ <bdi>baseline workup</bdi> (تخطيط قلب، كهارل، بول، دهون).",
    ],
    "rule": "قراءة ضغط مرتفعة وحيدة بدون <bdi>end organ damage</bdi> = تأكيد أول بقياس خارج العيادة (<bdi>ABPM</bdi> أو منزلي)، مو علاج مباشر ولا إعادة القياس بعد شهور.",
    "comparison": None,
    "labs": [["Blood pressure", "elevated (not specified)", "&lt;140/90 mmHg (office)"]],
    "guideline_note": None,
},

"AS-1853": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "سؤال تحديد موقع <bdi>stroke</bdi> حسب التوزيع: الطرف الأكثر تأثرًا يحدد أي شريان مصاب.",
    "clues": [
        ("confused and behaving in a strange way", "تغيّر سلوك/تشوش يشير لإصابة الفص الجبهي (<bdi>frontal lobe</bdi>)"),
        ("Left leg power is 2/5", "ضعف شديد بالساق اليسرى فقط، الذراع سليمة"),
        ("decreased sensation in the left leg", "فقدان حسي بالساق نفسها، يدعم نفس التوزيع"),
    ],
    "why_correct": [
        "مريض عنده عوامل خطر وعائية (<bdi>diabetes</bdi>، <bdi>hypertension</bdi>، <bdi>dyslipidemia</bdi>) وعنده ضعف وخلل حسي بالساق اليسرى فقط، بينما الذراع والأطراف الأخرى طبيعية.",
        "منطقة الساق بالقشرة الحركية والحسية تقع على السطح الإنسي للمخ، والمغذّي لها هو <bdi>anterior cerebral artery (ACA)</bdi>، فالإصابة بالساق أكثر من الذراع تدل على <bdi>ACA stroke</bdi>.",
        "إصابة الفص الجبهي الإنسي (منطقة <bdi>ACA</bdi>) تفسر أيضًا التشوش وتغيّر السلوك الغريب.",
        "بما إن الضعف بالساق اليسرى، فالإصابة بنصف الكرة اليمين، إذن <bdi>right ACA stroke</bdi>.",
    ],
    "when_changes": [
        "لو كان الضعف بالوجه والذراع أكثر من الساق، الجواب يتحول لـ <bdi>MCA stroke</bdi>.",
        "لو كان فيه شلل عيون أو دوخة وترنح وعجز ثنائي أو متصالب، الجواب يصير <bdi>basilar artery stroke</bdi>.",
    ],
    "rule": "ساق أضعف من الذراع = <bdi>ACA</bdi>؛ وجه وذراع أضعف من الساق = <bdi>MCA</bdi>.",
    "comparison": {
        "headers": ["الشريان", "التوزيع المميز"],
        "rows": [
            ["ACA", "الساق أكثر من الذراع + تغيّر سلوك"],
            ["MCA", "الوجه والذراع أكثر من الساق ± أفيزيا/إهمال"],
            ["Basilar", "علامات جذع المخ، دوخة، ترنح، عجز ثنائي/متصالب"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},

"AS-1854": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال سبب <bdi>hyponatremia</bdi> عند مريضة عندها آفة بالجهاز العصبي المركزي (<bdi>glioblastoma</bdi>).",
    "clues": [
        ("glioblastoma multiforme", "آفة بالجهاز العصبي المركزي (<bdi>CNS</bdi>)، سبب معروف لـ <bdi>SIADH</bdi>"),
        ("hyponatremia", "انخفاض <bdi>sodium</bdi> بالدم هو موضوع السؤال"),
    ],
    "why_correct": [
        "<bdi>glioblastoma multiforme</bdi> هو آفة بالجهاز العصبي المركزي، وآفات <bdi>CNS</bdi> (الأورام، الرضوض، العدوى، <bdi>stroke</bdi>) من أهم أسباب <bdi>syndrome of inappropriate ADH secretion (SIADH)</bdi>.",
        "زيادة <bdi>ADH</bdi> تسبب احتباس ماء وبالتالي <bdi>euvolemic hyponatremia</bdi> مع بول مُركّز بشكل غير متوقع.",
        "هالـ <bdi>hyponatremia</bdi> نفسه ممكن يزيد <bdi>seizures</bdi> ويضعف الوظيفة <bdi>cognitive</bdi>، وهذا يطابق عرضها.",
    ],
    "when_changes": [
        "لو المريضة كانت بعد جراحة بالمخ أو <bdi>SAH</bdi> وعندها علامات نقص حجم (<bdi>hypovolemic</bdi>)، الجواب يتحول لـ <bdi>cerebral salt wasting</bdi>.",
        "لو كان فيه تاريخ شرب ماء مفرط بدون سبب عضوي، الجواب يصير <bdi>primary polydipsia</bdi>.",
    ],
    "rule": "آفة بالمخ + <bdi>hyponatremia</bdi> = فكّر <bdi>SIADH</bdi> أولاً؛ لو المريض بعد جراحة عصبية وفيه نقص حجم، فكّر <bdi>cerebral salt wasting</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1855": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال اختيار خافض ضغط بمريض <bdi>type 1 diabetes</bdi> عنده <bdi>hypertension</bdi>، لازم يكون مع حماية كلوية.",
    "clues": [
        ("type I diabetes mellitus", "مرض سكري نوع أول، خطر <bdi>diabetic nephropathy</bdi>"),
        ("BP:150/90", "ضغط مرتفع يحتاج علاج"),
    ],
    "why_correct": [
        "شاب مصاب بـ <bdi>type 1 diabetes</bdi> وضغطه <bdi>150/90</bdi>: هالمريض معرض لاعتلال الكلى السكري.",
        "<bdi>ACE inhibitor</bdi> يخفض الضغط وله أثر <bdi>nephroprotective</bdi> مباشر: يوسّع الشريان الخارج من الكبيبة فيقلل الضغط داخلها ويقلل <bdi>proteinuria</bdi>، فيؤخر تقدم المرض الكلوي.",
        "لهذا السبب <bdi>ACE inhibitor</bdi> أو <bdi>ARB</bdi> هو الخيار الأول بأي مريض سكري عنده <bdi>hypertension</bdi>، بغض النظر عن العمر.",
    ],
    "when_changes": [
        "لو المريضة حامل، الجواب يتحول لـ <bdi>labetalol</bdi> أو <bdi>nifedipine</bdi> لأن <bdi>ACE inhibitors</bdi> ممنوعة بالحمل.",
        "لو احتاج علاج إضافي (<bdi>step 2</bdi>)، يُضاف <bdi>calcium channel blocker</bdi> أو <bdi>thiazide-like diuretic</bdi> مع <bdi>ACE inhibitor</bdi>، مو بدل عنه.",
    ],
    "rule": "مريض سكري + <bdi>hypertension</bdi> = ابدأ بـ <bdi>ACE inhibitor</bdi> (أو <bdi>ARB</bdi>) إلا لو حامل.",
    "comparison": None,
    "labs": [["Blood pressure", "150/90 mmHg", "&lt;130/80 mmHg (diabetic target)"]],
    "guideline_note": None,
},

"AS-1878": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "سؤال تشخيص سبب <bdi>jaundice</bdi> عند مريضة بـ <bdi>SLE</bdi>: النمط المناعي والخزعة يرجحون <bdi>autoimmune hepatitis</bdi>، والعلاج الأول <bdi>steroids</bdi>.",
    "clues": [
        ("jaundice", "اصفرار يدل على مرض بالكبد"),
        ("SLE", "مرض <bdi>autoimmune</bdi> آخر موجود، يزيد احتمال مرض كبد مناعي"),
        ("ANA: 1:640 (High)", "<bdi>ANA</bdi> مرتفع جدًا يدعم <bdi>autoimmune hepatitis</bdi>"),
        ("Interphase hepatitis with plasma cells", "صورة الخزعة الكلاسيكية لـ <bdi>autoimmune hepatitis</bdi>"),
    ],
    "why_correct": [
        "امرأة شابة عندها مرض <bdi>autoimmune</bdi> آخر (<bdi>SLE</bdi>)، <bdi>transaminases</bdi> مرتفعة جدًا، <bdi>ANA 1:640</bdi>، و<bdi>globulin</bdi> مرتفع.",
        "الخزعة أظهرت <bdi>interface hepatitis مع plasma cells</bdi>، وهذا النمط النسيجي يثبّت تشخيص <bdi>autoimmune hepatitis (AIH)</bdi>.",
        "العلاج الأول لـ <bdi>AIH</bdi> هو <bdi>corticosteroids</bdi> (<bdi>prednisolone</bdi>)، ممكن يضاف له <bdi>azathioprine</bdi> لاحقًا كـ <bdi>steroid-sparing agent</bdi>.",
    ],
    "when_changes": [
        "لو الخزعة أظهرت <bdi>steatohepatitis</bdi> مناسب للسمنة، الجواب يتحول لـ <bdi>vitamin E مع weight loss</bdi> (<bdi>NASH</bdi>).",
        "لو النمط كان <bdi>cholestatic</bdi> مع <bdi>ALP مرتفع</bdi> و<bdi>AMA +</bdi>، الجواب يصير <bdi>ursodeoxycholic acid</bdi> لـ <bdi>primary biliary cholangitis</bdi>.",
    ],
    "rule": "<bdi>interface hepatitis</bdi> مع <bdi>plasma cells</bdi> + <bdi>ANA</bdi> مرتفع = <bdi>autoimmune hepatitis</bdi> = <bdi>prednisolone</bdi> ± <bdi>azathioprine</bdi>.",
    "comparison": {
        "headers": ["المرض", "العلامة المميزة", "العلاج الأول"],
        "rows": [
            ["AIH", "ANA/anti-SMA + interface hepatitis", "Prednisolone ± azathioprine"],
            ["PBC", "AMA + high ALP + pruritus", "Ursodeoxycholic acid"],
            ["NASH", "Obesity + steatohepatitis", "Weight loss ± vitamin E"],
        ],
    },
    "labs": [
        ["ANA titer", "1:640", "negative/low titer"],
        ["AST", "654", "~10-40 U/L"],
        ["ALT", "734", "~7-56 U/L"],
        ["ALP", "129", "~44-147 U/L"],
        ["Total bilirubin", "43", "~0.3-1.2 mg/dL"],
    ],
    "guideline_note": None,
},

"AS-1897": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال اختيار نظام أوكسجين دقيق بمريض مرض رئوي، خصوصًا خطر احتباس <bdi>CO2</bdi>.",
    "clues": [
        ("Pulmonary Disease", "مرض رئوي مزمن (زي <bdi>COPD</bdi>) معرض لـ <bdi>CO2 retention</bdi> مع أوكسجين عالي غير منضبط"),
    ],
    "why_correct": [
        "بمرض رئوي مزمن زي <bdi>COPD</bdi>، إعطاء أوكسجين عالي بدون ضبط يزيد خطر احتباس <bdi>CO2</bdi> (فقدان <bdi>hypoxic drive</bdi> ومشاكل التهوية/التروية).",
        "<bdi>Venturi mask</bdi> يعطي نسبة <bdi>FiO2</bdi> ثابتة ودقيقة بغض النظر عن نمط تنفس المريض، فيسمح بضبط الهدف لمستوى تشبّع <bdi>88-92%</bdi> بدون تفاقم احتباس <bdi>CO2</bdi>.",
        "هذا الدقة بالتحكم هي اللي تجعله «الأفضل» بمريض رئوي مزمن، مو كمية الأوكسجين العالية.",
    ],
    "when_changes": [
        "لو المريض بحالة نقص أوكسجين حاد وشديد (زي صدمة أو رضح) بدون خطر احتباس <bdi>CO2</bdi>، الجواب يتحول لـ <bdi>rebreathing bag</bdi> لإعطاء أوكسجين عالي بسرعة.",
        "لو المريض مستقر ويحتاج أوكسجين منزلي طويل الأمد بجرعة منخفضة، <bdi>nasal cannula</bdi> تكون كافية.",
    ],
    "rule": "«الأفضل» بمريض رئوي مزمن معرض لاحتباس <bdi>CO2</bdi> يعني الأدق تحكمًا، وهذا <bdi>Venturi mask</bdi>، مو الأعلى تركيز أوكسجين.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1919": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "سؤال علاج <bdi>agitated delirium</bdi> بمريضة <bdi>palliative care</bdi> ما استجابت للتهدئة غير الدوائية.",
    "clues": [
        ("end-stage metastatic cancer", "مرض نهائي، سياق <bdi>palliative care</bdi>"),
        ("palliative care", "التعامل يركّز على الراحة والتهدئة الآمنة"),
        ("aggressive and confused", "تشوش حاد مع عدوانية = <bdi>hyperactive delirium</bdi>"),
    ],
    "why_correct": [
        "مريضة مسنّة بسرطان نهائي أصابها تشوش حاد وعدوانية مفاجئة مع فشل تهدئتها بالطرق غير الدوائية: هذا <bdi>hyperactive delirium</bdi>.",
        "بعد استبعاد الأسباب القابلة للعلاج، الدواء المفضّل عند فشل التهدئة هو <bdi>antipsychotic</bdi> بجرعة منخفضة، وأشهره <bdi>haloperidol</bdi>، لأنه يهدّئ الهياج بدون ما يزيد التشوش.",
    ],
    "when_changes": [
        "لو السبب هو انسحاب كحول أو <bdi>benzodiazepines</bdi>، الجواب يتحول لـ <bdi>benzodiazepine</bdi> كخيار أول.",
        "لو المريضة معروف عندها <bdi>Parkinson disease</bdi> أو <bdi>Lewy body dementia</bdi>، يتجنب <bdi>haloperidol</bdi> ويُستخدم خيار آخر.",
    ],
    "rule": "<bdi>delirium</bdi> مع عدوانية لم تستجب لتدابير غير دوائية = <bdi>haloperidol</bdi> بجرعة منخفضة، إلا بحالات انسحاب الكحول أو مرض <bdi>Parkinson/Lewy body</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1948": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال تشخيص تورّم طرف واحد عند مريض بعامل خطر كبير لـ <bdi>VTE</bdi> (سرطان + تنويم).",
    "clues": [
        ("pancreatic cancer", "من أكثر السرطانات المسببة لتخثر الدم (<bdi>thrombogenic</bdi>)"),
        ("swollen left lower limb during hospitalization", "تورّم جديد بطرف واحد خلال فترة عدم حركة بالمستشفى"),
        ("tender, erythematous swelling", "ألم واحمرار يحتاج تفريق عن <bdi>cellulitis</bdi>"),
    ],
    "why_correct": [
        "عنده عاملان قويان لـ <bdi>venous thromboembolism</bdi>: <bdi>pancreatic cancer</bdi> (من أكثر الأورام تسببًا بالتخثر) و<bdi>hospitalization</bdi> (قلة حركة).",
        "تورّم جديد، مؤلم، أحادي الجانب، مع احمرار بهذا السياق = <bdi>DVT</bdi> حتى يُستبعد، والخطوة التالية تأكيده بـ <bdi>compression Doppler ultrasound</bdi>.",
    ],
    "when_changes": [
        "لو كان فيه حمى وجرح جلدي أو مدخل عدوى واضح مع احمرار متمدد، الجواب يتحول لـ <bdi>cellulitis</bdi>.",
        "لو المريض عنده تاريخ خشونة ركبة وألم مفاجئ بالربلة مرتبط بحركة الركبة، فكّر بـ <bdi>ruptured Baker's cyst</bdi>.",
    ],
    "rule": "تورّم مؤلم أحادي الطرف + عامل خطر <bdi>VTE</bdi> (سرطان، تنويم، جراحة) = <bdi>DVT</bdi> حتى يُثبت العكس بـ <bdi>duplex ultrasound</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1951": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال اختيار المضاد الحيوي التجريبي لـ <bdi>cellulitis</bdi> بمريض سكري، لازم يغطي <bdi>Streptococcus</bdi> و<bdi>Staphylococcus</bdi>.",
    "clues": [
        ("long standing DM", "مريض سكري قديم، عامل خطر لعدوى الجلد"),
        ("cellulitis", "عدوى جلدية سطحية تحتاج تغطية <bdi>Gram positive</bdi>"),
    ],
    "why_correct": [
        "مريض سكري عنده <bdi>cellulitis</bdi> مع <bdi>WBC مرتفع (18)</bdi>، والسبب المعتاد هو <bdi>Streptococcus pyogenes</bdi> و<bdi>Staphylococcus aureus</bdi>.",
        "<bdi>clindamycin</bdi> يغطّي الاثنين معًا (بما فيها بعض سلالات <bdi>community MRSA</bdi>) وله توزع جيد بالجلد والأنسجة الرخوة، لذلك هو الخيار التجريبي الصحيح هنا.",
    ],
    "when_changes": [
        "لو كانت العدوى شديدة أو مع <bdi>sepsis</bdi> أو <bdi>MRSA</bdi> مؤكد، الجواب يتحول لـ <bdi>vancomycin</bdi>.",
        "لو المريض يحتاج تغطية <bdi>Pseudomonas</bdi> أو عدوى <bdi>Gram negative</bdi> (زي <bdi>pyelonephritis</bdi>)، يكون <bdi>ciprofloxacin</bdi> مناسب، مو بـ <bdi>cellulitis</bdi> البسيطة.",
    ],
    "rule": "<bdi>cellulitis</bdi> = اختر دواء يغطي <bdi>Streptococcus</bdi> و<bdi>Staphylococcus</bdi>؛ <bdi>quinolones</bdi> تغطيتها ضعيفة ضد <bdi>Streptococcus</bdi> فهي جواب خطأ كلاسيكي، و<bdi>vancomycin</bdi> يُحفظ للحالات الشديدة أو <bdi>MRSA</bdi>.",
    "comparison": None,
    "labs": [["WBC", "18 (x10^3/uL, implied)", "4-11 x10^3/uL"]],
    "guideline_note": None,
},

"AS-1975": {
    "correct_letter": "B",
    "self_judged": True,
    "idea": "سؤال قراءة سيرولوجيا <bdi>hepatitis B</bdi>: المصدر ما حدد جواب، لكن معطيات السيرولوجيا تحدد <bdi>chronic</bdi> مقابل <bdi>acute</bdi>.",
    "clues": [
        ("10 years ago", "تاريخ تعرّض بعيد (10 سنوات)، يدعم عدوى <bdi>chronic</bdi> مو حديثة"),
        ("HBs Ag +ve", "عدوى <bdi>hepatitis B</bdi> حالية مستمرة"),
        ("HBe Ag +ve", "يدل على <bdi>active viral replication</bdi>"),
    ],
    "why_correct": [
        "تاريخ التعرّض (نقل دم) من <bdi>10 سنوات</bdi> يستبعد عدوى <bdi>acute</bdi> حديثة؛ <bdi>IgG</bdi> إيجابي (مو <bdi>IgM</bdi>) هو المؤشر الكلاسيكي على <bdi>chronic infection</bdi> لا عدوى حادة.",
        "بما إن الخيارات المتوفرة فقط بين <bdi>«acute active»</bdi> و<bdi>«chronic inactive»</bdi>، وبُعد التاريخ الزمني ونوع الجسم المضاد يرجّحان <bdi>chronic</bdi> على <bdi>acute</bdi>، فالأقرب سريريًا هو <bdi>chronic hepatitis B</bdi>.",
        "هذا تقييم <bdi>self-judged</bdi> لأن المصدر لم يثبّت جوابًا، واخترت الأقرب للمنطق السريري من بين الخيارين المتاحين.",
    ],
    "when_changes": [
        "لو كان <bdi>Anti-HBc IgM</bdi> إيجابي بدل <bdi>IgG</bdi>، الجواب يصير <bdi>acute hepatitis B</bdi> بدون شك.",
        "لو كان <bdi>HBeAg</bdi> سلبي و<bdi>Anti-HBe</bdi> إيجابي مع <bdi>ALT</bdi> طبيعي وفيروس منخفض، هذا يطابق تمامًا <bdi>chronic inactive carrier</bdi>.",
    ],
    "rule": "<bdi>IgM anti-HBc</bdi> = عدوى حديثة (<bdi>acute</bdi>)؛ <bdi>IgG anti-HBc</bdi> مع <bdi>HBsAg</bdi> مستمر = <bdi>chronic</bdi>؛ <bdi>HBeAg</bdi> يحدد مستوى النشاط الفيروسي.",
    "comparison": {
        "headers": ["الحالة", "IgM/IgG anti-HBc", "HBeAg"],
        "rows": [
            ["Acute", "IgM +ve", "عادة +ve (نشاط عالي مؤقت)"],
            ["Chronic active", "IgG +ve", "+ve (نشاط فيروسي مستمر)"],
            ["Chronic inactive carrier", "IgG +ve", "-ve (anti-HBe +ve)"],
        ],
    },
    "labs": None,
    "guideline_note": "ملاحظة: <bdi>HBeAg</bdi> إيجابي يعني نشاط فيروسي مستمر، وهذا بالحقيقة أقرب لوصف <bdi>chronic active</bdi> لا <bdi>chronic inactive</bdi>؛ لكن بما إن المصدر لم يعطِ خيار <bdi>chronic active</bdi> صريح واختار المصدر عدم تثبيت جواب، فالاختيار هنا مبني على استبعاد <bdi>acute</bdi> أولاً (لأن <bdi>IgG</bdi> لا <bdi>IgM</bdi>) بين الخيارين المتاحين فقط.",
},

"AS-1977": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال علاج <bdi>tuberculous meningitis</bdi>، لازم يضاف <bdi>steroid</bdi> للعلاج الرباعي المعتاد.",
    "clues": [
        ("headache for 3 months", "صداع مزمن مستمر، يدعم عدوى مزمنة بالجهاز العصبي المركزي"),
        ("Mycobacterium tuberculosis", "تأكيد سبب العدوى بـ <bdi>PCR</bdi>"),
    ],
    "why_correct": [
        "رجل من منطقة موبوءة عنده تعب ونقص وزن وصداع لـ <bdi>3 أشهر</bdi>، تاريخ تعرّض للـ <bdi>tuberculosis</bdi>، و<bdi>PCR</bdi> إيجابي لـ <bdi>Mycobacterium tuberculosis</bdi>: هذا يطابق <bdi>TB meningitis</bdi>.",
        "علاج <bdi>TB meningitis</bdi> هو نفس العلاج الرباعي (<bdi>isoniazid, rifampin, pyrazinamide, ethambutol</bdi>) بالإضافة إلى <bdi>dexamethasone</bdi> كعلاج مساعد.",
        "<bdi>dexamethasone</bdi> يقلل الالتهاب والتليف حول الأغشية ويقلل الوفيات والمضاعفات مقارنة بالعلاج الرباعي لوحده.",
    ],
    "when_changes": [
        "لو كانت العدوى <bdi>pulmonary TB</bdi> بدون إصابة بالجهاز العصبي المركزي، العلاج الرباعي لوحده يكون كافيًا بدون <bdi>steroid</bdi>.",
        "لو السبب غير معروف بعد وفيه شك بـ <bdi>HSV encephalitis</bdi>، يضاف <bdi>acyclovir</bdi> تجريبيًا لحين استبعاده.",
    ],
    "rule": "<bdi>TB meningitis</bdi> = العلاج الرباعي المعتاد + <bdi>dexamethasone</bdi>؛ العلاج الرباعي لوحده يكفي فقط بـ <bdi>pulmonary TB</bdi> غير المعقدة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1978": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال العلاج التجريبي لـ <bdi>community-acquired pneumonia</bdi> عند مريض مُنوَّم بالمستشفى.",
    "clues": [
        ("productive cough, fever, and dyspnea for 3 days", "أعراض <bdi>pneumonia</bdi> نمطية حادة"),
        ("consolidation at the right lower lung field", "دليل فحص على التصلّب الرئوي (<bdi>consolidation</bdi>)"),
        ("empiric", "السؤال يبي علاج تجريبي قبل نتائج الزرع"),
    ],
    "why_correct": [
        "سعال مُنتج وحمى وضيق نفس لـ <bdi>3 أيام</bdi> مع <bdi>consolidation</bdi> بالفص السفلي الأيمن عند مريض مُجتمعي = <bdi>community-acquired pneumonia (CAP)</bdi>.",
        "بما إنه يُؤخذ له زرع دم وقشع بالطوارئ (يعني يُنوَّم)، العلاج التجريبي المعياري هو <bdi>beta-lactam + macrolide</bdi>: <bdi>ceftriaxone</bdi> يغطي <bdi>pneumococcus</bdi> وبعض <bdi>Gram negatives</bdi>، و<bdi>azithromycin</bdi> يغطي الكائنات <bdi>atypical</bdi>.",
    ],
    "when_changes": [
        "لو كانت العدوى <bdi>hospital-acquired</bdi> أو فيه خطر <bdi>Pseudomonas</bdi>، الجواب يتحول لـ <bdi>meropenem</bdi> أو مضاد مضاد لـ <bdi>Pseudomonas</bdi>.",
        "لو كان فيه خطر <bdi>MRSA</bdi> (عدوى سابقة أو مضادات وريدية حديثة)، يُضاف <bdi>vancomycin</bdi> للعلاج.",
    ],
    "rule": "<bdi>CAP</bdi> عند مريض مُنوَّم غير حرج = <bdi>beta-lactam (ceftriaxone) + macrolide (azithromycin)</bdi>، أو <bdi>respiratory fluoroquinolone</bdi> لوحده.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-1981": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "سؤال سبب <bdi>stroke</bdi> عند شاب سليم بعد حدث تخثر وريدي (<bdi>DVT/PE</bdi>): فكّر بـ <bdi>paradoxical embolism</bdi>.",
    "clues": [
        ("femur fracture", "عامل خطر لتكوّن خثرة وريدية (<bdi>venous thrombosis</bdi>)"),
        ("pulmonary embolism", "خثرة وريدية وصلت الدورة الرئوية، تؤكد المصدر الوريدي"),
        ("left cerebral infarction", "احتشاء شرياني بالمخ، يحتاج تفسير كيف انتقلت الخثرة من الوريد للشريان"),
    ],
    "why_correct": [
        "شاب سليم عنده <bdi>femur fracture</bdi> حديث و<bdi>pulmonary embolism</bdi> قبل يومين، والآن عنده احتشاء مخي يسار.",
        "وصول خثرة وريدية للدورة الشريانية يعني وجود تحويلة من اليمين لليسار (<bdi>right-to-left shunt</bdi>): هذا هو <bdi>paradoxical embolism</bdi> عبر <bdi>patent foramen ovale (PFO)</bdi>.",
        "ارتفاع ضغط الجانب الأيمن بالقلب بعد <bdi>PE</bdi> يزيد احتمال عبور الخثرة من اليمين لليسار عبر الـ <bdi>PFO</bdi>.",
    ],
    "when_changes": [
        "لو كان المريض مسن وعنده نبض غير منتظم، الجواب يتحول لـ <bdi>atrial fibrillation</bdi> كسبب <bdi>cardioembolic</bdi> أشيع.",
        "لو عنده عوامل خطر تصلب شرايين (تدخين، سكري، دهون) بدون قصة خثرة وريدية، فكّر بـ <bdi>carotid artery stenosis</bdi>.",
    ],
    "rule": "شاب سليم + خثرة وريدية (<bdi>DVT/PE</bdi>) + <bdi>stroke</bdi> شرياني = <bdi>paradoxical embolism</bdi> عبر <bdi>PFO</bdi> حتى يُستبعد.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-2005": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال تشخيص فقدان رؤية مؤقت بعين واحدة عند مريضة سكري: نمط كلاسيكي لـ <bdi>amaurosis fugax</bdi> (<bdi>TIA</bdi>).",
    "clues": [
        ("sudden left eye visual loss for 20 minutes", "فقدان مفاجئ وقصير المدة بعين واحدة"),
        ("vision returned to normal", "تعافٍ كامل تلقائي، يميل لحدث عابر وعائي"),
    ],
    "why_correct": [
        "فقدان رؤية مفاجئ بعين واحدة استمر <bdi>20 دقيقة</bdi> وعاد الوضع طبيعي تمامًا عند مريضة سكري: هذا <bdi>amaurosis fugax</bdi>، وهو <bdi>transient ischemic attack (TIA)</bdi> للدورة الشبكية (غالبًا صمّة من الشريان السباتي).",
        "الفحص الطبيعي بعد الحدث متوقع بالضبط لأن العجز كان عابرًا وتعافى بالكامل، وهذا يطابق تعريف <bdi>TIA</bdi>.",
    ],
    "when_changes": [
        "لو كان فقدان الرؤية مؤلم بعين شابة ويتطور بأيام، الجواب يتحول لـ <bdi>optic neuritis</bdi> ضمن <bdi>multiple sclerosis</bdi>.",
        "لو كان فيه ومضات وذباب طائر وستار دائم بالمجال البصري، الجواب يصير <bdi>retinal detachment</bdi>.",
    ],
    "rule": "فقدان رؤية بعين واحدة يتعافى بدقائق عند مريض بعامل خطر وعائي = <bdi>TIA</bdi> (<bdi>amaurosis fugax</bdi>)، وخطوته التالية <bdi>carotid duplex ultrasound</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},


"AS-2007": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال خطوة العلاج بـ <bdi>type 2 diabetes</bdi> بعد فشل تجربة <bdi>lifestyle</bdi> لوحدها برفع <bdi>HbA1c</bdi> عن الهدف.",
    "clues": [
        ("recently diagnosed with type 2 diabetes", "تشخيص حديث، وتم تجربة <bdi>lifestyle measures</bdi> بالفعل"),
        ("BMI 32 kg/m2", "<bdi>obesity</bdi>، يفضَّل دواء لا يزيد الوزن"),
        ("HA1C 6.9", "<bdi>HbA1c</bdi> مازال فوق الهدف بعد التجربة"),
    ],
    "why_correct": [
        "المريض شخّص حديثًا وطبّق <bdi>lifestyle plan</bdi> كامل، ومع ذلك <bdi>HbA1c</bdi> لسه <bdi>6.9%</bdi> مع <bdi>BMI 32</bdi>.",
        "بعد تجربة <bdi>lifestyle</bdi> لمدة 3-6 أشهر، لو <bdi>HbA1c</bdi> مازال فوق <bdi>6.5%</bdi>، هذا يعني فشل العلاج غير الدوائي لوحده، فتبدأ <bdi>metformin</bdi>.",
        "<bdi>metformin</bdi> هو الخيار الأول: لا يسبب زيادة وزن، لا يسبب <bdi>hypoglycemia</bdi>، ومناسب خصوصًا للمرضى <bdi>obese</bdi>.",
    ],
    "when_changes": [
        "لو كان <bdi>HbA1c</bdi> أعلى من <bdi>10%</bdi> أو المريض عنده أعراض <bdi>catabolic</bdi> شديدة، الجواب يتحول لـ <bdi>insulin</bdi>.",
        "لو كان هذا أول زيارة للمريض بدون تجربة <bdi>lifestyle</bdi> سابقة، الجواب يصير <bdi>lifestyle measures</bdi> أولاً.",
    ],
    "rule": "كلمة «الآن» بعد تجربة <bdi>lifestyle</bdi> فاشلة = تصعيد لـ <bdi>metformin</bdi>، مو إعادة نفس النصائح.",
    "comparison": None,
    "labs": [["HbA1c", "6.9%", "4.7-5.6%"], ["BMI", "32 kg/m2", "18.5-24.9 kg/m2"]],
    "guideline_note": None,
},

"AS-2008": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال خطوة العلاج التالية بعد فشل علاج <bdi>H. pylori</bdi> الأول (<bdi>clarithromycin triple therapy</bdi>).",
    "clues": [
        ("partial response", "استجابة جزئية فقط للعلاج الأول، يعني العلاج فشل بالقضاء على الجرثومة"),
        ("h pylori organism", "الخزعة أثبتت استمرار وجود الجرثومة بعد العلاج"),
    ],
    "why_correct": [
        "المريض أخذ <bdi>triple therapy</bdi> قائم على <bdi>clarithromycin</bdi> واستجاب جزئيًا فقط، والخزعة لسه تثبت وجود <bdi>H. pylori</bdi>: هذا فشل بالاستئصال.",
        "العلاج التالي يجب يتجنب <bdi>clarithromycin</bdi> (لاحتمال المقاومة)، والخيار المعياري هو <bdi>bismuth quadruple therapy</bdi>: <bdi>PPI + bismuth subcitrate + tetracycline + metronidazole</bdi> لمدة 14 يوم.",
    ],
    "when_changes": [
        "لو كان الخيار المتاح <bdi>levofloxacin-based triple therapy</bdi> صحيح ومصاغ بشكل معياري، يكون بديل مقبول كعلاج إنقاذ ثاني.",
        "لو كان المريض يأخذ العلاج الأول لأول مرة بدون فشل سابق، <bdi>clarithromycin triple therapy</bdi> يكون الخيار الأول الصحيح.",
    ],
    "rule": "فشل علاج <bdi>clarithromycin</bdi> لـ <bdi>H. pylori</bdi> = لا تعيد <bdi>clarithromycin</bdi>، انتقل لـ <bdi>bismuth quadruple therapy</bdi> لمدة 14 يوم.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-2009": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال خطوة العلاج المناسبة لمريض <bdi>GERD</bdi> عنده أعراض مستمرة وفشلت معه <bdi>antacids</bdi>.",
    "clues": [
        ("Gastro Esophageal Reflux Disease", "تشخيص معروف مسبقًا بـ <bdi>GERD</bdi>"),
        ("burning pain", "عرض نمطي لـ <bdi>reflux</bdi>"),
        ("over the counter antacids with no relief", "العلاج البسيط فشل، يحتاج تصعيد"),
    ],
    "why_correct": [
        "مريض معروف بـ <bdi>GERD</bdi> عنده أعراض نمطية (حرقة خلف الصدر تزيد بالانحناء، ارتجاع) وغير نمطية (سعال ليلي) لمدة 3 أشهر، وفشلت معه <bdi>antacids</bdi>.",
        "الخطوة المناسبة الآن هي قمع حمضي فعّال: <bdi>proton pump inhibitors (PPI)</bdi> هي العمود الفقري لعلاج <bdi>GERD</bdi> المستمر.",
    ],
    "when_changes": [
        "لو فشل العلاج بـ <bdi>PPI</bdi> بجرعة مثالية أو ظهرت مضاعفات، الجواب يتحول لـ <bdi>surgery (fundoplication)</bdi>.",
        "لو هذا أول زيارة بدون أي علاج سابق، الجواب يصير <bdi>lifestyle modification</bdi> أولاً.",
    ],
    "rule": "<bdi>lifestyle modification</bdi> تكون الجواب فقط لو لم يُجرَّب أي علاج؛ بعد فشل <bdi>antacids</bdi> الخطوة الصحيحة <bdi>PPI</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-2011": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال علاج <bdi>celiac disease</bdi> المؤكد بالسيرولوجيا وعلامات سوء الامتصاص.",
    "clues": [
        ("weight loss", "علامة سوء امتصاص (<bdi>malabsorption</bdi>)"),
        ("MCV 70", "<bdi>microcytic anemia</bdi> من سوء امتصاص الحديد"),
        ("Tissue transglutaminase antibody: Positive", "فحص <bdi>serology</bdi> نوعي لـ <bdi>celiac disease</bdi>"),
    ],
    "why_correct": [
        "عندها آلام بطن وانتفاخ ونقص وزن مع <bdi>BMI 18</bdi>، وفحوصات تدعم سوء امتصاص: <bdi>microcytic anemia</bdi> (<bdi>Hb 90</bdi>، <bdi>MCV 70</bdi>) من نقص الحديد، وكالسيوم وفوسفات منخفضان.",
        "<bdi>tissue transglutaminase antibody</bdi> الإيجابي يؤكد <bdi>celiac disease</bdi>.",
        "العلاج هو <bdi>gluten free diet</bdi> مدى الحياة، وهو العلاج الوحيد الفعّال.",
    ],
    "when_changes": [
        "لو كانت الحالة <bdi>refractory celiac disease</bdi> لا تستجيب لـ <bdi>gluten free diet</bdi>، يُضاف <bdi>glucocorticoids</bdi>.",
        "لو كانت الأعراض بسبب عدوى طفيلية (زي <bdi>giardiasis</bdi>) أو فرط نمو بكتيري، الجواب يتحول لـ <bdi>metronidazole</bdi>.",
    ],
    "rule": "<bdi>anti-tTG</bdi> إيجابي + سوء امتصاص وفقر دم بالحديد عند شاب = <bdi>celiac disease</bdi> = <bdi>gluten free diet</bdi> مدى الحياة.",
    "comparison": None,
    "labs": [
        ["Hb", "90 g/L", "120-160 g/L (female)"],
        ["MCV", "70 fL", "80-95 fL"],
        ["Calcium", "2.05 mmol/L", "2.15-2.62 mmol/L"],
        ["Phosphate", "0.79 mmol/L", "0.82-1.51 mmol/L"],
    ],
    "guideline_note": None,
},

"AS-2012": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "سؤال علاج <bdi>severe symptomatic hyponatremia</bdi> (<bdi>altered sensorium</bdi>) بسبب <bdi>SIADH</bdi> من <bdi>small cell lung cancer</bdi>.",
    "clues": [
        ("altered sensorium", "عرض عصبي خطير، يدل على <bdi>hyponatremia</bdi> شديدة ومُصحوبة بأعراض"),
        ("small cell carcinoma of the lung", "سبب شائع لـ <bdi>SIADH</bdi>"),
        ("euvolemic", "يدعم <bdi>SIADH</bdi> مو سبب آخر لـ <bdi>hyponatremia</bdi>"),
        ("Sodium 115", "<bdi>hyponatremia</bdi> شديدة"),
    ],
    "why_correct": [
        "<bdi>small cell lung cancer</bdi> + حالة <bdi>euvolemic</bdi> + <bdi>Na 115</bdi> يرجّحون <bdi>SIADH</bdi>، لكن وجود <bdi>altered sensorium</bdi> يجعلها <bdi>severe symptomatic hyponatremia</bdi>.",
        "العلاج الأولي الأفضل بهذه الحالة هو <bdi>hypertonic (3%) saline</bdi> لرفع الصوديوم بسرعة محدودة ومدروسة، مع الحرص على تجنب <bdi>osmotic demyelination</bdi> من تصحيح سريع جدًا.",
        "التقييد بالسوائل (<bdi>fluid restriction</bdi>) يُستخدم فقط بحالة <bdi>SIADH</bdi> بدون أعراض عصبية خطيرة.",
    ],
    "when_changes": [
        "لو لم يكن فيه أعراض عصبية شديدة (فقط <bdi>hyponatremia</bdi> خفيفة بسبب <bdi>SIADH</bdi>)، الجواب يتحول لـ <bdi>fluid restriction</bdi>.",
        "لو كانت الحالة <bdi>hypovolemic hyponatremia</bdi>، الجواب يصير <bdi>normal saline</bdi>.",
    ],
    "rule": "الأعراض العصبية الشديدة تتغلب على السبب: حتى لو السبب <bdi>SIADH</bdi>، وجود <bdi>confusion/seizure/coma</bdi> يعني <bdi>hypertonic saline</bdi> فورًا.",
    "comparison": None,
    "labs": [
        ["Sodium", "115 mmol/L", "134-146 mmol/L"],
        ["Potassium", "3.8 mmol/L", "3.5-5.1 mmol/L"],
        ["Urea", "4.3 mmol/L", "2.75-7.4 mmol/L"],
        ["Creatinine", "76 umol/L", "44-115 umol/L"],
    ],
    "guideline_note": None,
},

"AS-2014": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال سبب <bdi>breathlessness</bdi> بمدخّن طويل الأمد، والمفتاح وجود <bdi>clubbing</bdi> وهو علامة تحذيرية.",
    "clues": [
        ("smoking", "مدخّن طوال حياته، عامل خطر لأمراض رئوية متعددة"),
        ("lost the nail fold angle", "هذا وصف <bdi>finger clubbing</bdi>"),
    ],
    "why_correct": [
        "فقدان زاوية قاعدة الظفر (<bdi>nail fold angle</bdi>) هو تعريف <bdi>finger clubbing</bdi>.",
        "بمدخّن طويل الأمد عنده <bdi>breathlessness</bdi> لـ 6 أشهر، ظهور <bdi>clubbing</bdi> جديد يجب أن يُفترض أنه <bdi>bronchial carcinoma</bdi> حتى يُستبعد، لأن <bdi>COPD</bdi> و<bdi>asthma</bdi> لا يسببون <bdi>clubbing</bdi> أبدًا.",
    ],
    "when_changes": [
        "لو كان المريض نفس التدخين لكن بدون <bdi>clubbing</bdi>، الجواب يتحول لـ <bdi>COPD</bdi> كالسبب الأشيع.",
        "لو كان الشخص شاب عنده صفير متكرر مع محفزات والتاريخ يبدأ بعمر صغير، فكّر بـ <bdi>asthma</bdi> (بدون <bdi>clubbing</bdi>).",
    ],
    "rule": "مدخّن + <bdi>breathlessness</bdi> لوحده = <bdi>COPD</bdi>؛ مدخّن + <bdi>clubbing</bdi> جديد = <bdi>bronchial carcinoma</bdi> حتى يُستبعد.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-2015": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال تشخيص مريض مدخّن بسعال مُنتج متكرر لأكثر من موسم، مع <bdi>ABG</bdi> يثبّت احتباس <bdi>CO2</bdi> مزمن.",
    "clues": [
        ("20-pack-year smoking", "عامل خطر رئيسي لأمراض الرئة الانسدادية"),
        ("productive cough for 3 months", "يطابق التعريف السريري لـ <bdi>chronic bronchitis</bdi>"),
        ("similar attack last year", "يثبّت تكرار الحدث لسنتين متتاليتين، شرط التعريف"),
    ],
    "why_correct": [
        "«سعال مُنتج 3 أشهر» مع «نوبة مشابهة السنة الماضية» بمدخّن 20 <bdi>pack-year</bdi> هو التعريف السريري لـ <bdi>chronic bronchitis</bdi> (سعال مُنتج ≥3 أشهر لسنتين متتاليتين).",
        "<bdi>central cyanosis</bdi> مع <bdi>wheeze</bdi> يعطي صورة <bdi>blue bloater</bdi> الكلاسيكية.",
        "<bdi>ABG</bdi> يُظهر <bdi>PCO2 مرتفع (7.7)</bdi> مع <bdi>HCO3 مرتفع (36)</bdi> و<bdi>pH شبه طبيعي (7.35)</bdi>: هذا <bdi>chronic compensated respiratory acidosis</bdi> نمطي لـ <bdi>COPD</bdi>، مو حدث حاد.",
    ],
    "when_changes": [
        "لو كان الصفير متقطع مع استجابة كبيرة للموسّعات ويبدأ بعمر صغير، الجواب يتحول لـ <bdi>bronchial asthma</bdi>.",
        "لو كان الحدث حاد مفاجئ مع ألم جنبي وعامل خطر <bdi>DVT</bdi> و<bdi>PCO2 منخفض</bdi>، الجواب يصير <bdi>pulmonary embolism</bdi>.",
    ],
    "rule": "<bdi>HCO3</bdi> مرتفع + <bdi>PCO2</bdi> مرتفع + <bdi>pH</bdi> شبه طبيعي = احتباس <bdi>CO2</bdi> مزمن معوَّض، يعني <bdi>COPD/chronic bronchitis</bdi>، مو حدث حاد.",
    "comparison": {
        "headers": ["التشخيص", "PCO2", "السمة المميزة"],
        "rows": [
            ["Chronic bronchitis", "مرتفع، معوَّض", "سعال مُنتج ≥3 أشهر لسنتين"],
            ["Pulmonary embolism", "منخفض", "بداية حادة، ألم جنبي"],
            ["ILD", "طبيعي/منخفض", "سعال جاف، Velcro crackles"],
        ],
    },
    "labs": [
        ["ABG HCO3-", "36 mmol/L", "22-28 mmol/L"],
        ["ABG PCO2", "7.7 kPa", "4.7-6.0 kPa"],
        ["pH", "7.35", "7.36-7.45"],
        ["ABG PO2", "8.4 kPa", "10.6-14.2 kPa"],
    ],
    "guideline_note": None,
},

"AS-2016": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "سؤال الخطوة التالية بتقييم خطر قلبي عند شخص <bdi>asymptomatic</bdi> بخطر <bdi>intermediate</bdi>: المطلوب تحسين دقة التقييم، مو فحص لإثبات نقص تروية.",
    "clues": [
        ("intermediate risk", "خطر متوسط يحتاج توضيح إضافي قبل قرار العلاج"),
    ],
    "why_correct": [
        "المريض <bdi>asymptomatic</bdi> ونتيجة <bdi>Pooled Cohort Equations</bdi> وضعته بخطر <bdi>intermediate</bdi>، فالسؤال عن كيفية تحسين دقة تقدير الخطر لقرار بدء <bdi>statin</bdi>، مو عن تشخيص نقص تروية.",
        "<bdi>high-sensitivity C-reactive protein (hs-CRP)</bdi> هو أحد علامات «<bdi>risk-enhancing</bdi>» التي تساعد على حسم القرار نحو العلاج بالـ <bdi>statin</bdi>.",
    ],
    "when_changes": [
        "لو كان المريض عنده أعراض تشير لذبحة صدرية، الجواب يتحول لفحص تشخيصي لنقص التروية زي <bdi>stress echocardiography</bdi> أو <bdi>CCTA</bdi>.",
        "لو كان المطلوب فحص تصويري لتحسين تقدير الخطر (مو مصلي)، الجواب الصحيح يكون <bdi>coronary calcium score</bdi> لا <bdi>CT angiography</bdi>.",
    ],
    "rule": "كلمة «<bdi>asymptomatic</bdi>» تستثني كل فحوصات نقص التروية والتصوير التشريحي؛ اختر العلامة التي تحسّن تقدير الخطر (<bdi>hs-CRP</bdi>).",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-2017": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "سؤال الخطوة التالية بـ <bdi>acute decompensated heart failure</bdi> مع احتقان واضح، بغض النظر عن <bdi>ejection fraction</bdi>.",
    "clues": [
        ("left ventricular ejection fraction of 60%", "<bdi>EF</bdi> محفوظ (<bdi>HFpEF</bdi>)، لكن هذا لا يغيّر العلاج الحاد للاحتقان"),
        ("pulmonary edema", "دليل احتقان رئوي حاد"),
        ("Brain natriuretic peptide 900", "<bdi>BNP</bdi> مرتفع جدًا، يؤكد <bdi>heart failure</bdi>"),
    ],
    "why_correct": [
        "<bdi>orthopnea</bdi>، <bdi>raised CVP</bdi>، <bdi>crackles</bdi> بقاعدتي الرئة، <bdi>hepatomegaly</bdi>، <bdi>pitting edema</bdi>، <bdi>pulmonary edema</bdi> بالصورة، و<bdi>BNP 900</bdi>: كل هذا يعني <bdi>acute decompensated heart failure</bdi> مع احتقان شديد.",
        "<bdi>EF المحفوظ (60%)</bdi> يصنّفها <bdi>HFpEF</bdi>، لكن الخطوة الحادة لتخفيف الاحتقان واحدة بغض النظر عن <bdi>EF</bdi>: <bdi>loop diuretic (furosemide)</bdi>.",
    ],
    "when_changes": [
        "لو كان المريض مستقر وخارج فترة <bdi>decompensation</bdi> ومصنّف <bdi>HFrEF</bdi>، يُبدأ أو يُستمر <bdi>beta-blocker</bdi> كعلاج طويل الأمد.",
        "لو كان الهدف تحسين التكهّن طويل الأمد بـ <bdi>HFrEF</bdi> بعد الاستقرار، يُضاف <bdi>spironolactone</bdi>.",
    ],
    "rule": "علامات احتقان حاد (<bdi>orthopnea</bdi>، <bdi>crackles</bdi>، <bdi>edema</bdi>، <bdi>BNP</bdi> مرتفع) = <bdi>IV loop diuretic</bdi> فورًا، بغض النظر عن <bdi>EF</bdi>.",
    "comparison": None,
    "labs": [
        ["Sodium", "140 mmol/L", "134-146 mmol/L"],
        ["Potassium", "4 mmol/L", "3.5-5.1 mmol/L"],
        ["Creatinine", "88 umol/L", "44-115 umol/L"],
        ["BNP", "900 ng/L", "0-300 ng/L"],
        ["Ejection fraction", "60%", "50-70%"],
    ],
    "guideline_note": None,
},

"AS-2035": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال الفحص الأهم لتأكيد أساس <bdi>SLE</bdi> المناعي عند مريضة بصورة سريرية كلاسيكية.",
    "clues": [
        ("polyarthralgia, skin rash, mucosal ulcers", "صورة سريرية كلاسيكية لـ <bdi>SLE</bdi>"),
        ("malar rash", "علامة مميزة جدًا لـ <bdi>SLE</bdi>"),
        ("Complement C3 0.3", "<bdi>complement</bdi> منخفض، يدعم نشاط المرض المناعي"),
        ("most likely to confirm", "السؤال يبي الفحص الأهم لتأكيد الأساس المناعي"),
    ],
    "why_correct": [
        "عندها صورة <bdi>SLE</bdi> كلاسيكية: <bdi>malar rash</bdi>، <bdi>mucosal ulcers</bdi>، <bdi>arthritis</bdi>، <bdi>pancytopenia</bdi> خفيف، <bdi>C3/C4 منخفض</bdi>، و<bdi>lupus anticoagulant</bdi> إيجابي.",
        "<bdi>ANA (antinuclear antibodies)</bdi> إيجابي بنسبة عالية جدًا بمرضى <bdi>SLE</bdi>، فهو الفحص المستخدم لتثبيت الأساس المناعي؛ سلبيته تقريبًا تستبعد <bdi>SLE</bdi>.",
    ],
    "when_changes": [
        "لو السؤال يبي الفحص الأكثر تخصصًا (مو حساسية)، الجواب يتحول لـ <bdi>anti-dsDNA</bdi> أو <bdi>anti-Sm</bdi>.",
        "لو كانت الصورة تشمل علامات <bdi>myositis</bdi> أو <bdi>Raynaud</bdi> مع تداخل أمراض نسيج ضام، فكّر بـ <bdi>anti-RNP</bdi> (<bdi>MCTD</bdi>).",
    ],
    "rule": "«الأكثر حساسية/للفحص الأولي» = <bdi>ANA</bdi>؛ «الأكثر تخصصًا» = <bdi>anti-Sm</bdi> ثم <bdi>anti-dsDNA</bdi>.",
    "comparison": None,
    "labs": [
        ["Hb", "100 g/L", "120-160 g/L (female)"],
        ["Platelets", "100 x10^9/L", "150-400 x10^9/L"],
        ["WBC", "3 x10^9/L", "4.5-10.5 x10^9/L"],
        ["Complement C3", "0.3 g/L", "0.7-1.5 g/L"],
        ["Complement C4", "0.13 g/L", "0.15-0.45 g/L"],
    ],
    "guideline_note": None,
},

"AS-2038": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "سؤال عن مضاعفة التعرّض للإشعاع حسب التوقيت الزمني: أسبوعين بعد التعرّض يشير لفترة سمّية نقي العظم.",
    "clues": [
        ("Radiation exposure", "تعرّض إشعاعي كبير"),
        ("After 2 wks", "التوقيت أسبوعين بعد التعرّض، فترة كامنة متوسطة"),
    ],
    "why_correct": [
        "بعد تعرّض إشعاعي كبير، نقي العظم هو أكثر عضو حساس للإشعاع، ومتلازمة <bdi>hematopoietic syndrome</bdi> تظهر بعد فترة كامنة مع تراجع تدريجي بتعداد الدم.",
        "ظهور <bdi>fatigue</bdi> وفقدان الشهية وألم بطن «بعد أسبوعين» يطابق <bdi>bone marrow destruction</bdi> (فقر دم، نقص مناعة، نزف)، مو تأثير فوري أو متأخر جدًا.",
    ],
    "when_changes": [
        "لو كان رد فعل فوري بدقائق مع هبوط ضغط وطفح وصعوبة تنفس، الجواب يتحول لـ <bdi>anaphylactic shock</bdi>.",
        "لو كان ظهور المرض بعد سنوات من التعرّض، الجواب يصير سرطان متأخر (<bdi>malignant pattern</bdi>) ناتج عن الإشعاع.",
    ],
    "rule": "التوقيت يحدد الجواب: دقائق = حساسية/أرجية، أسابيع = فشل نقي العظم، سنوات = سرطان متأخر.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-2040": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "سؤال تحديد الشريان المسبب لـ <bdi>stroke</bdi> عند وجود فقدان سمع وضعف وجه بنفس الجهة (علامات جذع المخ المتجاورة).",
    "clues": [
        ("left-sided sensorineural hearing loss", "فقدان سمع من نوع <bdi>sensorineural</bdi> بنفس الجهة"),
        ("left-sided facial weakness", "ضعف الوجه بنفس جهة فقدان السمع، يدل على إصابة جذع المخ"),
    ],
    "why_correct": [
        "<bdi>labyrinthine artery</bdi> المغذّية للأذن الداخلية تنشأ عادة من <bdi>AICA</bdi>، وهي أيضًا تغذي الجزء الجانبي السفلي من الجسر (<bdi>pons</bdi>) حيث توجد نواة ومسار العصب الوجهي.",
        "احتشاء <bdi>AICA</bdi> يعطي فقدان سمع وضعف وجه بنفس الجهة (<bdi>ipsilateral CN VIII + CN VII</bdi>)، غالبًا مع دوخة وترنح، وهذا يطابق الصورة المذكورة بالضبط.",
    ],
    "when_changes": [
        "لو كان ضعف الوجه بالجهة المعاكسة لضعف الأطراف بدون فقدان سمع، الجواب يتحول لـ <bdi>MCA stroke</bdi>.",
        "لو كان فيه ترنح أحادي الجهة بدون فقدان سمع أو ضعف وجه، فكّر بـ <bdi>superior cerebellar artery</bdi>.",
    ],
    "rule": "فقدان سمع مرتبط بـ <bdi>stroke</bdi> = فكّر بـ <bdi>AICA</bdi>، لأن شريان الأذن الداخلية يتفرّع منه.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-2051": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال السبب الجرثومي الأشيع لـ <bdi>meningitis</bdi> عند بالغ، ويفترض وجود عامل خطر لـ <bdi>Listeria</bdi> ضمن تفاصيل السؤال المفقودة.",
    "clues": [
        ("Adult", "بالغ، يحدد المجموعة العمرية المناسبة للتفكير"),
        ("meningitis", "عدوى الأغشية السحائية"),
    ],
    "why_correct": [
        "الجواب المعتمد هنا هو <bdi>Listeria monocytogenes</bdi>، وهو السبب المناسب عندما يكون عند البالغ عامل خطر مثل عمر فوق 50، حمل، كبت مناعي، سكري، أو إدمان كحول.",
        "تفاصيل السؤال الأصلية غير مكتملة بالتفريغ، لكن الإجابة تدل على وجود عامل خطر لـ <bdi>Listeria</bdi> بالنسخة الأصلية، وهذا سبب إضافة <bdi>ampicillin</bdi> للعلاج التجريبي بهذه الفئات.",
    ],
    "when_changes": [
        "لو كان بالغ سليم بدون عوامل خطر، الجواب يتحول لـ <bdi>Streptococcus pneumoniae</bdi> كالسبب الأشيع عمومًا.",
        "لو كان المريض بعد جراحة عصبية أو عنده <bdi>shunt</bdi>، الجواب يصير <bdi>Staphylococcus</bdi> أو جراثيم <bdi>Gram negative</bdi>.",
    ],
    "rule": "بدون عامل خطر = <bdi>pneumococcus</bdi>؛ عمر فوق 50، حمل، أو كبت مناعي = يتحول الجواب لـ <bdi>Listeria</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-2055": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "سؤال أفضل خافض ضغط للوقاية الثانوية بعد <bdi>TIA</bdi>.",
    "clues": [
        ("after TIA", "سياق الوقاية الثانوية من السكتة"),
    ],
    "why_correct": [
        "للوقاية الثانوية «بعد <bdi>TIA</bdi>» أو السكتة، خفض الضغط بـ <bdi>ACE inhibitor</bdi> (غالبًا مع <bdi>thiazide-like diuretic</bdi>) له دليل تجارب سريرية قوي بتقليل تكرار السكتة، فـ <bdi>ramipril</bdi> هو الخيار المفضل.",
        "<bdi>ACE inhibitors</bdi> أيضًا تحمي الكلى والقلب، وهذا مفيد لأن كثير من مرضى <bdi>TIA</bdi> عندهم سكري أو مرض وعائي مصاحب.",
    ],
    "when_changes": [
        "لو كان المريض عنده مؤشر آخر (<bdi>post-MI</bdi>، ذبحة صدرية، أو <bdi>HFrEF</bdi>)، يُضاف <bdi>beta-blocker</bdi> لكن ليس كخيار أول للوقاية من السكتة.",
    ],
    "rule": "<bdi>beta-blockers</bdi> ضعيفة بالوقاية من السكتة مقارنة بغيرها؛ بعد <bdi>TIA/stroke</bdi> اختر <bdi>ACE inhibitor</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},

"AS-2060": {
    "correct_letter": "C",
    "self_judged": True,
    "idea": "سؤال اختيار أفضل موقع خزعة لمريض عنده كتلة بمنتصف الرئة مع تضخم عقد <bdi>hilar</bdi>، والخيارات المتاحة لا تشمل العقدة العنقية السطحية السهلة.",
    "clues": [
        ("hilar lymphadenopathy", "تضخم عقد بمنطقة <bdi>hilum</bdi> يُفضَّل الوصول له عن طريق القصبات"),
    ],
    "why_correct": [
        "المريض عنده تضخم عقد عنقية وكبد وتضخم عقد <bdi>hilar</bdi> وكتلة بمنتصف الرئة، لكن الخيارات المعطاة لا تشمل خزعة العقدة العنقية السطحية (وهي أسهل خيار لو كانت متوفرة).",
        "من بين الخيارات المتاحة، <bdi>transbronchial biopsy</bdi> هي الأنسب للوصول لكتلة مركزية بمنتصف الرئة مع تضخم عقد <bdi>hilar</bdi>، لأن القصبات توصل مباشرة لهذه المنطقة.",
        "<bdi>liver biopsy</bdi> يكون مفيد فقط لو كانت هناك آفة كبدية بؤرية واضحة بدون خيار أسهل، و<bdi>pleural biopsy</bdi> يحتاج انصباب جنبي غير مذكور هنا.",
    ],
    "when_changes": [
        "لو كان الخيار المعطى يشمل خزعة العقدة العنقية السطحية، هذا يكون الخيار الأسهل والأفضل أولاً.",
        "لو كانت الآفة بمحيط الرئة لا بمركزها، الجواب يتحول لـ <bdi>CT-guided transthoracic biopsy</bdi>.",
    ],
    "rule": "تضخم عقد <bdi>hilar</bdi> أو كتلة مركزية = يُصل لها عبر القصبات (<bdi>transbronchial/EBUS</bdi>)؛ الجنب يُخزع فقط لو كان هناك انصباب.",
    "comparison": None,
    "labs": None,
    "guideline_note": "هذا سؤال لم يحدد المصدر له جوابًا مؤكدًا (<bdi>answer_letter</bdi> فاضي)؛ الاختيار هنا مبني على أفضل الخيارات المتاحة سريريًا.",
},
}

WHY_WRONG = {

"AS-1851": {
    "A": "<bdi>ECG</bdi> يكون الصحيح لو كان الحدث احتمال <bdi>syncope</bdi> أو اضطراب نظم؛ هنا الوصف واضح أنه <bdi>generalized tonic-clonic seizure</bdi>.",
    "B": "<bdi>EEG</bdi> جزء من كل <bdi>workup</bdi> لأول <bdi>seizure</bdi>، لكنه يجي بعد الصورة، لأنه يصنّف النوبة ويقدّر خطر التكرار مو يستبعد سبب عضوي عاجل.",
    "D": "<bdi>lumbar puncture</bdi> يكون الصحيح مع حمى أو علامات <bdi>meningism</bdi> أو ضعف مناعة، أو شك بـ <bdi>SAH</bdi> مع صورة طبيعية؛ ماكو شي من هذا هنا، والتصوير يسبق الـ <bdi>LP</bdi>.",
},
"AS-1852": {
    "A": "<bdi>echocardiogram</bdi> غير مطلوب قبل تأكيد التشخيص؛ يُطلب مع شك بـ <bdi>LVH</bdi> أو نفخة قلبية أو فشل قلب.",
    "B": "البدء بعلاج دوائي من قراءة وحيدة يحمل خطر علاج <bdi>white coat hypertension</bdi>؛ العلاج الفوري محجوز لضغط مرتفع جدًا أو <bdi>end organ damage</bdi>.",
    "D": "الانتظار 3 شهور لقراءة عيادة أخرى يؤخر التشخيص ولا يستبعد أثر <bdi>white coat</bdi>؛ الموصى به هو <bdi>ABPM</bdi> أو قياس منزلي.",
},
"AS-1853": {
    "A": "<bdi>migraine</bdi> غير مرجح بدون صداع، والعجز البؤري الثابت عند مسن بعوامل خطر وعائية يُعتبر <bdi>stroke</bdi> حتى يُستبعد.",
    "B": "<bdi>right MCA stroke</bdi> يعطي ضعف بالوجه والذراع أكثر من الساق (مع إهمال لو نصف غير سائد)؛ هنا الذراع طبيعية وفقط الساق متأثرة.",
    "D": "<bdi>basilar artery stroke</bdi> يعطي علامات جذع المخ (شلل أعصاب قحفية، دوخة، ترنح، عجز ثنائي أو متصالب، تراجع وعي)، مو عجز أحادي بالساق فقط.",
},
"AS-1854": {
    "A": "<bdi>salt-wasting nephropathy</bdi> صحيح مع مرض كلوي أنبوبي يسبب <bdi>hypovolemic hyponatremia</bdi> مع صوديوم بولي مرتفع؛ ماكو دليل على مرض كلوي أو نقص حجم هنا.",
    "B": "<bdi>excessive water consumption</bdi> (<bdi>primary polydipsia</bdi>) يصح بمرضى نفسيين يشربون كميات كبيرة من الماء مع بول مخفف جدًا؛ هنا السبب العضوي (الورم) أوضح وأشيع.",
    "C": "زيادة استهلاك المشروبات الغازية ليست سبب معروف لـ <bdi>hyponatremia</bdi> بهذا السياق.",
},
"AS-1855": {
    "A": "<bdi>diuretics</bdi> تخفض الضغط لكن بدون أثر مضاد لـ <bdi>proteinuria</bdi>؛ تُستخدم كإضافة (<bdi>step 2</bdi>) مو كخيار أول بمريض سكري.",
    "B": "<bdi>calcium channel blockers</bdi> ما لها أثر حماية كلوية؛ تكون أول خيار بغير السكريين فوق 55 سنة أو من أصل أفريقي/كاريبي، أو كإضافة.",
    "C": "<bdi>beta-blockers</bdi> لا تحمي الكلى وممكن تخفي علامات <bdi>hypoglycemia</bdi> بمريض على <bdi>insulin</bdi>؛ تُستخدم لأسباب محددة زي بعد نوبة قلبية.",
},
"AS-1878": {
    "B": "<bdi>methotrexate</bdi> ليس علاج معياري لـ <bdi>autoimmune hepatitis</bdi> وهو نفسه سام للكبد؛ يُستخدم لـ <bdi>rheumatoid arthritis</bdi> أو كإضافة بـ <bdi>SLE</bdi>.",
    "C": "<bdi>vitamin E مع weight loss</bdi> علاج <bdi>NASH</bdi>؛ السمنة والكبد اللامع بالسونار تشتيت، لأن الخزعة أظهرت <bdi>interface hepatitis</bdi> بخلايا بلازمية، مو <bdi>steatohepatitis</bdi>.",
    "D": "<bdi>ursodeoxycholic acid</bdi> هو الخيار الأول لـ <bdi>primary biliary cholangitis</bdi> (نمط <bdi>cholestatic</bdi> مع <bdi>ALP</bdi> مرتفع جدًا و<bdi>AMA +</bdi>)؛ النمط هنا <bdi>hepatocellular</bdi> مع <bdi>ALP</bdi> مرتفع بشكل خفيف فقط.",
},
"AS-1897": {
    "A": "<bdi>simple face mask</bdi> يعطي <bdi>FiO2</bdi> متغيّر وغير دقيق ويحتاج تدفق عالي لتجنب إعادة استنشاق <bdi>CO2</bdi>؛ يناسب حاجة أوكسجين متوسطة قصيرة الأمد بدون خطر احتباس <bdi>CO2</bdi>.",
    "B": "<bdi>rebreathing bag</bdi> يعطي أوكسجين عالي وغير منضبط، يزيد خطر <bdi>CO2 narcosis</bdi> بمرضى <bdi>COPD</bdi>؛ يُستخدم بحالات نقص أوكسجين حاد شديد بدون خطر احتباس <bdi>CO2</bdi>.",
    "C": "<bdi>nasal cannula</bdi> مقبول بتدفق منخفض لكن <bdi>FiO2</bdi> يتغيّر حسب نمط تنفس المريض، فهو أقل دقة؛ يناسب المرضى المستقرين أو الأوكسجين المنزلي طويل الأمد.",
},
"AS-1919": {
    "B": "<bdi>lorazepam</bdi> وغيره من <bdi>benzodiazepines</bdi> ممكن يزيدون <bdi>delirium</bdi> ويسببون هياج أو تهدئة متناقضة بكبار السن؛ تكون الخيار الأول فقط بانسحاب كحول أو <bdi>benzodiazepines</bdi> أو نوبات، أو كإضافة بالهياج الشديد المقاوم.",
},
"AS-1948": {
    "A": "<bdi>lymphedema</bdi> تورّم مزمن غير مؤلم يتطور ببطء (بعد جراحة عقد لمفية أو علاج إشعاعي)، مو تورّم حاد مؤلم ومحمر.",
    "B": "<bdi>cellulitis</bdi> يصح مع حمى ومدخل جلدي للعدوى واحمرار متمدد؛ هنا ماكو مدخل عدوى وفيه عاملان قويان لـ <bdi>VTE</bdi>.",
    "C": "<bdi>ruptured Baker's cyst</bdi> يصح مع ألم مفاجئ بالربلة عند مريض بخشونة ركبة أو كيس معروف؛ ماكو تاريخ ركبة هنا.",
},
"AS-1951": {
    "A": "<bdi>ciprofloxacin</bdi> تغطيته ضعيفة ضد <bdi>Streptococcus</bdi>، فهو خيار ضعيف لـ <bdi>cellulitis</bdi> البسيطة؛ يُختار لعدوى <bdi>Gram negative</bdi> زي <bdi>pyelonephritis</bdi> أو <bdi>Pseudomonas</bdi>.",
    "C": "<bdi>vancomycin</bdi> يُحفظ لـ <bdi>cellulitis</bdi> الشديدة أو مع <bdi>sepsis</bdi>، <bdi>MRSA</bdi> معروف، أو فشل العلاج الأول؛ حالة بعمر 2 يوم بدون صدمة لا تحتاجه أولاً.",
    "D": "<bdi>meropenem</bdi> مضاد واسع الطيف محجوز لـ <bdi>febrile neutropenia</bdi> أو عدوى <bdi>Gram negative</bdi> شديدة مقاومة؛ مبالغ فيه لـ <bdi>cellulitis</bdi> غير معقدة.",
},
"AS-1975": {
    "A": "<bdi>acute active hepatitis B</bdi> يحتاج <bdi>IgM anti-HBc</bdi> إيجابي مع عدوى حديثة، لكن هنا <bdi>IgG</bdi> والتعرّض من <bdi>10 سنوات</bdi>، فهذا نمط <bdi>chronic</bdi> مو <bdi>acute</bdi>.",
},
"AS-1977": {
    "A": "العلاج الرباعي لوحده صحيح لـ <bdi>pulmonary TB</bdi>، لكن بـ <bdi>TB meningitis</bdi> يكون ناقص بدون إضافة <bdi>corticosteroid</bdi>.",
    "B": "<bdi>diuretics</bdi> ليست جزء من علاج <bdi>TB meningitis</bdi> القياسي؛ <bdi>hydrocephalus</bdi> كمضاعفة تُعالج بشكل منفصل (تصريف أو <bdi>shunt</bdi>) لو انسدادي، مو بمدّرات بشكل تلقائي.",
    "C": "<bdi>acyclovir</bdi> علاج لـ <bdi>HSV/VZV encephalitis</bdi> ويُعطى تجريبيًا فقط لحين استبعاد السبب الفيروسي؛ هنا <bdi>PCR</bdi> أكّد السبب السلي.",
},
"AS-1978": {
    "A": "<bdi>meropenem</bdi> كاربابينيم واسع الطيف محجوز لـ <bdi>hospital-acquired pneumonia</bdi> أو خطر <bdi>Pseudomonas</bdi>؛ ماكو شي من هذا بالسؤال.",
    "C": "<bdi>vancomycin</bdi> يغطي <bdi>MRSA</bdi> فقط، يُضاف مع عوامل خطر محددة (<bdi>MRSA</bdi> سابق، مضادات وريدية حديثة، <bdi>pneumonia</bdi> ناخرة شديدة)؛ وهو لا يغطي <bdi>Gram negatives</bdi>.",
    "D": "<bdi>oseltamivir</bdi> علاج للإنفلونزا؛ وجود <bdi>consolidation</bdi> فصّي مع سعال مُنتج يرجّح عدوى بكتيرية، وهذا المزيج يترك <bdi>pneumococcus</bdi> بدون تغطية كافية.",
},
"AS-1981": {
    "A": "<bdi>atrial fibrillation</bdi> هو السبب <bdi>cardioembolic</bdi> الأشيع بكبار السن، لكن ماكو دليل عليه بشاب سليم 27 سنة، وهو لا يفسر رابط الخثرة الوريدية.",
    "B": "<bdi>carotid artery stenosis</bdi> سبب تصلّب شرايين بمرضى مسنين بعوامل خطر وعائية (تدخين، سكري، دهون)، مو شاب سليم.",
    "D": "<bdi>hypertrophic cardiomyopathy</bdi> يظهر بإغماء بالجهد أو نفخة أو موت مفاجئ بالشباب؛ الـ <bdi>stroke</bdi> نادر معها وقصة <bdi>DVT/PE</bdi> تشير لسبب آخر.",
},
"AS-2005": {
    "A": "<bdi>multiple sclerosis</bdi> (<bdi>optic neuritis</bdi>) يتطور بأيام وغالبًا مؤلم عند الحركة ويتعافى بأسابيع، مو بـ 20 دقيقة.",
    "B": "<bdi>retinal detachment</bdi> يعطي ومضات وذباب طائر وستار دائم بالمجال البصري يحتاج جراحة عاجلة، ولا يتعافى تلقائيًا.",
    "C": "<bdi>conversion disorder</bdi> تشخيص استثناء بوجود محفزات نفسية؛ حدث وعائي حاد يتعافى بالكامل بمريضة سكري يجب تدبيره كـ <bdi>TIA</bdi> أولاً.",
},

}

HIGHLIGHT_TERMS = {
"AS-1851": ["first-time generalized tonic-clonic seizure", "Neurological findings are unremarkable"],
"AS-1852": ["elevated blood pressure during a routine checkup"],
"AS-1853": ["confused and behaving in a strange way", "Left leg power is 2/5", "decreased sensation in the left leg"],
"AS-1854": ["glioblastoma multiforme", "hyponatremia"],
"AS-1855": ["type I diabetes mellitus", "BP:150/90"],
"AS-1878": ["jaundice", "SLE", "ANA: 1:640 (High)", "Interphase hepatitis with plasma cells"],
"AS-1897": ["Pulmonary Disease"],
"AS-1919": ["end-stage metastatic cancer", "palliative care", "aggressive and confused"],
"AS-1948": ["pancreatic cancer", "swollen left lower limb during hospitalization", "tender, erythematous swelling"],
"AS-1951": ["long standing DM", "cellulitis"],
"AS-1975": ["10 years ago", "HBs Ag +ve", "HBe Ag +ve"],
"AS-1977": ["headache for 3 months", "Mycobacterium tuberculosis"],
"AS-1978": ["productive cough, fever, and dyspnea for 3 days", "consolidation at the right lower lung field", "empiric"],
"AS-1981": ["femur fracture", "pulmonary embolism", "left cerebral infarction"],
"AS-2005": ["sudden left eye visual loss for 20 minutes", "vision returned to normal"],
}

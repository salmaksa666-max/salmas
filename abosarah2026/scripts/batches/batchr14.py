# -*- coding: utf-8 -*-
# Batch r14: ENT (AS-1226.. AS-2379) + Pediatrics (AS-0017.. AS-0510)

EXPLANATIONS = {
"AS-1226": {
    "correct_letter": "A",
    "self_judged": True,
    "idea": "السؤال عن <bdi>epistaxis</bdi> (نزيف الأنف) ويبي أفضل <bdi>position</bdi> للمريض كإسعاف أولي.",
    "clues": [
        ("epistaxis", "نزيف أنف، أول خطوة هي <bdi>position</bdi> صحيح قبل أي إجراء"),
    ],
    "why_correct": [
        "<bdi>sitting and leaning forward</bdi> هو الوضع الصحيح لأي مريض عنده <bdi>epistaxis</bdi>: الجلوس مع إنحناء للأمام يخلي الدم ينزل من الأنف للخارج ومايدخل الحلق أو المعدة أو <bdi>airway</bdi>.",
        "بعد الوضع الصحيح نسوي <bdi>continuous pressure</bdi> على الجزء الطري من الأنف (مو العظم) لمدة 10-15 دقيقة.",
        "الوضع الخاطئ المشهور هو الإنحناء للخلف، لأنه يخلي الدم يروح للمعدة (قيء) أو <bdi>airway</bdi> (استنشاق).",
    ],
    "when_changes": [
        "لو النزيف مستمر مع هذا الوضع والضغط، الخطوة التالية <bdi>topical vasoconstrictor</bdi> أو <bdi>cautery</bdi> لنقطة النزيف الظاهرة.",
        "لو النزيف خلفي (<bdi>posterior</bdi>) وشديد، نحتاج <bdi>packing</bdi> خلفي أو بالون وإدخال المريض للمستشفى.",
    ],
    "rule": "في أي <bdi>epistaxis</bdi>، الوضع الصحيح دايمًا <bdi>sitting and leaning forward</bdi> مع ضغط مستمر على الجزء الطري من الأنف؛ الإنحناء للخلف غلط كلاسيكي.",
    "comparison": None,
    "labs": None,
    "guideline_note": "المصدر ما حدد جواب مؤكد لهذا السؤال، فالجواب هنا باجتهاد <bdi>clinical</bdi> مباشر حسب <bdi>first aid</bdi> المعروف لـ<bdi>epistaxis</bdi>.",
},
"AS-1270": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "السؤال عن طفل عنده <bdi>URTI</bdi> تحسّن، وبعدها رجعت الأعراض بشكل أسوأ (<bdi>double worsening</bdi>)، وهذا نمط كلاسيكي لـ<bdi>acute bacterial sinusitis</bdi>.",
    "clues": [
        ("3 days after resolving", "الأعراض تحسّنت وبعدها رجعت أسوأ، يعني <bdi>double worsening</bdi>"),
        ("purulent nasal discharge and frontal tenderness", "إفرازات <bdi>purulent</bdi> مع ألم بالجبهة، علامات <bdi>bacterial sinusitis</bdi>"),
    ],
    "why_correct": [
        "النمط هنا <bdi>double worsening</bdi>: <bdi>URTI</bdi> فايروسي تحسّن، وبعدها الطفل ساء مرة ثانية بإفرازات <bdi>purulent</bdi> وألم بالجبهة.",
        "تدهور جديد بعد تحسّن مع <bdi>sinus tenderness</bdi> هو معيار كلاسيكي لـ<bdi>acute bacterial sinusitis</bdi> بعد <bdi>viral illness</bdi>.",
        "التورم الفايروسي بالأغشية يسد تصريف الجيوب ويسمح بعدوى بكتيرية ثانوية.",
    ],
    "when_changes": [
        "لو الأعراض مستمرة أكثر من 10 أيام بدون تحسّن من البداية (بدون تحسّن ثم تدهور)، الجواب برضو <bdi>bacterial sinusitis</bdi> لكن بنمط <bdi>persistent</bdi> مو <bdi>double worsening</bdi>.",
        "لو الإفرازات صافية مع حكة وعطس بدون حمى، الجواب يصير <bdi>allergic rhinosinusitis</bdi>.",
    ],
    "rule": "<bdi>double worsening</bdi> (تحسّن ثم تدهور بإفرازات <bdi>purulent</bdi> وألم بالجيوب) = <bdi>acute bacterial sinusitis</bdi>، مو مجرد وجود إفرازات <bdi>purulent</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1286": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طفل عنده 4 نوبات <bdi>adenotonsillitis</bdi> بالسنة، والسؤال يبي الإدارة الصحيحة قبل ما نفكر بجراحة.",
    "clues": [
        ("4 recurrent adenotonsillitis within one academic year", "4 نوبات فقط، أقل من حد <bdi>Paradise criteria</bdi> للجراحة"),
    ],
    "why_correct": [
        "4 نوبات بالسنة أقل من حد <bdi>tonsillectomy</bdi> (7 بالسنة، أو 5 لمدة سنتين، أو 3 لمدة 3 سنوات)، فالإدارة <bdi>watchful waiting</bdi> ووقاية.",
        "أغلب النوبات تنتقل بالرذاذ ولمس الأيدي بالمدرسة، فـ<bdi>hand washing</bdi> و<bdi>respiratory etiquette</bdi> هي النصيحة الصحيحة للأبوين القلقين.",
    ],
    "when_changes": [
        "لو عدد النوبات وصل 7 بسنة واحدة (أو حسب <bdi>Paradise criteria</bdi>)، الجواب يصير <bdi>tonsillectomy</bdi>.",
        "لو عنده <bdi>obstructive sleep apnea</bdi> أو خُراج حول اللوز (<bdi>peritonsillar abscess</bdi>) متكرر، الجواب برضو <bdi>tonsillectomy</bdi> بدون اعتبار للعدد.",
    ],
    "rule": "أي سؤال عن <bdi>recurrent tonsillitis</bdi>، أول خطوة عد النوبات وقارنها بـ<bdi>Paradise criteria</bdi>؛ تحت الحد = <bdi>hygiene</bdi> ومراقبة، مو مضاد حيوي وقائي ومو جراحة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1337": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "رجل 40 سنة معروف بـ<bdi>hypertension</bdi> عنده نزيف أنف شديد ومستمر، والسؤال يبي نفرّق بين <bdi>anterior</bdi> و<bdi>posterior epistaxis</bdi>.",
    "clues": [
        ("profuse nosebleeding over 30 minutes", "نزيف شديد ومستمر، يرجّح <bdi>posterior epistaxis</bdi>"),
        ("known case of hypertension", "<bdi>hypertension</bdi> هي العامل الخطر الكلاسيكي لـ<bdi>posterior epistaxis</bdi>"),
    ],
    "why_correct": [
        "رجل 40 سنة معروف <bdi>hypertensive</bdi> عنده نزيف شديد لمدة 30 دقيقة وصار <bdi>pale and anxious</bdi>، هذا يناسب <bdi>posterior epistaxis</bdi> من فروع <bdi>sphenopalatine artery</bdi>.",
        "النزيف الأمامي (<bdi>Little's area</bdi>) عادة خفيف وينوقف بالضغط؛ النزيف الشديد المستمر بشخص كبير وعنده <bdi>hypertension</bdi> يوجّه للخلفي.",
        "<bdi>recurrent nasal congestion</bdi> بالقصة تفصيل غير مهم، مو له علاقة مباشرة بسبب النزيف.",
    ],
    "when_changes": [
        "لو المريض شاب بعمر البلوغ وعنده <bdi>unilateral nasal obstruction</bdi> مع نزيف متكرر، الجواب يصير <bdi>juvenile nasopharyngeal angiofibroma</bdi>.",
        "لو عنده <bdi>telangiectasias</bdi> بالشفايف واللسان مع قصة عائلية، الجواب يصير <bdi>hereditary hemorrhagic telangiectasia</bdi>.",
    ],
    "rule": "نزيف أنف شديد ومستمر بشخص كبير بالسن معروف <bdi>hypertensive</bdi> = <bdi>posterior epistaxis</bdi> من <bdi>sphenopalatine artery</bdi>، مو <bdi>anterior bleed</bdi> العادي.",
    "comparison": {
        "headers": ["النوع", "المكان", "الفئة النموذجية"],
        "rows": [
            ["<bdi>Anterior</bdi>", "<bdi>Little's area</bdi>", "أطفال وشباب، نزيف خفيف"],
            ["<bdi>Posterior</bdi>", "<bdi>sphenopalatine artery</bdi>", "كبار السن، <bdi>hypertension</bdi>، نزيف شديد"],
        ],
    },
    "labs": None,
    "guideline_note": None,
},
"AS-1414": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طفل عنده أعراض <bdi>sinusitis</bdi> ما تحسّنت مع عدة كورسات مضاد حيوي، والسؤال يبي الخطوة التالية الصحيحة.",
    "clues": [
        ("foul-smelling breath", "رائحة فم كريهة، يرجّح جسم غريب أو عدوى مزمنة بالجيوب"),
        ("worsened after 14 days, despite multiple courses of antibiotics", "فشل عدة كورسات مضاد حيوي، يعني نحتاج نشوف السبب مباشرة"),
    ],
    "why_correct": [
        "أعراض الجيوب تدهورت بعد 14 يوم مع عدة كورسات مضاد حيوي فاشلة، يعني <bdi>refractory sinusitis</bdi> ومو منطقي نعيد المضاد الحيوي عشوائي.",
        "<bdi>nasal endoscopy</bdi> تسمح بفحص مباشر للسبب (جسم غريب، تضخم اللحمية، <bdi>polyps</bdi>، انسداد تشريحي) وأخذ <bdi>culture</bdi> موجه للعلاج.",
    ],
    "when_changes": [
        "لو هذا أول فشل بعد 72 ساعة من مضاد حيوي، الخطوة تكون توسيع المضاد لـ<bdi>amoxicillin clavulanate</bdi> مو <bdi>endoscopy</bdi> مباشرة.",
        "لو فيه علامات بالعين أو عصبية، الخطوة تصير <bdi>contrast CT</bdi> ومضاد حيوي وريدي عاجل.",
    ],
    "rule": "فشل عدة كورسات مضاد حيوي بـ<bdi>sinusitis</bdi> يعني لازم نبحث عن السبب (<bdi>nasal endoscopy</bdi> أو <bdi>CT</bdi>)، مو نكرر مضاد حيوي آخر.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-1835": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "طفل عنده جسم غريب (عملة) داخل <bdi>trachea</bdi> مؤكد بالصورة، والسؤال يبي الإدارة النهائية (<bdi>definitive</bdi>).",
    "clues": [
        ("coin in the trachea", "جسم غريب مؤكد بمجرى الهواء، هذا طارئ ويحتاج إزالة فورية"),
    ],
    "why_correct": [
        "طفل كان يلعب بعملات وصار عنده <bdi>SOB</bdi> وأكدت الصورة وجود عملة بـ<bdi>trachea</bdi>، هذا جسم غريب بمجرى الهواء مؤكد.",
        "الإدارة النهائية <bdi>definitive</bdi> هي <bdi>rigid bronchoscopy</bdi> تحت تخدير عام، تؤكد التشخيص وتسحب الجسم بنفس الإجراء.",
        "جسم غريب بـ<bdi>trachea</bdi> ممكن يتحرك ويسد مجرى الهواء بالكامل، فما نتركه يمر لوحده.",
    ],
    "when_changes": [
        "لو العملة بالمعدة أو المريء السفلي وطفل مستقر بدون أعراض، الجواب يصير <bdi>observation</bdi> ومتابعة بصور متكررة.",
        "لو الجسم الغريب بطارية زر (<bdi>button battery</bdi>) بالمريء، الجواب يصير إزالة عاجلة فورًا بسبب خطر التآكل.",
    ],
    "rule": "جسم غريب مؤكد بمجرى الهواء (<bdi>trachea</bdi>) = <bdi>rigid bronchoscopy</bdi> فورًا للتشخيص والسحب بنفس الوقت؛ لا تطمينة ولا متابعة.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2075": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "مريض عنده <bdi>anterior epistaxis</bdi> مع <bdi>severe hypertension</bdi> وعلى <bdi>aspirin</bdi>، والتصوير سليم، والسؤال يبي الخطوة التالية لإيقاف النزيف.",
    "clues": [
        ("severe hypertension", "عامل يخلي النزيف أصعب بالسيطرة، يُعالج بالتوازي"),
        ("anterior epistaxis", "النزيف أمامي، يحتاج تحديد موضع النزيف محلياً"),
        ("aspirin", "مضاد صفائح يزيد صعوبة إيقاف النزيف"),
        ("Imaging normal", "ما فيه كسر أو ورم، فالخطوة التالية سريرية مو تصوير إضافي"),
    ],
    "why_correct": [
        "<bdi>anterior epistaxis</bdi> مع تصوير سليم يحتاج تحديد نقطة النزيف والسيطرة عليها محليًا، فالخطوة التالية <bdi>nasal endoscopy</bdi> (بعد الإسعاف الأولي بالضغط) لتحديد المصدر (عادة <bdi>Little's area</bdi>) وعلاجه بـ<bdi>cautery</bdi> أو <bdi>packing</bdi>.",
        "<bdi>severe hypertension</bdi> و<bdi>aspirin</bdi> يصعّبون إيقاف النزيف، لكن يُعالَجون بالتوازي (ضبط ضغط، مسكنات) مو بديل عن السيطرة المحلية.",
    ],
    "when_changes": [
        "لو كان النزيف خلفي (<bdi>posterior</bdi>) أو متكرر بدون سبب واضح، يصير الجواب <bdi>facial CT</bdi> لاستبعاد ورم أو كسر.",
        "لو ضغط المريض غير مستقر ويهدد حياته، يصير التركيز أولًا على ضبط <bdi>vital signs</bdi> قبل أي إجراء محلي.",
    ],
    "rule": "<bdi>hypertension</bdi> و<bdi>aspirin</bdi> عوامل تُعالَج بالتوازي؛ الخطوة التالية بـ<bdi>epistaxis</bdi> مع تصوير سليم تبقى تحديد وعلاج نقطة النزيف بـ<bdi>endoscopy</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2090": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "طفل عنده إفرازات أذن وحمى شديدة، والسؤال عن السبب الأكثر شيوعًا لـ<bdi>otitis media</bdi> عند الأطفال.",
    "clues": [
        ("ear discharge", "إفرازات أذن، يرجّح <bdi>acute otitis media</bdi> مع تمزق الطبلة"),
        ("high-grade fever", "حمى شديدة، يدعم عدوى بكتيرية فعالة"),
    ],
    "why_correct": [
        "إفرازات أذن مع حمى شديدة يناسب <bdi>acute otitis media</bdi> مع تمزق طبلة الأذن وخروج الإفرازات.",
        "أكثر فئة سبب شائعة لـ<bdi>pediatric AOM</bdi> هي <bdi>bacterial</bdi>، وعلى رأسها <bdi>Streptococcus pneumoniae</bdi> ثم <bdi>H. influenzae</bdi> و<bdi>Moraxella catarrhalis</bdi>.",
        "الفايروسات ممكن تسبق المرض وتهيّج <bdi>eustachian tube</bdi>، لكن العدوى القيحية نفسها غالبًا بكتيرية.",
    ],
    "when_changes": [
        "لو الخيارات كلها فايروسات محددة، الجواب يصير <bdi>rhinovirus</bdi> (الأكثر شيوعًا بين الفايروسات).",
        "لو السؤال عن <bdi>otitis externa</bdi> مو <bdi>otitis media</bdi>، الجواب يتغير لـ<bdi>Pseudomonas aeruginosa</bdi>.",
    ],
    "rule": "أكثر سبب لـ<bdi>pediatric acute otitis media</bdi> هو <bdi>bacterial</bdi> وعلى رأسه <bdi>Streptococcus pneumoniae</bdi>؛ لو الخيارات فايروسات فقط، الجواب <bdi>rhinovirus</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2268": {
    "correct_letter": "C",
    "self_judged": False,
    "idea": "نفس فكرة <bdi>recurrent tonsillitis</bdi> تحت حد الجراحة، والإدارة الصحيحة <bdi>hygiene</bdi> مو جراحة أو مضاد حيوي وقائي.",
    "clues": [
        ("4 episodes of tonsillitis", "4 نوبات فقط، أقل من <bdi>Paradise criteria</bdi>"),
        ("now doing well", "الطفل حاليًا بخير، مافيه مضاعفات تستدعي تدخل عاجل"),
    ],
    "why_correct": [
        "4 نوبات <bdi>tonsillitis</bdi> مع طفل الآن بخير لا تصل حد <bdi>tonsillectomy</bdi>، فالإدارة محافِظة: مراقبة ومنع انتقال العدوى.",
        "<bdi>hand hygiene</bdi> هي الوسيلة الأبسط والأكثر فعالية لتقليل انتقال العدوى الفايروسية والسترپتوكوكية المسؤولة عن <bdi>recurrent tonsillitis</bdi>.",
    ],
    "when_changes": [
        "لو عدد النوبات وصل 7 بسنة، الجواب يصير <bdi>tonsillectomy</bdi> حسب <bdi>Paradise criteria</bdi>.",
        "لو السؤال عن وقاية من <bdi>rheumatic fever</bdi> بعد عدوى <bdi>streptococcal</bdi> مؤكدة، يصير الجواب <bdi>penicillin prophylaxis</bdi>، مو هنا.",
    ],
    "rule": "عد نوبات <bdi>tonsillitis</bdi> قبل أي قرار: أقل من حد <bdi>Paradise criteria</bdi> = <bdi>hand hygiene</bdi> ومراقبة، مو جراحة ومو مضاد حيوي وقائي.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2305": {
    "correct_letter": "C",
    "self_judged": True,
    "idea": "طفل 10 سنوات عنده أعراض <bdi>sinusitis</bdi> بعد <bdi>URTI</bdi> بيومين فقط مع ألم بالخد، والسؤال عن أفضل إدارة تالية.",
    "clues": [
        ("frontal headache, fever, and stuffed nose", "أعراض جيوب جديدة"),
        ("left cheek tenderness", "ألم موضعي يدعم إصابة الجيوب الفكية"),
    ],
    "why_correct": [
        "القصة فيها <bdi>URTI</bdi> فايروسي قبل يومين وبعدها ألم بالخد وحمى وصداع جبهي، وهذا نمط <bdi>severe onset</bdi> (حمى عالية مع ألم موضعي شديد بأول الأعراض)، فيعتبر <bdi>bacterial sinusitis</bdi> ويحتاج مضاد حيوي.",
        "<bdi>Amoxicillin-clavulanate</bdi> خيار منطقي لـ<bdi>bacterial sinusitis</bdi> خصوصًا لو فيه عوامل خطر مقاومة أو أعراض شديدة.",
        "مجرد الألم الموضعي بدون انتظار 10 أيام ما يكفي وحده، لكن مع الحمى والصداع الشديد من البداية يرجّح البكتيري.",
    ],
    "when_changes": [
        "لو الأعراض خفيفة ومستمرة أقل من 10 أيام بدون حمى شديدة، الجواب يصير <bdi>reassurance</bdi> ودعم فقط (فايروسي).",
        "لو فيه علامات بالعين أو تغيّر بالوعي، الجواب يصير تصوير <bdi>CT</bdi> عاجل لاستبعاد مضاعفات.",
    ],
    "rule": "التوقيت ونمط الأعراض (مستمر، متدهور بعد تحسّن، أو شديد من البداية) هو اللي يحدد <bdi>bacterial sinusitis</bdi>، مو مجرد الألم الموضعي لوحده.",
    "comparison": None,
    "labs": None,
    "guideline_note": "المصدر ما حدد جواب مؤكد لهذا السؤال؛ الاجتهاد هنا حسب نمط <bdi>severe onset</bdi> للـ<bdi>bacterial sinusitis</bdi> عند الأطفال.",
},
"AS-2331": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "طفل 7 سنوات عنده إفرازات أنف مزمنة صافية مع حكة وعلامات حساسية بالوجه، والسؤال عن التشخيص الأرجح.",
    "clues": [
        ("chronic clear thin nasal discharge", "إفرازات صافية مزمنة، نموذجي لـ<bdi>allergic rhinitis</bdi>"),
        ("nasal itching", "حكة بالأنف، علامة تحسسية كلاسيكية"),
        ("periorbital dark swollen", "<bdi>allergic shiners</bdi>، علامة تحسسية حول العين"),
        ("pale turbinates mucosa", "غشاء شاحب منتفخ، يناسب <bdi>allergic rhinitis</bdi>"),
    ],
    "why_correct": [
        "طفل عنده إفرازات صافية مزمنة مع حكة، و<bdi>periorbital dark swollen</bdi> (<bdi>allergic shiners</bdi>) و<bdi>pale turbinates mucosa</bdi>، كل هذا الصورة الكلاسيكية لـ<bdi>allergic rhinitis</bdi>.",
        "الحكة والإفرازات المائية والأعراض الثنائية مع غشاء شاحب منتفخ هي البصمة التحسسية.",
    ],
    "when_changes": [
        "لو الإفرازات من جهة واحدة وكريهة الرائحة وقيحية بطفل صغير، الجواب يصير <bdi>foreign body</bdi>.",
        "لو فيه تاريخ استخدام بخاخ مزيل احتقان لفترة طويلة مع احتقان شديد، الجواب يصير <bdi>rhinitis medicamentosa</bdi>.",
    ],
    "rule": "حكة + إفرازات صافية مزمنة + غشاء شاحب منتفخ ثنائي = <bdi>allergic rhinitis</bdi>؛ إفرازات من جهة واحدة كريهة = <bdi>foreign body</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2335": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "طفل عنده نزيف بعد 5 أيام من <bdi>tonsillectomy</bdi>، والسؤال عن السبب الأكثر احتمالاً حسب توقيت النزيف.",
    "clues": [
        ("5 days post tonsillectomy", "نزيف بعد 24 ساعة، يعني <bdi>secondary haemorrhage</bdi>"),
    ],
    "why_correct": [
        "نزيف بعد 5 أيام من <bdi>tonsillectomy</bdi> يعتبر <bdi>secondary haemorrhage</bdi> (بعد 24 ساعة، نموذجيًا يوم 5-10)، وسببه الكلاسيكي <bdi>infection</bdi> بمكان الجراحة وانفصال القشرة الملتئمة.",
        "النزيف المبكر (<bdi>primary haemorrhage</bdi> خلال 24 ساعة) هو اللي يُنسب لخطأ بالتقنية الجراحية، مو هذا النوع.",
    ],
    "when_changes": [
        "لو النزيف صار خلال أول 24 ساعة بعد العملية، الجواب يصير مشكلة بالتقنية الجراحية (وعاء غير مثبّت جيدًا).",
        "لو النزيف صار وقت العملية مباشرة أو من مواضع متعددة، الجواب يصير <bdi>coagulopathy</bdi>.",
    ],
    "rule": "توقيت نزيف ما بعد <bdi>tonsillectomy</bdi> هو اللي يحدد السبب: أول 24 ساعة = تقنية جراحية، يوم 5-10 = <bdi>infection</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2377": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "طفل عنده <bdi>allergic rhinitis</bdi> وما تحسّن بالكامل مع <bdi>antihistamine</bdi>، والسؤال عن الخطوة التالية بسلم العلاج.",
    "clues": [
        ("allergic rhinitis", "التشخيص معروف مسبقًا"),
        ("after take antihistamine", "فشل أو عدم كفاية العلاج الأول، نحتاج خطوة أقوى"),
    ],
    "why_correct": [
        "استمرار العطس والاحتقان بعد <bdi>antihistamine</bdi> يعني نحتاج نرفع الخطوة لـ<bdi>intranasal corticosteroid</bdi>، وهو أقوى دواء منفرد لـ<bdi>allergic rhinitis</bdi> وأفضل شيء للاحتقان بالذات.",
        "يُعتبر الخط الأول للأعراض المستمرة أو المتوسطة إلى الشديدة عند الأطفال.",
    ],
    "when_changes": [
        "لو فيه <bdi>asthma</bdi> مصاحب، نضيف <bdi>montelukast</bdi> كعلاج مساعد.",
        "لو الأعراض مستمرة مع علاج مثالي شامل <bdi>intranasal steroid</bdi> وفيه مسبب تحسسي محدد، الجواب يصير <bdi>allergy immunotherapy</bdi>.",
    ],
    "rule": "فشل <bdi>antihistamine</bdi> بـ<bdi>allergic rhinitis</bdi> = ارفع لـ<bdi>intranasal corticosteroid</bdi>؛ <bdi>immunotherapy</bdi> يجي فقط بعد فشل العلاج الدوائي الأمثل.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2378": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "طفل عنده <bdi>URTI</bdi> تم علاجه، وبعد أسبوعين رجعت أعراض أنفية مع ألم بالخدود، والسؤال عن التشخيص الأرجح.",
    "clues": [
        ("URTI, treated. 2 weeks later", "تأخر الأعراض لأسبوعين كامل بعد <bdi>URTI</bdi>"),
        ("tenderness on the frontal cheeks", "ألم موضعي بالجيوب الفكية والجبهية"),
    ],
    "why_correct": [
        "استمرار أعراض أنفية بعد <bdi>URTI</bdi> لمدة أسبوعين مع احتقان وألم بالخدود يناسب <bdi>acute bacterial sinusitis</bdi>: أعراض تجاوزت 10 أيام بدون شفاء مع ألم بالجيوب.",
        "القصة والتوقيت (بعد <bdi>URTI</bdi> ومدة أطول من 10 أيام) ترجّح مضاعفة بكتيرية أكثر من عملية تحسسية جديدة.",
    ],
    "when_changes": [
        "لو الحكة والإفرازات الصافية مع تاريخ تحسسي هي الأبرز بدون ألم جيوب، الجواب يصير <bdi>allergic rhinitis</bdi>.",
        "لو الإفرازات من جهة واحدة كريهة الرائحة بطفل صغير، الجواب يصير <bdi>foreign body obstruction</bdi>.",
    ],
    "rule": "أعراض أنفية بعد <bdi>URTI</bdi> تستمر فوق 10 أيام مع ألم بالجيوب = <bdi>bacterial sinusitis</bdi>، مو <bdi>allergic rhinitis</bdi> حتى لو فيه حكة بالوصف.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2378B": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نفس فكرة <bdi>double worsening</bdi> بعد <bdi>URTI</bdi> فايروسي، تحسّن ثم تدهور بإفرازات <bdi>purulent</bdi> وألم بالجبهة.",
    "clues": [
        ("3 days after resolving of the symptoms", "تحسّن ثم تدهور مرة ثانية، نمط <bdi>double worsening</bdi>"),
        ("purulent nasal discharge and frontal tenderness", "إفرازات قيحية وألم جبهي، علامات بكتيرية"),
    ],
    "why_correct": [
        "النمط <bdi>double worsening</bdi>: <bdi>URTI</bdi> فايروسي تحسّن، وبعد 3 أيام تدهور الطفل مرة ثانية بإفرازات <bdi>purulent</bdi> وألم بالجبهة.",
        "تدهور جديد بعد تحسّن مع ألم بالجيوب هو معيار كلاسيكي لـ<bdi>acute bacterial sinusitis</bdi> الثانوي بعد العدوى الفايروسية.",
    ],
    "when_changes": [
        "لو الأعراض استمرت أكثر من 10 أيام من البداية بدون تحسّن، الجواب برضو <bdi>bacterial sinusitis</bdi> بنمط <bdi>persistent</bdi>.",
        "لو الإفرازات صافية مع حكة وعطس بدون حمى، الجواب يصير <bdi>allergic rhinosinusitis</bdi>.",
    ],
    "rule": "<bdi>double worsening</bdi> بعد <bdi>URTI</bdi> هو معيار قوي لـ<bdi>acute bacterial sinusitis</bdi>، مو مجرد استمرار إفرازات <bdi>purulent</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-2379": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "رجل سكري عنده صداع يزيد مع الكحة والجهد مع ألم بالحواجب، والسؤال عن التشخيص الأرجح بدون علامات عصبية خطيرة.",
    "clues": [
        ("dull aching headache increases with straining and coughing", "صداع يزيد مع رفع ضغط الجيوب، يناسب <bdi>sinusitis</bdi>"),
        ("tenderness all over the eyebrows", "ألم موضعي بمكان <bdi>frontal sinus</bdi>"),
    ],
    "why_correct": [
        "صداع يزيد مع الكحة والجهد (رفع ضغط الجيوب) مع ألم موضعي فوق الحواجب (<bdi>frontal sinus</bdi>) هو نموذجي لـ<bdi>sinusitis</bdi> الجبهي.",
        "ما فيه حمى واضحة ضمن النمط الالتهابي للسحايا، ولا تيبّس رقبة، ولا تشوّش وعي أو علامة بؤرية تدعم إصابة بالجهاز العصبي المركزي.",
    ],
    "when_changes": [
        "لو ظهرت علامات تسمم جهازي، تيبس رقبة، وتشوّش وعي، الجواب يصير <bdi>meningitis</bdi>.",
        "لو ظهرت علامات بؤرية عصبية أو تشنجات مع حمى، الجواب يصير <bdi>brain abscess</bdi>.",
        "لو هذا مريض سكري وظهر تنخر بالوجه أو إسوداد بالأنف، الجواب يصير <bdi>mucormycosis</bdi> وهو طارئ.",
    ],
    "rule": "صداع يزيد بالجهد والكحة مع ألم موضعي بمكان الجيوب = <bdi>sinusitis</bdi>؛ وبمريض سكري مع نخر أو إسوداد بالوجه نفكر فورًا بـ<bdi>mucormycosis</bdi>.",
    "comparison": None,
    "labs": None,
    "guideline_note": None,
},
"AS-0017": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "طفل 7 سنوات عنده <bdi>pneumonia</bdi> خفيفة مستقر، والسؤال يبي نقرر بين العلاج بالمنزل والدخول للمستشفى.",
    "clues": [
        ("localized left lower consolidation", "التماسك محدود بمكان واحد، يرجّح <bdi>pneumococcus</bdi>"),
        ("O2 is 94", "تشبع أكسجين غير منخفض بشدة، يدعم استقرار الحالة"),
        ("He can drink fluids", "قدرة على الشرب هي معيار الاستقرار للتدبير بالمنزل"),
    ],
    "why_correct": [
        "هذا <bdi>mild community-acquired pneumonia</bdi> بطفل مستقر: تماسك محدود، تشبع 94% (غير منخفض)، وأهم جملة «يقدر يشرب سوائل».",
        "الطفل المستقر اللي يقدر يأكل ويشرب يُدار كـ<bdi>outpatient</bdi>، و<bdi>oral amoxicillin</bdi> هو الخط الأول لأن <bdi>Streptococcus pneumoniae</bdi> هو الهدف الأساسي.",
        "تعليمات واضحة للرجوع (<bdi>safety-netting</bdi>) تكمل الخطة.",
    ],
    "when_changes": [
        "لو ذكر السؤال قيء مستمر أو رفض الطفل الأكل والشرب، الجواب يتحول للدخول بالمستشفى وعلاج وريدي.",
        "لو كان التماسك منتشر بالجهتين مع بداية تدريجية، الجواب يميل لـ<bdi>macrolide</bdi> لتغطية الأعراض اللانمطية.",
    ],
    "rule": "في أي سؤال <bdi>pediatric pneumonia</bdi>: القدرة على الشرب والتشبع الطبيعي يحددان العلاج بالمنزل بـ<bdi>oral amoxicillin</bdi>، مو شدة التشخيص بنفسه.",
    "comparison": None,
    "labs": [["Oxygen saturation", "94%", "95-100%"]],
    "guideline_note": None,
},
"AS-0018": {
    "correct_letter": "B",
    "self_judged": False,
    "idea": "نفس سيناريو <bdi>mild community-acquired pneumonia</bdi> لكن بطفل 4 سنوات، ونفس منطق التدبير بالمنزل.",
    "clues": [
        ("localized left lower consolidation", "تماسك محدود، يرجّح <bdi>pneumococcus</bdi>"),
        ("O2 is 94", "تشبع غير منخفض بشدة"),
        ("He can drink fluids", "معيار الاستقرار للتدبير بالمنزل"),
    ],
    "why_correct": [
        "<bdi>mild community-acquired pneumonia</bdi> بطفل مستقر: تماسك محدود، تشبع 94%، وقدرة على شرب السوائل.",
        "الطفل المستقر اللي يشرب يُدار بالمنزل بـ<bdi>oral amoxicillin</bdi> كخط أول ضد <bdi>Streptococcus pneumoniae</bdi>، مع تعليمات رجوع واضحة.",
    ],
    "when_changes": [
        "لو فيه قيء مستمر أو رفض الطفل الشرب، الجواب يتحول للدخول بالمستشفى وعلاج وريدي.",
        "لو الصورة تدعم عدوى لانمطية (بداية تدريجية، أعراض خارج الرئة)، الجواب يميل لـ<bdi>macrolide</bdi>.",
    ],
    "rule": "القدرة على الشرب والتشبع الطبيعي يحددان العلاج بالمنزل بـ<bdi>oral amoxicillin</bdi> بأي عمر، مو شدة التشخيص نفسه.",
    "comparison": None,
    "labs": [["Oxygen saturation", "94%", "95-100%"]],
    "guideline_note": None,
},
"AS-0018B": {
    "correct_letter": "D",
    "self_judged": False,
    "idea": "طفل 3 سنوات عنده <bdi>bacterial pneumonia</bdi> محددة بالفحص والمخبر، لكنه مستقر تمامًا بالعلامات الحيوية، فالعلاج بالمنزل.",
    "clues": [
        ("crackles over right lung middle zone", "صوت رئوي بؤري، يدعم <bdi>pneumonia</bdi> موضعية"),
        ("Oxygen saturation 97 %", "تشبع طبيعي، يدعم استقرار الحالة"),
        ("WBC 22", "ارتفاع واضح بكريات الدم البيضاء مع غلبة <bdi>neutrophils</bdi>، يدعم عدوى بكتيرية"),
    ],
    "why_correct": [
        "5 أيام حمى وكحة مع نقص دخول هواء وصوت <bdi>crackles</bdi> بؤري بالجهة اليمنى، مع <bdi>WBC 22</bdi> و84% <bdi>neutrophils</bdi>، يدعم <bdi>bacterial pneumonia</bdi> تحتاج مضاد حيوي.",
        "الطفل مستقر: تشبع 97%، ضغط طبيعي، بدون ضيق تنفس واضح، فهذا <bdi>mild pneumonia</bdi> تُدار بالمنزل بـ<bdi>oral amoxicillin</bdi> لمدة 7 أيام.",
    ],
    "when_changes": [
        "لو كان التشبع منخفض أو فيه ضيق تنفس شديد أو عدم قدرة على الشرب، الجواب يتحول لدخول المستشفى وعلاج وريدي.",
        "لو الصوت منتشر صفير (<bdi>wheeze</bdi>) بدون تماسك بؤري، الجواب يصير <bdi>bronchodilator</bdi> وستيرويد لمرض انسدادي مو <bdi>pneumonia</bdi>.",
    ],
    "rule": "التشخيص بـ<bdi>bacterial pneumonia</bdi> ما يحدد وحده مكان العلاج؛ شدة الحالة (تشبع، ضيق تنفس، قدرة على الشرب) هي اللي تحدد بين المنزل والمستشفى.",
    "comparison": None,
    "labs": [
        ["Oxygen saturation", "97%", "95-100%"],
        ["WBC", "22 x10^9/L", "4.5-13.5 x10^9/L (2-10y)"],
        ["Neutrophils", "84%", "40-60%"],
        ["Heart rate", "110/min", "70-110/min (3y)"],
        ["Blood pressure", "90/64 mmHg", "normal for age"],
        ["Temperature", "36.6 °C", "36.5-37.5 °C"],
    ],
    "guideline_note": None,
},
"AS-0024": {
    "correct_letter": "A",
    "self_judged": False,
    "idea": "رضيع خديج 29 أسبوع، حاليًا خرج من <bdi>oxygen</bdi> وفحصه طبيعي، والسؤال عن وقاية <bdi>RSV</bdi>.",
    "clues": [
        ("29 weeks", "عمر حملي عند حد <bdi>palivizumab</bdi> الكلاسيكي (دون 29 أسبوع)"),
        ("put off oxygen", "ما عنده مرض رئوي مزمن حاليًا يحتاج علاج أكسجين"),
        ("healthy with a completely normal examination", "طفل حاليًا سليم بالفحص"),
    ],
    "why_correct": [
        "القاعدة الكلاسيكية: الولادة قبل 29 أسبوع بالسنة الأولى تستحق <bdi>palivizumab</bdi>؛ الولادة عند 29 أسبوع أو أكثر، سليم وبدون أكسجين، يكفيها تطمين ونصائح نظافة.",
        "هذا الرضيع بالضبط عند الحد (29 أسبوع) وحاليًا سليم خارج الأكسجين، فالخيار المناسب هو <bdi>reassure</bdi> مع نصائح وقائية عامة.",
    ],
    "when_changes": [
        "لو كان عمر الحمل أقل من 29 أسبوع (مثلاً 28 أسبوع)، الجواب يتحول لـ<bdi>palivizumab</bdi>.",
        "لو عنده مرض رئوي مزمن للخداج أو قلب خلقي مهم، الجواب يصير <bdi>palivizumab</bdi> بغض النظر عن عمر الحمل بالضبط.",
    ],
    "rule": "عمر الحمل هو المحور: دون 29 أسبوع يميل لـ<bdi>palivizumab</bdi>، وعند أو بعد 29 أسبوع وسليم يميل لـ<bdi>reassurance</bdi> ونصائح نظافة.",
    "comparison": None,
    "labs": None,
    "guideline_note": "المصدر وضع إجابة A لكن أشار لتردد بين A و D بالملاحظة؛ أبقينا A لأنها إجابة المصدر المؤكدة.",
},
}

WHY_WRONG = {
"AS-1226": {
    "B": "الوقوف والانحناء للأمام يصعّب ثبات المريض ومراقبته، والطريقة المعيارية هي الجلوس لا الوقوف.",
    "C": "الانحناء للخلف هو الغلط الكلاسيكي: يخلي الدم يروح للحلق والمعدة (قيء) أو مجرى الهواء.",
    "D": "الوقوف مع إنحناء غير محدد الاتجاه، وأيضًا الوقوف أقل ثباتًا من الجلوس بهذا الوضع الطارئ.",
},
"AS-1270": {
    "A": "الفايروسي يفسر أول 4 أيام فقط، وما يرجع بعد التحسّن بإفرازات قيحية وألم جيوب.",
    "C": "الحساسية تعطي إفرازات مائية صافية وحكة وعطس بدون حمى أو إفرازات قيحية.",
    "D": "النوبة الثانية مرتبطة مباشرة بالـURTI لأن التورم الفايروسي سد تصريف الجيوب وسمح بعدوى بكتيرية.",
},
"AS-1286": {
    "A": "الجراحة الفورية تحتاج استيفاء معايير Paradise أو وجود انسداد أو خُراج متكرر؛ 4 نوبات لا تكفي.",
    "B": "المضاد الحيوي الوقائي غير موصى به بالالتهاب المتكرر؛ فائدته محدودة ويزيد المقاومة والأعراض الجانبية.",
    "D": "تجنب اللعب بالخارج ما يمنع العدوى؛ الانتقال يحصل بالتجمعات المغلقة، وتقييد النشاط يضر الطفل بدون فائدة.",
},
"AS-1337": {
    "A": "ورم angiofibroma يصيب شباب بعمر البلوغ الذكور مع انسداد أحادي الجانب، مو رجل 40 سنة.",
    "B": "HHT يسبب نزيف متكرر من الطفولة مع توسع شعيرات بالشفايف واللسان وتاريخ عائلي، غير موجود هنا.",
    "D": "اعتلال التخثر يحتاج تاريخ مضاد تخثر أو مرض كبد أو نزيف بمواضع أخرى؛ العامل الوحيد هنا هو الضغط.",
},
"AS-1414": {
    "A": "صورة الجيوب العادية غير موصى بها حاليًا؛ حساسيتها ودقتها ضعيفة، والتصوير المفضل بالحالات المعقدة هو CT.",
    "B": "كورس مضاد حيوي إضافي صحيح بأول فشل، لكن بعد فشل متعدد لازم نحدد السبب والجرثومة أولاً.",
},
"AS-2075": {
    "A": "صورة الوجه تُحجز لاشتباه ورم أو كسر أو نزيف خلفي متكرر غير مفسّر؛ التصوير هنا طبيعي وما يوقف النزيف.",
    "B": "ضبط الضغط يصير بالتوازي، لكن التحويل للقلب يترك النزيف النشط بدون علاج مباشر.",
},
"AS-1835": {
    "A": "التطمين يناسب فقط جسم غريب منخفض الخطر وصل المعدة بطفل سليم؛ جسم بمجرى الهواء مع ضيق تنفس حالة طارئة.",
    "B": "المراقبة تناسب عملة بالمعدة أو المريء السفلي بطفل بلا أعراض؛ الجسم الغريب بالمجرى التنفسي لا يمر لوحده وقد يسد المجرى فجأة.",
    "C": "الصور المتكررة تتابع مرور عملة بالجهاز الهضمي؛ عملة بمجرى الهواء لن تتحرك للأسفل، والانتظار يؤخر السحب.",
},
"AS-2090": {
    "A": "الفايروسات قد تسبق المرض وتهيّج قناة أوستاكي، لكن الإفرازات القيحية مع الحمى الشديدة ترجّح البكتيري.",
    "B": "الفطريات تسبب عدوى بالأذن الخارجية مع حكة وبقايا قطنية، غالبًا بدون حمى شديدة.",
    "D": "الطفيليات ليست سببًا معروفًا لالتهاب الأذن الوسطى؛ وجود حشرة بالقناة مشكلة جسم غريب مو عدوى بحمى.",
},
"AS-2268": {
    "A": "الجراحة تحتاج استيفاء معايير Paradise أو مضاعفات؛ 4 نوبات لا تكفي.",
    "B": "تجنب البرد خرافة شائعة؛ الالتهاب ينتقل بالرذاذ والتلامس لا بالتعرض للبرد.",
    "D": "المضاد الحيوي الوقائي غير موصى به بالالتهاب المتكرر؛ الوقاية طويلة المدى بالبنسلين تكون لحمى روماتيزمية لا التهاب لوز متكرر.",
},
"AS-2305": {
    "A": "صورة الوجه قليلة الفائدة لتشخيص sinusitis عند الأطفال وغير موصى بها كخطوة روتينية.",
    "B": "الصورة فيها حمى وصداع شديد مع ألم موضعي منذ بداية الأعراض تقريبًا، وهذا نمط شدة يحتاج علاج لا تطمين فقط.",
},
"AS-2331": {
    "B": "الجسم الغريب يعطي إفرازات من جهة واحدة كريهة الرائحة بطفل صغير، لا إفرازات ثنائية صافية مع حكة.",
    "C": "السل الأنفي نادر ويعطي تقرّح وتكتل مع أعراض جهازية، لا حكة وإفرازات مائية مزمنة.",
    "D": "التهاب الأنف الدوائي يحتاج تاريخ استخدام بخاخ مزيل احتقان طويل مع احتقان أحمر، غير مذكور هنا.",
},
"AS-2335": {
    "A": "الجسم الغريب ليس سببًا معروفًا لنزيف بعد الاستئصال؛ يسبب صدمة موضعية أو انسداد لا نزيف بهذا التوقيت.",
    "C": "الاستئصال الناقص يعطي نمو متبقي أو أعراض متكررة، لا نزيف محدد بتوقيت يوم 5.",
    "D": "اعتلال التخثر يظهر غالبًا أثناء أو بعد الجراحة مباشرة (نزيف أولي)، ويُفحص عنه قبل العملية.",
},
"AS-2377": {
    "B": "مونتيلوكاست أقل فعالية من الستيرويد الأنفي لالتهاب الأنف التحسسي؛ يُستخدم أساسًا مع ربو مصاحب أو كعلاج إضافي.",
    "C": "مزيل الاحتقان الفموي يعطي راحة قصيرة فقط مع آثار جانبية جهازية، وغير موصى به للأطفال الصغار، ولا يعالج الالتهاب التحسسي.",
    "D": "العلاج المناعي يُستخدم فقط بعد فشل العلاج الدوائي الأمثل شامل الستيرويد الأنفي، لا كخطوة مباشرة بعد مضاد الهيستامين.",
},
"AS-2378": {
    "B": "التهاب الأنف التحسسي يعطي حكة وعطس وإفرازات صافية مزمنة أو موسمية بدون ألم جيوب، والحكة هنا تفصيل مُضلّل.",
    "C": "الجسم الغريب يعطي إفرازات من جهة واحدة كريهة الرائحة بطفل صغير، غير مرتبط بـURTI سابق.",
    "D": "اللحميات الأنفية كتل رمادية لامعة مع انسداد مزمن وضعف شم؛ نادرة بالأطفال إلا مع التليف الكيسي، وما تسبب ألم خدود بعد نزلة برد.",
},
"AS-2378B": {
    "A": "الفايروسي يفسر أول 4 أيام فقط، وما يرجع بعد التحسّن بإفرازات قيحية وألم جيوب.",
    "C": "الحساسية تعطي إفرازات مائية صافية وحكة وعطس بدون حمى أو إفرازات قيحية.",
    "D": "النوبة الثانية مرتبطة مباشرة بالـURTI لأن التورم الفايروسي سد تصريف الجيوب وسمح بعدوى بكتيرية.",
},
"AS-2379": {
    "A": "التهاب السحايا الفايروسي يعطي حمى حادة وصداع مع تيبس رقبة وحساسية للضوء، لا ألم موضعي بالحواجب.",
    "B": "سل السحايا مرض تحت حاد لأسابيع مع حمى خفيفة وشلل أعصاب قحفية وتشوّش وعي، لا يناسب هذه الصورة.",
    "C": "خُراج الدماغ قد يزيد مع الكحة أيضًا، لكنه يترافق مع حمى وعلامات عصبية بؤرية أو تشنجات، وليس ألمًا سطحيًا موضعيًا بالحواجب.",
},
"AS-0017": {
    "A": "الدخول للمستشفى وعلاج وريدي يُحجز لحالة شديدة: نقص أكسجين، ضيق تنفس، عدم قدرة على الشرب، أو مضاعفات؛ هنا الطفل مستقر ويشرب.",
    "C": "الماكروليد يغطي الكائنات اللانمطية التي تظهر غالبًا بأعراض تدريجية منتشرة، بينما التماسك البؤري هنا يرجّح المكورة الرئوية.",
},
"AS-0018": {
    "A": "الدخول للمستشفى يُحجز لحالة شديدة بنقص أكسجين أو ضيق تنفس أو عدم قدرة على الشرب؛ هذا الطفل مستقر ويشرب.",
    "C": "الماكروليد يناسب عدوى لانمطية ببداية تدريجية منتشرة؛ التماسك البؤري هنا يرجّح المكورة الرئوية والأموكسيسيلين.",
},
"AS-0018B": {
    "A": "التطمين يتجاهل دليل واضح على عدوى بكتيرية (علامات بؤرية وارتفاع نيوتروفيلي)، وهذا يحتاج مضاد حيوي.",
    "B": "موسّعات الشعب والستيرويد يعالجان الصفير الناتج عن ربو أو مرض انسدادي، لا تماسك بكتيري بؤري.",
    "C": "الدخول والعلاج الوريدي يُحجز لحالة شديدة أو معقدة؛ هذا الطفل مستقر بتشبع 97% بدون ضيق تنفس.",
},
"AS-0024": {
    "B": "بالیفيزوماب يُعطى للخداج دون 29 أسبوع أو مع مرض رئوي مزمن أو قلب خلقي مهم؛ هذا الرضيع عند 29 أسبوع وسليم.",
    "C": "المضاد الحيوي لا دور وقائي له ضد RSV؛ الوقاية تكون بالأجسام المناعية الجاهزة أو النظافة.",
    "D": "الكحة طريقة انتقال صحيحة معلوماتيًا، لكنها ليست إجابة على سؤال «ماذا تفعل للوقاية» بالنسبة لهذا الرضيع.",
},
}

HIGHLIGHT_TERMS = {
"AS-1226": ["epistaxis"],
"AS-1270": ["3 days after resolving", "purulent nasal discharge and frontal tenderness"],
"AS-1286": ["4 recurrent adenotonsillitis within one academic year"],
"AS-1337": ["profuse nosebleeding over 30 minutes", "known case of hypertension"],
"AS-1414": ["foul-smelling breath", "worsened after 14 days, despite multiple courses of antibiotics"],
"AS-1835": ["coin in the trachea"],
"AS-2075": ["severe hypertension", "anterior epistaxis", "aspirin", "Imaging normal"],
"AS-2090": ["ear discharge", "high-grade fever"],
"AS-2268": ["4 episodes of tonsillitis", "now doing well"],
"AS-2305": ["10 year old", "frontal headache, fever, and stuffed nose", "left cheek tenderness"],
"AS-2331": ["chronic clear thin nasal discharge", "nasal itching", "periorbital dark swollen", "pale turbinates mucosa"],
"AS-2335": ["5 days post tonsillectomy"],
"AS-2377": ["allergic rhinitis", "after take antihistamine"],
"AS-2378": ["URTI, treated. 2 weeks later", "tenderness on the frontal cheeks"],
"AS-2378B": ["3 days after resolving of the symptoms", "purulent nasal discharge and frontal tenderness"],
"AS-2379": ["dull aching headache increases with straining and coughing", "tenderness all over the eyebrows"],
"AS-0017": ["7 y old", "localized left lower consolidation", "O2 is 94", "He can drink fluids"],
"AS-0018": ["4 y old", "localized left lower consolidation", "O2 is 94", "He can drink fluids"],
"AS-0018B": ["3-year-old", "crackles over right lung middle zone", "Oxygen saturation 97 %", "WBC 22"],
"AS-0024": ["29 weeks", "put off oxygen", "healthy with a completely normal examination"],
}

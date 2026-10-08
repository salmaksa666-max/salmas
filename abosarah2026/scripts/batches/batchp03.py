# -*- coding: utf-8 -*-
# Proper bilingual rewrite — batch p03 (45 questions, Medicine section).

EXPLANATIONS = {
"AS-0776": {"correct_letter": "A", "self_judged": False,
    "idea": "مريض <bdi>sickle cell disease</bdi> بعد <bdi>bone marrow transplant</bdi>، حمى مستمرة فوق مضاد حيوي واسع، بدون <bdi>pneumonia</bdi> أو <bdi>hypotension</bdi> — السؤال عن إضافة الدواء المناسب.",
    "clues": [("bone marrow transplant", "فترة نقص مناعة ونقص صفائح بيضاء عميق بعد الزرع"),
               ("ceftazidime", "مضاد حيوي واسع ضد الزائفة مُعطى من البداية"),
               ("did not improve after 72 hours", "الحمى مستمرة رغم التغطية الجرثومية الكافية"),
               ("no pneumonia or hypotension", "أهم جزء — ينفي كل دواعي إضافة الفانكومايسين")],
    "why_correct": [
        "حمى مستمرة فوق مضاد حيوي واسع بمريض نقص مناعة شديد (بعد زرع نخاع) تدفعنا نفكر بعدوى فطرية غازية، خصوصًا مع غياب كل دواعي الفانكومايسين (التهاب رئة، هبوط ضغط، عدوى قسطرة أو جلد).",
        "فالإضافة المناسبة هي مضاد فطري يغطي العفن مثل <bdi>voriconazole</bdi>، اللي يُعتبر الخط الأول لعلاج <bdi>aspergillosis</bdi> الغازي."],
    "when_changes": ["لو ظهر بالسؤال <bdi>pneumonia</bdi> أو <bdi>hypotension</bdi> أو عدوى قسطرة، الجواب يتغير لإضافة <bdi>vancomycin</bdi> بدل المضاد الفطري."],
    "rule": "حمى نقص مناعة مستمرة بدون دواعي فانكومايسين = فكّري بمضاد فطري (<bdi>voriconazole</bdi>)؛ وجود <bdi>pneumonia</bdi> صراحة = فانكومايسين.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0776B": {"correct_letter": "D", "self_judged": False,
    "idea": "مريضة لوكيميا حادة بعد زرع نخاع، نقص صفائح بيضاء وحمى وسعال، وتشخيص <bdi>invasive aspergillosis</bdi> مؤكد شعاعيًا ومخبريًا — السؤال عن العلاج.",
    "clues": [("acute leukemia", "مرض أساسي يحتاج زرع نخاع"),
               ("allogenic bone marrow transplantation", "تدخل يسبب نقص مناعة شديد"),
               ("invasive aspergillosis", "التشخيص مؤكد فعليًا، مو مشتبه")],
    "why_correct": [
        "التشخيص مؤكد: <bdi>invasive aspergillosis</bdi> عند مريضة بنقص مناعة شديد بعد زرع نخاع.",
        "<bdi>Aspergillus</bdi> فطر، والعلاج القياسي الخط الأول له هو <bdi>voriconazole</bdi>، وهو الدواء الفطري الوحيد بالخيارات."],
    "when_changes": ["لو كان التشخيص <bdi>mucormycosis</bdi> بدل الأسبرجيلوس، الجواب يتحول لـ<bdi>amphotericin B</bdi> لأن الفوريكونازول ما يغطيه."],
    "rule": "<bdi>invasive aspergillosis</bdi> مؤكد = <bdi>voriconazole</bdi> خط أول؛ <bdi>mucormycosis</bdi> = <bdi>amphotericin B</bdi>.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0777": {"correct_letter": "A", "self_judged": False,
    "idea": "مريض زرع نخاع بسبب سكل سيل، حمى نقص بيضاء بدون <bdi>pneumonia</bdi>، على <bdi>ceftazidime</bdi> وما تحسّن — السؤال عن الإضافة المناسبة.",
    "clues": [("bone marrow transplantation", "نقص مناعة بعد الزرع"),
               ("febrile neutropenia", "حمى مع نقص شديد بالخلايا البيضاء"),
               ("[NO] Pneumonia", "ينفي سبب رئوي واضح"),
               ("Ceftazidime", "التغطية الجرثومية الواسعة الحالية")],
    "why_correct": [
        "جواب هذا السؤال المسجل هو <bdi>vancomycin</bdi>: مريض زرع نخاع بنقص بيضاء على <bdi>ceftazidime</bdi> وما يتحسن.",
        "<bdi>ceftazidime</bdi> تغطيته ضعيفة للجراثيم موجبة الغرام (مثل <bdi>streptococci</bdi> من التهاب الفم أو <bdi>staphylococci</bdi> من القسطرة)، و<bdi>vancomycin</bdi> هو الخيار الوحيد اللي يضيف تغطية موجبة الغرام و<bdi>MRSA</bdi> هنا، وما فيه خيار مضاد فطري بالقائمة."],
    "when_changes": ["لو كان بالخيارات مضاد فطري وانتفت دواعي الفانكومايسين صراحة (زي عدم وجود عدوى قسطرة أو جلد)، الجواب يتحول لمضاد فطري."],
    "rule": "حمى نقص بيضاء ما تتحسن على <bdi>ceftazidime</bdi> بدون مضاد فطري بالخيارات = أضيفي <bdi>vancomycin</bdi> للتغطية موجبة الغرام.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0780": {"correct_letter": "B", "self_judged": True,
    "idea": "استسقاء بطني فشل مع <bdi>spironolactone</bdi> — السؤال عن الخطوة التالية بدون خيارات كثيرة متاحة.",
    "clues": [("Ascitis", "استسقاء بطني بسبب تليف الكبد غالبًا"),
               ("sparonolactone with no improvment", "فشل العلاج المدر الأولي")],
    "why_correct": [
        "استسقاء ما يتحسن على <bdi>spironolactone</bdi> لوحده يحتاج عادة إضافة <bdi>furosemide</bdi> أو زيادة الجرعة، لكن لو كان استسقاء كبير أو متوتر فالخطوة الفعلية هي <bdi>therapeutic paracentesis</bdi> لتفريغه وتخفيف الأعراض.",
        "بين الخيارين المتاحين، <bdi>TIPS</bdi> يُحجز لحالات الاستسقاء المتكرر اللي يحتاج بزل متكرر، مو كخطوة أولى بعد فشل مدر واحد."],
    "when_changes": ["لو كان الاستسقاء يحتاج بزل متكرر رغم العلاج الكامل (مدرات + بزل)، الجواب يتحول لـ<bdi>TIPS</bdi>."],
    "rule": "استسقاء كبير أو متوتر ما يتحسن بالمدر = <bdi>therapeutic paracentesis</bdi>؛ تكرار الحاجة للبزل = <bdi>TIPS</bdi>.",
    "comparison": None, "labs": None,
    "guideline_note": "ما فيه جواب مؤكد من المصدر لهذا السؤال تحديدًا، لكن المصدر يذكر سؤال مرجعي مطابق بنفس السيناريو واختار <bdi>Therapeutic paracentesis</bdi>، فاتبعنا نفس المنطق."},

"AS-0781": {"correct_letter": "B", "self_judged": False,
    "idea": "مريض تليف كبد، استسقاء متزايد رغم <bdi>spironolactone</bdi> و<bdi>furosemide</bdi>، بدون حمى ولا نقص وعي — استسقاء كبير مقاوم للمدرات، الخطوة الفعلية.",
    "clues": [("liver cirrhosis", "سبب الاستسقاء"),
               ("increasing ascites", "تدهور رغم العلاج المدر"),
               ("spironolactone 50 mg/day and furosemide 40 mg/day", "جرعة مدرات مزدوجة فعلية وما نجحت"),
               ("large ascites", "استسقاء كبير يحتاج تفريغ فعلي")],
    "why_correct": [
        "استسقاء كبير مستمر رغم مدرين (<bdi>spironolactone + furosemide</bdi>)، مع غياب الحمى (يبعد <bdi>SBP</bdi>) وغياب نقص الوعي (يبعد <bdi>encephalopathy</bdi>)، يُدار بـ<bdi>therapeutic large volume paracentesis</bdi> مع إعطاء <bdi>albumin</bdi> وريدي عند سحب كمية كبيرة."],
    "when_changes": ["لو كان فيه حمى أو ألم بطن، الجواب يتحول لبزل تشخيصي لاستبعاد <bdi>spontaneous bacterial peritonitis (SBP)</bdi> أولاً."],
    "rule": "استسقاء كبير ومقاوم لمدرين = <bdi>therapeutic paracentesis</bdi> + <bdi>albumin</bdi>؛ ما نزيد المدرات الوريدية ولا نقفز لـ<bdi>TIPS</bdi> مباشرة.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0782": {"correct_letter": "B", "self_judged": True,
    "idea": "سؤال مختصر جدًا عن سبب <bdi>watery diarrhea</bdi> بدون أي تفاصيل سريرية ثانية — نرجّح حسب نمط الإسهال الكلاسيكي بكل سبب.",
    "clues": [("Watary diarrhea", "إسهال مائي بدون دم ولا مخاط — يستبعد الأسباب الالتهابية الغازية")],
    "why_correct": [
        "<bdi>shigella</bdi> سببه الكلاسيكي إسهال دموي مع حمى، فهو أبعد خيار هنا لأن السؤال يذكر إسهال مائي صريح.",
        "بين <bdi>norovirus</bdi> (حاد، غالبًا مع قيء بارز وينتهي خلال أيام) و<bdi>Giardia</bdi> (إسهال مائي مزمن مع انتفاخ ونقص وزن)، الوصف العام «<bdi>watery diarrhea</bdi>» بدون سياق حاد (تفشي جماعي، قيء) يتماشى أكثر مع الصورة الكلاسيكية لـ<bdi>Giardia</bdi>."],
    "when_changes": ["لو ذُكر تفشي حاد جماعي مع قيء بارز، الجواب يتحول لـ<bdi>norovirus</bdi>؛ لو ظهر دم أو مخاط، يتحول لـ<bdi>shigella</bdi>."],
    "rule": "إسهال مائي مزمن = <bdi>Giardia</bdi>؛ إسهال مائي حاد مع قيء بتفشي جماعي = <bdi>norovirus</bdi>؛ إسهال دموي = <bdi>shigella</bdi>.",
    "comparison": None, "labs": None,
    "guideline_note": "السؤال مختصر جدًا وما فيه جواب مؤكد من المصدر؛ اخترنا الأقرب طبيًا بناءً على نمط الإسهال المائي الكلاسيكي."},

"AS-0785": {"correct_letter": "C", "self_judged": False,
    "idea": "امرأة ٤٠ سنة على علاج لقرحة اثني عشر مرتبطة بـ<bdi>H. pylori</bdi> متكررة، لاحظت برازها أسود بدون أن يكون قطراني — دواء يسبب تلون البراز، مو نزيف.",
    "clues": [("helicobacter-associated duodenal ulcer", "علاج يحتمل يحتوي أدوية متعددة لعلاج عدوى متكررة"),
               ("non-tarry black", "أسود بس مو لزج كريه الرائحة — يستبعد <bdi>melena</bdi> الحقيقي")],
    "why_correct": [
        "علاج القرحة المتكررة المرتبطة بـ<bdi>H. pylori</bdi> يعني غالبًا <bdi>bismuth quadruple therapy</bdi>.",
        "<bdi>Bismuth</bdi> يتفاعل مع كبريتيد الأمعاء ويكوّن <bdi>bismuth sulfide</bdi> الأسود، فيعطي برازًا أسود غير قطراني (وأحيانًا لسان أسود) مع علامات حيوية وهيموغلوبين طبيعيين، عكس <bdi>melena</bdi> الحقيقي."],
    "when_changes": ["لو كان البراز قطراني كريه الرائحة مع هبوط ضغط أو هيموغلوبين منخفض، الجواب يتحول لنزيف هضمي فعلي (<bdi>melena</bdi>)."],
    "rule": "براز أسود «غير قطراني» مع علامات حيوية وهيموغلوبين طبيعيين = أثر <bdi>bismuth</bdi> الدوائي، مو نزيف.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0788": {"correct_letter": "D", "self_judged": False,
    "idea": "مريض مشخّص بـ<bdi>celiac disease</bdi> — أي طعام لازم يتجنبه.",
    "clues": [("celiac disease", "مرض مناعي ضد الـ<bdi>gluten</bdi>")],
    "why_correct": [
        "<bdi>celiac disease</bdi> رد فعل مناعي ضد <bdi>gluten</bdi>، والعلاج حمية خالية من الغلوتين مدى الحياة.",
        "<bdi>wheat</bdi> (القمح) هو الحبوب الرئيسية المحتوية على الغلوتين، مع <bdi>barley</bdi> و<bdi>rye</bdi>."],
    "when_changes": ["لو كان الخيار <bdi>barley</bdi> بدل القمح، هو كمان صحيح لأنه يحتوي غلوتين — أي حبوب من الثلاثة (قمح، شعير، شيلم) يجب تجنبها."],
    "rule": "تجنبي BRW: <bdi>Barley, Rye, Wheat</bdi>؛ الأرز والذرة والبطاطس آمنة تمامًا بـ<bdi>celiac disease</bdi>.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0791": {"correct_letter": "B", "self_judged": False,
    "idea": "امرأة ٣٥ سنة حمى روماتيزمية، صمام صناعي من ٣ سنين، بدها عملية أسنان — الوقاية من التهاب الشغاف قبل الإجراء.",
    "clues": [("rheumatic heart disease", "خلفية صمامية"),
               ("prosthetic valve replacement", "عامل خطر عالي للشغاف — دواعي الوقاية مؤكدة"),
               ("dental operation", "إجراء عالي الخطورة يحتاج وقاية")],
    "why_correct": [
        "الصمام الصناعي حالة قلبية عالية الخطورة، والعملية السنية إجراء عالي الخطورة، فالوقاية من التهاب الشغاف (<bdi>infective endocarditis</bdi>) مطلوبة.",
        "البروتوكول القياسي جرعة فموية وحيدة من <bdi>amoxicillin</bdi> قبل الإجراء."],
    "when_changes": ["لو ما كانت تقدر تاخذ دواء فموي، البديل <bdi>ampicillin</bdi> أو <bdi>ceftriaxone</bdi> وريدي/عضلي."],
    "rule": "صمام صناعي + إجراء أسنان عالي الخطورة = جرعة وحيدة <bdi>amoxicillin</bdi> فموي قبل الإجراء، مو بعده.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0793": {"correct_letter": "C", "self_judged": False,
    "idea": "رجل ٥٣ سنة بعد قسطرة لاحتشاء قلبي قبل ٣ أشهر، ملتزم بالرياضة والحمية، كوليسترول ٥.٣ وضغط حدّي — الوقاية الثانوية تحتاج دواء مو بس نمط حياة.",
    "clues": [("post angioplasty after MI 3 monthes ago", "مرض قلبي تاجي مؤكد — وقاية ثانوية"),
               ("cholesterol was 5.3", "كوليسترول كلي أعلى من المعتاد رغم الحمية")],
    "why_correct": [
        "بعد احتشاء قلبي (<bdi>post angioplasty, MI</bdi>)، المريض عنده مرض شرايين تاجي مؤكد، فالستاتين عالي الجرعة مطلوب للوقاية الثانوية بغض النظر عن قيمة الكوليسترول الأساسية.",
        "كوليسترول ٥.٣ يعني <bdi>LDL</bdi> أعلى من أهداف الوقاية الثانوية، والحمية والرياضة وحدها ما تكفي للوصول للهدف، فالخطوة الصحيحة بدء دواء خافض للدهون فوق نمط الحياة الحالي."],
    "when_changes": ["لو كان المريض بدون مرض قلبي تاجي مؤكد (وقاية أولية)، القرار يعتمد على درجة الخطورة، والحمية قد تكفي لو الخطورة منخفضة."],
    "rule": "مرض قلبي تاجي مؤكد (احتشاء/قسطرة) = ستاتين عالي الجرعة مدى الحياة، مهما كان الكوليسترول.",
    "comparison": None, "labs": [["Cholesterol", "5.3 mmol/L", "&lt;4 mmol/L هدف بعد احتشاء"], ["BP", "139/75 mmHg", "&lt;130/80 mmHg هدف بعد احتشاء"]], "guideline_note": None},

"AS-0795": {"correct_letter": "C", "self_judged": False,
    "idea": "رجل ٥٠ سنة بيطري، ألم بمفصل العجز الحرقفي وحمى شهرين، تغيّر سلوكي وهيموغلوبين منخفض وصفائح منخفضة — عدوى من الحيوانات.",
    "clues": [("veterinarian", "تماس مباشر مع الحيوانات — مفتاح التشخيص"),
               ("right sacro-iliac pain and fever for 2 monthes", "حمى تحت حادة مع إصابة مفصل العجز الحرقفي")],
    "why_correct": [
        "<bdi>veterinarian</bdi> (تماس حيواني) مع حمى تمتد شهرين، ألم بالعجز الحرقفي والظهر، وتغيّر سلوكي، تطابق <bdi>brucellosis</bdi>: عدوى حيوانية المصدر تسبب حمى متموجة وإصابة عضلية هيكلية (التهاب مفصل عجزي حرقفي، التهاب فقار) وأحيانًا <bdi>neurobrucellosis</bdi>.",
        "فقر الدم ونقص الصفائح يعكسان إصابة نخاع العظم والجهاز الشبكي البطاني، وهذا شائع بـ<bdi>brucellosis</bdi>، والتماس المهني هو الدليل الحاسم."],
    "when_changes": ["لو كان المريض يشتكي سعال ونقص وزن مع تماس مريض سل، الجواب يتحول لـ<bdi>TB</bdi> بالعمود الفقري (غالبًا الصدري)."],
    "rule": "تماس حيواني (بيطري، حليب غير مبستر) + حمى طويلة + ألم عجزي حرقفي = <bdi>brucellosis</bdi> أولاً.",
    "comparison": None, "labs": [["Hb", "10 g/dL", "13.5-17.5 g/dL طبيعي للرجال"]], "guideline_note": None},

"AS-0796": {"correct_letter": "C", "self_judged": False,
    "idea": "مريض ضغط على <bdi>amlodipine</bdi> و<bdi>losartan</bdi> ما وصل للهدف، وظائف الكلى وصورة الدم طبيعية — الدواء الثالث المناسب بالسلم العلاجي.",
    "clues": [("failed to reach target blood pressure", "فشل بالعلاجين الحاليين"),
               ("on amlodipine and losartan", "A + C موجودين بالفعل")],
    "why_correct": [
        "هو أصلاً على <bdi>ARB</bdi> (<bdi>losartan</bdi>) مع حاصر قنوات كالسيوم (<bdi>amlodipine</bdi>) وما وصل للهدف، ووظائف الكلى طبيعية.",
        "الخطوة القياسية الثالثة هي A + C + D: إضافة مدر شبيه بالثيازيد (مثل <bdi>indapamide</bdi>)، ووظائف الكلى الطبيعية تضمن فعاليته."],
    "when_changes": ["لو كانت وظائف الكلى سيئة جدًا، المدر الثيازيدي يفقد فعاليته ونستخدم مدر عروة (<bdi>loop diuretic</bdi>) بدلاً منه."],
    "rule": "سلم الضغط: A أو C، ثم A+C، ثم A+C+D (مدر ثيازيدي)؛ لا تجمعي أبدًا بين <bdi>ACE inhibitor</bdi> و<bdi>ARB</bdi> معًا.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0848": {"correct_letter": "A", "self_judged": True,
    "idea": "امرأة جاءت بضعف، وتخطيط القلب يظهر <bdi>Afib</bdi> — السؤال عن سبب السكتة الدماغية.",
    "clues": [("weakness", "عرض السكتة الدماغية"), ("image show Afib", "الإيقاع المسبب الموثق بالصورة")],
    "why_correct": [
        "الضعف هنا هو عرض السكتة الدماغية، وصورة تخطيط القلب الموضحة تُظهر <bdi>atrial fibrillation</bdi> صراحة.",
        "<bdi>A.fib</bdi> يسبب ركود دم بالأذين الأيسر وتكوّن خثرة تنفصل وتسبب سكتة دماغية صمية (<bdi>cardioembolic stroke</bdi>)، فهو السبب المباشر المذكور بالصورة."],
    "when_changes": ["لو كانت الصورة تُظهر موجات نشارية منتظمة (<bdi>atrial flutter</bdi>) بدل عدم الانتظام التام، الجواب يتحول لـ<bdi>atrial flutter</bdi>."],
    "rule": "إيقاع غير منتظم تمامًا بدون موجات P = <bdi>A.fib</bdi>؛ موجات نشارية منتظمة = <bdi>atrial flutter</bdi>؛ كلاهما يسببان سكتة صمية.",
    "comparison": None, "labs": None,
    "guideline_note": "ما فيه جواب مؤكد من المصدر؛ اخترنا <bdi>A.fib</bdi> لأنه الإيقاع الموضح صراحة بالصورة وهو السبب الكلاسيكي المباشر للسكتة الصمية."},

"AS-0850": {"correct_letter": "B", "self_judged": False,
    "idea": "مريض مستقر ضيق تنفس وتعب، تخطيط القلب يظهر <bdi>bradycardia</bdi> — الخطوة التالية بالعلاج.",
    "clues": [("SOB and fatigue", "أعراض ناتجة عن بطء القلب"), ("stable", "مستقر هيموديناميكيًا لكن عرضي"), ("bradycardia", "التشخيص الموضح بتخطيط القلب")],
    "why_correct": [
        "تخطيط القلب يُظهر <bdi>bradycardia</bdi>، والمريض عنده أعراض (ضيق تنفس وتعب) ناتجة عن بطء النبض.",
        "من الخيارات، <bdi>atropine</bdi> هو العلاج الوحيد اللي يرفع نبض بطيء، وهو الدواء الأول بخوارزمية بطء القلب، تليه الناظمة أو <bdi>dopamine/epinephrine</bdi> لو فشل."],
    "when_changes": ["لو كان المريض غير مستقر (هبوط ضغط أو تغير وعي)، الخطوة بعد فشل الأتروبين تتحول للتنظيم الكهربائي المؤقت (<bdi>pacing</bdi>)."],
    "rule": "بطء قلب عرضي = <bdi>atropine</bdi> أولاً؛ لو فشل = ناظمة خطى أو <bdi>dopamine/epinephrine</bdi>.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0853": {"correct_letter": "C", "self_judged": False,
    "idea": "رجل سليم طبيًا، اكتُشف عنده <bdi>A-fib</bdi> صدفة بنبض ١١٠ وضغط ١١٠/٧٠ — السؤال عن ضبط النبض مو الإيقاع.",
    "clues": [("Incidentally Found To Have Atrial Fibrillation", "اكتشاف عرضي، مريض مستقر بدون أعراض خطيرة"),
               ("HR: 110 bpm", "نبض سريع يحتاج ضبط"),
               ("BP: 110/70 mmHg", "ضغط مستقر — لا داعي لتحويل كهربائي طارئ")],
    "why_correct": [
        "المريض عنده <bdi>A-fib</bdi> مستقر (ضغط ١١٠/٧٠) بنبض سريع (١١٠)، والسؤال يستبعد صراحة ضبط الإيقاع، فالخطوة الأساسية ضبط النبض بحاصر بيتا ليصل تحت ١٠٠.",
        "بما إنه «سليم طبيًا» بدون عوامل خطر سكتة واضحة، المصدر اختار إضافة الأسبرين مع حاصر البيتا (<bdi>bisoprolol</bdi>) بدل مميع كامل."],
    "when_changes": ["لو ارتفعت درجة خطورة السكتة (<bdi>CHA2DS2-VA ≥2</bdi>، مثل سكري أو ضغط مزمن أو سكتة سابقة)، الجواب يتحول لمضاد تخثر فموي مباشر مع حاصر بيتا."],
    "rule": "<bdi>A-fib</bdi> مستقر وسؤال عن النبض مو الإيقاع = حاصر بيتا؛ خطورة سكتة منخفضة = أسبرين لا مميع كامل.",
    "comparison": None, "labs": [["HR", "110 bpm", "60-100 bpm طبيعي"], ["BP", "110/70 mmHg", "مستقر"]], "guideline_note": None},

"AS-0854": {"correct_letter": "A", "self_judged": False,
    "idea": "سؤال عن المدى «المثالي» لـ<bdi>LDL-cholesterol</bdi> بشكل عام، بدون ذكر مرض قلبي وعائي سابق.",
    "clues": [("LDL-cholesterol", "القيمة المطلوب تحديد مداها"), ("Optimal range", "المدى المثالي العام، مو هدف بوجود مرض سابق")],
    "why_correct": [
        "المصدر يختار <bdi>&lt;2.5 mmol/L</bdi> كمدى «مثالي» عام، وهذا يطابق <bdi>LDL</bdi> المثالي الكلاسيكي (أقل من حوالي ١٠٠ ملغ/دل) لشخص بدون مرض تصلب شرايين مؤكد."],
    "when_changes": ["لو ذُكر مرض قلبي وعائي مؤكد (احتشاء، سكتة، مرض شرايين محيطية)، الهدف ينخفض لحوالي ٢.٠ أو أقل."],
    "rule": "بدون مرض تصلب شرايين مؤكد = هدف <bdi>LDL &lt;2.5 mmol/L</bdi>؛ مع مرض مؤكد = هدف أقل من ٢.٠.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0868": {"correct_letter": "B", "self_judged": False,
    "idea": "مريض ١٣-١٥ سنة، تاريخ عائلي سكري، عطش وكثرة تبول، سكر صائم ونسبة سكر تراكمي فوق الطبيعي بفحصين — السكري مؤكد، السؤال عن أول علاج.",
    "clues": [("family hx of diabetes", "عامل خطر قوي لسكري النوع الثاني بالشباب"),
               ("thirst and polyuria", "أعراض سكري كلاسيكية"),
               ("Fasting glucose 8 to 10 mmol", "فحص أول غير طبيعي"),
               ("Hb a1c above 7 , 7.8 %", "فحص ثاني غير طبيعي يؤكد التشخيص")],
    "why_correct": [
        "التشخيص مؤكد فعلاً: أعراض كلاسيكية (عطش وكثرة تبول) مع فحصين غير طبيعيين — سكر صائم فوق ٧ وسكر تراكمي ٧.٨٪ (فوق ٦.٥٪) — والتاريخ العائلي القوي يرجّح سكري النوع الثاني بالشباب.",
        "بمراهق مستقر استقلابيًا (بدون كيتونات، وسكر تراكمي تحت ٨.٥٪ تقريبًا)، العلاج يبدأ بتعديل نمط الحياة مع <bdi>metformin</bdi>، وهو الدواء الأول من عمر ١٠ سنوات فما فوق."],
    "when_changes": ["لو كان فيه كيتونات أو حماض كيتوني أو سكر تراكمي فوق ٨.٥٪ مع أعراض شديدة، العلاج يبدأ بالإنسولين أولاً."],
    "rule": "فحصان غير طبيعيان يؤكدان السكري؛ مراهق مستقر بدون كيتونات = نمط حياة + <bdi>metformin</bdi>.",
    "comparison": None, "labs": [["Fasting glucose", "8-10 mmol/L", "&lt;5.6 mmol/L طبيعي"], ["HbA1c", "7.8%", "&lt;5.7% طبيعي، ≥6.5% سكري"]], "guideline_note": None},

"AS-0868B": {"correct_letter": "B", "self_judged": False,
    "idea": "امرأة شابة، <bdi>BMI 31</bdi>، سكر تراكمي ٧.٨٪، ضغط طبيعي وبدون أمراض مصاحبة — أول علاج دوائي للسكري.",
    "clues": [("BMI 31", "بدانة — يفضّل دواء لا يزيد الوزن"), ("HbA1C 7.8", "سكري مؤكد بمستوى متوسط"), ("first line anti-diabetic", "السؤال عن الدواء الأول تحديدًا")],
    "why_correct": [
        "امرأة بدينة بسكري تراكمي ٧.٨٪ بدون أمراض مصاحبة عندها سكري نوع ثاني كلاسيكي؛ مستوى السكر التراكمي بين ٧.٥-١٠٪ عند التشخيص يعني نمط حياة مع <bdi>metformin</bdi>.",
        "<bdi>metformin</bdi> هو الدواء الأول: محايد للوزن، لا يسبب نقص سكر لوحده، ورخيص."],
    "when_changes": ["لو كان السكر التراكمي فوق ١٠٪ أو مع كيتونات، الجواب يتحول للإنسولين أولاً."],
    "rule": "الدواء الأول لسكري النوع الثاني = <bdi>metformin</bdi> مع نمط الحياة، إلا بوجود قصور كلوي شديد أو سكر تراكمي فوق ١٠٪.",
    "comparison": None, "labs": [["HbA1c", "7.8%", "≥6.5% سكري"]], "guideline_note": None},

"AS-0869": {"correct_letter": "B", "self_judged": False,
    "idea": "مريض تاريخ عائلي قوي للسكري، عطش عرضي وتعب، سكر صائم واحد ٧.٥ بدون ذكر سكر تراكمي — فحص واحد غير طبيعي، السؤال عن أولوية الإدارة.",
    "clues": [("strong family history of diabetes", "عامل خطر قوي"), ("occasionally thirst", "عرض خفيف غير قاطع"), ("fasting blood glucose (FBG ) is 7.5 mmol/L", "فحص واحد فقط غير طبيعي"), ("No Mention Of A1c", "ما فيه فحص ثاني يؤكد التشخيص")],
    "why_correct": [
        "فحص صائم واحد فقط بقيمة ٧.٥ بدون سكر تراكمي، مع أعراض خفيفة غير قاطعة (عطش عرضي وتعب)، ما يكفي لتأكيد السكري.",
        "التشخيص يحتاج فحصين غير طبيعيين، فالأولوية إعادة الفحص (أو إضافة سكر تراكمي) قبل تسمية التشخيص أو بدء أي دواء."],
    "when_changes": ["لو ظهرت قيمة ثانية غير طبيعية (مثل سكر تراكمي ≥٦.٥٪)، الجواب يتحول لبدء <bdi>metformin</bdi> مباشرة."],
    "rule": "فحص غير طبيعي واحد = أكّدي أولاً بفحص ثاني؛ فحصان غير طبيعيان = شخّصي وابدئي العلاج.",
    "comparison": None, "labs": [["FBG", "7.5 mmol/L", "&lt;5.6 طبيعي، 5.6-6.9 مقدمات سكري، ≥7.0 سكري"]], "guideline_note": None},

"AS-0875": {"correct_letter": "B", "self_judged": False,
    "idea": "رجل ٢٥ سنة، نقص وزن وألم بطن وبراز دموي، والأم والإخوة عندهم نفس الأعراض — مرض وراثي بالقولون ينتقل عائليًا بشكل سائد.",
    "clues": [("25-year-old", "عمر مبكر لمرض وراثي يتقدم باكرًا"), ("bloody stools", "نزيف من آفات قولونية متعددة"), ("mother and siblings", "توريث عمودي يوحي بمرض سائد")],
    "why_correct": [
        "رجل بعمر ٢٥ سنة بألم بطن ونقص وزن وبراز دموي، وأمه وإخوته عندهم نفس الصورة، يطابق مرض وراثي سائد بالقولون: <bdi>familial adenomatous polyposis (FAP)</bdi>.",
        "<bdi>FAP</bdi> يظهر بالشباب بنزيف وإسهال ونقص وزن من مئات السلائل (<bdi>polyps</bdi>)، ويتطور لسرطان قولون لو لم يُعالج؛ البطن الطبيعي بالفحص يتماشى مع مرض غشائي داخل التجويف."],
    "when_changes": ["لو ظهرت تصبغات بالشفايف أو الفم أو انغلاف معوي، الجواب يتحول لـ<bdi>Peutz-Jeghers syndrome</bdi>."],
    "rule": "شاب + نزيف شرجي + تاريخ عائلي عمودي قوي (أم وإخوة) = فكّري <bdi>FAP</bdi> أولاً.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0876": {"correct_letter": "C", "self_judged": False,
    "idea": "رجل ٥٥ سنة تعب يومين، فحص وتخطيط قلب طبيعيان، بوتاسيوم ٦.٦ وبيكربونات منخفضة — فرط بوتاسيوم بدون تغيرات تخطيط، العلاج الأولي.",
    "clues": [("lethargy", "عرض فرط البوتاسيوم العام"), ("ECG shows no acute changes", "أهم جزء — ينفي الحاجة لتثبيت غشاء القلب فورًا"), ("Potassium 6.6", "فرط بوتاسيوم كبير"), ("Bicarbonate 15", "حماض مصاحب")],
    "why_correct": [
        "<bdi>K 6.6</bdi> فرط بوتاسيوم كبير، لكن العلامات الحيوية مستقرة وتخطيط القلب بدون تغيرات حادة، فتثبيت الغشاء بالكالسيوم مو إلزامي فورًا.",
        "العلاج الأولي الأنسب نقل البوتاسيوم للداخل بـ<bdi>insulin plus dextrose</bdi>، اللي يعمل خلال دقائق."],
    "when_changes": ["لو ظهرت موجات <bdi>T</bdi> مدببة أو توسع <bdi>QRS</bdi> بتخطيط القلب، الجواب يتحول لـ<bdi>calcium gluconate</bdi> وريدي أولاً."],
    "rule": "فرط بوتاسيوم بدون تغيرات تخطيط = <bdi>insulin + dextrose</bdi>؛ وجود تغيرات تخطيط = كالسيوم أولاً لتثبيت القلب.",
    "comparison": None, "labs": [["Potassium", "6.6 mmol/L", "3.5-5.1 mmol/L طبيعي"], ["Bicarbonate", "15 mmol/L", "21-28 mmol/L طبيعي"]], "guideline_note": None},

"AS-0877": {"correct_letter": "D", "self_judged": False,
    "idea": "رجل ٥٥ سنة، سكري وضغط حديث التشخيص، بدأ على أسبرين وميتفورمين وليزينوبريل وهيدروكلوروثيازايد، صار ألم واحمرار وتورم بمفصل إصبع القدم الكبير — نوبة نقرس من دواء مُحدث.",
    "clues": [("severe pain, redness, and swelling of the first metatarsophalangeal (MTP) joint", "الصورة الكلاسيكية لنوبة نقرس حادة")],
    "why_correct": [
        "ألم واحمرار وتورم حاد بمفصل إصبع القدم الكبير بعد أدوية جديدة هي نوبة نقرس كلاسيكية (<bdi>podagra</bdi>).",
        "<bdi>Hydrochlorothiazide</bdi> السبب الكلاسيكي: الثيازيد يقلل إفراغ الكلية لحمض اليوريك، يسبب فرط حمض يوريك ويحفز نوبات النقرس."],
    "when_changes": ["لو كان الدواء الجديد مدر عروة (<bdi>furosemide</bdi>) بدل الثيازيد، هو كمان يسبب فرط حمض يوريك ويصير السبب."],
    "rule": "نوبة نقرس بعد بدء علاج جديد = شكّي بالمدرات (ثيازيد أو عروة) أولاً، لا بـ<bdi>metformin</bdi> ولا <bdi>ACE inhibitor</bdi>.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0879": {"correct_letter": "A", "self_judged": True,
    "idea": "مريض دخل العناية المركزة بسبب انصمام رئوي بدون تقرير عن العلامات الحيوية — لا يوجد وصف صريح لعدم استقرار.",
    "clues": [("pulmonary embolism", "التشخيص الأساسي"), ("no vital report", "ما فيه معلومة عن الاستقرار الهيموديناميكي")],
    "why_correct": [
        "بدون وصف صريح لعدم استقرار (هبوط ضغط، صدمة)، لا يوجد مبرر لافتراض <bdi>massive PE</bdi>، فالخطة القياسية تبدأ بمميع من فئة <bdi>LMWH</bdi> مثل <bdi>enoxaparin</bdi> كخط أول للانصمام الرئوي المستقر."],
    "when_changes": ["لو ذُكر صراحة هبوط ضغط أو صدمة (<bdi>massive PE</bdi>)، الجواب يتحول للتحليل الخثري (<bdi>thrombolysis</bdi>)."],
    "rule": "انصمام رئوي بدون دليل على عدم استقرار = <bdi>enoxaparin</bdi>؛ «<bdi>massive</bdi>» أو هبوط ضغط = <bdi>thrombolysis</bdi>.",
    "comparison": None, "labs": None,
    "guideline_note": "ما فيه جواب مؤكد من المصدر هنا؛ اخترنا <bdi>enoxaparin</bdi> لأن السؤال ما ذكر عدم استقرار صريح، بعكس AS-0880 اللي يذكر «<bdi>massive</bdi>» صراحة."},

"AS-0880": {"correct_letter": "B", "self_judged": False,
    "idea": "رجل ٣٥ سنة سليم طبيًا، دخل العناية المركزة بانصمام رئوي «<bdi>massive</bdi>» — العلاج الأولي الأنسب.",
    "clues": [("massive pulmonary embolism", "عدم استقرار هيموديناميكي صريح")],
    "why_correct": [
        "«<bdi>massive pulmonary embolism</bdi>» عند مريض بالعناية المركزة يعني عدم استقرار هيموديناميكي (خطورة عالية).",
        "بشاب سليم بدون مضاد استطباب للتحليل الخثري، <bdi>thrombolysis</bdi> هو العلاج الأولي الأنسب، يليه الهيبارين."],
    "when_changes": ["لو كان مستقر (بدون «<bdi>massive</bdi>» أو هبوط ضغط)، الجواب يتحول لـ<bdi>LMWH</bdi> مباشرة."],
    "rule": "«<bdi>massive</bdi>» أو هبوط ضغط/صدمة بانصمام رئوي = <bdi>thrombolysis</bdi>؛ مستقر = <bdi>LMWH</bdi>.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0881": {"correct_letter": "C", "self_judged": True,
    "idea": "مريض تشخص بـ<bdi>STEMI</bdi> وعولج حسب البروتوكول — السؤال عن الأدوية طويلة المدى من بين الخيارات المتاحة.",
    "clues": [("stemi", "احتشاء مؤكد يحتاج علاج وقاية ثانوية مدى الحياة"), ("long term", "السؤال عن الاستمرار طويل المدى، مو العلاج الحاد")],
    "why_correct": [
        "بعد <bdi>STEMI</bdi>، أدوية الوقاية الثانوية الأساسية مدى الحياة هي الأسبرين وستاتين عالي الجرعة (مع حاصر بيتا ومثبط <bdi>ACE</bdi>).",
        "من بين الخيارات المتاحة، <bdi>aspirin with high-intensity statin</bdi> هو الأقرب لهذا المبدأ (أسبرين لازم يستمر، والستاتين لازم يكون بجرعة عالية مهما كان الكوليسترول)."],
    "when_changes": ["لو كان فيه خيار يجمع الأسبرين والستاتين العالي مع حاصر بيتا ومثبط <bdi>ACE</bdi> معًا، هو الأكمل والأفضل."],
    "rule": "بعد <bdi>STEMI</bdi> = أسبرين + ستاتين عالي الجرعة مدى الحياة كحد أدنى، بالإضافة لحاصر بيتا ومثبط <bdi>ACE</bdi> حسب الحالة.",
    "comparison": None, "labs": None,
    "guideline_note": "ما فيه جواب مؤكد من المصدر؛ اخترنا الخيار اللي يجمع الأسبرين مع الستاتين عالي الجرعة لأنه أقرب لحزمة الوقاية الثانوية القياسية بعد الاحتشاء."},

"AS-0882": {"correct_letter": "B", "self_judged": False,
    "idea": "أي نتيجة زرع بول تعتبر مهمة أو مشخّصة لعدوى المسالك البولية.",
    "clues": [("significant or diagnostic for uti", "المعيار المختبري المطلوب")],
    "why_correct": [
        "زرع البول يكون مهمًا لما تنمو جرثومة واحدة بعدد مستعمرات ١٠^٥ أو أكثر بكل مل من عينة بول وسطية نظيفة.",
        "جرثومة واحدة بعدد عالي تعكس عدوى حقيقية بالمثانة، مو تلوث من الجلد أو منطقة العجان."],
    "when_changes": ["لو كانت العينة مأخوذة بشفط فوق العانة، أي نمو جرثومي (حتى بعدد قليل) يعتبر مهم."],
    "rule": "جرثومة واحدة بعدد ≥١٠^٥ = عدوى حقيقية؛ أكثر من جرثومة معًا = تلوث، كرري العينة.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0887": {"correct_letter": "B", "self_judged": False,
    "idea": "رجل ٢٨ سنة سليم سابقًا، ألم بالربع العلوي الأيمن وقيء ٥ أيام، تلا ذلك يرقان بالعين والجلد، بدون كحول أو مخدرات، إنزيمات كبد عالية جدًا — التهاب كبد فيروسي حاد.",
    "clues": [("yellowish discolouration", "يرقان حقيقي، مو مجرد شحوب"), ("Alanine aminotransferase 990", "ارتفاع ضخم بإنزيم الكبد يوجه لالتهاب كبدي خلوي"), ("Aspartate aminotransferase 789", "ارتفاع مماثل يؤكد الصورة الخلوية")],
    "why_correct": [
        "شخص «سليم سابقًا» بعمر ٢٨ سنة بألم بطن وقيء ثم يرقان، مع <bdi>ALT 990</bdi> و<bdi>AST 789</bdi> لكن <bdi>ALP</bdi> طبيعي، صورة التهاب كبد خلوي حاد مو انسدادي.",
        "بشخص صغير بدون كحول أو أدوية، التهاب الكبد الفيروسي <bdi>A</bdi> هو أشيع سبب لالتهاب كبد فيروسي حاد، ويُؤكد التشخيص الحاد بفحص <bdi>anti-HAV IgM</bdi>."],
    "when_changes": ["لو كان عنده عامل خطر لـ<bdi>HBV</bdi> (جنس غير محمي، تعاطي وريدي، تماس مصاب)، الفحص الأول يتحول لـ<bdi>HBsAg</bdi>."],
    "rule": "صورة التهاب كبد خلوي حاد بشاب سليم = <bdi>HAV IgM</bdi>؛ <bdi>IgM</bdi> = عدوى حالية، <bdi>IgG</bdi> = مناعة أو عدوى سابقة.",
    "comparison": None, "labs": [["ALT", "990 IU/L", "5-40 IU/L طبيعي"], ["AST", "789 IU/L", "12-40 IU/L طبيعي"], ["ALP", "109 IU/L", "39-117 IU/L طبيعي"]], "guideline_note": None},

"AS-0890": {"correct_letter": "A", "self_judged": False,
    "idea": "امرأة ٤٦ سنة، أصابع متورمة بشكل «سجق» بالكف اليسرى مع تنقر بالأظافر — السؤال عن ماذا نتوقع نلقاه بالتاريخ.",
    "clues": [("Sausage digits", "تورم كامل الإصبع — علامة مفصلية مميزة"), ("nail pitting", "تغيّر بالأظافر مرتبط بمرض جلدي")],
    "why_correct": [
        "«أصابع السجق» (<bdi>dactylitis</bdi>) مع «تنقر الأظافر» (<bdi>nail pitting</bdi>) توقيع <bdi>psoriatic arthritis</bdi>.",
        "أكثر شي متوقع بالتاريخ هو مشكلة جلدية — لويحات <bdi>psoriasis</bdi> (عند المريضة أو قريب درجة أولى)، واللي غالبًا تسبق التهاب المفصل."],
    "when_changes": ["لو كان المريض يشكو حرارة وتعب وزيادة شرب ماء بدل الأصابع المتورمة، نفكر بأسباب هرمونية زي فرط الدرقية بدل <bdi>psoriatic arthritis</bdi>."],
    "rule": "<bdi>dactylitis</bdi> + <bdi>nail pitting</bdi> = <bdi>psoriatic arthritis</bdi>، اسألي عن <bdi>psoriasis</bdi> بالتاريخ الشخصي أو العائلي.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0894": {"correct_letter": "D", "self_judged": False,
    "idea": "امرأة ٤٤ سنة تورم رقبة ٣ أشهر، بدون أعراض، عقدة درقية ٢×٢ سم — الخطوة الأولى بتقييم العقدة.",
    "clues": [("asymptomatic", "ما فيه أعراض فرط أو قصور درقية واضحة"), ("thyroid nodule 2x2 cm", "عقدة واضحة سريريًا تحتاج تقييم منظم")],
    "why_correct": [
        "أي عقدة درقية ملموسة، الخطوة الأولى بتقييمها هي فحص <bdi>TSH</bdi>، لأن وظيفة الدرقية تحدد المسار التالي.",
        "لو <bdi>TSH</bdi> منخفض، نفكر بعقدة «حارة» مفرطة النشاط تحتاج مسح نووي ونادرًا تحتاج خزعة؛ لو طبيعي أو مرتفع، نروح للسونار لتحديد الحاجة لخزعة (<bdi>FNA</bdi>)."],
    "when_changes": ["لو كان <bdi>TSH</bdi> مذكور أصلاً طبيعي، الخطوة التالية تتحول مباشرة للسونار الدرقي."],
    "rule": "عقدة درقية: <bdi>TSH</bdi> أولاً، ثم سونار، ثم خزعة (<bdi>FNA</bdi>) لو استوفت المعايير.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0907": {"correct_letter": "A", "self_judged": False,
    "idea": "رجل ٦٧ سنة معروف بـ<bdi>Afib</bdi> وضغط واكتئاب، جاء بأرق وتهيج وخفقان، على <bdi>amiodarone</bdi> وغيره — أعراض تشبه فرط الدرقية بسبب الدواء.",
    "clues": [("insomnia , irritability and palpitation", "أعراض فرط درقية، ممكن تُنسب خطأ للاكتئاب"), ("amiodarone", "دواء غني باليود يأثر على الدرقية")],
    "why_correct": [
        "<bdi>amiodarone</bdi> غني باليود وممكن يسبب فرط أو قصور درقية.",
        "الأرق والتهيج والخفقان أعراض فرط درقية كلاسيكية، فالخطوة الأولى قياس <bdi>free T4</bdi> و<bdi>TSH</bdi> قبل ما نحكم إنها بسبب الاكتئاب أو نعالج الأعراض بشكل عشوائي."],
    "when_changes": ["لو طلعت وظائف الدرقية طبيعية، يصير منطقي نراجع التشخيص النفسي أو نفكر بسبب آخر للأعراض."],
    "rule": "أعراض جديدة تشبه النفسية عند مريض على <bdi>amiodarone</bdi> = فحصي وظائف الدرقية أولاً قبل أي شي ثاني.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0911": {"correct_letter": "A", "self_judged": False,
    "idea": "مراهق ١٧ سنة، توقف مفاجئ بالحركة بدون سقوط لمدة ١٥ ثانية مع لعق الشفايف، تخطيط الدماغ يُظهر موجة شوكية ٣ هرتز — نوبة غياب كلاسيكية.",
    "clues": [("sudden movement stop without falling for 15 seconds", "توقف قصير بدون سقوط ولا وعي كامل مفقود طويلاً"), ("EEG : 3 Hz spike", "النمط الكهربائي المميز لنوبات الغياب")],
    "why_correct": [
        "توقف الحركة فجأة بدون سقوط لمدة قصيرة (حوالي ١٥ ثانية) مع حركات آلية مثل لعق الشفايف، وتخطيط دماغ يُظهر موجة شوكية ٣ هرتز، هي نوبات الغياب (<bdi>absence seizure</bdi>) الكلاسيكية.",
        "<bdi>Ethosuximide</bdi> هو الدواء الأول لنوبات الغياب (والبديل <bdi>valproate</bdi>)."],
    "when_changes": ["لو ترافقت نوبات الغياب مع نوبات تشنجية كبرى (<bdi>GTC</bdi>) بمراهق، الدواء يتحول لـ<bdi>valproate</bdi> لأنه يغطي النوعين معًا."],
    "rule": "موجة شوكية ٣ هرتز + توقف قصير بدون سقوط = نوبة غياب = <bdi>ethosuximide</bdi>؛ تجنبي <bdi>phenytoin</bdi> و<bdi>carbamazepine</bdi> اللي ممكن تسوّئها.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0914": {"correct_letter": "A", "self_judged": False,
    "idea": "امرأة ٣١ سنة، أزيز وضيق تنفس يومي يحد نشاطها عدة مرات أسبوعيًا، مشخّصة بربو «<bdi>moderate persistent</bdi>» — الخطوة العلاجية المناسبة فوق المنفّس السريع.",
    "clues": [("daily wheezing", "أعراض يومية — تحدد الدرجة"), ("moderate persistent asthma", "التصنيف المؤكد صراحة بالسؤال")],
    "why_correct": [
        "أزيز يومي يحد النشاط عدة مرات بالأسبوع يحدد درجة الربو «<bdi>moderate persistent</bdi>»، وهذي الدرجة أعلى من اللي يُضبط بـ<bdi>ICS</bdi> لوحده.",
        "العلاج المفضل بهذي الدرجة إضافة <bdi>low-dose inhaled corticosteroid</bdi> مع <bdi>long-acting B2-agonist (LABA)</bdi> معًا فوق المنفّس السريع."],
    "when_changes": ["لو كانت الأعراض أكثر من مرتين أسبوعيًا بس مو يومية (<bdi>mild persistent</bdi>)، يكفي <bdi>low-dose ICS</bdi> لوحده بدون <bdi>LABA</bdi>."],
    "rule": "أعراض «يومية» = ربو متوسط مستمر = <bdi>ICS + LABA</bdi>؛ أبدًا لا تعطي <bdi>LABA</bdi> لوحده بدون <bdi>ICS</bdi>.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0915": {"correct_letter": "D", "self_judged": False,
    "idea": "رجل ٤٤ سنة، ضيق تنفس بالمجهود، نفخة انبساطية مبكرة بقاعدة القلب تزيد شدتها ومدتها مع الشهيق — تحديد الصمام المصاب حسب جهة النفخة وتأثرها بالتنفس.",
    "clues": [("early diastolic murmur", "نفخة انبساطية مبكرة — ترشّح صمامين فقط بقاعدة القلب"), ("increase during INSPIRATION", "المفتاح — الجانب الأيمن يقوى بالشهيق")],
    "why_correct": [
        "نفخة انبساطية مبكرة بقاعدة القلب تضيّق الاحتمال لصمام الأبهر أو الصمام الرئوي، والشهيق يرفع العود الوريدي للقلب الأيمن فتقوى النفخات اليمنى (نفس مبدأ علامة <bdi>Carvallo</bdi> بالارتجاع ثلاثي الشرف).",
        "نفخة يمنى انبساطية مبكرة بقاعدة القلب تعني ارتجاع الصمام الرئوي (<bdi>pulmonary regurgitation</bdi>)."],
    "when_changes": ["لو كانت النفخة تقوى بالزفير وهو مائل للأمام، الجواب يتحول لارتجاع الأبهر (<bdi>aortic regurgitation</bdi>)."],
    "rule": "نفخة انبساطية مبكرة بقاعدة القلب: تقوى بالشهيق = <bdi>pulmonary regurgitation</bdi>؛ تقوى بالزفير ومائل للأمام = <bdi>aortic regurgitation</bdi>.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0915B": {"correct_letter": "D", "self_judged": False,
    "idea": "نفخة انبساطية مبكرة بحافة القص تقوى بالانحناء للأمام، تخطيط القلب يُظهر تضخم البطين الأيسر — صمام أيسر مصاب بارتجاع.",
    "clues": [("early diastolic murmur", "نفخة انبساطية مبكرة بحافة القص"), ("increased by leaning forward", "تقوى بالزفير والانحناء للأمام — جانب أيسر"), ("left ventricular hypertrophy", "نتيجة حمل زائد مزمن على البطين الأيسر")],
    "why_correct": [
        "نفخة انبساطية مبكرة بحافة القص تقوى بالانحناء للأمام (وبالزفير الكامل) هي ارتجاع الأبهر (<bdi>aortic regurgitation</bdi>).",
        "الحمل الحجمي المزمن على البطين الأيسر يفسر تضخمه (<bdi>LVH</bdi>) بتخطيط القلب."],
    "when_changes": ["لو كانت النفخة انبساطية متوسطة منخفضة النبرة بقمة القلب مع انبساطة فتح، الجواب يتحول لتضيّق الصمام الميترالي."],
    "rule": "نفخة انبساطية مبكرة + انحناء للأمام = ارتجاع أبهري؛ نفخة انبساطية متوسطة بقمة القلب مع انبساطة فتح = تضيّق ميترالي.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0925": {"correct_letter": "C", "self_judged": False,
    "idea": "رجل ٤٠ سنة معروف نقرس على <bdi>allopurinol</bdi> بانتظام، صار عنده التهاب مفصل جديد بالكاحل والركبتين بالإضافة لإصبع القدم القديم، وهو معروف بـ<bdi>psoriasis</bdi> من سنين — تشخيص ثانٍ يفسر الصورة الجديدة.",
    "clues": [("known case of psoriasis", "تاريخ جلدي مزمن — مفتاح التشخيص"), ("no improvement", "التهاب فعّال رغم الالتزام بعلاج النقرس")],
    "why_correct": [
        "النقرس يفسر إصبع القدم الكبير، لكنه ما يفسر التهاب مفصل جديد فعّال بالكاحل الأيسر والركبتين رغم الالتزام بـ<bdi>allopurinol</bdi> بانتظام.",
        "برجل معروف بـ<bdi>psoriasis</bdi> من سنين، التهاب مفاصل كبيرة غير متناظر هو <bdi>psoriatic arthritis</bdi> لحد إثبات العكس — تاريخ الجلد هو الدليل الحاسم المزروع بالسؤال."],
    "when_changes": ["لو لم يكن له تاريخ <bdi>psoriasis</bdi> وكان حمض اليوريك مرتفع بوضوح، النوبة الجديدة تبقى نقرس فعال (استمرار رغم العلاج أحيانًا يحتاج ضبط الجرعة)."],
    "rule": "مرض جلدي خلفي (<bdi>psoriasis</bdi>) بسؤال التهاب مفاصل نادرًا يكون مجرد ديكور — غالبًا هو التشخيص.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0926": {"correct_letter": "A", "self_judged": False,
    "idea": "مسن بدون أعراض، تخطيط قلب يُظهر تضخم بطين أيسر، وصدى قلب يُظهر تضيّق صمام أبهري ثنائي الشرف شديد مع كسر قذفي طبيعي — الإدارة المناسبة.",
    "clues": [("asymptomatic", "أهم جزء — غياب الأعراض يمنع التدخل الفوري"), ("Severe bicuspid aortic stenosis", "تضيّق شديد تشريحيًا"), ("Normal left ventricular ejection fraction", "وظيفة ضخ محفوظة")],
    "why_correct": [
        "رغم إن التضيّق شديد تشريحيًا (صمام ثنائي الشرف مع <bdi>LVH</bdi>)، المريض بدون أعراض وكسر القذف طبيعي.",
        "الأعراض (ذبحة، إغماء، ضيق تنفس) أو ضعف وظيفة البطين الأيسر هما اللي يستدعيان استبدال الصمام؛ غيابهما يعني متابعة بسونار دوري مع تدخل فوري بظهور أي منهما."],
    "when_changes": ["لو ظهرت أعراض (ذبحة أو إغماء أو ضيق تنفس) أو انخفض كسر القذف تحت ٥٠٪، الجواب يتحول لاستبدال الصمام."],
    "rule": "قاعدة الصمامات: بدون أعراض = متابعة؛ أعراض أو ضعف وظيفة البطين = استبدال الصمام.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0928": {"correct_letter": "C", "self_judged": False,
    "idea": "مريض سكري وضغط، شُخّص حديثًا بارتفاع كوليسترول، صار عنده تشنج عضلي وعدم راحة بالساقين — عرض جانبي كلاسيكي لدواء الكوليسترول.",
    "clues": [("high cholesterol level", "تشخيص حديث يوحي ببدء علاج جديد"), ("cramps in muscle", "عرض جانبي شائع لدواء خفض الدهون")],
    "why_correct": [
        "مريض شُخّص حديثًا بارتفاع كوليسترول (يعني غالبًا بدأ على ستاتين)، وصار عنده تشنج عضلي وعدم راحة بالساقين — هذي أعراض عضلية مرتبطة بالستاتين.",
        "<bdi>Atorvastatin</bdi> هو السبب الأرجح؛ الخطوة التالية فحص <bdi>CK</bdi> ومراجعة الجرعة."],
    "when_changes": ["لو كان على مدر ثيازيدي وكان البوتاسيوم منخفض بالتحاليل، التشنج يتحول سببه لنقص البوتاسيوم من المدر مو الستاتين."],
    "rule": "تشنج عضلي بعد بدء دواء كوليسترول = فكّري بالستاتين أولاً (<bdi>statin myopathy</bdi>)، وافحصي <bdi>CK</bdi>.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0928B": {"correct_letter": "C", "self_judged": False,
    "idea": "مريض على حاصر بيتا ومثبط <bdi>ACE</bdi> و<bdi>salbutamol</bdi> ومدر ثيازيدي، جاء بدوخة وتشنج عضلي والتحاليل تُظهر بوتاسيوم منخفض — أي دواء هو السبب المزمن.",
    "clues": [("low potassium", "القيمة المخبرية المحورية بالسؤال")],
    "why_correct": [
        "المدرات الثيازيدية تزيد وصول الصوديوم للنبيب البعيد وتسبب فقدان كلوي للبوتاسيوم مع حماض قلوي استقلابي، فهي السبب المزمن الأرجح بهذا النظام الدوائي الثابت."],
    "when_changes": ["لو كان السياق حاد (استنشاق متكرر لـ<bdi>salbutamol</bdi> بنوبة ربو حادة)، الانخفاض المفاجئ بالبوتاسيوم يتحول سببه لـ<bdi>salbutamol</bdi> نفسه بدل الثيازيد."],
    "rule": "مدرات ثيازيدية وعروة تُنقص البوتاسيوم؛ مثبط <bdi>ACE</bdi>/<bdi>ARB</bdi> وحاصر البيتا يرفعانه.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0931": {"correct_letter": "B", "self_judged": False,
    "idea": "مريض رجع من أفريقيا بحمى متقطعة وأعراض تشبه الملاريا — السؤال عن العلاج المناسب من بين الخيارات المتاحة فقط.",
    "clues": [("went to africa", "تماس وبائي بمنطقة الملاريا"), ("intermittent fever", "نمط حمى كلاسيكي للملاريا")],
    "why_correct": [
        "مسافر عائد من أفريقيا بحمى متقطعة وصورة تشبه الملاريا تُعتبر ملاريا لحد ما ينفيها مسحة الدم.",
        "جواب هذا السؤال المسجل هو <bdi>Chloroquine</bdi> لأنه كان الدواء المضاد للملاريا الوحيد المتاح بالخيارات، والباقي كانت مضادات جراثيم أو فيروسات بدون أي فعالية ضد الطفيلي."],
    "when_changes": ["لو ظهر بالخيارات دواء من فئة <bdi>ACT (artemisinin-based combination therapy)</bdi> لملاريا <bdi>falciparum</bdi> من أفريقيا، هو الأفضل ويتفوق على الكلوروكين لمقاومته الواسعة هناك."],
    "rule": "حمى متقطعة بعد سفر لأفريقيا = ملاريا لحد إثبات العكس؛ اقرئي الخيارات — لو فيه <bdi>ACT</bdi> أو <bdi>artesunate</bdi> هو الأفضل من الكلوروكين.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0940": {"correct_letter": "B", "self_judged": False,
    "idea": "مريض انخفاض بموجة <bdi>ST</bdi> وارتفاع التروبونين (بدون ذكر توقيت) — السؤال عن أفضل علاج «يُبدأ» فورًا.",
    "clues": [("st depression", "يستبعد <bdi>STEMI</bdi>"), ("elevated troponin", "يميز <bdi>NSTEMI</bdi> عن الذبحة غير المستقرة")],
    "why_correct": [
        "انخفاض <bdi>ST</bdi> مع ارتفاع التروبونين يعني <bdi>NSTEMI</bdi> (التروبونين يفصله عن الذبحة غير المستقرة، وغياب ارتفاع <bdi>ST</bdi> يفصله عن <bdi>STEMI</bdi>).",
        "كل مريض <bdi>NSTE-ACS</bdi> يبدأ بعلاج مضاد للصفائح مزدوج (أسبرين + <bdi>clopidogrel</bdi>) مع مضاد تخثر مثل الهيبارين، بينما توقيت القسطرة يتحدد لاحقًا حسب درجة الخطورة."],
    "when_changes": ["لو كان الموصوف ارتفاع <bdi>ST</bdi> (أو حصار حزمة يسرى جديد)، الجواب يتحول لإعادة ترويه فورية (قسطرة أولية أو تحليل خثري)."],
    "rule": "تخطيط القلب يحدد إعادة الترويه؛ التروبونين يحدد <bdi>NSTEMI</bdi> مقابل الذبحة؛ <bdi>NSTE-ACS</bdi> يبدأ دايمًا بأسبرين + مضاد صفائح ثاني + مضاد تخثر.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0941": {"correct_letter": "D", "self_judged": False,
    "idea": "مريض سكري وضغط، ضيق تنفس شديد وهبوط ضغط وتسرع قلب وتنفس، صدى قلب يُظهر تضخم بطين أيسر، <bdi>BNP</bdi> وتروبونين مرتفعين — نوع الصدمة.",
    "clues": [("hypotension, tachycardia", "صدمة فعلية"), ("LV hyper atrophy", "مرض قلبي كامن سبّب ضعف ضخ"), ("500 bnb", "<bdi>BNP</bdi> مرتفع يدعم قصور القلب")],
    "why_correct": [
        "سكري وضغط مع تضخم بطين أيسر بالصدى، <bdi>BNP</bdi> مرتفع، وتروبونين مرتفع واضح (١ مقابل الطبيعي ٠.٠٧)، كلها تشير لعضلة قلب فاشلة.",
        "إضافة ضيق تنفس وهبوط ضغط وتسرع قلب تعني فشل ضخ بنتاج قلبي منخفض، يعني صدمة قلبية المنشأ (<bdi>cardiogenic shock</bdi>)؛ ما فيه بالسؤال أي دليل نزيف أو إصابة نخاعية أو انسداد خارج القلب."],
    "when_changes": ["لو كان الصدى يُظهر انصباب تاموري كبير أو بطين أيمن متوسع ومجهد بدل تضخم البطين الأيسر، الجواب يتحول لصدمة انسدادية."],
    "rule": "هبوط ضغط + ضيق تنفس + <bdi>BNP</bdi> مرتفع + مرض بطين أيسر بالصدى = صدمة قلبية المنشأ؛ الصدمة الانسدادية تحتاج انصباب أو بطين أيمن مجهد.",
    "comparison": None, "labs": [["BNP", "500", "&lt;300 طبيعي"], ["Troponin", "1", "0.07 طبيعي"]], "guideline_note": None},

"AS-0944": {"correct_letter": "A", "self_judged": False,
    "idea": "حركة رعشية سريعة بالذراع لمدة قصيرة — نوع النوبة حسب المدة والشكل.",
    "clues": [("jerky movement", "حركة رعشية قصيرة — المفتاح لتحديد نوع النوبة")],
    "why_correct": [
        "حركة رعشية بالذراع تستمر لمدة قصيرة توصف بالنوبة النفضية (<bdi>myoclonic seizure</bdi>): نفضات عضلية مفاجئة وقصيرة شبيهة بالصدمة، غالبًا بالذراعين، مع وعي محفوظ عادة.",
        "القصر الزمني هو الدليل الحاسم؛ النوبة الرمعية (<bdi>clonic</bdi>) تكون رعشة إيقاعية مستمرة لفترة أطول."],
    "when_changes": ["لو كانت الحركة رعشة إيقاعية مستمرة لفترة أطول مع تغيّر بمستوى الوعي، الجواب يتحول لنوبة رمعية (<bdi>clonic</bdi>)."],
    "rule": "«رعشة قصيرة سريعة» = نفضية (<bdi>myoclonic</bdi>)؛ «رعشة إيقاعية مستمرة» = رمعية (<bdi>clonic</bdi>).",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0945": {"correct_letter": "D", "self_judged": False,
    "idea": "رجل ٣٣ سنة بميكانيكي سيارات، ضيق تنفس وتعب وسعال ليلي ترافق أيام العمل منذ ٨ أشهر، فحص رئوي وتصوير وقياس تنفس طبيعية بعد إجازة — ربو مهني محتمل يحتاج تأكيد موضوعي.",
    "clues": [("car repair shop", "تماس بمهيجات مهنية (أصباغ، <bdi>isocyanates</bdi>)"), ("symptoms are associated with his workdays", "ربط واضح بين الأعراض وأيام الدوام"), ("spirometry results are normal", "فحص طبيعي، لكن أُخذ بعد انقطاع عن العمل")],
    "why_correct": [
        "أعراض ترتبط بـ«أيام الدوام» عند عامل ورشة سيارات (تماس أصباغ ومواد كيميائية) توحي بربو مهني.",
        "بما إن الفحص أُخذ «بعد عدة أيام إجازة»، فحص قياس التنفس الطبيعي ما ينفي التشخيص، فالخطوة التالية تأكيد الرابطة موضوعيًا بإعادة قياس التنفس (أو قياسات متكررة لتدفق الذروة) بعد التعرض الفعلي بالعمل."],
    "when_changes": ["لو تأكد الرابط بين العمل والأعراض موضوعيًا، الخطوة التالية تصير النصح بتغيير العمل أو إبعاده عن مصدر التعرض."],
    "rule": "اشتباه ربو مهني مع فحوصات طبيعية بعد انقطاع عن العمل = أعيدي الفحص بعد التعرض الفعلي، لا تحكمي من فحص أُخذ بإجازة.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0946": {"correct_letter": "B", "self_judged": False,
    "idea": "امرأة ٣٣ سنة روماتويد من ٣ سنين، على <bdi>prednisone</bdi> و<bdi>methotrexate</bdi> و<bdi>etanercept</bdi>، تورم وألم حاد بالركبة اليسرى مع حمى خفيفة ٣ أيام — مفصل واحد ملتهب بمريضة مثبطة مناعيًا.",
    "clues": [("rheumatoid arthritis", "خلفية مرض مفاصل مزمن"), ("pain and swelling of the left knee and low-grade fever", "التهاب حاد بمفصل واحد مع حمى"), ("prednisone, methotrexate, and etanercept", "تثبيط مناعي كبير يرفع خطر العدوى")],
    "why_correct": [
        "تورم حاد بمفصل واحد (الركبة) مع حمى خفيفة بمريضة روماتويد مثبطة مناعيًا (ستيرويد + ميثوتريكسات + مضاد <bdi>TNF</bdi>) يُعتبر التهاب مفصل إنتاني لحد إثبات العكس.",
        "الخطوة الأولى بزل المفصل (<bdi>arthrocentesis</bdi>) مع صبغة غرام وزرع وعدّ خلايا وفحص بلورات، بالإضافة لزرع دم، قبل أي مضاد حيوي؛ التهاب المفاصل الخفيف بالأصابع مجرد نشاط روماتويد خلفي."],
    "when_changes": ["لو كان الالتهاب يشمل عدة مفاصل بشكل متناظر بدون حمى، نفكر بنوبة نشاط للروماتويد نفسه مو عدوى."],
    "rule": "مفصل واحد يشتعل أكثر من الباقي بمريضة روماتويد مثبطة مناعيًا = التهاب مفصل إنتاني، ابزليه أولاً.",
    "comparison": None, "labs": None, "guideline_note": None},

"AS-0947": {"correct_letter": "D", "self_judged": False,
    "idea": "رجل ٣٥ سنة، حمى وتعرق ليلي وتعب وألم مفاصل وأسفل الظهر ٤ أشهر، تاريخ شرب حليب غير مبستر، التهاب بالركبة وحركة محدودة بالعمود الفقري، زرع الدم سلبي — عدوى مزمنة تحتاج فحص غير الزرع.",
    "clues": [("lower back pain", "إصابة عمودية مصاحبة"), ("history of unpasteurized milk ingestion", "مصدر العدوى المحتمل — المفتاح الحاسم"), ("Blood culture: Negative", "الزرع ما يفيد بهذي الحالة المزمنة")],
    "why_correct": [
        "حليب غير مبستر مع حمى متموجة ٤ أشهر وتعرق ليلي وألم مفاصل وأسفل ظهر مع التهاب بالركبة وحركة عمود فقري محدودة يطابق <bdi>brucellosis</bdi> عظمي مفصلي مزمن.",
        "زرع الدم كثيرًا يكون سلبي بالحالات المزمنة، فالخطوة العملية التالية فحص أجسام مضادة للبروسيلا (<bdi>serology</bdi>)."],
    "when_changes": ["لو كان الزرع المصلي غير حاسم، الخطوة التالية تتحول لزرع نخاع العظم اللي له حساسية أعلى من زرع الدم."],
    "rule": "حليب غير مبستر + حمى مزمنة + مرض عظمي مفصلي + زرع دم سلبي = فحص مصلي للبروسيلا، لا تكرري الزرع ولا تلجئي للخزعة مباشرة.",
    "comparison": None, "labs": None, "guideline_note": None},
}

WHY_WRONG = {
"AS-0776": {
    "B": "<bdi>Ceftriaxone</bdi> ما فيه تغطية ضد الزائفة، فإضافته أو التحويل له ما يضيف شي فوق <bdi>ceftazidime</bdi> بمريض نقص مناعة.",
    "C": "<bdi>Sulfamethoxazole</bdi> (<bdi>co-trimoxazole</bdi>) يُستخدم للوقاية أو علاج <bdi>Pneumocystis</bdi>، مو لحمى نقص بيضاء غير مفسرة.",
    "D": "<bdi>Vancomycin</bdi> يُضاف فقط بدواعٍ محددة (التهاب رئة، هبوط ضغط/إنتان، عدوى قسطرة أو جلد، <bdi>MRSA</bdi>)؛ السؤال استبعدها كلها صراحة."},
"AS-0776B": {
    "A": "<bdi>Rifampicin</bdi> مضاد جراثيم (يستخدم بالسل والبروسيلا)، بدون أي فعالية ضد الفطريات.",
    "B": "<bdi>Valaciclovir</bdi> مضاد فيروسي (للهربس والحماق النطاقي)، ما يعمل ضد <bdi>Aspergillus</bdi>.",
    "C": "<bdi>Tigecycline</bdi> مضاد جراثيم واسع الطيف للجراثيم المقاومة، ما يعالج عدوى فطرية."},
"AS-0777": {
    "B": "<bdi>Tazocin</bdi> بديل أول خط آخر ضد الزائفة، ما يضيف تغطية جديدة فعلية فوق <bdi>ceftazidime</bdi> لمريض ما يتحسن.",
    "C": "<bdi>Ceftriaxone</bdi> بدون تغطية ضد الزائفة، فهو تراجع بمريض نقص بيضاء.",
    "D": "<bdi>Trimethoprim-Sulfamethoxazole</bdi> للوقاية أو علاج <bdi>Pneumocystis</bdi>، مو تصعيد تجريبي لحمى نقص بيضاء."},
"AS-0780": {
    "A": "<bdi>TIPS</bdi> يُحجز للاستسقاء المتكرر اللي يحتاج بزل متكرر، مو كخطوة بعد فشل مدر واحد مباشرة."},
"AS-0781": {
    "A": "المدرات الوريدية ما لها دور بعلاج استسقاء التليف الكبدي، وترفع خطر أذية كلوية واضطراب كهارل.",
    "C": "زيادة جرعة المدر الفموي مناسبة باستسقاء متوسط، لكن ما تخفف استسقاء كبير بسرعة؛ وعند تصعيد المدرات نزيد <bdi>spironolactone</bdi> و<bdi>furosemide</bdi> معًا بنسبة ثابتة، مو فوروسمايد لوحده.",
    "D": "<bdi>TIPS</bdi> لحالات الاستسقاء المقاوم اللي يحتاج بزل متكرر، مو الخطوة التالية بهذا العرض."},
"AS-0782": {
    "A": "<bdi>norovirus</bdi> سببه الكلاسيكي تفشي حاد مع قيء بارز، مو إسهال مائي مزمن بدون سياق تفشي.",
    "C": "<bdi>shigella</bdi> سببه الكلاسيكي إسهال دموي مع حمى وتشنجات، مو إسهال مائي بسيط."},
"AS-0785": {
    "A": "<bdi>Ranitidine</bdi> (حاصر <bdi>H2</bdi>) ما يسبب تلون البراز.",
    "B": "<bdi>Pantoprazole</bdi> (<bdi>PPI</bdi>) ما يسبب برازًا أسود؛ هو العمود الأساسي لتثبيط الحمض بعلاج الاستئصال.",
    "D": "<bdi>Aluminium hydroxide</bdi> يسبب إمساك (أما مضادات الحموضة المحتوية مغنيسيوم فتسبب إسهال)، مو برازًا أسود."},
"AS-0788": {
    "A": "الأرز خالٍ من الغلوتين طبيعيًا وآمن تمامًا بـ<bdi>celiac disease</bdi>.",
    "B": "الذرة (<bdi>maize</bdi>) خالية من الغلوتين وآمنة.",
    "C": "البطاطس خالية من الغلوتين وآمنة."},
"AS-0791": {
    "A": "<bdi>Ampicillin</bdi> وريدي/عضلي بديل فقط لمن ما يقدر ياخذ دواء فموي؛ الأمكسيسيلين الفموي هو الخيار الأول.",
    "C": "<bdi>Clindamycin</bdi> كان الخيار القديم لحساسية البنسلين، وما عاد مفضل بإرشادات <bdi>AHA</bdi> الحديثة؛ ما فيه ذكر حساسية هنا.",
    "D": "<bdi>Ceftriaxone</bdi> وريدي/عضلي بديل لمن ما يقدر ياخذ دواء فموي، مو الخيار الأول."},
"AS-0793": {
    "A": "متابعة الكوليسترول سنويًا خطوة مراقبة لوقاية أولية بخطورة منخفضة؛ مريض بعد احتشاء يحتاج علاج الآن مو مراقبة فقط.",
    "B": "الاستمرار بالرياضة والحمية صحيح لكن غير كافٍ لوحده؛ بعد احتشاء، نمط الحياة دايمًا يُدمج مع ستاتين.",
    "D": "ضغط ١٣٩/٧٥ حدّي بس (الهدف بعد احتشاء أقل، حوالي ١٣٠/٨٠)، فالخطوة الأولى نمط حياة وإعادة قياس؛ الدواء الضغطي يُضاف لو استمر فوق الهدف، بينما الستاتين إلزامي بعد الاحتشاء مباشرة."},
"AS-0795": {
    "A": "<bdi>TB</bdi> يسبب حمى مزمنة ومرض بالعمود الفقري (مرض بوت)، لكنه يفضّل الفقرات الصدرية القطنية مو مفصل العجز الحرقفي، وما له ارتباط بالعمل مع الحيوانات.",
    "B": "<bdi>Syphilis</bdi> ممكن يسبب تغيّر سلوكي (<bdi>neurosyphilis</bdi>)، بس مو حمى طويلة مع التهاب مفصل عجزي حرقفي؛ يناسب أكثر مع تاريخ جنسي أو طفح أو قرحة.",
    "D": "<bdi>Toxoplasmosis</bdi> (تماس قطط أو لحم نيء) يسبب تضخم عقد لمفاوية، أو خراجات دماغية بنقص المناعة، مو التهاب مفصل عجزي حرقفي."},
"AS-0796": {
    "A": "<bdi>ACE inhibitor</bdi> يكرر نفس عمل <bdi>ARB</bdi> الموجود أصلاً؛ الجمع بينهما يرفع خطر فرط البوتاسيوم والأذية الكلوية، فيُتجنب.",
    "B": "حاصر ألفا خيار الدرجة الرابعة (ضغط مقاوم)، أو يُختار أولاً لو فيه أعراض تضخم بروستاتا مصاحبة؛ يجي بعد المدر.",
    "D": "حاصر بيتا يُحجز لدواعٍ خاصة (ذبحة، بعد احتشاء، قصور قلب، ضبط نبض) أو خطوات لاحقة؛ مو الدواء الثالث القياسي."},
"AS-0848": {
    "B": "<bdi>atrial flutter</bdi> إيقاع منتظم بموجات نشارية، بينما الصورة الموضحة تحديدًا تُظهر <bdi>A.fib</bdi>."},
"AS-0850": {
    "A": "<bdi>cardioversion</bdi> علاج لاضطرابات النظم السريعة غير المستقرة (<bdi>VT, SVT</bdi>، أو <bdi>fast AF</bdi>)؛ ما له دور برفع نبض بطيء.",
    "C": "<bdi>Aspirin</bdi> لعلاج <bdi>ACS</bdi>؛ ما فيه ألم صدر أو صورة إقفارية هنا، وما يأثر على النبض.",
    "D": "العلاج المضاد للصفائح المزدوج لـ<bdi>ACS</bdi> مؤكد أو بعد قسطرة، مو لبطء نبض عرضي."},
"AS-0853": {
    "A": "<bdi>Amiodarone</bdi> دواء ضبط إيقاع، والسؤال استبعد صراحة ضبط الإيقاع؛ وهو مو خط أول لضبط النبض بمريض مستقر بدون قصور قلب.",
    "B": "العلاج المضاد للصفائح المزدوج لمرض الشرايين التاجية (<bdi>ACS</bdi>، دعامات)، مو لـ<bdi>A-fib</bdi>؛ ما يضبط النبض وما يكفي للوقاية من السكتة.",
    "D": "مضاد تخثر فموي مباشر مع حاصر بيتا مناسب لو درجة الخطورة <bdi>CHA2DS2-VA ≥2</bdi>؛ هذا المريض «سليم طبيًا» فما يستحق مميع كامل حسب الدرجة."},
"AS-0854": {
    "B": "<bdi>&lt;2.2 mmol/L</bdi> مو حد معياري بأي مخطط أهداف رئيسي؛ يقع بين هدف الوقاية الأولية والثانوية.",
    "C": "<bdi>&lt;2.0 mmol/L</bdi> هدف أشد يُستخدم فقط بوجود مرض تصلب شرايين مؤكد، وما فيه تاريخ كذا هنا.",
    "D": "<bdi>&lt;3.0 mmol/L</bdi> هدف أوسع للأشخاص منخفضي الخطورة فقط، مو القيمة المثالية."},
"AS-0868": {
    "A": "ما فيه حاجة لفحص إضافي للتفريق بين مقدمات السكري والسكري؛ فيه فعلاً فحصان مختلفان بمدى السكري، والسكر العشوائي يكون تشخيصيًا بس مع أعراض وقيمة ≥١١.١."},
"AS-0868B": {
    "A": "<bdi>Sitagliptin</bdi> (مثبط <bdi>DPP-4</bdi>) دواء إضافي بالدرجة الثانية لو الميتفورمين ما كفى أو ما تحمّلته.",
    "C": "<bdi>Liraglutide</bdi> (منبه <bdi>GLP-1</bdi>) يساعد بالوزن ويُفضّل كإضافة مع مرض قلبي وعائي مؤكد أو بدانة تحتاج نزول وزن إضافي، لكنه مو الدواء الأول هنا.",
    "D": "<bdi>Glimepiride</bdi> (سلفونيل يوريا) يسبب نقص سكر وزيادة وزن، خيار سيء بمريضة بدينة؛ يُضاف لاحقًا."},
"AS-0869": {
    "A": "<bdi>metformin</bdi> يبدأ بعد تأكيد السكري (فحصان غير طبيعيان، أو سكر عشوائي عرضي ≥١١.١)؛ العلاج على فحص صائم واحد غير مؤكد سابق لأوانه."},
"AS-0875": {
    "A": "<bdi>Peutz-Jeghers</bdi> وراثي سائد كمان، لكنه يسبب سلائل هامارتومية بالأمعاء الدقيقة مع تصبغات بالشفة/الفم وغالبًا انغلاف معوي؛ ما فيه وصف تصبغات هنا.",
    "C": "<bdi>Ulcerative colitis</bdi> يعطي إسهال دموي مع إلحاح ومخاط؛ التجمع العائلي أضعف، وإصابة الأم والإخوة معًا توحي أكثر بمتلازمة سليلات سائدة.",
    "D": "<bdi>Crohn's disease</bdi> عادة إسهال غير دموي، ألم بالربع السفلي الأيمن أو كتلة، مرض شرجي وقرح فموية؛ التوريث العمودي بالأم والإخوة مو نمطه."},
"AS-0876": {
    "A": "الديال خطوة أخيرة لحالات فرط البوتاسيوم المقاوم للعلاج الدوائي أو مع قصور كلوي شديد؛ الكرياتينين هنا مرتفع بشكل طفيف فقط.",
    "B": "البيكربونات الوريدي مكمّل فقط عند حماض واضح؛ رغم <bdi>HCO3 15</bdi> هو أضعف وأبطأ من الإنسولين/الغلوكوز وما يُعتبر المعيار الأولي.",
    "D": "المحلول الملحي العادي ما يخفض البوتاسيوم بشكل مهم؛ يُستخدم لنقص السوائل، وهذا غير موجود هنا."},
"AS-0877": {
    "A": "الأسبرين بجرعة منخفضة ممكن يرفع حمض اليوريك قليلاً، لكن الثيازيد هو السبب الكلاسيكي والأرجح؛ الأسبرين يصير الجواب فقط لو ما فيه مدر بالقائمة.",
    "B": "<bdi>Metformin</bdi> ما يسبب فرط حمض يوريك أو نقرس؛ أعراضه الجانبية الأساسية اضطراب هضمي ونقص <bdi>B12</bdi> وحماض لبني.",
    "C": "<bdi>Lisinopril</bdi> (مثبط <bdi>ACE</bdi>) ليس سببًا للنقرس؛ أعراضه الجانبية الكلاسيكية سعال جاف ووذمة وعائية وفرط بوتاسيوم."},
"AS-0879": {
    "B": "<bdi>Thrombolysis</bdi> (التحليل الخثري) يُحجز للانصمام الرئوي غير المستقر («<bdi>massive</bdi>» أو هبوط ضغط)، وما فيه دليل على عدم استقرار بهذا السؤال."},
"AS-0880": {
    "A": "<bdi>Warfarin</bdi> للتمييع طويل المدى، يحتاج أيام ليعمل، وما يُستخدم أبدًا كعلاج أولي لانصمام رئوي حاد.",
    "C": "<bdi>LMWH</bdi> خط أول بانصمام مستقر؛ الانصمام «<bdi>massive</bdi>» غير مستقر ويحتاج تحليل خثري.",
    "D": "<bdi>Dabigatran</bdi> دواء فموي للاستقرار طويل المدى، مو لانصمام رئوي «<bdi>massive</bdi>»."},
"AS-0881": {
    "A": "جرعة الأسبرين منخفضة صحيحة، لكن الستاتين «المنخفض» غير كافٍ بعد احتشاء؛ لازم يكون عالي الجرعة.",
    "B": "حاصر البيتا مفيد خصوصًا بانخفاض كسر القذف، لكن الستاتين عالي الجرعة لازم يكون موجود مع الأسبرين كأساس الوقاية الثانوية الدوائية.",
    "D": "حاصرات قنوات الكالسيوم (<bdi>CCBs</bdi>) ما لها فائدة ثابتة على البقيا بعد احتشاء، وما تغني عن الأسبرين والستاتين."},
"AS-0882": {
    "A": "نمو عدة جراثيم مختلطة بزرع البول غالبًا يعني تلوث العينة أثناء الجمع؛ الخطوة الصحيحة إعادة عينة نظيفة، مو تشخيص عدوى."},
"AS-0887": {
    "A": "<bdi>HAV IgG</bdi> يدل على مناعة سابقة أو تطعيم (عدوى قديمة)، يبقى إيجابي مدى الحياة وما يقدر يثبت إن المرض الحالي من <bdi>HAV</bdi>.",
    "C": "<bdi>HBsAg</bdi> جزء من فحص التهاب كبد حاد شامل، لكن <bdi>HBV</bdi> حضانته أطول (أسابيع لأشهر) وأقل شيوعًا بهذا العرض؛ يكون الفحص الأول مع عوامل خطر زي جنس غير محمي أو تعاطي وريدي.",
    "D": "<bdi>HCV</bdi> نادرًا يسبب التهاب كبد حاد مصحوب يرقان، والأجسام المضادة ممكن تكون سلبية مبكرًا؛ يُفحص مع عوامل خطر دموية أو مرض كبد مزمن."},
"AS-0890": {
    "B": "حرارة الجسم المرتفعة التحمل (<bdi>heat intolerance</bdi>) توجه لفرط الدرقية؛ التضخم بالأصابع (<bdi>acropachy</bdi>) ممكن يصير لكن بدون تنقر أظافر مع أصابع سجقية."},
"AS-0894": {
    "A": "السونار يُطلب تقريبًا لكل عقدة ويترافق مع <bdi>TSH</bdi>، لكن الخوارزمية تتفرع من <bdi>TSH</bdi> أولاً؛ يكون السونار الجواب لو كان <bdi>TSH</bdi> معروف مسبقًا بأنه طبيعي.",
    "B": "<bdi>FNA</bdi> خطوة تشخيصية لعقدة استوفت معايير السونار (حجم وملامح مشبوهة) مع <bdi>TSH</bdi> طبيعي أو مرتفع؛ مبكرة هنا قبل معرفة <bdi>TSH</bdi>، والعقد الحارة نادرًا تحتاجها.",
    "C": "الخزعة بالإبرة الغليظة مو الفحص النسيجي الأول القياسي للعقد الدرقية؛ تُحجز لحالات خاصة مثل خزعة <bdi>FNA</bdi> غير حاسمة."},
"AS-0907": {
    "B": "التحويل للطبيب النفسي يفترض إن الأعراض من الاكتئاب ويفوّت سبب درقي دوائي قابل للعكس؛ يُنظر فيه فقط بعد التأكد من وظائف الدرقية.",
    "C": "<bdi>Propranolol</bdi> يعالج الأعراض الودية لكنه ما يعالج السبب، وما يُعتبر الخطوة الأولى؛ يُضاف بعد تأكيد فرط الدرقية."},
"AS-0911": {
    "B": "<bdi>Phenytoin</bdi> يُستخدم للنوبات البؤرية والتشنجية الكبرى وحالة الصرع المستمر؛ عديم الفعالية بنوبات الغياب وممكن يسوّئها."},
"AS-0914": {
    "B": "<bdi>Low-dose ICS</bdi> لوحده مناسب لربو خفيف مستمر (أعراض أكثر من مرتين أسبوعيًا بس مو يومية)؛ الأعراض اليومية تحتاج خطوة <bdi>ICS + LABA</bdi>.",
    "C": "مضاد <bdi>leukotriene</bdi> دواء بديل أو إضافي (مفيد مع التهاب أنف تحسسي أو ربو حساس للأسبرين)، مو العلاج المفضل بهذي الدرجة.",
    "D": "<bdi>Theophylline</bdi> إضافة أقل تفضيلًا بسبب نافذته العلاجية الضيقة وتفاعلاته وسميته."},
"AS-0915": {
    "A": "<bdi>Mitral regurgitation</bdi> نفخة انقباضية شاملة بقمة القلب تنتشر للإبط، مو نفخة انبساطية بقاعدة القلب.",
    "B": "<bdi>Aortic regurgitation</bdi> نفخة انبساطية مبكرة بقاعدة القلب بس جانبها أيسر، فتضعف مع الشهيق وتقوى بالزفير وهو مائل للأمام.",
    "C": "<bdi>Tricuspid regurgitation</bdi> تقوى بالشهيق صحيح، لكنها نفخة انقباضية شاملة بحافة القص السفلى اليسرى، مو انبساطية بقاعدة القلب."},
"AS-0915B": {
    "A": "<bdi>Mitral stenosis</bdi> نفخة انبساطية متوسطة منخفضة النبرة بقمة القلب بالوضع الجانبي الأيسر مع انبساطة فتح؛ تسبب تضخم أذين أيسر مو <bdi>LVH</bdi>.",
    "B": "<bdi>Mitral regurgitation</bdi> نفخة انقباضية شاملة بقمة القلب تنتشر للإبط.",
    "C": "<bdi>Aortic stenosis</bdi> يسبب <bdi>LVH</bdi> كمان، لكن نفختها انقباضية قذفية بالمنطقة الأبهرية تنتشر للشرايين السباتية."},
"AS-0925": {
    "A": "<bdi>Pseudogout</bdi> يصيب عادة مفصل كبير مثل الركبة بمريض مسن (مع هشاشة عظام أو فرط جارات درقية)؛ ما يربط بـ<bdi>psoriasis</bdi> ولا يفسر النمط برجل ٤٠ سنة.",
    "B": "<bdi>Active gout arthritis</bdi> ممكن ينتشر للكاحل والركبتين، لكن استمرار الالتهاب رغم <bdi>allopurinol</bdi> بانتظام برجل معروف بـ<bdi>psoriasis</bdi> طويل الأمد يرجّح تشخيص ثاني؛ يصح لو ما فيه <bdi>psoriasis</bdi> ويوجد حمض يوريك مرتفع يفسر النوبات.",
    "D": "<bdi>Osteoarthritis</bdi> مرض تنكسي غير التهابي بكبار السن؛ ما يسبب التهاب مفصل فعّال برجل ٤٠ سنة؛ يصح مع ألم آلي يزيد بالاستخدام وتضيّق مسافة مفصلية."},
"AS-0926": {
    "B": "<bdi>TAVR</bdi> (استبدال، مو تصليح) يُستخدم بتضيّق شديد عرضي أو ضعف وظيفة البطين، خصوصًا بالمسنين أو عالي الخطورة الجراحية؛ ما هو الخيار الافتراضي بمريض بدون أعراض وكسر قذف طبيعي.",
    "C": "استبدال الصمام الجراحي (الميكانيكي) يُختار بحالات عرضية أو ضعف وظيفة البطين، غالبًا بمرضى أصغر يقدرون يستمرون على التمييع مدى الحياة؛ مبكر هنا."},
"AS-0928": {
    "A": "<bdi>Metformin</bdi> أعراضه الجانبية الأساسية اضطراب هضمي ونقص <bdi>B12</bdi> ونادرًا حماض لبني، مو تشنج عضلي.",
    "B": "<bdi>Lisinopril</bdi> يسبب سعال جاف ووذمة وعائية وفرط بوتاسيوم وقصور كلوي، مو ألم عضلي.",
    "D": "<bdi>Fibrate</bdi> يُستخدم أساسًا لارتفاع الدهون الثلاثية؛ لارتفاع الكوليسترول بمريض سكري وضغط الستاتين هو الخط الأول، وسمية العضل بالفايبريت غالبًا تحصل عند دمجه مع ستاتين (خصوصًا <bdi>gemfibrozil</bdi>)."},
"AS-0928B": {
    "A": "حاصر البيتا يخفف تحفيز بيتا-٢ لدخول البوتاسيوم للخلايا، فميله يرفع البوتاسيوم قليلاً، مو ينقصه.",
    "B": "<bdi>Salbutamol</bdi> ينقص البوتاسيوم بإدخاله للخلايا، لكن تأثيره عابر ومرتبط بالجرعة؛ يصير الجواب بسياق حاد (استنشاق متكرر)، مو نظام ثابت خارجي.",
    "D": "مثبطات <bdi>ACE</bdi> تقلل الألدوستيرون وتسبب فرط بوتاسيوم، مو نقصه."},
"AS-0931": {
    "A": "<bdi>Vancomycin</bdi> (والباقي بالخيارات) مضادات جراثيم أو فيروسات بدون أي فعالية ضد الملاريا؛ الفانكومايسين مناسب لـ<bdi>MRSA</bdi> أو عدوى <bdi>C. difficile</bdi> الفموية."},
"AS-0940": {
    "A": "<bdi>Primary angioplasty</bdi> استراتيجية إعادة الترويه الطارئة لـ<bdi>STEMI</bdi>؛ بـ<bdi>NSTEMI</bdi> القسطرة خطوة باكرة توقيتها حسب الخطورة، مو العلاج الأول اللي يُبدأ.",
    "C": "التحليل الخثري ما له فائدة ويرفع خطر النزيف بـ<bdi>NSTEMI</bdi> أو الذبحة غير المستقرة؛ يُستخدم فقط بـ<bdi>STEMI</bdi> لو القسطرة الأولية غير متاحة بالوقت المناسب."},
"AS-0941": {
    "A": "الصدمة النزفية تحتاج مصدر نزيف واضح (رضح، نزيف هضمي، تمدد أوعية ممزق) وما ترفع <bdi>BNP</bdi> أو التروبونين بمرض بطين أيسر؛ المشكلة هناك نقص حجم مو فشل ضخ.",
    "B": "الصدمة العصبية تتبع إصابة النخاع الشوكي وتعطي هبوط ضغط مع بطء نبض وجلد دافئ؛ هذا المريض متسرع القلب بدون محفز عصبي.",
    "C": "الصدمة الانسدادية (دكاك تاموري، انصمام رئوي ضخم، استرواح مضغوط) يُظهر الصدى انصباب أو بطين أيمن متوسع ومجهد، مو تضخم بطين أيسر، وما فيه محفز مفاجئ هنا."},
"AS-0944": {
    "B": "النوبة الرمعية (<bdi>clonic</bdi>) حركة رعشية إيقاعية متكررة تستمر لفترة أطول، غالبًا مع تغيّر بالوعي؛ تصح لو وصف السؤال رعشة إيقاعية مستمرة مو نفضة قصيرة مفردة."},
"AS-0945": {
    "A": "التصوير الطبقي عالي الدقة للرئة يُستخدم لاشتباه مرض رئوي خلالي أو توسع قصبات؛ ما يشخّص ربو مهني، وتصوير الصدر هنا طبيعي أصلاً.",
    "B": "بدء الستيرويد الاستنشاقي اليومي قبل تأكيد التشخيص سابق لأوانه؛ العلاج يجي بعد التأكيد الموضوعي.",
    "C": "النصح بتغيير العمل خطوة كبيرة تحتاج تشخيص مؤكد أولاً؛ تصير الجواب الصحيح بمجرد تأكيد الربط بالعمل."},
"AS-0946": {
    "A": "المسح العظمي غير نوعي وبطيء؛ ما يفرّق بين العدوى والالتهاب ويؤخر بزل مفصل يُحتمل إنتانه.",
    "C": "الأشعة السينية العادية ممكن تُعمل كخط أساس، لكنها غالبًا طبيعية بالمراحل المبكرة من التهاب المفصل الإنتاني وما تستبعد العدوى.",
    "D": "الرنين المغناطيسي مفيد لالتهاب العظم والنقي أو إصابة داخلية بالمفصل، لكنه ما يعوّض تحليل سائل المفصل بالتهاب مفصل حاد مفرد."},
"AS-0947": {
    "A": "خزعة الكبد إجراء باضع غير ضروري؛ يُنظر فيه لالتهاب كبد حبيبي غير واضح السبب، مو لما يقدر فحص مصلي بسيط يأكد التشخيص.",
    "B": "خزعة/زرع نخاع العظم حساسيته أعلى من زرع الدم للبروسيلا، لكنه باضع ويُحجز لما يكون الفحص المصلي غير حاسم؛ مو الخطوة الأولى.",
    "C": "إعادة زرع الدم غالبًا سلبية بالبروسيلا المزمنة (جرثومة بطيئة النمو) وتؤخر التشخيص؛ الفحص المصلي هو الأنسب هنا."},
}

HIGHLIGHT_TERMS = {
"AS-0776": ["bone marrow transplant", "ceftazidime", "did not improve after 72 hours", "no pneumonia or hypotension"],
"AS-0776B": ["acute leukemia", "allogenic bone marrow transplantation", "invasive aspergillosis"],
"AS-0777": ["bone marrow transplantation", "febrile neutropenia", "[NO] Pneumonia", "Ceftazidime"],
"AS-0780": ["Ascitis", "sparonolactone with no improvment"],
"AS-0781": ["liver cirrhosis", "increasing ascites", "spironolactone 50 mg/day and furosemide 40 mg/day", "large ascites"],
"AS-0782": ["Watary diarrhea"],
"AS-0785": ["helicobacter-associated duodenal ulcer", "non-tarry black"],
"AS-0788": ["celiac disease"],
"AS-0791": ["rheumatic heart disease", "prosthetic valve replacement", "dental operation"],
"AS-0793": ["post angioplasty after MI 3 monthes ago", "cholesterol was 5.3"],
"AS-0795": ["veterinarian", "right sacro-iliac pain and fever for 2 monthes"],
"AS-0796": ["failed to reach target blood pressure", "on amlodipine and losartan"],
"AS-0848": ["weakness", "image show Afib"],
"AS-0850": ["SOB and fatigue", "stable", "bradycardia"],
"AS-0853": ["Incidentally Found To Have Atrial Fibrillation", "HR: 110 bpm", "BP: 110/70 mmHg"],
"AS-0854": ["LDL-cholesterol", "Optimal range"],
"AS-0868": ["family hx of diabetes", "thirst and polyuria", "Fasting glucose 8 to 10 mmol", "Hb a1c above 7 , 7.8 %"],
"AS-0868B": ["BMI 31", "HbA1C 7.8", "first line anti-diabetic"],
"AS-0869": ["strong family history of diabetes", "occasionally thirst", "fasting blood glucose (FBG ) is 7.5 mmol/L", "No Mention Of A1c"],
"AS-0875": ["25-year-old", "bloody stools", "mother and siblings"],
"AS-0876": ["lethargy", "ECG shows no acute changes", "Potassium 6.6", "Bicarbonate 15"],
"AS-0877": ["severe pain, redness, and swelling of the first metatarsophalangeal (MTP) joint"],
"AS-0879": ["pulmonary embolism", "no vital report"],
"AS-0880": ["massive pulmonary embolism"],
"AS-0881": ["stemi", "long term"],
"AS-0882": ["significant or diagnostic for uti"],
"AS-0887": ["yellowish discolouration", "Alanine aminotransferase 990", "Aspartate aminotransferase 789"],
"AS-0890": ["Sausage digits", "nail pitting"],
"AS-0894": ["asymptomatic", "thyroid nodule 2x2 cm"],
"AS-0907": ["insomnia , irritability and palpitation", "amiodarone"],
"AS-0911": ["sudden movement stop without falling for 15 seconds", "EEG : 3 Hz spike"],
"AS-0914": ["daily wheezing", "moderate persistent asthma"],
"AS-0915": ["early diastolic murmur", "increase during INSPIRATION"],
"AS-0915B": ["early diastolic murmur", "increased by leaning forward", "left ventricular hypertrophy"],
"AS-0925": ["known case of psoriasis", "no improvement"],
"AS-0926": ["asymptomatic", "Severe bicuspid aortic stenosis", "Normal left ventricular ejection fraction"],
"AS-0928": ["high cholesterol level", "cramps in muscle"],
"AS-0928B": ["low potassium"],
"AS-0931": ["went to africa", "intermittent fever"],
"AS-0940": ["st depression", "elevated troponin"],
"AS-0941": ["hypotension, tachycardia", "LV hyper atrophy", "500 bnb"],
"AS-0944": ["jerky movement"],
"AS-0945": ["car repair shop", "symptoms are associated with his workdays", "spirometry results are normal"],
"AS-0946": ["rheumatoid arthritis", "pain and swelling of the left knee and low-grade fever", "prednisone, methotrexate, and etanercept"],
"AS-0947": ["lower back pain", "history of unpasteurized milk ingestion", "Blood culture: Negative"],
}

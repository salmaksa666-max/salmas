# -*- coding: utf-8 -*-
"""Surgery and OB/GYN systems -> topics for build_dense_merged.py (SPEC=surgery / SPEC=obgyn).
Same shape as the Medicine SYS list: (system, system regex, [(topic, regex), ..., (last topic, ".")])."""

SURGERY = [
 ("Trauma & ATLS", r"trauma|mva|motor vehicle|accident|rta\b|fall from|stab|gunshot|atls|airway|intubat|gcs|cricothyr|tension pneumothorax|hemothorax|chest tube|flail|tamponade|fast\b|pelvic (binder|fracture)|hemorrhagic shock|blunt|penetrating|head injury|epidural|subdural|spleen|splenic|liver laceration|c-?spine|collar|primary survey", [
   ("Airway / breathing / chest", r"airway|intubat|cricothyr|tension|pneumothorax|hemothorax|chest tube|flail|tamponade|needle|thoracostomy|rib"),
   ("Shock / abdomen / pelvis", r"shock|fast\b|spleen|splenic|liver|laparotomy|pelvic|pelvis|binder|blunt abdominal|penetrating|fluid|transfus|hypotens"),
   ("Head & spine injury", r"head|gcs|epidural|subdural|skull|brain|c-?spine|collar|spinal|hyperventilat|mannitol"),
   ("Other trauma", r".")]),
 ("Burns, wounds & soft tissue", r"burn|scald|inhalation injury|parkland|escharotomy|wound|lacerat|suture|abscess|cellulitis|necrotizing|fournier|gangrene|gas gangrene|perfringens|tetanus|bite|pressure (ulcer|injury|sore)|lipoma|sebaceous|epidermoid|cyst|keloid|skin lesion|melanoma|basal cell|squamous cell|pilonidal|ingrown|nail|lidocaine|local anesthe", [
   ("Burns", r"burn|scald|inhalation|parkland|escharotomy|carbon"),
   ("Wounds / infections / ulcers", r"wound|lacerat|suture|abscess|cellulitis|necrotizing|fournier|gangrene|perfringens|tetanus|bite|pressure|ulcer|pilonidal|ingrown|nail|lidocaine|anesthe"),
   ("Skin lumps / skin cancer", r"lipoma|sebaceous|epidermoid|cyst|keloid|lesion|melanoma|basal|squamous|mole|nevus"),
   ("Other skin", r".")]),
 ("Breast", r"breast|mammo|nipple|fibroadenoma|mastitis|gynecomastia|brca|axilla|lumpectomy|mastectomy|tru-?cut|core biopsy", [
   ("Breast lumps & imaging", r"lump|mass|mammo|ultrasound|fibroadenoma|cyst|tru-?cut|core|fna|biopsy|birads|bi-rads"),
   ("Breast cancer & screening", r"cancer|carcinoma|brca|screen|mastectomy|lumpectomy|axilla|sentinel|tamoxifen|her2|dcis|lcis|atypia"),
   ("Nipple / infection / other", r"."),
   ]),
 ("Thyroid, parathyroid & neck", r"thyroid|parathyroid|goit|neck (mass|swelling|lump)|thyroglossal|branchial|cervical lymph|lymph node|parotid|salivary|submandibular|hypocalc|chvostek|trousseau|recurrent laryngeal|hoarse", [
   ("Thyroid nodule / goitre / cancer", r"nodule|goit|cancer|carcinoma|papillary|follicular|medullary|fna|thyroidectomy|graves|toxic"),
   ("Post-thyroidectomy complications", r"post|hypocalc|chvostek|trousseau|recurrent laryngeal|hoarse|hematoma|stridor|after (the )?surgery"),
   ("Neck lumps / salivary / parathyroid", r"."),
   ]),
 ("Upper GI, hepatobiliary & pancreas", r"epigastr|peptic|perforat|ulcer|erect|free air|gastric|stomach|duoden|esophag|achalasia|dysphagia|hematemesis|upper gi bleed|gallbladder|gallstone|biliary|cholecyst|cholangit|cholelith|choledoch|murphy|jaundice|ercp|mrcp|pancrea|pseudocyst|amylase|lipase|liver (abscess|mass|cyst)|hydatid|bariatric|obes", [
   ("Gallbladder / biliary", r"gallbladder|gallstone|biliary|cholecyst|cholangit|cholelith|choledoch|murphy|ercp|mrcp|jaundice|fatty meal"),
   ("Pancreas", r"pancrea|pseudocyst|amylase|lipase|whipple"),
   ("Stomach / esophagus / perforation", r"epigastr|peptic|perforat|ulcer|erect|free air|gastric|stomach|duoden|esophag|achalasia|dysphagia|hematemesis|nsaid"),
   ("Liver / bariatric / other", r"."),
   ]),
 ("Appendix, bowel & acute abdomen", r"appendic|right (lower|iliac)|rlq|mcburney|obstruction|distension|volvulus|sigmoid|adhesion|ileus|mesenteric|ischemi|atrial fibrillation|af\b|diverticul|colon|colorectal|polyp|bowel|small intestine|acute abdomen|abdominal pain|laparotomy|laparoscop|stoma|ileostomy|colostomy|anastomo", [
   ("Appendicitis", r"appendic|right (lower|iliac)|rlq|mcburney|alvarado"),
   ("Bowel obstruction / volvulus / ischemia", r"obstruction|distension|volvulus|sigmoid|adhesion|ileus|mesenteric|ischemi|atrial fibrillation|af\b|nasogastric|ngt|npo"),
   ("Colon (diverticulitis / polyps / cancer)", r"diverticul|colon|colorectal|polyp|cancer|carcinoma|colonoscopy|cea|stoma|colostomy"),
   ("Other abdomen", r".")]),
 ("Anorectal & hernia", r"hernia|inguinal|femoral|umbilical|incisional|groin|bulge|mesh|hemorrhoid|fissure|fistula|perianal|\banal\b|pilonidal|rectal prolapse|pruritus ani|dre\b|digital rectal", [
   ("Hernia", r"hernia|inguinal|femoral|umbilical|incisional|groin|bulge|mesh|strangulat|incarcerat"),
   ("Anorectal (hemorrhoids / fissure / fistula / abscess)", r"."),
   ]),
 ("Vascular", r"claudication|abi\b|ankle[- ]brachial|peripheral arter|popliteal|femoral artery|limb ischemia|embol|aneurysm|aaa\b|aorta|aortic|varicose|venous|dvt|ulcer.*(leg|venous)|carotid|endarterectomy|gangrene|pulseless|amputat|diabetic foot", [
   ("Arterial (claudication / acute limb ischemia)", r"claudication|abi\b|ankle|peripheral|popliteal|femoral|limb ischemia|embol|pulseless|amputat|gangrene|bypass|stent"),
   ("Aneurysm / carotid", r"aneurysm|aaa\b|aort|carotid|endarterectomy"),
   ("Venous / diabetic foot / other", r"."),
   ]),
 ("Urology", r"kidney stone|renal colic|ureter|stone|calculi|hydronephrosis|hematuria|bladder|prostat|bph|psa|urinary retention|catheter|testi(s|cle|cular|es)\b|scrot|torsion|varicocele|hydrocele|epididym|undescended|cryptorch|penile|priapism|phimosis|circumcis|urethr|renal (mass|cell)|wilms", [
   ("Stones / renal colic", r"stone|calculi|renal colic|colic|ureter|hydronephrosis|kub|flank"),
   ("Scrotum / testis", r"testi(s|cle|cular|es)\b|scrot|torsion|varicocele|hydrocele|epididym|undescended|cryptorch"),
   ("Prostate / bladder / retention / cancer", r"."),
   ]),
 ("Orthopedics", r"fracture|dislocat|sprain|ligament|acl\b|menisc|knee|\bhip|shoulder|elbow|wrist|ankle|scaphoid|colles|smith|tibia|femur|humerus|radius|ulna|clavicle|cast|splint|compartment syndrome|osteomyel|septic arthritis|back pain|\bdisc\b|sciatica|cauda equina|spine|carpal tunnel|trigger finger|de quervain|ganglion|osteosarcoma|bone tumou?r|gout", [
   ("Fractures & dislocations", r"fracture|dislocat|scaphoid|colles|smith|tibia|femur|humerus|radius|ulna|clavicle|cast|splint|compartment"),
   ("Back / spine", r"back pain|\bdisc\b|sciatica|cauda equina|spine|spinal|lumbar|cervical"),
   ("Joints / sports / hand", r"sprain|ligament|acl\b|menisc|knee|shoulder|rotator|elbow|wrist|carpal tunnel|trigger finger|de quervain|ganglion"),
   ("Bone infection / tumours / other", r".")]),
 ("Perioperative, anesthesia & post-op", r"pre-?op|post-?op|postoperative|after (the |an )?(operation|surgery)|day \d|surgical site|wound infection|anesthe|anaesthe|malignant hyperthermia|suxamethonium|succinylcholine|asa\b|fasting|npo before|consent|fever after|atelectasis|anastomotic leak|dvt prophylaxis|warfarin.*surgery|stop (aspirin|clopidogrel)|blood transfusion|catheter|urine output|oliguria|fluid", [
   ("Post-op fever & complications", r"post|after|day \d|fever|atelectasis|leak|wound|surgical site|oliguria|urine output|catheter|confus|delirium"),
   ("Pre-op & anesthesia", r"pre-?op|anesthe|anaesthe|malignant hyperthermia|suxamethonium|succinylcholine|asa\b|fasting|consent|warfarin|aspirin|clopidogrel|stop|lidocaine"),
   ("Other perioperative", r".")]),
 ("ENT, eye & neurosurgery", r"\bent\b|\bears?\b|otitis|tonsil|epistaxis|nasal|sinus|larynx|hoarseness|hearing|vertigo|eye|vision|visual|glaucoma|cataract|retina|cornea|conjunctiv|orbital|squint|brain tumou?r|hydroceph|subarachnoid|aneurysm.*brain|craniotomy", [
   ("ENT", r"\bent\b|\bears?\b|otitis|tonsil|epistaxis|nasal|nose|sinus|larynx|hoarse|hearing|vertigo|throat"),
   ("Eye", r"eye|vision|visual|glaucoma|cataract|retina|cornea|conjunctiv|orbital|squint"),
   ("Neurosurgery / other", r".")]),
]
SURGERY_ORDER = ["Trauma & ATLS", "Burns, wounds & soft tissue", "Breast", "Thyroid, parathyroid & neck", "Upper GI, hepatobiliary & pancreas",
                 "Appendix, bowel & acute abdomen", "Anorectal & hernia", "Vascular", "Urology", "Orthopedics",
                 "Perioperative, anesthesia & post-op", "ENT, eye & neurosurgery"]

OBGYN = [
 ("Antenatal care & screening", r"antenatal|prenatal|booking|first (visit|trimester)|gestational age|dating|lmp|naegele|folic|supplement|vaccin|screening|down syndrome|nuchal|amniocent|cvs\b|anomaly scan|\brh\b|anti-?d|rhesus|isoimmun|ultrasound.*(weeks|pregnan)|teratogen|contraindicated in pregnancy|safe in pregnancy|drug.*pregnan|pregnan.*drug|isotretinoin|vegetarian|bacteriuria|nausea|vomiting|hyperemesis|weight gain", [
   ("Booking / dating / supplements / vaccines", r"booking|first (visit|trimester)|dating|lmp|naegele|gestational age|folic|iron|supplement|vaccin|weight gain"),
   ("Prenatal screening / Rh", r"screening|down|nuchal|amniocent|cvs\b|anomaly|\brh\b|anti-?d|rhesus|isoimmun|kleihauer|coombs"),
   ("Drugs / hyperemesis / other antenatal", r".")]),
 ("Early pregnancy & bleeding", r"miscarriage|abortion|threatened|inevitable|incomplete|missed|ectopic|tubal|methotrexate|beta[- ]?hcg|\bhcg\b|molar|hydatidiform|gestational trophoblastic|placenta previa|previa|abruption|abruptio|antepartum hemorrhage|vaginal bleeding.*(pregnan|weeks)|vasa previa|cervical insufficiency|cerclage|recurrent (pregnancy )?loss", [
   ("Miscarriage", r"miscarriage|abortion|threatened|inevitable|incomplete|missed|os (closed|open)|recurrent|cerclage|cervical insufficiency"),
   ("Ectopic / molar", r"ectopic|tubal|methotrexate|hcg|molar|hydatidiform|trophoblastic"),
   ("Antepartum hemorrhage (previa / abruption)", r".")]),
 ("Medical problems in pregnancy", r"preeclampsia|pre-eclampsia|eclampsia|hellp|gestational hypertension|blood pressure|1[4-9]0/\d+|mcv|hypothyroid|thyroxin|mitral|cardiac|pleuritic|supine hypotension|labetalol|hydralazine|nifedipine|magnesium|gestational diabetes|\bgdm\b|ogtt|glucose|insulin|metformin|diabet|thyroid|anemia|epilep|seizure|heart disease|asthma|dvt|thrombo|heparin|uti|pyelonephritis|bacteriuria|cholestasis|itching|fatty liver|lupus|sle|hiv|hepatitis|syphilis|toxoplasm|cmv|rubella|varicella|gbs|group b strep", [
   ("Hypertension / preeclampsia", r"1[4-9]0/\d+|headache|blurred|preeclampsia|pre-eclampsia|eclampsia|hellp|hypertension|blood pressure|labetalol|hydralazine|nifedipine|magnesium|proteinuria"),
   ("Diabetes in pregnancy", r"gestational diabetes|\bgdm\b|ogtt|glucose|insulin|metformin|diabet|macrosomia"),
   ("Infections in pregnancy", r"uti|pyelonephritis|bacteriuria|hiv|hepatitis|syphilis|toxoplasm|cmv|rubella|varicella|gbs|group b|chorioamnion|fever"),
   ("Other medical (thyroid / anemia / VTE / cholestasis)", r".")]),
 ("Labor & delivery", r"labou?r|contraction|cervical dilat|dilatation|effacement|\bstation|partogram|bishop|induction|oxytocin|misoprostol|ripening|rupture of membranes|\bprom\b|pprom|preterm labou?r|tocoly|steroids? (for|to) (fetal|lung)|betamethasone|dexamethasone|ctg|fetal heart|deceleration|variability|fetal distress|breech|presentation|malpresentation|transverse|occiput posterior|shoulder dystocia|cord prolapse|cesarean|caesarean|c-?section|vbac|instrumental|vacuum|forceps|episiotomy|perineal tear|twin|multiple pregnancy|post-?term|post-?dates|iugr|fgr|growth restriction|oligohydramnios|polyhydramnios|stillbirth|iufd|fetal death|reduced fetal movement", [
   ("Labor progress / induction", r"labou?r|contraction|dilat|effacement|\bstation|partogram|bishop|induction|oxytocin|misoprostol|ripening|arrest|prolonged|post-?term|post-?dates|epidural"),
   ("PROM / preterm labor", r"rupture of membranes|\bprom\b|pprom|preterm|tocoly|betamethasone|dexamethasone|steroid|nifedipine|magnesium"),
   ("CTG / fetal wellbeing / growth", r"ctg|fetal heart|deceleration|variability|distress|iugr|fgr|growth restriction|oligohydramnios|polyhydramnios|stillbirth|iufd|fetal death|fetal movement|biophysical|doppler"),
   ("Malpresentation / emergencies / operative delivery", r".")]),
 ("Postpartum", r"postpartum|post-?partum|after (delivery|birth)|puerper|pph\b|uterine atony|retained placenta|placenta accreta|lochia|breast ?feed|lactation|mastitis|engorgement|endometritis|postnatal depression|postpartum depression|blues|psychosis|sheehan", [
   ("PPH", r"pph\b|hemorrhage|bleeding|atony|retained|accreta|oxytocin|carboprost|misoprostol|tranexamic"),
   ("Postpartum infection / breast / mood / other", r".")]),
 ("Menstrual disorders & amenorrhea", r"amenorrh|menstrua|menses|period|menorrhagia|heavy (menstrual )?bleeding|aub\b|abnormal uterine bleeding|dysmenorrh|premenstrual|pms|pmdd|oligomenorrh|polycystic|pcos|hirsutism|prolactin|turner|mullerian|imperforate|puberty|menarche|fibroid|leiomyoma|adenomyosis|endometrial (hyperplasia|polyp|thickness)|polyp", [
   ("Amenorrhea / PCOS / hirsutism", r"amenorrh|oligomenorrh|polycystic|pcos|hirsutism|prolactin|turner|mullerian|imperforate|puberty|menarche|androgen"),
   ("AUB / fibroids / adenomyosis", r"menorrhagia|heavy|aub\b|abnormal uterine|fibroid|leiomyoma|adenomyosis|polyp|hyperplasia|bleeding"),
   ("Dysmenorrhea / PMS / other", r".")]),
 ("Infertility, contraception & menopause", r"infertil|subfertil|conceive|semen|ovulat|clomiphene|letrozole|ivf|hsg|tubal patency|contracept|ocp|combined pill|progestin|iud|copper|implant|depot|emergency contracep|morning after|sterilization|menopaus|hot flush|hot flash|hrt|hormone replacement|osteopor|vaginal atrophy|postmenopausal", [
   ("Infertility", r"infertil|subfertil|conceive|semen|ovulat|clomiphene|letrozole|ivf|hsg|tubal patency"),
   ("Contraception", r"contracept|ocp|pill|progestin|iud|copper|implant|depot|emergency|morning after|sterilization"),
   ("Menopause / HRT", r".")]),
 ("Gyn infections & pelvic pain", r"discharge|vaginitis|vaginosis|clue cells|whiff|candid|trichomon|metronidazole|fluconazole|\bpid\b|pelvic inflammatory|chlamydia|gonorr|cervicitis|std|sti\b|herpes|genital ulcer|wart|hpv|bartholin|toxic shock|endometriosis|chronic pelvic pain|dyspareunia|ovarian torsion|torsion|ovarian cyst|cyst rupture", [
   ("Vaginal discharge / STIs / PID", r"discharge|vaginitis|vaginosis|clue|whiff|candid|trichomon|metronidazole|fluconazole|\bpid\b|pelvic inflammatory|chlamydia|gonorr|cervicitis|std|sti\b|herpes|ulcer|wart|bartholin|toxic shock"),
   ("Endometriosis / pelvic pain / ovarian cysts", r".")]),
 ("Gyn oncology & screening", r"cancer|carcinoma|malignan|tumou?r|pap|smear|cytology|colposcopy|\bcin\b|hpv|cervical screening|ascus|lsil|hsil|ovarian mass|adnexal mass|ca-?125|dermoid|teratoma|endometrial cancer|postmenopausal bleeding|vulvar|lichen sclerosus|choriocarcinoma", [
   ("Cervical screening / cervical cancer", r"\bpap\b|smear|cytology|colposcopy|\bcin\b|hpv|cervical|ascus|lsil|hsil|leep|cone"),
   ("Ovarian / adnexal masses", r"ovar|adnexal|ca-?125|dermoid|teratoma|cyst"),
   ("Endometrial / vulvar / other", r".")]),
 ("Urogynecology & other gyn", r"incontinence|stress urinary|urge|overactive bladder|prolapse|cystocele|rectocele|pessary|vesicovaginal|fistula|pelvic floor|kegel|ethic|consent|confidential|sexual assault|rape|domestic", [
   ("Incontinence / prolapse", r"incontinence|stress|urge|overactive|prolapse|cystocele|rectocele|pessary|pelvic floor|kegel|fistula"),
   ("Ethics / other gyn", r".")]),
]
OBGYN_ORDER = ["Antenatal care & screening", "Early pregnancy & bleeding", "Medical problems in pregnancy", "Labor & delivery", "Postpartum",
               "Menstrual disorders & amenorrhea", "Infertility, contraception & menopause", "Gyn infections & pelvic pain",
               "Gyn oncology & screening", "Urogynecology & other gyn"]

"""Group every OB/GYN question into a diagnosis-based cluster (no 'Other' bucket).
usage: group_obgyn.py out_items.json out_expl.json items1.json:expl1.json:Tag items2.json:expl2.json:Tag
Writes items carrying sys / topic (= cluster title) / howto, ordered system -> cluster -> nearest-neighbour chain."""
import json, re, sys
from collections import Counter
import numpy as np

# (system, cluster, how to solve, regex)  -- evaluated on answer / last sentence / options / stem
G = [
 ("Early pregnancy & bleeding", "Abortion types (threatened / inevitable / incomplete / missed / septic)",
  "Closed os + viable fetus = THREATENED → reassure. Open os = INEVITABLE → evacuate. Some tissue passed + open os = INCOMPLETE → misoprostol / D&C. Dead fetus + closed os = MISSED → misoprostol / D&C. Fever + foul discharge = SEPTIC → IV antibiotics then evacuate.",
  r"abortion|miscarr|products of conception|retained products|passed (some )?tissue|blood and tissue|missed|threatened|inevitable|incomplete|os (is )?(open|closed|dilated)|no fetal (heart|pole)|empty sac|anembry"),
 ("Early pregnancy & bleeding", "Recurrent miscarriage & cervical insufficiency",
  "≥3 losses → antiphospholipid screen (aspirin + heparin), karyotype, uterine anomaly. Painless 2nd-trimester dilatation = cervical insufficiency → cerclage (McDonald).",
  r"recurrent|antiphospholipid|lupus anticoag|cerclage|insufficien|incompeten|habitual|three (consecutive )?(miscarr|abort|loss)"),
 ("Early pregnancy & bleeding", "Ectopic pregnancy",
  "Positive hCG + no IUP + pain/bleeding. Unstable / ruptured → surgery. Stable, hCG <5000, no cardiac activity, unruptured → methotrexate (check LFT/CBC/renal). Rh-negative → anti-D.",
  r"ectopic|methotrexate|salping|tubal|adnexal mass|culdocent|fallopian|free fluid in (pouch|douglas)|empty uterus"),
 ("Early pregnancy & bleeding", "Molar pregnancy / GTN",
  "Snowstorm US + very high hCG + hyperemesis/early preeclampsia = complete mole → suction evacuation, then weekly hCG until negative. Plateau/rise of hCG = GTN → methotrexate/actinomycin.",
  r"mole\b|molar|hydatid|gtn|choriocarcin|trophoblast|theca.?lutein|snow.?storm|grape"),
 ("Early pregnancy & bleeding", "Early pregnancy: hCG / ultrasound landmarks / hyperemesis",
  "Gestational sac ≈ 5 wk (hCG ~1500–2000 on TVUS), yolk sac 5.5 wk, cardiac activity 6 wk. hCG doubles q48h. Hyperemesis: IV fluids, thiamine, pyridoxine ± doxylamine, then ondansetron/metoclopramide.",
  r"bhcg|b-hcg|beta.?hcg|hcg|discriminatory|gestational sac|yolk sac|hyperemesis|ketone|vomiting in pregnancy|morning sickness"),
 ("Early pregnancy & bleeding", "Placenta previa",
  "Painless bright-red bleeding in 3rd trimester → US (never digital exam). Stable <37 wk → admit, steroids, expectant. Major previa → elective CS at 36–37 wk. Unstable / heavy → emergency CS.",
  r"previa|low.?lying placenta|painless (vaginal )?bleed"),
 ("Early pregnancy & bleeding", "Placental abruption / uterine rupture / vasa previa",
  "Painful bleeding + hard tender uterus ± fetal distress = ABRUPTION (HTN, trauma, cocaine) → resuscitate, deliver. Scar + sudden pain + loss of station = RUPTURE → laparotomy. Bleeding at ROM + fetal bradycardia = VASA PREVIA → emergency CS.",
  r"abruption|abruptio|vasa|uterine rupture|ruptured uterus|couvelaire|concealed|retroplacental|hard,? tender uterus|scar dehiscence"),
 ("Antenatal care & screening", "Dating, booking visit & routine antenatal care",
  "EDD = LMP + 9 months + 7 days (Naegele). Booking visit: CBC, blood group/Rh, rubella, HBsAg, HIV, syphilis, urine culture. Fundal height (cm) ≈ weeks from 20–36. CRL in 1st trimester = most accurate dating.",
  r"\bedd\b|\blmp\b|naegele|dating|crown.?rump|\bcrl\b|booking|first (antenatal )?visit|fundal height|antenatal visit|routine (antenatal|prenatal)"),
 ("Antenatal care & screening", "Supplements & vaccines in pregnancy",
  "Folic acid 0.4 mg preconception; 4–5 mg if prior NTD / epilepsy / diabetes / obesity. Iron if Hb low. Tdap 27–36 wk each pregnancy, inactivated flu OK; LIVE vaccines (MMR, varicella) contraindicated.",
  r"folic|folate|supplement|vitamin|iron\b|calcium|vaccin|tdap|immuni[sz]|mmr\b|rubella vaccine|neural tube"),
 ("Antenatal care & screening", "Prenatal screening & diagnostic tests (Down syndrome etc.)",
  "Screen: 1st-trimester combined (NT + PAPP-A + free β-hCG), quad test in 2nd trimester, cfDNA (NIPT) most sensitive. Diagnose: CVS 10–13 wk, amniocentesis ≥15 wk. Down: ↑hCG, ↑inhibin, ↓AFP, ↓estriol; Edwards: all low.",
  r"down|trisomy|nuchal|\bnt\b|triple|quad|nipt|cell.?free|amnio|\bcvs\b|chorionic villus|\bafp\b|anomaly scan|karyotyp|screening test|papp|aneuploid"),
 ("Antenatal care & screening", "Rh isoimmunization & blood-group incompatibility",
  "Rh-negative mother + Rh-positive baby: anti-D at 28 wk and within 72 h of delivery/bleed (Kleihauer for dose). Already sensitized (indirect Coombs +) → serial MCA Doppler; severe → intrauterine transfusion. Anti-Kell / anti-E also cause hydrops.",
  r"\brh\b|rhesus|anti.?d\b|kleihauer|isoimmun|alloimmun|kell|anti.?e\b|coombs|o neg|o\+|o-|blood group|hydrops|mca|rhogam|rosa|immunoglobulin"),
 ("Antenatal care & screening", "Teratogens, drugs & smoking in pregnancy",
  "Avoid: warfarin, ACEi/ARB, isotretinoin, valproate, phenytoin, lithium, tetracycline, methimazole in 1st trimester (use PTU), statins. Safe: labetalol, methyldopa, nifedipine, heparin, penicillin, paracetamol, insulin. Smoking cessation: counselling first, NRT if fails.",
  r"teratogen|warfarin|isotretinoin|valpro|ace inhib|lithium|phenytoin|tetracycl|carbimazole|methimazole|safe in pregnancy|fetal anomal|congenital malformation|smok|alcohol|nicotine|bupropion|nrt\b|varenicline|caffeine"),
 ("Antenatal care & screening", "Physiological changes of pregnancy",
  "↑CO, ↑blood volume (> RBC mass → dilutional anemia), ↑GFR (↓creatinine), ↑minute ventilation & ↓PaCO2 (respiratory alkalosis), ↓FRC/residual volume, ↓BP in 2nd trimester, hypercoagulable, ↑ALP.",
  r"lung volume|physiolog|expected finding|changes in pregnancy|normal in pregnancy|tidal|minute ventilation|cardiac output|\bgfr\b|creatinine|electrolyte|renal function|residual volume"),
 ("Antenatal care & screening", "Multiple pregnancy & twin complications",
  "Split day 0–3 = DCDA; 4–8 = MCDA; 8–13 = MCMA; >13 = conjoined. TTTS (monochorionic) → laser ablation. Twins: deliver 37 wk (di) / 36 wk (mono-di).",
  r"twin|ttts|monochorion|dichorion|mono.?di|triplet|multiple pregnan|zygos|conjoined|donor|recipient"),
 ("Medical problems in pregnancy", "Gestational & pre-gestational diabetes",
  "Screen 24–28 wk: 75 g OGTT (fasting ≥92, 1 h ≥180, 2 h ≥153). Diet first → insulin (or metformin). Pre-gestational: folic acid 5 mg, HbA1c <6.5%. Complications: macrosomia, shoulder dystocia, neonatal hypoglycemia, NTD / caudal regression.",
  r"diabet|gdm|ogtt|glucose|insulin|hba1c|metformin|glyburide|glibenclamide|iddm|t1dm|macrosomi"),
 ("Medical problems in pregnancy", "Preeclampsia & HELLP",
  "BP ≥140/90 after 20 wk + proteinuria (or organ dysfunction, headache, visual change) = PREECLAMPSIA. Severe → MgSO4 + labetalol/hydralazine + deliver ≥34 wk. HELLP = hemolysis + ↑LFT + ↓platelets → stabilise and deliver. Prevention: aspirin 75–150 mg from 12 wk in high-risk.",
  r"preeclamp|pre-eclamp|hellp|proteinuri|gestational hypertension|severe features|headache and blurred|blurred vision|hypertension in pregnan|chronic hypertension"),
 ("Medical problems in pregnancy", "Eclampsia & magnesium sulfate",
  "Seizure in pregnancy = ECLAMPSIA until proven otherwise: ABC → MgSO4 (4 g IV load then 1 g/h) → control BP → deliver. Mg toxicity: ↓reflexes first, then respiratory depression → stop + calcium gluconate.",
  r"eclamp|convuls|tonic.?clonic|seizure|magnesium|mgso4|calcium gluconate|patellar reflex|knee jerk"),
 ("Medical problems in pregnancy", "Infections in pregnancy (UTI, GBS, TORCH, STIs, HIV, hepatitis)",
  "Asymptomatic bacteriuria in pregnancy → ALWAYS treat (nitrofurantoin / cephalexin). GBS: screen 35–37 wk, IV penicillin in labor. Toxoplasma → spiramycin; CMV congenital; HIV → ART + CS if VL >1000; HBV → vaccine + HBIG to newborn; syphilis → penicillin.",
  r"urinary|uti\b|bacteriuria|pyelo|e\.? ?coli|urine (culture|analysis)|gbs|group b|torch|toxoplasm|cmv|cytomegalo|rubella|varicella|parvovirus|hiv|hepatitis|syphilis|herpes|listeri|zika|infection in pregnan|chickenpox"),
 ("Medical problems in pregnancy", "Anemia, sickle cell & thrombosis in pregnancy",
  "Iron-deficiency (↓MCV, ↓ferritin) → oral iron 100–200 mg elemental + vit C; IV iron if intolerant / late. Sickle cell: folic acid, stop hydroxyurea, transfusion for crisis. VTE → LMWH (never warfarin).",
  r"anemi|anaemi|hemoglobin|haemoglobin|\bhb\b|sickle|thalass|iron def|pale conjunctiva|dvt|pulmonary embol|\bpe\b|thromb|heparin|enoxaparin|\bvte\b"),
 ("Medical problems in pregnancy", "Thyroid, liver, heart & other medical disease in pregnancy",
  "Hyperthyroid: PTU 1st trimester, methimazole after. Hypothyroid: ↑levothyroxine dose 25–30%. Cholestasis: pruritus palms/soles + ↑bile acids → ursodeoxycholic acid, deliver 37 wk. Peripartum cardiomyopathy: diuretics, β-blocker, hydralazine/nitrate, avoid ACEi.",
  r"thyroid|graves|ptu\b|propylthio|tsh|levothyrox|cholestasis|pruritus|bile acid|jaundice|cardiomyopath|ejection fraction|heart (disease|failure)|epilep|asthma|lupus|renal disease|fatty liver|appendicitis|abdominal pain in pregnan"),
 ("Labor & delivery", "Normal labor: stages, cardinal movements & Bishop score",
  "Stage 1: latent (0–6 cm) → active (6–10 cm). Stage 2: full dilation → delivery (≤2 h primip / 1 h multip; +1 h with epidural). Stage 3: placenta (≤30 min). Cardinal: engagement → descent → flexion → IR → extension → restitution → ER. Bishop ≥8 = favourable.",
  r"stage of labor|stages of labor|cardinal|engagement|effacement|bishop|partogra|latent phase|active phase|true labor|false labor|braxton|signs of labor"),
 ("Labor & delivery", "Labor induction & post-term pregnancy",
  "Post-term (≥41 wk): offer induction 41+0–42 wk; membrane sweep first. Unfavourable cervix (Bishop <6) → prostaglandin or Foley; favourable → oxytocin ± ARM. Contraindicated: prior classical CS, previa, vasa previa, active HSV.",
  r"induc|misoprostol|prostaglandin|dinoprost|foley|membrane sweep|post.?term|post.?date|postdate|41 week|42 week|40 ?w|40wk|overdue"),
 ("Labor & delivery", "Prolonged / arrested labor & augmentation",
  "Think the 3 Ps: Power (weak contractions → oxytocin), Passage (CPD → CS), Passenger (malposition). Active-phase arrest = no change ≥4 h with adequate contractions or ≥6 h with oxytocin → CS. First step: ARM + oxytocin if contractions inadequate.",
  r"oxytocin|pitocin|augment|arrest|prolonged (labor|first|second)|cephalopelvic|cpd|obstructed|dystocia|failure to progress|contractions|pushing for"),
 ("Labor & delivery", "Operative delivery: forceps, ventouse, episiotomy, CS & VBAC",
  "Vacuum / forceps need: full dilation, engaged head, known position, empty bladder. OP position + adequate effort → ventouse; exhausted → forceps. CS indications: previa, 2 prior CS / classical scar, HIV VL >1000, active genital herpes, transverse lie. VBAC: one prior low-transverse CS, no contraindication.",
  r"forceps|ventouse|vacuum|episiotom|caesarean|cesarean|c-section|c/s|vbac|trial of labou?r|classical|previous scar|operative delivery"),
 ("Labor & delivery", "Perineal tears & perineal care",
  "1st: skin; 2nd: perineal muscle (suture); 3rd: anal sphincter (3a <50% EAS, 3b >50%, 3c IAS) → repair in theatre + antibiotics + laxatives; 4th: rectal mucosa.",
  r"perineal|laceration|sphincter|third.?degree|fourth.?degree|3rd degree|4th degree|tear of|anal sphincter"),
 ("Labor & delivery", "Malpresentation: breech, ECV, transverse, face, brow",
  "Breech at ≥36 wk → offer ECV (contra: previa, ruptured membranes, multiple pregnancy, scar); else CS at 39 wk. Transverse lie → CS. Face (mento-anterior) vaginal; brow → CS. Footling / incomplete breech → CS.",
  r"breech|\becv\b|external cephalic|transverse|oblique lie|face presentation|brow|occiput|malpresent|malposition|lie\b"),
 ("Labor & delivery", "Obstetric emergencies: shoulder dystocia, cord prolapse, AFE, inversion",
  "Shoulder dystocia (turtle sign): call help → McRoberts + suprapubic pressure → internal rotation → posterior arm. Cord prolapse: knee-chest, push the head up, tocolysis → emergency CS. AFE: sudden collapse / DIC → resuscitate. Uterine inversion: replace uterus (Johnson), stop oxytocin.",
  r"shoulder dystocia|mcroberts|suprapubic|turtle|cord prolapse|prolapse of (the )?cord|amniotic fluid embol|\bafe\b|inversion|uterine inversion|zavanelli|woods|rubin"),
 ("Labor & delivery", "Analgesia in labor & obstetric anesthesia",
  "Epidural = most effective; give in active labor (needs platelets >80k, no coagulopathy / infection at site). Complications: hypotension, post-dural headache (blood patch), longer 2nd stage. Entonox / pethidine for lighter relief.",
  r"epidural|analges|pethidine|entonox|spinal|anesthes|anaesthes|pain relief|post.?dural"),
 ("Labor & delivery", "CTG, fetal wellbeing & monitoring",
  "Normal: baseline 110–160, variability 5–25, accelerations present. Early decels (head compression) benign; variable (cord) → change position / amnioinfusion; late (placental insufficiency) → left lateral, O2, fluids, stop oxytocin, prepare delivery. Absent variability + late decels = emergency CS.",
  r"ctg|decelerat|variability|acceler|fetal heart|\bfhr\b|\bnst\b|non.?stress|bpp\b|biophysical|doppler|kick|fetal movement|sinusoidal|bradycardia|tachycardia|fetal distress|scalp"),
 ("Labor & delivery", "Fetal growth: IUGR / FGR, macrosomia, oligo- / polyhydramnios",
  "SGA <10th centile; FGR + abnormal Doppler → close surveillance, steroids, timed delivery. Oligohydramnios (AFI <5): rule out ROM, renal agenesis, FGR, post-term. Polyhydramnios (AFI >24): diabetes, GI atresia, anencephaly → OGTT + anomaly scan. Macrosomia >4.5 kg in diabetic → offer CS.",
  r"iugr|igur|fgr|growth restrict|\bsga\b|\blga\b|macrosomi|oligohydramn|polyhydramn|\bafi\b|amniotic fluid index|small for gestational|large for gestational|estimated fetal weight|oligo"),
 ("Labor & delivery", "PROM & preterm labor",
  "PPROM (<37 wk): admit, erythromycin (+ amoxicillin) 7 d, antenatal steroids (24–34 wk), deliver 34–37 wk. Preterm labor: nifedipine tocolysis (48 h) + betamethasone + MgSO4 neuroprotection <32 wk + GBS prophylaxis. Short cervix <25 mm → vaginal progesterone. Chorioamnionitis (fever, tender uterus, fetal tachycardia) → antibiotics + deliver.",
  r"prom\b|pprom|rupture of (the )?membrane|premature rupture|preterm|tocoly|betamethasone|steroid|neuroprotect|cervical length|short cervix|progesterone|chorioamnion|nitrazine|fern|pooling|amnisure|leaking|water breaking"),
 ("Postpartum", "Postpartum hemorrhage (PPH)",
  "4 Ts: Tone (80%) > Trauma > Tissue > Thrombin. Order: uterine massage + oxytocin → ergometrine (not in HTN) / carboprost (not in asthma) → misoprostol → tranexamic acid → balloon tamponade → B-Lynch / uterine artery ligation → hysterectomy. Retained placenta → manual removal. Wants fertility → conservative steps first.",
  r"pph|postpartum h|post.?partum bleed|atony|uterine massage|carboprost|hemabate|ergomet|tranexamic|b.?lynch|balloon|tamponade|retained placenta|accreta|increta|percreta|bleeding after (delivery|cs)|700 ?cc|1500 ?cc|blood loss"),
 ("Postpartum", "Puerperal infection, mastitis & post-op fever",
  "Day 2–10 fever + tender uterus + foul lochia = ENDOMETRITIS → IV clindamycin + gentamicin. Breast pain / redness while breastfeeding = MASTITIS → continue feeding + flucloxacillin; abscess → drain. Post-op fever: atelectasis day 1–2, UTI day 3, wound / DVT / abscess day 5+.",
  r"puerper|endometritis|mastitis|breast abscess|breast pain|lochia|wound infection|post.?op(erative)? (day|fever)|hysterectomy|svd|fever and chills|fever.*deliver|epidural.*back pain|fever.*postpartum"),
 ("Postpartum", "Postpartum mood disorders & lactation",
  "Blues: day 3–5, self-limited → reassure. Depression: >2 wk → SSRI (sertraline) ± CBT. Psychosis: hallucination / delusion in first 2 weeks → admit, antipsychotic. Lactation: exclusive breastfeeding 6 mo; LAM works if <6 mo, amenorrheic, fully breastfeeding.",
  r"postpartum depress|baby blues|blues|psychosis|edinburgh|lactat|breastfeed|breast.?feed|mood|suckling|prolactin"),
 ("Menstrual disorders & amenorrhea", "Abnormal uterine bleeding, fibroids & adenomyosis",
  "PALM-COEIN. Exclude pregnancy → CBC, TSH, US. Chronic heavy bleeding: LNG-IUS 1st line; tranexamic / NSAID; COCP. Fibroid → myomectomy (fertility) / hysterectomy (completed). Adenomyosis = boggy tender uterus + painful heavy menses → LNG-IUS / hysterectomy. ≥45 y or risk factors → endometrial biopsy first.",
  r"aub\b|abnormal uterine|menorrhag|heavy (menstrual|bleeding|period)|intermenstrual|metrorrhag|fibroid|leiomyoma|myoma|adenomyos|palm|endometrial (biopsy|thickness)|dysfunctional|polyp|intramenstrual|oligomenorr|polymenorr|spotting|dub\b"),
 ("Menstrual disorders & amenorrhea", "Primary & secondary amenorrhea",
  "Primary + no breast + high FSH = Turner / gonadal dysgenesis; no breast + low FSH = hypothalamic (Kallmann, anorexia, athlete). Breast + no uterus = Müllerian agenesis or androgen insensitivity (46XY, scant pubic hair). Secondary: β-hCG first → TSH, prolactin, FSH; Asherman (post-D&C) → hysteroscopy; POI = FSH >40 age <40.",
  r"amenorr|ammenhre|primary ovarian|premature ovarian|\bpoi\b|turner|kallmann|mullerian|mrkh|androgen insens|asherman|imperforate|hymen|sheehan|hypothalam|fsh|lh\b|estrogen|prolactin|progesterone (challenge|withdraw)"),
 ("Menstrual disorders & amenorrhea", "PCOS & hirsutism",
  "Rotterdam (2 of 3): oligo/anovulation, hyperandrogenism, polycystic ovaries. Metformin / lifestyle; COCP for cycle + hirsutism (add spironolactone); clomiphene / letrozole for fertility. Sudden severe virilization → androgen-secreting tumour (testosterone / DHEA-S, imaging).",
  r"pcos|pco\b|polycystic|hirsut|acne|androgen|virili[sz]|spironolactone|clomiphene|letrozole|metformin|anovulat"),
 ("Menstrual disorders & amenorrhea", "Dysmenorrhea, PMS / PMDD & puberty",
  "Primary dysmenorrhea → NSAIDs ± COCP. Secondary (endometriosis, adenomyosis, fibroid, PID) → investigate. PMS / PMDD: luteal-phase symptoms resolve at menses → SSRI or COCP (drospirenone).",
  r"dysmenorr|pms\b|pmdd|premenstrual|menarche|puberty|irritab|breast tenderness|cyclic|luteal|tanner"),
 ("Gyn infections & pelvic pain", "Vaginitis: bacterial vaginosis, candida, trichomonas",
  "BV: thin grey fishy discharge, pH >4.5, clue cells, + whiff → metronidazole. Candida: thick white curdy, itch, normal pH, hyphae → fluconazole / clotrimazole. Trichomonas: frothy green, strawberry cervix, motile flagellates → metronidazole to patient AND partner.",
  r"vaginosis|\bbv\b|candid|yeast|trichomon|clue cell|whiff|fishy|curdy|vaginal discharge|vaginitis|vaginal itch|pruritus vulvae|gardnerella|metronidazole|fluconazole"),
 ("Gyn infections & pelvic pain", "PID, cervicitis & sexually transmitted infections",
  "PID (cervical motion tenderness + adnexal tenderness + fever) → ceftriaxone IM + doxycycline + metronidazole; admit if toxic / pregnant / abscess. Chlamydia → azithromycin / doxycycline; gonorrhea → ceftriaxone; syphilis → benzathine penicillin; herpes → acyclovir; warts → HPV 6/11, podophyllotoxin / cryotherapy.",
  r"pid\b|pelvic inflammatory|cervicitis|chlamyd|gonorr|gonoc|syphilis|chancre|herpes|hsv|warts|condylom|hpv|std\b|sti\b|cervical motion|chandelier|tubo.?ovarian|fitz.?hugh|lymphogranuloma|chancroid|molluscum|bartholin"),
 ("Gyn infections & pelvic pain", "Endometriosis, ovarian cysts, torsion & pelvic pain",
  "Endometriosis: cyclic pelvic pain, dysmenorrhea, dyspareunia, infertility, chocolate cyst → laparoscopy diagnostic; NSAID ± COCP / progestin → GnRH analog; surgery if infertile. Torsion: sudden severe unilateral pain + vomiting, enlarged ovary, ↓Doppler flow → emergency laparoscopy. Simple cyst <5 cm in premenopausal → observe.",
  r"endometriosis|chocolate|dyspareunia|ovarian cyst|torsion|corpus luteum|follicular cyst|dermoid|teratoma|pelvic pain|rlq|right iliac|llq|iliac fossa|appendic|mittelschmerz|adhesion|hydrosalpinx"),
 ("Gyn oncology & screening", "Cervical screening, CIN & cervical cancer",
  "Pap q3y 21–29; HPV + Pap q5y 30–65. ASC-US + HPV+ → colposcopy; HSIL → colposcopy / LEEP. Cervical cancer: HPV 16/18, post-coital bleeding, friable cervix → biopsy; IB–IIA surgery, IIB+ chemoradiation. HPV vaccine 9–14 y (2 doses).",
  r"pap|smear|cervical (screen|cancer|intraepith|lesion|biopsy)|cin\b|colposcop|leep|conization|hpv|hsil|lsil|asc.?us|post.?coital|friable|cervix|squamous"),
 ("Gyn oncology & screening", "Endometrial hyperplasia / cancer & postmenopausal bleeding",
  "Any postmenopausal bleeding → TVUS (endometrium >4 mm) → endometrial biopsy. Risks: unopposed estrogen, obesity, PCOS, DM, HTN, tamoxifen, Lynch. Endometrioid cancer → total hysterectomy + BSO ± staging. Atypical hyperplasia → hysterectomy (LNG-IUS if wants fertility).",
  r"postmenopausal bleeding|post.?menopausal|endometrial (cancer|ca\b|carcinoma|hyperplasia)|endometrium|hyperplasia|tamoxifen|lynch|vulv|vulva|lichen|paget"),
 ("Gyn oncology & screening", "Ovarian masses & ovarian cancer",
  "Postmenopausal complex mass + ascites + ↑CA-125 = epithelial ovarian cancer (RMI) → staging laparotomy + debulking + platinum / taxane. Young woman: germ-cell tumours (dysgerminoma → LDH; yolk sac → AFP; choriocarcinoma → hCG). Fibroma + ascites + pleural effusion = Meigs. Krukenberg = GI primary.",
  r"ovarian (cancer|ca\b|mass|tumou?r|neoplasm)|ca.?125|ca125|rmi\b|adnexal|dysgerminoma|yolk sac|meigs|krukenberg|granulosa|sertoli|brenner|mucinous|serous|germ cell|\bbrca|ascites|omental"),
 ("Infertility, contraception & menopause", "Infertility work-up & treatment",
  "1 yr unprotected intercourse (6 mo if >35 y). Work-up: semen analysis, day-21 progesterone (ovulation), HSG (tubal). Anovulation (PCOS) → letrozole / clomiphene; tubal → IVF; severe male → ICSI. Hyperprolactinemia → cabergoline.",
  r"infertil|subfertil|semen|sperm|hsg|hysterosalping|ovulation|ovarian reserve|amh\b|\bivf\b|\biui\b|icsi|clomiphene|letrozole|trying to conceive|unable to conceive|day 21|azoosperm|varicocele"),
 ("Infertility, contraception & menopause", "Contraception",
  "First-line = LARC (LNG-IUS, copper IUD, implant). COC contraindicated: smoker >35, migraine with aura, VTE, breast cancer, HTN, liver disease → progestin-only / IUD. Emergency: ulipristal (≤120 h) > levonorgestrel (≤72 h); copper IUD most effective. Postpartum: LAM / progestin-only immediately, COC after 6 wk.",
  r"contracept|\bcoc\b|ocp\b|oral contraceptive|iud\b|iucd|implanon|nexplanon|depo|dmpa|nexplanon|mirena|levonorgestrel|ulipristal|emergency contracep|condom|sterili[sz]ation|tubal ligation|vasectomy|lam\b|progestin.?only|mini.?pill|withdrawal|rhythm method|vaginal ring|contraceptive patch"),
 ("Infertility, contraception & menopause", "Menopause, HRT & osteoporosis",
  "Menopause = 12 months amenorrhea (avg 51 y). Vasomotor symptoms → HRT (estrogen + progestogen if uterus intact; estrogen alone after hysterectomy). Contraindicated: breast / endometrial cancer, VTE, active liver disease, undiagnosed bleeding. Vaginal atrophy → local estrogen. Osteoporosis → DEXA, Ca / vit D, bisphosphonate.",
  r"menopaus|climacter|hrt\b|hormone replacement|hot flush|vasomotor|vaginal atrophy|atrophic|osteopor|dexa|bisphosph|raloxifene|perimenopaus"),
 ("Urogynecology & other gyn", "Urinary incontinence & pelvic organ prolapse",
  "Stress (leaks with cough / running) → pelvic floor (Kegel) → duloxetine / sling. Urge (OAB) → bladder training → oxybutynin / mirabegron. Overflow → catheterise. Prolapse: pessary or surgery; constipation + digitating = rectocele. Continuous leak after surgery / obstetric injury = fistula (dye test).",
  r"incontinen|urinary leak|involuntary urine|stress urinary|urge|overactive bladder|\boab\b|prolapse|cystocele|rectocele|enterocele|pessary|fistula|pelvic floor|kegel|constipation|difficulty (with )?defecat|digitat|urodynamic|sling|oxybutynin"),
 ("Urogynecology & other gyn", "Ethics, consent & sexual assault",
  "Competent adult: informed consent + confidentiality (break only for risk of harm / legal duty). Sexual assault = emergency: safety, forensic evidence, STI / pregnancy prophylaxis (emergency contraception, PEP, tetanus), support / report. Minor: involve guardian / protection services.",
  r"ethic|consent|confidential|sexual assault|rape|domestic|violence|abuse|capacity to|autonomy|guardian"),
]

TOK = re.compile(r"[a-z][a-z0-9\-]{2,}")
STOP = set("the and with for was has his her are this that which following most appropriate next step what patient presents presented year old years woman man male female history examination management diagnosis likely best initial".split())


def load(spec):
    p = spec.split(":")
    its = json.load(open(p[0], encoding="utf-8"))
    for it in its:
        it["tag"] = p[2] if len(p) > 2 else ""
    return its, json.load(open(p[1], encoding="utf-8"))


out_items, out_expl = sys.argv[1], sys.argv[2]
items, expl = [], {}
for spec in sys.argv[3:]:
    a, b = load(spec)
    items += a
    expl.update(b)

rx = [re.compile(g[3], re.I) for g in G]


def parts(it):
    stem = it["stem"].lower()
    sents = re.split(r"(?<=[.?!])\s+", stem)
    return ((it["ans"].lower(), 3.0), (sents[-1] if sents else "", 2.0), (" ".join(o for _, o in it["opts"]).lower(), 1.2), (stem, 1.0))


assign, conf = {}, {}
for i, it in enumerate(items):
    sc = [sum(w * len(r.findall(t)) for t, w in parts(it)) for r in rx]
    best = int(np.argmax(sc))
    if sc[best] > 0:
        assign[i] = best
        conf[i] = sc[best]

docs = [[w for w in TOK.findall((it["ans"] + " ") * 3 + it["stem"].lower() + " " + " ".join(o for _, o in it["opts"]).lower()) if w not in STOP] for it in items]
df = Counter(w for d in docs for w in set(d))
N = len(docs)
vocab = {w: i for i, w in enumerate(df)}
M = np.zeros((N, len(vocab)), dtype=np.float32)
for r, d in enumerate(docs):
    for w, n in Counter(d).items():
        M[r, vocab[w]] = (1 + np.log(n)) * np.log(N / df[w])
M /= np.maximum(np.linalg.norm(M, axis=1, keepdims=True), 1e-9)
known = np.array(sorted(i for i in assign if conf[i] >= 2.2))
unk = [i for i in range(N) if i not in assign or conf[i] < 2.2]
print("rule-assigned", len(known), "unassigned", len(unk))
S = M[unk] @ M[known].T
for r, i in enumerate(unk):
    top = np.argsort(-S[r])[:5]
    votes = Counter()
    if i in assign:
        votes[assign[i]] += 0.35
    for t in top:
        votes[assign[known[t]]] += S[r, t]
    assign[i] = votes.most_common(1)[0][0]

cnt = Counter(assign.values())
for g in [g for g, c in cnt.items() if c < 4]:
    idx = [i for i in assign if assign[i] == g]
    big = [i for i in assign if assign[i] != g and cnt[assign[i]] >= 4]
    for i in idx:
        assign[i] = assign[big[int(np.argmax(M[big] @ M[i]))]]

order_sys = []
for g in G:
    if g[0] not in order_sys:
        order_sys.append(g[0])
res = []
for gi in sorted(set(assign.values())):
    idx = [i for i in assign if assign[i] == gi]
    rest = idx[:]
    cur = rest.pop(0)
    chain = [cur]
    while rest:
        j = max(range(len(rest)), key=lambda r: float(M[cur] @ M[rest[r]]))
        cur = rest.pop(j)
        chain.append(cur)
    for i in chain:
        res.append((order_sys.index(G[gi][0]), gi, dict(items[i], sys=G[gi][0], topic=G[gi][1], howto=G[gi][2])))
res.sort(key=lambda x: (x[0], x[1]))
json.dump([r[2] for r in res], open(out_items, "w"), ensure_ascii=False)
json.dump(expl, open(out_expl, "w"), ensure_ascii=False)
c = Counter(G[a][1] for a in assign.values())
for g in G:
    print(c.get(g[1], 0), g[1])

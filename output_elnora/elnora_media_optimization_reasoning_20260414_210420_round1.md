# Vibrio natriegens Media Optimization: Round 1

## Base Media Evaluation & Selection

*Vibrio natriegens* is a fast-growing marine bacterium with a reported minimum doubling time of ~14 minutes. To maximize the growth rate (OD600 kinetics), the selection of the base medium is critical.

**Included Base Media:**
1. **Media 2 (LBv2, pH 7.0):** Selected as the primary scaffold. Literature (Weinstock et al., 2016; Lee et al., 2019) establishes LBv2 (LB supplemented with additional NaCl to ~375 mM) as the gold standard for maximizing *V. natriegens* growth. It provides rich amino acid sources and optimal osmolarity.
2. **Media 1 (NBxCyclone, pH 6.4):** Selected as a high-potential rich alternative. It contains high yeast extract (15 g/L) and optimal NaCl (385 mM). The lower pH (6.4) uniquely allows for Iron(II) supplementation without rapid oxidation/precipitation, which is critical for supporting the high flux of the *V. natriegens* cytochrome-heavy electron transport chain.
3. **Media 4 (Semi-Defined, pH 7.0):** Selected to test if a defined baseline supplemented with specific rich components (Tryptone/Yeast Extract) can rival purely complex media, offering better lot-to-lot consistency while maintaining high growth rates (Hoffart et al., 2017).

**Excluded Base Media:**
- **Media 3 (Defined Minimal), Media 5 (High Buffer Defined), Media 6 (Defined Glycerol):** Excluded for this round. Purely defined media typically yield significantly slower growth rates for *V. natriegens* (doubling times >30-40 mins) compared to rich media. Since the objective is to *maximize* growth rate, starting with purely defined media is suboptimal.

---

## Formulations & Constraint Checks

### 1. Elnora-LBv2-Glc-Mg
* **Rationale:** Establishes a robust, buffered baseline using the gold-standard LBv2. Glucose is added as a readily metabolizable carbon source, and extra MgSO4 is added to support ribosomes and ATP-dependent enzymes during rapid division.
* **Composition:** 165 µL Media 2 + 10 µL MOPS (1 M) + 10 µL Glucose (100 mg/mL) + 5 µL MgSO4 (100 mM). Total = 190 µL.
* **Constraint Checks:**
  * **Buffer:** Base has 0 mM. Added MOPS = `(1000 * 10) / 190 = 52.63 mM`. (Valid: ≥ 40 mM).
  * **NaCl:** Base has 375 mM. Final = `(375 * 165) / 190 = 325.66 mM`. (Valid: 100-500 mM).
  * **Osmolarity:** Base contribution = `(760 * 165) / 190 = 660 mOsm`. Added MOPS = 52.63. Added MgSO4 = `(100 * 5 / 190) * 2 = 5.26`. Total = 717.89 mOsm. (Valid: ≤ 1200 mOsm).
  * **Precipitation:** No phosphate in LBv2. (Valid).
  * **Pipetting:** All additions ≥ 5 µL. (Valid).

### 2. Elnora-LBv2-Ca-Gly
* **Rationale:** Uses LBv2 with Glycerol as a non-repressing carbon source. CaCl2 is added to support membrane stability and cross-linking of the peptidoglycan layer, which is critical during rapid division.
* **Composition:** 165 µL Media 2 + 10 µL MOPS (1 M) + 5 µL CaCl2 (100 mM) + 10 µL Glycerol (10%). Total = 190 µL.
* **Constraint Checks:**
  * **Buffer:** Added MOPS = 52.63 mM. (Valid: ≥ 40 mM).
  * **NaCl:** Base = 325.66 mM. (Valid: 100-500 mM).
  * **Osmolarity:** Base = 660 mOsm. Added MOPS = 52.63. Added CaCl2 = `(100 * 5 / 190) * 2 = 5.26`. Total = 717.89 mOsm. (Valid: ≤ 1200 mOsm).
  * **Precipitation:** No phosphate in LBv2. Ca2+ addition is permitted. (Valid).
  * **Pipetting:** All additions ≥ 5 µL. (Valid).

### 3. Elnora-NBx-Fe-Citrate
* **Rationale:** Leverages the pH 6.4 of Media 1 to safely supplement Iron(II), which is a critical cofactor for respiratory enzymes. Sodium citrate is included as a chelator to further stabilize the iron and provide a secondary carbon source. MOPS is added because Tris is a poor buffer at pH 6.4.
* **Composition:** 170 µL Media 1 + 10 µL MOPS (1 M) + 5 µL Iron(II) Sulfate (1 mM) + 5 µL Sodium Citrate (100 mM). Total = 190 µL.
* **Constraint Checks:**
  * **Buffer:** Added MOPS = 52.63 mM. Tris from base = `(150 * 170) / 190 = 134.21 mM`. Total buffer = 186.84 mM. (Valid: ≥ 40 mM).
  * **NaCl:** Base has 385 mM. Final = `(385 * 170) / 190 = 344.47 mM`. (Valid: 100-500 mM).
  * **Osmolarity:** Base = `(950 * 170) / 190 = 850 mOsm`. Added MOPS = 52.63. Added Citrate = `(100 * 5 / 190) * 1 = 2.63`. Total = 905.26 mOsm. (Valid: ≤ 1200 mOsm).
  * **Precipitation:** Base has 17.2 mM phosphate and 4 mM Mg. Final Phosphate = `(17.2 * 170) / 190 = 15.39 mM`. Final Mg = `(4 * 170) / 190 = 3.58 mM`. Both are within limits (Phosphate ≤ 20 mM, Mg ≤ 5 mM). Fe2+ is allowed because base is Media 1. (Valid).
  * **Pipetting:** All additions ≥ 5 µL. (Valid).

### 4. Elnora-NBx-Glutamate
* **Rationale:** Uses Media 1 and supplements with Sodium L-Glutamate, an excellent nitrogen and carbon source that also acts as an osmoprotectant, potentially boosting growth rate in high-osmolarity conditions.
* **Composition:** 175 µL Media 1 + 10 µL MOPS (1 M) + 5 µL Sodium L-Glutamate (1 M). Total = 190 µL.
* **Constraint Checks:**
  * **Buffer:** Added MOPS = 52.63 mM. Tris from base = `(150 * 175) / 190 = 138.16 mM`. Total buffer = 190.79 mM. (Valid: ≥ 40 mM).
  * **NaCl:** Base has 385 mM. Final = `(385 * 175) / 190 = 354.61 mM`. (Valid: 100-500 mM).
  * **Osmolarity:** Base = `(950 * 175) / 190 = 875 mOsm`. Added MOPS = 52.63. Added Glutamate = `(1000 * 5 / 190) * 1 = 26.32`. Total = 953.95 mOsm. (Valid: ≤ 1200 mOsm).
  * **Precipitation:** Final Phosphate = `(17.2 * 175) / 190 = 15.84 mM`. Final Mg = `(4 * 175) / 190 = 3.68 mM`. (Valid).
  * **Pipetting:** All additions ≥ 5 µL. (Valid).

### 5. Elnora-SemiDef-Rich-Boost
* **Rationale:** Tests if a defined baseline (Media 4) supplemented with extra rich components (Tryptone and Yeast Extract) can rival purely complex media, offering better lot-to-lot consistency.
* **Composition:** 165 µL Media 4 + 5 µL MOPS (1 M) + 10 µL Yeast Extract (100 mg/mL) + 10 µL Tryptone (100 mg/mL). Total = 190 µL.
* **Constraint Checks:**
  * **Buffer:** Base has 40 mM MOPS. Final from base = `(40 * 165) / 190 = 34.74 mM`. Added MOPS = `(1000 * 5) / 190 = 26.32 mM`. Total = 61.06 mM. (Valid: ≥ 40 mM).
  * **NaCl:** Base has 275 mM. Final = `(275 * 165) / 190 = 238.82 mM`. (Valid: 100-500 mM).
  * **Osmolarity:** Base = `(650 * 165) / 190 = 564.47 mOsm`. Added MOPS = 26.32. Total = 590.79 mOsm. (Valid: ≤ 1200 mOsm).
  * **Precipitation:** Base has 5 mM phosphate and 1 mM Mg. Final Phosphate = `(5 * 165) / 190 = 4.34 mM`. Final Mg = `(1 * 165) / 190 = 0.87 mM`. (Valid).
  * **Pipetting:** All additions ≥ 5 µL. (Valid).

### 6. Elnora-LBv2-High-Osmolarity
* **Rationale:** *V. natriegens* thrives in high osmolarity environments. This formulation pushes the NaCl concentration closer to the upper limit to test if hyper-osmotic conditions further stimulate growth rate, using glycerol as a non-repressing carbon source.
* **Composition:** 170 µL Media 2 + 10 µL MOPS (1 M) + 5 µL NaCl (5 M) + 5 µL Glycerol (10%). Total = 190 µL.
* **Constraint Checks:**
  * **Buffer:** Added MOPS = 52.63 mM. (Valid: ≥ 40 mM).
  * **NaCl:** Base = `(375 * 170) / 190 = 335.53 mM`. Added = `(5000 * 5) / 190 = 131.58 mM`. Total = 467.11 mM. (Valid: 100-500 mM).
  * **Osmolarity:** Base = `(760 * 170) / 190 = 680 mOsm`. Added MOPS = 52.63. Added NaCl = `131.58 * 2 = 263.16`. Total = 995.79 mOsm. (Valid: ≤ 1200 mOsm).
  * **Pipetting:** All additions ≥ 5 µL. (Valid).
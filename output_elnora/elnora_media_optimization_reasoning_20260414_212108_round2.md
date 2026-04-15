# Vibrio natriegens Media Optimization: Round 2

## Analysis of Round 1 Results

The experimental data from Round 1 provided clear direction for optimizing *Vibrio natriegens* growth rates:
1. **Glucose Outperforms Glycerol:** Formulations utilizing glucose (e.g., B-F1-R1 at 7.45 hr⁻¹) vastly outperformed those relying on glycerol (B-F2-R1 at 4.28 hr⁻¹ and B-F6-R1 at 3.75 hr⁻¹). *V. natriegens* exhibits extreme carbon catabolite repression and prioritizes glucose, which fuels its rapid central carbon metabolism.
2. **Rich Supplementation is Highly Effective:** The Semi-Defined medium supplemented with extra Yeast Extract and Tryptone (B-F5-R1) achieved an exceptional growth rate of 6.84 hr⁻¹, proving that a defined baseline can rival purely complex media when heavily supplemented with amino acids and vitamins.
3. **Magnesium is Critical:** The top-performing formulation (B-F1-R1) included supplemental MgSO₄. *V. natriegens* possesses an unusually high number of ribosomes to sustain its rapid doubling time, and high intracellular Mg²⁺ is required for ribosomal stability and ATP-dependent enzyme function (Hoffart et al., 2017).

## Base Media Selection for Round 2

**Included Base Media:**
- **Media 2 (LBv2, pH 7.0):** Retained as the primary scaffold. It produced the highest growth rate in Round 1 when supplemented with Glucose and Mg²⁺.
- **Media 4 (Semi-Defined, pH 7.0):** Retained because it performed exceptionally well when supplemented with rich components, offering a cleaner background than LBv2.
- **Media 1 (NBxCyclone, pH 6.4):** Retained to test if replacing citrate with glucose can unlock its high-yeast-extract potential while maintaining Fe²⁺ solubility.
- **Media 5 (High Buffer Defined, pH 7.0):** Introduced to test if the high growth rates seen in the Semi-Defined medium (Media 4) can be further extended by preventing late-stage pH drift with a massive 100 mM MOPS buffer capacity.

**Excluded Base Media:**
- **Media 3 (Defined Minimal) & Media 6 (Defined Glycerol):** Excluded. Purely defined media and glycerol-based carbon sources have proven too slow for maximizing absolute growth rate in this organism.

---

## Formulations & Constraint Checks

### 1. Elnora-LBv2-Glc-Mg-YE
* **Rationale:** Builds on the best Round 1 formulation (LBv2 + Glc + Mg) by adding extra Yeast Extract. This provides an overabundance of B-vitamins and trace nutrients to ensure no micronutrient becomes rate-limiting during exponential growth.
* **Composition:** 155 µL Media 2 + 10 µL MOPS (1 M) + 10 µL Glucose (100 mg/mL) + 5 µL MgSO₄ (100 mM) + 10 µL Yeast Extract (100 mg/mL). Total = 190 µL.
* **Constraint Checks:**
  * **Buffer:** Added MOPS = `(1000 * 10) / 190 = 52.63 mM`. (Valid: ≥ 40 mM).
  * **NaCl:** Base has 375 mM. Final = `(375 * 155) / 190 = 305.92 mM`. (Valid: 100-500 mM).
  * **Osmolarity:** Base contribution = `(760 * 155) / 190 = 620 mOsm`. Added MOPS = 52.63. Added MgSO₄ = `(100 * 5 / 190) * 2 = 5.26`. Total = 677.89 mOsm. (Valid: ≤ 1200 mOsm).
  * **Precipitation:** No phosphate in LBv2. (Valid).
  * **Pipetting:** All additions ≥ 5 µL. (Valid).

### 2. Elnora-SemiDef-Glc-Rich
* **Rationale:** Takes the highly successful Semi-Defined + Rich formulation from Round 1 and adds Glucose. This combines the best carbon source with the best amino acid supplementation strategy.
* **Composition:** 155 µL Media 4 + 5 µL MOPS (1 M) + 10 µL Yeast Extract (100 mg/mL) + 10 µL Tryptone (100 mg/mL) + 10 µL Glucose (100 mg/mL). Total = 190 µL.
* **Constraint Checks:**
  * **Buffer:** Base has 40 mM MOPS. Final from base = `(40 * 155) / 190 = 32.63 mM`. Added MOPS = `(1000 * 5) / 190 = 26.32 mM`. Total = 58.95 mM. (Valid: ≥ 40 mM).
  * **NaCl:** Base has 275 mM. Final = `(275 * 155) / 190 = 224.34 mM`. (Valid: 100-500 mM).
  * **Osmolarity:** Base = `(650 * 155) / 190 = 530.26 mOsm`. Added MOPS = 26.32. Total = 556.58 mOsm. (Valid: ≤ 1200 mOsm).
  * **Precipitation:** Base has 5 mM phosphate and 1 mM Mg. Final Phosphate = `(5 * 155) / 190 = 4.08 mM`. Final Mg = `(1 * 155) / 190 = 0.82 mM`. (Valid).
  * **Pipetting:** All additions ≥ 5 µL. (Valid).

### 3. Elnora-LBv2-Glc-Ca
* **Rationale:** Tests if Ca²⁺ supplementation is beneficial when paired with the optimal carbon source (Glucose). Ca²⁺ is critical for outer membrane stability in marine vibrios, which may be stressed during ultra-fast division.
* **Composition:** 165 µL Media 2 + 10 µL MOPS (1 M) + 10 µL Glucose (100 mg/mL) + 5 µL CaCl₂ (100 mM). Total = 190 µL.
* **Constraint Checks:**
  * **Buffer:** Added MOPS = 52.63 mM. (Valid: ≥ 40 mM).
  * **NaCl:** Base = 325.66 mM. (Valid: 100-500 mM).
  * **Osmolarity:** Base = 660 mOsm. Added MOPS = 52.63. Added CaCl₂ = `(100 * 5 / 190) * 2 = 5.26`. Total = 717.89 mOsm. (Valid: ≤ 1200 mOsm).
  * **Precipitation:** No phosphate in LBv2. Ca²⁺ addition is permitted. (Valid).
  * **Pipetting:** All additions ≥ 5 µL. (Valid).

### 4. Elnora-NBx-Glc-Fe
* **Rationale:** Leverages the pH 6.4 of Media 1 to safely supplement Iron(II), but replaces the suboptimal citrate from Round 1 with Glucose to drive faster central metabolism.
* **Composition:** 165 µL Media 1 + 10 µL MOPS (1 M) + 5 µL Iron(II) Sulfate Heptahydrate (1 mM) + 10 µL Glucose (100 mg/mL). Total = 190 µL.
* **Constraint Checks:**
  * **Buffer:** Added MOPS = 52.63 mM. Tris from base = `(150 * 165) / 190 = 130.26 mM`. Total buffer = 182.89 mM. (Valid: ≥ 40 mM).
  * **NaCl:** Base has 385 mM. Final = `(385 * 165) / 190 = 334.34 mM`. (Valid: 100-500 mM).
  * **Osmolarity:** Base = `(950 * 165) / 190 = 825 mOsm`. Added MOPS = 52.63. Total = 877.63 mOsm. (Valid: ≤ 1200 mOsm).
  * **Precipitation:** Base has 17.2 mM phosphate and 4 mM Mg. Final Phosphate = `(17.2 * 165) / 190 = 14.94 mM`. Final Mg = `(4 * 165) / 190 = 3.47 mM`. Both are within limits. Fe²⁺ is allowed because base is Media 1. (Valid).
  * **Pipetting:** All additions ≥ 5 µL. (Valid).

### 5. Elnora-HighBuf-Rich
* **Rationale:** Tests if the high growth rates seen in the Semi-Defined medium can be further extended by preventing late-stage pH drift. Uses Media 5 (100 mM MOPS) supplemented with Yeast Extract, Tryptone, and Glucose.
* **Composition:** 160 µL Media 5 + 10 µL Yeast Extract (100 mg/mL) + 10 µL Tryptone (100 mg/mL) + 10 µL Glucose (100 mg/mL). Total = 190 µL.
* **Constraint Checks:**
  * **Buffer:** Base has 100 mM MOPS. Final = `(100 * 160) / 190 = 84.21 mM`. (Valid: ≥ 40 mM).
  * **NaCl:** Base has 275 mM. Final = `(275 * 160) / 190 = 231.58 mM`. (Valid: 100-500 mM).
  * **Osmolarity:** Base = `(750 * 160) / 190 = 631.58 mOsm`. Total = 631.58 mOsm. (Valid: ≤ 1200 mOsm).
  * **Precipitation:** Base has 5 mM phosphate and 1 mM Mg. Final Phosphate = `(5 * 160) / 190 = 4.21 mM`. Final Mg = `(1 * 160) / 190 = 0.84 mM`. (Valid).
  * **Pipetting:** All additions ≥ 5 µL. (Valid).

### 6. Elnora-LBv2-Glc-KCl
* **Rationale:** *V. natriegens* requires high intracellular potassium for optimal ribosomal function and protein synthesis. This formulation tests if additional K⁺ (via KCl) boosts growth when paired with Glucose in LBv2.
* **Composition:** 160 µL Media 2 + 10 µL MOPS (1 M) + 10 µL Glucose (100 mg/mL) + 10 µL KCl (200 mM). Total = 190 µL.
* **Constraint Checks:**
  * **Buffer:** Added MOPS = 52.63 mM. (Valid: ≥ 40 mM).
  * **NaCl:** Base = `(375 * 160) / 190 = 315.79 mM`. (Valid: 100-500 mM).
  * **Osmolarity:** Base = `(760 * 160) / 190 = 640 mOsm`. Added MOPS = 52.63. Added KCl = `(200 * 10 / 190) * 2 = 21.05`. Total = 713.68 mOsm. (Valid: ≤ 1200 mOsm).
  * **Pipetting:** All additions ≥ 5 µL. (Valid).
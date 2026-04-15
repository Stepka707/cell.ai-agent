# Vibrio natriegens Media Optimization - Round 1 Reasoning & Calculations

## Base Media Selection & Rationale

*Vibrio natriegens* is a marine bacterium known for its exceptionally rapid growth rate (doubling time ~14 minutes under optimal conditions). Literature (e.g., Lee et al., 2016; Weinstock et al., 2016) demonstrates that *V. natriegens* thrives in extremely rich, high-osmolarity media (such as LB3 or BHI v2) and requires high sodium concentrations. 

**Selected Base Media:**
1. **Media 1 (NBxCyclone, pH 6.4):** Selected because it is the richest available medium. Its high yeast extract and tryptone content provide abundant amino acids and vitamins necessary for maximum biomass accumulation. It is also the only medium where Fe²⁺ addition is permitted, allowing us to test iron-stimulated respiratory growth.
2. **Media 2 (LBv2, pH 7.0):** Selected as a standard, highly validated rich medium for *V. natriegens*. It lacks phosphate, which uniquely allows us to test calcium supplementation (Ca²⁺ stabilizes the outer membrane during rapid division).
3. **Media 4 (Semi-Defined, pH 7.0):** Selected to test if a defined base with targeted rich spikes (yeast extract/tryptone) can compete with purely complex media while offering better metabolic control and less batch-to-batch variability.

**Excluded Base Media:**
*   **Media 3, 5, and 6 (Defined Minimal/Glycerol):** Excluded for Round 1. While useful for metabolic flux studies, minimal media inherently bottleneck *V. natriegens* growth rates compared to rich media due to the metabolic burden of synthesizing all amino acids de novo. Our primary objective is maximizing absolute growth rate.

---

## Formulation Designs & Constraint Checks

*General Constraints:* Total Volume = 190 µL. Minimum pipetting volume = 5 µL.

### Formulation 1: Elnora-NBx-Fe-Boost
**Rationale:** Media 1 is extremely rich. *V. natriegens* has high iron requirements for rapid respiration (cytochromes) during exponential growth. We are adding Fe²⁺ since Media 1 is the only base where it is permitted (pH 6.4). MOPS is added to satisfy the buffer constraint.
*   **Base:** Media 1 (NBxCyclone) - 160 µL
*   **MOPS (1 M stock):** Target 40 mM final. Volume = (40 * 190) / 1000 = 7.6 µL
*   **Iron(II) Sulfate (1 mM stock):** Target 0.05 mM final. Volume = (0.05 * 190) / 1 = 9.5 µL
*   **Sterile H₂O:** 190 - 160 - 7.6 - 9.5 = 12.9 µL
*   **Constraint Checks:**
    *   *Dilution Factor:* 160 / 190 = 0.842
    *   *Pipetting:* All volumes ≥ 5 µL. (Pass)
    *   *Buffer:* Base Tris (150 * 0.842 = 126.3 mM) + Added MOPS (40 mM). Total buffer = 166.3 mM ≥ 40 mM. MOPS is ≥ 40 mM, validating Tris contribution. (Pass)
    *   *Solubility:* Base PO₄ (17.2 * 0.842 = 14.48 mM) ≤ 20 mM. Base Mg²⁺ (4 * 0.842 = 3.37 mM) ≤ 5 mM. Fe²⁺ = 0.05 mM ≤ 1 mM. (Pass)
    *   *NaCl:* Base NaCl (385 * 0.842 = 324 mM). Range 100-500 mM. (Pass)
    *   *Osmolarity:* (324*2) + (3.37*2) + (14.48*2) + (40*1) + (126.3*1) = 648 + 6.74 + 28.96 + 40 + 126.3 = 850 mOsm ≤ 1200 mOsm. (Pass)

### Formulation 2: Elnora-LBv2-Ca-Rich
**Rationale:** LBv2 is a standard rich medium. *V. natriegens* benefits from Ca²⁺ for membrane stability at high growth rates. Media 2 is the only base without PO₄, allowing Ca²⁺ addition without precipitation. Glucose is added for an immediate carbon burst.
*   **Base:** Media 2 (LBv2) - 150 µL
*   **MOPS (1 M stock):** Target 50 mM final. Volume = (50 * 190) / 1000 = 9.5 µL
*   **CaCl₂ (100 mM stock):** Target 5 mM final. Volume = (5 * 190) / 100 = 9.5 µL
*   **Glucose (100 mg/mL stock):** Target 5 mg/mL final. Volume = (5 * 190) / 100 = 9.5 µL
*   **Sterile H₂O:** 190 - 150 - 9.5 - 9.5 - 9.5 = 11.5 µL
*   **Constraint Checks:**
    *   *Dilution Factor:* 150 / 190 = 0.789
    *   *Pipetting:* All volumes ≥ 5 µL. (Pass)
    *   *Buffer:* Added MOPS = 50 mM ≥ 40 mM. (Pass)
    *   *Solubility:* PO₄ = 0 mM. Ca²⁺ = 5 mM. No Ca/PO4 conflict. (Pass)
    *   *NaCl:* Base NaCl (375 * 0.789 = 296 mM). Range 100-500 mM. (Pass)
    *   *Osmolarity:* (296*2) + (1.58*2) + (3.16*2) + (5*2) + (50*1) = 592 + 3.16 + 6.32 + 10 + 50 = 661.5 mOsm ≤ 1200 mOsm. (Pass)

### Formulation 3: Elnora-LBv2-Osmotic-Max
**Rationale:** Push the osmolarity closer to the 1200 mOsm limit using NaCl and Glutamate, mimicking the marine environment of *V. natriegens* to maximize growth rate (Hoffart et al., 2017). Glutamate serves as both an osmoprotectant and a premium carbon/nitrogen source.
*   **Base:** Media 2 (LBv2) - 140 µL
*   **MOPS (1 M stock):** Target 50 mM final. Volume = (50 * 190) / 1000 = 9.5 µL
*   **NaCl (5 M stock):** Target 150 mM final. Volume = (150 * 190) / 5000 = 5.7 µL
*   **Sodium L-Glutamate (1 M stock):** Target 50 mM final. Volume = (50 * 190) / 1000 = 9.5 µL
*   **Sterile H₂O:** 190 - 140 - 9.5 - 5.7 - 9.5 = 25.3 µL
*   **Constraint Checks:**
    *   *Dilution Factor:* 140 / 190 = 0.737
    *   *Pipetting:* All volumes ≥ 5 µL. (Pass)
    *   *Buffer:* Added MOPS = 50 mM ≥ 40 mM. (Pass)
    *   *NaCl:* Base NaCl (375 * 0.737 = 276.4 mM) + Added NaCl (150 mM) = 426.4 mM. Range 100-500 mM. (Pass)
    *   *Osmolarity:* (426.4*2) + (1.47*2) + (2.95*2) + (50*1) + (50*1) = 852.8 + 2.94 + 5.9 + 50 + 50 = 961.6 mOsm ≤ 1200 mOsm. (Pass)

### Formulation 4: Elnora-SemiDef-Carbon-Boost
**Rationale:** Semi-defined media provides a controlled baseline. Supplementing with extra carbon (Glycerol) and Yeast Extract bridges the gap between defined and rich media, supporting rapid biomass accumulation while preventing the rapid pH crash often seen in purely complex media.
*   **Base:** Media 4 (Semi-Defined) - 150 µL
*   **Yeast Extract (100 mg/mL stock):** Target 5 mg/mL final. Volume = (5 * 190) / 100 = 9.5 µL
*   **Glycerol (10% stock):** Target 0.5% final. Volume = (0.5 * 190) / 10 = 9.5 µL
*   **MOPS (1 M stock):** Target 30 mM final. Volume = (30 * 190) / 1000 = 5.7 µL
*   **Sterile H₂O:** 190 - 150 - 9.5 - 9.5 - 5.7 = 15.3 µL
*   **Constraint Checks:**
    *   *Dilution Factor:* 150 / 190 = 0.789
    *   *Pipetting:* All volumes ≥ 5 µL. (Pass)
    *   *Buffer:* Base MOPS (40 * 0.789 = 31.5 mM) + Added MOPS (30 mM) = 61.5 mM ≥ 40 mM. (Pass)
    *   *Solubility:* Base PO₄ (5 * 0.789 = 3.95 mM) ≤ 20 mM. Base Mg²⁺ (1 * 0.789 = 0.79 mM) ≤ 5 mM. (Pass)
    *   *NaCl:* Base NaCl (275 * 0.789 = 217 mM). Range 100-500 mM. (Pass)
    *   *Osmolarity:* (217*2) + (0.79*2) + (3.16*2) + (0.79*2) + (7.89*3) + (61.5*1) = 434 + 1.58 + 6.32 + 1.58 + 23.67 + 61.5 = 528.6 mOsm ≤ 1200 mOsm. (Pass)

### Formulation 5: Elnora-NBx-Citrate-Carbon
**Rationale:** *V. natriegens* can utilize citrate as a carbon source and chelator. Adding Sodium Citrate to NBxCyclone provides an alternative TCA cycle intermediate, potentially bypassing glycolysis bottlenecks during peak exponential growth.
*   **Base:** Media 1 (NBxCyclone) - 150 µL
*   **MOPS (1 M stock):** Target 50 mM final. Volume = (50 * 190) / 1000 = 9.5 µL
*   **Sodium Citrate (100 mM stock):** Target 5 mM final. Volume = (5 * 190) / 100 = 9.5 µL
*   **Sterile H₂O:** 190 - 150 - 9.5 - 9.5 = 21.0 µL
*   **Constraint Checks:**
    *   *Dilution Factor:* 150 / 190 = 0.789
    *   *Pipetting:* All volumes ≥ 5 µL. (Pass)
    *   *Buffer:* Base Tris (150 * 0.789 = 118.35 mM) + Added MOPS (50 mM). Total = 168.35 mM. MOPS is ≥ 40 mM. (Pass)
    *   *Solubility:* Base PO₄ (17.2 * 0.789 = 13.57 mM) ≤ 20 mM. Base Mg²⁺ (4 * 0.789 = 3.16 mM) ≤ 5 mM. (Pass)
    *   *NaCl:* Base NaCl (385 * 0.789 = 303.8 mM). Range 100-500 mM. (Pass)
    *   *Osmolarity:* (303.8*2) + (3.16*2) + (13.57*2) + (50*1) + (118.35*1) + (5*1) = 607.6 + 6.32 + 27.14 + 50 + 118.35 + 5 = 814.4 mOsm ≤ 1200 mOsm. (Pass)

### Formulation 6: Elnora-LBv2-Phosphate-Spike
**Rationale:** LBv2 lacks phosphate, which is essential for ATP and nucleic acid synthesis during exponential growth. Adding a controlled amount of K₂HPO₄ and KH₂PO₄ prevents phosphate depletion, while strictly adhering to the Mg²⁺/PO₄ solubility limits to avoid precipitation.
*   **Base:** Media 2 (LBv2) - 140 µL
*   **MOPS (1 M stock):** Target 50 mM final. Volume = (50 * 190) / 1000 = 9.5 µL
*   **K₂HPO₄ (50 mM stock):** Target 5 mM final. Volume = (5 * 190) / 50 = 19.0 µL
*   **KH₂PO₄ (100 mM stock):** Target 3 mM final. Volume = (3 * 190) / 100 = 5.7 µL
*   **Sterile H₂O:** 190 - 140 - 9.5 - 19.0 - 5.7 = 15.8 µL
*   **Constraint Checks:**
    *   *Dilution Factor:* 140 / 190 = 0.737
    *   *Pipetting:* All volumes ≥ 5 µL. (Pass)
    *   *Buffer:* Added MOPS = 50 mM ≥ 40 mM. (Pass)
    *   *Solubility:* Added PO₄ = 8 mM ≤ 20 mM. Base Mg²⁺ (2 * 0.737 = 1.47 mM) ≤ 5 mM. (Pass)
    *   *NaCl:* Base NaCl (375 * 0.737 = 276.4 mM). Range 100-500 mM. (Pass)
    *   *Osmolarity:* (276.4*2) + (1.47*2) + (2.95*2) + (5*2) + (3*2) + (50*1) = 552.8 + 2.94 + 5.9 + 10 + 6 + 50 = 627.6 mOsm ≤ 1200 mOsm. (Pass)
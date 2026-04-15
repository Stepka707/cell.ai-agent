# Vibrio natriegens Media Optimization - Round 1

## Literature & Base Media Selection
*Vibrio natriegens* is a fast-growing marine bacterium known for its exceptionally short generation time (doubling time ~21 mins under optimal conditions). It requires high sodium concentrations (typically 200-400 mM) and thrives in rich, highly buffered media. Recent literature indicates that optimal growth is achieved with high osmolality (1.0-1.6 Osmol/kg) and robust buffering (e.g., MOPS) to counteract rapid acidification during exponential growth.

**Selected Base Media:**
1. **Media 2 (LBv2):** LB is a standard rich medium, but LBv2 is optimized with higher salt (375 mM NaCl) which is ideal for *V. natriegens*. It lacks buffer, so MOPS must be added.
2. **Media 1 (NBxCyclone):** A very rich, complex medium with high yeast extract and tryptone. It has a lower pH (6.4) which allows for the addition of Fe2+ to support rapid respiratory growth. It requires MOPS supplementation to maintain buffering capacity across the growth curve, as Tris provides no buffering at this pH.
3. **Media 4 (Semi-Defined):** Provides a balance of defined carbon/nitrogen sources with a small amount of complex nutrients (tryptone/yeast extract). This is an excellent baseline to test specific metabolic additions like extra carbon sources or specific salts.

**Excluded Base Media:**
- **Media 3 (Defined Minimal) & Media 6 (Defined Glycerol):** Excluded for Round 1 because minimal media typically result in significantly slower growth rates compared to rich or semi-defined media. We want to maximize growth rate first.
- **Media 5 (High Buffer Defined):** Excluded in favor of Media 4, as we can manually adjust the buffer in Media 4 while testing other complex additives.

---

## Formulations & Constraint Checks

### Formulation 1: LBv2-MOPS-Glc-Ca
**Rationale:** LBv2 provides a strong baseline. We add 50 mM MOPS to satisfy the buffer requirement. Glucose (5 mg/mL) is added as a preferred, rapidly metabolizable carbon source. Calcium (3 mM) is added to support cell envelope stability, which is permissible here since LBv2 contains no phosphate.
**Constraint Checks:**
- **Volume:** Base (165.3 µL) + MOPS (9.5 µL) + Glucose (9.5 µL) + CaCl2 (5.7 µL) = 190 µL. All pipetting volumes ≥ 5 µL.
- **Buffer:** 50 mM MOPS added (≥ 40 mM required).
- **Osmolarity:** Base (~760) + MOPS (50) + CaCl2 (6) = ~816 mOsm (≤ 1200 mOsm).
- **NaCl:** 375 mM * (165.3/190) = 326.25 mM (within 100-500 mM).
- **Precipitation:** No phosphate present, so Ca2+ addition is safe. Mg2+ is 1.74 mM.

### Formulation 2: LBv2-MOPS-Gly-Glu
**Rationale:** Tests an alternative carbon/nitrogen supplementation strategy on the LBv2 base. Glycerol (0.5%) provides a non-fermentable carbon source that may reduce rapid acidification compared to glucose. Sodium L-Glutamate (30 mM) acts as both an osmoprotectant and a readily usable nitrogen/carbon source.
**Constraint Checks:**
- **Volume:** Base (165.3 µL) + MOPS (9.5 µL) + Glycerol (9.5 µL) + Na-Glutamate (5.7 µL) = 190 µL. All pipetting volumes ≥ 5 µL.
- **Buffer:** 50 mM MOPS added (≥ 40 mM required).
- **Osmolarity:** Base (~760) + MOPS (50) + Na-Glutamate (30) = ~840 mOsm (≤ 1200 mOsm).
- **NaCl:** 326.25 mM (within 100-500 mM).
- **Precipitation:** No phosphate present.

### Formulation 3: NBx-MOPS-Fe-Glc
**Rationale:** NBxCyclone is extremely rich. The pH of 6.4 allows us to supplement with Fe2+ (0.05 mM) to boost respiratory enzyme activity (e.g., cytochromes) for faster growth. Glucose is added to ensure carbon is not limiting. MOPS is added because Tris does not buffer at pH 6.4.
**Constraint Checks:**
- **Volume:** Base (161.5 µL) + MOPS (9.5 µL) + FeSO4 (9.5 µL) + Glucose (9.5 µL) = 190 µL. All pipetting volumes ≥ 5 µL.
- **Buffer:** 50 mM MOPS added. Total buffer = 50 mM MOPS + 127.5 mM Tris = 177.5 mM (≥ 40 mM required).
- **Osmolarity:** Base (~950) + MOPS (50) = ~1000 mOsm (≤ 1200 mOsm).
- **NaCl:** 385 mM * (161.5/190) = 327.25 mM (within 100-500 mM).
- **Precipitation:** Phosphate = 17.2 * 0.85 = 14.62 mM (≤ 20 mM). Mg2+ = 4 * 0.85 = 3.4 mM (≤ 5 mM). Fe2+ = 0.05 mM (≤ 1 mM, allowed at pH 6.4).

### Formulation 4: NBx-MOPS-Fe-Cit
**Rationale:** Similar to F3, but uses Sodium Citrate (5 mM) instead of glucose. Citrate can act as an iron chelator to keep Fe2+ soluble and bioavailable, while also serving as a TCA cycle intermediate.
**Constraint Checks:**
- **Volume:** Base (165.3 µL) + MOPS (9.5 µL) + FeSO4 (5.7 µL) + Na-Citrate (9.5 µL) = 190 µL. All pipetting volumes ≥ 5 µL.
- **Buffer:** 50 mM MOPS added. Total buffer = 50 mM MOPS + 130.5 mM Tris = 180.5 mM (≥ 40 mM required).
- **Osmolarity:** Base (~950) + MOPS (50) + Na-Citrate (5) = ~1005 mOsm (≤ 1200 mOsm).
- **NaCl:** 385 mM * (165.3/190) = 334.95 mM (within 100-500 mM).
- **Precipitation:** Phosphate = 14.96 mM (≤ 20 mM). Mg2+ = 3.48 mM (≤ 5 mM). Fe2+ = 0.03 mM (≤ 1 mM, allowed at pH 6.4).

### Formulation 5: SemiDef-MOPS-YE-Tryp
**Rationale:** Media 4 (Semi-Defined) already contains 40 mM MOPS, but dilution with additives drops it below the 40 mM threshold. We add 30 mM MOPS to ensure robust buffering. We supplement with extra Yeast Extract and Tryptone to push the semi-defined medium closer to a rich medium, testing if the defined baseline + complex spike outperforms purely complex media.
**Constraint Checks:**
- **Volume:** Base (165.3 µL) + MOPS (5.7 µL) + Yeast Extract (9.5 µL) + Tryptone (9.5 µL) = 190 µL. All pipetting volumes ≥ 5 µL.
- **Buffer:** Base MOPS (40 * 0.87 = 34.8 mM) + Added MOPS (30 mM) = 64.8 mM (≥ 40 mM required).
- **Osmolarity:** Base (~650) + MOPS (30) = ~680 mOsm (≤ 1200 mOsm).
- **NaCl:** 275 mM * (165.3/190) = 239.25 mM (within 100-500 mM).
- **Precipitation:** Phosphate = 5 * 0.87 = 4.35 mM (≤ 20 mM). Mg2+ = 1 * 0.87 = 0.87 mM (≤ 5 mM).

### Formulation 6: SemiDef-MOPS-Gly-KCl
**Rationale:** Tests the Semi-Defined base with Glycerol (0.5%) instead of extra complex nitrogen. We also add KCl (10 mM) to provide additional potassium, which is often beneficial for halophilic organisms like *V. natriegens* to maintain intracellular turgor pressure.
**Constraint Checks:**
- **Volume:** Base (165.3 µL) + MOPS (5.7 µL) + Glycerol (9.5 µL) + KCl (9.5 µL) = 190 µL. All pipetting volumes ≥ 5 µL.
- **Buffer:** Base MOPS (34.8 mM) + Added MOPS (30 mM) = 64.8 mM (≥ 40 mM required).
- **Osmolarity:** Base (~650) + MOPS (30) + KCl (20) = ~700 mOsm (≤ 1200 mOsm).
- **NaCl:** 239.25 mM (within 100-500 mM).
- **Precipitation:** Phosphate = 4.35 mM (≤ 20 mM). Mg2+ = 0.87 mM (≤ 5 mM).
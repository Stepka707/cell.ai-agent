# Vibrio natriegens Media Optimization: Reasoning & Constraint Verification

## Overview
*Vibrio natriegens* is a marine halophile known for its exceptionally fast growth rate. To maximize OD600 kinetics in an unattended Opentrons Flex microplate run, formulations must provide abundant carbon/nitrogen, maintain strict pH stability (≥ 40 mM buffer), and stay within optimal osmolarity (~700–1100 mOsm) and salinity (100–500 mM NaCl) ranges. The following 6 formulations explore distinct metabolic strategies while strictly adhering to all solubility, buffering, and pipetting constraints.

---

## Formulation 1: Semi-Defined Enriched
**Base Medium:** Media 4 (Semi-Defined, pH 7.0)
**Strategy:** Use a balanced semi-defined base and push the maximum growth rate by supplementing extra carbon (Glucose) and an easily assimilated nitrogen/carbon source (Sodium Glutamate). Extra MOPS is added to counter the rapid acidification expected from accelerated glucose metabolism.

### Volume Calculations (Total = 190 µL)
- **Glucose (100 mg/mL):** 5 µL added $\rightarrow$ `(100 * 5) / 190` = 2.63 mg/mL (0.26%)
- **Sodium L-Glutamate (1 M):** 5 µL added $\rightarrow$ `(1000 * 5) / 190` = 26.32 mM
- **MOPS (1 M):** 5 µL added $\rightarrow$ `(1000 * 5) / 190` = 26.32 mM
- **Base Medium 4:** 190 - 15 = 175 µL

### Constraint Checks
- **Solubility (Phosphate/Mg²⁺):** Base contains 5 mM total phosphate and 1 mM Mg²⁺. No additions. 
  - Phosphate ≤ 20 mM? **PASS** (5 mM)
  - Mg²⁺ ≤ 5 mM? **PASS** (1 mM)
- **Solubility (Fe²⁺/Ca²⁺):** None added. **PASS**
- **Salt (NaCl):** Base contains 275 mM. 
  - 100 ≤ NaCl ≤ 500 mM? **PASS** (275 mM)
- **Osmolarity:** Base (650) + Glutamate (26.32 × 1) + MOPS (26.32 × 1) = 702.64 mOsm. 
  - ≤ 1200 mOsm? **PASS**
- **Buffer Capacity:** Base MOPS (40 mM) + Added MOPS (26.32 mM) = 66.32 mM. 
  - ≥ 40 mM? **PASS**
- **Pipetting:** All additions ≥ 5 µL. **PASS**

---

## Formulation 2: High Buffer Defined + Citrate/Glutamate
**Base Medium:** Media 5 (High Buffer Defined, pH 7.0)
**Strategy:** Leverage the high baseline buffer (100 mM MOPS) to support heavy organic acid production. Supplement with Sodium Citrate (TCA cycle intermediate) and Sodium Glutamate to bypass glycolysis bottlenecks. A small addition of Yeast Extract provides trace vitamins to prevent cofactor depletion.

### Volume Calculations (Total = 190 µL)
- **Sodium Citrate (100 mM):** 10 µL added $\rightarrow$ `(100 * 10) / 190` = 5.26 mM
- **Sodium L-Glutamate (1 M):** 10 µL added $\rightarrow$ `(1000 * 10) / 190` = 52.63 mM
- **Yeast Extract (100 mg/mL):** 5 µL added $\rightarrow$ `(100 * 5) / 190` = 2.63 mg/mL
- **Base Medium 5:** 190 - 25 = 165 µL

### Constraint Checks
- **Solubility (Phosphate/Mg²⁺):** Base contains 5 mM phosphate and 1 mM Mg²⁺. 
  - Phosphate ≤ 20 mM? **PASS** (5 mM)
  - Mg²⁺ ≤ 5 mM? **PASS** (1 mM)
- **Solubility (Fe²⁺/Ca²⁺):** None added. **PASS**
- **Salt (NaCl):** Base contains 275 mM. 
  - 100 ≤ NaCl ≤ 500 mM? **PASS** (275 mM)
- **Osmolarity:** Base (750) + Citrate (5.26 × 1) + Glutamate (52.63 × 1) = 807.89 mOsm. 
  - ≤ 1200 mOsm? **PASS**
- **Buffer Capacity:** Base MOPS = 100 mM. 
  - ≥ 40 mM? **PASS**
- **Pipetting:** All additions ≥ 5 µL. **PASS**

---

## Formulation 3: LBv2 + MOPS/Ca/Glc
**Base Medium:** Media 2 (LBv2, pH 7.0)
**Strategy:** LBv2 is a rich complex medium but lacks buffer and phosphate. The lack of phosphate makes this the *only* base where CaCl₂ can be added to test calcium's effect on membrane stability. MOPS is added to satisfy the mandatory buffer constraint, and glucose is added as a primary carbon source.

### Volume Calculations (Total = 190 µL)
- **MOPS (1 M):** 10 µL added $\rightarrow$ `(1000 * 10) / 190` = 52.63 mM
- **CaCl₂ (100 mM):** 5 µL added $\rightarrow$ `(100 * 5) / 190` = 2.63 mM
- **Glucose (100 mg/mL):** 10 µL added $\rightarrow$ `(100 * 10) / 190` = 5.26 mg/mL (0.53%)
- **Base Medium 2:** 190 - 25 = 165 µL

### Constraint Checks
- **Solubility (Phosphate/Mg²⁺):** Base contains 0 mM phosphate and 2 mM Mg²⁺. 
  - Phosphate ≤ 20 mM? **PASS** (0 mM)
- **Solubility (Ca²⁺):** 2.63 mM Ca²⁺ added. Phosphate is 0 mM. 
  - Ca²⁺ and phosphate never together? **PASS**
- **Solubility (Fe²⁺):** None added. **PASS**
- **Salt (NaCl):** Base contains 375 mM. 
  - 100 ≤ NaCl ≤ 500 mM? **PASS** (375 mM)
- **Osmolarity:** Base (760) + MOPS (52.63 × 1) + CaCl₂ (2.63 × 2) = 817.89 mOsm. 
  - ≤ 1200 mOsm? **PASS**
- **Buffer Capacity:** Added MOPS = 52.63 mM. 
  - ≥ 40 mM? **PASS** (Mandatory LBv2 buffer rule satisfied)
- **Pipetting:** All additions ≥ 5 µL. **PASS**

---

## Formulation 4: NBxCyclone + MOPS/Fe/Gly
**Base Medium:** Media 1 (NBxCyclone, pH 6.4)
**Strategy:** NBxCyclone is the only base with a pH ≤ 6.8, making it the exclusive candidate for Fe²⁺ supplementation to boost cytochrome activity. Because Tris provides no buffering at pH 6.4, MOPS co-addition is mandatory. Glycerol is used instead of glucose to prevent rapid, lethal acidification.

### Volume Calculations (Total = 190 µL)
- **MOPS (1 M):** 10 µL added $\rightarrow$ `(1000 * 10) / 190` = 52.63 mM
- **FeSO₄ (1 mM):** 5 µL added $\rightarrow$ `(1 * 5) / 190` = 0.026 mM
- **Glycerol (10%):** 10 µL added $\rightarrow$ `(10 * 10) / 190` = 0.526%
- **Base Medium 1:** 190 - 25 = 165 µL

### Constraint Checks
- **Solubility (Phosphate/Mg²⁺):** Base contains 17.24 mM phosphate and 4 mM Mg²⁺. 
  - Phosphate ≤ 20 mM? **PASS** (17.24 mM)
  - Mg²⁺ ≤ 5 mM? **PASS** (4 mM)
- **Solubility (Fe²⁺):** 0.026 mM Fe²⁺ added. Base pH is 6.4. 
  - Fe²⁺ ≤ 1 mM and pH ≤ 6.8? **PASS**
- **Solubility (Ca²⁺):** None added. **PASS**
- **Salt (NaCl):** Base contains 385.5 mM. 
  - 100 ≤ NaCl ≤ 500 mM? **PASS** (385.5 mM)
- **Osmolarity:** Base (950) + MOPS (52.63 × 1) = 1002.63 mOsm. 
  - ≤ 1200 mOsm? **PASS**
- **Buffer Capacity:** Added MOPS = 52.63 mM. 
  - MOPS ≥ 40 mM for Media 1? **PASS** (Tris rule satisfied)
- **Pipetting:** All additions ≥ 5 µL. **PASS**

---

## Formulation 5: Defined Minimal + Organics/NaCl
**Base Medium:** Media 3 (Defined Minimal, pH 7.0)
**Strategy:** Convert the defined minimal medium into a custom rich medium by adding Tryptone and Yeast Extract. Furthermore, add extra NaCl to push the osmolarity closer to the marine optimum (~900-1000 mOsm) to test if higher salinity improves the baseline growth rate.

### Volume Calculations (Total = 190 µL)
- **Tryptone (100 mg/mL):** 10 µL added $\rightarrow$ `(100 * 10) / 190` = 5.26 mg/mL
- **Yeast Extract (100 mg/mL):** 10 µL added $\rightarrow$ `(100 * 10) / 190` = 5.26 mg/mL
- **NaCl (5 M):** 5 µL added $\rightarrow$ `(5000 * 5) / 190` = 131.58 mM
- **Base Medium 3:** 190 - 25 = 165 µL

### Constraint Checks
- **Solubility (Phosphate/Mg²⁺):** Base contains 5 mM phosphate and 1 mM Mg²⁺. 
  - Phosphate ≤ 20 mM? **PASS** (5 mM)
  - Mg²⁺ ≤ 5 mM? **PASS** (1 mM)
- **Solubility (Fe²⁺/Ca²⁺):** None added. **PASS**
- **Salt (NaCl):** Base (275 mM) + Added (131.58 mM) = 406.58 mM. 
  - 100 ≤ NaCl ≤ 500 mM? **PASS**
- **Osmolarity:** Base (650) + NaCl (131.58 × 2) = 913.16 mOsm. 
  - ≤ 1200 mOsm? **PASS**
- **Buffer Capacity:** Base MOPS = 40 mM. 
  - ≥ 40 mM? **PASS**
- **Pipetting:** All additions ≥ 5 µL. **PASS**

---

## Formulation 6: Defined Glycerol + Glu/KCl/Trace
**Base Medium:** Media 6 (Defined Glycerol, pH 7.0)
**Strategy:** Enhance the defined glycerol base with Sodium Glutamate (dual nitrogen/carbon source), KCl (potassium for osmoregulation), and extra Trace Metals to ensure no enzymatic bottlenecks occur during the peak exponential phase of glycerol metabolism.

### Volume Calculations (Total = 190 µL)
- **Sodium L-Glutamate (1 M):** 10 µL added $\rightarrow$ `(1000 * 10) / 190` = 52.63 mM
- **KCl (200 mM):** 10 µL added $\rightarrow$ `(200 * 10) / 190` = 10.53 mM
- **Trace Metals (10x):** 5 µL added $\rightarrow$ `(10 * 5) / 190` = 0.26x (Total = 1.26x)
- **Base Medium 6:** 190 - 25 = 165 µL

### Constraint Checks
- **Solubility (Phosphate/Mg²⁺):** Base contains 5 mM phosphate and 1 mM Mg²⁺. 
  - Phosphate ≤ 20 mM? **PASS** (5 mM)
  - Mg²⁺ ≤ 5 mM? **PASS** (1 mM)
- **Solubility (Fe²⁺/Ca²⁺):** None added. **PASS**
- **Salt (NaCl):** Base contains 275 mM. 
  - 100 ≤ NaCl ≤ 500 mM? **PASS** (275 mM)
- **Osmolarity:** Base (650) + Glutamate (52.63 × 1) + KCl (10.53 × 2) = 723.69 mOsm. 
  - ≤ 1200 mOsm? **PASS**
- **Buffer Capacity:** Base MOPS = 40 mM. 
  - ≥ 40 mM? **PASS**
- **Pipetting:** All additions ≥ 5 µL. **PASS**
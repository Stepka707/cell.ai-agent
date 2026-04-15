1: 13.58 mM (Mg 3.16) - OK
        *   F2: 0 mM (Mg 1.58) - OK
        *   F3: 3.95 mM (Mg 0.79) - OK
        *   F4: 3.95 mM (Mg 0.79) - OK
        *   F5: 3.95 mM (Mg 0.79) - OK
        *   F6: 3.69 mM (Mg 0.74) - OK
    *   *Mg²⁺ ≤ 5 mM when phosphate is present.*
        *   All Mg²⁺ values are ≤ 3.16 mM. OK.
    *   *Fe²⁺ < 1 mM. Fe²⁺ only in Media 1.*
        *   F1 has 0.053 mM Fe²⁺. Base is Media 1. OK.
    *   *Ca²⁺ and phosphate never together. CaCl₂ only in Media 2.*
        *   F2 has 5.26 mM Ca²⁺. Base is Media 2 (0 phosphate). OK.
    *   *NaCl 100–500 mM.*
        *   F1: 303.9, F2: 296.1, F3: 217.1, F4: 217.1, F```markdown
# Vibrio natriegens Media Optimization Reasoning & Calculations

This document details the design of 6 novel media formulations for automated OD600 kinetics on the Opentrons Flex. All formulations are designed for a fixed 190 µL final well volume, with minimum pipetting volumes of 5 µL.

## Global Constraints Checklist
- **Volume:** Total well volume = 190 µL. Minimum pipettable volume = 5 µL.
- **Phosphate/Mg²⁺:** Combined phosphate ≤ 20 mM when Mg²⁺ is present. Mg²⁺ ≤ 5 mM when phosphate is present.
- **Fe²⁺:** < 1 mM. Only permitted in Media 1 (pH 6.4).
- **Ca²⁺:** Never with phosphate. Only permitted in Media 2 (LBv2).
- **NaCl:** 100–500 mM final.
- **Osmolarity:** ≤ 1200 mOsm.
- **Buffer:** Total MOPS + Tris ≥ 40 mM. Media 1 requires ≥ 40 mM MOPS (Tris insufficient at pH < 7.5). Media 2 requires ≥ 40 mM MOPS.

---

## Formulation 1: NBxCyclone + Iron + MOPS
**Rationale:** Maximize growth using a rich, complex base (Media 1), supplemented with Iron (only permitted in this pH 6.4 base) to support cytochromes, and the mandatory MOPS buffer to maintain pH capacity.

**Volume Breakdown:**
- Base: Media 1 (NBxCyclone) = 150 µL
- Addition 1: MOPS pH 7 (1 M stock) = 10 µL
- Addition 2: Iron(II) Sulfate (1 mM stock) = 10 µL
- Sterile H₂O = 20 µL
- **Total Volume = 190 µL**

**Concentration Calculations (Dilution Factor = 150/190 = 0.7895):**
- Base NaCl: 385 mM × 0.7895 = 303.9 mM
- Base MgSO₄: 4 mM × 0.7895 = 3.16 mM
- Base K₂HPO₄: 17.2 mM × 0.7895 = 13.58 mM
- Base Tris: 150 mM × 0.7895 = 118.4 mM
- Added MOPS: (1000 mM × 10 µL) / 190 µL = 52.6 mM
- Added Fe²⁺: (1 mM × 10 µL) / 190 µL = 0.053 mM

**Constraint Checks:**
- **Min Volume:** 10 µL ≥ 5 µL (PASS)
- **Phosphate:** 13.58 mM ≤ 20 mM (PASS)
- **Mg²⁺:** 3.16 mM ≤ 5 mM (PASS)
- **Fe²⁺:** 0.053 mM < 1 mM, added to Media 1 (PASS)
- **Ca²⁺:** 0 mM (PASS)
- **NaCl:** 303.9 mM is within 100–500 mM (PASS)
- **Buffer:** 52.6 mM MOPS ≥ 40 mM (PASS)
- **Osmolarity:** (303.9×2) + (3.16×2) + (13.58×2) + (118.4×1) + (52.6×1) = 607.8 + 6.32 + 27.16 + 118.4 + 52.6 = **812.28 mOsm** ≤ 1200 (PASS)

---

## Formulation 2: LBv2 + Calcium + MOPS
**Rationale:** Utilize LBv2 (Media 2) to test the effect of Calcium supplementation. Since LBv2 lacks phosphate, it is the only base where CaCl₂ can be safely added without precipitation. Mandatory MOPS is added for buffering.

**Volume Breakdown:**
- Base: Media 2 (LBv2) = 150 µL
- Addition 1: MOPS pH 7 (1 M stock) = 10 µL
- Addition 2: CaCl₂ (100 mM stock) = 10 µL
- Sterile H₂O = 20 µL
- **Total Volume = 190 µL**

**Concentration Calculations (Dilution Factor = 150/190 = 0.7895):**
- Base NaCl: 375 mM × 0.7895 = 296.1 mM
- Base KCl: 4 mM × 0.7895 = 3.16 mM
- Base MgSO₄: 2 mM × 0.7895 = 1.58 mM
- Added MOPS: (1000 mM × 10 µL) / 190 µL = 52.6 mM
- Added CaCl₂: (100 mM × 10 µL) / 190 µL = 5.26 mM

**Constraint Checks:**
- **Min Volume:** 10 µL ≥ 5 µL (PASS)
- **Phosphate:** 0 mM (PASS)
- **Mg²⁺:** 1.58 mM ≤ 5 mM (PASS)
- **Fe²⁺:** 0 mM (PASS)
- **Ca²⁺:** 5.26 mM, added to Media 2 (no phosphate) (PASS)
- **NaCl:** 296.1 mM is within 100–500 mM (PASS)
- **Buffer:** 52.6 mM MOPS ≥ 40 mM (PASS)
- **Osmolarity:** (296.1×2) + (1.58×2) + (3.16×2) + (5.26×2) + (52.6×1) = 592.2 + 3.16 + 6.32 + 10.52 + 52.6 = **664.8 mOsm** ≤ 1200 (PASS)

---

## Formulation 3: Semi-Defined + Glycerol + Glutamate
**Rationale:** Boost the Semi-Defined base (Media 4) with additional carbon (glycerol) and an amino acid/osmolyte source (Sodium L-Glutamate) to accelerate exponential phase growth.

**Volume Breakdown:**
- Base: Media 4 (Semi-Defined) = 150 µL
- Addition 1: MOPS pH 7 (1 M stock) = 5 µL
- Addition 2: Glycerol (10% stock) = 10 µL
- Addition 3: Sodium L-Glutamate (1 M stock) = 10 µL
- Sterile H₂O = 15 µL
- **Total Volume = 190 µL**

**Concentration Calculations (Dilution Factor = 150/190 = 0.7895):**
- Base NaCl: 275 mM × 0.7895 = 217.1 mM
- Base MOPS: 40 mM × 0.7895 = 31.58 mM
- Base K₂HPO₄: 4 mM × 0.7895 = 3.16 mM
- Base KH₂PO₄: 1 mM × 0.7895 = 0.79 mM
- Base (NH₄)₂SO₄: 10 mM × 0.7895 = 7.9 mM
- Base MgSO₄: 1 mM × 0.7895 = 0.79 mM
- Added MOPS: (1000 mM × 5 µL) / 190 µL = 26.3 mM (Total MOPS = 57.88 mM)
- Added Glutamate: (1000 mM × 10 µL) / 190 µL = 52.6 mM

**Constraint Checks:**
- **Min Volume:** 5 µL ≥ 5 µL (PASS)
- **Phosphate:** 3.16 + 0.79 = 3.95 mM ≤ 20 mM (PASS)
- **Mg²⁺:** 0.79 mM ≤ 5 mM (PASS)
- **Fe²⁺:** 0 mM (PASS)
- **Ca²⁺:** 0 mM (PASS)
- **NaCl:** 217.1 mM is within 100–500 mM (PASS)
- **Buffer:** 57.88 mM MOPS ≥ 40 mM (PASS)
- **Osmolarity:** (217.1×2) + (0.79×2) + (3.16×2) + (0.79×2) + (7.9×3) + (57.88×1) + (52.6×1) = 434.2 + 1.58 + 6.32 + 1.58 + 23.7 + 57.88 + 52.6 = **577.86 mOsm** ≤ 1200 (PASS)

---

## Formulation 4: High Buffer Defined + Yeast Extract + Citrate
**Rationale:** Use the High Buffer Defined base (Media 5) to ensure absolute pH stability, supplementing with complex nutrients (Yeast Extract) and Sodium Citrate as a chelator/TCA cycle intermediate.

**Volume Breakdown:**
- Base: Media 5 (High Buffer Defined) = 150 µL
- Addition 1: Yeast Extract (100 mg/mL stock) = 10 µL
- Addition 2: Sodium Citrate (100 mM stock) = 10 µL
- Sterile H₂O = 20 µL
- **Total Volume = 190 µL**

**Concentration Calculations (Dilution Factor = 150/190 = 0.7895):**
- Base NaCl: 275 mM × 0.7895 = 217.1 mM
- Base MOPS: 100 mM × 0.7895 = 78.95 mM
- Base K₂HPO₄: 4 mM × 0.7895 = 3.16 mM
- Base KH₂PO₄: 1 mM × 0.7895 = 0.79 mM
- Base (NH₄)₂SO₄: 20 mM × 0.7895 = 15.79 mM
- Base MgSO₄: 1 mM × 0.7895 = 0.79 mM
- Added Citrate: (100 mM × 10 µL) / 190 µL = 5.26 mM

**Constraint Checks:**
- **Min Volume:** 10 µL ≥ 5 µL (PASS)
- **Phosphate:** 3.16 + 0.79 = 3.95 mM ≤ 20 mM (PASS)
- **Mg²⁺:** 0.79 mM ≤ 5 mM (PASS)
- **Fe²⁺:** 0 mM (PASS)
- **Ca²⁺:** 0 mM (PASS)
- **NaCl:** 217.1 mM is within 100–500 mM (PASS)
- **Buffer:** 78.95 mM MOPS ≥ 40 mM (PASS)
- **Osmolarity:** (217.1×2) + (0.79×2) + (3.16×2) + (0.79×2) + (15.79×3) + (78.95×1) + (5.26×1) = 434.2 + 1.58 + 6.32 + 1.58 + 47.37 + 78.95 + 5.26 = **575.26 mOsm** ≤ 1200 (PASS)

---

## Formulation 5: Defined Minimal + Tryptone + Extra NaCl
**Rationale:** Take the Defined Minimal base (Media 3) and push the osmolarity higher with extra NaCl, as *V. natriegens* is a marine organism that often exhibits enhanced growth rates at higher salinities. Tryptone provides amino acids.

**Volume Breakdown:**
- Base: Media 3 (Defined Minimal) = 150 µL
- Addition 1: MOPS pH 7 (1 M stock) = 5 µL
- Addition 2: Tryptone (100
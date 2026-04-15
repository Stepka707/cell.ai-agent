# Vibrio natriegens Media Optimization - Formulation Design

This document details 6 novel media formulations designed to maximize *Vibrio natriegens* growth rate in an automated Opentrons Flex microplate assay. All formulations have been rigorously validated against the operational constraints.

## F1: Enhanced Semi-Defined
**Strategy**: Enhance Semi-Defined media with additional carbon (glucose) and nitrogen (glutamate) sources, plus a trace metals boost to support rapid exponential growth.

**Composition**:
- Base Medium: Semi-Defined (175 µL)
- Glucose: 5 µL (Final: 2.63)
- Sodium L-Glutamate: 5 µL (Final: 26.32)
- Trace metals: 5 µL (Final: 0.26)
- Sterile H₂O: 0 µL

**Constraint Validation**:
- **Phosphate & Mg2+**: Total Phosphate = 5.00 mM, Total Mg2+ = 1.00 mM. PASS
- **Iron (Fe2+)**: Total Fe2+ = 0.000 mM. Base pH = 7.0. PASS
- **Calcium & Phosphate**: Total Ca2+ = 0.00 mM, Total Phosphate = 5.00 mM. PASS
- **NaCl**: Total NaCl = 275.00 mM. PASS
- **Osmolarity**: Total Estimated Osmolarity = 658.32 mOsm. PASS
- **Buffer Capacity**: Total MOPS = 40.00 mM, Total Tris = 0.00 mM. PASS
- **Pipetting Volume**: All additions >= 5 µL. Total volume = 190 µL. PASS

---

## F2: Buffered LBv2 with Carbon/Nitrogen
**Strategy**: Upgrade rich LBv2 media by adding mandatory MOPS buffer to prevent pH drift, supplementing with glucose and glutamate for energy, and adding CaCl2 (permitted since LBv2 lacks phosphate) to support cell envelope stability.

**Composition**:
- Base Medium: LBv2 (160 µL)
- MOPS pH 7: 10 µL (Final: 52.63)
- Glucose: 5 µL (Final: 2.63)
- Sodium L-Glutamate: 10 µL (Final: 52.63)
- CaCl2: 5 µL (Final: 2.63)
- Sterile H₂O: 0 µL

**Constraint Validation**:
- **Phosphate & Mg2+**: Total Phosphate = 0.00 mM, Total Mg2+ = 2.00 mM. PASS
- **Iron (Fe2+)**: Total Fe2+ = 0.000 mM. Base pH = 7.0. PASS
- **Calcium & Phosphate**: Total Ca2+ = 2.63 mM, Total Phosphate = 0.00 mM. PASS
- **NaCl**: Total NaCl = 375.00 mM. PASS
- **Osmolarity**: Total Estimated Osmolarity = 872.53 mOsm. PASS
- **Buffer Capacity**: Total MOPS = 52.63 mM, Total Tris = 0.00 mM. PASS
- **Pipetting Volume**: All additions >= 5 µL. Total volume = 190 µL. PASS

---

## F3: Buffered NBxCyclone with Iron
**Strategy**: Utilize NBxCyclone (pH 6.4) to allow Fe2+ supplementation. Mandatory MOPS co-addition ensures buffering across the 6.0-7.5 range where Tris is ineffective. Glucose and trace metals provide additional growth factors.

**Composition**:
- Base Medium: NBxCyclone (165 µL)
- MOPS pH 7: 10 µL (Final: 52.63)
- FeSO4: 5 µL (Final: 0.03)
- Glucose: 5 µL (Final: 2.63)
- Trace metals: 5 µL (Final: 0.26)
- Sterile H₂O: 0 µL

**Constraint Validation**:
- **Phosphate & Mg2+**: Total Phosphate = 17.24 mM, Total Mg2+ = 4.00 mM. PASS
- **Iron (Fe2+)**: Total Fe2+ = 0.026 mM. Base pH = 6.4. PASS
- **Calcium & Phosphate**: Total Ca2+ = 0.00 mM, Total Phosphate = 17.24 mM. PASS
- **NaCl**: Total NaCl = 385.00 mM. PASS
- **Osmolarity**: Total Estimated Osmolarity = 1015.11 mOsm. PASS
- **Buffer Capacity**: Total MOPS = 52.63 mM, Total Tris = 150.00 mM. PASS
- **Pipetting Volume**: All additions >= 5 µL. Total volume = 190 µL. PASS

---

## F4: High Buffer Defined with Citrate/Glutamate
**Strategy**: Leverage High Buffer Defined media's strong pH stability. Supplement with citrate (carbon/chelator), glutamate (nitrogen), and yeast extract to bridge the gap between defined and rich media.

**Composition**:
- Base Medium: High Buffer Defined (165 µL)
- Sodium Citrate: 10 µL (Final: 5.26)
- Sodium L-Glutamate: 10 µL (Final: 52.63)
- Yeast Extract: 5 µL (Final: 2.63)
- Sterile H₂O: 0 µL

**Constraint Validation**:
- **Phosphate & Mg2+**: Total Phosphate = 5.00 mM, Total Mg2+ = 1.00 mM. PASS
- **Iron (Fe2+)**: Total Fe2+ = 0.000 mM. Base pH = 7.0. PASS
- **Calcium & Phosphate**: Total Ca2+ = 0.00 mM, Total Phosphate = 5.00 mM. PASS
- **NaCl**: Total NaCl = 275.00 mM. PASS
- **Osmolarity**: Total Estimated Osmolarity = 779.89 mOsm. PASS
- **Buffer Capacity**: Total MOPS = 100.00 mM, Total Tris = 0.00 mM. PASS
- **Pipetting Volume**: All additions >= 5 µL. Total volume = 190 µL. PASS

---

## F5: High Salt Defined Minimal
**Strategy**: Push the osmolarity and salt tolerance of V. natriegens by adding extra NaCl and (NH4)2SO4 to Defined Minimal media, while supplementing with rich components (tryptone, yeast extract) for amino acids.

**Composition**:
- Base Medium: Defined Minimal (160 µL)
- (NH4)2SO4: 5 µL (Final: 26.32)
- Tryptone: 10 µL (Final: 5.26)
- Yeast Extract: 10 µL (Final: 5.26)
- NaCl: 5 µL (Final: 131.58)
- Sterile H₂O: 0 µL

**Constraint Validation**:
- **Phosphate & Mg2+**: Total Phosphate = 5.00 mM, Total Mg2+ = 1.00 mM. PASS
- **Iron (Fe2+)**: Total Fe2+ = 0.000 mM. Base pH = 7.0. PASS
- **Calcium & Phosphate**: Total Ca2+ = 0.00 mM, Total Phosphate = 5.00 mM. PASS
- **NaCl**: Total NaCl = 406.58 mM. PASS
- **Osmolarity**: Total Estimated Osmolarity = 974.11 mOsm. PASS
- **Buffer Capacity**: Total MOPS = 40.00 mM, Total Tris = 0.00 mM. PASS
- **Pipetting Volume**: All additions >= 5 µL. Total volume = 190 µL. PASS

---

## F6: Enhanced Defined Glycerol
**Strategy**: Optimize Defined Glycerol media by increasing glycerol concentration, adding KCl for osmotic balance without increasing sodium, boosting Mg2+ within the 5 mM limit, and adding glutamate.

**Composition**:
- Base Medium: Defined Glycerol (155 µL)
- Glycerol: 10 µL (Final: 0.53)
- KCl: 10 µL (Final: 10.53)
- MgSO4: 5 µL (Final: 2.63)
- Sodium L-Glutamate: 10 µL (Final: 52.63)
- Sterile H₂O: 0 µL

**Constraint Validation**:
- **Phosphate & Mg2+**: Total Phosphate = 5.00 mM, Total Mg2+ = 3.63 mM. PASS
- **Iron (Fe2+)**: Total Fe2+ = 0.000 mM. Base pH = 7.0. PASS
- **Calcium & Phosphate**: Total Ca2+ = 0.00 mM, Total Phosphate = 5.00 mM. PASS
- **NaCl**: Total NaCl = 275.00 mM. PASS
- **Osmolarity**: Total Estimated Osmolarity = 710.95 mOsm. PASS
- **Buffer Capacity**: Total MOPS = 40.00 mM, Total Tris = 0.00 mM. PASS
- **Pipetting Volume**: All additions >= 5 µL. Total volume = 190 µL. PASS

---
# Vibrio natriegens Media Optimization - Round 1

## Base Media Evaluation & Literature Justification

*Vibrio natriegens* is a fast-growing marine bacterium known for its remarkable doubling time of <15 minutes under optimal conditions. Achieving this maximum growth rate requires highly rich media with abundant amino acids, specific salts (especially Na+, K+, Mg2+), and a slightly alkaline or well-buffered pH (Weinstock et al., 2016; Lee et al., 2019). 

**Included Base Media:**
*   **Media 1 (NBxCyclone, pH 6.4):** Highly promising. Its massive yeast extract (15 g/L) and tryptone content mimic Brain Heart Infusion (BHI) broth, which is known to support the absolute fastest growth rates for *V. natriegens*. The high baseline osmolarity is well-tolerated by this marine organism.
*   **Media 2 (LBv2, pH 7.0):** Highly promising. This is a standard high-salt LB variant (Lennox/Miller style). *V. natriegens* requires elevated NaCl (typically 1.5-3% or ~250-500 mM) for optimal growth, making LBv2 an excellent, proven baseline.
*   **Media 4 (Semi-Defined, pH 7.0):** Included as a comparative baseline. While less rich than M1/M2, supplementing this defined background with targeted rich components (Tryptone/YE) allows us to test if a controlled nutrient profile can approach the kinetics of completely undefined rich media.

**Excluded Base Media:**
*   **Media 3, Media 5, Media 6 (Defined Minimal Media):** Excluded. Literature consistently demonstrates that *V. natriegens* grown in minimal media (even with glucose or glycerol) exhibits significantly slower growth kinetics (doubling times >40 mins) due to the metabolic burden of synthesizing all amino acids and vitamins de novo. Since the objective is to *maximize* growth rate, minimal media are unpromising starting points for this optimization.

---

## Formulation Designs & Constraint Checks

All formulations are designed for a final well volume of exactly **190 µL**. All pipetting volumes are $\ge$ 5 µL.

### 1. Elnora-NBx-Fe-Glutamate
*   **Concept:** Boost respiration and carbon/nitrogen availability in a highly rich background. Fe2+ is added (permitted in pH 6.4 M1) to support cytochromes, and glutamate provides an easily assimilated carbon/nitrogen source.
*   **Base:** Media 1 (150 µL)
*   **Additions:** 
    *   MOPS (1 M stock): 40 mM final $\rightarrow$ (40 * 190) / 1000 = 7.6 µL
    *   FeSO4 (1 mM stock): 0.05 mM final $\rightarrow$ (0.05 * 190) / 1 = 9.5 µL
    *   Na-Glutamate (1 M stock): 30 mM final $\rightarrow$ (30 * 190) / 1000 = 5.7 µL
    *   Water: 190 - 150 - 7.6 - 9.5 - 5.7 = 17.2 µL
*   **Constraint Checks:**
    *   **Buffer:** 40 mM added MOPS + 118.4 mM diluted Tris (150 * 150/190) = 158.4 mM $\ge$ 40 mM. (Pass)
    *   **Phosphate:** Base K2HPO4 is 3 g/L (~17.2 mM). Diluted: 17.2 * 150/190 = 13.6 mM $\le$ 20 mM. (Pass)
    *   **Mg2+:** Base MgSO4 is 4 mM. Diluted: 4 * 150/190 = 3.16 mM $\le$ 5 mM. (Pass)
    *   **Fe2+:** 0.05 mM $\le$ 1 mM. Allowed in M1. (Pass)
    *   **NaCl:** Base NaCl is 22.5 g/L (~385 mM). Diluted: 385 * 150/190 = 303.9 mM (in range 100-500). (Pass)
    *   **Osmolarity:** Base (~950 * 150/190 = 750) + MOPS (40) + Glutamate (30) = ~820 mOsm $\le$ 1200 mOsm. (Pass)
    *   **Min Volume:** 5.7 µL $\ge$ 5 µL. (Pass)

### 2. Elnora-LBv2-Ca-Rich
*   **Concept:** Calcium supplementation has been shown to stabilize the outer membrane of marine vibrios. Combined with extra glucose for a rapid carbon source.
*   **Base:** Media 2 (150 µL)
*   **Additions:** 
    *   MOPS (1 M stock): 50 mM final $\rightarrow$ (50 * 190) / 1000 = 9.5 µL
    *   CaCl2 (100 mM stock): 5 mM final $\rightarrow$ (5 * 190) / 100 = 9.5 µL
    *   Glucose (100 mg/mL stock): 5 mg/mL final $\rightarrow$ (5 * 190) / 100 = 9.5 µL
    *   Water: 190 - 150 - 9.5 - 9.5 - 9.5 = 11.5 µL
*   **Constraint Checks:**
    *   **Buffer:** 50 mM added MOPS $\ge$ 40 mM. (Pass)
    *   **Phosphate:** 0 mM. (Pass)
    *   **Ca2+:** 5 mM. Allowed in M2 (no phosphate). (Pass)
    *   **NaCl:** Base NaCl is 375 mM. Diluted: 375 * 150/190 = 296 mM (in range 100-500). (Pass)
    *   **Osmolarity:** Base (~760 * 150/190 = 600) + MOPS (50) + CaCl2 (5*2=10) = ~660 mOsm $\le$ 1200 mOsm. (Pass)
    *   **Min Volume:** 9.5 µL $\ge$ 5 µL. (Pass)

### 3. Elnora-SemiDef-Boost
*   **Concept:** Supplementing a semi-defined medium with additional rich components (Tryptone and Yeast Extract) to bridge the gap between defined and undefined media kinetics.
*   **Base:** Media 4 (150 µL)
*   **Additions:** 
    *   MOPS (1 M stock): 30 mM final $\rightarrow$ (30 * 190) / 1000 = 5.7 µL
    *   Tryptone (100 mg/mL stock): 5 mg/mL final $\rightarrow$ (5 * 190) / 100 = 9.5 µL
    *   Yeast Extract (100 mg/mL stock): 5 mg/mL final $\rightarrow$ (5 * 190) / 100 = 9.5 µL
    *   Water: 190 - 150 - 5.7 - 9.5 - 9.5 = 15.3 µL
*   **Constraint Checks:**
    *   **Buffer:** Base MOPS (40 * 150/190 = 31.6 mM) + 30 mM added = 61.6 mM $\ge$ 40 mM. (Pass)
    *   **Phosphate:** Base PO4 (5 * 150/190) = 3.95 mM $\le$ 20 mM. (Pass)
    *   **Mg2+:** Base MgSO4 (1 * 150/190) = 0.79 mM $\le$ 5 mM. (Pass)
    *   **NaCl:** Base NaCl (275 * 150/190) = 217.1 mM (in range 100-500). (Pass)
    *   **Osmolarity:** Base (~650 * 150/190 = 513) + MOPS (30) = ~543 mOsm $\le$ 1200 mOsm. (Pass)
    *   **Min Volume:** 5.7 µL $\ge$ 5 µL. (Pass)

### 4. Elnora-LBv2-High-Osm
*   **Concept:** Pushing the osmolarity higher with KCl and adding glycerol as a secondary carbon source. *V. natriegens* thrives in high-salt environments, and K+ is crucial for osmoregulation.
*   **Base:** Media 2 (140 µL)
*   **Additions:** 
    *   MOPS (1 M stock): 50 mM final $\rightarrow$ (50 * 190) / 1000 = 9.5 µL
    *   KCl (200 mM stock): 20 mM final $\rightarrow$ (20 * 190) / 200 = 19.0 µL
    *   Glycerol (10% stock): 0.5% final $\rightarrow$ (0.5 * 190) / 10 = 9.5 µL
    *   Water: 190 - 140 - 9.5 - 19.0 - 9.5 = 12.0 µL
*   **Constraint Checks:**
    *   **Buffer:** 50 mM added MOPS $\ge$ 40 mM. (Pass)
    *   **Phosphate:** 0 mM. (Pass)
    *   **NaCl:** Base NaCl (375 * 140/190) = 276.3 mM (in range 100-500). (Pass)
    *   **Osmolarity:** Base (~760 * 140/190 = 560) + MOPS (50) + KCl (20*2=40) = ~650 mOsm $\le$ 1200 mOsm. (Pass)
    *   **Min Volume:** 9.5 µL $\ge$ 5 µL. (Pass)

### 5. Elnora-NBx-Citrate
*   **Concept:** Citrate acts as both a chelator and a potential carbon source, while glucose provides immediate energy in the ultra-rich NBxCyclone background.
*   **Base:** Media 1 (140 µL)
*   **Additions:** 
    *   MOPS (1 M stock): 40 mM final $\rightarrow$ (40 * 190) / 1000 = 7.6 µL
    *   Sodium Citrate (100 mM stock): 10 mM final $\rightarrow$ (10 * 190) / 100 = 19.0 µL
    *   Glucose (100 mg/mL stock): 5 mg/mL final $\rightarrow$ (5 * 190) / 100 = 9.5 µL
    *   Water: 190 - 140 - 7.6 - 19.0 - 9.5 = 13.9 µL
*   **Constraint Checks:**
    *   **Buffer:** 40 mM added MOPS + 110.5 mM diluted Tris (150 * 140/190) = 150.5 mM $\ge$ 40 mM. (Pass)
    *   **Phosphate:** Base K2HPO4 (~17.2 * 140/190) = 12.69 mM $\le$ 20 mM. (Pass)
    *   **Mg2+:** Base MgSO4 (4 * 140/190) = 2.95 mM $\le$ 5 mM. (Pass)
    *   **NaCl:** Base NaCl (~385 * 140/190) = 283.7 mM (in range 100-500). (Pass)
    *   **Osmolarity:** Base (~950 * 140/190 = 700) + MOPS (40) + Citrate (10) = ~750 mOsm $\le$ 1200 mOsm. (Pass)
    *   **Min Volume:** 7.6 µL $\ge$ 5 µL. (Pass)

### 6. Elnora-LBv2-Ammonium
*   **Concept:** Providing a strong inorganic nitrogen source (ammonium sulfate) alongside additional yeast extract to ensure nitrogen is never limiting during exponential growth.
*   **Base:** Media 2 (150 µL)
*   **Additions:** 
    *   MOPS (1 M stock): 40 mM final $\rightarrow$ (40 * 190) / 1000 = 7.6 µL
    *   (NH4)2SO4 (1 M stock): 30 mM final $\rightarrow$ (30 * 190) / 1000 = 5.7 µL
    *   Yeast Extract (100 mg/mL stock): 5 mg/mL final $\rightarrow$ (5 * 190) / 100 = 9.5 µL
    *   Water: 190 - 150 - 7.6 - 5.7 - 9.5 = 17.2 µL
*   **Constraint Checks:**
    *   **Buffer:** 40 mM added MOPS $\ge$ 40 mM. (Pass)
    *   **Phosphate:** 0 mM. (Pass)
    *   **NaCl:** Base NaCl (375 * 150/190) = 296 mM (in range 100-500). (Pass)
    *   **Osmolarity:** Base (~760 * 150/190 = 600) + MOPS (40) + (NH4)2SO4 (30*3=90) = ~730 mOsm $\le$ 1200 mOsm. (Pass)
    *   **Min Volume:** 5.7 µL $\ge$ 5 µL. (Pass)
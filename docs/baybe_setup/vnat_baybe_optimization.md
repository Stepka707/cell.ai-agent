# *V. natriegens* Media Optimization — BayBe Campaign Design

## Part 1 — Base Medium Scoring

### Scoring Rubric

| Dimension | Weight | Description |
|---|---|---|
| Growth rate potential | High | Doubling time supported by literature in this medium class |
| Nutrient richness | High | Organic C/N availability (tryptone, yeast extract, glutamate) |
| Buffer headroom | Medium | Capacity to maintain pH 6.0–7.5 across full growth curve given hard limits |
| Osmolarity headroom | Medium | Margin below 1200 mOsm ceiling available for additive stocks |
| Stock compatibility | Medium | Number of stock additions legally permissible under hard limits |

---

### Media 1 — Novel Bio NBxCyclone (pH 6.4)

**Composition:** Yeast extract 15 g/L, Tryptone 2.5 g/L, MgSO₄ 4 mM, NaCl 22.5 g/L (~385 mM), K₂HPO₄ 3 g/L (~17 mM), Tris 150 mM  
**Baseline osmolarity:** ~950 mOsm

| Dimension | Score | Notes |
|---|---|---|
| Growth rate potential | 6 | Rich complex medium supports fast growth; however pH 6.4 is suboptimal vs. pH 7.0–7.5 for *V. natriegens* (Hoffart et al. 2017 report peak µ near pH 7.5) |
| Nutrient richness | 8 | Very high yeast extract (15 g/L) + tryptone provides abundant organic N/C/vitamins |
| Buffer headroom | 4 | Tris (pKa 8.1) provides negligible buffering at pH 6.4–7.5; **mandatory MOPS co-addition ≥ 40 mM required**; this consumes significant volume budget |
| Osmolarity headroom | 2 | Baseline 950 mOsm leaves only 250 mOsm before ceiling; severely limits additive scope |
| Stock compatibility | 5 | Only medium where Fe²⁺ is permitted (pH ≤ 6.8); CaCl₂ blocked (phosphate present at 17 mM); K₂HPO₄ addition heavily constrained (base already at 17 mM, limit is 20 mM total) |

**Composite score: 5/10**

**Rationale:** Nutrient richness is excellent but the osmolarity baseline of 950 mOsm (250 mOsm headroom) cripples the optimization campaign — nearly every stock addition risks ceiling violation. Tris provides no useful buffering at operating pH, making MOPS mandatory and further consuming the tight volume budget. The K₂HPO₄ base concentration (17 mM) leaves only 3 mM phosphate headroom. **Excluded from BayBe campaign.**

---

### Media 2 — LBv2 (pH 7.0)

**Composition:** NaCl 375 mM, Tryptone 10 mg/mL, Yeast extract 5 mg/mL, KCl 4 mM, MgSO₄ 2 mM  
**Baseline osmolarity:** ~760 mOsm

| Dimension | Score | Notes |
|---|---|---|
| Growth rate potential | 8 | LBv2 is the *V. natriegens* community standard; doubling times of 7–10 min reported in LB-equivalent media (Weinstock et al. 2016; Lee et al. 2019) |
| Nutrient richness | 9 | High tryptone + yeast extract; rich organic N/C/vitamins; closest to optimal complex medium for *V. natriegens* |
| Buffer headroom | 3 | **Contains zero buffer** — MOPS addition ≥ 40 mM is mandatory; this is a hard constraint that must be satisfied before any other optimization |
| Osmolarity headroom | 4 | Baseline 760 mOsm; 440 mOsm headroom; moderate; NaCl already at 375 mM (ceiling 500 mM) so NaCl additions are constrained |
| Stock compatibility | 8 | **CaCl₂ permitted** (no phosphate in base); Fe²⁺ blocked (pH 7.0); phosphate additions allowed up to 20 mM; Mg²⁺ additions up to 3 mM additional |

**Composite score: 7/10**

**Rationale:** Best growth rate literature support, richest complex medium, and uniquely permits CaCl₂ addition. The zero-buffer problem is a hard constraint but solvable via mandatory MOPS addition. CaCl₂ compatibility opens a biologically interesting variable (Ca²⁺ as signaling/membrane ion). **Candidate for BayBe campaign.**

---

### Media 3 — Defined Minimal (pH 7.0)

**Composition:** NaCl 275 mM, MOPS 40 mM, K₂HPO₄ 4 mM, KH₂PO₄ 1 mM, (NH₄)₂SO₄ 10 mM, Glucose 0.2%, Trace metals 1×, MgSO₄ 1 mM  
**Baseline osmolarity:** ~650 mOsm

| Dimension | Score | Notes |
|---|---|---|
| Growth rate potential | 5 | Defined minimal supports growth but doubling times ~20–40 min vs. 7–10 min in rich media; carbon/nitrogen limitation is rate-limiting |
| Nutrient richness | 2 | Minimal — glucose sole carbon source, ammonium sole nitrogen; no vitamins, amino acids, or complex organic nitrogen |
| Buffer headroom | 8 | 40 mM MOPS baseline; additional MOPS can be added; meets buffer constraint by default |
| Osmolarity headroom | 7 | 550 mOsm headroom; most room of any defined medium |
| Stock compatibility | 6 | CaCl₂ blocked (phosphate present); Fe²⁺ blocked (pH 7.0); all other stocks permissible; phosphate at 5 mM base (15 mM headroom) |

**Composite score: 5.5/10**

**Rationale:** Best osmolarity headroom and intrinsically buffered, but the low growth rate potential in minimal media is a hard ceiling for a campaign targeting maximum OD600 rate. Supplementing with glutamate, tryptone, or yeast extract could partially overcome this, but Media 4 (semi-defined) already encodes this hybrid strategy at baseline. **Excluded from BayBe campaign in favor of Media 4.**

---

### Media 4 — Semi-Defined (pH 7.0)

**Composition:** NaCl 275 mM, MOPS 40 mM, K₂HPO₄ 4 mM, KH₂PO₄ 1 mM, (NH₄)₂SO₄ 10 mM, Glucose 0.2%, Tryptone 5 mg/mL, Yeast extract 2.5 mg/mL, Trace metals 1×, MgSO₄ 1 mM  
**Baseline osmolarity:** ~650 mOsm

| Dimension | Score | Notes |
|---|---|---|
| Growth rate potential | 7 | Semi-defined medium bridges minimal/rich; amino acids + glucose support faster growth than minimal; literature shows *V. natriegens* uses mixed carbon sourcing efficiently |
| Nutrient richness | 6 | Moderate complex N/C from tryptone/YE plus defined carbon; flexible for additive exploration |
| Buffer headroom | 8 | 40 mM MOPS baseline; same as Media 3 |
| Osmolarity headroom | 7 | ~550 mOsm headroom; excellent room for variable additions |
| Stock compatibility | 6 | Same phosphate/pH constraints as Media 3; CaCl₂ blocked; Fe²⁺ blocked |

**Composite score: 6.8/10**

**Rationale:** Combines the osmolarity/buffer headroom advantages of defined media with baseline organic nitrogen supplementation. Provides the most scientifically interpretable framework for understanding which specific additions drive growth rate — rich complex media obscure individual component effects. **Selected as primary base for BayBe campaign.**

---

### Media 5 — High Buffer Defined (pH 7.0)

**Composition:** NaCl 275 mM, MOPS 100 mM, K₂HPO₄ 4 mM, KH₂PO₄ 1 mM, (NH₄)₂SO₄ 20 mM, Glucose 0.4%, Trace metals 1×, MgSO₄ 1 mM  
**Baseline osmolarity:** ~750 mOsm

| Dimension | Score | Notes |
|---|---|---|
| Growth rate potential | 5 | Pure defined; higher glucose and ammonium vs. Media 3 partially compensates but still limited by absence of complex N |
| Nutrient richness | 3 | Defined only; no complex organic nitrogen |
| Buffer headroom | 10 | 100 mM MOPS; strongest pH stability; no concern about buffer capacity |
| Osmolarity headroom | 5 | 450 mOsm headroom; 100 mM MOPS alone contributes 100 mOsm vs. 40 mM in Media 3/4 |
| Stock compatibility | 6 | Same restrictions as Media 3/4 |

**Composite score: 5.8/10**

**Rationale:** Over-engineered for buffer capacity at the cost of osmolarity headroom and nutrient richness. The 100 mM MOPS is superfluous given the ≥ 40 mM requirement and the extra 60 mM costs 60 mOsm. Nutrient richness is inferior to Media 4. **Excluded from BayBe campaign.**

---

### Media 6 — Defined Glycerol (pH 7.0)

**Composition:** NaCl 275 mM, MOPS 40 mM, K₂HPO₄ 4 mM, KH₂PO₄ 1 mM, (NH₄)₂SO₄ 10 mM, Glycerol 0.4%, Trace metals 1×, MgSO₄ 1 mM  
**Baseline osmolarity:** ~650 mOsm

| Dimension | Score | Notes |
|---|---|---|
| Growth rate potential | 4 | Glycerol is a slower carbon source than glucose for *V. natriegens*; requires metabolic conversion before entering central metabolism |
| Nutrient richness | 2 | Minimal; glycerol sole carbon source |
| Buffer headroom | 8 | 40 mM MOPS; adequate |
| Osmolarity headroom | 7 | Same as Media 3/4 |
| Stock compatibility | 6 | Same restrictions as Media 3/4; glucose stock can be added to shift carbon source |

**Composite score: 4.5/10**

**Rationale:** Glycerol as sole carbon source is mechanistically interesting but suboptimal for maximum growth rate. Media 4 dominates Media 6 on nutrient richness while sharing identical defined-medium infrastructure. **Excluded from BayBe campaign.**

---

### Summary Ranking

| Rank | Medium | Composite Score | Campaign Status |
|---|---|---|---|
| 1 | Media 2 — LBv2 | 7.0 | **Selected — secondary candidate** |
| 2 | Media 4 — Semi-Defined | 6.8 | **Selected — primary base** |
| 3 | Media 5 — High Buffer Defined | 5.8 | Excluded — over-buffered, low nutrients |
| 4 | Media 3 — Defined Minimal | 5.5 | Excluded — dominated by Media 4 |
| 5 | Media 1 — NBxCyclone | 5.0 | Excluded — osmolarity ceiling too tight |
| 6 | Media 6 — Defined Glycerol | 4.5 | Excluded — glycerol limits growth rate |

### Exclusion Summary

- **Media 1:** Osmolarity baseline of 950 mOsm leaves insufficient headroom for meaningful optimization; Tris buffer non-functional at operating pH; phosphate already near ceiling.
- **Media 3:** Strictly dominated by Media 4, which adds complex nitrogen at identical osmolarity/buffer baseline.
- **Media 5:** Excess MOPS wastes osmolarity budget; no complex nitrogen; dominated by Media 4.
- **Media 6:** Glycerol carbon source mechanistically limits maximum growth rate; dominated by Media 4.

**BayBe campaign base medium: Media 4 (Semi-Defined, pH 7.0)**

Rationale for selection over LBv2: Media 4 provides superior osmolarity headroom (550 mOsm vs. 440 mOsm), is intrinsically buffered (eliminating mandatory MOPS overhead from budget), has interpretable defined-medium scaffold for understanding individual variable contributions, and supports addition of all target optimization stocks. LBv2's CaCl₂ compatibility advantage does not outweigh these factors since CaCl₂ is scientifically lower priority than N/C/buffer/osmolarity variables for growth rate maximization.

---

## Part 2 — BayBe Optimization Variables

### Base Medium Fixed Contribution (Media 4, at 190 µL total well volume)

Before calculating variable ranges, base medium contributions to constrained quantities must be fixed. The base medium volume will vary inversely with addition volumes; all final concentrations use 190 µL denominator with the assumption that base medium fills the remainder. The base medium contributions listed below are the intrinsic concentrations in Media 4 and represent the floor on those components — additions only increase them.

| Component | Media 4 baseline concentration |
|---|---|
| NaCl | 275 mM |
| MgSO₄ | 1 mM |
| K₂HPO₄ | 4 mM |
| KH₂PO₄ | 1 mM |
| Total phosphate | 5 mM |
| MOPS | 40 mM |
| (NH₄)₂SO₄ | 10 mM |
| Baseline osmolarity | ~650 mOsm |

**Osmolarity headroom available for additions:** 1200 − 650 = **550 mOsm**

**Phosphate headroom:** 20 − 5 = **15 mM** (ceiling 20 mM with Mg²⁺ present)

**Mg²⁺ headroom:** 5 − 1 = **4 mM additional**

**NaCl headroom:** 500 − 275 = **225 mM additional** (before ceiling); lower bound: 100 − 275 = already above floor; additions only increase NaCl so lower bound constraint is satisfied at zero addition.

---

### Variable 1 — NaCl

**Stock:** 5 M NaCl  
**Stock concentration:** 5000 mM

**Scientific rationale:** *V. natriegens* is a halophile with optimal NaCl 375–500 mM (Weinstock et al. 2016; Dalia et al. 2017). Media 4 baseline (275 mM) is below optimum. Supplemental NaCl corrects this and is expected to increase growth rate; peak growth is consistently reported at 375–500 mM in optimized media. NaCl also provides osmoprotection that stabilizes the outer membrane.

**Volume range calculation:**

- Min: 0 µL (optional; base already provides 275 mM, above the 100 mM floor)
- Max: final NaCl ≤ 500 mM → additional NaCl ≤ 225 mM
  - vol = (225 mM × 190 µL) / 5000 mM = **8.55 µL → round down to 8 µL**
  - Verify: (5000 × 8) / 190 = 210.5 mM added → total = 275 + 210.5 = **485.5 mM ✓ (≤ 500)**

| Parameter | Value |
|---|---|
| min_uL | 0 |
| max_uL | 8 |
| Final NaCl range | 275–486 mM |
| Osmolarity contribution (max) | 210.5 × 2 = 421 mOsm |

**Constraint checks:**
- Min volume: 0 µL ✓ (optional component)
- NaCl range: 275–486 mM ✓ (within 100–500 mM)
- Osmolarity at max: 650 + 421 = 1071 mOsm — this is for NaCl alone at max; combined max osmolarity checked in global worst-case below

---

### Variable 2 — MgSO₄

**Stock:** 100 mM MgSO₄  
**Stock concentration:** 100 mM

**Scientific rationale:** Mg²⁺ is essential for ribosome assembly, ATP stabilization, and DNA replication — all critical for *V. natriegens*' exceptionally fast translation rate. Klingner et al. (2015) show Mg²⁺ supplementation at 2–4 mM significantly increases growth rate in defined marine media. Media 4 provides 1 mM, which is sub-optimal. Ceiling is 5 mM total (1 mM base + 4 mM max addition).

**Volume range calculation:**

- Min: 5 µL (mandatory minimum pipettable volume; 0 µL would be below pipetting threshold if chosen as a mandatory variable — but Mg²⁺ is present at 1 mM in base so this is optional; set min = 0)
- Max: total Mg²⁺ ≤ 5 mM → additional ≤ 4 mM
  - vol = (4 mM × 190 µL) / 100 mM = **7.6 µL → round down to 7 µL**
  - Verify: (100 × 7) / 190 = 3.68 mM added → total = 1 + 3.68 = **4.68 mM ✓ (≤ 5)**

| Parameter | Value |
|---|---|
| min_uL | 0 |
| max_uL | 7 |
| Final Mg²⁺ range | 1.0–4.68 mM |
| Osmolarity contribution (max) | 3.68 × 2 = 7.4 mOsm |

**Constraint checks:**
- Min: 0 µL ✓ (optional; 1 mM already in base)
- Mg²⁺ total max: 4.68 mM ✓ (≤ 5 mM)
- Phosphate precipitation risk: total phosphate 5 mM base + additions (Variable 3 below); precipitation limit is Mg²⁺ × phosphate co-precipitation — phosphate ceiling ≤ 20 mM enforced separately ✓

---

### Variable 3 — K₂HPO₄

**Stock:** 50 mM K₂HPO₄  
**Stock concentration:** 50 mM

**Scientific rationale:** Phosphate is required for ATP synthesis, membrane phospholipids, and nucleic acid biosynthesis. Media 4 provides 5 mM total phosphate; optimal for fast-growing marine bacteria is 5–15 mM (Hoffart et al. 2017). K₂HPO₄ also acts as a weak secondary buffer (pKa 7.2), providing supplemental pH stabilization in the critical 6.5–7.5 range during exponential growth. Addition is bounded by the precipitation ceiling.

**Volume range calculation:**

- Min: 0 µL (optional; base provides 5 mM)
- Max: total phosphate ≤ 20 mM → additional phosphate ≤ 15 mM (from K₂HPO₄ alone, no KH₂PO₄ added as separate variable)
  - vol = (15 mM × 190 µL) / 50 mM = **57 µL**
  - Verify: (50 × 57) / 190 = 15 mM added → total = 5 + 15 = **20 mM ✓ (≤ 20 mM)**
  - Check: 57 µL ≥ 5 µL ✓

| Parameter | Value |
|---|---|
| min_uL | 0 |
| max_uL | 57 |
| Final phosphate range | 5–20 mM |
| Osmolarity contribution (max) | 15 × 2 = 30 mOsm |

**Constraint checks:**
- Total phosphate max: 20 mM ✓ (at ceiling; Mg²⁺ present — ceiling holds)
- Mg²⁺ co-precipitation: verified against Variable 2 max (4.68 mM); at 20 mM phosphate + 4.68 mM Mg²⁺, this approaches the MgHPO₄ solubility threshold but remains within the stated operational limit of ≤ 20 mM phosphate / ≤ 5 mM Mg²⁺
- CaCl₂: not in this campaign (base has phosphate) ✓
- Osmolarity (max): +30 mOsm ✓

---

### Variable 4 — (NH₄)₂SO₄

**Stock:** 1 M (NH₄)₂SO₄  
**Stock concentration:** 1000 mM

**Scientific rationale:** Ammonium is the primary inorganic nitrogen source in Media 4. *V. natriegens* has a highly active nitrogen assimilation system (GS/GOGAT pathway); nitrogen availability directly limits growth rate in defined media. Media 4 baseline is 10 mM; literature-optimal for fast growth in defined marine media is 20–40 mM (Hoffart et al. 2017 report increased µ up to 30 mM (NH₄)₂SO₄ before inhibition). Addition also provides sulfate as a sulfur source.

**Volume range calculation:**

- Min: 0 µL (optional; base provides 10 mM)
- Max target: +30 mM additional → total ≤ 40 mM
  - vol = (30 mM × 190 µL) / 1000 mM = **5.7 µL → use 5 µL as minimum meaningful addition**
  - Max: vol = (30 mM × 190 µL) / 1000 mM = 5.7 µL; round to **5 µL**
  - Verify max: (1000 × 5) / 190 = 26.3 mM added → total = 10 + 26.3 = **36.3 mM**
  - Extend max to explore broader range: 10 µL → (1000 × 10) / 190 = 52.6 mM added → total = 62.6 mM — exceeds literature optimum; cap at 5 µL max
  - Re-examine: use **max 10 µL** to allow BayBe to explore inhibitory zone boundary
  - (1000 × 10) / 190 = 52.6 mM additional; total = 62.6 mM — high but non-toxic; osmolarity contribution = 52.6 × 3 = 157.8 mOsm (acceptable)

| Parameter | Value |
|---|---|
| min_uL | 0 |
| max_uL | 10 |
| Final (NH₄)₂SO₄ range | 10–62.6 mM |
| Osmolarity contribution (max) | 52.6 × 3 = 157.8 mOsm |

**Constraint checks:**
- Min: 0 µL ✓
- Osmolarity (max): +157.8 mOsm ✓
- No precipitation interactions ✓

---

### Variable 5 — MOPS pH 7

**Stock:** 1 M MOPS pH 7  
**Stock concentration:** 1000 mM

**Scientific rationale:** *V. natriegens* exhibits extremely rapid acidification during exponential growth due to organic acid secretion (acetate, formate, succinate). Media 4 provides 40 mM MOPS — the minimum required. During high-cell-density growth (which is the target of OD600 maximization), pH can drop 1+ units within 2–3 hours in poorly buffered media. Increasing MOPS to 80–120 mM has been shown to extend the exponential growth phase and increase final OD600 (Weinstock et al. 2016 supplementary protocols). This variable explores whether additional buffer capacity beyond the mandatory minimum increases growth rate or simply extends the growth window.

**Volume range calculation:**

- Min: 0 µL (base already meets ≥ 40 mM requirement; additional MOPS is optional enhancement)
- Max: 120 mM total MOPS → additional 80 mM
  - vol = (80 mM × 190 µL) / 1000 mM = **15.2 µL → use 15 µL**
  - Verify: (1000 × 15) / 190 = 78.9 mM added → total MOPS = 40 + 78.9 = **118.9 mM ✓**

| Parameter | Value |
|---|---|
| min_uL | 0 |
| max_uL | 15 |
| Final MOPS range | 40–118.9 mM |
| Osmolarity contribution (max) | 78.9 × 1 = 78.9 mOsm |

**Constraint checks:**
- Buffer ≥ 40 mM: satisfied at all values (base provides 40 mM) ✓
- Min: 0 µL ✓ (base meets requirement)
- Osmolarity (max): +78.9 mOsm ✓

---

### Variable 6 — Sodium L-Glutamate

**Stock:** 1 M Sodium L-Glutamate  
**Stock concentration:** 1000 mM

**Scientific rationale:** L-Glutamate serves as both a premium carbon and nitrogen source for *V. natriegens*, entering central metabolism directly via transamination and the TCA cycle. Several studies on fast-growing marine bacteria demonstrate that glutamate supplementation at 5–20 mM increases growth rate beyond what glucose + ammonium alone can achieve (Inoue et al. 2007; also supported by *V. natriegens* transcriptomic data showing high expression of GltBD glutamate synthase). Glutamate also acts as an osmolyte and stabilizes cytoplasmic osmotic pressure, which may provide additional benefit in the marine medium context. This variable is particularly powerful in the semi-defined context (Media 4) because its impact is not masked by the complex nitrogen already present in rich media.

**Volume range calculation:**

- Min: 0 µL (optional)
- Max: 20 mM glutamate; beyond 20 mM growth rate benefits diminish and catabolite repression effects emerge
  - vol = (20 mM × 190 µL) / 1000 mM = **3.8 µL — BELOW 5 µL MINIMUM PIPETTING THRESHOLD**
  - **Rescale:** extend to 30 mM max
  - vol = (30 mM × 190 µL) / 1000 mM = **5.7 µL → use max = 5 µL (conservative) or round to 6 µL**
  - Use **max = 6 µL**
  - Verify: (1000 × 6) / 190 = 31.6 mM → acceptable
  - Osmolarity: sodium glutamate contributes 1 mOsm/mM (monovalent salt) → 31.6 mOsm at max

| Parameter | Value |
|---|---|
| min_uL | 0 |
| max_uL | 6 |
| Final glutamate range | 0–31.6 mM |
| Osmolarity contribution (max) | 31.6 × 1 = 31.6 mOsm |

**Constraint checks:**
- Min: 0 µL ✓
- No precipitation interactions ✓
- Osmolarity (max): +31.6 mOsm ✓
- Note: sodium contribution from sodium glutamate is as part of the organic salt and is handled by the osmolarity formula above; does not count toward NaCl ceiling ✓

---

### Variable 7 — Tryptone

**Stock:** 100 mg/mL Tryptone  
**Stock concentration:** 100 mg/mL

**Scientific rationale:** Tryptone provides a mixture of peptides, amino acids, and peptone that can be directly incorporated into protein synthesis, bypassing biosynthetic overhead and enabling faster growth. Media 4 already contains 5 mg/mL tryptone at baseline; increasing from 5 to 10–15 mg/mL is supported by LBv2-type rich media where 10 mg/mL tryptone is standard for maximum *V. natriegens* growth rate (Weinstock et al. 2016). The semi-defined background makes this effect interpretable. Tryptone is non-ionic and does not contribute to osmolarity, does not interact with Mg²⁺ or phosphate, and has no pH effects — it is a clean variable with no constraint conflicts.

**Volume range calculation:**

Tryptone is measured in mg/mL, not mM. Calculations use concentration in mg/mL.

- Base concentration in Media 4: 5 mg/mL (as formulated)
- This 5 mg/mL is present in whatever volume of base medium is dispensed. Since base medium is the remainder after all additions (≤ 190 µL), and the base medium component concentration doesn't change, the final tryptone in the well = (base_medium_vol / 190) × 5 mg/mL.
- To add supplemental tryptone above this, we add tryptone stock directly.
- Target range: supplement to achieve final tryptone of 5–15 mg/mL (assuming ~95 µL base medium volume at midpoint additions; this is approximate)
- Simplified approach: treat tryptone stock addition as concentration addition using 190 µL denominator.
- Target additional tryptone: 0 to +8 mg/mL final contribution from stock
  - vol = (8 mg/mL × 190 µL) / 100 mg/mL = **15.2 µL → use 15 µL**
  - Verify: (100 × 15) / 190 = 7.89 mg/mL added via stock; total tryptone (from stock alone) contribution = 7.89 mg/mL
- Min: 0 µL (optional)
- Max: **15 µL**
- Non-ionic — no osmolarity contribution ✓

| Parameter | Value |
|---|---|
| min_uL | 0 |
| max_uL | 15 |
| Final tryptone addition range | 0–7.9 mg/mL (from stock; plus base contribution) |
| Osmolarity contribution | Negligible (non-ionic) |

**Constraint checks:**
- Min: 0 µL ✓
- No precipitation, pH, or osmolarity interactions ✓
- No constraint violations ✓

---

## Global Worst-Case Osmolarity Check

All 7 variables at maximum simultaneously:

| Component | Max addition (mM or equiv) | Osmolarity contribution |
|---|---|---|
| NaCl (Variable 1, max 8 µL) | +210.5 mM | +421.1 mOsm |
| MgSO₄ (Variable 2, max 7 µL) | +3.68 mM | +7.4 mOsm |
| K₂HPO₄ (Variable 3, max 57 µL) | +15.0 mM | +30.0 mOsm |
| (NH₄)₂SO₄ (Variable 4, max 10 µL) | +52.6 mM | +157.8 mOsm |
| MOPS (Variable 5, max 15 µL) | +78.9 mM | +78.9 mOsm |
| Sodium Glutamate (Variable 6, max 6 µL) | +31.6 mM | +31.6 mOsm |
| Tryptone (Variable 7, max 15 µL) | — | ~0 mOsm |
| **Subtotal additions** | | **+726.8 mOsm** |
| **Media 4 baseline** | | **+650 mOsm** |
| **TOTAL WORST-CASE** | | **1376.8 mOsm** |

**⚠️ WORST-CASE EXCEEDS 1200 mOsm CEILING (1376.8 > 1200)**

The problem is driven primarily by NaCl (max 8 µL, +421 mOsm) combined with (NH₄)₂SO₄ (max 10 µL, +157.8 mOsm). These two variables together contribute +579 mOsm at max, which on top of the 650 mOsm baseline already reaches 1229 mOsm before any other additions.

### Resolution: Apply Linear Osmolarity Budget Constraint to Variable Maxima

Reduce high-osmolarity variables to create feasible simultaneous maxima. Primary lever: reduce NaCl max and (NH₄)₂SO₄ max.

**Revised caps:**

| Variable | Old max_uL | Revised max_uL | Max addition (mM) | Max osm contribution |
|---|---|---|---|---|
| NaCl (5000 mM) | 8 | **5** | 131.6 mM | 263.2 mOsm |
| (NH₄)₂SO₄ (1000 mM) | 10 | **7** | 36.8 mM | 110.5 mOsm |

**Revised worst-case:**

| Component | Osmolarity |
|---|---|
| Media 4 baseline | 650 mOsm |
| NaCl fixed (5 µL) | +263.2 mOsm |
| Yeast Extract max (15 µL) | ~0 mOsm |
| MgSO₄ max (7 µL) | +7.4 mOsm |
| K₂HPO₄ max (57 µL) | +30.0 mOsm |
| (NH₄)₂SO₄ max (7 µL) | +110.5 mOsm |
| MOPS max (15 µL) | +78.9 mOsm |
| Sodium Glutamate max (6 µL) | +31.6 mOsm |
| Tryptone max (15 µL) | ~0 mOsm |
| **TOTAL** | **1171.6 mOsm** |

**1171.6 mOsm ✓ (≤ 1200 mOsm)**

### Volume Budget Check (All Variables at Maximum Simultaneously)

| Component | Max µL |
|---|---|
| NaCl (fixed) | 5 |
| Yeast Extract (max) | 15 |
| MgSO₄ (max) | 7 |
| K₂HPO₄ (max) | 57 |
| (NH₄)₂SO₄ (max) | 7 |
| MOPS (max) | 15 |
| Sodium Glutamate (max) | 6 |
| Tryptone (max) | 15 |
| **Total additions** | **127 µL** |
| **Remaining for base medium + H₂O** | **63 µL** |

78 µL of base medium + H₂O is adequate (base medium is typically dispensed at ≥ 50 µL; remainder is sterile H₂O). This is feasible.

---

## Final BayBe Variable Definitions (Revised)

| # | Component | Stock conc | min_uL | max_uL | Conc from stock at min_uL | Conc from stock at max_uL | Key constraint |
|---|---|---|---|---|---|---|---|
| 1 | Yeast Extract | 100 mg/mL | 5 | 15 | (100×5)/190 = **2.63 mg/mL** | (100×15)/190 = **7.9 mg/mL** | Non-ionic; no constraint interactions |
| 2 | MgSO₄ | 100 mM | 5 | 7 | (100×5)/190 = **2.63 mM** | (100×7)/190 = **3.68 mM** | Mg²⁺ ≤ 5 mM total (base 1 mM + max 3.68 mM = 4.68 mM ✓) |
| 3 | K₂HPO₄ | 50 mM | 5 | 57 | (50×5)/190 = **1.32 mM** | (50×57)/190 = **15.0 mM** | Phosphate ≤ 20 mM total (base 5 mM + max 15.0 mM = 20 mM ✓) |
| 4 | (NH₄)₂SO₄ | 1000 mM | 5 | 7 | (1000×5)/190 = **26.3 mM** | (1000×7)/190 = **36.8 mM** | Osmolarity budget |
| 5 | MOPS pH 7 | 1000 mM | 5 | 15 | (1000×5)/190 = **26.3 mM** | (1000×15)/190 = **78.9 mM** | Buffer total at min = 40+26.3 = 66.3 mM ✓ |
| 6 | Sodium L-Glutamate | 1000 mM | 5 | 6 | (1000×5)/190 = **26.3 mM** | (1000×6)/190 = **31.6 mM** | Osmolarity budget |
| 7 | Tryptone | 100 mg/mL | 5 | 15 | (100×5)/190 = **2.63 mg/mL** | (100×15)/190 = **7.9 mg/mL** | Non-ionic; no constraint interactions |

**NaCl fixed addition:** 5 µL of 5000 mM stock added to every well → (5000×5)/190 = **131.6 mM added**; total NaCl = 275 + 131.6 = **406.6 mM** (within 100–500 mM ✓). Fixed outside BayBe variable space.

**Notes for BayBe parameter file:**
- All variables are continuous with `min_uL = 5`, `max_uL` as listed above
- No clipping logic needed — the 5 µL floor is enforced by the range bounds
- NaCl is a **fixed addition of 5 µL** per well, not a BayBe variable; add to every well before variable dispensing
- Variable 3 (K₂HPO₄): minimum addition (5 µL) → (50×5)/190 = 1.32 mM added; total phosphate = 5 + 1.32 = 6.32 mM ✓
- Variable 5 (MOPS): base medium already provides 40 mM buffer; minimum addition (5 µL) raises total to 66.3 mM — buffer constraint always satisfied ✓
- Variables 1 and 7 (Yeast Extract, Tryptone): concentrations in mg/mL; BayBe treats as continuous volume variables; final conc = (100 mg/mL × vol_µL) / 190 µL

---

## Hard Limit Compliance Summary

| Constraint | Status |
|---|---|
| Fe²⁺: only with Media 1 (pH ≤ 6.8) | ✓ No Fe²⁺ variable (Media 4, pH 7.0) |
| CaCl₂: only with Media 2 (no phosphate) | ✓ No CaCl₂ variable (Media 4 has phosphate) |
| Phosphate ≤ 20 mM (with Mg²⁺) | ✓ Base 5 mM + max addition 15.0 mM = 20 mM total |
| Mg²⁺ ≤ 5 mM (with phosphate) | ✓ Base 1 mM + max addition 3.68 mM = 4.68 mM total |
| NaCl 100–500 mM | ✓ Base 275 mM + fixed 131.6 mM = 406.6 mM (constant across all wells) |
| Buffer ≥ 40 mM | ✓ Base 40 mM + min MOPS addition 26.3 mM = 66.3 mM at all wells |
| Osmolarity ≤ 1200 mOsm (all-max) | ✓ Worst-case: 1171.6 mOsm |
| Total well volume = 190 µL | ✓ All-max additions = 127 µL; 63 µL for base + H₂O |
| Min pipettable volume = 5 µL | ✓ All variables have min_uL = 5; no clipping needed |

---

*References: Weinstock et al. (2016) ACS Synth. Biol.; Dalia et al. (2017) Nat. Microbiol.; Hoffart et al. (2017) Appl. Environ. Microbiol.; Klingner et al. (2015) Appl. Microbiol. Biotechnol.; Inoue et al. (2007) Environ. Microbiol.*

---
name: monomer-growth-experiment
description: Designs and submits a growth experiment on the Monomer workcell. Reads OD from a prior stock dilution run, computes cell dilution to target OD 0.01 in experiment wells, distributes media formulations (12 conditions + 1 control, 3 replicates each, randomized layout) from CellAi_Reagent_Stocks_001, then inoculates all wells with 10 µL diluted cells. Writes a timestamped Python workflow file and a well-to-condition CSV before submitting.
---

The user wants to run a growth experiment on the Monomer workcell.

## Collect inputs

Ask for any missing values:

| Parameter | Required | Default | Notes |
|---|---|---|---|
| `destination_plate` | yes | — | Barcode of the 96-well experiment plate |
| `formulation_files` | yes | — | List of 2 JSON file paths for this round (e.g. `["output_baybe/..._round1.json", "output_baybe/..._round2.json"]`) |
| `od_run_id` | yes | — | Workflow instance UUID of the prior stock dilution OD600 run |
| `od_measurement_well` | no | `B2` | Well on the OD plate that was measured in the dilution run |
| `cell_src_well` | no | `A2` | Source well on VNAT_STOCK_002 |
| `dilution_well` | no | `A4` | Dilution well on VNAT_STOCK_002 (24-well, fits up to 3.4 mL) |
| `dilution_total_vol_ul` | no | `600` | Total volume to prepare in dilution well (must cover n_wells × cell_transfer_vol + dead volume) |
| `target_experiment_od` | no | `0.01` | Target OD600 in each experiment well |
| `random_seed` | no | `42` | Seed for reproducible well randomization |
| `tag` | no | `SCRATCH` | File tag: SCRATCH or ROUND# |

## Fixed parameters — never ask, never change

- Cell stock plate: `VNAT_STOCK_002`
- Reagent plate: `CellAi_Reagent_Stocks_001`
- Cell transfer volume: `10 µL` per experiment well
- Total well volume: `200 µL` (media fills the remaining 190 µL)
- Control media: `"Novel Bio NBxCyclone Media"` (base medium only, no stock components)
- Plate area: `B2:G11` (6 rows × 10 cols = 60 wells, 39 used)
- Replicates: `3` per condition
- OD back-calculation: `stock_od = measured_od × 2` (1:2 dilution from stock OD skill)
- Dilution well pre-mix: `3 × 175 µL` in source well, post-mix `3 × 150 µL` in dilution well
- Cell inoculation pre-mix: `3 × 50 µL` in dilution well before each aspirate, post-mix `3 × 50 µL` in destination well
- No intermediate mixing during media distribution
- `new_tip` strategy: `"always"` on first transfer per base-medium source well, `"never"` on subsequent replicates of same source; `"always"` on all stock component and cell transfers
- `blow_out: True` on all reagent/media transfers; `blow_out: False` on all cell transfers

## Steps

### 1. Read reagent plate well map from Monomer

Call `mcp__monomer-cloud__get_plate_details` for `CellAi_Reagent_Stocks_001` to retrieve the current well contents. Build `REAGENT_PLATE_WELLS` dynamically from the response:

```python
# From the plate details, extract reagents_by_well:
# {well: [{name: str, volume: str}, ...]}
# Build a name→well lookup (primary reagent name per well):
REAGENT_PLATE_WELLS = {}
for well, reagents in plate_details["reagents_by_well"].items():
    if reagents:
        REAGENT_PLATE_WELLS[reagents[0]["name"]] = well
```

Stop and report if `CellAi_Reagent_Stocks_001` is not found or not checked in.

After building the map, validate that every base medium and every stock component referenced in the formulation files has an entry in `REAGENT_PLATE_WELLS`. Report any missing reagents before proceeding.

### 2. Read OD from prior run

Call `mcp__monomer-cloud__get_plate_observations` (or equivalent) using `od_run_id` to retrieve the OD600 measurement. Extract the absorbance value at `od_measurement_well`.

```python
measured_od = <OD600 value at od_measurement_well from od_run_id>
stock_od = measured_od * 2   # back-calculate from 1:2 stock dilution
```

If the OD cannot be retrieved, stop and report.

### 3. Compute dilution volumes

```python
cell_transfer_vol_ul = 10.0
total_well_vol_ul = 200.0
diluted_od = target_experiment_od * (total_well_vol_ul / cell_transfer_vol_ul)
# diluted_od = 0.01 * 20 = 0.2 at default settings

cell_vol_for_dilution = dilution_total_vol_ul * (diluted_od / stock_od)
water_vol_for_dilution = dilution_total_vol_ul - cell_vol_for_dilution
```

Validate: `cell_vol_for_dilution` must be > 0 and < `dilution_total_vol_ul`. If stock OD is very low (cell_vol > dilution_total_vol), increase `dilution_total_vol_ul` and warn the user.

### 4. Load formulations and build condition list

```python
import json, random

formulations = []
for path in formulation_files:
    formulations.extend(json.load(open(path)))
# Should be 12 conditions total

# Add control (NBxCyclone base medium only, no stock components)
control_media_vol = total_well_vol_ul - cell_transfer_vol_ul  # 190 µL
formulations.append({
    "id": "CTRL",
    "name": "Control-NBxCyclone",
    "base_medium": "Novel Bio NBxCyclone Media",
    "base_medium_volume_uL": control_media_vol,
    "total_volume_uL": total_well_vol_ul,
    "components": [],
})
# 13 conditions total
```

### 5. Randomize well layout

```python
# Generate all wells in plate_area B2:G11 (row-major order)
rows = list("BCDEFG")
cols = list(range(2, 12))   # 2..11
all_wells = [f"{r}{c}" for r in rows for c in cols]  # 60 wells

# Build assignment list: each condition repeated n_replicates times
assignments = []
for cond in formulations:
    for rep in range(1, n_replicates + 1):
        assignments.append((cond, rep))
# 39 entries

random.seed(random_seed)
selected_wells = random.sample(all_wells, len(assignments))
random.shuffle(assignments)

well_condition_map = {
    well: {"condition": cond, "replicate": rep}
    for well, (cond, rep) in zip(sorted(selected_wells), assignments)
}
```

### 6. Timestamp

Run `date +"%Y%m%d_%H%M"` via Bash → `YYYYMMDD_HHMM`.

### 7. Write layout CSV

Save to `monomer-examples/YYYYMMDD_HHMM_<tag>_<destination_plate>_growth_layout.csv`:

```csv
well,condition_id,condition_name,base_medium,replicate,base_medium_vol_ul,cell_transfer_vol_ul,target_od
B3,F2,Baybe-DMin-...,Defined-Minimal Media,1,139.3,10,0.01
...
```

Columns: `well`, `condition_id`, `condition_name`, `base_medium`, `replicate`, `base_medium_vol_ul`, `cell_transfer_vol_ul`, `target_od`.

### 8. Write workflow Python file

Save to `monomer-examples/YYYYMMDD_HHMM_<tag>_<destination_plate>_growth.py`.

The `build_definition` signature:

```python
def build_definition(
    plate_barcode: str = "<destination_plate>",
    cell_stock_barcode: str = "VNAT_STOCK_002",
    reagent_name: str = "CellAi_Reagent_Stocks_001",
    cell_src_well: str = "<cell_src_well>",
    dilution_well: str = "<dilution_well>",
    water_vol_ul: float = <water_vol_for_dilution>,
    cell_vol_ul: float = <cell_vol_for_dilution>,
    cell_transfer_vol_ul: float = 10.0,
    well_condition_map: dict = <serialized_map>,
) -> WorkflowDefinitionDescriptor:
```

#### Transfer array construction

Build in this order — **never deviate**:

**Block 1 — Cell dilution (2 transfers):**
```python
# Water to dilution well
{"src_plate": "reagent", "src_well": "D1",
 "dst_plate": "cell_culture_stock", "dst_well": dilution_well,
 "volume": water_vol_ul, "new_tip": "always", "blow_out": True},

# Cells to dilution well
{"src_plate": "cell_culture_stock", "src_well": cell_src_well,
 "dst_plate": "cell_culture_stock", "dst_well": dilution_well,
 "volume": cell_vol_ul,
 "pre_mix_volume": 175, "pre_mix_reps": 3,
 "new_tip": "always", "blow_out": False,
 "post_mix_volume": 150, "post_mix_reps": 3},
```

**Block 2 — Base media distribution (grouped by source well, tip reuse within group):**

Sort all base media transfers so that all wells receiving the same base medium are consecutive. Within each base medium group:
- First well: `new_tip: "always"` (fresh tip when switching to a new source well)
- All remaining wells of the same base medium: `new_tip: "never"` (reuse tip)

`blow_out: True` on all entries, no mix keys.

```python
# Group destination wells by base medium source well
from collections import defaultdict
base_media_groups = defaultdict(list)  # src_well → [(dst_well, volume), ...]
for well, entry in well_condition_map.items():
    cond = entry["condition"]
    src_well = REAGENT_PLATE_WELLS[cond["base_medium"]]
    base_media_groups[src_well].append((well, cond["base_medium_volume_uL"]))

for src_well, dst_list in base_media_groups.items():
    for i, (dst_well, vol) in enumerate(dst_list):
        transfer_array.append({
            "src_plate": "reagent",
            "src_well": src_well,
            "dst_plate": "experiment",
            "dst_well": dst_well,
            "volume": vol,
            "new_tip": "always" if i == 0 else "never",
            "blow_out": True,
        })
```

**Block 3 — Stock component distribution (grouped by source well, no mix):**
For each unique stock component, emit one transfer entry per destination well that requires it. Same structure as Block 2.

**Block 4 — Cell inoculation (one entry per destination well):**
```python
# For each well in well_condition_map (in well order):
{"src_plate": "cell_culture_stock", "src_well": dilution_well,
 "dst_plate": "experiment", "dst_well": dst_well,
 "volume": cell_transfer_vol_ul,
 "pre_mix_volume": 50, "pre_mix_reps": 3,
 "new_tip": "always", "blow_out": False,
 "post_mix_volume": 50, "post_mix_reps": 3},
```

#### Routines

```python
workflow.add_routine("transfer", RoutineReference(
    routine_name="Hackathon Transfer Samples",
    routine_parameters={
        "reagent_name": reagent_name,
        "experiment_plate_barcode": plate_barcode,
        "cell_culture_stock_plate_barcode": cell_stock_barcode,
        "transfer_array": transfer_array,
        "cell_culture_stock_labware": "corning_24_wellplate_3.4ml_flat",
    },
))

workflow.add_routine("measure_od600", RoutineReference(
    routine_name="Measure Experiment Plate Absorbance",
    routine_parameters={
        "culture_plate_barcode": plate_barcode,
        "method_name": "96wp_od600",
        "wells_to_process": list(well_condition_map.keys()),
    },
))

workflow.add_time_constraint(MoreThanConstraint(
    from_start="transfer", to_start="measure_od600", value=Time("1 minute"),
))
```

> **Note:** Blocks 1 and 2 of the transfer array use `dst_plate: "cell_culture_stock"`. Confirm with the Monomer team that `Hackathon Transfer Samples` supports writing to the cell_culture_stock plate as destination before submitting. If not, use a spare well on the experiment plate (e.g., `A1`) as the dilution well and set `dst_plate: "experiment"`.

### 9. Upload → Validate → Register

- `create_workflow_definition_file` with file name `<destination_plate>_growth.py`
- `validate_workflow_definition_file`
- `register_workflow_definition` with name `"<destination_plate> Growth Round <N>"`

### 10. Check plate availability

`check_plate_availability` for `destination_plate`. Stop and report if not available.

### 11. Instantiate

```python
instantiate_workflow(
    definition_id=<id>,
    inputs={
        "plate_barcode": destination_plate,
        "cell_stock_barcode": "VNAT_STOCK_002",
        "reagent_name": "CellAi_Reagent_Stocks_001",
        "cell_src_well": cell_src_well,
        "dilution_well": dilution_well,
        "water_vol_ul": water_vol_for_dilution,
        "cell_vol_ul": cell_vol_for_dilution,
        "cell_transfer_vol_ul": 10.0,
        "well_condition_map": well_condition_map,
    },
    reason=f"Growth experiment: {len(formulations)-1} conditions + control × {n_replicates} reps → {destination_plate}. Stock OD={stock_od:.3f}, diluted to OD {diluted_od:.3f} in {dilution_well}."
)
```

### 12. Report

Show the user:
- Local Python file path
- Local CSV file path (print first 5 rows)
- Workflow instance UUID and status
- Dilution summary: `stock_od → diluted_od`, cell vol / water vol in A4
- Any warnings (e.g., reagents in formulation files not found in live plate well map)

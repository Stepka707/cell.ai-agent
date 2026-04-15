---
name: monomer-stock-od-measurement
description: Prepares and submits a stock dilution OD600 measurement workflow on the Monomer workcell. Transfers 100 µL sterile H₂O (CellAi_Reagent_Stocks_001 D1) then 100 µL cells (VNAT_STOCK_002) into a destination well on an experiment plate, followed by OD600 measurement. Writes a timestamped local Python file and submits to Monomer.
---

The user wants to run a stock dilution OD600 measurement on the Monomer workcell.

## Collect inputs

Ask the user for any missing values:

| Parameter | Required | Default | Notes |
|---|---|---|---|
| `destination_plate` | yes | — | Barcode of the 96-well experiment plate |
| `dst_well` | no | `B2` | Destination well on the experiment plate |
| `cell_src_well` | no | `A2` | Source well on VNAT_STOCK_002 |

## Fixed parameters — never ask, never change

- Cell stock plate: `VNAT_STOCK_002`
- Reagent plate name: `CellAi_Reagent_Stocks_001`
- Water source well: `D1`
- Water: 100 µL · `new_tip: always` · `blow_out: True` · no mix
- Cells: 100 µL · `new_tip: always` · `blow_out: False`
  - Pre-mix: 3 × 175 µL in source well before aspirating
  - Post-mix: 3 × 150 µL in destination well after dispensing
- Transfer order: water first, then cells
- OD600: `96wp_od600` on destination well only, always runs after transfer

## Steps

1. **Timestamp** — run `date +"%Y%m%d_%H%M"` via Bash to get `YYYYMMDD_HHMM`

2. **Write local file** — save to:
   `monomer-examples/YYYYMMDD_HHMM_SCRATCH_<destination_plate>_stock_od600.py`

   The `build_definition` function signature must be:
   ```python
   def build_definition(
       plate_barcode: str = "<destination_plate>",
       cell_stock_barcode: str = "VNAT_STOCK_002",
       reagent_name: str = "CellAi_Reagent_Stocks_001",
       cell_src_well: str = "<cell_src_well>",
       water_src_well: str = "D1",
       dst_well: str = "<dst_well>",
       cell_volume_ul: float = 100.0,
       water_volume_ul: float = 100.0,
   ) -> WorkflowDefinitionDescriptor:
   ```

   Transfer array:
   ```python
   [
       # 1. Water first — no mix
       {
           "src_plate": "reagent",
           "src_well": water_src_well,
           "dst_plate": "experiment",
           "dst_well": dst_well,
           "volume": water_volume_ul,
           "new_tip": "always",
           "blow_out": True,
       },
       # 2. Cells — pre-mix 3×175 µL, post-mix 3×150 µL
       {
           "src_plate": "cell_culture_stock",
           "src_well": cell_src_well,
           "dst_plate": "experiment",
           "dst_well": dst_well,
           "volume": cell_volume_ul,
           "pre_mix_volume": 175,
           "pre_mix_reps": 3,
           "new_tip": "always",
           "blow_out": False,
           "post_mix_volume": 150,
           "post_mix_reps": 3,
       },
   ]
   ```

3. **Upload** — `create_workflow_definition_file` with file name `<destination_plate>_stock_od600.py`

4. **Validate** — `validate_workflow_definition_file` with test inputs

5. **Register** — `register_workflow_definition` with name `"<destination_plate> Stock OD600"`

6. **Check availability** — `check_plate_availability` for `destination_plate`; stop and report if not available

7. **Instantiate** — `instantiate_workflow` with:
   - All inputs matching `build_definition` parameters
   - `reason`: `"Stock dilution OD600: 100 µL H2O (CellAi_Reagent_Stocks_001 D1) + 100 µL cells (VNAT_STOCK_002 <cell_src_well>) → <destination_plate> <dst_well>"`

8. **Report** — show the user: local file path, workflow instance UUID, status

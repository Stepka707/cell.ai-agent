"""CellAI stock dilution OD600: 100 µL H₂O + 100 µL cells → CellAi_Experiment_Plate_001 B2.

OVERVIEW
--------
1. Transfer 100 µL sterile H₂O from CellAI Reagent Plate (MEDIA_20260415_134551_009654)
   well D1 into CellAi_Experiment_Plate_001 well B2.
2. Transfer 100 µL cells from VNAT_STOCK_002 well A2 (pre-mix 3×175 µL, post-mix 3×150 µL)
   into CellAi_Experiment_Plate_001 well B2.
3. Transport CellAi_Experiment_Plate_001 to the reader and take an OD600 measurement.

PLATE REQUIREMENTS
------------------
- CellAi_Experiment_Plate_001          : 96-well experiment plate — checked in
- VNAT_STOCK_002                        : 24-well cell culture stock plate — cells in A2
- CellAI Reagent Plate                  : 24-well reagent plate (MEDIA_20260415_134551_009654)
                                          sterile H₂O in D1
"""

from __future__ import annotations

from src.platform.core_domain.units import Time
from src.workflows.workflow_definition_dsl.workflow_definition_descriptor import (
    MoreThanConstraint,
    RoutineReference,
    WorkflowDefinitionDescriptor,
)


def build_definition(
    plate_barcode: str = "CellAi_Experiment_Plate_001",
    cell_stock_barcode: str = "VNAT_STOCK_002",
    reagent_name: str = "CellAI Reagent Plate",
    cell_src_well: str = "A2",
    water_src_well: str = "D1",
    dst_well: str = "B2",
    cell_volume_ul: float = 100.0,
    water_volume_ul: float = 100.0,
) -> WorkflowDefinitionDescriptor:
    """Transfer water then cells into experiment plate, then measure OD600.

    :param plate_barcode: Barcode of the 96-well experiment plate.
    :param cell_stock_barcode: Barcode of the 24-well cell culture stock plate.
    :param reagent_name: Monomer tag (initial_media_type) for the reagent plate.
    :param cell_src_well: Source well for cells on VNAT_STOCK_002 (default A2).
    :param water_src_well: Source well for sterile H₂O on the reagent plate (default D1).
    :param dst_well: Destination well on the experiment plate (default B2).
    :param cell_volume_ul: Volume of cells to transfer in µL (default 100).
    :param water_volume_ul: Volume of water to transfer in µL (default 100).
    :return: Complete workflow definition.
    """
    workflow = WorkflowDefinitionDescriptor(
        description=(
            f"Stock dilution OD600: {water_volume_ul} µL H₂O + {cell_volume_ul} µL cells "
            f"→ {plate_barcode} {dst_well}."
        )
    )

    transfer_array = [
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
        # 2. Cells — pre-mix 3×175 µL in source, post-mix 3×150 µL in destination
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

    workflow.add_routine(
        "transfer",
        RoutineReference(
            routine_name="Hackathon Transfer Samples",
            routine_parameters={
                "reagent_name": reagent_name,
                "experiment_plate_barcode": plate_barcode,
                "cell_culture_stock_plate_barcode": cell_stock_barcode,
                "transfer_array": transfer_array,
                "cell_culture_stock_labware": "corning_24_wellplate_3.4ml_flat",
            },
        ),
    )

    workflow.add_routine(
        "measure_od600",
        RoutineReference(
            routine_name="Measure Experiment Plate Absorbance",
            routine_parameters={
                "culture_plate_barcode": plate_barcode,
                "method_name": "96wp_od600",
                "wells_to_process": [dst_well],
            },
        ),
    )

    workflow.add_time_constraint(
        MoreThanConstraint(
            from_start="transfer",
            to_start="measure_od600",
            value=Time("1 minute"),
        )
    )

    return workflow


if __name__ == "__main__":
    import json
    print(json.dumps(build_definition().model_dump(), indent=2))

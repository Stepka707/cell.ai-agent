"""VNAMO experiment: transfer cell stock into experiment plate, then read OD600.

OVERVIEW
--------
1. Transfer 200 µL from VNAMO_CELL_STOCK_002 well A1 (with pre-mix) into
   VNAMO_EXPERIMENT_PLATE_001 well B2 via the Opentrons Flex.
2. Transport VNAMO_EXPERIMENT_PLATE_001 to the reader and take an OD600 measurement.

NOTE ON REAGENT PLATE
---------------------
The Hackathon Transfer Samples routine unconditionally loads three plates onto the
OT-Flex deck — including a reagent plate from the LPX220 cold storage — even if no
transfer touches it. reagent_name must match a real checked-in plate tag in the LPX220.
Currently using "VNAMO Reagent Plate 1" (barcode MEDIA_20260330_185221_384471).
The reagent plate will be loaded on the deck and returned untouched.
"""

from __future__ import annotations

from src.platform.core_domain.units import Time
from src.workflows.workflow_definition_dsl.workflow_definition_descriptor import (
    MoreThanConstraint,
    RoutineReference,
    WorkflowDefinitionDescriptor,
)


def build_definition(
    plate_barcode: str = "VNAMO_EXPERIMENT_PLATE_001",
    cell_stock_barcode: str = "VNAMO_CELL_STOCK_002",
    reagent_name: str = "VNAMO Reagent Plate 1",
    src_well: str = "A1",
    dst_well: str = "B2",
    volume_ul: float = 200.0,
) -> WorkflowDefinitionDescriptor:
    """Transfer premixed cell stock into experiment plate, then measure OD600.

    :param plate_barcode: Barcode of the 96-well experiment plate (STX220).
    :param cell_stock_barcode: Barcode of the 24-well cell culture stock plate (STX220).
    :param reagent_name: Tag for the LPX220 reagent plate. Loaded on deck but not
        touched — must match a real checked-in plate in the LPX220.
    :param src_well: Source well on the cell stock plate (default A1).
    :param dst_well: Destination well on the experiment plate (default B2).
    :param volume_ul: Transfer volume in µL (default 200).
    :return: Complete workflow definition.
    """
    workflow = WorkflowDefinitionDescriptor(
        description=(
            f"Transfer {volume_ul} µL from {cell_stock_barcode} {src_well} "
            f"to {plate_barcode} {dst_well} (with premix), then read OD600."
        )
    )

    transfer_array = [
        {
            "src_plate": "cell_culture_stock",
            "src_well": src_well,
            "dst_plate": "experiment",
            "dst_well": dst_well,
            "volume": volume_ul,
            "pre_mix_volume": 100,
            "pre_mix_reps": 3,
            "new_tip": "always",
            "blow_out": True,
        }
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

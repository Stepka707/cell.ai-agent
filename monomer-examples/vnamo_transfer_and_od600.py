from src.platform.core_domain.units import Time
from src.workflows.workflow_definition_dsl.workflow_definition_descriptor import (
    MoreThanConstraint,
    RoutineReference,
    WorkflowDefinitionDescriptor,
)


def build_definition(
    plate_barcode: str = "VNAMO_EXPERIMENT_PLATE_001",
    cell_stock_barcode: str = "VNAMO_CELL_STOCK_002",
    reagent_name: str = "VNAMO_REAGENT",
    src_well: str = "A1",
    dst_well: str = "B2",
    volume_ul: float = 200.0,
) -> WorkflowDefinitionDescriptor:
    """Transfer premixed cell stock into experiment plate, then measure OD600.

    Aspirates volume_ul from cell_stock_barcode src_well (with pre-mix to
    homogenise the premix), dispenses into plate_barcode dst_well, then
    immediately transports the experiment plate to the reader for an OD600
    measurement.

    :param plate_barcode: Barcode of the 96-well experiment plate (STX220)
    :param cell_stock_barcode: Barcode of the 24-well cell culture stock plate (STX220)
    :param reagent_name: Reagent tag for the LPX220 reagent plate (loaded on deck but not used in transfers)
    :param src_well: Source well on cell stock plate (default A1)
    :param dst_well: Destination well on experiment plate (default B2)
    :param volume_ul: Transfer volume in µL (default 200)
    :return: Complete workflow definition
    """
    workflow = WorkflowDefinitionDescriptor()
    workflow.description = (
        f"Transfer {volume_ul} µL from {cell_stock_barcode} {src_well} "
        f"to {plate_barcode} {dst_well} (with premix), then read OD600."
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

    transfer = RoutineReference(
        routine_name="Hackathon Transfer Samples",
        routine_parameters={
            "reagent_name": reagent_name,
            "experiment_plate_barcode": plate_barcode,
            "cell_culture_stock_plate_barcode": cell_stock_barcode,
            "transfer_array": transfer_array,
            "cell_culture_stock_labware": "corning_24_wellplate_3.4ml_flat",
        },
    )
    workflow.add_routine("transfer", transfer)

    measure = RoutineReference(
        routine_name="Measure Experiment Plate Absorbance",
        routine_parameters={
            "culture_plate_barcode": plate_barcode,
            "method_name": "96wp_od600",
            "wells_to_process": [dst_well],
        },
    )
    workflow.add_routine("measure_od600", measure)

    # OD600 measurement must run after the transfer completes
    workflow.add_time_constraint(
        MoreThanConstraint(
            from_start="transfer",
            to_start="measure_od600",
            value=Time("1 minute"),
        )
    )

    return workflow

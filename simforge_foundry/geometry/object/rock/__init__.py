from pathlib import Path
from typing import List, Tuple

from pydantic import NonNegativeFloat, PositiveFloat, PositiveInt
from simforge import BlGeometry, BlGeometryNodesModifier, BlMaterial, BlNodesFromPython


class RockNodes(BlGeometryNodesModifier):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="Rock",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )

    detail: PositiveInt = 4
    scale: Tuple[PositiveFloat, PositiveFloat, PositiveFloat] = (0.1, 0.1, 0.075)
    scale_std: Tuple[NonNegativeFloat, NonNegativeFloat, NonNegativeFloat] = (
        0.01,
        0.01,
        0.005,
    )
    horizontal_cut_enable: bool = False
    horizontal_cut_offset: float = 0.0
    mat: BlMaterial | None = None


class RockGeo(BlGeometry):
    ops: List[BlGeometryNodesModifier] = [RockNodes()]

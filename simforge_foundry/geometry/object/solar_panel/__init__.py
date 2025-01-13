from pathlib import Path
from typing import List, Tuple

from pydantic import NonNegativeFloat, PositiveFloat, SerializeAsAny
from simforge import (
    BlGeometry,
    BlGeometryNodesModifier,
    BlGeometryOp,
    BlMaterial,
    BlNodesFromPython,
)


class SolarPanelNodes(BlGeometryNodesModifier):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="SolarPanel",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )

    scale: Tuple[PositiveFloat, PositiveFloat, PositiveFloat] = (1.0, 1.0, 0.05)
    border_size: NonNegativeFloat = 0.0
    panel_depth: NonNegativeFloat = 0.0
    frame_mat: BlMaterial | None = None
    cells_mat: BlMaterial | None = None


class SolarPanelGeo(BlGeometry):
    ops: List[SerializeAsAny[BlGeometryOp]] = [SolarPanelNodes()]

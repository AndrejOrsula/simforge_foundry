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


class MoonSurfaceNodes(BlGeometryNodesModifier):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="MoonSurface",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )

    scale: Tuple[PositiveFloat, PositiveFloat, PositiveFloat] = (5.0, 5.0, 0.5)
    density: PositiveFloat = 0.1
    flat_area_size: NonNegativeFloat = 0.0
    rock_mesh_boolean_enable: bool = False
    mat: BlMaterial | None = None


class MoonSurfaceGeo(BlGeometry):
    ops: List[SerializeAsAny[BlGeometryOp]] = [MoonSurfaceNodes()]

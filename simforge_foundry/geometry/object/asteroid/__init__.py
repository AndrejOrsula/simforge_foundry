from pathlib import Path
from typing import List, Tuple

from pydantic import NonNegativeFloat, PositiveFloat, PositiveInt, SerializeAsAny
from simforge import (
    BlGeometry,
    BlGeometryNodesModifier,
    BlGeometryOp,
    BlMaterial,
    BlNodesFromPython,
)


class AsteroidNodes(BlGeometryNodesModifier):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="Asteroid",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )

    detail: PositiveInt = 4
    scale: Tuple[PositiveFloat, PositiveFloat, PositiveFloat] = (0.1, 0.1, 0.1)
    scale_std: Tuple[NonNegativeFloat, NonNegativeFloat, NonNegativeFloat] = (
        0.01,
        0.01,
        0.01,
    )
    mat: BlMaterial | None = None


class AsteroidGeo(BlGeometry):
    ops: List[SerializeAsAny[BlGeometryOp]] = [AsteroidNodes()]

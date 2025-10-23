from pathlib import Path
from typing import List, Tuple

from pydantic import PositiveInt, SerializeAsAny
from simforge import (
    BlGeometry,
    BlGeometryNodesModifier,
    BlGeometryOp,
    BlMaterial,
    BlNodesFromPython,
    BlTriangulateModifier,
)

from simforge_foundry.material import MarsRockMat, MoonRockMat, RandomMaterialNodes


class BagRandomNodes(BlGeometryNodesModifier):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="random_bag",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )

    detail: PositiveInt = 3
    scale: Tuple[float, float, float] = (0.35, 0.2, 0.075)
    mat: BlMaterial | None = None


class BagRandomGeo(BlGeometry):
    ops: List[SerializeAsAny[BlGeometryOp]] = [
        BagRandomNodes(),
        BlTriangulateModifier(),
        RandomMaterialNodes(
            mat_count=2,
            mat0=MoonRockMat(),
            mat1=MarsRockMat(),
        ),
    ]

from pathlib import Path
from typing import List

from pydantic import PositiveFloat, PositiveInt, SerializeAsAny
from simforge import (
    BlGeometry,
    BlGeometryNodesModifier,
    BlGeometryOp,
    BlNodesFromPython,
)

from simforge_foundry.material import (
    BrushedChromeMat,
    RandomMaterialNodes,
    ScratchedMetalMat,
    ScratchedPlasticMat,
    SmoothGoldMat,
)


class ScoopRandomNodes(BlGeometryNodesModifier):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="random_scoop",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )

    subdivisions: PositiveInt = 3
    tooth_subdivisions_offset: int = -1
    mount_radius: PositiveFloat = 0.025
    mount_vertices_ratio: PositiveFloat = 0.75


class ScoopRandomGeo(BlGeometry):
    ops: List[SerializeAsAny[BlGeometryOp]] = [
        ScoopRandomNodes(),
        RandomMaterialNodes(
            mat_count=4,
            mat0=ScratchedMetalMat(),
            mat1=ScratchedPlasticMat(),
            mat2=SmoothGoldMat(),
            mat3=BrushedChromeMat(),
        ),
    ]

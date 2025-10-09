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
    AsteroidMat,
    BrushedChromeMat,
    MarsRockMat,
    MoonRockMat,
    RandomMaterialNodes,
    ScratchedMetalMat,
    ScratchedPlasticMat,
    SmoothGoldMat,
    SmoothMetalMat,
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
            mat_count=8,
            mat0=SmoothMetalMat(),
            mat1=ScratchedMetalMat(),
            mat2=BrushedChromeMat(),
            mat3=SmoothGoldMat(),
            mat4=ScratchedPlasticMat(),
            mat5=MoonRockMat(),
            mat6=MarsRockMat(),
            mat7=AsteroidMat(),
        ),
    ]

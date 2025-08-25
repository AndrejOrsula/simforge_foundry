from pathlib import Path
from typing import List

from pydantic import PositiveFloat, PositiveInt, SerializeAsAny
from simforge import (
    BlGeometry,
    BlGeometryNodesModifier,
    BlGeometryOp,
    BlNodesFromPython,
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
    ops: List[SerializeAsAny[BlGeometryOp]] = [ScoopRandomNodes()]

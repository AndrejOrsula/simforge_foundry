from pathlib import Path

from pydantic import InstanceOf
from simforge import BlMaterial, BlNodesFromPython, BlShader


class MarsRockShader(BlShader):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="MarsRockShader",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )


class MarsRockMat(BlMaterial):
    shader: InstanceOf[BlShader] = MarsRockShader()

from pathlib import Path

from pydantic import InstanceOf
from simforge import BlMaterial, BlNodesFromPython, BlShader


class MarsSurfaceShader(BlShader):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="MarsSurfaceShader",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )


class MarsSurfaceMat(BlMaterial):
    shader: InstanceOf[BlShader] = MarsSurfaceShader()

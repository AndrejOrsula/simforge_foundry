from pathlib import Path

from pydantic import InstanceOf
from simforge import BlMaterial, BlNodesFromPython, BlShader


class MoonSurfaceShader(BlShader):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="MoonSurfaceShader",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )


class MoonSurfaceMat(BlMaterial):
    shader: InstanceOf[BlShader] = MoonSurfaceShader()

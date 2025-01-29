from pathlib import Path

from simforge import BlMaterial, BlNodesFromPython, BlShader


class SmoothMetalShader(BlShader):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="Smooth Metal",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )


class SmoothMetalMat(BlMaterial):
    shader: BlShader = SmoothMetalShader()

from pathlib import Path

from simforge import BlMaterial, BlNodesFromPython, BlShader


class ScratchedMetalShader(BlShader):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="ScratchedMetalShader",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )


class ScratchedMetalMat(BlMaterial):
    shader: BlShader = ScratchedMetalShader()

from pathlib import Path

from simforge import BlMaterial, BlNodesFromPython, BlShader


class ScratchedPlasticShader(BlShader):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="ScratchedPlasticShader",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )


class ScratchedPlasticMat(BlMaterial):
    shader: BlShader = ScratchedPlasticShader()

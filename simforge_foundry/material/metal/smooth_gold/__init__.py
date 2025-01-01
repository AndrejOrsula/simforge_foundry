from pathlib import Path

from simforge import BlMaterial, BlNodesFromPython, BlShader


class SmoothGoldShader(BlShader):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="GoldSmoothShader",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )


class SmoothGoldMat(BlMaterial):
    shader: BlShader = SmoothGoldShader()

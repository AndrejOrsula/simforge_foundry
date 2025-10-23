from pathlib import Path

from simforge import BlMaterial, BlNodesFromPython, BlShader


class WovenFabricShader(BlShader):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="WovenFabricShader",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )


class WovenFabricMat(BlMaterial):
    shader: BlShader = WovenFabricShader()

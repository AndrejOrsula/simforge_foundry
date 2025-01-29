from pathlib import Path

from simforge import BlMaterial, BlNodesFromPython, BlShader


class BrushedChromeShader(BlShader):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="BrushedChrome",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )


class BrushedChromeMat(BlMaterial):
    shader: BlShader = BrushedChromeShader()

from pathlib import Path
from typing import Tuple

from pydantic import NonNegativeFloat
from simforge import BlMaterial, BlNodesFromPython, BlShader


class SolarPanelShader(BlShader):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="SolarPanelShader",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )

    color1: Tuple[
        NonNegativeFloat, NonNegativeFloat, NonNegativeFloat, NonNegativeFloat
    ] = (
        0.0,
        0.015,
        0.175,
        1.0,
    )
    color2: Tuple[
        NonNegativeFloat, NonNegativeFloat, NonNegativeFloat, NonNegativeFloat
    ] = (
        0.0,
        0.005,
        0.125,
        1.0,
    )


class SolarPanelMat(BlMaterial):
    shader: BlShader = SolarPanelShader()

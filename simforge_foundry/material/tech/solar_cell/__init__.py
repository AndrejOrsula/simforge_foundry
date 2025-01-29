from pathlib import Path
from typing import Tuple

from pydantic import NonNegativeFloat, PositiveFloat
from simforge import BlMaterial, BlNodesFromPython, BlShader


class SolarCellShader(BlShader):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="SolarCellShader",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )

    scale: PositiveFloat = 1.0
    color1: Tuple[
        NonNegativeFloat, NonNegativeFloat, NonNegativeFloat, NonNegativeFloat
    ] = (
        1.0,
        0.35,
        0.065,
        1.0,
    )
    color2: Tuple[
        NonNegativeFloat, NonNegativeFloat, NonNegativeFloat, NonNegativeFloat
    ] = (
        0.02,
        0.02,
        0.02,
        1.0,
    )
    grid_visibility: NonNegativeFloat = 0.3
    roughness: NonNegativeFloat = 1.0
    bump_strength: NonNegativeFloat = 0.2


class SolarCellMat(BlMaterial):
    shader: BlShader = SolarCellShader()

from pathlib import Path
from typing import Tuple

from pydantic import InstanceOf, NonNegativeFloat, PositiveFloat
from simforge import BlMaterial, BlNodesFromPython, BlShader


class AsteroidShader(BlShader):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="AsteroidShader",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )

    scale: PositiveFloat = 1.0
    color1: Tuple[
        NonNegativeFloat, NonNegativeFloat, NonNegativeFloat, NonNegativeFloat
    ] = (
        0.1,
        0.1,
        0.1,
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


class AsteroidMat(BlMaterial):
    shader: InstanceOf[BlShader] = AsteroidShader()

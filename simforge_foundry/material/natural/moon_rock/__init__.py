from pathlib import Path
from typing import Tuple

from pydantic import InstanceOf, NonNegativeFloat, PositiveFloat
from simforge import BlMaterial, BlNodesFromPython, BlShader


class MoonRockShader(BlShader):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="MoonRockShader",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )

    scale: PositiveFloat = 16.0
    color1: Tuple[
        NonNegativeFloat, NonNegativeFloat, NonNegativeFloat, NonNegativeFloat
    ] = (
        0.25,
        0.25,
        0.25,
        1.0,
    )
    color2: Tuple[
        NonNegativeFloat, NonNegativeFloat, NonNegativeFloat, NonNegativeFloat
    ] = (
        0.01,
        0.01,
        0.01,
        1.0,
    )
    edge_color: Tuple[
        NonNegativeFloat, NonNegativeFloat, NonNegativeFloat, NonNegativeFloat
    ] = (
        0.4,
        0.4,
        0.4,
        1.0,
    )
    noise_scale: NonNegativeFloat = 7.0
    noise_detail: NonNegativeFloat = 15.0
    noise_roughness: NonNegativeFloat = 0.25
    light_noise_scale: NonNegativeFloat = 5.0
    light_noise_roughness: NonNegativeFloat = 0.8
    roughness: NonNegativeFloat = 1.0
    noise_bump_scale: NonNegativeFloat = 15.0
    noise_bump_strength: NonNegativeFloat = 0.05
    detailed_noise_bump_strength: NonNegativeFloat = 0.25
    edge_color_strength: NonNegativeFloat = 0.75
    noise_scale_mixer: NonNegativeFloat = 0.01
    noise_bump_roughness: NonNegativeFloat = 1.0
    voronoi_bump_scale: NonNegativeFloat = 2.0
    voronoi_bump_strength: NonNegativeFloat = 0.75


class MoonRockMat(BlMaterial):
    shader: InstanceOf[BlShader] = MoonRockShader()

from math import pi
from pathlib import Path
from typing import ClassVar, List, Tuple

from pydantic import PositiveFloat, PositiveInt, SerializeAsAny
from simforge import (
    BlGeometry,
    BlGeometryNodesModifier,
    BlGeometryOp,
    BlNodesFromPython,
    BlTriangulateModifier,
    OpType,
)


class ModuleNodes(BlGeometryNodesModifier):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="Module",
        python_file=Path(__file__).parent.joinpath("nodes_module.py"),
    )

    module_centering: bool = True
    module_size: PositiveFloat = 0.15
    module_thickness: PositiveFloat = 0.2
    module_size_tolerance: PositiveFloat = 0.0
    module_count_x: PositiveInt = 1
    module_count_y: PositiveInt = 1
    holes_enable: bool = False
    holes_vertices: PositiveInt = 16
    holes_offset_from_corner: PositiveFloat = 0.015
    holes_diameter: PositiveFloat = 0.0043


class ModuleGeo(BlGeometry):
    ops: List[SerializeAsAny[BlGeometryOp]] = [ModuleNodes()]


class HoleNodes(BlGeometryNodesModifier):
    OP_TYPE: ClassVar[OpType] = OpType.MODIFY
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="Hole",
        python_file=Path(__file__).parent.joinpath("nodes_hole.py"),
    )

    hole_position_offset_min: Tuple[float, float, float] = (-0.05, -0.05, -0.05)
    hole_position_offset_max: Tuple[float, float, float] = (0.05, 0.05, 0.05)
    hole_orientation_offset_min: Tuple[float, float, float] = (
        -20.0 / 180.0 * pi,
        -20.0 / 180.0 * pi,
        -pi,
    )
    hole_orientation_offset_max: Tuple[float, float, float] = (
        20.0 / 180.0 * pi,
        20.0 / 180.0 * pi,
        pi,
    )
    hole_insertion_angle_min: float = 0.0
    hole_insertion_angle_max: float = 2.0 * pi

    hole_depth_factor_min: PositiveFloat = 0.25
    hole_depth_factor_max: PositiveFloat = 0.75
    hole_size_tolerance: PositiveFloat = 0.001
    wall_enable: bool = True
    wall_remove_inner_holes: bool = False
    wall_thickness: PositiveFloat = 0.005
    wall_include_bottom: bool = True


class HoleGeo(BlGeometry):
    ops: List[SerializeAsAny[BlGeometryOp]] = [
        ModuleNodes(),
        HoleNodes(),
        BlTriangulateModifier(),
    ]


class PegNodes(BlGeometryNodesModifier):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="Peg",
        python_file=Path(__file__).parent.joinpath("nodes_peg.py"),
    )

    profile_p_circle: PositiveFloat = 0.333
    profile_n_vertices_circle: PositiveInt = 48
    profile_n_vertices_ngon_min: PositiveInt = 3
    profile_n_vertices_ngon_max: PositiveInt = 12
    radius_min: PositiveFloat = 0.01
    radius_max: PositiveFloat = 0.025
    height_min: PositiveFloat = 0.04
    height_max: PositiveFloat = 0.08
    aspect_ratio_min: PositiveFloat = 0.25
    aspect_ratio_max: PositiveFloat = 1.0
    taper_factor_min: PositiveFloat = 0.0
    taper_factor_max: PositiveFloat = 0.0
    use_uniform_geometry: bool = False


class PegGeo(BlGeometry):
    ops: List[SerializeAsAny[BlGeometryOp]] = [PegNodes()]

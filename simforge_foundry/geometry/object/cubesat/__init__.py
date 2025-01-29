from pathlib import Path
from typing import List

from pydantic import NonNegativeFloat, PositiveFloat, SerializeAsAny
from simforge import (
    BlGeometry,
    BlGeometryNodesModifier,
    BlGeometryOp,
    BlMaterial,
    BlNodesFromPython,
)

from simforge_foundry.material import (
    BrushedChromeMat,
    ScratchedMetalMat,
    ScratchedPlasticMat,
    SmoothGoldMat,
    SolarCellMat,
    SolarPanelMat,
    SolarPanelShader,
)


class CubesatNodes(BlGeometryNodesModifier):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="Cubesat",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )

    rail_size: PositiveFloat = 0.005
    rail_end_length: NonNegativeFloat = 0.01
    border_size: PositiveFloat = 0.002
    cells_mat1: BlMaterial = SolarPanelMat()
    cells_mat2: BlMaterial = SolarPanelMat(
        shader=SolarPanelShader(
            color1=(0.15, 0.15, 0.15, 1.0),
            color2=(0.05, 0.05, 0.05, 1.0),
        )
    )
    cells_mat3: BlMaterial = SolarCellMat()
    frame_mat1: BlMaterial = SmoothGoldMat()
    frame_mat2: BlMaterial = ScratchedMetalMat()
    frame_mat3: BlMaterial = ScratchedPlasticMat()
    frame_mat4: BlMaterial = BrushedChromeMat()


class CubesatGeo(BlGeometry):
    ops: List[SerializeAsAny[BlGeometryOp]] = [CubesatNodes()]

from pathlib import Path

from pydantic import PositiveInt
from simforge import BlGeometryNodesModifier, BlMaterial, BlNodesFromPython


class RandomMaterialNodes(BlGeometryNodesModifier):
    nodes: BlNodesFromPython = BlNodesFromPython(
        name="random_material",
        python_file=Path(__file__).parent.joinpath("nodes.py"),
    )

    mat_count: PositiveInt = 2
    mat0: BlMaterial | None = None
    mat1: BlMaterial | None = None
    mat2: BlMaterial | None = None
    mat3: BlMaterial | None = None
    mat4: BlMaterial | None = None
    mat5: BlMaterial | None = None
    mat6: BlMaterial | None = None
    mat7: BlMaterial | None = None
    mat8: BlMaterial | None = None
    mat9: BlMaterial | None = None
    mat10: BlMaterial | None = None
    mat11: BlMaterial | None = None
    mat12: BlMaterial | None = None
    mat13: BlMaterial | None = None
    mat14: BlMaterial | None = None
    mat15: BlMaterial | None = None
    mat16: BlMaterial | None = None
    mat17: BlMaterial | None = None
    mat18: BlMaterial | None = None
    mat19: BlMaterial | None = None
    mat20: BlMaterial | None = None
    mat21: BlMaterial | None = None
    mat22: BlMaterial | None = None
    mat23: BlMaterial | None = None
    mat24: BlMaterial | None = None
    mat25: BlMaterial | None = None
    mat26: BlMaterial | None = None
    mat27: BlMaterial | None = None
    mat28: BlMaterial | None = None
    mat29: BlMaterial | None = None
    mat30: BlMaterial | None = None
    mat31: BlMaterial | None = None

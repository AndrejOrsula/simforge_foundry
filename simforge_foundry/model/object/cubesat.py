from pydantic import InstanceOf, SerializeAsAny
from simforge import BakeType, BlGeometry, BlModel, TexResConfig

from simforge_foundry.geometry import CubesatGeo


class Cubesat(BlModel):
    geo: SerializeAsAny[InstanceOf[BlGeometry]] = CubesatGeo()
    mat: None = None  # Set via Geometry Nodes
    texture_resolution: TexResConfig = {
        BakeType.ALBEDO: 512,
        BakeType.METALLIC: 256,
        BakeType.NORMAL: 1024,
        BakeType.ROUGHNESS: 256,
    }

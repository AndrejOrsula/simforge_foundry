from pydantic import InstanceOf, SerializeAsAny
from simforge import BakeType, BlGeometry, BlModel, TexResConfig

from simforge_foundry.geometry import BagRandomGeo


class BagRandom(BlModel):
    geo: SerializeAsAny[InstanceOf[BlGeometry]] = BagRandomGeo()
    mat: None = None  # Set via Geometry Nodes
    texture_resolution: TexResConfig = {
        BakeType.ALBEDO: 1024,
        BakeType.METALLIC: 512,
        BakeType.NORMAL: 1024,
        BakeType.ROUGHNESS: 512,
    }

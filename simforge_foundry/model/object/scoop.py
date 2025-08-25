from pydantic import InstanceOf, SerializeAsAny
from simforge import BakeType, BlGeometry, BlMaterial, BlModel, TexResConfig

from simforge_foundry.geometry import ScoopRandomGeo
from simforge_foundry.material import ScratchedMetalMat


class ScoopRandom(BlModel):
    geo: SerializeAsAny[InstanceOf[BlGeometry]] = ScoopRandomGeo()
    mat: SerializeAsAny[InstanceOf[BlMaterial]] | None = ScratchedMetalMat()
    texture_resolution: TexResConfig = {
        BakeType.ALBEDO: 1024,
        BakeType.METALLIC: 512,
        BakeType.NORMAL: 1024,
        BakeType.ROUGHNESS: 512,
    }

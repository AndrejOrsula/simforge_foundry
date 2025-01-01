from pydantic import InstanceOf, SerializeAsAny
from simforge import BakeType, BlGeometry, BlMaterial, BlModel, TexResConfig

from simforge_foundry.geometry import RockGeo
from simforge_foundry.material import MarsRockMat, MoonRockMat


class MoonRock(BlModel):
    geo: SerializeAsAny[InstanceOf[BlGeometry]] = RockGeo()
    mat: SerializeAsAny[InstanceOf[BlMaterial]] | None = MoonRockMat()
    texture_resolution: TexResConfig = {
        BakeType.ALBEDO: 256,
        BakeType.NORMAL: 512,
        BakeType.ROUGHNESS: 128,
    }


class MarsRock(BlModel):
    geo: SerializeAsAny[InstanceOf[BlGeometry]] = RockGeo()
    mat: SerializeAsAny[InstanceOf[BlMaterial]] | None = MarsRockMat()
    texture_resolution: TexResConfig = {
        BakeType.ALBEDO: 256,
        BakeType.NORMAL: 512,
        BakeType.ROUGHNESS: 128,
    }

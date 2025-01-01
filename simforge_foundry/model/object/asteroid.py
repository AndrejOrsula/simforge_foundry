from pydantic import InstanceOf, SerializeAsAny
from simforge import BakeType, BlGeometry, BlMaterial, BlModel, TexResConfig

from simforge_foundry.geometry import AsteroidGeo
from simforge_foundry.material import AsteroidMat


class Asteroid(BlModel):
    geo: SerializeAsAny[InstanceOf[BlGeometry]] = AsteroidGeo()
    mat: SerializeAsAny[InstanceOf[BlMaterial]] | None = AsteroidMat()
    texture_resolution: TexResConfig = {
        BakeType.ALBEDO: 256,
        BakeType.NORMAL: 1024,
    }

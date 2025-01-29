from pydantic import InstanceOf, SerializeAsAny
from simforge import BakeType, BlGeometry, BlMaterial, BlModel, TexResConfig

from simforge_foundry.geometry import MarsSurfaceGeo, MoonSurfaceGeo
from simforge_foundry.material import MarsSurfaceMat, MoonSurfaceMat


class MoonSurface(BlModel):
    geo: SerializeAsAny[InstanceOf[BlGeometry]] = MoonSurfaceGeo()
    mat: SerializeAsAny[InstanceOf[BlMaterial]] | None = MoonSurfaceMat()
    texture_resolution: TexResConfig = {
        BakeType.ALBEDO: 1024,
        BakeType.NORMAL: 2048,
        BakeType.ROUGHNESS: 512,
    }


class MarsSurface(BlModel):
    geo: SerializeAsAny[InstanceOf[BlGeometry]] = MarsSurfaceGeo()
    mat: SerializeAsAny[InstanceOf[BlMaterial]] | None = MarsSurfaceMat()
    texture_resolution: TexResConfig = {
        BakeType.ALBEDO: 1024,
        BakeType.NORMAL: 2048,
        BakeType.ROUGHNESS: 512,
    }

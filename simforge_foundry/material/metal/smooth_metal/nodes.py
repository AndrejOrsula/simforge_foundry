import bpy, mathutils

mat = bpy.data.materials.new(name = "Smooth Metal")
mat.use_nodes = True
#initialize Smooth Metal node group
def smooth_metal_node_group():

    smooth_metal = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "Smooth Metal")

    smooth_metal.color_tag = 'NONE'
    smooth_metal.description = ""
    smooth_metal.default_group_node_width = 140
    

    #smooth_metal interface
    #Socket Shader
    shader_socket = smooth_metal.interface.new_socket(name = "Shader", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    shader_socket.attribute_domain = 'POINT'
    shader_socket.default_input = 'VALUE'
    shader_socket.structure_type = 'AUTO'

    #Socket Scale
    scale_socket = smooth_metal.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    #Socket Base Color
    base_color_socket = smooth_metal.interface.new_socket(name = "Base Color", in_out='INPUT', socket_type = 'NodeSocketColor')
    base_color_socket.default_value = (0.457051545381546, 0.457051545381546, 0.457051545381546, 1.0)
    base_color_socket.attribute_domain = 'POINT'
    base_color_socket.default_input = 'VALUE'
    base_color_socket.structure_type = 'AUTO'

    #Socket Metallic
    metallic_socket = smooth_metal.interface.new_socket(name = "Metallic", in_out='INPUT', socket_type = 'NodeSocketFloat')
    metallic_socket.default_value = 1.0
    metallic_socket.min_value = 0.0
    metallic_socket.max_value = 1.0
    metallic_socket.subtype = 'FACTOR'
    metallic_socket.attribute_domain = 'POINT'
    metallic_socket.default_input = 'VALUE'
    metallic_socket.structure_type = 'AUTO'

    #Socket Detail
    detail_socket = smooth_metal.interface.new_socket(name = "Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detail_socket.default_value = 10.0
    detail_socket.min_value = 0.0
    detail_socket.max_value = 15.0
    detail_socket.subtype = 'NONE'
    detail_socket.attribute_domain = 'POINT'
    detail_socket.default_input = 'VALUE'
    detail_socket.structure_type = 'AUTO'

    #Socket Roughness
    roughness_socket = smooth_metal.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = 'NONE'
    roughness_socket.attribute_domain = 'POINT'
    roughness_socket.default_input = 'VALUE'
    roughness_socket.structure_type = 'AUTO'

    #Socket Bump Strength
    bump_strength_socket = smooth_metal.interface.new_socket(name = "Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    bump_strength_socket.default_value = 0.009999999776482582
    bump_strength_socket.min_value = 0.0
    bump_strength_socket.max_value = 1.0
    bump_strength_socket.subtype = 'FACTOR'
    bump_strength_socket.attribute_domain = 'POINT'
    bump_strength_socket.default_input = 'VALUE'
    bump_strength_socket.structure_type = 'AUTO'


    #initialize smooth_metal nodes
    #node Group Output
    group_output = smooth_metal.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = smooth_metal.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Principled BSDF
    principled_bsdf = smooth_metal.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    #IOR
    principled_bsdf.inputs[3].default_value = 1.5
    #Alpha
    principled_bsdf.inputs[4].default_value = 1.0
    #Diffuse Roughness
    principled_bsdf.inputs[7].default_value = 0.0
    #Subsurface Weight
    principled_bsdf.inputs[8].default_value = 0.0
    #Subsurface Radius
    principled_bsdf.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    #Subsurface Scale
    principled_bsdf.inputs[10].default_value = 0.05000000074505806
    #Subsurface Anisotropy
    principled_bsdf.inputs[12].default_value = 0.0
    #Specular IOR Level
    principled_bsdf.inputs[13].default_value = 0.5
    #Specular Tint
    principled_bsdf.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    #Anisotropic
    principled_bsdf.inputs[15].default_value = 0.0
    #Anisotropic Rotation
    principled_bsdf.inputs[16].default_value = 0.0
    #Tangent
    principled_bsdf.inputs[17].default_value = (0.0, 0.0, 0.0)
    #Transmission Weight
    principled_bsdf.inputs[18].default_value = 0.0
    #Coat Weight
    principled_bsdf.inputs[19].default_value = 0.0
    #Coat Roughness
    principled_bsdf.inputs[20].default_value = 0.029999999329447746
    #Coat IOR
    principled_bsdf.inputs[21].default_value = 1.5
    #Coat Tint
    principled_bsdf.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    #Coat Normal
    principled_bsdf.inputs[23].default_value = (0.0, 0.0, 0.0)
    #Sheen Weight
    principled_bsdf.inputs[24].default_value = 0.0
    #Sheen Roughness
    principled_bsdf.inputs[25].default_value = 0.5
    #Sheen Tint
    principled_bsdf.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    #Emission Color
    principled_bsdf.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    #Emission Strength
    principled_bsdf.inputs[28].default_value = 0.0
    #Thin Film Thickness
    principled_bsdf.inputs[29].default_value = 0.0
    #Thin Film IOR
    principled_bsdf.inputs[30].default_value = 1.3300000429153442

    #node Voronoi Texture
    voronoi_texture = smooth_metal.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = 'EUCLIDEAN'
    voronoi_texture.feature = 'F1'
    voronoi_texture.normalize = False
    voronoi_texture.voronoi_dimensions = '3D'
    #Scale
    voronoi_texture.inputs[2].default_value = 20.0
    #Roughness
    voronoi_texture.inputs[4].default_value = 0.5
    #Lacunarity
    voronoi_texture.inputs[5].default_value = 2.0
    #Randomness
    voronoi_texture.inputs[8].default_value = 1.0

    #node Mapping
    mapping = smooth_metal.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = 'POINT'
    #Location
    mapping.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    mapping.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Texture Coordinate
    texture_coordinate = smooth_metal.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False

    #node Noise Texture
    noise_texture = smooth_metal.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    #Scale
    noise_texture.inputs[2].default_value = 3.0
    #Roughness
    noise_texture.inputs[4].default_value = 0.44999998807907104
    #Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    #Distortion
    noise_texture.inputs[8].default_value = 0.0

    #node Mix
    mix = smooth_metal.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'LINEAR_LIGHT'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'
    #Factor_Float
    mix.inputs[0].default_value = 0.30000001192092896

    #node ColorRamp
    colorramp = smooth_metal.nodes.new("ShaderNodeValToRGB")
    colorramp.name = "ColorRamp"
    colorramp.color_ramp.color_mode = 'RGB'
    colorramp.color_ramp.hue_interpolation = 'NEAR'
    colorramp.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    colorramp.color_ramp.elements.remove(colorramp.color_ramp.elements[0])
    colorramp_cre_0 = colorramp.color_ramp.elements[0]
    colorramp_cre_0.position = 0.3550724983215332
    colorramp_cre_0.alpha = 1.0
    colorramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    colorramp_cre_1 = colorramp.color_ramp.elements.new(0.5942029356956482)
    colorramp_cre_1.alpha = 1.0
    colorramp_cre_1.color = (0.40373504161834717, 0.40373504161834717, 0.40373504161834717, 1.0)


    #node Hue/Saturation/Value
    hue_saturation_value = smooth_metal.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    #Hue
    hue_saturation_value.inputs[0].default_value = 0.5
    #Saturation
    hue_saturation_value.inputs[1].default_value = 1.0
    #Fac
    hue_saturation_value.inputs[3].default_value = 1.0

    #node Noise Texture.001
    noise_texture_001 = smooth_metal.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = '3D'
    noise_texture_001.noise_type = 'FBM'
    noise_texture_001.normalize = True
    #Scale
    noise_texture_001.inputs[2].default_value = 2.0
    #Roughness
    noise_texture_001.inputs[4].default_value = 1.0
    #Lacunarity
    noise_texture_001.inputs[5].default_value = 2.0
    #Distortion
    noise_texture_001.inputs[8].default_value = 0.0

    #node Mix.001
    mix_001 = smooth_metal.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'LINEAR_LIGHT'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'RGBA'
    mix_001.factor_mode = 'UNIFORM'
    #Factor_Float
    mix_001.inputs[0].default_value = 0.029999999329447746

    #node Bump
    bump = smooth_metal.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    #Distance
    bump.inputs[1].default_value = 1.0
    #Filter Width
    bump.inputs[2].default_value = 0.10000000149011612
    #Normal
    bump.inputs[4].default_value = (0.0, 0.0, 0.0)


    #Set locations
    group_output.location = (0.0, 0.0)
    group_input.location = (0.0, 0.0)
    principled_bsdf.location = (0.0, 0.0)
    voronoi_texture.location = (0.0, 0.0)
    mapping.location = (0.0, 0.0)
    texture_coordinate.location = (0.0, 0.0)
    noise_texture.location = (0.0, 0.0)
    mix.location = (0.0, 0.0)
    colorramp.location = (0.0, 0.0)
    hue_saturation_value.location = (0.0, 0.0)
    noise_texture_001.location = (0.0, 0.0)
    mix_001.location = (0.0, 0.0)
    bump.location = (0.0, 0.0)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    principled_bsdf.width, principled_bsdf.height = 240.0, 100.0
    voronoi_texture.width, voronoi_texture.height = 140.0, 100.0
    mapping.width, mapping.height = 140.0, 100.0
    texture_coordinate.width, texture_coordinate.height = 140.0, 100.0
    noise_texture.width, noise_texture.height = 140.0, 100.0
    mix.width, mix.height = 140.0, 100.0
    colorramp.width, colorramp.height = 240.0, 100.0
    hue_saturation_value.width, hue_saturation_value.height = 150.0, 100.0
    noise_texture_001.width, noise_texture_001.height = 140.0, 100.0
    mix_001.width, mix_001.height = 140.0, 100.0
    bump.width, bump.height = 140.0, 100.0

    #initialize smooth_metal links
    #mapping.Vector -> mix.A
    smooth_metal.links.new(mapping.outputs[0], mix.inputs[6])
    #texture_coordinate.Object -> mapping.Vector
    smooth_metal.links.new(texture_coordinate.outputs[3], mapping.inputs[0])
    #noise_texture_001.Color -> bump.Height
    smooth_metal.links.new(noise_texture_001.outputs[1], bump.inputs[3])
    #voronoi_texture.Distance -> mix.B
    smooth_metal.links.new(voronoi_texture.outputs[0], mix.inputs[7])
    #mix.Result -> noise_texture.Vector
    smooth_metal.links.new(mix.outputs[2], noise_texture.inputs[0])
    #mix_001.Result -> noise_texture_001.Vector
    smooth_metal.links.new(mix_001.outputs[2], noise_texture_001.inputs[0])
    #hue_saturation_value.Color -> principled_bsdf.Roughness
    smooth_metal.links.new(hue_saturation_value.outputs[0], principled_bsdf.inputs[2])
    #mapping.Vector -> mix_001.A
    smooth_metal.links.new(mapping.outputs[0], mix_001.inputs[6])
    #noise_texture_001.Color -> colorramp.Fac
    smooth_metal.links.new(noise_texture_001.outputs[1], colorramp.inputs[0])
    #noise_texture.Color -> mix_001.B
    smooth_metal.links.new(noise_texture.outputs[1], mix_001.inputs[7])
    #colorramp.Color -> hue_saturation_value.Color
    smooth_metal.links.new(colorramp.outputs[0], hue_saturation_value.inputs[4])
    #mapping.Vector -> voronoi_texture.Vector
    smooth_metal.links.new(mapping.outputs[0], voronoi_texture.inputs[0])
    #bump.Normal -> principled_bsdf.Normal
    smooth_metal.links.new(bump.outputs[0], principled_bsdf.inputs[5])
    #principled_bsdf.BSDF -> group_output.Shader
    smooth_metal.links.new(principled_bsdf.outputs[0], group_output.inputs[0])
    #group_input.Scale -> mapping.Scale
    smooth_metal.links.new(group_input.outputs[0], mapping.inputs[3])
    #group_input.Detail -> voronoi_texture.Detail
    smooth_metal.links.new(group_input.outputs[3], voronoi_texture.inputs[3])
    #group_input.Detail -> noise_texture.Detail
    smooth_metal.links.new(group_input.outputs[3], noise_texture.inputs[3])
    #group_input.Detail -> noise_texture_001.Detail
    smooth_metal.links.new(group_input.outputs[3], noise_texture_001.inputs[3])
    #group_input.Roughness -> hue_saturation_value.Value
    smooth_metal.links.new(group_input.outputs[4], hue_saturation_value.inputs[2])
    #group_input.Bump Strength -> bump.Strength
    smooth_metal.links.new(group_input.outputs[5], bump.inputs[0])
    #group_input.Base Color -> principled_bsdf.Base Color
    smooth_metal.links.new(group_input.outputs[1], principled_bsdf.inputs[0])
    #group_input.Metallic -> principled_bsdf.Metallic
    smooth_metal.links.new(group_input.outputs[2], principled_bsdf.inputs[1])
    return smooth_metal

smooth_metal = smooth_metal_node_group()

#initialize Smooth Metal node group
def smooth_metal_1_node_group():

    smooth_metal_1 = mat.node_tree
    #start with a clean node tree
    for node in smooth_metal_1.nodes:
        smooth_metal_1.nodes.remove(node)
    smooth_metal_1.color_tag = 'NONE'
    smooth_metal_1.description = ""
    smooth_metal_1.default_group_node_width = 140
    

    #smooth_metal_1 interface

    #initialize smooth_metal_1 nodes
    #node Material Output
    material_output = smooth_metal_1.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    #Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Thickness
    material_output.inputs[3].default_value = 0.0

    #node Group
    group = smooth_metal_1.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = smooth_metal
    #Socket_1
    group.inputs[0].default_value = 1.0
    #Socket_2
    group.inputs[1].default_value = (0.457051545381546, 0.457051545381546, 0.457051545381546, 1.0)
    #Socket_3
    group.inputs[2].default_value = 1.0
    #Socket_4
    group.inputs[3].default_value = 10.0
    #Socket_5
    group.inputs[4].default_value = 1.0
    #Socket_6
    group.inputs[5].default_value = 0.009999999776482582


    #Set locations
    material_output.location = (0.0, 0.0)
    group.location = (0.0, 0.0)

    #Set dimensions
    material_output.width, material_output.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0

    #initialize smooth_metal_1 links
    #group.Shader -> material_output.Surface
    smooth_metal_1.links.new(group.outputs[0], material_output.inputs[0])
    return smooth_metal_1

smooth_metal_1 = smooth_metal_1_node_group()


import bpy, mathutils

mat = bpy.data.materials.new(name = "ScratchedMetal")
mat.use_nodes = True
#initialize ScratchedMetalShader node group
def scratchedmetalshader_node_group():

    scratchedmetalshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "ScratchedMetalShader")

    scratchedmetalshader.color_tag = 'NONE'
    scratchedmetalshader.description = ""
    scratchedmetalshader.default_group_node_width = 140
    

    #scratchedmetalshader interface
    #Socket Shader
    shader_socket = scratchedmetalshader.interface.new_socket(name = "Shader", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    shader_socket.attribute_domain = 'POINT'
    shader_socket.default_input = 'VALUE'
    shader_socket.structure_type = 'AUTO'

    #Socket Scale
    scale_socket = scratchedmetalshader.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    #Socket Metallic
    metallic_socket = scratchedmetalshader.interface.new_socket(name = "Metallic", in_out='INPUT', socket_type = 'NodeSocketFloat')
    metallic_socket.default_value = 1.0
    metallic_socket.min_value = 0.0
    metallic_socket.max_value = 1.0
    metallic_socket.subtype = 'FACTOR'
    metallic_socket.attribute_domain = 'POINT'
    metallic_socket.default_input = 'VALUE'
    metallic_socket.structure_type = 'AUTO'

    #Socket Metal Color 1
    metal_color_1_socket = scratchedmetalshader.interface.new_socket(name = "Metal Color 1", in_out='INPUT', socket_type = 'NodeSocketColor')
    metal_color_1_socket.default_value = (0.17062200605869293, 0.17062200605869293, 0.17062200605869293, 1.0)
    metal_color_1_socket.attribute_domain = 'POINT'
    metal_color_1_socket.default_input = 'VALUE'
    metal_color_1_socket.structure_type = 'AUTO'

    #Socket Metal Color 2
    metal_color_2_socket = scratchedmetalshader.interface.new_socket(name = "Metal Color 2", in_out='INPUT', socket_type = 'NodeSocketColor')
    metal_color_2_socket.default_value = (0.03146599978208542, 0.03146599978208542, 0.03146599978208542, 1.0)
    metal_color_2_socket.attribute_domain = 'POINT'
    metal_color_2_socket.default_input = 'VALUE'
    metal_color_2_socket.structure_type = 'AUTO'

    #Socket Noise Scale
    noise_scale_socket = scratchedmetalshader.interface.new_socket(name = "Noise Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_scale_socket.default_value = 1.0
    noise_scale_socket.min_value = -3.4028234663852886e+38
    noise_scale_socket.max_value = 3.4028234663852886e+38
    noise_scale_socket.subtype = 'NONE'
    noise_scale_socket.attribute_domain = 'POINT'
    noise_scale_socket.default_input = 'VALUE'
    noise_scale_socket.structure_type = 'AUTO'

    #Socket Scratches Scale
    scratches_scale_socket = scratchedmetalshader.interface.new_socket(name = "Scratches Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_scale_socket.default_value = 1.0
    scratches_scale_socket.min_value = -3.4028234663852886e+38
    scratches_scale_socket.max_value = 3.4028234663852886e+38
    scratches_scale_socket.subtype = 'NONE'
    scratches_scale_socket.attribute_domain = 'POINT'
    scratches_scale_socket.default_input = 'VALUE'
    scratches_scale_socket.structure_type = 'AUTO'

    #Socket Scratches Color
    scratches_color_socket = scratchedmetalshader.interface.new_socket(name = "Scratches Color", in_out='INPUT', socket_type = 'NodeSocketColor')
    scratches_color_socket.default_value = (0.10046499967575073, 0.10046499967575073, 0.10046499967575073, 1.0)
    scratches_color_socket.attribute_domain = 'POINT'
    scratches_color_socket.default_input = 'VALUE'
    scratches_color_socket.structure_type = 'AUTO'

    #Socket Roughness
    roughness_socket = scratchedmetalshader.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = 'NONE'
    roughness_socket.attribute_domain = 'POINT'
    roughness_socket.default_input = 'VALUE'
    roughness_socket.structure_type = 'AUTO'

    #Socket Noise Bump Strength
    noise_bump_strength_socket = scratchedmetalshader.interface.new_socket(name = "Noise Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_strength_socket.default_value = 0.05000000074505806
    noise_bump_strength_socket.min_value = 0.0
    noise_bump_strength_socket.max_value = 1.0
    noise_bump_strength_socket.subtype = 'FACTOR'
    noise_bump_strength_socket.attribute_domain = 'POINT'
    noise_bump_strength_socket.default_input = 'VALUE'
    noise_bump_strength_socket.structure_type = 'AUTO'

    #Socket Scratches Bump Strength
    scratches_bump_strength_socket = scratchedmetalshader.interface.new_socket(name = "Scratches Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_bump_strength_socket.default_value = 0.10000000149011612
    scratches_bump_strength_socket.min_value = 0.0
    scratches_bump_strength_socket.max_value = 1.0
    scratches_bump_strength_socket.subtype = 'FACTOR'
    scratches_bump_strength_socket.attribute_domain = 'POINT'
    scratches_bump_strength_socket.default_input = 'VALUE'
    scratches_bump_strength_socket.structure_type = 'AUTO'


    #initialize scratchedmetalshader nodes
    #node Frame
    frame = scratchedmetalshader.nodes.new("NodeFrame")
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    #node Frame.002
    frame_002 = scratchedmetalshader.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    #node Frame.003
    frame_003 = scratchedmetalshader.nodes.new("NodeFrame")
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    #node Frame.004
    frame_004 = scratchedmetalshader.nodes.new("NodeFrame")
    frame_004.name = "Frame.004"
    frame_004.label_size = 20
    frame_004.shrink = True

    #node Frame.001
    frame_001 = scratchedmetalshader.nodes.new("NodeFrame")
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    #node Frame.005
    frame_005 = scratchedmetalshader.nodes.new("NodeFrame")
    frame_005.name = "Frame.005"
    frame_005.label_size = 20
    frame_005.shrink = True

    #node Group Output
    group_output = scratchedmetalshader.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Texture Coordinate
    texture_coordinate = scratchedmetalshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False

    #node Noise Texture.002
    noise_texture_002 = scratchedmetalshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_002.name = "Noise Texture.002"
    noise_texture_002.noise_dimensions = '3D'
    noise_texture_002.noise_type = 'FBM'
    noise_texture_002.normalize = True
    #Scale
    noise_texture_002.inputs[2].default_value = 15.0
    #Detail
    noise_texture_002.inputs[3].default_value = 15.0
    #Roughness
    noise_texture_002.inputs[4].default_value = 0.5
    #Lacunarity
    noise_texture_002.inputs[5].default_value = 2.0
    #Distortion
    noise_texture_002.inputs[8].default_value = 0.0

    #node Color Ramp.004
    color_ramp_004 = scratchedmetalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_004.name = "Color Ramp.004"
    color_ramp_004.color_ramp.color_mode = 'RGB'
    color_ramp_004.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_004.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    color_ramp_004.color_ramp.elements.remove(color_ramp_004.color_ramp.elements[0])
    color_ramp_004_cre_0 = color_ramp_004.color_ramp.elements[0]
    color_ramp_004_cre_0.position = 0.3718593120574951
    color_ramp_004_cre_0.alpha = 1.0
    color_ramp_004_cre_0.color = (0.502767026424408, 0.502767026424408, 0.502767026424408, 1.0)

    color_ramp_004_cre_1 = color_ramp_004.color_ramp.elements.new(0.6457287073135376)
    color_ramp_004_cre_1.alpha = 1.0
    color_ramp_004_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Color Ramp.005
    color_ramp_005 = scratchedmetalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_005.name = "Color Ramp.005"
    color_ramp_005.color_ramp.color_mode = 'RGB'
    color_ramp_005.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_005.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    color_ramp_005.color_ramp.elements.remove(color_ramp_005.color_ramp.elements[0])
    color_ramp_005_cre_0 = color_ramp_005.color_ramp.elements[0]
    color_ramp_005_cre_0.position = 0.14824114739894867
    color_ramp_005_cre_0.alpha = 1.0
    color_ramp_005_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_005_cre_1 = color_ramp_005.color_ramp.elements.new(0.8040200471878052)
    color_ramp_005_cre_1.alpha = 1.0
    color_ramp_005_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Mix.003
    mix_003 = scratchedmetalshader.nodes.new("ShaderNodeMix")
    mix_003.name = "Mix.003"
    mix_003.blend_type = 'MIX'
    mix_003.clamp_factor = True
    mix_003.clamp_result = False
    mix_003.data_type = 'RGBA'
    mix_003.factor_mode = 'UNIFORM'

    #node Color Ramp.006
    color_ramp_006 = scratchedmetalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_006.name = "Color Ramp.006"
    color_ramp_006.color_ramp.color_mode = 'RGB'
    color_ramp_006.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_006.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    color_ramp_006.color_ramp.elements.remove(color_ramp_006.color_ramp.elements[0])
    color_ramp_006_cre_0 = color_ramp_006.color_ramp.elements[0]
    color_ramp_006_cre_0.position = 0.0
    color_ramp_006_cre_0.alpha = 1.0
    color_ramp_006_cre_0.color = (0.2911059856414795, 0.2911059856414795, 0.2911059856414795, 1.0)

    color_ramp_006_cre_1 = color_ramp_006.color_ramp.elements.new(1.0)
    color_ramp_006_cre_1.alpha = 1.0
    color_ramp_006_cre_1.color = (0.596705973148346, 0.596705973148346, 0.596705973148346, 1.0)


    #node Voronoi Texture
    voronoi_texture = scratchedmetalshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = 'EUCLIDEAN'
    voronoi_texture.feature = 'DISTANCE_TO_EDGE'
    voronoi_texture.normalize = False
    voronoi_texture.voronoi_dimensions = '3D'
    #Scale
    voronoi_texture.inputs[2].default_value = 50.0
    #Detail
    voronoi_texture.inputs[3].default_value = 15.0
    #Roughness
    voronoi_texture.inputs[4].default_value = 0.75
    #Lacunarity
    voronoi_texture.inputs[5].default_value = 2.0
    #Randomness
    voronoi_texture.inputs[8].default_value = 1.0

    #node Voronoi Texture.001
    voronoi_texture_001 = scratchedmetalshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001.name = "Voronoi Texture.001"
    voronoi_texture_001.distance = 'EUCLIDEAN'
    voronoi_texture_001.feature = 'DISTANCE_TO_EDGE'
    voronoi_texture_001.normalize = False
    voronoi_texture_001.voronoi_dimensions = '3D'
    #Scale
    voronoi_texture_001.inputs[2].default_value = 114.0
    #Detail
    voronoi_texture_001.inputs[3].default_value = 15.0
    #Roughness
    voronoi_texture_001.inputs[4].default_value = 0.75
    #Lacunarity
    voronoi_texture_001.inputs[5].default_value = 2.0
    #Randomness
    voronoi_texture_001.inputs[8].default_value = 1.0

    #node Color Ramp
    color_ramp = scratchedmetalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp.name = "Color Ramp"
    color_ramp.color_ramp.color_mode = 'RGB'
    color_ramp.color_ramp.hue_interpolation = 'NEAR'
    color_ramp.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
    color_ramp_cre_0 = color_ramp.color_ramp.elements[0]
    color_ramp_cre_0.position = 0.0
    color_ramp_cre_0.alpha = 1.0
    color_ramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_cre_1 = color_ramp.color_ramp.elements.new(0.037688400596380234)
    color_ramp_cre_1.alpha = 1.0
    color_ramp_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Noise Texture
    noise_texture = scratchedmetalshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    #Scale
    noise_texture.inputs[2].default_value = 35.0
    #Detail
    noise_texture.inputs[3].default_value = 15.0
    #Roughness
    noise_texture.inputs[4].default_value = 0.7300000190734863
    #Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    #Distortion
    noise_texture.inputs[8].default_value = 0.0

    #node Color Ramp.001
    color_ramp_001 = scratchedmetalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_001.name = "Color Ramp.001"
    color_ramp_001.color_ramp.color_mode = 'RGB'
    color_ramp_001.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_001.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    color_ramp_001.color_ramp.elements.remove(color_ramp_001.color_ramp.elements[0])
    color_ramp_001_cre_0 = color_ramp_001.color_ramp.elements[0]
    color_ramp_001_cre_0.position = 0.0
    color_ramp_001_cre_0.alpha = 1.0
    color_ramp_001_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_001_cre_1 = color_ramp_001.color_ramp.elements.new(0.037688400596380234)
    color_ramp_001_cre_1.alpha = 1.0
    color_ramp_001_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Mix
    mix = scratchedmetalshader.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'DARKEN'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'
    #Factor_Float
    mix.inputs[0].default_value = 1.0

    #node Mix.001
    mix_001 = scratchedmetalshader.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'LIGHTEN'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'RGBA'
    mix_001.factor_mode = 'UNIFORM'
    #B_Color
    mix_001.inputs[7].default_value = (1.0, 1.0, 1.0, 1.0)

    #node Color Ramp.002
    color_ramp_002 = scratchedmetalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_002.name = "Color Ramp.002"
    color_ramp_002.color_ramp.color_mode = 'RGB'
    color_ramp_002.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_002.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    color_ramp_002.color_ramp.elements.remove(color_ramp_002.color_ramp.elements[0])
    color_ramp_002_cre_0 = color_ramp_002.color_ramp.elements[0]
    color_ramp_002_cre_0.position = 0.40703511238098145
    color_ramp_002_cre_0.alpha = 1.0
    color_ramp_002_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_002_cre_1 = color_ramp_002.color_ramp.elements.new(0.6532663106918335)
    color_ramp_002_cre_1.alpha = 1.0
    color_ramp_002_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Color Ramp.003
    color_ramp_003 = scratchedmetalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_003.name = "Color Ramp.003"
    color_ramp_003.color_ramp.color_mode = 'RGB'
    color_ramp_003.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_003.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    color_ramp_003.color_ramp.elements.remove(color_ramp_003.color_ramp.elements[0])
    color_ramp_003_cre_0 = color_ramp_003.color_ramp.elements[0]
    color_ramp_003_cre_0.position = 0.0
    color_ramp_003_cre_0.alpha = 1.0
    color_ramp_003_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_003_cre_1 = color_ramp_003.color_ramp.elements.new(0.4321606159210205)
    color_ramp_003_cre_1.alpha = 1.0
    color_ramp_003_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Mapping
    mapping = scratchedmetalshader.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = 'POINT'
    #Location
    mapping.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    mapping.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Principled BSDF
    principled_bsdf = scratchedmetalshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    #IOR
    principled_bsdf.inputs[3].default_value = 1.4500000476837158
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

    #node Mix.002
    mix_002 = scratchedmetalshader.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = 'MIX'
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = 'RGBA'
    mix_002.factor_mode = 'UNIFORM'

    #node Reroute
    reroute = scratchedmetalshader.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketVector"
    #node Reroute.001
    reroute_001 = scratchedmetalshader.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketVector"
    #node Mapping.002
    mapping_002 = scratchedmetalshader.nodes.new("ShaderNodeMapping")
    mapping_002.name = "Mapping.002"
    mapping_002.vector_type = 'POINT'
    #Location
    mapping_002.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    mapping_002.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Mapping.001
    mapping_001 = scratchedmetalshader.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = 'POINT'
    #Location
    mapping_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Hue/Saturation/Value
    hue_saturation_value = scratchedmetalshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    #Hue
    hue_saturation_value.inputs[0].default_value = 0.5
    #Saturation
    hue_saturation_value.inputs[1].default_value = 1.0
    #Fac
    hue_saturation_value.inputs[3].default_value = 1.0

    #node Bump
    bump = scratchedmetalshader.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    #Distance
    bump.inputs[1].default_value = 1.0
    #Filter Width
    bump.inputs[2].default_value = 0.10000000149011612
    #Normal
    bump.inputs[4].default_value = (0.0, 0.0, 0.0)

    #node Bump.001
    bump_001 = scratchedmetalshader.nodes.new("ShaderNodeBump")
    bump_001.name = "Bump.001"
    bump_001.invert = False
    #Distance
    bump_001.inputs[1].default_value = 1.0
    #Filter Width
    bump_001.inputs[2].default_value = 0.10000000149011612

    #node Group Input
    group_input = scratchedmetalshader.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Noise Texture.001
    noise_texture_001 = scratchedmetalshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = '3D'
    noise_texture_001.noise_type = 'FBM'
    noise_texture_001.normalize = True
    #Scale
    noise_texture_001.inputs[2].default_value = 15.0
    #Detail
    noise_texture_001.inputs[3].default_value = 15.0
    #Lacunarity
    noise_texture_001.inputs[5].default_value = 2.0
    #Distortion
    noise_texture_001.inputs[8].default_value = 0.0

    #node Clamp
    clamp = scratchedmetalshader.nodes.new("ShaderNodeClamp")
    clamp.name = "Clamp"
    clamp.hide = True
    clamp.clamp_type = 'MINMAX'
    #Min
    clamp.inputs[1].default_value = 0.0
    #Max
    clamp.inputs[2].default_value = 1.0


    #Set locations
    frame.location = (0.0, 0.0)
    frame_002.location = (0.0, 0.0)
    frame_003.location = (0.0, 0.0)
    frame_004.location = (0.0, 0.0)
    frame_001.location = (0.0, 0.0)
    frame_005.location = (0.0, 0.0)
    group_output.location = (0.0, 0.0)
    texture_coordinate.location = (0.0, 0.0)
    noise_texture_002.location = (0.0, 0.0)
    color_ramp_004.location = (0.0, 0.0)
    color_ramp_005.location = (0.0, 0.0)
    mix_003.location = (0.0, 0.0)
    color_ramp_006.location = (0.0, 0.0)
    voronoi_texture.location = (0.0, 0.0)
    voronoi_texture_001.location = (0.0, 0.0)
    color_ramp.location = (0.0, 0.0)
    noise_texture.location = (0.0, 0.0)
    color_ramp_001.location = (0.0, 0.0)
    mix.location = (0.0, 0.0)
    mix_001.location = (0.0, 0.0)
    color_ramp_002.location = (0.0, 0.0)
    color_ramp_003.location = (0.0, 0.0)
    mapping.location = (0.0, 0.0)
    principled_bsdf.location = (0.0, 0.0)
    mix_002.location = (0.0, 0.0)
    reroute.location = (0.0, 0.0)
    reroute_001.location = (0.0, 0.0)
    mapping_002.location = (0.0, 0.0)
    mapping_001.location = (0.0, 0.0)
    hue_saturation_value.location = (0.0, 0.0)
    bump.location = (0.0, 0.0)
    bump_001.location = (0.0, 0.0)
    group_input.location = (0.0, 0.0)
    noise_texture_001.location = (0.0, 0.0)
    clamp.location = (0.0, 0.0)

    #Set dimensions
    frame.width, frame.height = 150.0, 100.0
    frame_002.width, frame_002.height = 150.0, 100.0
    frame_003.width, frame_003.height = 150.0, 100.0
    frame_004.width, frame_004.height = 150.0, 100.0
    frame_001.width, frame_001.height = 150.0, 100.0
    frame_005.width, frame_005.height = 150.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    texture_coordinate.width, texture_coordinate.height = 140.0, 100.0
    noise_texture_002.width, noise_texture_002.height = 140.0, 100.0
    color_ramp_004.width, color_ramp_004.height = 240.0, 100.0
    color_ramp_005.width, color_ramp_005.height = 240.0, 100.0
    mix_003.width, mix_003.height = 140.0, 100.0
    color_ramp_006.width, color_ramp_006.height = 240.0, 100.0
    voronoi_texture.width, voronoi_texture.height = 140.0, 100.0
    voronoi_texture_001.width, voronoi_texture_001.height = 140.0, 100.0
    color_ramp.width, color_ramp.height = 240.0, 100.0
    noise_texture.width, noise_texture.height = 140.0, 100.0
    color_ramp_001.width, color_ramp_001.height = 240.0, 100.0
    mix.width, mix.height = 140.0, 100.0
    mix_001.width, mix_001.height = 140.0, 100.0
    color_ramp_002.width, color_ramp_002.height = 240.0, 100.0
    color_ramp_003.width, color_ramp_003.height = 240.0, 100.0
    mapping.width, mapping.height = 140.0, 100.0
    principled_bsdf.width, principled_bsdf.height = 240.0, 100.0
    mix_002.width, mix_002.height = 140.0, 100.0
    reroute.width, reroute.height = 140.0, 100.0
    reroute_001.width, reroute_001.height = 140.0, 100.0
    mapping_002.width, mapping_002.height = 140.0, 100.0
    mapping_001.width, mapping_001.height = 140.0, 100.0
    hue_saturation_value.width, hue_saturation_value.height = 150.0, 100.0
    bump.width, bump.height = 140.0, 100.0
    bump_001.width, bump_001.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    noise_texture_001.width, noise_texture_001.height = 140.0, 100.0
    clamp.width, clamp.height = 140.0, 100.0

    #initialize scratchedmetalshader links
    #mix_003.Result -> principled_bsdf.Base Color
    scratchedmetalshader.links.new(mix_003.outputs[2], principled_bsdf.inputs[0])
    #mix_003.Result -> color_ramp_006.Fac
    scratchedmetalshader.links.new(mix_003.outputs[2], color_ramp_006.inputs[0])
    #noise_texture.Fac -> color_ramp_002.Fac
    scratchedmetalshader.links.new(noise_texture.outputs[0], color_ramp_002.inputs[0])
    #reroute_001.Output -> voronoi_texture.Vector
    scratchedmetalshader.links.new(reroute_001.outputs[0], voronoi_texture.inputs[0])
    #bump.Normal -> bump_001.Normal
    scratchedmetalshader.links.new(bump.outputs[0], bump_001.inputs[4])
    #mix.Result -> mix_001.A
    scratchedmetalshader.links.new(mix.outputs[2], mix_001.inputs[6])
    #reroute_001.Output -> noise_texture.Vector
    scratchedmetalshader.links.new(reroute_001.outputs[0], noise_texture.inputs[0])
    #color_ramp_003.Color -> mix_003.Factor
    scratchedmetalshader.links.new(color_ramp_003.outputs[0], mix_003.inputs[0])
    #reroute.Output -> noise_texture_002.Vector
    scratchedmetalshader.links.new(reroute.outputs[0], noise_texture_002.inputs[0])
    #voronoi_texture_001.Distance -> color_ramp_001.Fac
    scratchedmetalshader.links.new(voronoi_texture_001.outputs[0], color_ramp_001.inputs[0])
    #texture_coordinate.Object -> mapping.Vector
    scratchedmetalshader.links.new(texture_coordinate.outputs[3], mapping.inputs[0])
    #color_ramp_002.Color -> mix_001.Factor
    scratchedmetalshader.links.new(color_ramp_002.outputs[0], mix_001.inputs[0])
    #voronoi_texture.Distance -> color_ramp.Fac
    scratchedmetalshader.links.new(voronoi_texture.outputs[0], color_ramp.inputs[0])
    #noise_texture_002.Fac -> color_ramp_004.Fac
    scratchedmetalshader.links.new(noise_texture_002.outputs[0], color_ramp_004.inputs[0])
    #color_ramp_001.Color -> mix.A
    scratchedmetalshader.links.new(color_ramp_001.outputs[0], mix.inputs[6])
    #bump_001.Normal -> principled_bsdf.Normal
    scratchedmetalshader.links.new(bump_001.outputs[0], principled_bsdf.inputs[5])
    #reroute_001.Output -> voronoi_texture_001.Vector
    scratchedmetalshader.links.new(reroute_001.outputs[0], voronoi_texture_001.inputs[0])
    #noise_texture_001.Fac -> color_ramp_005.Fac
    scratchedmetalshader.links.new(noise_texture_001.outputs[0], color_ramp_005.inputs[0])
    #color_ramp_005.Color -> mix_002.Factor
    scratchedmetalshader.links.new(color_ramp_005.outputs[0], mix_002.inputs[0])
    #color_ramp_006.Color -> hue_saturation_value.Color
    scratchedmetalshader.links.new(color_ramp_006.outputs[0], hue_saturation_value.inputs[4])
    #noise_texture_001.Fac -> bump.Height
    scratchedmetalshader.links.new(noise_texture_001.outputs[0], bump.inputs[3])
    #mix_002.Result -> mix_003.B
    scratchedmetalshader.links.new(mix_002.outputs[2], mix_003.inputs[7])
    #reroute.Output -> noise_texture_001.Vector
    scratchedmetalshader.links.new(reroute.outputs[0], noise_texture_001.inputs[0])
    #mix_001.Result -> color_ramp_003.Fac
    scratchedmetalshader.links.new(mix_001.outputs[2], color_ramp_003.inputs[0])
    #color_ramp.Color -> mix.B
    scratchedmetalshader.links.new(color_ramp.outputs[0], mix.inputs[7])
    #hue_saturation_value.Color -> principled_bsdf.Roughness
    scratchedmetalshader.links.new(hue_saturation_value.outputs[0], principled_bsdf.inputs[2])
    #color_ramp_003.Color -> bump_001.Height
    scratchedmetalshader.links.new(color_ramp_003.outputs[0], bump_001.inputs[3])
    #principled_bsdf.BSDF -> group_output.Shader
    scratchedmetalshader.links.new(principled_bsdf.outputs[0], group_output.inputs[0])
    #group_input.Scale -> mapping.Scale
    scratchedmetalshader.links.new(group_input.outputs[0], mapping.inputs[3])
    #group_input.Metallic -> principled_bsdf.Metallic
    scratchedmetalshader.links.new(group_input.outputs[1], principled_bsdf.inputs[1])
    #group_input.Metal Color 1 -> mix_002.A
    scratchedmetalshader.links.new(group_input.outputs[2], mix_002.inputs[6])
    #group_input.Metal Color 2 -> mix_002.B
    scratchedmetalshader.links.new(group_input.outputs[3], mix_002.inputs[7])
    #mapping_002.Vector -> reroute.Input
    scratchedmetalshader.links.new(mapping_002.outputs[0], reroute.inputs[0])
    #mapping_001.Vector -> reroute_001.Input
    scratchedmetalshader.links.new(mapping_001.outputs[0], reroute_001.inputs[0])
    #mapping.Vector -> mapping_001.Vector
    scratchedmetalshader.links.new(mapping.outputs[0], mapping_001.inputs[0])
    #mapping.Vector -> mapping_002.Vector
    scratchedmetalshader.links.new(mapping.outputs[0], mapping_002.inputs[0])
    #group_input.Noise Scale -> mapping_002.Scale
    scratchedmetalshader.links.new(group_input.outputs[4], mapping_002.inputs[3])
    #group_input.Scratches Scale -> mapping_001.Scale
    scratchedmetalshader.links.new(group_input.outputs[5], mapping_001.inputs[3])
    #group_input.Scratches Color -> mix_003.A
    scratchedmetalshader.links.new(group_input.outputs[6], mix_003.inputs[6])
    #group_input.Roughness -> hue_saturation_value.Value
    scratchedmetalshader.links.new(group_input.outputs[7], hue_saturation_value.inputs[2])
    #group_input.Noise Bump Strength -> bump.Strength
    scratchedmetalshader.links.new(group_input.outputs[8], bump.inputs[0])
    #group_input.Scratches Bump Strength -> bump_001.Strength
    scratchedmetalshader.links.new(group_input.outputs[9], bump_001.inputs[0])
    #color_ramp_004.Color -> clamp.Value
    scratchedmetalshader.links.new(color_ramp_004.outputs[0], clamp.inputs[0])
    #clamp.Result -> noise_texture_001.Roughness
    scratchedmetalshader.links.new(clamp.outputs[0], noise_texture_001.inputs[4])
    return scratchedmetalshader

scratchedmetalshader = scratchedmetalshader_node_group()

#initialize ScratchedMetal node group
def scratchedmetal_node_group():

    scratchedmetal = mat.node_tree
    #start with a clean node tree
    for node in scratchedmetal.nodes:
        scratchedmetal.nodes.remove(node)
    scratchedmetal.color_tag = 'NONE'
    scratchedmetal.description = ""
    scratchedmetal.default_group_node_width = 140
    

    #scratchedmetal interface

    #initialize scratchedmetal nodes
    #node Material Output
    material_output = scratchedmetal.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    #Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Thickness
    material_output.inputs[3].default_value = 0.0

    #node Group
    group = scratchedmetal.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = scratchedmetalshader
    #Socket_1
    group.inputs[0].default_value = 1.0
    #Socket_2
    group.inputs[1].default_value = 1.0
    #Socket_3
    group.inputs[2].default_value = (0.17062200605869293, 0.17062200605869293, 0.17062200605869293, 1.0)
    #Socket_4
    group.inputs[3].default_value = (0.03146599978208542, 0.03146599978208542, 0.03146599978208542, 1.0)
    #Socket_5
    group.inputs[4].default_value = 1.0
    #Socket_6
    group.inputs[5].default_value = 1.0
    #Socket_7
    group.inputs[6].default_value = (0.10046499967575073, 0.10046499967575073, 0.10046499967575073, 1.0)
    #Socket_8
    group.inputs[7].default_value = 1.0
    #Socket_9
    group.inputs[8].default_value = 0.009999999776482582
    #Socket_10
    group.inputs[9].default_value = 0.02500000037252903


    #Set locations
    material_output.location = (0.0, 0.0)
    group.location = (0.0, 0.0)

    #Set dimensions
    material_output.width, material_output.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0

    #initialize scratchedmetal links
    #group.Shader -> material_output.Surface
    scratchedmetal.links.new(group.outputs[0], material_output.inputs[0])
    return scratchedmetal

scratchedmetal = scratchedmetal_node_group()


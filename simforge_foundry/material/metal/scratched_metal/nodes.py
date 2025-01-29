import bpy

mat = bpy.data.materials.new(name = "ScratchedMetal")
mat.use_nodes = True

def scratchedmetalshader_node_group():
    scratchedmetalshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "ScratchedMetalShader")
    scratchedmetalshader.color_tag = 'NONE'
    scratchedmetalshader.default_group_node_width = 140
    shader_socket = scratchedmetalshader.interface.new_socket(name = "Shader", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    shader_socket.attribute_domain = 'POINT'
    scale_socket = scratchedmetalshader.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    metallic_socket = scratchedmetalshader.interface.new_socket(name = "Metallic", in_out='INPUT', socket_type = 'NodeSocketFloat')
    metallic_socket.default_value = 1.0
    metallic_socket.min_value = 0.0
    metallic_socket.max_value = 1.0
    metallic_socket.subtype = 'FACTOR'
    metallic_socket.attribute_domain = 'POINT'
    metal_color_1_socket = scratchedmetalshader.interface.new_socket(name = "Metal Color 1", in_out='INPUT', socket_type = 'NodeSocketColor')
    metal_color_1_socket.default_value = (0.17062200605869293, 0.17062200605869293, 0.17062200605869293, 1.0)
    metal_color_1_socket.attribute_domain = 'POINT'
    metal_color_2_socket = scratchedmetalshader.interface.new_socket(name = "Metal Color 2", in_out='INPUT', socket_type = 'NodeSocketColor')
    metal_color_2_socket.default_value = (0.03146599978208542, 0.03146599978208542, 0.03146599978208542, 1.0)
    metal_color_2_socket.attribute_domain = 'POINT'
    noise_scale_socket = scratchedmetalshader.interface.new_socket(name = "Noise Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_scale_socket.default_value = 1.0
    noise_scale_socket.min_value = -3.4028234663852886e+38
    noise_scale_socket.max_value = 3.4028234663852886e+38
    noise_scale_socket.subtype = 'NONE'
    noise_scale_socket.attribute_domain = 'POINT'
    scratches_scale_socket = scratchedmetalshader.interface.new_socket(name = "Scratches Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_scale_socket.default_value = 1.0
    scratches_scale_socket.min_value = -3.4028234663852886e+38
    scratches_scale_socket.max_value = 3.4028234663852886e+38
    scratches_scale_socket.subtype = 'NONE'
    scratches_scale_socket.attribute_domain = 'POINT'
    scratches_color_socket = scratchedmetalshader.interface.new_socket(name = "Scratches Color", in_out='INPUT', socket_type = 'NodeSocketColor')
    scratches_color_socket.default_value = (0.10046499967575073, 0.10046499967575073, 0.10046499967575073, 1.0)
    scratches_color_socket.attribute_domain = 'POINT'
    roughness_socket = scratchedmetalshader.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = 'NONE'
    roughness_socket.attribute_domain = 'POINT'
    noise_bump_strength_socket = scratchedmetalshader.interface.new_socket(name = "Noise Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_strength_socket.default_value = 0.05000000074505806
    noise_bump_strength_socket.min_value = 0.0
    noise_bump_strength_socket.max_value = 1.0
    noise_bump_strength_socket.subtype = 'FACTOR'
    noise_bump_strength_socket.attribute_domain = 'POINT'
    scratches_bump_strength_socket = scratchedmetalshader.interface.new_socket(name = "Scratches Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_bump_strength_socket.default_value = 0.10000000149011612
    scratches_bump_strength_socket.min_value = 0.0
    scratches_bump_strength_socket.max_value = 1.0
    scratches_bump_strength_socket.subtype = 'FACTOR'
    scratches_bump_strength_socket.attribute_domain = 'POINT'
    frame = scratchedmetalshader.nodes.new("NodeFrame")
    frame.name = "Frame"
    frame_002 = scratchedmetalshader.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    frame_003 = scratchedmetalshader.nodes.new("NodeFrame")
    frame_003.name = "Frame.003"
    frame_004 = scratchedmetalshader.nodes.new("NodeFrame")
    frame_004.name = "Frame.004"
    frame_001 = scratchedmetalshader.nodes.new("NodeFrame")
    frame_001.name = "Frame.001"
    frame_005 = scratchedmetalshader.nodes.new("NodeFrame")
    frame_005.name = "Frame.005"
    group_output = scratchedmetalshader.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    texture_coordinate = scratchedmetalshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False
    noise_texture_002 = scratchedmetalshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_002.name = "Noise Texture.002"
    noise_texture_002.noise_dimensions = '3D'
    noise_texture_002.noise_type = 'FBM'
    noise_texture_002.normalize = True
    noise_texture_002.inputs[2].default_value = 15.0
    noise_texture_002.inputs[3].default_value = 15.0
    noise_texture_002.inputs[4].default_value = 0.5
    noise_texture_002.inputs[5].default_value = 2.0
    noise_texture_002.inputs[8].default_value = 0.0
    color_ramp_004 = scratchedmetalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_004.name = "Color Ramp.004"
    color_ramp_004.color_ramp.color_mode = 'RGB'
    color_ramp_004.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_004.color_ramp.interpolation = 'LINEAR'
    color_ramp_004.color_ramp.elements.remove(color_ramp_004.color_ramp.elements[0])
    color_ramp_004_cre_0 = color_ramp_004.color_ramp.elements[0]
    color_ramp_004_cre_0.position = 0.3718593120574951
    color_ramp_004_cre_0.alpha = 1.0
    color_ramp_004_cre_0.color = (0.502767026424408, 0.502767026424408, 0.502767026424408, 1.0)
    color_ramp_004_cre_1 = color_ramp_004.color_ramp.elements.new(0.6457287073135376)
    color_ramp_004_cre_1.alpha = 1.0
    color_ramp_004_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    color_ramp_005 = scratchedmetalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_005.name = "Color Ramp.005"
    color_ramp_005.color_ramp.color_mode = 'RGB'
    color_ramp_005.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_005.color_ramp.interpolation = 'LINEAR'
    color_ramp_005.color_ramp.elements.remove(color_ramp_005.color_ramp.elements[0])
    color_ramp_005_cre_0 = color_ramp_005.color_ramp.elements[0]
    color_ramp_005_cre_0.position = 0.14824114739894867
    color_ramp_005_cre_0.alpha = 1.0
    color_ramp_005_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_005_cre_1 = color_ramp_005.color_ramp.elements.new(0.8040200471878052)
    color_ramp_005_cre_1.alpha = 1.0
    color_ramp_005_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    mix_003 = scratchedmetalshader.nodes.new("ShaderNodeMix")
    mix_003.name = "Mix.003"
    mix_003.blend_type = 'MIX'
    mix_003.clamp_factor = True
    mix_003.clamp_result = False
    mix_003.data_type = 'RGBA'
    mix_003.factor_mode = 'UNIFORM'
    color_ramp_006 = scratchedmetalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_006.name = "Color Ramp.006"
    color_ramp_006.color_ramp.color_mode = 'RGB'
    color_ramp_006.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_006.color_ramp.interpolation = 'LINEAR'
    color_ramp_006.color_ramp.elements.remove(color_ramp_006.color_ramp.elements[0])
    color_ramp_006_cre_0 = color_ramp_006.color_ramp.elements[0]
    color_ramp_006_cre_0.position = 0.0
    color_ramp_006_cre_0.alpha = 1.0
    color_ramp_006_cre_0.color = (0.2911059856414795, 0.2911059856414795, 0.2911059856414795, 1.0)
    color_ramp_006_cre_1 = color_ramp_006.color_ramp.elements.new(1.0)
    color_ramp_006_cre_1.alpha = 1.0
    color_ramp_006_cre_1.color = (0.596705973148346, 0.596705973148346, 0.596705973148346, 1.0)
    voronoi_texture = scratchedmetalshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = 'EUCLIDEAN'
    voronoi_texture.feature = 'DISTANCE_TO_EDGE'
    voronoi_texture.normalize = False
    voronoi_texture.voronoi_dimensions = '3D'
    voronoi_texture.inputs[2].default_value = 50.0
    voronoi_texture.inputs[3].default_value = 15.0
    voronoi_texture.inputs[4].default_value = 0.75
    voronoi_texture.inputs[5].default_value = 2.0
    voronoi_texture.inputs[8].default_value = 1.0
    voronoi_texture_001 = scratchedmetalshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001.name = "Voronoi Texture.001"
    voronoi_texture_001.distance = 'EUCLIDEAN'
    voronoi_texture_001.feature = 'DISTANCE_TO_EDGE'
    voronoi_texture_001.normalize = False
    voronoi_texture_001.voronoi_dimensions = '3D'
    voronoi_texture_001.inputs[2].default_value = 114.0
    voronoi_texture_001.inputs[3].default_value = 15.0
    voronoi_texture_001.inputs[4].default_value = 0.75
    voronoi_texture_001.inputs[5].default_value = 2.0
    voronoi_texture_001.inputs[8].default_value = 1.0
    color_ramp = scratchedmetalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp.name = "Color Ramp"
    color_ramp.color_ramp.color_mode = 'RGB'
    color_ramp.color_ramp.hue_interpolation = 'NEAR'
    color_ramp.color_ramp.interpolation = 'LINEAR'
    color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
    color_ramp_cre_0 = color_ramp.color_ramp.elements[0]
    color_ramp_cre_0.position = 0.0
    color_ramp_cre_0.alpha = 1.0
    color_ramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_cre_1 = color_ramp.color_ramp.elements.new(0.037688400596380234)
    color_ramp_cre_1.alpha = 1.0
    color_ramp_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    noise_texture = scratchedmetalshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    noise_texture.inputs[2].default_value = 35.0
    noise_texture.inputs[3].default_value = 15.0
    noise_texture.inputs[4].default_value = 0.7300000190734863
    noise_texture.inputs[5].default_value = 2.0
    noise_texture.inputs[8].default_value = 0.0
    color_ramp_001 = scratchedmetalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_001.name = "Color Ramp.001"
    color_ramp_001.color_ramp.color_mode = 'RGB'
    color_ramp_001.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_001.color_ramp.interpolation = 'LINEAR'
    color_ramp_001.color_ramp.elements.remove(color_ramp_001.color_ramp.elements[0])
    color_ramp_001_cre_0 = color_ramp_001.color_ramp.elements[0]
    color_ramp_001_cre_0.position = 0.0
    color_ramp_001_cre_0.alpha = 1.0
    color_ramp_001_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_001_cre_1 = color_ramp_001.color_ramp.elements.new(0.037688400596380234)
    color_ramp_001_cre_1.alpha = 1.0
    color_ramp_001_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    mix = scratchedmetalshader.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'DARKEN'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'
    mix.inputs[0].default_value = 1.0
    mix_001 = scratchedmetalshader.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'LIGHTEN'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'RGBA'
    mix_001.factor_mode = 'UNIFORM'
    mix_001.inputs[7].default_value = (1.0, 1.0, 1.0, 1.0)
    color_ramp_002 = scratchedmetalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_002.name = "Color Ramp.002"
    color_ramp_002.color_ramp.color_mode = 'RGB'
    color_ramp_002.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_002.color_ramp.interpolation = 'LINEAR'
    color_ramp_002.color_ramp.elements.remove(color_ramp_002.color_ramp.elements[0])
    color_ramp_002_cre_0 = color_ramp_002.color_ramp.elements[0]
    color_ramp_002_cre_0.position = 0.40703511238098145
    color_ramp_002_cre_0.alpha = 1.0
    color_ramp_002_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_002_cre_1 = color_ramp_002.color_ramp.elements.new(0.6532663106918335)
    color_ramp_002_cre_1.alpha = 1.0
    color_ramp_002_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    color_ramp_003 = scratchedmetalshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_003.name = "Color Ramp.003"
    color_ramp_003.color_ramp.color_mode = 'RGB'
    color_ramp_003.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_003.color_ramp.interpolation = 'LINEAR'
    color_ramp_003.color_ramp.elements.remove(color_ramp_003.color_ramp.elements[0])
    color_ramp_003_cre_0 = color_ramp_003.color_ramp.elements[0]
    color_ramp_003_cre_0.position = 0.0
    color_ramp_003_cre_0.alpha = 1.0
    color_ramp_003_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_003_cre_1 = color_ramp_003.color_ramp.elements.new(0.4321606159210205)
    color_ramp_003_cre_1.alpha = 1.0
    color_ramp_003_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    mapping = scratchedmetalshader.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = 'POINT'
    mapping.inputs[1].default_value = (0.0, 0.0, 0.0)
    mapping.inputs[2].default_value = (0.0, 0.0, 0.0)
    principled_bsdf = scratchedmetalshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    principled_bsdf.inputs[3].default_value = 1.4500000476837158
    principled_bsdf.inputs[4].default_value = 1.0
    principled_bsdf.inputs[7].default_value = 0.0
    principled_bsdf.inputs[8].default_value = 0.0
    principled_bsdf.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    principled_bsdf.inputs[10].default_value = 0.05000000074505806
    principled_bsdf.inputs[12].default_value = 0.0
    principled_bsdf.inputs[13].default_value = 0.5
    principled_bsdf.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf.inputs[15].default_value = 0.0
    principled_bsdf.inputs[16].default_value = 0.0
    principled_bsdf.inputs[17].default_value = (0.0, 0.0, 0.0)
    principled_bsdf.inputs[18].default_value = 0.0
    principled_bsdf.inputs[19].default_value = 0.0
    principled_bsdf.inputs[20].default_value = 0.029999999329447746
    principled_bsdf.inputs[21].default_value = 1.5
    principled_bsdf.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf.inputs[23].default_value = (0.0, 0.0, 0.0)
    principled_bsdf.inputs[24].default_value = 0.0
    principled_bsdf.inputs[25].default_value = 0.5
    principled_bsdf.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf.inputs[28].default_value = 0.0
    principled_bsdf.inputs[29].default_value = 0.0
    principled_bsdf.inputs[30].default_value = 1.3300000429153442
    mix_002 = scratchedmetalshader.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = 'MIX'
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = 'RGBA'
    mix_002.factor_mode = 'UNIFORM'
    reroute = scratchedmetalshader.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketVector"
    reroute_001 = scratchedmetalshader.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketVector"
    mapping_002 = scratchedmetalshader.nodes.new("ShaderNodeMapping")
    mapping_002.name = "Mapping.002"
    mapping_002.vector_type = 'POINT'
    mapping_002.inputs[1].default_value = (0.0, 0.0, 0.0)
    mapping_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    mapping_001 = scratchedmetalshader.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = 'POINT'
    mapping_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    hue_saturation_value = scratchedmetalshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    hue_saturation_value.inputs[0].default_value = 0.5
    hue_saturation_value.inputs[1].default_value = 1.0
    hue_saturation_value.inputs[3].default_value = 1.0
    bump = scratchedmetalshader.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    bump.inputs[1].default_value = 1.0
    bump.inputs[3].default_value = (0.0, 0.0, 0.0)
    bump_001 = scratchedmetalshader.nodes.new("ShaderNodeBump")
    bump_001.name = "Bump.001"
    bump_001.invert = False
    bump_001.inputs[1].default_value = 1.0
    group_input = scratchedmetalshader.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    noise_texture_001 = scratchedmetalshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = '3D'
    noise_texture_001.noise_type = 'FBM'
    noise_texture_001.normalize = True
    noise_texture_001.inputs[2].default_value = 15.0
    noise_texture_001.inputs[3].default_value = 15.0
    noise_texture_001.inputs[5].default_value = 2.0
    noise_texture_001.inputs[8].default_value = 0.0
    clamp = scratchedmetalshader.nodes.new("ShaderNodeClamp")
    clamp.name = "Clamp"
    clamp.hide = True
    clamp.clamp_type = 'MINMAX'
    clamp.inputs[1].default_value = 0.0
    clamp.inputs[2].default_value = 1.0
    scratchedmetalshader.links.new(mix_003.outputs[2], principled_bsdf.inputs[0])
    scratchedmetalshader.links.new(mix_003.outputs[2], color_ramp_006.inputs[0])
    scratchedmetalshader.links.new(noise_texture.outputs[0], color_ramp_002.inputs[0])
    scratchedmetalshader.links.new(reroute_001.outputs[0], voronoi_texture.inputs[0])
    scratchedmetalshader.links.new(bump.outputs[0], bump_001.inputs[3])
    scratchedmetalshader.links.new(mix.outputs[2], mix_001.inputs[6])
    scratchedmetalshader.links.new(reroute_001.outputs[0], noise_texture.inputs[0])
    scratchedmetalshader.links.new(color_ramp_003.outputs[0], mix_003.inputs[0])
    scratchedmetalshader.links.new(reroute.outputs[0], noise_texture_002.inputs[0])
    scratchedmetalshader.links.new(voronoi_texture_001.outputs[0], color_ramp_001.inputs[0])
    scratchedmetalshader.links.new(texture_coordinate.outputs[3], mapping.inputs[0])
    scratchedmetalshader.links.new(color_ramp_002.outputs[0], mix_001.inputs[0])
    scratchedmetalshader.links.new(voronoi_texture.outputs[0], color_ramp.inputs[0])
    scratchedmetalshader.links.new(noise_texture_002.outputs[0], color_ramp_004.inputs[0])
    scratchedmetalshader.links.new(color_ramp_001.outputs[0], mix.inputs[6])
    scratchedmetalshader.links.new(bump_001.outputs[0], principled_bsdf.inputs[5])
    scratchedmetalshader.links.new(reroute_001.outputs[0], voronoi_texture_001.inputs[0])
    scratchedmetalshader.links.new(noise_texture_001.outputs[0], color_ramp_005.inputs[0])
    scratchedmetalshader.links.new(color_ramp_005.outputs[0], mix_002.inputs[0])
    scratchedmetalshader.links.new(color_ramp_006.outputs[0], hue_saturation_value.inputs[4])
    scratchedmetalshader.links.new(noise_texture_001.outputs[0], bump.inputs[2])
    scratchedmetalshader.links.new(mix_002.outputs[2], mix_003.inputs[7])
    scratchedmetalshader.links.new(reroute.outputs[0], noise_texture_001.inputs[0])
    scratchedmetalshader.links.new(mix_001.outputs[2], color_ramp_003.inputs[0])
    scratchedmetalshader.links.new(color_ramp.outputs[0], mix.inputs[7])
    scratchedmetalshader.links.new(hue_saturation_value.outputs[0], principled_bsdf.inputs[2])
    scratchedmetalshader.links.new(color_ramp_003.outputs[0], bump_001.inputs[2])
    scratchedmetalshader.links.new(principled_bsdf.outputs[0], group_output.inputs[0])
    scratchedmetalshader.links.new(group_input.outputs[0], mapping.inputs[3])
    scratchedmetalshader.links.new(group_input.outputs[1], principled_bsdf.inputs[1])
    scratchedmetalshader.links.new(group_input.outputs[2], mix_002.inputs[6])
    scratchedmetalshader.links.new(group_input.outputs[3], mix_002.inputs[7])
    scratchedmetalshader.links.new(mapping_002.outputs[0], reroute.inputs[0])
    scratchedmetalshader.links.new(mapping_001.outputs[0], reroute_001.inputs[0])
    scratchedmetalshader.links.new(mapping.outputs[0], mapping_001.inputs[0])
    scratchedmetalshader.links.new(mapping.outputs[0], mapping_002.inputs[0])
    scratchedmetalshader.links.new(group_input.outputs[4], mapping_002.inputs[3])
    scratchedmetalshader.links.new(group_input.outputs[5], mapping_001.inputs[3])
    scratchedmetalshader.links.new(group_input.outputs[6], mix_003.inputs[6])
    scratchedmetalshader.links.new(group_input.outputs[7], hue_saturation_value.inputs[2])
    scratchedmetalshader.links.new(group_input.outputs[8], bump.inputs[0])
    scratchedmetalshader.links.new(group_input.outputs[9], bump_001.inputs[0])
    scratchedmetalshader.links.new(color_ramp_004.outputs[0], clamp.inputs[0])
    scratchedmetalshader.links.new(clamp.outputs[0], noise_texture_001.inputs[4])
    return scratchedmetalshader

scratchedmetalshader = scratchedmetalshader_node_group()

def scratchedmetal_node_group():
    scratchedmetal = mat.node_tree
    for node in scratchedmetal.nodes:
        scratchedmetal.nodes.remove(node)
    scratchedmetal.color_tag = 'NONE'
    scratchedmetal.default_group_node_width = 140
    material_output = scratchedmetal.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    material_output.inputs[3].default_value = 0.0
    group = scratchedmetal.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = scratchedmetalshader
    group.inputs[0].default_value = 1.0
    group.inputs[1].default_value = 1.0
    group.inputs[2].default_value = (0.17062200605869293, 0.17062200605869293, 0.17062200605869293, 1.0)
    group.inputs[3].default_value = (0.03146599978208542, 0.03146599978208542, 0.03146599978208542, 1.0)
    group.inputs[4].default_value = 1.0
    group.inputs[5].default_value = 1.0
    group.inputs[6].default_value = (0.10046499967575073, 0.10046499967575073, 0.10046499967575073, 1.0)
    group.inputs[7].default_value = 1.0
    group.inputs[8].default_value = 0.009999999776482582
    group.inputs[9].default_value = 0.02500000037252903
    scratchedmetal.links.new(group.outputs[0], material_output.inputs[0])
    return scratchedmetal

scratchedmetal = scratchedmetal_node_group()


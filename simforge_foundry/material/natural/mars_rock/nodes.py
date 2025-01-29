import bpy

mat = bpy.data.materials.new(name = "MarsRockMat")
mat.use_nodes = True

def random_x2___mat_node_group():
    random_x2___mat = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "Random x2 | Mat")
    random_x2___mat.color_tag = 'NONE'
    random_x2___mat.default_group_node_width = 140
    _0_socket = random_x2___mat.interface.new_socket(name = "0", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _0_socket.default_value = 0.0
    _0_socket.min_value = 0.0
    _0_socket.max_value = 1.0
    _0_socket.subtype = 'NONE'
    _0_socket.attribute_domain = 'POINT'
    _1_socket = random_x2___mat.interface.new_socket(name = "1", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _1_socket.default_value = 0.0
    _1_socket.min_value = 0.0
    _1_socket.max_value = 1.0
    _1_socket.subtype = 'NONE'
    _1_socket.attribute_domain = 'POINT'
    _2_socket = random_x2___mat.interface.new_socket(name = "2", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _2_socket.default_value = 0.0
    _2_socket.min_value = -3.4028234663852886e+38
    _2_socket.max_value = 3.4028234663852886e+38
    _2_socket.subtype = 'NONE'
    _2_socket.attribute_domain = 'POINT'
    seed_socket = random_x2___mat.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketFloat')
    seed_socket.default_value = 0.0
    seed_socket.min_value = 0.0
    seed_socket.max_value = 1.0
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    group_output = random_x2___mat.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    group_input = random_x2___mat.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    object_info = random_x2___mat.nodes.new("ShaderNodeObjectInfo")
    object_info.name = "Object Info"
    math = random_x2___mat.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'ADD'
    math.use_clamp = False
    white_noise_texture = random_x2___mat.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture.name = "White Noise Texture"
    white_noise_texture.noise_dimensions = '4D'
    separate_color = random_x2___mat.nodes.new("ShaderNodeSeparateColor")
    separate_color.name = "Separate Color"
    separate_color.mode = 'RGB'
    random_x2___mat.links.new(object_info.outputs[5], white_noise_texture.inputs[1])
    random_x2___mat.links.new(math.outputs[0], white_noise_texture.inputs[0])
    random_x2___mat.links.new(white_noise_texture.outputs[1], separate_color.inputs[0])
    random_x2___mat.links.new(object_info.outputs[3], math.inputs[1])
    random_x2___mat.links.new(group_input.outputs[0], math.inputs[0])
    random_x2___mat.links.new(separate_color.outputs[0], group_output.inputs[0])
    random_x2___mat.links.new(separate_color.outputs[1], group_output.inputs[1])
    random_x2___mat.links.new(separate_color.outputs[2], group_output.inputs[2])
    return random_x2___mat

random_x2___mat = random_x2___mat_node_group()

def rockshader___3_node_group():
    rockshader___3 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "RockShader | 3")
    rockshader___3.color_tag = 'NONE'
    rockshader___3.default_group_node_width = 140
    shader_socket = rockshader___3.interface.new_socket(name = "Shader", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    shader_socket.attribute_domain = 'POINT'
    scale_socket = rockshader___3.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    color_1_socket = rockshader___3.interface.new_socket(name = "Color 1", in_out='INPUT', socket_type = 'NodeSocketColor')
    color_1_socket.default_value = (1.0, 0.33455199003219604, 0.12201099842786789, 1.0)
    color_1_socket.attribute_domain = 'POINT'
    color_2_socket = rockshader___3.interface.new_socket(name = "Color 2", in_out='INPUT', socket_type = 'NodeSocketColor')
    color_2_socket.default_value = (0.10239599645137787, 0.009690999984741211, 0.0059830001555383205, 1.0)
    color_2_socket.attribute_domain = 'POINT'
    color_3_socket = rockshader___3.interface.new_socket(name = "Color 3", in_out='INPUT', socket_type = 'NodeSocketColor')
    color_3_socket.default_value = (0.13511300086975098, 0.041269998997449875, 0.015100999735295773, 1.0)
    color_3_socket.attribute_domain = 'POINT'
    color_4_socket = rockshader___3.interface.new_socket(name = "Color 4", in_out='INPUT', socket_type = 'NodeSocketColor')
    color_4_socket.default_value = (1.0, 0.27467700839042664, 0.0886560007929802, 1.0)
    color_4_socket.attribute_domain = 'POINT'
    noise_scale_socket = rockshader___3.interface.new_socket(name = "Noise Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_scale_socket.default_value = 16.0
    noise_scale_socket.min_value = -1000.0
    noise_scale_socket.max_value = 1000.0
    noise_scale_socket.subtype = 'NONE'
    noise_scale_socket.attribute_domain = 'POINT'
    chunks_scale_socket = rockshader___3.interface.new_socket(name = "Chunks Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    chunks_scale_socket.default_value = 4.0
    chunks_scale_socket.min_value = -1000.0
    chunks_scale_socket.max_value = 1000.0
    chunks_scale_socket.subtype = 'NONE'
    chunks_scale_socket.attribute_domain = 'POINT'
    noise_detail_1_socket = rockshader___3.interface.new_socket(name = "Noise Detail 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_detail_1_socket.default_value = 15.0
    noise_detail_1_socket.min_value = 0.0
    noise_detail_1_socket.max_value = 15.0
    noise_detail_1_socket.subtype = 'NONE'
    noise_detail_1_socket.attribute_domain = 'POINT'
    noise_detail_2_socket = rockshader___3.interface.new_socket(name = "Noise Detail 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_detail_2_socket.default_value = 0.44999998807907104
    noise_detail_2_socket.min_value = 0.0
    noise_detail_2_socket.max_value = 1.0
    noise_detail_2_socket.subtype = 'FACTOR'
    noise_detail_2_socket.attribute_domain = 'POINT'
    distortion_socket = rockshader___3.interface.new_socket(name = "Distortion", in_out='INPUT', socket_type = 'NodeSocketFloat')
    distortion_socket.default_value = 0.10000000149011612
    distortion_socket.min_value = 0.0
    distortion_socket.max_value = 1.0
    distortion_socket.subtype = 'FACTOR'
    distortion_socket.attribute_domain = 'POINT'
    roughness_socket = rockshader___3.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = 'NONE'
    roughness_socket.attribute_domain = 'POINT'
    noise_bump_strength_socket = rockshader___3.interface.new_socket(name = "Noise Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_strength_socket.default_value = 0.20000000298023224
    noise_bump_strength_socket.min_value = 0.0
    noise_bump_strength_socket.max_value = 1.0
    noise_bump_strength_socket.subtype = 'FACTOR'
    noise_bump_strength_socket.attribute_domain = 'POINT'
    detail_bump_strength_socket = rockshader___3.interface.new_socket(name = "Detail Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detail_bump_strength_socket.default_value = 0.10000000149011612
    detail_bump_strength_socket.min_value = 0.0
    detail_bump_strength_socket.max_value = 1.0
    detail_bump_strength_socket.subtype = 'FACTOR'
    detail_bump_strength_socket.attribute_domain = 'POINT'
    group_output_1 = rockshader___3.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True
    texture_coordinate = rockshader___3.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False
    mapping_001 = rockshader___3.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = 'POINT'
    mapping_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    mapping_001.inputs[3].default_value = (1.0, 1.0, 1.5)
    noise_texture_001 = rockshader___3.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = '3D'
    noise_texture_001.noise_type = 'FBM'
    noise_texture_001.normalize = True
    noise_texture_001.inputs[2].default_value = 19.0
    noise_texture_001.inputs[3].default_value = 15.0
    noise_texture_001.inputs[4].default_value = 0.699999988079071
    noise_texture_001.inputs[5].default_value = 2.0
    noise_texture_001.inputs[8].default_value = 0.0
    colorramp_001 = rockshader___3.nodes.new("ShaderNodeValToRGB")
    colorramp_001.name = "ColorRamp.001"
    colorramp_001.color_ramp.color_mode = 'RGB'
    colorramp_001.color_ramp.hue_interpolation = 'NEAR'
    colorramp_001.color_ramp.interpolation = 'LINEAR'
    colorramp_001.color_ramp.elements.remove(colorramp_001.color_ramp.elements[0])
    colorramp_001_cre_0 = colorramp_001.color_ramp.elements[0]
    colorramp_001_cre_0.position = 0.0
    colorramp_001_cre_0.alpha = 1.0
    colorramp_001_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    colorramp_001_cre_1 = colorramp_001.color_ramp.elements.new(0.604113757610321)
    colorramp_001_cre_1.alpha = 1.0
    colorramp_001_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    mix_001 = rockshader___3.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'MIX'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'RGBA'
    mix_001.factor_mode = 'UNIFORM'
    mix_001.inputs[6].default_value = (0.14487500488758087, 0.14487500488758087, 0.14487500488758087, 1.0)
    colorramp_003 = rockshader___3.nodes.new("ShaderNodeValToRGB")
    colorramp_003.name = "ColorRamp.003"
    colorramp_003.color_ramp.color_mode = 'RGB'
    colorramp_003.color_ramp.hue_interpolation = 'NEAR'
    colorramp_003.color_ramp.interpolation = 'LINEAR'
    colorramp_003.color_ramp.elements.remove(colorramp_003.color_ramp.elements[0])
    colorramp_003_cre_0 = colorramp_003.color_ramp.elements[0]
    colorramp_003_cre_0.position = 0.0
    colorramp_003_cre_0.alpha = 1.0
    colorramp_003_cre_0.color = (0.5663849711418152, 0.5663849711418152, 0.5663849711418152, 1.0)
    colorramp_003_cre_1 = colorramp_003.color_ramp.elements.new(1.0)
    colorramp_003_cre_1.alpha = 1.0
    colorramp_003_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    voronoi_texture = rockshader___3.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = 'EUCLIDEAN'
    voronoi_texture.feature = 'F1'
    voronoi_texture.normalize = False
    voronoi_texture.voronoi_dimensions = '3D'
    voronoi_texture.inputs[2].default_value = 350.0
    voronoi_texture.inputs[3].default_value = 0.0
    voronoi_texture.inputs[4].default_value = 0.5
    voronoi_texture.inputs[5].default_value = 2.0
    voronoi_texture.inputs[8].default_value = 1.0
    bump_001 = rockshader___3.nodes.new("ShaderNodeBump")
    bump_001.name = "Bump.001"
    bump_001.invert = False
    bump_001.inputs[1].default_value = 1.0
    principled_bsdf = rockshader___3.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK_SKIN'
    principled_bsdf.inputs[1].default_value = 0.0
    principled_bsdf.inputs[3].default_value = 1.4500000476837158
    principled_bsdf.inputs[4].default_value = 1.0
    principled_bsdf.inputs[7].default_value = 0.0
    principled_bsdf.inputs[8].default_value = 0.0
    principled_bsdf.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    principled_bsdf.inputs[10].default_value = 0.05000000074505806
    principled_bsdf.inputs[11].default_value = 1.399999976158142
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
    principled_bsdf.inputs[27].default_value = (0.0, 0.0, 0.0, 1.0)
    principled_bsdf.inputs[28].default_value = 1.0
    principled_bsdf.inputs[29].default_value = 0.0
    principled_bsdf.inputs[30].default_value = 1.3300000429153442
    mapping = rockshader___3.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = 'POINT'
    mapping.inputs[2].default_value = (0.0, 0.0, 0.0)
    colorramp_002 = rockshader___3.nodes.new("ShaderNodeValToRGB")
    colorramp_002.name = "ColorRamp.002"
    colorramp_002.color_ramp.color_mode = 'RGB'
    colorramp_002.color_ramp.hue_interpolation = 'NEAR'
    colorramp_002.color_ramp.interpolation = 'LINEAR'
    colorramp_002.color_ramp.elements.remove(colorramp_002.color_ramp.elements[0])
    colorramp_002_cre_0 = colorramp_002.color_ramp.elements[0]
    colorramp_002_cre_0.position = 0.08226212114095688
    colorramp_002_cre_0.alpha = 1.0
    colorramp_002_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    colorramp_002_cre_1 = colorramp_002.color_ramp.elements.new(0.15424175560474396)
    colorramp_002_cre_1.alpha = 1.0
    colorramp_002_cre_1.color = (0.3593989908695221, 0.3593989908695221, 0.3593989908695221, 1.0)
    colorramp_002_cre_2 = colorramp_002.color_ramp.elements.new(0.2776348292827606)
    colorramp_002_cre_2.alpha = 1.0
    colorramp_002_cre_2.color = (0.0, 0.0, 0.0, 1.0)
    colorramp = rockshader___3.nodes.new("ShaderNodeValToRGB")
    colorramp.name = "ColorRamp"
    colorramp.color_ramp.color_mode = 'RGB'
    colorramp.color_ramp.hue_interpolation = 'NEAR'
    colorramp.color_ramp.interpolation = 'LINEAR'
    colorramp.color_ramp.elements.remove(colorramp.color_ramp.elements[0])
    colorramp_cre_0 = colorramp.color_ramp.elements[0]
    colorramp_cre_0.position = 0.010282879695296288
    colorramp_cre_0.alpha = 1.0
    colorramp_cre_0.color = (1.0, 1.0, 1.0, 1.0)
    colorramp_cre_1 = colorramp.color_ramp.elements.new(0.15167097747325897)
    colorramp_cre_1.alpha = 1.0
    colorramp_cre_1.color = (0.0, 0.0, 0.0, 1.0)
    mix_002 = rockshader___3.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = 'MIX'
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = 'RGBA'
    mix_002.factor_mode = 'UNIFORM'
    mix_003 = rockshader___3.nodes.new("ShaderNodeMix")
    mix_003.name = "Mix.003"
    mix_003.blend_type = 'MIX'
    mix_003.clamp_factor = True
    mix_003.clamp_result = False
    mix_003.data_type = 'RGBA'
    mix_003.factor_mode = 'UNIFORM'
    mix_004 = rockshader___3.nodes.new("ShaderNodeMix")
    mix_004.name = "Mix.004"
    mix_004.blend_type = 'LIGHTEN'
    mix_004.clamp_factor = True
    mix_004.clamp_result = False
    mix_004.data_type = 'RGBA'
    mix_004.factor_mode = 'UNIFORM'
    voronoi_texture_001 = rockshader___3.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001.name = "Voronoi Texture.001"
    voronoi_texture_001.distance = 'EUCLIDEAN'
    voronoi_texture_001.feature = 'DISTANCE_TO_EDGE'
    voronoi_texture_001.normalize = False
    voronoi_texture_001.voronoi_dimensions = '3D'
    voronoi_texture_001.inputs[3].default_value = 0.0
    voronoi_texture_001.inputs[4].default_value = 0.5
    voronoi_texture_001.inputs[5].default_value = 2.0
    voronoi_texture_001.inputs[8].default_value = 1.0
    noise_texture = rockshader___3.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    noise_texture.inputs[5].default_value = 2.0
    noise_texture.inputs[8].default_value = 0.0
    mix = rockshader___3.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'LINEAR_LIGHT'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'
    hue_saturation_value = rockshader___3.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue Saturation Value"
    hue_saturation_value.inputs[0].default_value = 0.5
    hue_saturation_value.inputs[1].default_value = 1.0
    hue_saturation_value.inputs[3].default_value = 1.0
    bump = rockshader___3.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    bump.inputs[1].default_value = 1.0
    bump.inputs[3].default_value = (0.0, 0.0, 0.0)
    group_input_1 = rockshader___3.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"
    clamp = rockshader___3.nodes.new("ShaderNodeClamp")
    clamp.name = "Clamp"
    clamp.hide = True
    clamp.clamp_type = 'MINMAX'
    clamp.inputs[1].default_value = 0.0
    clamp.inputs[2].default_value = 1.0
    map_range_011 = rockshader___3.nodes.new("ShaderNodeMapRange")
    map_range_011.name = "Map Range.011"
    map_range_011.clamp = True
    map_range_011.data_type = 'FLOAT'
    map_range_011.interpolation_type = 'LINEAR'
    map_range_011.inputs[1].default_value = 0.0
    map_range_011.inputs[2].default_value = 1.0
    map_range_011.inputs[3].default_value = -1000.0
    map_range_011.inputs[4].default_value = 1000.0
    group_001 = rockshader___3.nodes.new("ShaderNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = random_x2___mat
    group_001.inputs[0].default_value = 0.5241000056266785
    rockshader___3.links.new(colorramp_001.outputs[0], mix_003.inputs[0])
    rockshader___3.links.new(mix_003.outputs[2], mix_004.inputs[6])
    rockshader___3.links.new(voronoi_texture.outputs[0], bump_001.inputs[2])
    rockshader___3.links.new(mix.outputs[2], voronoi_texture.inputs[0])
    rockshader___3.links.new(bump_001.outputs[0], principled_bsdf.inputs[5])
    rockshader___3.links.new(texture_coordinate.outputs[3], mapping.inputs[0])
    rockshader___3.links.new(hue_saturation_value.outputs[0], principled_bsdf.inputs[2])
    rockshader___3.links.new(mix_004.outputs[2], principled_bsdf.inputs[0])
    rockshader___3.links.new(voronoi_texture_001.outputs[0], colorramp_002.inputs[0])
    rockshader___3.links.new(mapping_001.outputs[0], noise_texture.inputs[0])
    rockshader___3.links.new(noise_texture.outputs[0], mix.inputs[7])
    rockshader___3.links.new(mapping_001.outputs[0], mix.inputs[6])
    rockshader___3.links.new(voronoi_texture_001.outputs[0], bump.inputs[2])
    rockshader___3.links.new(mix.outputs[2], voronoi_texture_001.inputs[0])
    rockshader___3.links.new(colorramp_003.outputs[0], hue_saturation_value.inputs[4])
    rockshader___3.links.new(mapping.outputs[0], mapping_001.inputs[0])
    rockshader___3.links.new(voronoi_texture.outputs[0], mix_001.inputs[0])
    rockshader___3.links.new(voronoi_texture_001.outputs[0], mix_001.inputs[7])
    rockshader___3.links.new(colorramp.outputs[0], mix_002.inputs[0])
    rockshader___3.links.new(mix_001.outputs[2], colorramp.inputs[0])
    rockshader___3.links.new(bump.outputs[0], bump_001.inputs[3])
    rockshader___3.links.new(mapping_001.outputs[0], noise_texture_001.inputs[0])
    rockshader___3.links.new(noise_texture_001.outputs[0], colorramp_001.inputs[0])
    rockshader___3.links.new(mix_001.outputs[2], colorramp_003.inputs[0])
    rockshader___3.links.new(mix_002.outputs[2], mix_003.inputs[6])
    rockshader___3.links.new(colorramp_002.outputs[0], mix_004.inputs[0])
    rockshader___3.links.new(principled_bsdf.outputs[0], group_output_1.inputs[0])
    rockshader___3.links.new(group_input_1.outputs[0], mapping.inputs[3])
    rockshader___3.links.new(group_input_1.outputs[1], mix_002.inputs[6])
    rockshader___3.links.new(group_input_1.outputs[2], mix_002.inputs[7])
    rockshader___3.links.new(group_input_1.outputs[3], mix_003.inputs[7])
    rockshader___3.links.new(group_input_1.outputs[4], mix_004.inputs[7])
    rockshader___3.links.new(group_input_1.outputs[5], noise_texture.inputs[2])
    rockshader___3.links.new(group_input_1.outputs[6], voronoi_texture_001.inputs[2])
    rockshader___3.links.new(group_input_1.outputs[7], noise_texture.inputs[3])
    rockshader___3.links.new(group_input_1.outputs[9], mix.inputs[0])
    rockshader___3.links.new(group_input_1.outputs[10], hue_saturation_value.inputs[2])
    rockshader___3.links.new(group_input_1.outputs[11], bump.inputs[0])
    rockshader___3.links.new(group_input_1.outputs[12], bump_001.inputs[0])
    rockshader___3.links.new(group_input_1.outputs[8], clamp.inputs[0])
    rockshader___3.links.new(clamp.outputs[0], noise_texture.inputs[4])
    rockshader___3.links.new(group_001.outputs[0], map_range_011.inputs[0])
    rockshader___3.links.new(map_range_011.outputs[0], mapping.inputs[1])
    return rockshader___3

rockshader___3 = rockshader___3_node_group()

def rockshader___4_node_group():
    rockshader___4 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "RockShader | 4")
    rockshader___4.color_tag = 'NONE'
    rockshader___4.default_group_node_width = 140
    shader_socket_1 = rockshader___4.interface.new_socket(name = "Shader", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    shader_socket_1.attribute_domain = 'POINT'
    scale_socket_1 = rockshader___4.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket_1.default_value = 1.0
    scale_socket_1.min_value = -3.4028234663852886e+38
    scale_socket_1.max_value = 3.4028234663852886e+38
    scale_socket_1.subtype = 'NONE'
    scale_socket_1.attribute_domain = 'POINT'
    color_1_socket_1 = rockshader___4.interface.new_socket(name = "Color 1", in_out='INPUT', socket_type = 'NodeSocketColor')
    color_1_socket_1.default_value = (0.6590179800987244, 0.24836499989032745, 0.0748089998960495, 1.0)
    color_1_socket_1.attribute_domain = 'POINT'
    color_2_socket_1 = rockshader___4.interface.new_socket(name = "Color 2", in_out='INPUT', socket_type = 'NodeSocketColor')
    color_2_socket_1.default_value = (0.07483299821615219, 0.01208100002259016, 0.006566000171005726, 1.0)
    color_2_socket_1.attribute_domain = 'POINT'
    color_3_socket_1 = rockshader___4.interface.new_socket(name = "Color 3", in_out='INPUT', socket_type = 'NodeSocketColor')
    color_3_socket_1.default_value = (0.046142999082803726, 0.007871000096201897, 0.004050000105053186, 1.0)
    color_3_socket_1.attribute_domain = 'POINT'
    noise_scale_socket_1 = rockshader___4.interface.new_socket(name = "Noise Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_scale_socket_1.default_value = 18.0
    noise_scale_socket_1.min_value = -1000.0
    noise_scale_socket_1.max_value = 1000.0
    noise_scale_socket_1.subtype = 'NONE'
    noise_scale_socket_1.attribute_domain = 'POINT'
    voronoi_scale_socket = rockshader___4.interface.new_socket(name = "Voronoi Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    voronoi_scale_socket.default_value = 16.0
    voronoi_scale_socket.min_value = -1000.0
    voronoi_scale_socket.max_value = 1000.0
    voronoi_scale_socket.subtype = 'NONE'
    voronoi_scale_socket.attribute_domain = 'POINT'
    wave_scale_socket = rockshader___4.interface.new_socket(name = "Wave Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    wave_scale_socket.default_value = 6.0
    wave_scale_socket.min_value = -1000.0
    wave_scale_socket.max_value = 1000.0
    wave_scale_socket.subtype = 'NONE'
    wave_scale_socket.attribute_domain = 'POINT'
    cracks_scale_socket = rockshader___4.interface.new_socket(name = "Cracks Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    cracks_scale_socket.default_value = 4.0
    cracks_scale_socket.min_value = -1000.0
    cracks_scale_socket.max_value = 1000.0
    cracks_scale_socket.subtype = 'NONE'
    cracks_scale_socket.attribute_domain = 'POINT'
    texture_detail_socket = rockshader___4.interface.new_socket(name = "Texture Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
    texture_detail_socket.default_value = 15.0
    texture_detail_socket.min_value = 0.0
    texture_detail_socket.max_value = 15.0
    texture_detail_socket.subtype = 'NONE'
    texture_detail_socket.attribute_domain = 'POINT'
    roughness_socket_1 = rockshader___4.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket_1.default_value = 1.0
    roughness_socket_1.min_value = 0.0
    roughness_socket_1.max_value = 2.0
    roughness_socket_1.subtype = 'NONE'
    roughness_socket_1.attribute_domain = 'POINT'
    noise_bump_strength_socket_1 = rockshader___4.interface.new_socket(name = "Noise Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_strength_socket_1.default_value = 0.10000000149011612
    noise_bump_strength_socket_1.min_value = 0.0
    noise_bump_strength_socket_1.max_value = 1.0
    noise_bump_strength_socket_1.subtype = 'FACTOR'
    noise_bump_strength_socket_1.attribute_domain = 'POINT'
    cracks_bump_strength_socket = rockshader___4.interface.new_socket(name = "Cracks Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    cracks_bump_strength_socket.default_value = 0.6000000238418579
    cracks_bump_strength_socket.min_value = 0.0
    cracks_bump_strength_socket.max_value = 1.0
    cracks_bump_strength_socket.subtype = 'FACTOR'
    cracks_bump_strength_socket.attribute_domain = 'POINT'
    strength_socket = rockshader___4.interface.new_socket(name = "Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    strength_socket.default_value = 0.09132219105958939
    strength_socket.min_value = 0.0
    strength_socket.max_value = 1.0
    strength_socket.subtype = 'FACTOR'
    strength_socket.attribute_domain = 'POINT'
    group_output_2 = rockshader___4.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True
    texture_coordinate_1 = rockshader___4.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_1.name = "Texture Coordinate"
    texture_coordinate_1.from_instancer = False
    mapping_1 = rockshader___4.nodes.new("ShaderNodeMapping")
    mapping_1.name = "Mapping"
    mapping_1.vector_type = 'POINT'
    mapping_1.inputs[2].default_value = (0.0, 0.0, 0.0)
    mapping_001_1 = rockshader___4.nodes.new("ShaderNodeMapping")
    mapping_001_1.name = "Mapping.001"
    mapping_001_1.vector_type = 'POINT'
    mapping_001_1.inputs[1].default_value = (0.0, 0.0, 0.0)
    mapping_001_1.inputs[2].default_value = (0.0, 0.0, 0.0)
    mapping_001_1.inputs[3].default_value = (1.0, 1.0, 1.399999976158142)
    mix_1 = rockshader___4.nodes.new("ShaderNodeMix")
    mix_1.name = "Mix"
    mix_1.blend_type = 'LINEAR_LIGHT'
    mix_1.clamp_factor = True
    mix_1.clamp_result = False
    mix_1.data_type = 'RGBA'
    mix_1.factor_mode = 'UNIFORM'
    mix_1.inputs[0].default_value = 0.10000000149011612
    colorramp_1 = rockshader___4.nodes.new("ShaderNodeValToRGB")
    colorramp_1.name = "ColorRamp"
    colorramp_1.color_ramp.color_mode = 'RGB'
    colorramp_1.color_ramp.hue_interpolation = 'NEAR'
    colorramp_1.color_ramp.interpolation = 'LINEAR'
    colorramp_1.color_ramp.elements.remove(colorramp_1.color_ramp.elements[0])
    colorramp_1_cre_0 = colorramp_1.color_ramp.elements[0]
    colorramp_1_cre_0.position = 0.0
    colorramp_1_cre_0.alpha = 1.0
    colorramp_1_cre_0.color = (1.0, 1.0, 1.0, 1.0)
    colorramp_1_cre_1 = colorramp_1.color_ramp.elements.new(0.20822615921497345)
    colorramp_1_cre_1.alpha = 1.0
    colorramp_1_cre_1.color = (0.5014079809188843, 0.5014079809188843, 0.5014079809188843, 1.0)
    principled_bsdf_1 = rockshader___4.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_1.name = "Principled BSDF"
    principled_bsdf_1.distribution = 'GGX'
    principled_bsdf_1.subsurface_method = 'RANDOM_WALK_SKIN'
    principled_bsdf_1.inputs[1].default_value = 0.0
    principled_bsdf_1.inputs[3].default_value = 1.4500000476837158
    principled_bsdf_1.inputs[4].default_value = 1.0
    principled_bsdf_1.inputs[7].default_value = 0.0
    principled_bsdf_1.inputs[8].default_value = 0.0
    principled_bsdf_1.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    principled_bsdf_1.inputs[10].default_value = 0.05000000074505806
    principled_bsdf_1.inputs[11].default_value = 1.399999976158142
    principled_bsdf_1.inputs[12].default_value = 0.0
    principled_bsdf_1.inputs[13].default_value = 0.5
    principled_bsdf_1.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_1.inputs[15].default_value = 0.0
    principled_bsdf_1.inputs[16].default_value = 0.0
    principled_bsdf_1.inputs[17].default_value = (0.0, 0.0, 0.0)
    principled_bsdf_1.inputs[18].default_value = 0.0
    principled_bsdf_1.inputs[19].default_value = 0.0
    principled_bsdf_1.inputs[20].default_value = 0.029999999329447746
    principled_bsdf_1.inputs[21].default_value = 1.5
    principled_bsdf_1.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_1.inputs[23].default_value = (0.0, 0.0, 0.0)
    principled_bsdf_1.inputs[24].default_value = 0.0
    principled_bsdf_1.inputs[25].default_value = 0.5
    principled_bsdf_1.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_1.inputs[27].default_value = (0.0, 0.0, 0.0, 1.0)
    principled_bsdf_1.inputs[28].default_value = 1.0
    principled_bsdf_1.inputs[29].default_value = 0.0
    principled_bsdf_1.inputs[30].default_value = 1.3300000429153442
    rgb_curves = rockshader___4.nodes.new("ShaderNodeRGBCurve")
    rgb_curves.name = "RGB Curves"
    rgb_curves.mapping.extend = 'EXTRAPOLATED'
    rgb_curves.mapping.tone = 'STANDARD'
    rgb_curves.mapping.black_level = (0.0, 0.0, 0.0)
    rgb_curves.mapping.white_level = (1.0, 1.0, 1.0)
    rgb_curves.mapping.clip_min_x = 0.0
    rgb_curves.mapping.clip_min_y = 0.0
    rgb_curves.mapping.clip_max_x = 1.0
    rgb_curves.mapping.clip_max_y = 1.0
    rgb_curves.mapping.use_clip = True
    rgb_curves_curve_0 = rgb_curves.mapping.curves[0]
    rgb_curves_curve_0_point_0 = rgb_curves_curve_0.points[0]
    rgb_curves_curve_0_point_0.location = (0.0, 0.0)
    rgb_curves_curve_0_point_0.handle_type = 'AUTO'
    rgb_curves_curve_0_point_1 = rgb_curves_curve_0.points[1]
    rgb_curves_curve_0_point_1.location = (1.0, 1.0)
    rgb_curves_curve_0_point_1.handle_type = 'AUTO'
    rgb_curves_curve_1 = rgb_curves.mapping.curves[1]
    rgb_curves_curve_1_point_0 = rgb_curves_curve_1.points[0]
    rgb_curves_curve_1_point_0.location = (0.0, 0.0)
    rgb_curves_curve_1_point_0.handle_type = 'AUTO'
    rgb_curves_curve_1_point_1 = rgb_curves_curve_1.points[1]
    rgb_curves_curve_1_point_1.location = (1.0, 1.0)
    rgb_curves_curve_1_point_1.handle_type = 'AUTO'
    rgb_curves_curve_2 = rgb_curves.mapping.curves[2]
    rgb_curves_curve_2_point_0 = rgb_curves_curve_2.points[0]
    rgb_curves_curve_2_point_0.location = (0.0, 0.0)
    rgb_curves_curve_2_point_0.handle_type = 'AUTO'
    rgb_curves_curve_2_point_1 = rgb_curves_curve_2.points[1]
    rgb_curves_curve_2_point_1.location = (1.0, 1.0)
    rgb_curves_curve_2_point_1.handle_type = 'AUTO'
    rgb_curves_curve_3 = rgb_curves.mapping.curves[3]
    rgb_curves_curve_3_point_0 = rgb_curves_curve_3.points[0]
    rgb_curves_curve_3_point_0.location = (0.0, 0.0)
    rgb_curves_curve_3_point_0.handle_type = 'AUTO'
    rgb_curves_curve_3_point_1 = rgb_curves_curve_3.points[1]
    rgb_curves_curve_3_point_1.location = (0.2107970118522644, 0.2904413044452667)
    rgb_curves_curve_3_point_1.handle_type = 'AUTO'
    rgb_curves_curve_3_point_2 = rgb_curves_curve_3.points.new(0.4678661823272705, 0.4007352888584137)
    rgb_curves_curve_3_point_2.handle_type = 'AUTO'
    rgb_curves_curve_3_point_3 = rgb_curves_curve_3.points.new(0.5861183404922485, 0.7536765933036804)
    rgb_curves_curve_3_point_3.handle_type = 'AUTO'
    rgb_curves_curve_3_point_4 = rgb_curves_curve_3.points.new(1.0, 1.0)
    rgb_curves_curve_3_point_4.handle_type = 'AUTO'
    rgb_curves.mapping.update()
    rgb_curves.inputs[0].default_value = 1.0
    mix_001_1 = rockshader___4.nodes.new("ShaderNodeMix")
    mix_001_1.name = "Mix.001"
    mix_001_1.blend_type = 'DARKEN'
    mix_001_1.clamp_factor = True
    mix_001_1.clamp_result = False
    mix_001_1.data_type = 'RGBA'
    mix_001_1.factor_mode = 'UNIFORM'
    mix_001_1.inputs[0].default_value = 1.0
    colorramp_001_1 = rockshader___4.nodes.new("ShaderNodeValToRGB")
    colorramp_001_1.name = "ColorRamp.001"
    colorramp_001_1.color_ramp.color_mode = 'RGB'
    colorramp_001_1.color_ramp.hue_interpolation = 'NEAR'
    colorramp_001_1.color_ramp.interpolation = 'LINEAR'
    colorramp_001_1.color_ramp.elements.remove(colorramp_001_1.color_ramp.elements[0])
    colorramp_001_1_cre_0 = colorramp_001_1.color_ramp.elements[0]
    colorramp_001_1_cre_0.position = 0.0
    colorramp_001_1_cre_0.alpha = 1.0
    colorramp_001_1_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    colorramp_001_1_cre_1 = colorramp_001_1.color_ramp.elements.new(0.05912623554468155)
    colorramp_001_1_cre_1.alpha = 1.0
    colorramp_001_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    rgb_curves_001 = rockshader___4.nodes.new("ShaderNodeRGBCurve")
    rgb_curves_001.name = "RGB Curves.001"
    rgb_curves_001.mapping.extend = 'EXTRAPOLATED'
    rgb_curves_001.mapping.tone = 'STANDARD'
    rgb_curves_001.mapping.black_level = (0.0, 0.0, 0.0)
    rgb_curves_001.mapping.white_level = (1.0, 1.0, 1.0)
    rgb_curves_001.mapping.clip_min_x = 0.0
    rgb_curves_001.mapping.clip_min_y = 0.0
    rgb_curves_001.mapping.clip_max_x = 1.0
    rgb_curves_001.mapping.clip_max_y = 1.0
    rgb_curves_001.mapping.use_clip = True
    rgb_curves_001_curve_0 = rgb_curves_001.mapping.curves[0]
    rgb_curves_001_curve_0_point_0 = rgb_curves_001_curve_0.points[0]
    rgb_curves_001_curve_0_point_0.location = (0.0, 0.0)
    rgb_curves_001_curve_0_point_0.handle_type = 'AUTO'
    rgb_curves_001_curve_0_point_1 = rgb_curves_001_curve_0.points[1]
    rgb_curves_001_curve_0_point_1.location = (1.0, 1.0)
    rgb_curves_001_curve_0_point_1.handle_type = 'AUTO'
    rgb_curves_001_curve_1 = rgb_curves_001.mapping.curves[1]
    rgb_curves_001_curve_1_point_0 = rgb_curves_001_curve_1.points[0]
    rgb_curves_001_curve_1_point_0.location = (0.0, 0.0)
    rgb_curves_001_curve_1_point_0.handle_type = 'AUTO'
    rgb_curves_001_curve_1_point_1 = rgb_curves_001_curve_1.points[1]
    rgb_curves_001_curve_1_point_1.location = (1.0, 1.0)
    rgb_curves_001_curve_1_point_1.handle_type = 'AUTO'
    rgb_curves_001_curve_2 = rgb_curves_001.mapping.curves[2]
    rgb_curves_001_curve_2_point_0 = rgb_curves_001_curve_2.points[0]
    rgb_curves_001_curve_2_point_0.location = (0.0, 0.0)
    rgb_curves_001_curve_2_point_0.handle_type = 'AUTO'
    rgb_curves_001_curve_2_point_1 = rgb_curves_001_curve_2.points[1]
    rgb_curves_001_curve_2_point_1.location = (1.0, 1.0)
    rgb_curves_001_curve_2_point_1.handle_type = 'AUTO'
    rgb_curves_001_curve_3 = rgb_curves_001.mapping.curves[3]
    rgb_curves_001_curve_3_point_0 = rgb_curves_001_curve_3.points[0]
    rgb_curves_001_curve_3_point_0.location = (0.0, 0.0)
    rgb_curves_001_curve_3_point_0.handle_type = 'AUTO'
    rgb_curves_001_curve_3_point_1 = rgb_curves_001_curve_3.points[1]
    rgb_curves_001_curve_3_point_1.location = (0.34961429238319397, 0.15073515474796295)
    rgb_curves_001_curve_3_point_1.handle_type = 'AUTO'
    rgb_curves_001_curve_3_point_2 = rgb_curves_001_curve_3.points.new(0.6143959164619446, 0.764706015586853)
    rgb_curves_001_curve_3_point_2.handle_type = 'AUTO'
    rgb_curves_001_curve_3_point_3 = rgb_curves_001_curve_3.points.new(1.0, 1.0)
    rgb_curves_001_curve_3_point_3.handle_type = 'AUTO'
    rgb_curves_001.mapping.update()
    rgb_curves_001.inputs[0].default_value = 1.0
    mix_002_1 = rockshader___4.nodes.new("ShaderNodeMix")
    mix_002_1.name = "Mix.002"
    mix_002_1.blend_type = 'MIX'
    mix_002_1.clamp_factor = True
    mix_002_1.clamp_result = False
    mix_002_1.data_type = 'RGBA'
    mix_002_1.factor_mode = 'UNIFORM'
    mix_003_1 = rockshader___4.nodes.new("ShaderNodeMix")
    mix_003_1.name = "Mix.003"
    mix_003_1.blend_type = 'MIX'
    mix_003_1.clamp_factor = True
    mix_003_1.clamp_result = False
    mix_003_1.data_type = 'RGBA'
    mix_003_1.factor_mode = 'UNIFORM'
    voronoi_texture_1 = rockshader___4.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_1.name = "Voronoi Texture"
    voronoi_texture_1.distance = 'CHEBYCHEV'
    voronoi_texture_1.feature = 'F1'
    voronoi_texture_1.normalize = False
    voronoi_texture_1.voronoi_dimensions = '3D'
    voronoi_texture_1.inputs[3].default_value = 0.0
    voronoi_texture_1.inputs[4].default_value = 0.5
    voronoi_texture_1.inputs[5].default_value = 2.0
    voronoi_texture_1.inputs[8].default_value = 1.0
    wave_texture = rockshader___4.nodes.new("ShaderNodeTexWave")
    wave_texture.name = "Wave Texture"
    wave_texture.bands_direction = 'Z'
    wave_texture.rings_direction = 'X'
    wave_texture.wave_profile = 'SIN'
    wave_texture.wave_type = 'BANDS'
    wave_texture.inputs[2].default_value = 8.0
    wave_texture.inputs[4].default_value = 2.0
    wave_texture.inputs[5].default_value = 0.6200000047683716
    wave_texture.inputs[6].default_value = 0.0
    noise_texture_1 = rockshader___4.nodes.new("ShaderNodeTexNoise")
    noise_texture_1.name = "Noise Texture"
    noise_texture_1.noise_dimensions = '4D'
    noise_texture_1.noise_type = 'FBM'
    noise_texture_1.normalize = True
    noise_texture_1.inputs[1].default_value = 0.0
    noise_texture_1.inputs[4].default_value = 0.550000011920929
    noise_texture_1.inputs[5].default_value = 2.0
    noise_texture_1.inputs[8].default_value = 0.0
    wave_texture_001 = rockshader___4.nodes.new("ShaderNodeTexWave")
    wave_texture_001.name = "Wave Texture.001"
    wave_texture_001.bands_direction = 'Z'
    wave_texture_001.rings_direction = 'X'
    wave_texture_001.wave_profile = 'SIN'
    wave_texture_001.wave_type = 'BANDS'
    wave_texture_001.inputs[2].default_value = 20.0
    wave_texture_001.inputs[4].default_value = 2.0
    wave_texture_001.inputs[5].default_value = 0.6200000047683716
    wave_texture_001.inputs[6].default_value = 0.0
    hue_saturation_value_1 = rockshader___4.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_1.name = "Hue Saturation Value"
    hue_saturation_value_1.inputs[0].default_value = 0.5
    hue_saturation_value_1.inputs[1].default_value = 1.0
    hue_saturation_value_1.inputs[3].default_value = 1.0
    bump_1 = rockshader___4.nodes.new("ShaderNodeBump")
    bump_1.name = "Bump"
    bump_1.invert = False
    bump_1.inputs[1].default_value = 1.0
    bump_1.inputs[3].default_value = (0.0, 0.0, 0.0)
    bump_001_1 = rockshader___4.nodes.new("ShaderNodeBump")
    bump_001_1.name = "Bump.001"
    bump_001_1.invert = False
    bump_001_1.inputs[1].default_value = 1.0
    group_input_2 = rockshader___4.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"
    map_range_011_1 = rockshader___4.nodes.new("ShaderNodeMapRange")
    map_range_011_1.name = "Map Range.011"
    map_range_011_1.clamp = True
    map_range_011_1.data_type = 'FLOAT'
    map_range_011_1.interpolation_type = 'LINEAR'
    map_range_011_1.inputs[1].default_value = 0.0
    map_range_011_1.inputs[2].default_value = 1.0
    map_range_011_1.inputs[3].default_value = -1000.0
    map_range_011_1.inputs[4].default_value = 1000.0
    group_001_1 = rockshader___4.nodes.new("ShaderNodeGroup")
    group_001_1.name = "Group.001"
    group_001_1.node_tree = random_x2___mat
    group_001_1.inputs[0].default_value = 0.12449999898672104
    bump_002 = rockshader___4.nodes.new("ShaderNodeBump")
    bump_002.name = "Bump.002"
    bump_002.invert = False
    bump_002.inputs[1].default_value = 1.0
    bump_002.inputs[2].default_value = 1.0
    rockshader___4.links.new(mix_001_1.outputs[2], mix_002_1.inputs[0])
    rockshader___4.links.new(colorramp_001_1.outputs[0], bump_001_1.inputs[2])
    rockshader___4.links.new(hue_saturation_value_1.outputs[0], principled_bsdf_1.inputs[2])
    rockshader___4.links.new(mix_1.outputs[2], voronoi_texture_1.inputs[0])
    rockshader___4.links.new(mix_003_1.outputs[2], principled_bsdf_1.inputs[0])
    rockshader___4.links.new(noise_texture_1.outputs[1], mix_1.inputs[7])
    rockshader___4.links.new(bump_1.outputs[0], bump_001_1.inputs[3])
    rockshader___4.links.new(colorramp_1.outputs[0], hue_saturation_value_1.inputs[4])
    rockshader___4.links.new(mapping_001_1.outputs[0], mix_1.inputs[6])
    rockshader___4.links.new(noise_texture_1.outputs[0], bump_1.inputs[2])
    rockshader___4.links.new(rgb_curves_001.outputs[0], mix_001_1.inputs[6])
    rockshader___4.links.new(voronoi_texture_1.outputs[0], mix_003_1.inputs[0])
    rockshader___4.links.new(mapping_001_1.outputs[0], noise_texture_1.inputs[0])
    rockshader___4.links.new(mix_002_1.outputs[2], mix_003_1.inputs[6])
    rockshader___4.links.new(mapping_001_1.outputs[0], wave_texture_001.inputs[0])
    rockshader___4.links.new(texture_coordinate_1.outputs[3], mapping_1.inputs[0])
    rockshader___4.links.new(wave_texture.outputs[0], rgb_curves.inputs[1])
    rockshader___4.links.new(voronoi_texture_1.outputs[0], rgb_curves_001.inputs[1])
    rockshader___4.links.new(mix_003_1.outputs[2], colorramp_1.inputs[0])
    rockshader___4.links.new(mapping_001_1.outputs[0], wave_texture.inputs[0])
    rockshader___4.links.new(mapping_1.outputs[0], mapping_001_1.inputs[0])
    rockshader___4.links.new(rgb_curves.outputs[0], mix_001_1.inputs[7])
    rockshader___4.links.new(wave_texture_001.outputs[0], colorramp_001_1.inputs[0])
    rockshader___4.links.new(principled_bsdf_1.outputs[0], group_output_2.inputs[0])
    rockshader___4.links.new(group_input_2.outputs[0], mapping_1.inputs[3])
    rockshader___4.links.new(group_input_2.outputs[1], mix_002_1.inputs[6])
    rockshader___4.links.new(group_input_2.outputs[2], mix_002_1.inputs[7])
    rockshader___4.links.new(group_input_2.outputs[3], mix_003_1.inputs[7])
    rockshader___4.links.new(group_input_2.outputs[4], noise_texture_1.inputs[2])
    rockshader___4.links.new(group_input_2.outputs[5], voronoi_texture_1.inputs[2])
    rockshader___4.links.new(group_input_2.outputs[6], wave_texture.inputs[1])
    rockshader___4.links.new(group_input_2.outputs[7], wave_texture_001.inputs[1])
    rockshader___4.links.new(group_input_2.outputs[8], wave_texture.inputs[3])
    rockshader___4.links.new(group_input_2.outputs[8], noise_texture_1.inputs[3])
    rockshader___4.links.new(group_input_2.outputs[8], wave_texture_001.inputs[3])
    rockshader___4.links.new(group_input_2.outputs[9], hue_saturation_value_1.inputs[2])
    rockshader___4.links.new(group_input_2.outputs[10], bump_1.inputs[0])
    rockshader___4.links.new(group_input_2.outputs[11], bump_001_1.inputs[0])
    rockshader___4.links.new(group_001_1.outputs[0], map_range_011_1.inputs[0])
    rockshader___4.links.new(map_range_011_1.outputs[0], mapping_1.inputs[1])
    rockshader___4.links.new(bump_001_1.outputs[0], bump_002.inputs[3])
    rockshader___4.links.new(bump_002.outputs[0], principled_bsdf_1.inputs[5])
    rockshader___4.links.new(group_input_2.outputs[12], bump_002.inputs[0])
    return rockshader___4

rockshader___4 = rockshader___4_node_group()

def random_x4___mat_001_node_group():
    random_x4___mat_001 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "Random x4 | Mat.001")
    random_x4___mat_001.color_tag = 'NONE'
    random_x4___mat_001.default_group_node_width = 140
    _0_socket_1 = random_x4___mat_001.interface.new_socket(name = "0", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _0_socket_1.default_value = 0.0
    _0_socket_1.min_value = 0.0
    _0_socket_1.max_value = 1.0
    _0_socket_1.subtype = 'NONE'
    _0_socket_1.attribute_domain = 'POINT'
    _1_socket_1 = random_x4___mat_001.interface.new_socket(name = "1", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _1_socket_1.default_value = 0.0
    _1_socket_1.min_value = 0.0
    _1_socket_1.max_value = 1.0
    _1_socket_1.subtype = 'NONE'
    _1_socket_1.attribute_domain = 'POINT'
    _2_socket_1 = random_x4___mat_001.interface.new_socket(name = "2", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _2_socket_1.default_value = 0.0
    _2_socket_1.min_value = 0.0
    _2_socket_1.max_value = 1.0
    _2_socket_1.subtype = 'NONE'
    _2_socket_1.attribute_domain = 'POINT'
    _3_socket = random_x4___mat_001.interface.new_socket(name = "3", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _3_socket.default_value = 0.0
    _3_socket.min_value = 0.0
    _3_socket.max_value = 1.0
    _3_socket.subtype = 'NONE'
    _3_socket.attribute_domain = 'POINT'
    _4_socket = random_x4___mat_001.interface.new_socket(name = "4", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _4_socket.default_value = 0.0
    _4_socket.min_value = -3.4028234663852886e+38
    _4_socket.max_value = 3.4028234663852886e+38
    _4_socket.subtype = 'NONE'
    _4_socket.attribute_domain = 'POINT'
    seed_socket_1 = random_x4___mat_001.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketFloat')
    seed_socket_1.default_value = 0.0
    seed_socket_1.min_value = 0.0
    seed_socket_1.max_value = 1.0
    seed_socket_1.subtype = 'NONE'
    seed_socket_1.attribute_domain = 'POINT'
    group_output_3 = random_x4___mat_001.nodes.new("NodeGroupOutput")
    group_output_3.name = "Group Output"
    group_output_3.is_active_output = True
    group_input_3 = random_x4___mat_001.nodes.new("NodeGroupInput")
    group_input_3.name = "Group Input"
    object_info_1 = random_x4___mat_001.nodes.new("ShaderNodeObjectInfo")
    object_info_1.name = "Object Info"
    math_1 = random_x4___mat_001.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = 'ADD'
    math_1.use_clamp = False
    white_noise_texture_1 = random_x4___mat_001.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture_1.name = "White Noise Texture"
    white_noise_texture_1.noise_dimensions = '4D'
    separate_color_1 = random_x4___mat_001.nodes.new("ShaderNodeSeparateColor")
    separate_color_1.name = "Separate Color"
    separate_color_1.mode = 'RGB'
    math_001 = random_x4___mat_001.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'ADD'
    math_001.use_clamp = False
    white_noise_texture_001 = random_x4___mat_001.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture_001.name = "White Noise Texture.001"
    white_noise_texture_001.noise_dimensions = '4D'
    separate_color_001 = random_x4___mat_001.nodes.new("ShaderNodeSeparateColor")
    separate_color_001.name = "Separate Color.001"
    separate_color_001.mode = 'RGB'
    random_x4___mat_001.links.new(object_info_1.outputs[5], white_noise_texture_1.inputs[1])
    random_x4___mat_001.links.new(math_1.outputs[0], white_noise_texture_1.inputs[0])
    random_x4___mat_001.links.new(white_noise_texture_1.outputs[1], separate_color_1.inputs[0])
    random_x4___mat_001.links.new(object_info_1.outputs[3], math_1.inputs[1])
    random_x4___mat_001.links.new(group_input_3.outputs[0], math_1.inputs[0])
    random_x4___mat_001.links.new(separate_color_1.outputs[0], group_output_3.inputs[0])
    random_x4___mat_001.links.new(separate_color_1.outputs[1], group_output_3.inputs[1])
    random_x4___mat_001.links.new(math_001.outputs[0], white_noise_texture_001.inputs[0])
    random_x4___mat_001.links.new(white_noise_texture_001.outputs[1], separate_color_001.inputs[0])
    random_x4___mat_001.links.new(separate_color_1.outputs[2], math_001.inputs[1])
    random_x4___mat_001.links.new(math_1.outputs[0], math_001.inputs[0])
    random_x4___mat_001.links.new(separate_color_001.outputs[0], group_output_3.inputs[2])
    random_x4___mat_001.links.new(separate_color_001.outputs[1], group_output_3.inputs[3])
    random_x4___mat_001.links.new(object_info_1.outputs[5], white_noise_texture_001.inputs[1])
    random_x4___mat_001.links.new(separate_color_001.outputs[2], group_output_3.inputs[4])
    return random_x4___mat_001

random_x4___mat_001 = random_x4___mat_001_node_group()

def moonrockshader_node_group():
    moonrockshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "MoonRockShader")
    moonrockshader.color_tag = 'NONE'
    moonrockshader.default_group_node_width = 140
    bsdf_socket = moonrockshader.interface.new_socket(name = "BSDF", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    bsdf_socket.attribute_domain = 'POINT'
    scale_socket_2 = moonrockshader.interface.new_socket(name = "scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket_2.default_value = 16.0
    scale_socket_2.min_value = 0.0
    scale_socket_2.max_value = 3.4028234663852886e+38
    scale_socket_2.subtype = 'NONE'
    scale_socket_2.attribute_domain = 'POINT'
    color1_socket = moonrockshader.interface.new_socket(name = "color1", in_out='INPUT', socket_type = 'NodeSocketColor')
    color1_socket.default_value = (0.24619978666305542, 0.24620160460472107, 0.2462015002965927, 1.0)
    color1_socket.attribute_domain = 'POINT'
    color2_socket = moonrockshader.interface.new_socket(name = "color2", in_out='INPUT', socket_type = 'NodeSocketColor')
    color2_socket.default_value = (0.005181482061743736, 0.005181520711630583, 0.005181518383324146, 1.0)
    color2_socket.attribute_domain = 'POINT'
    edge_color_socket = moonrockshader.interface.new_socket(name = "edge_color", in_out='INPUT', socket_type = 'NodeSocketColor')
    edge_color_socket.default_value = (0.4000000059604645, 0.4000000059604645, 0.4000000059604645, 1.0)
    edge_color_socket.attribute_domain = 'POINT'
    noise_scale_socket_2 = moonrockshader.interface.new_socket(name = "noise_scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_scale_socket_2.default_value = 7.0
    noise_scale_socket_2.min_value = -1000.0
    noise_scale_socket_2.max_value = 1000.0
    noise_scale_socket_2.subtype = 'NONE'
    noise_scale_socket_2.attribute_domain = 'POINT'
    noise_detail_socket = moonrockshader.interface.new_socket(name = "noise_detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_detail_socket.default_value = 15.0
    noise_detail_socket.min_value = 0.0
    noise_detail_socket.max_value = 15.0
    noise_detail_socket.subtype = 'NONE'
    noise_detail_socket.attribute_domain = 'POINT'
    noise_roughness_socket = moonrockshader.interface.new_socket(name = "noise_roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_roughness_socket.default_value = 0.25
    noise_roughness_socket.min_value = 0.0
    noise_roughness_socket.max_value = 1.0
    noise_roughness_socket.subtype = 'FACTOR'
    noise_roughness_socket.attribute_domain = 'POINT'
    light_noise_scale_socket = moonrockshader.interface.new_socket(name = "light_noise_scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    light_noise_scale_socket.default_value = 5.0
    light_noise_scale_socket.min_value = 0.0
    light_noise_scale_socket.max_value = 15.0
    light_noise_scale_socket.subtype = 'NONE'
    light_noise_scale_socket.attribute_domain = 'POINT'
    light_noise_roughness_socket = moonrockshader.interface.new_socket(name = "light_noise_roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    light_noise_roughness_socket.default_value = 0.800000011920929
    light_noise_roughness_socket.min_value = 0.0
    light_noise_roughness_socket.max_value = 1.0
    light_noise_roughness_socket.subtype = 'FACTOR'
    light_noise_roughness_socket.attribute_domain = 'POINT'
    roughness_socket_2 = moonrockshader.interface.new_socket(name = "roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket_2.default_value = 1.0
    roughness_socket_2.min_value = 0.0
    roughness_socket_2.max_value = 2.0
    roughness_socket_2.subtype = 'NONE'
    roughness_socket_2.attribute_domain = 'POINT'
    noise_bump_scale_socket = moonrockshader.interface.new_socket(name = "noise_bump_scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_scale_socket.default_value = 15.0
    noise_bump_scale_socket.min_value = -1000.0
    noise_bump_scale_socket.max_value = 1000.0
    noise_bump_scale_socket.subtype = 'NONE'
    noise_bump_scale_socket.attribute_domain = 'POINT'
    noise_bump_strength_socket_2 = moonrockshader.interface.new_socket(name = "noise_bump_strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_strength_socket_2.default_value = 0.05000000074505806
    noise_bump_strength_socket_2.min_value = 0.0
    noise_bump_strength_socket_2.max_value = 1.0
    noise_bump_strength_socket_2.subtype = 'FACTOR'
    noise_bump_strength_socket_2.attribute_domain = 'POINT'
    detailed_noise_bump_strength_socket = moonrockshader.interface.new_socket(name = "detailed_noise_bump_strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detailed_noise_bump_strength_socket.default_value = 0.25
    detailed_noise_bump_strength_socket.min_value = 0.0
    detailed_noise_bump_strength_socket.max_value = 1.0
    detailed_noise_bump_strength_socket.subtype = 'FACTOR'
    detailed_noise_bump_strength_socket.attribute_domain = 'POINT'
    edge_color_strength_socket = moonrockshader.interface.new_socket(name = "edge_color_strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    edge_color_strength_socket.default_value = 0.75
    edge_color_strength_socket.min_value = 0.0
    edge_color_strength_socket.max_value = 1.0
    edge_color_strength_socket.subtype = 'FACTOR'
    edge_color_strength_socket.attribute_domain = 'POINT'
    noise_scale_mixer_socket = moonrockshader.interface.new_socket(name = "noise_scale_mixer", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_scale_mixer_socket.default_value = 0.009999999776482582
    noise_scale_mixer_socket.min_value = 0.0
    noise_scale_mixer_socket.max_value = 1.0
    noise_scale_mixer_socket.subtype = 'FACTOR'
    noise_scale_mixer_socket.attribute_domain = 'POINT'
    noise_bump_roughness_socket = moonrockshader.interface.new_socket(name = "noise_bump_roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_roughness_socket.default_value = 1.0
    noise_bump_roughness_socket.min_value = 0.0
    noise_bump_roughness_socket.max_value = 1.0
    noise_bump_roughness_socket.subtype = 'FACTOR'
    noise_bump_roughness_socket.attribute_domain = 'POINT'
    voronoi_bump_scale_socket = moonrockshader.interface.new_socket(name = "voronoi_bump_scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    voronoi_bump_scale_socket.default_value = 20.0
    voronoi_bump_scale_socket.min_value = -1000.0
    voronoi_bump_scale_socket.max_value = 1000.0
    voronoi_bump_scale_socket.subtype = 'NONE'
    voronoi_bump_scale_socket.attribute_domain = 'POINT'
    voronoi_bump_strength_socket = moonrockshader.interface.new_socket(name = "voronoi_bump_strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    voronoi_bump_strength_socket.default_value = 0.75
    voronoi_bump_strength_socket.min_value = 0.0
    voronoi_bump_strength_socket.max_value = 1.0
    voronoi_bump_strength_socket.subtype = 'FACTOR'
    voronoi_bump_strength_socket.attribute_domain = 'POINT'
    group_output_4 = moonrockshader.nodes.new("NodeGroupOutput")
    group_output_4.name = "Group Output"
    group_output_4.is_active_output = True
    group_input_4 = moonrockshader.nodes.new("NodeGroupInput")
    group_input_4.name = "Group Input"
    noise_texture_2 = moonrockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_2.name = "Noise Texture"
    noise_texture_2.noise_dimensions = '4D'
    noise_texture_2.noise_type = 'FBM'
    noise_texture_2.normalize = True
    noise_texture_2.inputs[5].default_value = 20.0
    noise_texture_2.inputs[8].default_value = 0.0
    mapping_001_2 = moonrockshader.nodes.new("ShaderNodeMapping")
    mapping_001_2.name = "Mapping.001"
    mapping_001_2.vector_type = 'POINT'
    mapping_001_2.inputs[2].default_value = (0.0, 0.0, 0.0)
    texture_coordinate_001 = moonrockshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_001.name = "Texture Coordinate.001"
    texture_coordinate_001.from_instancer = False
    texture_coordinate_001.outputs[0].hide = True
    texture_coordinate_001.outputs[1].hide = True
    texture_coordinate_001.outputs[2].hide = True
    texture_coordinate_001.outputs[4].hide = True
    texture_coordinate_001.outputs[5].hide = True
    texture_coordinate_001.outputs[6].hide = True
    bump_2 = moonrockshader.nodes.new("ShaderNodeBump")
    bump_2.name = "Bump"
    bump_2.invert = False
    bump_2.inputs[1].default_value = 1.0
    color_ramp = moonrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp.name = "Color Ramp"
    color_ramp.color_ramp.color_mode = 'RGB'
    color_ramp.color_ramp.hue_interpolation = 'NEAR'
    color_ramp.color_ramp.interpolation = 'LINEAR'
    color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
    color_ramp_cre_0 = color_ramp.color_ramp.elements[0]
    color_ramp_cre_0.position = 0.30181822180747986
    color_ramp_cre_0.alpha = 1.0
    color_ramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_cre_1 = color_ramp.color_ramp.elements.new(0.3945455849170685)
    color_ramp_cre_1.alpha = 1.0
    color_ramp_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    noise_texture_001_1 = moonrockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_001_1.name = "Noise Texture.001"
    noise_texture_001_1.noise_dimensions = '4D'
    noise_texture_001_1.noise_type = 'FBM'
    noise_texture_001_1.normalize = True
    noise_texture_001_1.inputs[5].default_value = 2.0
    noise_texture_001_1.inputs[8].default_value = 0.0
    color_ramp_001 = moonrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_001.name = "Color Ramp.001"
    color_ramp_001.color_ramp.color_mode = 'RGB'
    color_ramp_001.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_001.color_ramp.interpolation = 'LINEAR'
    color_ramp_001.color_ramp.elements.remove(color_ramp_001.color_ramp.elements[0])
    color_ramp_001_cre_0 = color_ramp_001.color_ramp.elements[0]
    color_ramp_001_cre_0.position = 0.4054546356201172
    color_ramp_001_cre_0.alpha = 1.0
    color_ramp_001_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_001_cre_1 = color_ramp_001.color_ramp.elements.new(0.64090895652771)
    color_ramp_001_cre_1.alpha = 1.0
    color_ramp_001_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    mix_2 = moonrockshader.nodes.new("ShaderNodeMix")
    mix_2.name = "Mix"
    mix_2.blend_type = 'MIX'
    mix_2.clamp_factor = True
    mix_2.clamp_result = False
    mix_2.data_type = 'RGBA'
    mix_2.factor_mode = 'UNIFORM'
    mix_001_2 = moonrockshader.nodes.new("ShaderNodeMix")
    mix_001_2.name = "Mix.001"
    mix_001_2.blend_type = 'MIX'
    mix_001_2.clamp_factor = True
    mix_001_2.clamp_result = False
    mix_001_2.data_type = 'RGBA'
    mix_001_2.factor_mode = 'UNIFORM'
    geometry = moonrockshader.nodes.new("ShaderNodeNewGeometry")
    geometry.name = "Geometry"
    geometry.outputs[0].hide = True
    geometry.outputs[1].hide = True
    geometry.outputs[2].hide = True
    geometry.outputs[3].hide = True
    geometry.outputs[4].hide = True
    geometry.outputs[5].hide = True
    geometry.outputs[6].hide = True
    geometry.outputs[8].hide = True
    color_ramp_002 = moonrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_002.name = "Color Ramp.002"
    color_ramp_002.color_ramp.color_mode = 'RGB'
    color_ramp_002.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_002.color_ramp.interpolation = 'EASE'
    color_ramp_002.color_ramp.elements.remove(color_ramp_002.color_ramp.elements[0])
    color_ramp_002_cre_0 = color_ramp_002.color_ramp.elements[0]
    color_ramp_002_cre_0.position = 0.5186362266540527
    color_ramp_002_cre_0.alpha = 1.0
    color_ramp_002_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_002_cre_1 = color_ramp_002.color_ramp.elements.new(0.6045457124710083)
    color_ramp_002_cre_1.alpha = 1.0
    color_ramp_002_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    mix_003_2 = moonrockshader.nodes.new("ShaderNodeMix")
    mix_003_2.name = "Mix.003"
    mix_003_2.blend_type = 'MIX'
    mix_003_2.clamp_factor = True
    mix_003_2.clamp_result = False
    mix_003_2.data_type = 'RGBA'
    mix_003_2.factor_mode = 'UNIFORM'
    color_ramp_004 = moonrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_004.name = "Color Ramp.004"
    color_ramp_004.color_ramp.color_mode = 'RGB'
    color_ramp_004.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_004.color_ramp.interpolation = 'LINEAR'
    color_ramp_004.color_ramp.elements.remove(color_ramp_004.color_ramp.elements[0])
    color_ramp_004_cre_0 = color_ramp_004.color_ramp.elements[0]
    color_ramp_004_cre_0.position = 0.0
    color_ramp_004_cre_0.alpha = 1.0
    color_ramp_004_cre_0.color = (0.6514015197753906, 0.6514063477516174, 0.6514060497283936, 1.0)
    color_ramp_004_cre_1 = color_ramp_004.color_ramp.elements.new(1.0)
    color_ramp_004_cre_1.alpha = 1.0
    color_ramp_004_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    noise_texture_003 = moonrockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_003.name = "Noise Texture.003"
    noise_texture_003.noise_dimensions = '4D'
    noise_texture_003.noise_type = 'FBM'
    noise_texture_003.normalize = True
    noise_texture_003.inputs[3].default_value = 15.0
    noise_texture_003.inputs[5].default_value = 0.0
    noise_texture_003.inputs[8].default_value = 0.0
    bump_001_2 = moonrockshader.nodes.new("ShaderNodeBump")
    bump_001_2.name = "Bump.001"
    bump_001_2.invert = False
    bump_001_2.inputs[1].default_value = 1.0
    frame_001 = moonrockshader.nodes.new("NodeFrame")
    frame_001.name = "Frame.001"
    frame_002 = moonrockshader.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    frame = moonrockshader.nodes.new("NodeFrame")
    frame.name = "Frame"
    hue_saturation_value_2 = moonrockshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_2.name = "Hue/Saturation/Value"
    hue_saturation_value_2.inputs[0].default_value = 0.5
    hue_saturation_value_2.inputs[1].default_value = 1.0
    hue_saturation_value_2.inputs[3].default_value = 1.0
    frame_003 = moonrockshader.nodes.new("NodeFrame")
    frame_003.name = "Frame.003"
    principled_bsdf_2 = moonrockshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_2.name = "Principled BSDF"
    principled_bsdf_2.distribution = 'MULTI_GGX'
    principled_bsdf_2.subsurface_method = 'RANDOM_WALK'
    principled_bsdf_2.inputs[1].default_value = 0.0
    principled_bsdf_2.inputs[3].default_value = 1.5
    principled_bsdf_2.inputs[4].default_value = 1.0
    principled_bsdf_2.inputs[7].default_value = 0.0
    principled_bsdf_2.inputs[8].default_value = 0.0
    principled_bsdf_2.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    principled_bsdf_2.inputs[10].default_value = 0.05000000074505806
    principled_bsdf_2.inputs[12].default_value = 0.0
    principled_bsdf_2.inputs[13].default_value = 0.5
    principled_bsdf_2.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_2.inputs[15].default_value = 0.0
    principled_bsdf_2.inputs[16].default_value = 0.0
    principled_bsdf_2.inputs[17].default_value = (0.0, 0.0, 0.0)
    principled_bsdf_2.inputs[18].default_value = 0.0
    principled_bsdf_2.inputs[19].default_value = 0.0
    principled_bsdf_2.inputs[20].default_value = 0.029999999329447746
    principled_bsdf_2.inputs[21].default_value = 1.5
    principled_bsdf_2.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_2.inputs[23].default_value = (0.0, 0.0, 0.0)
    principled_bsdf_2.inputs[24].default_value = 0.0
    principled_bsdf_2.inputs[25].default_value = 0.5
    principled_bsdf_2.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_2.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_2.inputs[28].default_value = 0.0
    principled_bsdf_2.inputs[29].default_value = 0.0
    principled_bsdf_2.inputs[30].default_value = 1.3300000429153442
    math_2 = moonrockshader.nodes.new("ShaderNodeMath")
    math_2.name = "Math"
    math_2.operation = 'MULTIPLY'
    math_2.use_clamp = False
    math_2.inputs[1].default_value = 10.0
    group_001_2 = moonrockshader.nodes.new("ShaderNodeGroup")
    group_001_2.name = "Group.001"
    group_001_2.node_tree = random_x4___mat_001
    group_001_2.inputs[0].default_value = 0.5213124752044678
    voronoi_texture_2 = moonrockshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_2.name = "Voronoi Texture"
    voronoi_texture_2.distance = 'EUCLIDEAN'
    voronoi_texture_2.feature = 'F1'
    voronoi_texture_2.normalize = True
    voronoi_texture_2.voronoi_dimensions = '4D'
    voronoi_texture_2.inputs[3].default_value = 0.0
    voronoi_texture_2.inputs[4].default_value = 1.0
    voronoi_texture_2.inputs[5].default_value = 2.0
    voronoi_texture_2.inputs[8].default_value = 1.0
    bump_002_1 = moonrockshader.nodes.new("ShaderNodeBump")
    bump_002_1.name = "Bump.002"
    bump_002_1.invert = False
    bump_002_1.inputs[1].default_value = 1.0
    color_ramp_005 = moonrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_005.name = "Color Ramp.005"
    color_ramp_005.color_ramp.color_mode = 'RGB'
    color_ramp_005.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_005.color_ramp.interpolation = 'EASE'
    color_ramp_005.color_ramp.elements.remove(color_ramp_005.color_ramp.elements[0])
    color_ramp_005_cre_0 = color_ramp_005.color_ramp.elements[0]
    color_ramp_005_cre_0.position = 0.0
    color_ramp_005_cre_0.alpha = 1.0
    color_ramp_005_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_005_cre_1 = color_ramp_005.color_ramp.elements.new(0.15909108519554138)
    color_ramp_005_cre_1.alpha = 1.0
    color_ramp_005_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    voronoi_texture_001_1 = moonrockshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001_1.name = "Voronoi Texture.001"
    voronoi_texture_001_1.distance = 'EUCLIDEAN'
    voronoi_texture_001_1.feature = 'SMOOTH_F1'
    voronoi_texture_001_1.normalize = True
    voronoi_texture_001_1.voronoi_dimensions = '4D'
    voronoi_texture_001_1.inputs[3].default_value = 0.0
    voronoi_texture_001_1.inputs[4].default_value = 1.0
    voronoi_texture_001_1.inputs[5].default_value = 2.0
    voronoi_texture_001_1.inputs[6].default_value = 1.0
    voronoi_texture_001_1.inputs[8].default_value = 1.0
    color_ramp_006 = moonrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_006.name = "Color Ramp.006"
    color_ramp_006.color_ramp.color_mode = 'RGB'
    color_ramp_006.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_006.color_ramp.interpolation = 'CARDINAL'
    color_ramp_006.color_ramp.elements.remove(color_ramp_006.color_ramp.elements[0])
    color_ramp_006_cre_0 = color_ramp_006.color_ramp.elements[0]
    color_ramp_006_cre_0.position = 0.0
    color_ramp_006_cre_0.alpha = 1.0
    color_ramp_006_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_006_cre_1 = color_ramp_006.color_ramp.elements.new(0.13181859254837036)
    color_ramp_006_cre_1.alpha = 1.0
    color_ramp_006_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    math_001_1 = moonrockshader.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = 'DIVIDE'
    math_001_1.use_clamp = False
    bump_003 = moonrockshader.nodes.new("ShaderNodeBump")
    bump_003.name = "Bump.003"
    bump_003.invert = False
    bump_003.inputs[1].default_value = 1.0
    bump_003.inputs[3].default_value = (0.0, 0.0, 0.0)
    map_range_004 = moonrockshader.nodes.new("ShaderNodeMapRange")
    map_range_004.name = "Map Range.004"
    map_range_004.clamp = True
    map_range_004.data_type = 'FLOAT'
    map_range_004.interpolation_type = 'LINEAR'
    map_range_004.inputs[1].default_value = 0.0
    map_range_004.inputs[2].default_value = 1.0
    map_range_004.inputs[3].default_value = -1000.0
    map_range_004.inputs[4].default_value = 1000.0
    group_002 = moonrockshader.nodes.new("ShaderNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = random_x4___mat_001
    math_002 = moonrockshader.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'MULTIPLY'
    math_002.use_clamp = False
    math_003 = moonrockshader.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'MULTIPLY'
    math_003.use_clamp = False
    math_003.inputs[1].default_value = 5.0
    math_004 = moonrockshader.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'MULTIPLY'
    math_004.use_clamp = False
    moonrockshader.links.new(mapping_001_2.outputs[0], noise_texture_001_1.inputs[0])
    moonrockshader.links.new(noise_texture_001_1.outputs[0], color_ramp_001.inputs[0])
    moonrockshader.links.new(color_ramp_001.outputs[0], mix_2.inputs[7])
    moonrockshader.links.new(color_ramp_004.outputs[0], hue_saturation_value_2.inputs[4])
    moonrockshader.links.new(mix_001_2.outputs[2], mix_003_2.inputs[6])
    moonrockshader.links.new(mix_003_2.outputs[2], principled_bsdf_2.inputs[0])
    moonrockshader.links.new(color_ramp_002.outputs[0], mix_003_2.inputs[0])
    moonrockshader.links.new(hue_saturation_value_2.outputs[0], principled_bsdf_2.inputs[2])
    moonrockshader.links.new(color_ramp.outputs[0], mix_2.inputs[6])
    moonrockshader.links.new(mix_2.outputs[2], color_ramp_004.inputs[0])
    moonrockshader.links.new(mapping_001_2.outputs[0], noise_texture_003.inputs[0])
    moonrockshader.links.new(bump_2.outputs[0], bump_001_2.inputs[3])
    moonrockshader.links.new(mix_2.outputs[2], mix_001_2.inputs[0])
    moonrockshader.links.new(mapping_001_2.outputs[0], noise_texture_2.inputs[0])
    moonrockshader.links.new(geometry.outputs[7], color_ramp_002.inputs[0])
    moonrockshader.links.new(mix_2.outputs[2], bump_001_2.inputs[2])
    moonrockshader.links.new(noise_texture_2.outputs[0], color_ramp.inputs[0])
    moonrockshader.links.new(texture_coordinate_001.outputs[3], mapping_001_2.inputs[0])
    moonrockshader.links.new(principled_bsdf_2.outputs[0], group_output_4.inputs[0])
    moonrockshader.links.new(group_input_4.outputs[0], mapping_001_2.inputs[3])
    moonrockshader.links.new(group_input_4.outputs[1], mix_001_2.inputs[6])
    moonrockshader.links.new(group_input_4.outputs[2], mix_001_2.inputs[7])
    moonrockshader.links.new(group_input_4.outputs[3], mix_003_2.inputs[7])
    moonrockshader.links.new(group_input_4.outputs[5], noise_texture_2.inputs[3])
    moonrockshader.links.new(group_input_4.outputs[6], noise_texture_2.inputs[4])
    moonrockshader.links.new(group_input_4.outputs[5], noise_texture_001_1.inputs[3])
    moonrockshader.links.new(group_input_4.outputs[6], noise_texture_001_1.inputs[4])
    moonrockshader.links.new(group_input_4.outputs[9], hue_saturation_value_2.inputs[2])
    moonrockshader.links.new(group_input_4.outputs[11], bump_2.inputs[0])
    moonrockshader.links.new(group_input_4.outputs[10], noise_texture_003.inputs[2])
    moonrockshader.links.new(group_input_4.outputs[12], bump_001_2.inputs[0])
    moonrockshader.links.new(group_input_4.outputs[4], noise_texture_001_1.inputs[2])
    moonrockshader.links.new(group_input_4.outputs[14], mix_2.inputs[0])
    moonrockshader.links.new(group_input_4.outputs[4], math_2.inputs[0])
    moonrockshader.links.new(math_2.outputs[0], noise_texture_2.inputs[2])
    moonrockshader.links.new(group_input_4.outputs[15], noise_texture_003.inputs[4])
    moonrockshader.links.new(group_001_2.outputs[4], noise_texture_001_1.inputs[1])
    moonrockshader.links.new(group_001_2.outputs[3], noise_texture_2.inputs[1])
    moonrockshader.links.new(group_001_2.outputs[1], noise_texture_003.inputs[1])
    moonrockshader.links.new(bump_001_2.outputs[0], principled_bsdf_2.inputs[5])
    moonrockshader.links.new(noise_texture_003.outputs[0], bump_2.inputs[2])
    moonrockshader.links.new(mapping_001_2.outputs[0], voronoi_texture_2.inputs[0])
    moonrockshader.links.new(group_001_2.outputs[1], voronoi_texture_2.inputs[1])
    moonrockshader.links.new(color_ramp_005.outputs[0], bump_002_1.inputs[2])
    moonrockshader.links.new(bump_002_1.outputs[0], bump_2.inputs[3])
    moonrockshader.links.new(voronoi_texture_2.outputs[0], color_ramp_005.inputs[0])
    moonrockshader.links.new(group_input_4.outputs[16], voronoi_texture_2.inputs[2])
    moonrockshader.links.new(mapping_001_2.outputs[0], voronoi_texture_001_1.inputs[0])
    moonrockshader.links.new(group_001_2.outputs[1], voronoi_texture_001_1.inputs[1])
    moonrockshader.links.new(math_001_1.outputs[0], voronoi_texture_001_1.inputs[2])
    moonrockshader.links.new(voronoi_texture_001_1.outputs[0], color_ramp_006.inputs[0])
    moonrockshader.links.new(group_input_4.outputs[16], math_001_1.inputs[0])
    moonrockshader.links.new(color_ramp_006.outputs[0], bump_003.inputs[2])
    moonrockshader.links.new(bump_003.outputs[0], bump_002_1.inputs[3])
    moonrockshader.links.new(map_range_004.outputs[0], mapping_001_2.inputs[1])
    moonrockshader.links.new(group_001_2.outputs[0], map_range_004.inputs[0])
    moonrockshader.links.new(group_002.outputs[0], math_002.inputs[1])
    moonrockshader.links.new(group_input_4.outputs[17], math_002.inputs[0])
    moonrockshader.links.new(math_002.outputs[0], bump_003.inputs[0])
    moonrockshader.links.new(group_001_2.outputs[2], group_002.inputs[0])
    moonrockshader.links.new(math_003.outputs[0], math_001_1.inputs[1])
    moonrockshader.links.new(group_002.outputs[1], math_003.inputs[0])
    moonrockshader.links.new(group_input_4.outputs[17], math_004.inputs[0])
    moonrockshader.links.new(group_002.outputs[2], math_004.inputs[1])
    moonrockshader.links.new(math_004.outputs[0], bump_002_1.inputs[0])
    return moonrockshader

moonrockshader = moonrockshader_node_group()

def marsrockshader_node_group():
    marsrockshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "MarsRockShader")
    marsrockshader.color_tag = 'NONE'
    marsrockshader.default_group_node_width = 140
    shader_socket_2 = marsrockshader.interface.new_socket(name = "Shader", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    shader_socket_2.attribute_domain = 'POINT'
    group_output_5 = marsrockshader.nodes.new("NodeGroupOutput")
    group_output_5.name = "Group Output"
    group_output_5.is_active_output = True
    group_005 = marsrockshader.nodes.new("ShaderNodeGroup")
    group_005.name = "Group.005"
    group_005.node_tree = rockshader___3
    group_005.inputs[0].default_value = 1.0
    group_005.inputs[5].default_value = 17.600000381469727
    group_005.inputs[6].default_value = 2.7400002479553223
    group_005.inputs[7].default_value = 15.0
    group_005.inputs[8].default_value = 0.6979339122772217
    group_005.inputs[9].default_value = 0.3623966872692108
    group_005.inputs[10].default_value = 2.0
    group_005.inputs[11].default_value = 0.43471091985702515
    group_005.inputs[12].default_value = 0.2264467179775238
    group_006 = marsrockshader.nodes.new("ShaderNodeGroup")
    group_006.name = "Group.006"
    group_006.node_tree = rockshader___4
    group_006.inputs[0].default_value = 1.0
    group_006.inputs[4].default_value = 18.68000030517578
    group_006.inputs[5].default_value = 3.840001106262207
    group_006.inputs[6].default_value = 4.180000305175781
    group_006.inputs[7].default_value = 0.010000094771385193
    group_006.inputs[8].default_value = 15.0
    group_006.inputs[9].default_value = 2.0
    group_006.inputs[10].default_value = 0.3370434641838074
    group_006.inputs[11].default_value = 0.931240439414978
    group_006.inputs[12].default_value = 0.19363099336624146
    combine_color_001 = marsrockshader.nodes.new("ShaderNodeCombineColor")
    combine_color_001.name = "Combine Color.001"
    combine_color_001.mode = 'HSV'
    combine_color_001.inputs[0].default_value = 0.029999999329447746
    combine_color_001.inputs[1].default_value = 0.8999999761581421
    map_range_005 = marsrockshader.nodes.new("ShaderNodeMapRange")
    map_range_005.name = "Map Range.005"
    map_range_005.clamp = True
    map_range_005.data_type = 'FLOAT'
    map_range_005.interpolation_type = 'LINEAR'
    map_range_005.inputs[1].default_value = 0.0
    map_range_005.inputs[2].default_value = 1.0
    map_range_005.inputs[3].default_value = 0.05000000074505806
    map_range_005.inputs[4].default_value = 0.30000001192092896
    combine_color_002 = marsrockshader.nodes.new("ShaderNodeCombineColor")
    combine_color_002.name = "Combine Color.002"
    combine_color_002.mode = 'HSV'
    combine_color_002.inputs[0].default_value = 0.021490026265382767
    combine_color_002.inputs[1].default_value = 0.800000011920929
    map_range_006 = marsrockshader.nodes.new("ShaderNodeMapRange")
    map_range_006.name = "Map Range.006"
    map_range_006.clamp = True
    map_range_006.data_type = 'FLOAT'
    map_range_006.interpolation_type = 'LINEAR'
    map_range_006.inputs[1].default_value = 0.0
    map_range_006.inputs[2].default_value = 1.0
    map_range_006.inputs[3].default_value = 0.009999999776482582
    map_range_006.inputs[4].default_value = 0.019999999552965164
    group_008 = marsrockshader.nodes.new("ShaderNodeGroup")
    group_008.name = "Group.008"
    group_008.node_tree = moonrockshader
    group_008.inputs[0].default_value = 1.5
    group_008.inputs[4].default_value = 11.029998779296875
    group_008.inputs[5].default_value = 15.0
    group_008.inputs[6].default_value = 0.6499999761581421
    group_008.inputs[7].default_value = 8.320000648498535
    group_008.inputs[8].default_value = 0.7736417055130005
    group_008.inputs[9].default_value = 2.0
    group_008.inputs[10].default_value = 17.369998931884766
    group_008.inputs[11].default_value = 0.16358695924282074
    group_008.inputs[12].default_value = 0.3608698546886444
    group_008.inputs[13].default_value = 0.5271739959716797
    group_008.inputs[15].default_value = 0.2190222144126892
    group_008.inputs[16].default_value = 15.0
    group_008.inputs[17].default_value = 0.2663043737411499
    mix_shader_001 = marsrockshader.nodes.new("ShaderNodeMixShader")
    mix_shader_001.name = "Mix Shader.001"
    mix_shader_002 = marsrockshader.nodes.new("ShaderNodeMixShader")
    mix_shader_002.name = "Mix Shader.002"
    mapping_001_3 = marsrockshader.nodes.new("ShaderNodeMapping")
    mapping_001_3.name = "Mapping.001"
    mapping_001_3.vector_type = 'POINT'
    mapping_001_3.inputs[2].default_value = (0.0, 0.0, 0.0)
    mapping_001_3.inputs[3].default_value = (1.0, 1.0, 1.0)
    texture_coordinate_001_1 = marsrockshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_001_1.name = "Texture Coordinate.001"
    texture_coordinate_001_1.from_instancer = False
    texture_coordinate_001_1.outputs[0].hide = True
    texture_coordinate_001_1.outputs[1].hide = True
    texture_coordinate_001_1.outputs[2].hide = True
    texture_coordinate_001_1.outputs[4].hide = True
    texture_coordinate_001_1.outputs[5].hide = True
    texture_coordinate_001_1.outputs[6].hide = True
    noise_texture_003_1 = marsrockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_003_1.name = "Noise Texture.003"
    noise_texture_003_1.noise_dimensions = '3D'
    noise_texture_003_1.noise_type = 'HETERO_TERRAIN'
    noise_texture_003_1.normalize = True
    noise_texture_003_1.inputs[3].default_value = 15.0
    noise_texture_003_1.inputs[4].default_value = 0.5166667103767395
    noise_texture_003_1.inputs[5].default_value = 15.179998397827148
    noise_texture_003_1.inputs[6].default_value = 0.14000000059604645
    noise_texture_003_1.inputs[8].default_value = 0.0
    color_ramp_004_1 = marsrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_004_1.name = "Color Ramp.004"
    color_ramp_004_1.color_ramp.color_mode = 'RGB'
    color_ramp_004_1.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_004_1.color_ramp.interpolation = 'EASE'
    color_ramp_004_1.color_ramp.elements.remove(color_ramp_004_1.color_ramp.elements[0])
    color_ramp_004_1_cre_0 = color_ramp_004_1.color_ramp.elements[0]
    color_ramp_004_1_cre_0.position = 0.18636341392993927
    color_ramp_004_1_cre_0.alpha = 1.0
    color_ramp_004_1_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_004_1_cre_1 = color_ramp_004_1.color_ramp.elements.new(0.9186362028121948)
    color_ramp_004_1_cre_1.alpha = 1.0
    color_ramp_004_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    map_range_002 = marsrockshader.nodes.new("ShaderNodeMapRange")
    map_range_002.name = "Map Range.002"
    map_range_002.clamp = True
    map_range_002.data_type = 'FLOAT'
    map_range_002.interpolation_type = 'LINEAR'
    map_range_002.inputs[1].default_value = 0.0
    map_range_002.inputs[2].default_value = 1.0
    map_range_002.inputs[3].default_value = 0.020000003278255463
    map_range_002.inputs[4].default_value = 0.08000001311302185
    noise_texture_005 = marsrockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_005.name = "Noise Texture.005"
    noise_texture_005.noise_dimensions = '3D'
    noise_texture_005.noise_type = 'FBM'
    noise_texture_005.normalize = True
    noise_texture_005.inputs[3].default_value = 5.0
    noise_texture_005.inputs[4].default_value = 0.6670835614204407
    noise_texture_005.inputs[5].default_value = 5.0
    noise_texture_005.inputs[8].default_value = 0.0
    color_ramp_006_1 = marsrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_006_1.name = "Color Ramp.006"
    color_ramp_006_1.color_ramp.color_mode = 'RGB'
    color_ramp_006_1.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_006_1.color_ramp.interpolation = 'EASE'
    color_ramp_006_1.color_ramp.elements.remove(color_ramp_006_1.color_ramp.elements[0])
    color_ramp_006_1_cre_0 = color_ramp_006_1.color_ramp.elements[0]
    color_ramp_006_1_cre_0.position = 0.5681818127632141
    color_ramp_006_1_cre_0.alpha = 1.0
    color_ramp_006_1_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_006_1_cre_1 = color_ramp_006_1.color_ramp.elements.new(0.7000001072883606)
    color_ramp_006_1_cre_1.alpha = 1.0
    color_ramp_006_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    map_range_007 = marsrockshader.nodes.new("ShaderNodeMapRange")
    map_range_007.name = "Map Range.007"
    map_range_007.clamp = True
    map_range_007.data_type = 'FLOAT'
    map_range_007.interpolation_type = 'LINEAR'
    map_range_007.inputs[1].default_value = 0.0
    map_range_007.inputs[2].default_value = 1.0
    map_range_007.inputs[3].default_value = 0.02500000037252903
    map_range_007.inputs[4].default_value = 0.07500000298023224
    map_range_015 = marsrockshader.nodes.new("ShaderNodeMapRange")
    map_range_015.name = "Map Range.015"
    map_range_015.clamp = True
    map_range_015.data_type = 'FLOAT'
    map_range_015.interpolation_type = 'LINEAR'
    map_range_015.inputs[1].default_value = 0.0
    map_range_015.inputs[2].default_value = 1.0
    map_range_015.inputs[3].default_value = -1000.0
    map_range_015.inputs[4].default_value = 1000.0
    group = marsrockshader.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = random_x4___mat_001
    group.inputs[0].default_value = 0.521340012550354
    combine_color_006 = marsrockshader.nodes.new("ShaderNodeCombineColor")
    combine_color_006.name = "Combine Color.006"
    combine_color_006.mode = 'HSV'
    combine_color_006.inputs[0].default_value = 0.03500000014901161
    combine_color_006.inputs[1].default_value = 0.08500000089406967
    map_range_011_2 = marsrockshader.nodes.new("ShaderNodeMapRange")
    map_range_011_2.name = "Map Range.011"
    map_range_011_2.clamp = True
    map_range_011_2.data_type = 'FLOAT'
    map_range_011_2.interpolation_type = 'LINEAR'
    map_range_011_2.inputs[1].default_value = 0.0
    map_range_011_2.inputs[2].default_value = 1.0
    map_range_011_2.inputs[3].default_value = 0.0
    map_range_011_2.inputs[4].default_value = 0.029999999329447746
    marsrockshader.links.new(combine_color_002.outputs[0], group_006.inputs[2])
    marsrockshader.links.new(group.outputs[0], map_range_015.inputs[0])
    marsrockshader.links.new(group.outputs[2], map_range_002.inputs[0])
    marsrockshader.links.new(combine_color_001.outputs[0], group_005.inputs[1])
    marsrockshader.links.new(group_006.outputs[0], mix_shader_001.inputs[2])
    marsrockshader.links.new(group.outputs[2], map_range_007.inputs[0])
    marsrockshader.links.new(group_005.outputs[0], mix_shader_001.inputs[1])
    marsrockshader.links.new(color_ramp_004_1.outputs[0], mix_shader_001.inputs[0])
    marsrockshader.links.new(mix_shader_001.outputs[0], mix_shader_002.inputs[2])
    marsrockshader.links.new(color_ramp_006_1.outputs[0], mix_shader_002.inputs[0])
    marsrockshader.links.new(texture_coordinate_001_1.outputs[3], mapping_001_3.inputs[0])
    marsrockshader.links.new(map_range_005.outputs[0], combine_color_001.inputs[2])
    marsrockshader.links.new(combine_color_001.outputs[0], group_008.inputs[3])
    marsrockshader.links.new(map_range_006.outputs[0], combine_color_002.inputs[2])
    marsrockshader.links.new(combine_color_002.outputs[0], group_008.inputs[1])
    marsrockshader.links.new(noise_texture_003_1.outputs[0], color_ramp_004_1.inputs[0])
    marsrockshader.links.new(mapping_001_3.outputs[0], noise_texture_003_1.inputs[0])
    marsrockshader.links.new(map_range_002.outputs[0], noise_texture_003_1.inputs[2])
    marsrockshader.links.new(group.outputs[1], map_range_005.inputs[0])
    marsrockshader.links.new(map_range_015.outputs[0], mapping_001_3.inputs[1])
    marsrockshader.links.new(noise_texture_005.outputs[0], color_ramp_006_1.inputs[0])
    marsrockshader.links.new(combine_color_002.outputs[0], group_005.inputs[4])
    marsrockshader.links.new(mapping_001_3.outputs[0], noise_texture_005.inputs[0])
    marsrockshader.links.new(map_range_007.outputs[0], noise_texture_005.inputs[2])
    marsrockshader.links.new(combine_color_001.outputs[0], group_006.inputs[3])
    marsrockshader.links.new(mix_shader_002.outputs[0], group_output_5.inputs[0])
    marsrockshader.links.new(group_008.outputs[0], mix_shader_002.inputs[1])
    marsrockshader.links.new(group.outputs[0], map_range_006.inputs[0])
    marsrockshader.links.new(group.outputs[3], group_008.inputs[14])
    marsrockshader.links.new(combine_color_006.outputs[0], group_008.inputs[2])
    marsrockshader.links.new(combine_color_006.outputs[0], group_005.inputs[2])
    marsrockshader.links.new(combine_color_006.outputs[0], group_006.inputs[1])
    marsrockshader.links.new(combine_color_006.outputs[0], group_005.inputs[3])
    marsrockshader.links.new(map_range_011_2.outputs[0], combine_color_006.inputs[2])
    marsrockshader.links.new(group.outputs[4], map_range_011_2.inputs[0])
    return marsrockshader

marsrockshader = marsrockshader_node_group()

def marsrockmat_node_group():
    marsrockmat = mat.node_tree
    for node in marsrockmat.nodes:
        marsrockmat.nodes.remove(node)
    marsrockmat.color_tag = 'NONE'
    marsrockmat.default_group_node_width = 140
    material_output = marsrockmat.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    material_output.inputs[3].default_value = 0.0
    group_003 = marsrockmat.nodes.new("ShaderNodeGroup")
    group_003.name = "Group.003"
    group_003.node_tree = marsrockshader
    marsrockmat.links.new(group_003.outputs[0], material_output.inputs[0])
    return marsrockmat

marsrockmat = marsrockmat_node_group()


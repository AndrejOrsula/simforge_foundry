import bpy

mat = bpy.data.materials.new(name = "MoonRockMat")
mat.use_nodes = True

def random_x4___mat_node_group():
    random_x4___mat = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "Random x4 | Mat")
    random_x4___mat.color_tag = 'NONE'
    random_x4___mat.default_group_node_width = 140
    _0_socket = random_x4___mat.interface.new_socket(name = "0", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _0_socket.default_value = 0.0
    _0_socket.min_value = 0.0
    _0_socket.max_value = 1.0
    _0_socket.subtype = 'NONE'
    _0_socket.attribute_domain = 'POINT'
    _1_socket = random_x4___mat.interface.new_socket(name = "1", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _1_socket.default_value = 0.0
    _1_socket.min_value = 0.0
    _1_socket.max_value = 1.0
    _1_socket.subtype = 'NONE'
    _1_socket.attribute_domain = 'POINT'
    _2_socket = random_x4___mat.interface.new_socket(name = "2", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _2_socket.default_value = 0.0
    _2_socket.min_value = 0.0
    _2_socket.max_value = 1.0
    _2_socket.subtype = 'NONE'
    _2_socket.attribute_domain = 'POINT'
    _3_socket = random_x4___mat.interface.new_socket(name = "3", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _3_socket.default_value = 0.0
    _3_socket.min_value = 0.0
    _3_socket.max_value = 1.0
    _3_socket.subtype = 'NONE'
    _3_socket.attribute_domain = 'POINT'
    _4_socket = random_x4___mat.interface.new_socket(name = "4", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _4_socket.default_value = 0.0
    _4_socket.min_value = -3.4028234663852886e+38
    _4_socket.max_value = 3.4028234663852886e+38
    _4_socket.subtype = 'NONE'
    _4_socket.attribute_domain = 'POINT'
    seed_socket = random_x4___mat.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketFloat')
    seed_socket.default_value = 0.0
    seed_socket.min_value = 0.0
    seed_socket.max_value = 1.0
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    group_output = random_x4___mat.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    group_input = random_x4___mat.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    object_info = random_x4___mat.nodes.new("ShaderNodeObjectInfo")
    object_info.name = "Object Info"
    math = random_x4___mat.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'ADD'
    math.use_clamp = False
    white_noise_texture = random_x4___mat.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture.name = "White Noise Texture"
    white_noise_texture.noise_dimensions = '4D'
    separate_color = random_x4___mat.nodes.new("ShaderNodeSeparateColor")
    separate_color.name = "Separate Color"
    separate_color.mode = 'RGB'
    math_001 = random_x4___mat.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'ADD'
    math_001.use_clamp = False
    white_noise_texture_001 = random_x4___mat.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture_001.name = "White Noise Texture.001"
    white_noise_texture_001.noise_dimensions = '4D'
    separate_color_001 = random_x4___mat.nodes.new("ShaderNodeSeparateColor")
    separate_color_001.name = "Separate Color.001"
    separate_color_001.mode = 'RGB'
    random_x4___mat.links.new(object_info.outputs[5], white_noise_texture.inputs[1])
    random_x4___mat.links.new(math.outputs[0], white_noise_texture.inputs[0])
    random_x4___mat.links.new(white_noise_texture.outputs[1], separate_color.inputs[0])
    random_x4___mat.links.new(object_info.outputs[3], math.inputs[1])
    random_x4___mat.links.new(group_input.outputs[0], math.inputs[0])
    random_x4___mat.links.new(separate_color.outputs[0], group_output.inputs[0])
    random_x4___mat.links.new(separate_color.outputs[1], group_output.inputs[1])
    random_x4___mat.links.new(math_001.outputs[0], white_noise_texture_001.inputs[0])
    random_x4___mat.links.new(white_noise_texture_001.outputs[1], separate_color_001.inputs[0])
    random_x4___mat.links.new(separate_color.outputs[2], math_001.inputs[1])
    random_x4___mat.links.new(math.outputs[0], math_001.inputs[0])
    random_x4___mat.links.new(separate_color_001.outputs[0], group_output.inputs[2])
    random_x4___mat.links.new(separate_color_001.outputs[1], group_output.inputs[3])
    random_x4___mat.links.new(object_info.outputs[5], white_noise_texture_001.inputs[1])
    random_x4___mat.links.new(separate_color_001.outputs[2], group_output.inputs[4])
    return random_x4___mat

random_x4___mat = random_x4___mat_node_group()

def moonrockshader_node_group():
    moonrockshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "MoonRockShader")
    moonrockshader.color_tag = 'NONE'
    moonrockshader.default_group_node_width = 140
    bsdf_socket = moonrockshader.interface.new_socket(name = "BSDF", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    bsdf_socket.attribute_domain = 'POINT'
    scale_socket = moonrockshader.interface.new_socket(name = "scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 16.0
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    color1_socket = moonrockshader.interface.new_socket(name = "color1", in_out='INPUT', socket_type = 'NodeSocketColor')
    color1_socket.default_value = (0.24619978666305542, 0.24620160460472107, 0.2462015002965927, 1.0)
    color1_socket.attribute_domain = 'POINT'
    color2_socket = moonrockshader.interface.new_socket(name = "color2", in_out='INPUT', socket_type = 'NodeSocketColor')
    color2_socket.default_value = (0.005181482061743736, 0.005181520711630583, 0.005181518383324146, 1.0)
    color2_socket.attribute_domain = 'POINT'
    edge_color_socket = moonrockshader.interface.new_socket(name = "edge_color", in_out='INPUT', socket_type = 'NodeSocketColor')
    edge_color_socket.default_value = (0.4000000059604645, 0.4000000059604645, 0.4000000059604645, 1.0)
    edge_color_socket.attribute_domain = 'POINT'
    noise_scale_socket = moonrockshader.interface.new_socket(name = "noise_scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_scale_socket.default_value = 7.0
    noise_scale_socket.min_value = -1000.0
    noise_scale_socket.max_value = 1000.0
    noise_scale_socket.subtype = 'NONE'
    noise_scale_socket.attribute_domain = 'POINT'
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
    roughness_socket = moonrockshader.interface.new_socket(name = "roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = 'NONE'
    roughness_socket.attribute_domain = 'POINT'
    noise_bump_scale_socket = moonrockshader.interface.new_socket(name = "noise_bump_scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_scale_socket.default_value = 15.0
    noise_bump_scale_socket.min_value = -1000.0
    noise_bump_scale_socket.max_value = 1000.0
    noise_bump_scale_socket.subtype = 'NONE'
    noise_bump_scale_socket.attribute_domain = 'POINT'
    noise_bump_strength_socket = moonrockshader.interface.new_socket(name = "noise_bump_strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_strength_socket.default_value = 0.05000000074505806
    noise_bump_strength_socket.min_value = 0.0
    noise_bump_strength_socket.max_value = 1.0
    noise_bump_strength_socket.subtype = 'FACTOR'
    noise_bump_strength_socket.attribute_domain = 'POINT'
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
    group_output_1 = moonrockshader.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True
    group_input_1 = moonrockshader.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"
    noise_texture = moonrockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '4D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    noise_texture.inputs[5].default_value = 20.0
    noise_texture.inputs[8].default_value = 0.0
    mapping_001 = moonrockshader.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = 'POINT'
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    texture_coordinate_001 = moonrockshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_001.name = "Texture Coordinate.001"
    texture_coordinate_001.from_instancer = False
    texture_coordinate_001.outputs[0].hide = True
    texture_coordinate_001.outputs[1].hide = True
    texture_coordinate_001.outputs[2].hide = True
    texture_coordinate_001.outputs[4].hide = True
    texture_coordinate_001.outputs[5].hide = True
    texture_coordinate_001.outputs[6].hide = True
    bump = moonrockshader.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    bump.inputs[1].default_value = 1.0
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
    noise_texture_001 = moonrockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = '4D'
    noise_texture_001.noise_type = 'FBM'
    noise_texture_001.normalize = True
    noise_texture_001.inputs[5].default_value = 2.0
    noise_texture_001.inputs[8].default_value = 0.0
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
    mix = moonrockshader.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'MIX'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'
    mix_001 = moonrockshader.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'MIX'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'RGBA'
    mix_001.factor_mode = 'UNIFORM'
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
    mix_003 = moonrockshader.nodes.new("ShaderNodeMix")
    mix_003.name = "Mix.003"
    mix_003.blend_type = 'MIX'
    mix_003.clamp_factor = True
    mix_003.clamp_result = False
    mix_003.data_type = 'RGBA'
    mix_003.factor_mode = 'UNIFORM'
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
    bump_001 = moonrockshader.nodes.new("ShaderNodeBump")
    bump_001.name = "Bump.001"
    bump_001.invert = False
    bump_001.inputs[1].default_value = 1.0
    frame_001 = moonrockshader.nodes.new("NodeFrame")
    frame_001.name = "Frame.001"
    frame_002 = moonrockshader.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    frame = moonrockshader.nodes.new("NodeFrame")
    frame.name = "Frame"
    hue_saturation_value = moonrockshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    hue_saturation_value.inputs[0].default_value = 0.5
    hue_saturation_value.inputs[1].default_value = 1.0
    hue_saturation_value.inputs[3].default_value = 1.0
    frame_003 = moonrockshader.nodes.new("NodeFrame")
    frame_003.name = "Frame.003"
    principled_bsdf = moonrockshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    principled_bsdf.inputs[1].default_value = 0.0
    principled_bsdf.inputs[3].default_value = 1.5
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
    math_1 = moonrockshader.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = 'MULTIPLY'
    math_1.use_clamp = False
    math_1.inputs[1].default_value = 10.0
    group_001 = moonrockshader.nodes.new("ShaderNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = random_x4___mat
    group_001.inputs[0].default_value = 0.5213124752044678
    voronoi_texture = moonrockshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = 'EUCLIDEAN'
    voronoi_texture.feature = 'F1'
    voronoi_texture.normalize = True
    voronoi_texture.voronoi_dimensions = '4D'
    voronoi_texture.inputs[3].default_value = 0.0
    voronoi_texture.inputs[4].default_value = 1.0
    voronoi_texture.inputs[5].default_value = 2.0
    voronoi_texture.inputs[8].default_value = 1.0
    bump_002 = moonrockshader.nodes.new("ShaderNodeBump")
    bump_002.name = "Bump.002"
    bump_002.invert = False
    bump_002.inputs[1].default_value = 1.0
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
    voronoi_texture_001 = moonrockshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001.name = "Voronoi Texture.001"
    voronoi_texture_001.distance = 'EUCLIDEAN'
    voronoi_texture_001.feature = 'SMOOTH_F1'
    voronoi_texture_001.normalize = True
    voronoi_texture_001.voronoi_dimensions = '4D'
    voronoi_texture_001.inputs[3].default_value = 0.0
    voronoi_texture_001.inputs[4].default_value = 1.0
    voronoi_texture_001.inputs[5].default_value = 2.0
    voronoi_texture_001.inputs[6].default_value = 1.0
    voronoi_texture_001.inputs[8].default_value = 1.0
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
    group_002.node_tree = random_x4___mat
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
    moonrockshader.links.new(mapping_001.outputs[0], noise_texture_001.inputs[0])
    moonrockshader.links.new(noise_texture_001.outputs[0], color_ramp_001.inputs[0])
    moonrockshader.links.new(color_ramp_001.outputs[0], mix.inputs[7])
    moonrockshader.links.new(color_ramp_004.outputs[0], hue_saturation_value.inputs[4])
    moonrockshader.links.new(mix_001.outputs[2], mix_003.inputs[6])
    moonrockshader.links.new(mix_003.outputs[2], principled_bsdf.inputs[0])
    moonrockshader.links.new(color_ramp_002.outputs[0], mix_003.inputs[0])
    moonrockshader.links.new(hue_saturation_value.outputs[0], principled_bsdf.inputs[2])
    moonrockshader.links.new(color_ramp.outputs[0], mix.inputs[6])
    moonrockshader.links.new(mix.outputs[2], color_ramp_004.inputs[0])
    moonrockshader.links.new(mapping_001.outputs[0], noise_texture_003.inputs[0])
    moonrockshader.links.new(bump.outputs[0], bump_001.inputs[3])
    moonrockshader.links.new(mix.outputs[2], mix_001.inputs[0])
    moonrockshader.links.new(mapping_001.outputs[0], noise_texture.inputs[0])
    moonrockshader.links.new(geometry.outputs[7], color_ramp_002.inputs[0])
    moonrockshader.links.new(mix.outputs[2], bump_001.inputs[2])
    moonrockshader.links.new(noise_texture.outputs[0], color_ramp.inputs[0])
    moonrockshader.links.new(texture_coordinate_001.outputs[3], mapping_001.inputs[0])
    moonrockshader.links.new(principled_bsdf.outputs[0], group_output_1.inputs[0])
    moonrockshader.links.new(group_input_1.outputs[0], mapping_001.inputs[3])
    moonrockshader.links.new(group_input_1.outputs[1], mix_001.inputs[6])
    moonrockshader.links.new(group_input_1.outputs[2], mix_001.inputs[7])
    moonrockshader.links.new(group_input_1.outputs[3], mix_003.inputs[7])
    moonrockshader.links.new(group_input_1.outputs[5], noise_texture.inputs[3])
    moonrockshader.links.new(group_input_1.outputs[6], noise_texture.inputs[4])
    moonrockshader.links.new(group_input_1.outputs[5], noise_texture_001.inputs[3])
    moonrockshader.links.new(group_input_1.outputs[6], noise_texture_001.inputs[4])
    moonrockshader.links.new(group_input_1.outputs[9], hue_saturation_value.inputs[2])
    moonrockshader.links.new(group_input_1.outputs[11], bump.inputs[0])
    moonrockshader.links.new(group_input_1.outputs[10], noise_texture_003.inputs[2])
    moonrockshader.links.new(group_input_1.outputs[12], bump_001.inputs[0])
    moonrockshader.links.new(group_input_1.outputs[4], noise_texture_001.inputs[2])
    moonrockshader.links.new(group_input_1.outputs[14], mix.inputs[0])
    moonrockshader.links.new(group_input_1.outputs[4], math_1.inputs[0])
    moonrockshader.links.new(math_1.outputs[0], noise_texture.inputs[2])
    moonrockshader.links.new(group_input_1.outputs[15], noise_texture_003.inputs[4])
    moonrockshader.links.new(group_001.outputs[4], noise_texture_001.inputs[1])
    moonrockshader.links.new(group_001.outputs[3], noise_texture.inputs[1])
    moonrockshader.links.new(group_001.outputs[1], noise_texture_003.inputs[1])
    moonrockshader.links.new(bump_001.outputs[0], principled_bsdf.inputs[5])
    moonrockshader.links.new(noise_texture_003.outputs[0], bump.inputs[2])
    moonrockshader.links.new(mapping_001.outputs[0], voronoi_texture.inputs[0])
    moonrockshader.links.new(group_001.outputs[1], voronoi_texture.inputs[1])
    moonrockshader.links.new(color_ramp_005.outputs[0], bump_002.inputs[2])
    moonrockshader.links.new(bump_002.outputs[0], bump.inputs[3])
    moonrockshader.links.new(voronoi_texture.outputs[0], color_ramp_005.inputs[0])
    moonrockshader.links.new(group_input_1.outputs[16], voronoi_texture.inputs[2])
    moonrockshader.links.new(mapping_001.outputs[0], voronoi_texture_001.inputs[0])
    moonrockshader.links.new(group_001.outputs[1], voronoi_texture_001.inputs[1])
    moonrockshader.links.new(math_001_1.outputs[0], voronoi_texture_001.inputs[2])
    moonrockshader.links.new(voronoi_texture_001.outputs[0], color_ramp_006.inputs[0])
    moonrockshader.links.new(group_input_1.outputs[16], math_001_1.inputs[0])
    moonrockshader.links.new(color_ramp_006.outputs[0], bump_003.inputs[2])
    moonrockshader.links.new(bump_003.outputs[0], bump_002.inputs[3])
    moonrockshader.links.new(map_range_004.outputs[0], mapping_001.inputs[1])
    moonrockshader.links.new(group_001.outputs[0], map_range_004.inputs[0])
    moonrockshader.links.new(group_002.outputs[0], math_002.inputs[1])
    moonrockshader.links.new(group_input_1.outputs[17], math_002.inputs[0])
    moonrockshader.links.new(math_002.outputs[0], bump_003.inputs[0])
    moonrockshader.links.new(group_001.outputs[2], group_002.inputs[0])
    moonrockshader.links.new(math_003.outputs[0], math_001_1.inputs[1])
    moonrockshader.links.new(group_002.outputs[1], math_003.inputs[0])
    moonrockshader.links.new(group_input_1.outputs[17], math_004.inputs[0])
    moonrockshader.links.new(group_002.outputs[2], math_004.inputs[1])
    moonrockshader.links.new(math_004.outputs[0], bump_002.inputs[0])
    return moonrockshader

moonrockshader = moonrockshader_node_group()

def moonrockmat_node_group():
    moonrockmat = mat.node_tree
    for node in moonrockmat.nodes:
        moonrockmat.nodes.remove(node)
    moonrockmat.color_tag = 'NONE'
    moonrockmat.default_group_node_width = 140
    material_output = moonrockmat.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    material_output.inputs[3].default_value = 0.0
    group_006 = moonrockmat.nodes.new("ShaderNodeGroup")
    group_006.name = "Group.006"
    group_006.node_tree = moonrockshader
    group_006.inputs[0].default_value = 16.0
    group_006.inputs[1].default_value = (0.24619978666305542, 0.24620160460472107, 0.2462015002965927, 1.0)
    group_006.inputs[2].default_value = (0.005181482061743736, 0.005181520711630583, 0.005181518383324146, 1.0)
    group_006.inputs[3].default_value = (0.4000000059604645, 0.4000000059604645, 0.4000000059604645, 1.0)
    group_006.inputs[4].default_value = 7.0
    group_006.inputs[5].default_value = 15.0
    group_006.inputs[6].default_value = 0.25
    group_006.inputs[7].default_value = 5.0
    group_006.inputs[8].default_value = 0.800000011920929
    group_006.inputs[9].default_value = 1.0
    group_006.inputs[10].default_value = 15.0
    group_006.inputs[11].default_value = 0.05000000074505806
    group_006.inputs[12].default_value = 0.25
    group_006.inputs[13].default_value = 0.75
    group_006.inputs[14].default_value = 0.009999999776482582
    group_006.inputs[15].default_value = 1.0
    group_006.inputs[16].default_value = 20.0
    group_006.inputs[17].default_value = 0.75
    moonrockmat.links.new(group_006.outputs[0], material_output.inputs[0])
    return moonrockmat

moonrockmat = moonrockmat_node_group()


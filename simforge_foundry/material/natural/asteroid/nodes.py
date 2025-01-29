import bpy

mat = bpy.data.materials.new(name = "AsteroidMat")
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

def asteroidshader_node_group():
    asteroidshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "AsteroidShader")
    asteroidshader.color_tag = 'NONE'
    asteroidshader.default_group_node_width = 140
    bsdf_socket = asteroidshader.interface.new_socket(name = "BSDF", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    bsdf_socket.attribute_domain = 'POINT'
    scale_socket = asteroidshader.interface.new_socket(name = "scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'DISTANCE'
    scale_socket.attribute_domain = 'POINT'
    color1_socket = asteroidshader.interface.new_socket(name = "color1", in_out='INPUT', socket_type = 'NodeSocketColor')
    color1_socket.default_value = (0.0998980849981308, 0.0998988226056099, 0.09989877790212631, 1.0)
    color1_socket.attribute_domain = 'POINT'
    color2_socket = asteroidshader.interface.new_socket(name = "color2", in_out='INPUT', socket_type = 'NodeSocketColor')
    color2_socket.default_value = (0.019382229074835777, 0.019382374361157417, 0.01938236691057682, 1.0)
    color2_socket.attribute_domain = 'POINT'
    group_output_1 = asteroidshader.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True
    group_input_1 = asteroidshader.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"
    mapping_001 = asteroidshader.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = 'POINT'
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    texture_coordinate_001 = asteroidshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_001.name = "Texture Coordinate.001"
    texture_coordinate_001.from_instancer = False
    texture_coordinate_001.outputs[0].hide = True
    texture_coordinate_001.outputs[1].hide = True
    texture_coordinate_001.outputs[2].hide = True
    texture_coordinate_001.outputs[4].hide = True
    texture_coordinate_001.outputs[5].hide = True
    texture_coordinate_001.outputs[6].hide = True
    principled_bsdf = asteroidshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    principled_bsdf.inputs[1].default_value = 0.0
    principled_bsdf.inputs[2].default_value = 0.800000011920929
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
    group_001 = asteroidshader.nodes.new("ShaderNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = random_x4___mat
    group_001.inputs[0].default_value = 0.801234245300293
    map_range_004 = asteroidshader.nodes.new("ShaderNodeMapRange")
    map_range_004.name = "Map Range.004"
    map_range_004.clamp = True
    map_range_004.data_type = 'FLOAT'
    map_range_004.interpolation_type = 'LINEAR'
    map_range_004.inputs[1].default_value = 0.0
    map_range_004.inputs[2].default_value = 1.0
    map_range_004.inputs[3].default_value = -1000.0
    map_range_004.inputs[4].default_value = 1000.0
    voronoi_texture = asteroidshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = 'EUCLIDEAN'
    voronoi_texture.feature = 'SMOOTH_F1'
    voronoi_texture.normalize = False
    voronoi_texture.voronoi_dimensions = '4D'
    voronoi_texture.inputs[3].default_value = 0.0
    voronoi_texture.inputs[4].default_value = 0.5
    voronoi_texture.inputs[5].default_value = 2.0
    voronoi_texture.inputs[6].default_value = 1.0
    voronoi_texture.inputs[8].default_value = 1.0
    bump_003 = asteroidshader.nodes.new("ShaderNodeBump")
    bump_003.name = "Bump.003"
    bump_003.invert = False
    bump_003.inputs[1].default_value = 1.0
    bump_003.inputs[3].default_value = (0.0, 0.0, 0.0)
    noise_texture = asteroidshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '4D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    noise_texture.inputs[3].default_value = 15.0
    noise_texture.inputs[4].default_value = 0.5
    noise_texture.inputs[5].default_value = 2.0
    noise_texture.inputs[8].default_value = 0.0
    mix = asteroidshader.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'LINEAR_LIGHT'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'
    mix.inputs[0].default_value = 0.012000000104308128
    color_ramp = asteroidshader.nodes.new("ShaderNodeValToRGB")
    color_ramp.name = "Color Ramp"
    color_ramp.color_ramp.color_mode = 'RGB'
    color_ramp.color_ramp.hue_interpolation = 'NEAR'
    color_ramp.color_ramp.interpolation = 'EASE'
    color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
    color_ramp_cre_0 = color_ramp.color_ramp.elements[0]
    color_ramp_cre_0.position = 0.13636358082294464
    color_ramp_cre_0.alpha = 1.0
    color_ramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_cre_1 = color_ramp.color_ramp.elements.new(0.4454546570777893)
    color_ramp_cre_1.alpha = 1.0
    color_ramp_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    hue_saturation_value = asteroidshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    hue_saturation_value.inputs[0].default_value = 0.5
    hue_saturation_value.inputs[1].default_value = 1.0
    hue_saturation_value.inputs[3].default_value = 1.0
    rgb_curves = asteroidshader.nodes.new("ShaderNodeRGBCurve")
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
    rgb_curves_curve_3_point_0.handle_type = 'AUTO_CLAMPED'
    rgb_curves_curve_3_point_1 = rgb_curves_curve_3.points[1]
    rgb_curves_curve_3_point_1.location = (0.2545453608036041, 0.7124989032745361)
    rgb_curves_curve_3_point_1.handle_type = 'AUTO_CLAMPED'
    rgb_curves_curve_3_point_2 = rgb_curves_curve_3.points.new(0.7045456171035767, 0.9687498211860657)
    rgb_curves_curve_3_point_2.handle_type = 'AUTO_CLAMPED'
    rgb_curves_curve_3_point_3 = rgb_curves_curve_3.points.new(1.0, 1.0)
    rgb_curves_curve_3_point_3.handle_type = 'AUTO'
    rgb_curves.mapping.update()
    rgb_curves.inputs[0].default_value = 1.0
    voronoi_texture_001 = asteroidshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001.name = "Voronoi Texture.001"
    voronoi_texture_001.distance = 'EUCLIDEAN'
    voronoi_texture_001.feature = 'F1'
    voronoi_texture_001.normalize = False
    voronoi_texture_001.voronoi_dimensions = '4D'
    voronoi_texture_001.inputs[2].default_value = 4.0
    voronoi_texture_001.inputs[3].default_value = 8.0
    voronoi_texture_001.inputs[4].default_value = 0.5
    voronoi_texture_001.inputs[5].default_value = 2.0
    voronoi_texture_001.inputs[8].default_value = 1.0
    mix_002 = asteroidshader.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = 'MIX'
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = 'RGBA'
    mix_002.factor_mode = 'UNIFORM'
    bump_004 = asteroidshader.nodes.new("ShaderNodeBump")
    bump_004.name = "Bump.004"
    bump_004.invert = False
    bump_004.inputs[1].default_value = 1.0
    map_range = asteroidshader.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = True
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    map_range.inputs[1].default_value = 0.0
    map_range.inputs[2].default_value = 1.0
    map_range.inputs[3].default_value = 2.0
    map_range.inputs[4].default_value = 10.0
    group_002 = asteroidshader.nodes.new("ShaderNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = random_x4___mat
    map_range_001 = asteroidshader.nodes.new("ShaderNodeMapRange")
    map_range_001.name = "Map Range.001"
    map_range_001.clamp = True
    map_range_001.data_type = 'FLOAT'
    map_range_001.interpolation_type = 'LINEAR'
    map_range_001.inputs[1].default_value = 0.0
    map_range_001.inputs[2].default_value = 1.0
    map_range_001.inputs[3].default_value = 20.0
    map_range_001.inputs[4].default_value = 40.0
    map_range_002 = asteroidshader.nodes.new("ShaderNodeMapRange")
    map_range_002.name = "Map Range.002"
    map_range_002.clamp = True
    map_range_002.data_type = 'FLOAT'
    map_range_002.interpolation_type = 'LINEAR'
    map_range_002.inputs[1].default_value = 0.0
    map_range_002.inputs[2].default_value = 1.0
    map_range_002.inputs[3].default_value = 0.800000011920929
    map_range_002.inputs[4].default_value = 1.399999976158142
    map_range_003 = asteroidshader.nodes.new("ShaderNodeMapRange")
    map_range_003.name = "Map Range.003"
    map_range_003.clamp = True
    map_range_003.data_type = 'FLOAT'
    map_range_003.interpolation_type = 'LINEAR'
    map_range_003.inputs[1].default_value = 0.0
    map_range_003.inputs[2].default_value = 1.0
    map_range_003.inputs[3].default_value = 0.07500000298023224
    map_range_003.inputs[4].default_value = 0.20000000298023224
    map_range_005 = asteroidshader.nodes.new("ShaderNodeMapRange")
    map_range_005.name = "Map Range.005"
    map_range_005.clamp = True
    map_range_005.data_type = 'FLOAT'
    map_range_005.interpolation_type = 'LINEAR'
    map_range_005.inputs[1].default_value = 0.0
    map_range_005.inputs[2].default_value = 1.0
    map_range_005.inputs[3].default_value = 0.22499999403953552
    map_range_005.inputs[4].default_value = 0.5
    asteroidshader.links.new(texture_coordinate_001.outputs[3], mapping_001.inputs[0])
    asteroidshader.links.new(principled_bsdf.outputs[0], group_output_1.inputs[0])
    asteroidshader.links.new(group_input_1.outputs[0], mapping_001.inputs[3])
    asteroidshader.links.new(map_range_004.outputs[0], mapping_001.inputs[1])
    asteroidshader.links.new(group_001.outputs[0], map_range_004.inputs[0])
    asteroidshader.links.new(mapping_001.outputs[0], noise_texture.inputs[0])
    asteroidshader.links.new(mix.outputs[2], voronoi_texture.inputs[0])
    asteroidshader.links.new(noise_texture.outputs[1], mix.inputs[7])
    asteroidshader.links.new(mapping_001.outputs[0], mix.inputs[6])
    asteroidshader.links.new(hue_saturation_value.outputs[0], color_ramp.inputs[0])
    asteroidshader.links.new(voronoi_texture.outputs[0], hue_saturation_value.inputs[4])
    asteroidshader.links.new(color_ramp.outputs[0], rgb_curves.inputs[1])
    asteroidshader.links.new(mapping_001.outputs[0], voronoi_texture_001.inputs[0])
    asteroidshader.links.new(mix_002.outputs[2], principled_bsdf.inputs[0])
    asteroidshader.links.new(voronoi_texture_001.outputs[0], mix_002.inputs[0])
    asteroidshader.links.new(bump_003.outputs[0], bump_004.inputs[3])
    asteroidshader.links.new(bump_004.outputs[0], principled_bsdf.inputs[5])
    asteroidshader.links.new(voronoi_texture_001.outputs[0], bump_004.inputs[2])
    asteroidshader.links.new(rgb_curves.outputs[0], bump_003.inputs[2])
    asteroidshader.links.new(group_input_1.outputs[1], mix_002.inputs[6])
    asteroidshader.links.new(group_input_1.outputs[2], mix_002.inputs[7])
    asteroidshader.links.new(group_001.outputs[1], noise_texture.inputs[1])
    asteroidshader.links.new(group_001.outputs[2], voronoi_texture.inputs[1])
    asteroidshader.links.new(group_001.outputs[3], voronoi_texture_001.inputs[1])
    asteroidshader.links.new(group_001.outputs[4], group_002.inputs[0])
    asteroidshader.links.new(map_range.outputs[0], voronoi_texture.inputs[2])
    asteroidshader.links.new(group_002.outputs[0], map_range_001.inputs[0])
    asteroidshader.links.new(group_002.outputs[1], map_range.inputs[0])
    asteroidshader.links.new(map_range_001.outputs[0], noise_texture.inputs[2])
    asteroidshader.links.new(group_002.outputs[2], map_range_002.inputs[0])
    asteroidshader.links.new(map_range_002.outputs[0], hue_saturation_value.inputs[2])
    asteroidshader.links.new(group_002.outputs[3], map_range_003.inputs[0])
    asteroidshader.links.new(group_002.outputs[4], map_range_005.inputs[0])
    asteroidshader.links.new(map_range_005.outputs[0], bump_003.inputs[0])
    asteroidshader.links.new(map_range_003.outputs[0], bump_004.inputs[0])
    return asteroidshader

asteroidshader = asteroidshader_node_group()

def asteroidmat_node_group():
    asteroidmat = mat.node_tree
    for node in asteroidmat.nodes:
        asteroidmat.nodes.remove(node)
    asteroidmat.color_tag = 'NONE'
    asteroidmat.default_group_node_width = 140
    material_output = asteroidmat.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    material_output.inputs[3].default_value = 0.0
    group_006 = asteroidmat.nodes.new("ShaderNodeGroup")
    group_006.name = "Group.006"
    group_006.node_tree = asteroidshader
    group_006.inputs[0].default_value = 1.0
    group_006.inputs[1].default_value = (0.0998980849981308, 0.0998988226056099, 0.09989877790212631, 1.0)
    group_006.inputs[2].default_value = (0.019382229074835777, 0.019382374361157417, 0.01938236691057682, 1.0)
    asteroidmat.links.new(group_006.outputs[0], material_output.inputs[0])
    return asteroidmat

asteroidmat = asteroidmat_node_group()


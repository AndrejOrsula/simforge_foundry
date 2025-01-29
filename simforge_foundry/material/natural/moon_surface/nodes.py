import bpy

mat = bpy.data.materials.new(name = "MoonSurfaceMat")
mat.use_nodes = True

def random_x4___mat_005_node_group():
    random_x4___mat_005 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "Random x4 | Mat.005")
    random_x4___mat_005.color_tag = 'NONE'
    random_x4___mat_005.default_group_node_width = 140
    _0_socket = random_x4___mat_005.interface.new_socket(name = "0", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _0_socket.default_value = 0.0
    _0_socket.min_value = 0.0
    _0_socket.max_value = 1.0
    _0_socket.subtype = 'NONE'
    _0_socket.attribute_domain = 'POINT'
    _1_socket = random_x4___mat_005.interface.new_socket(name = "1", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _1_socket.default_value = 0.0
    _1_socket.min_value = 0.0
    _1_socket.max_value = 1.0
    _1_socket.subtype = 'NONE'
    _1_socket.attribute_domain = 'POINT'
    _2_socket = random_x4___mat_005.interface.new_socket(name = "2", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _2_socket.default_value = 0.0
    _2_socket.min_value = 0.0
    _2_socket.max_value = 1.0
    _2_socket.subtype = 'NONE'
    _2_socket.attribute_domain = 'POINT'
    _3_socket = random_x4___mat_005.interface.new_socket(name = "3", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _3_socket.default_value = 0.0
    _3_socket.min_value = 0.0
    _3_socket.max_value = 1.0
    _3_socket.subtype = 'NONE'
    _3_socket.attribute_domain = 'POINT'
    _4_socket = random_x4___mat_005.interface.new_socket(name = "4", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _4_socket.default_value = 0.0
    _4_socket.min_value = -3.4028234663852886e+38
    _4_socket.max_value = 3.4028234663852886e+38
    _4_socket.subtype = 'NONE'
    _4_socket.attribute_domain = 'POINT'
    seed_socket = random_x4___mat_005.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketFloat')
    seed_socket.default_value = 0.0
    seed_socket.min_value = 0.0
    seed_socket.max_value = 1.0
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    group_output = random_x4___mat_005.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    group_input = random_x4___mat_005.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    object_info = random_x4___mat_005.nodes.new("ShaderNodeObjectInfo")
    object_info.name = "Object Info"
    math = random_x4___mat_005.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'ADD'
    math.use_clamp = False
    white_noise_texture = random_x4___mat_005.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture.name = "White Noise Texture"
    white_noise_texture.noise_dimensions = '4D'
    separate_color = random_x4___mat_005.nodes.new("ShaderNodeSeparateColor")
    separate_color.name = "Separate Color"
    separate_color.mode = 'RGB'
    math_001 = random_x4___mat_005.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'ADD'
    math_001.use_clamp = False
    white_noise_texture_001 = random_x4___mat_005.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture_001.name = "White Noise Texture.001"
    white_noise_texture_001.noise_dimensions = '4D'
    separate_color_001 = random_x4___mat_005.nodes.new("ShaderNodeSeparateColor")
    separate_color_001.name = "Separate Color.001"
    separate_color_001.mode = 'RGB'
    random_x4___mat_005.links.new(object_info.outputs[5], white_noise_texture.inputs[1])
    random_x4___mat_005.links.new(math.outputs[0], white_noise_texture.inputs[0])
    random_x4___mat_005.links.new(white_noise_texture.outputs[1], separate_color.inputs[0])
    random_x4___mat_005.links.new(object_info.outputs[3], math.inputs[1])
    random_x4___mat_005.links.new(group_input.outputs[0], math.inputs[0])
    random_x4___mat_005.links.new(separate_color.outputs[0], group_output.inputs[0])
    random_x4___mat_005.links.new(separate_color.outputs[1], group_output.inputs[1])
    random_x4___mat_005.links.new(math_001.outputs[0], white_noise_texture_001.inputs[0])
    random_x4___mat_005.links.new(white_noise_texture_001.outputs[1], separate_color_001.inputs[0])
    random_x4___mat_005.links.new(separate_color.outputs[2], math_001.inputs[1])
    random_x4___mat_005.links.new(math.outputs[0], math_001.inputs[0])
    random_x4___mat_005.links.new(separate_color_001.outputs[0], group_output.inputs[2])
    random_x4___mat_005.links.new(separate_color_001.outputs[1], group_output.inputs[3])
    random_x4___mat_005.links.new(object_info.outputs[5], white_noise_texture_001.inputs[1])
    random_x4___mat_005.links.new(separate_color_001.outputs[2], group_output.inputs[4])
    return random_x4___mat_005

random_x4___mat_005 = random_x4___mat_005_node_group()

def rockygroundshader_002_node_group():
    rockygroundshader_002 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "RockyGroundShader.002")
    rockygroundshader_002.color_tag = 'NONE'
    rockygroundshader_002.default_group_node_width = 140
    shader_socket = rockygroundshader_002.interface.new_socket(name = "Shader", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    shader_socket.attribute_domain = 'POINT'
    scale_socket = rockygroundshader_002.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    rocks_visibility_socket = rockygroundshader_002.interface.new_socket(name = "Rocks Visibility", in_out='INPUT', socket_type = 'NodeSocketFloat')
    rocks_visibility_socket.default_value = 1.0
    rocks_visibility_socket.min_value = 0.0
    rocks_visibility_socket.max_value = 2.0
    rocks_visibility_socket.subtype = 'NONE'
    rocks_visibility_socket.attribute_domain = 'POINT'
    rock_color_1_socket = rockygroundshader_002.interface.new_socket(name = "Rock Color 1", in_out='INPUT', socket_type = 'NodeSocketColor')
    rock_color_1_socket.default_value = (0.10047899931669235, 0.10047899931669235, 0.10047899931669235, 1.0)
    rock_color_1_socket.attribute_domain = 'POINT'
    rock_color_2_socket = rockygroundshader_002.interface.new_socket(name = "Rock Color 2", in_out='INPUT', socket_type = 'NodeSocketColor')
    rock_color_2_socket.default_value = (0.10048799961805344, 0.08293099701404572, 0.07997799664735794, 1.0)
    rock_color_2_socket.attribute_domain = 'POINT'
    rocks_detail_socket = rockygroundshader_002.interface.new_socket(name = "Rocks Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
    rocks_detail_socket.default_value = 0.5
    rocks_detail_socket.min_value = 0.0
    rocks_detail_socket.max_value = 1.0
    rocks_detail_socket.subtype = 'FACTOR'
    rocks_detail_socket.attribute_domain = 'POINT'
    large_rocks_scale_socket = rockygroundshader_002.interface.new_socket(name = "Large Rocks Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    large_rocks_scale_socket.default_value = 14.0
    large_rocks_scale_socket.min_value = -1000.0
    large_rocks_scale_socket.max_value = 1000.0
    large_rocks_scale_socket.subtype = 'NONE'
    large_rocks_scale_socket.attribute_domain = 'POINT'
    small_rocks_scale_socket = rockygroundshader_002.interface.new_socket(name = "Small Rocks Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    small_rocks_scale_socket.default_value = 34.0
    small_rocks_scale_socket.min_value = -1000.0
    small_rocks_scale_socket.max_value = 1000.0
    small_rocks_scale_socket.subtype = 'NONE'
    small_rocks_scale_socket.attribute_domain = 'POINT'
    dirt_color_1_socket = rockygroundshader_002.interface.new_socket(name = "Dirt Color 1", in_out='INPUT', socket_type = 'NodeSocketColor')
    dirt_color_1_socket.default_value = (0.12273299694061279, 0.06268499791622162, 0.028358999639749527, 1.0)
    dirt_color_1_socket.attribute_domain = 'POINT'
    dirt_color_2_socket = rockygroundshader_002.interface.new_socket(name = "Dirt Color 2", in_out='INPUT', socket_type = 'NodeSocketColor')
    dirt_color_2_socket.default_value = (0.016374999657273293, 0.011485000140964985, 0.006409999914467335, 1.0)
    dirt_color_2_socket.attribute_domain = 'POINT'
    dirt_color_3_socket = rockygroundshader_002.interface.new_socket(name = "Dirt Color 3", in_out='INPUT', socket_type = 'NodeSocketColor')
    dirt_color_3_socket.default_value = (0.01637599989771843, 0.012590999715030193, 0.00964600034058094, 1.0)
    dirt_color_3_socket.attribute_domain = 'POINT'
    roughness_socket = rockygroundshader_002.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = 'NONE'
    roughness_socket.attribute_domain = 'POINT'
    dirt_bump_strength_socket = rockygroundshader_002.interface.new_socket(name = "Dirt Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    dirt_bump_strength_socket.default_value = 0.15000000596046448
    dirt_bump_strength_socket.min_value = 0.0
    dirt_bump_strength_socket.max_value = 1.0
    dirt_bump_strength_socket.subtype = 'FACTOR'
    dirt_bump_strength_socket.attribute_domain = 'POINT'
    rock_bump_strength_socket = rockygroundshader_002.interface.new_socket(name = "Rock Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    rock_bump_strength_socket.default_value = 0.5
    rock_bump_strength_socket.min_value = 0.0
    rock_bump_strength_socket.max_value = 1.0
    rock_bump_strength_socket.subtype = 'FACTOR'
    rock_bump_strength_socket.attribute_domain = 'POINT'
    extra_bump_strength_socket = rockygroundshader_002.interface.new_socket(name = "Extra Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    extra_bump_strength_socket.default_value = 0.05999999865889549
    extra_bump_strength_socket.min_value = 0.0
    extra_bump_strength_socket.max_value = 1000.0
    extra_bump_strength_socket.subtype = 'NONE'
    extra_bump_strength_socket.attribute_domain = 'POINT'
    frame_001 = rockygroundshader_002.nodes.new("NodeFrame")
    frame_001.name = "Frame.001"
    frame_002 = rockygroundshader_002.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    frame_004 = rockygroundshader_002.nodes.new("NodeFrame")
    frame_004.name = "Frame.004"
    frame_003 = rockygroundshader_002.nodes.new("NodeFrame")
    frame_003.name = "Frame.003"
    frame_006 = rockygroundshader_002.nodes.new("NodeFrame")
    frame_006.name = "Frame.006"
    frame_005 = rockygroundshader_002.nodes.new("NodeFrame")
    frame_005.name = "Frame.005"
    frame_009 = rockygroundshader_002.nodes.new("NodeFrame")
    frame_009.name = "Frame.009"
    frame = rockygroundshader_002.nodes.new("NodeFrame")
    frame.name = "Frame"
    frame_008 = rockygroundshader_002.nodes.new("NodeFrame")
    frame_008.name = "Frame.008"
    group_output_1 = rockygroundshader_002.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True
    color_ramp = rockygroundshader_002.nodes.new("ShaderNodeValToRGB")
    color_ramp.name = "Color Ramp"
    color_ramp.color_ramp.color_mode = 'RGB'
    color_ramp.color_ramp.hue_interpolation = 'NEAR'
    color_ramp.color_ramp.interpolation = 'LINEAR'
    color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
    color_ramp_cre_0 = color_ramp.color_ramp.elements[0]
    color_ramp_cre_0.position = 0.06783919036388397
    color_ramp_cre_0.alpha = 1.0
    color_ramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_cre_1 = color_ramp.color_ramp.elements.new(1.0)
    color_ramp_cre_1.alpha = 1.0
    color_ramp_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    noise_texture = rockygroundshader_002.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    noise_texture.inputs[2].default_value = 0.30000001192092896
    noise_texture.inputs[3].default_value = 15.0
    noise_texture.inputs[4].default_value = 0.550000011920929
    noise_texture.inputs[5].default_value = 2.4000000953674316
    noise_texture.inputs[8].default_value = 0.0
    noise_texture_001 = rockygroundshader_002.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = '3D'
    noise_texture_001.noise_type = 'FBM'
    noise_texture_001.normalize = True
    noise_texture_001.inputs[2].default_value = 8.0
    noise_texture_001.inputs[3].default_value = 15.0
    noise_texture_001.inputs[4].default_value = 0.33000001311302185
    noise_texture_001.inputs[5].default_value = 2.4000000953674316
    noise_texture_001.inputs[8].default_value = 0.0
    color_ramp_001 = rockygroundshader_002.nodes.new("ShaderNodeValToRGB")
    color_ramp_001.name = "Color Ramp.001"
    color_ramp_001.color_ramp.color_mode = 'RGB'
    color_ramp_001.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_001.color_ramp.interpolation = 'LINEAR'
    color_ramp_001.color_ramp.elements.remove(color_ramp_001.color_ramp.elements[0])
    color_ramp_001_cre_0 = color_ramp_001.color_ramp.elements[0]
    color_ramp_001_cre_0.position = 0.4547737240791321
    color_ramp_001_cre_0.alpha = 1.0
    color_ramp_001_cre_0.color = (1.0, 1.0, 1.0, 1.0)
    color_ramp_001_cre_1 = color_ramp_001.color_ramp.elements.new(0.5804020762443542)
    color_ramp_001_cre_1.alpha = 1.0
    color_ramp_001_cre_1.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_003 = rockygroundshader_002.nodes.new("ShaderNodeValToRGB")
    color_ramp_003.name = "Color Ramp.003"
    color_ramp_003.color_ramp.color_mode = 'RGB'
    color_ramp_003.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_003.color_ramp.interpolation = 'LINEAR'
    color_ramp_003.color_ramp.elements.remove(color_ramp_003.color_ramp.elements[0])
    color_ramp_003_cre_0 = color_ramp_003.color_ramp.elements[0]
    color_ramp_003_cre_0.position = 0.4547737240791321
    color_ramp_003_cre_0.alpha = 1.0
    color_ramp_003_cre_0.color = (1.0, 1.0, 1.0, 1.0)
    color_ramp_003_cre_1 = color_ramp_003.color_ramp.elements.new(0.5804020762443542)
    color_ramp_003_cre_1.alpha = 1.0
    color_ramp_003_cre_1.color = (0.0, 0.0, 0.0, 1.0)
    noise_texture_002 = rockygroundshader_002.nodes.new("ShaderNodeTexNoise")
    noise_texture_002.name = "Noise Texture.002"
    noise_texture_002.noise_dimensions = '3D'
    noise_texture_002.noise_type = 'FBM'
    noise_texture_002.normalize = True
    noise_texture_002.inputs[2].default_value = 0.8999999761581421
    noise_texture_002.inputs[3].default_value = 15.0
    noise_texture_002.inputs[4].default_value = 0.550000011920929
    noise_texture_002.inputs[5].default_value = 2.4000000953674316
    noise_texture_002.inputs[8].default_value = 0.0
    mix_002 = rockygroundshader_002.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = 'LINEAR_LIGHT'
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = 'RGBA'
    mix_002.factor_mode = 'UNIFORM'
    mix_002.inputs[0].default_value = 0.30000001192092896
    noise_texture_003 = rockygroundshader_002.nodes.new("ShaderNodeTexNoise")
    noise_texture_003.name = "Noise Texture.003"
    noise_texture_003.noise_dimensions = '3D'
    noise_texture_003.noise_type = 'FBM'
    noise_texture_003.normalize = True
    noise_texture_003.inputs[2].default_value = 17.0
    noise_texture_003.inputs[3].default_value = 15.0
    noise_texture_003.inputs[4].default_value = 0.33000001311302185
    noise_texture_003.inputs[5].default_value = 2.4000000953674316
    noise_texture_003.inputs[8].default_value = 0.0
    color_ramp_002 = rockygroundshader_002.nodes.new("ShaderNodeValToRGB")
    color_ramp_002.name = "Color Ramp.002"
    color_ramp_002.color_ramp.color_mode = 'RGB'
    color_ramp_002.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_002.color_ramp.interpolation = 'LINEAR'
    color_ramp_002.color_ramp.elements.remove(color_ramp_002.color_ramp.elements[0])
    color_ramp_002_cre_0 = color_ramp_002.color_ramp.elements[0]
    color_ramp_002_cre_0.position = 0.19346728920936584
    color_ramp_002_cre_0.alpha = 1.0
    color_ramp_002_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_002_cre_1 = color_ramp_002.color_ramp.elements.new(0.5854271054267883)
    color_ramp_002_cre_1.alpha = 1.0
    color_ramp_002_cre_1.color = (0.17047399282455444, 0.17047399282455444, 0.17047399282455444, 1.0)
    mix_001 = rockygroundshader_002.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'MIX'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'RGBA'
    mix_001.factor_mode = 'UNIFORM'
    mix_001.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)
    mix_003 = rockygroundshader_002.nodes.new("ShaderNodeMix")
    mix_003.name = "Mix.003"
    mix_003.blend_type = 'MIX'
    mix_003.clamp_factor = True
    mix_003.clamp_result = False
    mix_003.data_type = 'RGBA'
    mix_003.factor_mode = 'UNIFORM'
    mix_003.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)
    noise_texture_005 = rockygroundshader_002.nodes.new("ShaderNodeTexNoise")
    noise_texture_005.name = "Noise Texture.005"
    noise_texture_005.noise_dimensions = '3D'
    noise_texture_005.noise_type = 'FBM'
    noise_texture_005.normalize = True
    noise_texture_005.inputs[2].default_value = 13.0
    noise_texture_005.inputs[3].default_value = 15.0
    noise_texture_005.inputs[4].default_value = 0.699999988079071
    noise_texture_005.inputs[5].default_value = 2.0
    noise_texture_005.inputs[8].default_value = 0.0
    noise_texture_004 = rockygroundshader_002.nodes.new("ShaderNodeTexNoise")
    noise_texture_004.name = "Noise Texture.004"
    noise_texture_004.noise_dimensions = '3D'
    noise_texture_004.noise_type = 'FBM'
    noise_texture_004.normalize = True
    noise_texture_004.inputs[2].default_value = 8.699999809265137
    noise_texture_004.inputs[3].default_value = 15.0
    noise_texture_004.inputs[4].default_value = 0.6200000047683716
    noise_texture_004.inputs[5].default_value = 3.5999999046325684
    noise_texture_004.inputs[8].default_value = 0.0
    color_ramp_004 = rockygroundshader_002.nodes.new("ShaderNodeValToRGB")
    color_ramp_004.name = "Color Ramp.004"
    color_ramp_004.color_ramp.color_mode = 'RGB'
    color_ramp_004.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_004.color_ramp.interpolation = 'LINEAR'
    color_ramp_004.color_ramp.elements.remove(color_ramp_004.color_ramp.elements[0])
    color_ramp_004_cre_0 = color_ramp_004.color_ramp.elements[0]
    color_ramp_004_cre_0.position = 0.31407034397125244
    color_ramp_004_cre_0.alpha = 1.0
    color_ramp_004_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_004_cre_1 = color_ramp_004.color_ramp.elements.new(0.6834171414375305)
    color_ramp_004_cre_1.alpha = 1.0
    color_ramp_004_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    color_ramp_005 = rockygroundshader_002.nodes.new("ShaderNodeValToRGB")
    color_ramp_005.name = "Color Ramp.005"
    color_ramp_005.color_ramp.color_mode = 'RGB'
    color_ramp_005.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_005.color_ramp.interpolation = 'LINEAR'
    color_ramp_005.color_ramp.elements.remove(color_ramp_005.color_ramp.elements[0])
    color_ramp_005_cre_0 = color_ramp_005.color_ramp.elements[0]
    color_ramp_005_cre_0.position = 0.0
    color_ramp_005_cre_0.alpha = 1.0
    color_ramp_005_cre_0.color = (0.10046599805355072, 0.10046599805355072, 0.10046599805355072, 1.0)
    color_ramp_005_cre_1 = color_ramp_005.color_ramp.elements.new(0.497487336397171)
    color_ramp_005_cre_1.alpha = 1.0
    color_ramp_005_cre_1.color = (0.031199999153614044, 0.031199999153614044, 0.031199999153614044, 1.0)
    color_ramp_005_cre_2 = color_ramp_005.color_ramp.elements.new(1.0)
    color_ramp_005_cre_2.alpha = 1.0
    color_ramp_005_cre_2.color = (0.4479770064353943, 0.4479770064353943, 0.4479770064353943, 1.0)
    voronoi_texture_002 = rockygroundshader_002.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_002.name = "Voronoi Texture.002"
    voronoi_texture_002.distance = 'EUCLIDEAN'
    voronoi_texture_002.feature = 'SMOOTH_F1'
    voronoi_texture_002.normalize = False
    voronoi_texture_002.voronoi_dimensions = '3D'
    voronoi_texture_002.inputs[2].default_value = 5.0
    voronoi_texture_002.inputs[3].default_value = 15.0
    voronoi_texture_002.inputs[4].default_value = 0.5
    voronoi_texture_002.inputs[5].default_value = 6.400000095367432
    voronoi_texture_002.inputs[6].default_value = 1.0
    voronoi_texture_002.inputs[8].default_value = 1.0
    mix_008 = rockygroundshader_002.nodes.new("ShaderNodeMix")
    mix_008.name = "Mix.008"
    mix_008.blend_type = 'MIX'
    mix_008.clamp_factor = True
    mix_008.clamp_result = False
    mix_008.data_type = 'RGBA'
    mix_008.factor_mode = 'UNIFORM'
    noise_texture_007 = rockygroundshader_002.nodes.new("ShaderNodeTexNoise")
    noise_texture_007.name = "Noise Texture.007"
    noise_texture_007.noise_dimensions = '3D'
    noise_texture_007.noise_type = 'FBM'
    noise_texture_007.normalize = True
    noise_texture_007.inputs[2].default_value = 35.0
    noise_texture_007.inputs[3].default_value = 15.0
    noise_texture_007.inputs[4].default_value = 0.699999988079071
    noise_texture_007.inputs[5].default_value = 2.0
    noise_texture_007.inputs[8].default_value = 0.0
    color_ramp_006 = rockygroundshader_002.nodes.new("ShaderNodeValToRGB")
    color_ramp_006.name = "Color Ramp.006"
    color_ramp_006.color_ramp.color_mode = 'RGB'
    color_ramp_006.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_006.color_ramp.interpolation = 'LINEAR'
    color_ramp_006.color_ramp.elements.remove(color_ramp_006.color_ramp.elements[0])
    color_ramp_006_cre_0 = color_ramp_006.color_ramp.elements[0]
    color_ramp_006_cre_0.position = 0.359296590089798
    color_ramp_006_cre_0.alpha = 1.0
    color_ramp_006_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_006_cre_1 = color_ramp_006.color_ramp.elements.new(0.7638190984725952)
    color_ramp_006_cre_1.alpha = 1.0
    color_ramp_006_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    color_ramp_007 = rockygroundshader_002.nodes.new("ShaderNodeValToRGB")
    color_ramp_007.name = "Color Ramp.007"
    color_ramp_007.color_ramp.color_mode = 'RGB'
    color_ramp_007.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_007.color_ramp.interpolation = 'LINEAR'
    color_ramp_007.color_ramp.elements.remove(color_ramp_007.color_ramp.elements[0])
    color_ramp_007_cre_0 = color_ramp_007.color_ramp.elements[0]
    color_ramp_007_cre_0.position = 0.0
    color_ramp_007_cre_0.alpha = 1.0
    color_ramp_007_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_007_cre_1 = color_ramp_007.color_ramp.elements.new(0.06281421333551407)
    color_ramp_007_cre_1.alpha = 1.0
    color_ramp_007_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    mix_009 = rockygroundshader_002.nodes.new("ShaderNodeMix")
    mix_009.name = "Mix.009"
    mix_009.blend_type = 'LIGHTEN'
    mix_009.clamp_factor = True
    mix_009.clamp_result = False
    mix_009.data_type = 'RGBA'
    mix_009.factor_mode = 'UNIFORM'
    mix_009.inputs[0].default_value = 0.15000000596046448
    math_1 = rockygroundshader_002.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = 'ADD'
    math_1.use_clamp = False
    math_1.inputs[1].default_value = 0.5
    principled_bsdf = rockygroundshader_002.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    principled_bsdf.inputs[1].default_value = 0.0
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
    noise_texture_006 = rockygroundshader_002.nodes.new("ShaderNodeTexNoise")
    noise_texture_006.name = "Noise Texture.006"
    noise_texture_006.noise_dimensions = '3D'
    noise_texture_006.noise_type = 'FBM'
    noise_texture_006.normalize = True
    noise_texture_006.inputs[2].default_value = 18.0
    noise_texture_006.inputs[3].default_value = 15.0
    noise_texture_006.inputs[5].default_value = 2.0
    noise_texture_006.inputs[8].default_value = 0.0
    texture_coordinate = rockygroundshader_002.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False
    mapping = rockygroundshader_002.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = 'POINT'
    mapping.inputs[2].default_value = (0.0, 0.0, 0.0)
    mix_004 = rockygroundshader_002.nodes.new("ShaderNodeMix")
    mix_004.name = "Mix.004"
    mix_004.blend_type = 'LIGHTEN'
    mix_004.clamp_factor = True
    mix_004.clamp_result = False
    mix_004.data_type = 'RGBA'
    mix_004.factor_mode = 'UNIFORM'
    mix_004.inputs[0].default_value = 1.0
    hue_saturation_value_001 = rockygroundshader_002.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_001.name = "Hue/Saturation/Value.001"
    hue_saturation_value_001.inputs[0].default_value = 0.5
    hue_saturation_value_001.inputs[1].default_value = 1.0
    hue_saturation_value_001.inputs[3].default_value = 1.0
    hue_saturation_value_002 = rockygroundshader_002.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_002.name = "Hue/Saturation/Value.002"
    hue_saturation_value_002.inputs[0].default_value = 0.5
    hue_saturation_value_002.inputs[1].default_value = 1.0
    hue_saturation_value_002.inputs[3].default_value = 1.0
    mix_007 = rockygroundshader_002.nodes.new("ShaderNodeMix")
    mix_007.name = "Mix.007"
    mix_007.blend_type = 'MIX'
    mix_007.clamp_factor = True
    mix_007.clamp_result = False
    mix_007.data_type = 'RGBA'
    mix_007.factor_mode = 'UNIFORM'
    mix = rockygroundshader_002.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'LINEAR_LIGHT'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'
    voronoi_texture = rockygroundshader_002.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = 'EUCLIDEAN'
    voronoi_texture.feature = 'DISTANCE_TO_EDGE'
    voronoi_texture.normalize = False
    voronoi_texture.voronoi_dimensions = '3D'
    voronoi_texture.inputs[3].default_value = 0.0
    voronoi_texture.inputs[4].default_value = 0.5
    voronoi_texture.inputs[5].default_value = 2.0
    voronoi_texture.inputs[8].default_value = 1.0
    voronoi_texture_001 = rockygroundshader_002.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001.name = "Voronoi Texture.001"
    voronoi_texture_001.distance = 'EUCLIDEAN'
    voronoi_texture_001.feature = 'DISTANCE_TO_EDGE'
    voronoi_texture_001.normalize = False
    voronoi_texture_001.voronoi_dimensions = '3D'
    voronoi_texture_001.inputs[3].default_value = 0.0
    voronoi_texture_001.inputs[4].default_value = 0.5
    voronoi_texture_001.inputs[5].default_value = 2.0
    voronoi_texture_001.inputs[8].default_value = 1.0
    mix_005 = rockygroundshader_002.nodes.new("ShaderNodeMix")
    mix_005.name = "Mix.005"
    mix_005.blend_type = 'MIX'
    mix_005.clamp_factor = True
    mix_005.clamp_result = False
    mix_005.data_type = 'RGBA'
    mix_005.factor_mode = 'UNIFORM'
    mix_006 = rockygroundshader_002.nodes.new("ShaderNodeMix")
    mix_006.name = "Mix.006"
    mix_006.blend_type = 'MIX'
    mix_006.clamp_factor = True
    mix_006.clamp_result = False
    mix_006.data_type = 'RGBA'
    mix_006.factor_mode = 'UNIFORM'
    color_ramp_008 = rockygroundshader_002.nodes.new("ShaderNodeValToRGB")
    color_ramp_008.name = "Color Ramp.008"
    color_ramp_008.color_ramp.color_mode = 'RGB'
    color_ramp_008.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_008.color_ramp.interpolation = 'LINEAR'
    color_ramp_008.color_ramp.elements.remove(color_ramp_008.color_ramp.elements[0])
    color_ramp_008_cre_0 = color_ramp_008.color_ramp.elements[0]
    color_ramp_008_cre_0.position = 0.0
    color_ramp_008_cre_0.alpha = 1.0
    color_ramp_008_cre_0.color = (0.7721049785614014, 0.7721049785614014, 0.7721049785614014, 1.0)
    color_ramp_008_cre_1 = color_ramp_008.color_ramp.elements.new(0.1356785148382187)
    color_ramp_008_cre_1.alpha = 1.0
    color_ramp_008_cre_1.color = (0.6128469705581665, 0.6128469705581665, 0.6128469705581665, 1.0)
    hue_saturation_value = rockygroundshader_002.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    hue_saturation_value.inputs[0].default_value = 0.5
    hue_saturation_value.inputs[1].default_value = 1.0
    hue_saturation_value.inputs[3].default_value = 1.0
    bump = rockygroundshader_002.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    bump.inputs[1].default_value = 1.0
    bump_002 = rockygroundshader_002.nodes.new("ShaderNodeBump")
    bump_002.name = "Bump.002"
    bump_002.invert = False
    bump_002.inputs[1].default_value = 1.0
    bump_001 = rockygroundshader_002.nodes.new("ShaderNodeBump")
    bump_001.name = "Bump.001"
    bump_001.invert = False
    bump_001.inputs[1].default_value = 1.0
    group_input_1 = rockygroundshader_002.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"
    clamp = rockygroundshader_002.nodes.new("ShaderNodeClamp")
    clamp.name = "Clamp"
    clamp.hide = True
    clamp.clamp_type = 'MINMAX'
    clamp.inputs[1].default_value = 0.0
    clamp.inputs[2].default_value = 1.0
    bump_003 = rockygroundshader_002.nodes.new("ShaderNodeBump")
    bump_003.name = "Bump.003"
    bump_003.invert = False
    bump_003.inputs[1].default_value = 1.0
    bump_003.inputs[3].default_value = (0.0, 0.0, 0.0)
    group_001 = rockygroundshader_002.nodes.new("ShaderNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = random_x4___mat_005
    group_001.inputs[0].default_value = 0.5231512188911438
    map_range_004 = rockygroundshader_002.nodes.new("ShaderNodeMapRange")
    map_range_004.name = "Map Range.004"
    map_range_004.clamp = True
    map_range_004.data_type = 'FLOAT'
    map_range_004.interpolation_type = 'LINEAR'
    map_range_004.inputs[1].default_value = 0.0
    map_range_004.inputs[2].default_value = 1.0
    map_range_004.inputs[3].default_value = -1000.0
    map_range_004.inputs[4].default_value = 1000.0
    rockygroundshader_002.links.new(color_ramp_002.outputs[0], mix_003.inputs[6])
    rockygroundshader_002.links.new(mapping.outputs[0], mix_002.inputs[6])
    rockygroundshader_002.links.new(hue_saturation_value_001.outputs[0], mix_004.inputs[7])
    rockygroundshader_002.links.new(hue_saturation_value_002.outputs[0], mix_004.inputs[6])
    rockygroundshader_002.links.new(mapping.outputs[0], noise_texture_004.inputs[0])
    rockygroundshader_002.links.new(noise_texture_004.outputs[0], color_ramp_004.inputs[0])
    rockygroundshader_002.links.new(mix_004.outputs[2], color_ramp_007.inputs[0])
    rockygroundshader_002.links.new(color_ramp_004.outputs[0], mix_005.inputs[0])
    rockygroundshader_002.links.new(mapping.outputs[0], voronoi_texture_002.inputs[0])
    rockygroundshader_002.links.new(mix_004.outputs[2], bump_001.inputs[2])
    rockygroundshader_002.links.new(voronoi_texture_002.outputs[0], color_ramp_005.inputs[0])
    rockygroundshader_002.links.new(mapping.outputs[0], noise_texture_002.inputs[0])
    rockygroundshader_002.links.new(color_ramp_005.outputs[0], mix_006.inputs[0])
    rockygroundshader_002.links.new(mapping.outputs[0], noise_texture_001.inputs[0])
    rockygroundshader_002.links.new(mix_005.outputs[2], mix_006.inputs[6])
    rockygroundshader_002.links.new(mapping.outputs[0], noise_texture_005.inputs[0])
    rockygroundshader_002.links.new(noise_texture_005.outputs[0], mix_007.inputs[0])
    rockygroundshader_002.links.new(mapping.outputs[0], noise_texture_003.inputs[0])
    rockygroundshader_002.links.new(mapping.outputs[0], noise_texture_006.inputs[0])
    rockygroundshader_002.links.new(mapping.outputs[0], noise_texture_007.inputs[0])
    rockygroundshader_002.links.new(mix.outputs[2], voronoi_texture.inputs[0])
    rockygroundshader_002.links.new(bump_001.outputs[0], bump_002.inputs[3])
    rockygroundshader_002.links.new(mix_004.outputs[2], mix_009.inputs[6])
    rockygroundshader_002.links.new(noise_texture_007.outputs[0], color_ramp_006.inputs[0])
    rockygroundshader_002.links.new(texture_coordinate.outputs[3], mapping.inputs[0])
    rockygroundshader_002.links.new(color_ramp_007.outputs[0], mix_008.inputs[0])
    rockygroundshader_002.links.new(bump.outputs[0], bump_001.inputs[3])
    rockygroundshader_002.links.new(mix_007.outputs[2], mix_008.inputs[7])
    rockygroundshader_002.links.new(noise_texture.outputs[1], mix.inputs[7])
    rockygroundshader_002.links.new(voronoi_texture_001.outputs[0], color_ramp_002.inputs[0])
    rockygroundshader_002.links.new(voronoi_texture.outputs[0], color_ramp.inputs[0])
    rockygroundshader_002.links.new(noise_texture_006.outputs[0], mix_009.inputs[7])
    rockygroundshader_002.links.new(mix_008.outputs[2], principled_bsdf.inputs[0])
    rockygroundshader_002.links.new(mapping.outputs[0], noise_texture.inputs[0])
    rockygroundshader_002.links.new(noise_texture_006.outputs[0], bump_002.inputs[2])
    rockygroundshader_002.links.new(noise_texture_001.outputs[0], color_ramp_001.inputs[0])
    rockygroundshader_002.links.new(color_ramp_001.outputs[0], mix_001.inputs[0])
    rockygroundshader_002.links.new(color_ramp.outputs[0], mix_001.inputs[6])
    rockygroundshader_002.links.new(mix_009.outputs[2], math_1.inputs[0])
    rockygroundshader_002.links.new(mapping.outputs[0], mix.inputs[6])
    rockygroundshader_002.links.new(hue_saturation_value.outputs[0], principled_bsdf.inputs[2])
    rockygroundshader_002.links.new(noise_texture_002.outputs[1], mix_002.inputs[7])
    rockygroundshader_002.links.new(bump_002.outputs[0], principled_bsdf.inputs[5])
    rockygroundshader_002.links.new(color_ramp_008.outputs[0], hue_saturation_value.inputs[4])
    rockygroundshader_002.links.new(color_ramp_007.outputs[0], color_ramp_008.inputs[0])
    rockygroundshader_002.links.new(mix_006.outputs[2], bump.inputs[2])
    rockygroundshader_002.links.new(mix_002.outputs[2], voronoi_texture_001.inputs[0])
    rockygroundshader_002.links.new(noise_texture_003.outputs[0], color_ramp_003.inputs[0])
    rockygroundshader_002.links.new(color_ramp_003.outputs[0], mix_003.inputs[0])
    rockygroundshader_002.links.new(mix_006.outputs[2], mix_008.inputs[6])
    rockygroundshader_002.links.new(principled_bsdf.outputs[0], group_output_1.inputs[0])
    rockygroundshader_002.links.new(group_input_1.outputs[0], mapping.inputs[3])
    rockygroundshader_002.links.new(mix_003.outputs[2], hue_saturation_value_001.inputs[4])
    rockygroundshader_002.links.new(mix_001.outputs[2], hue_saturation_value_002.inputs[4])
    rockygroundshader_002.links.new(group_input_1.outputs[1], hue_saturation_value_002.inputs[2])
    rockygroundshader_002.links.new(group_input_1.outputs[1], hue_saturation_value_001.inputs[2])
    rockygroundshader_002.links.new(group_input_1.outputs[2], mix_007.inputs[6])
    rockygroundshader_002.links.new(group_input_1.outputs[3], mix_007.inputs[7])
    rockygroundshader_002.links.new(group_input_1.outputs[4], mix.inputs[0])
    rockygroundshader_002.links.new(group_input_1.outputs[5], voronoi_texture.inputs[2])
    rockygroundshader_002.links.new(group_input_1.outputs[6], voronoi_texture_001.inputs[2])
    rockygroundshader_002.links.new(group_input_1.outputs[7], mix_005.inputs[6])
    rockygroundshader_002.links.new(group_input_1.outputs[8], mix_005.inputs[7])
    rockygroundshader_002.links.new(group_input_1.outputs[9], mix_006.inputs[7])
    rockygroundshader_002.links.new(group_input_1.outputs[10], hue_saturation_value.inputs[2])
    rockygroundshader_002.links.new(group_input_1.outputs[11], bump.inputs[0])
    rockygroundshader_002.links.new(group_input_1.outputs[11], bump_002.inputs[0])
    rockygroundshader_002.links.new(group_input_1.outputs[12], bump_001.inputs[0])
    rockygroundshader_002.links.new(color_ramp_006.outputs[0], clamp.inputs[0])
    rockygroundshader_002.links.new(clamp.outputs[0], noise_texture_006.inputs[4])
    rockygroundshader_002.links.new(group_input_1.outputs[13], bump_003.inputs[0])
    rockygroundshader_002.links.new(math_1.outputs[0], bump_003.inputs[2])
    rockygroundshader_002.links.new(bump_003.outputs[0], bump.inputs[3])
    rockygroundshader_002.links.new(group_001.outputs[0], map_range_004.inputs[0])
    rockygroundshader_002.links.new(map_range_004.outputs[0], mapping.inputs[1])
    return rockygroundshader_002

rockygroundshader_002 = rockygroundshader_002_node_group()

def lunarsurfaceshader_node_group():
    lunarsurfaceshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "LunarSurfaceShader")
    lunarsurfaceshader.color_tag = 'NONE'
    lunarsurfaceshader.default_group_node_width = 140
    bsdf_socket = lunarsurfaceshader.interface.new_socket(name = "BSDF", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    bsdf_socket.attribute_domain = 'POINT'
    scale_socket_1 = lunarsurfaceshader.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket_1.default_value = 1.0
    scale_socket_1.min_value = 0.0
    scale_socket_1.max_value = 3.4028234663852886e+38
    scale_socket_1.subtype = 'DISTANCE'
    scale_socket_1.attribute_domain = 'POINT'
    texture_scale_1_socket = lunarsurfaceshader.interface.new_socket(name = "Texture Scale 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    texture_scale_1_socket.default_value = 5.0
    texture_scale_1_socket.min_value = -1000.0
    texture_scale_1_socket.max_value = 1000.0
    texture_scale_1_socket.subtype = 'NONE'
    texture_scale_1_socket.attribute_domain = 'POINT'
    texture_scale_2_socket = lunarsurfaceshader.interface.new_socket(name = "Texture Scale 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    texture_scale_2_socket.default_value = 6.0
    texture_scale_2_socket.min_value = -1000.0
    texture_scale_2_socket.max_value = 1000.0
    texture_scale_2_socket.subtype = 'NONE'
    texture_scale_2_socket.attribute_domain = 'POINT'
    color_1_socket = lunarsurfaceshader.interface.new_socket(name = "Color 1", in_out='INPUT', socket_type = 'NodeSocketColor')
    color_1_socket.default_value = (0.1532880961894989, 0.1532880961894989, 0.1532880961894989, 1.0)
    color_1_socket.attribute_domain = 'POINT'
    color_2_socket = lunarsurfaceshader.interface.new_socket(name = "Color 2", in_out='INPUT', socket_type = 'NodeSocketColor')
    color_2_socket.default_value = (0.02125433087348938, 0.02125433087348938, 0.02125433087348938, 1.0)
    color_2_socket.attribute_domain = 'POINT'
    color_brightness_socket = lunarsurfaceshader.interface.new_socket(name = "Color Brightness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    color_brightness_socket.default_value = 1.0
    color_brightness_socket.min_value = 0.0
    color_brightness_socket.max_value = 2.0
    color_brightness_socket.subtype = 'NONE'
    color_brightness_socket.attribute_domain = 'POINT'
    distortion_socket = lunarsurfaceshader.interface.new_socket(name = "Distortion", in_out='INPUT', socket_type = 'NodeSocketFloat')
    distortion_socket.default_value = 0.17000000178813934
    distortion_socket.min_value = 0.0
    distortion_socket.max_value = 1.0
    distortion_socket.subtype = 'FACTOR'
    distortion_socket.attribute_domain = 'POINT'
    detail_1_socket = lunarsurfaceshader.interface.new_socket(name = "Detail 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detail_1_socket.default_value = 15.0
    detail_1_socket.min_value = 0.0
    detail_1_socket.max_value = 15.0
    detail_1_socket.subtype = 'NONE'
    detail_1_socket.attribute_domain = 'POINT'
    detail_2_socket = lunarsurfaceshader.interface.new_socket(name = "Detail 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detail_2_socket.default_value = 0.5
    detail_2_socket.min_value = 0.0
    detail_2_socket.max_value = 1.0
    detail_2_socket.subtype = 'FACTOR'
    detail_2_socket.attribute_domain = 'POINT'
    _detail_3_socket = lunarsurfaceshader.interface.new_socket(name = " Detail 3", in_out='INPUT', socket_type = 'NodeSocketFloat')
    _detail_3_socket.default_value = 0.0
    _detail_3_socket.min_value = 0.0
    _detail_3_socket.max_value = 15.0
    _detail_3_socket.subtype = 'NONE'
    _detail_3_socket.attribute_domain = 'POINT'
    hills_height_socket = lunarsurfaceshader.interface.new_socket(name = "Hills Height", in_out='INPUT', socket_type = 'NodeSocketFloat')
    hills_height_socket.default_value = 1.0
    hills_height_socket.min_value = 0.0
    hills_height_socket.max_value = 2.0
    hills_height_socket.subtype = 'NONE'
    hills_height_socket.attribute_domain = 'POINT'
    roughness_socket_1 = lunarsurfaceshader.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket_1.default_value = 1.0
    roughness_socket_1.min_value = 0.0
    roughness_socket_1.max_value = 2.0
    roughness_socket_1.subtype = 'NONE'
    roughness_socket_1.attribute_domain = 'POINT'
    bump_strength_1_socket = lunarsurfaceshader.interface.new_socket(name = "Bump Strength 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    bump_strength_1_socket.default_value = 0.10000000149011612
    bump_strength_1_socket.min_value = 0.0
    bump_strength_1_socket.max_value = 1.0
    bump_strength_1_socket.subtype = 'FACTOR'
    bump_strength_1_socket.attribute_domain = 'POINT'
    bump_strength_2_socket = lunarsurfaceshader.interface.new_socket(name = "Bump Strength 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    bump_strength_2_socket.default_value = 0.10000000149011612
    bump_strength_2_socket.min_value = 0.0
    bump_strength_2_socket.max_value = 1.0
    bump_strength_2_socket.subtype = 'FACTOR'
    bump_strength_2_socket.attribute_domain = 'POINT'
    bump_strength_3_socket = lunarsurfaceshader.interface.new_socket(name = "Bump Strength 3", in_out='INPUT', socket_type = 'NodeSocketFloat')
    bump_strength_3_socket.default_value = 0.10000000149011612
    bump_strength_3_socket.min_value = 0.0
    bump_strength_3_socket.max_value = 1.0
    bump_strength_3_socket.subtype = 'FACTOR'
    bump_strength_3_socket.attribute_domain = 'POINT'
    group_output_2 = lunarsurfaceshader.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True
    group_input_2 = lunarsurfaceshader.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"
    principled_bsdf_1 = lunarsurfaceshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_1.name = "Principled BSDF"
    principled_bsdf_1.distribution = 'MULTI_GGX'
    principled_bsdf_1.subsurface_method = 'RANDOM_WALK'
    principled_bsdf_1.inputs[1].default_value = 0.0
    principled_bsdf_1.inputs[3].default_value = 1.5
    principled_bsdf_1.inputs[4].default_value = 1.0
    principled_bsdf_1.inputs[7].default_value = 0.0
    principled_bsdf_1.inputs[8].default_value = 0.0
    principled_bsdf_1.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    principled_bsdf_1.inputs[10].default_value = 0.05000000074505806
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
    principled_bsdf_1.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_1.inputs[28].default_value = 0.0
    principled_bsdf_1.inputs[29].default_value = 0.0
    principled_bsdf_1.inputs[30].default_value = 1.3300000429153442
    noise_texture_1 = lunarsurfaceshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_1.name = "Noise Texture"
    noise_texture_1.noise_dimensions = '4D'
    noise_texture_1.noise_type = 'FBM'
    noise_texture_1.normalize = True
    noise_texture_1.inputs[1].default_value = 0.0
    noise_texture_1.inputs[2].default_value = 23.0
    noise_texture_1.inputs[3].default_value = 15.0
    noise_texture_1.inputs[4].default_value = 0.6000000238418579
    noise_texture_1.inputs[5].default_value = 2.0
    noise_texture_1.inputs[8].default_value = 0.0
    mapping_1 = lunarsurfaceshader.nodes.new("ShaderNodeMapping")
    mapping_1.name = "Mapping"
    mapping_1.vector_type = 'POINT'
    mapping_1.inputs[2].default_value = (0.0, 0.0, 0.0)
    texture_coordinate_1 = lunarsurfaceshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_1.name = "Texture Coordinate"
    texture_coordinate_1.from_instancer = False
    texture_coordinate_1.outputs[0].hide = True
    texture_coordinate_1.outputs[1].hide = True
    texture_coordinate_1.outputs[2].hide = True
    texture_coordinate_1.outputs[4].hide = True
    texture_coordinate_1.outputs[5].hide = True
    texture_coordinate_1.outputs[6].hide = True
    hue_saturation_value_1 = lunarsurfaceshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_1.name = "Hue/Saturation/Value"
    hue_saturation_value_1.inputs[0].default_value = 0.5
    hue_saturation_value_1.inputs[1].default_value = 1.0
    hue_saturation_value_1.inputs[3].default_value = 1.0
    noise_texture_001_1 = lunarsurfaceshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_001_1.name = "Noise Texture.001"
    noise_texture_001_1.noise_dimensions = '4D'
    noise_texture_001_1.noise_type = 'FBM'
    noise_texture_001_1.normalize = True
    noise_texture_001_1.inputs[1].default_value = 0.0
    noise_texture_001_1.inputs[5].default_value = 2.0
    noise_texture_001_1.inputs[8].default_value = 0.0
    voronoi_texture_1 = lunarsurfaceshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_1.name = "Voronoi Texture"
    voronoi_texture_1.distance = 'EUCLIDEAN'
    voronoi_texture_1.feature = 'F1'
    voronoi_texture_1.normalize = True
    voronoi_texture_1.voronoi_dimensions = '4D'
    voronoi_texture_1.inputs[1].default_value = 0.0
    voronoi_texture_1.inputs[4].default_value = 0.5
    voronoi_texture_1.inputs[5].default_value = 2.0
    voronoi_texture_1.inputs[8].default_value = 1.0
    mix_1 = lunarsurfaceshader.nodes.new("ShaderNodeMix")
    mix_1.name = "Mix"
    mix_1.blend_type = 'LINEAR_LIGHT'
    mix_1.clamp_factor = True
    mix_1.clamp_result = False
    mix_1.data_type = 'RGBA'
    mix_1.factor_mode = 'UNIFORM'
    hue_saturation_value_001_1 = lunarsurfaceshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_001_1.name = "Hue/Saturation/Value.001"
    hue_saturation_value_001_1.inputs[0].default_value = 0.5
    hue_saturation_value_001_1.inputs[1].default_value = 1.0
    hue_saturation_value_001_1.inputs[3].default_value = 1.0
    color_ramp_1 = lunarsurfaceshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_1.name = "Color Ramp"
    color_ramp_1.color_ramp.color_mode = 'RGB'
    color_ramp_1.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_1.color_ramp.interpolation = 'LINEAR'
    color_ramp_1.color_ramp.elements.remove(color_ramp_1.color_ramp.elements[0])
    color_ramp_1_cre_0 = color_ramp_1.color_ramp.elements[0]
    color_ramp_1_cre_0.position = 0.0
    color_ramp_1_cre_0.alpha = 1.0
    color_ramp_1_cre_0.color = (0.22696438431739807, 0.22696606814861298, 0.2269659787416458, 1.0)
    color_ramp_1_cre_1 = color_ramp_1.color_ramp.elements.new(1.0)
    color_ramp_1_cre_1.alpha = 1.0
    color_ramp_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    mix_001_1 = lunarsurfaceshader.nodes.new("ShaderNodeMix")
    mix_001_1.name = "Mix.001"
    mix_001_1.blend_type = 'LINEAR_LIGHT'
    mix_001_1.clamp_factor = True
    mix_001_1.clamp_result = False
    mix_001_1.data_type = 'RGBA'
    mix_001_1.factor_mode = 'UNIFORM'
    mix_001_1.inputs[0].default_value = 0.12700000405311584
    mix_002_1 = lunarsurfaceshader.nodes.new("ShaderNodeMix")
    mix_002_1.name = "Mix.002"
    mix_002_1.blend_type = 'MIX'
    mix_002_1.clamp_factor = True
    mix_002_1.clamp_result = False
    mix_002_1.data_type = 'RGBA'
    mix_002_1.factor_mode = 'UNIFORM'
    color_ramp_001_1 = lunarsurfaceshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_001_1.name = "Color Ramp.001"
    color_ramp_001_1.color_ramp.color_mode = 'RGB'
    color_ramp_001_1.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_001_1.color_ramp.interpolation = 'LINEAR'
    color_ramp_001_1.color_ramp.elements.remove(color_ramp_001_1.color_ramp.elements[0])
    color_ramp_001_1_cre_0 = color_ramp_001_1.color_ramp.elements[0]
    color_ramp_001_1_cre_0.position = 0.0
    color_ramp_001_1_cre_0.alpha = 1.0
    color_ramp_001_1_cre_0.color = (0.8126243352890015, 0.8126243352890015, 0.8126243352890015, 1.0)
    color_ramp_001_1_cre_1 = color_ramp_001_1.color_ramp.elements.new(1.0)
    color_ramp_001_1_cre_1.alpha = 1.0
    color_ramp_001_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    hue_saturation_value_002_1 = lunarsurfaceshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_002_1.name = "Hue/Saturation/Value.002"
    hue_saturation_value_002_1.inputs[0].default_value = 0.5
    hue_saturation_value_002_1.inputs[1].default_value = 1.0
    hue_saturation_value_002_1.inputs[3].default_value = 1.0
    map_range = lunarsurfaceshader.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = False
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    map_range.inputs[1].default_value = 0.20000000298023224
    map_range.inputs[2].default_value = 0.6299999952316284
    map_range.inputs[3].default_value = 0.0
    map_range.inputs[4].default_value = 1.0
    bump_1 = lunarsurfaceshader.nodes.new("ShaderNodeBump")
    bump_1.name = "Bump"
    bump_1.invert = False
    bump_1.inputs[1].default_value = 1.0
    bump_1.inputs[3].default_value = (0.0, 0.0, 0.0)
    bump_001_1 = lunarsurfaceshader.nodes.new("ShaderNodeBump")
    bump_001_1.name = "Bump.001"
    bump_001_1.invert = False
    bump_001_1.inputs[1].default_value = 1.0
    bump_002_1 = lunarsurfaceshader.nodes.new("ShaderNodeBump")
    bump_002_1.name = "Bump.002"
    bump_002_1.invert = False
    bump_002_1.inputs[1].default_value = 1.0
    group_001_1 = lunarsurfaceshader.nodes.new("ShaderNodeGroup")
    group_001_1.name = "Group.001"
    group_001_1.node_tree = random_x4___mat_005
    group_001_1.inputs[0].default_value = 0.6134099960327148
    map_range_004_1 = lunarsurfaceshader.nodes.new("ShaderNodeMapRange")
    map_range_004_1.name = "Map Range.004"
    map_range_004_1.clamp = True
    map_range_004_1.data_type = 'FLOAT'
    map_range_004_1.interpolation_type = 'LINEAR'
    map_range_004_1.inputs[1].default_value = 0.0
    map_range_004_1.inputs[2].default_value = 1.0
    map_range_004_1.inputs[3].default_value = -1000.0
    map_range_004_1.inputs[4].default_value = 1000.0
    lunarsurfaceshader.links.new(mix_002_1.outputs[2], principled_bsdf_1.inputs[0])
    lunarsurfaceshader.links.new(map_range.outputs[0], mix_002_1.inputs[0])
    lunarsurfaceshader.links.new(bump_1.outputs[0], bump_001_1.inputs[3])
    lunarsurfaceshader.links.new(noise_texture_1.outputs[0], hue_saturation_value_1.inputs[4])
    lunarsurfaceshader.links.new(texture_coordinate_1.outputs[3], mapping_1.inputs[0])
    lunarsurfaceshader.links.new(bump_001_1.outputs[0], bump_002_1.inputs[3])
    lunarsurfaceshader.links.new(mapping_1.outputs[0], noise_texture_001_1.inputs[0])
    lunarsurfaceshader.links.new(mix_001_1.outputs[2], map_range.inputs[0])
    lunarsurfaceshader.links.new(color_ramp_1.outputs[0], bump_1.inputs[2])
    lunarsurfaceshader.links.new(hue_saturation_value_1.outputs[0], mix_001_1.inputs[7])
    lunarsurfaceshader.links.new(hue_saturation_value_002_1.outputs[0], principled_bsdf_1.inputs[2])
    lunarsurfaceshader.links.new(color_ramp_1.outputs[0], color_ramp_001_1.inputs[0])
    lunarsurfaceshader.links.new(voronoi_texture_1.outputs[0], hue_saturation_value_001_1.inputs[4])
    lunarsurfaceshader.links.new(hue_saturation_value_1.outputs[0], bump_001_1.inputs[2])
    lunarsurfaceshader.links.new(hue_saturation_value_001_1.outputs[0], color_ramp_1.inputs[0])
    lunarsurfaceshader.links.new(color_ramp_1.outputs[0], mix_001_1.inputs[6])
    lunarsurfaceshader.links.new(color_ramp_001_1.outputs[0], hue_saturation_value_002_1.inputs[4])
    lunarsurfaceshader.links.new(map_range.outputs[0], bump_002_1.inputs[2])
    lunarsurfaceshader.links.new(mapping_1.outputs[0], noise_texture_1.inputs[0])
    lunarsurfaceshader.links.new(principled_bsdf_1.outputs[0], group_output_2.inputs[0])
    lunarsurfaceshader.links.new(group_input_2.outputs[0], mapping_1.inputs[3])
    lunarsurfaceshader.links.new(group_input_2.outputs[1], noise_texture_001_1.inputs[2])
    lunarsurfaceshader.links.new(group_input_2.outputs[2], voronoi_texture_1.inputs[2])
    lunarsurfaceshader.links.new(group_input_2.outputs[3], mix_002_1.inputs[6])
    lunarsurfaceshader.links.new(group_input_2.outputs[4], mix_002_1.inputs[7])
    lunarsurfaceshader.links.new(group_input_2.outputs[5], hue_saturation_value_1.inputs[2])
    lunarsurfaceshader.links.new(group_input_2.outputs[6], mix_1.inputs[0])
    lunarsurfaceshader.links.new(group_input_2.outputs[7], noise_texture_001_1.inputs[3])
    lunarsurfaceshader.links.new(group_input_2.outputs[9], voronoi_texture_1.inputs[3])
    lunarsurfaceshader.links.new(group_input_2.outputs[8], noise_texture_001_1.inputs[4])
    lunarsurfaceshader.links.new(group_input_2.outputs[10], hue_saturation_value_001_1.inputs[2])
    lunarsurfaceshader.links.new(group_input_2.outputs[11], hue_saturation_value_002_1.inputs[2])
    lunarsurfaceshader.links.new(group_input_2.outputs[12], bump_1.inputs[0])
    lunarsurfaceshader.links.new(group_input_2.outputs[13], bump_001_1.inputs[0])
    lunarsurfaceshader.links.new(group_input_2.outputs[14], bump_002_1.inputs[0])
    lunarsurfaceshader.links.new(noise_texture_001_1.outputs[0], mix_1.inputs[7])
    lunarsurfaceshader.links.new(mapping_1.outputs[0], mix_1.inputs[6])
    lunarsurfaceshader.links.new(mix_1.outputs[2], voronoi_texture_1.inputs[0])
    lunarsurfaceshader.links.new(bump_002_1.outputs[0], principled_bsdf_1.inputs[5])
    lunarsurfaceshader.links.new(group_001_1.outputs[0], map_range_004_1.inputs[0])
    lunarsurfaceshader.links.new(map_range_004_1.outputs[0], mapping_1.inputs[1])
    return lunarsurfaceshader

lunarsurfaceshader = lunarsurfaceshader_node_group()

def random_x8___mat_node_group():
    random_x8___mat = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "Random x8 | Mat")
    random_x8___mat.color_tag = 'NONE'
    random_x8___mat.default_group_node_width = 140
    _0_socket_1 = random_x8___mat.interface.new_socket(name = "0", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _0_socket_1.default_value = 0.0
    _0_socket_1.min_value = 0.0
    _0_socket_1.max_value = 1.0
    _0_socket_1.subtype = 'NONE'
    _0_socket_1.attribute_domain = 'POINT'
    _1_socket_1 = random_x8___mat.interface.new_socket(name = "1", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _1_socket_1.default_value = 0.0
    _1_socket_1.min_value = 0.0
    _1_socket_1.max_value = 1.0
    _1_socket_1.subtype = 'NONE'
    _1_socket_1.attribute_domain = 'POINT'
    _2_socket_1 = random_x8___mat.interface.new_socket(name = "2", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _2_socket_1.default_value = 0.0
    _2_socket_1.min_value = 0.0
    _2_socket_1.max_value = 1.0
    _2_socket_1.subtype = 'NONE'
    _2_socket_1.attribute_domain = 'POINT'
    _3_socket_1 = random_x8___mat.interface.new_socket(name = "3", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _3_socket_1.default_value = 0.0
    _3_socket_1.min_value = 0.0
    _3_socket_1.max_value = 1.0
    _3_socket_1.subtype = 'NONE'
    _3_socket_1.attribute_domain = 'POINT'
    _4_socket_1 = random_x8___mat.interface.new_socket(name = "4", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _4_socket_1.default_value = 0.0
    _4_socket_1.min_value = 0.0
    _4_socket_1.max_value = 1.0
    _4_socket_1.subtype = 'NONE'
    _4_socket_1.attribute_domain = 'POINT'
    _5_socket = random_x8___mat.interface.new_socket(name = "5", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _5_socket.default_value = 0.0
    _5_socket.min_value = 0.0
    _5_socket.max_value = 1.0
    _5_socket.subtype = 'NONE'
    _5_socket.attribute_domain = 'POINT'
    _6_socket = random_x8___mat.interface.new_socket(name = "6", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _6_socket.default_value = 0.0
    _6_socket.min_value = 0.0
    _6_socket.max_value = 1.0
    _6_socket.subtype = 'NONE'
    _6_socket.attribute_domain = 'POINT'
    _7_socket = random_x8___mat.interface.new_socket(name = "7", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _7_socket.default_value = 0.0
    _7_socket.min_value = 0.0
    _7_socket.max_value = 1.0
    _7_socket.subtype = 'NONE'
    _7_socket.attribute_domain = 'POINT'
    _8_socket = random_x8___mat.interface.new_socket(name = "8", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _8_socket.default_value = 0.0
    _8_socket.min_value = -3.4028234663852886e+38
    _8_socket.max_value = 3.4028234663852886e+38
    _8_socket.subtype = 'NONE'
    _8_socket.attribute_domain = 'POINT'
    seed_socket_1 = random_x8___mat.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketFloat')
    seed_socket_1.default_value = 0.0
    seed_socket_1.min_value = 0.0
    seed_socket_1.max_value = 1.0
    seed_socket_1.subtype = 'NONE'
    seed_socket_1.attribute_domain = 'POINT'
    group_output_3 = random_x8___mat.nodes.new("NodeGroupOutput")
    group_output_3.name = "Group Output"
    group_output_3.is_active_output = True
    group_input_3 = random_x8___mat.nodes.new("NodeGroupInput")
    group_input_3.name = "Group Input"
    object_info_1 = random_x8___mat.nodes.new("ShaderNodeObjectInfo")
    object_info_1.name = "Object Info"
    math_2 = random_x8___mat.nodes.new("ShaderNodeMath")
    math_2.name = "Math"
    math_2.operation = 'ADD'
    math_2.use_clamp = False
    white_noise_texture_1 = random_x8___mat.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture_1.name = "White Noise Texture"
    white_noise_texture_1.noise_dimensions = '4D'
    separate_color_1 = random_x8___mat.nodes.new("ShaderNodeSeparateColor")
    separate_color_1.name = "Separate Color"
    separate_color_1.mode = 'RGB'
    math_001_1 = random_x8___mat.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = 'ADD'
    math_001_1.use_clamp = False
    white_noise_texture_001_1 = random_x8___mat.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture_001_1.name = "White Noise Texture.001"
    white_noise_texture_001_1.noise_dimensions = '4D'
    separate_color_001_1 = random_x8___mat.nodes.new("ShaderNodeSeparateColor")
    separate_color_001_1.name = "Separate Color.001"
    separate_color_001_1.mode = 'RGB'
    math_002 = random_x8___mat.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'ADD'
    math_002.use_clamp = False
    white_noise_texture_002 = random_x8___mat.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture_002.name = "White Noise Texture.002"
    white_noise_texture_002.noise_dimensions = '4D'
    separate_color_002 = random_x8___mat.nodes.new("ShaderNodeSeparateColor")
    separate_color_002.name = "Separate Color.002"
    separate_color_002.mode = 'RGB'
    math_003 = random_x8___mat.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'ADD'
    math_003.use_clamp = False
    white_noise_texture_003 = random_x8___mat.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture_003.name = "White Noise Texture.003"
    white_noise_texture_003.noise_dimensions = '4D'
    separate_color_003 = random_x8___mat.nodes.new("ShaderNodeSeparateColor")
    separate_color_003.name = "Separate Color.003"
    separate_color_003.mode = 'RGB'
    random_x8___mat.links.new(object_info_1.outputs[5], white_noise_texture_1.inputs[1])
    random_x8___mat.links.new(math_2.outputs[0], white_noise_texture_1.inputs[0])
    random_x8___mat.links.new(white_noise_texture_1.outputs[1], separate_color_1.inputs[0])
    random_x8___mat.links.new(object_info_1.outputs[3], math_2.inputs[1])
    random_x8___mat.links.new(group_input_3.outputs[0], math_2.inputs[0])
    random_x8___mat.links.new(separate_color_1.outputs[0], group_output_3.inputs[0])
    random_x8___mat.links.new(separate_color_1.outputs[1], group_output_3.inputs[1])
    random_x8___mat.links.new(math_001_1.outputs[0], white_noise_texture_001_1.inputs[0])
    random_x8___mat.links.new(white_noise_texture_001_1.outputs[1], separate_color_001_1.inputs[0])
    random_x8___mat.links.new(math_002.outputs[0], white_noise_texture_002.inputs[0])
    random_x8___mat.links.new(white_noise_texture_002.outputs[1], separate_color_002.inputs[0])
    random_x8___mat.links.new(math_003.outputs[0], white_noise_texture_003.inputs[0])
    random_x8___mat.links.new(white_noise_texture_003.outputs[1], separate_color_003.inputs[0])
    random_x8___mat.links.new(separate_color_002.outputs[2], math_003.inputs[1])
    random_x8___mat.links.new(separate_color_001_1.outputs[2], math_002.inputs[1])
    random_x8___mat.links.new(separate_color_1.outputs[2], math_001_1.inputs[1])
    random_x8___mat.links.new(math_2.outputs[0], math_001_1.inputs[0])
    random_x8___mat.links.new(math_2.outputs[0], math_002.inputs[0])
    random_x8___mat.links.new(math_2.outputs[0], math_003.inputs[0])
    random_x8___mat.links.new(separate_color_001_1.outputs[0], group_output_3.inputs[2])
    random_x8___mat.links.new(separate_color_001_1.outputs[1], group_output_3.inputs[3])
    random_x8___mat.links.new(separate_color_002.outputs[0], group_output_3.inputs[4])
    random_x8___mat.links.new(separate_color_002.outputs[1], group_output_3.inputs[5])
    random_x8___mat.links.new(separate_color_003.outputs[0], group_output_3.inputs[6])
    random_x8___mat.links.new(separate_color_003.outputs[1], group_output_3.inputs[7])
    random_x8___mat.links.new(object_info_1.outputs[5], white_noise_texture_001_1.inputs[1])
    random_x8___mat.links.new(object_info_1.outputs[5], white_noise_texture_002.inputs[1])
    random_x8___mat.links.new(object_info_1.outputs[5], white_noise_texture_003.inputs[1])
    random_x8___mat.links.new(separate_color_003.outputs[2], group_output_3.inputs[8])
    return random_x8___mat

random_x8___mat = random_x8___mat_node_group()

def sandshader_002_node_group():
    sandshader_002 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "SandShader.002")
    sandshader_002.color_tag = 'NONE'
    sandshader_002.default_group_node_width = 140
    bsdf_socket_1 = sandshader_002.interface.new_socket(name = "BSDF", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    bsdf_socket_1.attribute_domain = 'POINT'
    scale_socket_2 = sandshader_002.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket_2.default_value = 1.0
    scale_socket_2.min_value = 0.0
    scale_socket_2.max_value = 3.4028234663852886e+38
    scale_socket_2.subtype = 'NONE'
    scale_socket_2.attribute_domain = 'POINT'
    rock_scale_socket = sandshader_002.interface.new_socket(name = "Rock Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    rock_scale_socket.default_value = 135.0
    rock_scale_socket.min_value = -1000.0
    rock_scale_socket.max_value = 1000.0
    rock_scale_socket.subtype = 'NONE'
    rock_scale_socket.attribute_domain = 'POINT'
    rock_individual_size_socket = sandshader_002.interface.new_socket(name = "Rock Individual Size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    rock_individual_size_socket.default_value = 1.0
    rock_individual_size_socket.min_value = 0.0
    rock_individual_size_socket.max_value = 2.0
    rock_individual_size_socket.subtype = 'NONE'
    rock_individual_size_socket.attribute_domain = 'POINT'
    rock_color_socket = sandshader_002.interface.new_socket(name = "Rock Color", in_out='INPUT', socket_type = 'NodeSocketColor')
    rock_color_socket.default_value = (0.5, 0.5, 0.5, 1.0)
    rock_color_socket.attribute_domain = 'POINT'
    sand_color_1_socket = sandshader_002.interface.new_socket(name = "Sand Color 1", in_out='INPUT', socket_type = 'NodeSocketColor')
    sand_color_1_socket.default_value = (0.5, 0.5, 0.5, 1.0)
    sand_color_1_socket.attribute_domain = 'POINT'
    sand_color_2_socket = sandshader_002.interface.new_socket(name = "Sand Color 2", in_out='INPUT', socket_type = 'NodeSocketColor')
    sand_color_2_socket.default_value = (0.5, 0.5, 0.5, 1.0)
    sand_color_2_socket.attribute_domain = 'POINT'
    detail_socket = sandshader_002.interface.new_socket(name = "Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detail_socket.default_value = 15.0
    detail_socket.min_value = 0.0
    detail_socket.max_value = 15.0
    detail_socket.subtype = 'NONE'
    detail_socket.attribute_domain = 'POINT'
    roughness_socket_2 = sandshader_002.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket_2.default_value = 0.5
    roughness_socket_2.min_value = 0.0
    roughness_socket_2.max_value = 1.0
    roughness_socket_2.subtype = 'FACTOR'
    roughness_socket_2.attribute_domain = 'POINT'
    sand_bump_strength_1_socket = sandshader_002.interface.new_socket(name = "Sand Bump Strength 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    sand_bump_strength_1_socket.default_value = 0.10000000149011612
    sand_bump_strength_1_socket.min_value = 0.0
    sand_bump_strength_1_socket.max_value = 1.0
    sand_bump_strength_1_socket.subtype = 'FACTOR'
    sand_bump_strength_1_socket.attribute_domain = 'POINT'
    sand_bump_strength_2_socket = sandshader_002.interface.new_socket(name = "Sand Bump Strength 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    sand_bump_strength_2_socket.default_value = 0.10000000149011612
    sand_bump_strength_2_socket.min_value = 0.0
    sand_bump_strength_2_socket.max_value = 1.0
    sand_bump_strength_2_socket.subtype = 'FACTOR'
    sand_bump_strength_2_socket.attribute_domain = 'POINT'
    rock_bump_strength_socket_1 = sandshader_002.interface.new_socket(name = "Rock Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    rock_bump_strength_socket_1.default_value = 0.30000001192092896
    rock_bump_strength_socket_1.min_value = 0.0
    rock_bump_strength_socket_1.max_value = 1.0
    rock_bump_strength_socket_1.subtype = 'FACTOR'
    rock_bump_strength_socket_1.attribute_domain = 'POINT'
    group_output_4 = sandshader_002.nodes.new("NodeGroupOutput")
    group_output_4.name = "Group Output"
    group_output_4.is_active_output = True
    group_input_4 = sandshader_002.nodes.new("NodeGroupInput")
    group_input_4.name = "Group Input"
    principled_bsdf_2 = sandshader_002.nodes.new("ShaderNodeBsdfPrincipled")
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
    mapping_2 = sandshader_002.nodes.new("ShaderNodeMapping")
    mapping_2.name = "Mapping"
    mapping_2.vector_type = 'POINT'
    mapping_2.inputs[2].default_value = (0.0, 0.0, 0.0)
    texture_coordinate_2 = sandshader_002.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_2.name = "Texture Coordinate"
    texture_coordinate_2.from_instancer = False
    texture_coordinate_2.outputs[0].hide = True
    texture_coordinate_2.outputs[1].hide = True
    texture_coordinate_2.outputs[2].hide = True
    texture_coordinate_2.outputs[4].hide = True
    texture_coordinate_2.outputs[5].hide = True
    texture_coordinate_2.outputs[6].hide = True
    voronoi_texture_2 = sandshader_002.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_2.name = "Voronoi Texture"
    voronoi_texture_2.distance = 'EUCLIDEAN'
    voronoi_texture_2.feature = 'F1'
    voronoi_texture_2.normalize = False
    voronoi_texture_2.voronoi_dimensions = '3D'
    voronoi_texture_2.inputs[3].default_value = 2.0
    voronoi_texture_2.inputs[4].default_value = 0.5
    voronoi_texture_2.inputs[5].default_value = 1.7000000476837158
    voronoi_texture_2.inputs[8].default_value = 1.0
    hue_saturation_value_2 = sandshader_002.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_2.name = "Hue/Saturation/Value"
    hue_saturation_value_2.inputs[0].default_value = 0.5
    hue_saturation_value_2.inputs[1].default_value = 1.0
    hue_saturation_value_2.inputs[3].default_value = 1.0
    color_ramp_001_2 = sandshader_002.nodes.new("ShaderNodeValToRGB")
    color_ramp_001_2.name = "Color Ramp.001"
    color_ramp_001_2.color_ramp.color_mode = 'RGB'
    color_ramp_001_2.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_001_2.color_ramp.interpolation = 'LINEAR'
    color_ramp_001_2.color_ramp.elements.remove(color_ramp_001_2.color_ramp.elements[0])
    color_ramp_001_2_cre_0 = color_ramp_001_2.color_ramp.elements[0]
    color_ramp_001_2_cre_0.position = 0.6227270364761353
    color_ramp_001_2_cre_0.alpha = 1.0
    color_ramp_001_2_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_001_2_cre_1 = color_ramp_001_2.color_ramp.elements.new(0.6272730827331543)
    color_ramp_001_2_cre_1.alpha = 1.0
    color_ramp_001_2_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    color_ramp_002_1 = sandshader_002.nodes.new("ShaderNodeValToRGB")
    color_ramp_002_1.name = "Color Ramp.002"
    color_ramp_002_1.color_ramp.color_mode = 'RGB'
    color_ramp_002_1.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_002_1.color_ramp.interpolation = 'LINEAR'
    color_ramp_002_1.color_ramp.elements.remove(color_ramp_002_1.color_ramp.elements[0])
    color_ramp_002_1_cre_0 = color_ramp_002_1.color_ramp.elements[0]
    color_ramp_002_1_cre_0.position = 0.0
    color_ramp_002_1_cre_0.alpha = 1.0
    color_ramp_002_1_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_002_1_cre_1 = color_ramp_002_1.color_ramp.elements.new(0.6272730827331543)
    color_ramp_002_1_cre_1.alpha = 1.0
    color_ramp_002_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    noise_texture_2 = sandshader_002.nodes.new("ShaderNodeTexNoise")
    noise_texture_2.name = "Noise Texture"
    noise_texture_2.noise_dimensions = '3D'
    noise_texture_2.noise_type = 'FBM'
    noise_texture_2.normalize = True
    noise_texture_2.inputs[2].default_value = 15.0
    noise_texture_2.inputs[4].default_value = 0.4000000059604645
    noise_texture_2.inputs[5].default_value = 2.0
    noise_texture_2.inputs[8].default_value = 0.0
    mix_001_2 = sandshader_002.nodes.new("ShaderNodeMix")
    mix_001_2.name = "Mix.001"
    mix_001_2.blend_type = 'MIX'
    mix_001_2.clamp_factor = True
    mix_001_2.clamp_result = False
    mix_001_2.data_type = 'RGBA'
    mix_001_2.factor_mode = 'UNIFORM'
    mix_003_1 = sandshader_002.nodes.new("ShaderNodeMix")
    mix_003_1.name = "Mix.003"
    mix_003_1.blend_type = 'MIX'
    mix_003_1.clamp_factor = True
    mix_003_1.clamp_result = False
    mix_003_1.data_type = 'RGBA'
    mix_003_1.factor_mode = 'UNIFORM'
    noise_texture_001_2 = sandshader_002.nodes.new("ShaderNodeTexNoise")
    noise_texture_001_2.name = "Noise Texture.001"
    noise_texture_001_2.noise_dimensions = '3D'
    noise_texture_001_2.noise_type = 'FBM'
    noise_texture_001_2.normalize = True
    noise_texture_001_2.inputs[2].default_value = 15.0
    noise_texture_001_2.inputs[4].default_value = 0.699999988079071
    noise_texture_001_2.inputs[5].default_value = 2.0
    noise_texture_001_2.inputs[8].default_value = 0.0
    bump_2 = sandshader_002.nodes.new("ShaderNodeBump")
    bump_2.name = "Bump"
    bump_2.invert = False
    bump_2.inputs[1].default_value = 1.0
    bump_2.inputs[3].default_value = (0.0, 0.0, 0.0)
    bump_001_2 = sandshader_002.nodes.new("ShaderNodeBump")
    bump_001_2.name = "Bump.001"
    bump_001_2.invert = False
    bump_001_2.inputs[1].default_value = 1.0
    bump_002_2 = sandshader_002.nodes.new("ShaderNodeBump")
    bump_002_2.name = "Bump.002"
    bump_002_2.invert = False
    bump_002_2.inputs[1].default_value = 1.0
    group_001_2 = sandshader_002.nodes.new("ShaderNodeGroup")
    group_001_2.name = "Group.001"
    group_001_2.node_tree = random_x4___mat_005
    group_001_2.inputs[0].default_value = 0.23152099549770355
    map_range_004_2 = sandshader_002.nodes.new("ShaderNodeMapRange")
    map_range_004_2.name = "Map Range.004"
    map_range_004_2.clamp = True
    map_range_004_2.data_type = 'FLOAT'
    map_range_004_2.interpolation_type = 'LINEAR'
    map_range_004_2.inputs[1].default_value = 0.0
    map_range_004_2.inputs[2].default_value = 1.0
    map_range_004_2.inputs[3].default_value = -1000.0
    map_range_004_2.inputs[4].default_value = 1000.0
    sandshader_002.links.new(color_ramp_001_2.outputs[0], mix_003_1.inputs[0])
    sandshader_002.links.new(bump_2.outputs[0], bump_001_2.inputs[3])
    sandshader_002.links.new(noise_texture_2.outputs[0], bump_2.inputs[2])
    sandshader_002.links.new(texture_coordinate_2.outputs[3], mapping_2.inputs[0])
    sandshader_002.links.new(mapping_2.outputs[0], voronoi_texture_2.inputs[0])
    sandshader_002.links.new(noise_texture_001_2.outputs[0], bump_001_2.inputs[2])
    sandshader_002.links.new(mix_001_2.outputs[2], mix_003_1.inputs[7])
    sandshader_002.links.new(mapping_2.outputs[0], noise_texture_001_2.inputs[0])
    sandshader_002.links.new(bump_002_2.outputs[0], principled_bsdf_2.inputs[5])
    sandshader_002.links.new(color_ramp_002_1.outputs[0], bump_002_2.inputs[2])
    sandshader_002.links.new(bump_001_2.outputs[0], bump_002_2.inputs[3])
    sandshader_002.links.new(hue_saturation_value_2.outputs[0], color_ramp_001_2.inputs[0])
    sandshader_002.links.new(voronoi_texture_2.outputs[1], hue_saturation_value_2.inputs[4])
    sandshader_002.links.new(hue_saturation_value_2.outputs[0], color_ramp_002_1.inputs[0])
    sandshader_002.links.new(mapping_2.outputs[0], noise_texture_2.inputs[0])
    sandshader_002.links.new(mix_003_1.outputs[2], principled_bsdf_2.inputs[0])
    sandshader_002.links.new(noise_texture_2.outputs[0], mix_001_2.inputs[0])
    sandshader_002.links.new(principled_bsdf_2.outputs[0], group_output_4.inputs[0])
    sandshader_002.links.new(group_input_4.outputs[0], mapping_2.inputs[3])
    sandshader_002.links.new(group_input_4.outputs[1], voronoi_texture_2.inputs[2])
    sandshader_002.links.new(group_input_4.outputs[2], hue_saturation_value_2.inputs[2])
    sandshader_002.links.new(group_input_4.outputs[3], mix_003_1.inputs[6])
    sandshader_002.links.new(group_input_4.outputs[4], mix_001_2.inputs[6])
    sandshader_002.links.new(group_input_4.outputs[5], mix_001_2.inputs[7])
    sandshader_002.links.new(group_input_4.outputs[6], noise_texture_2.inputs[3])
    sandshader_002.links.new(group_input_4.outputs[6], noise_texture_001_2.inputs[3])
    sandshader_002.links.new(group_input_4.outputs[7], principled_bsdf_2.inputs[2])
    sandshader_002.links.new(group_input_4.outputs[8], bump_2.inputs[0])
    sandshader_002.links.new(group_input_4.outputs[9], bump_001_2.inputs[0])
    sandshader_002.links.new(group_input_4.outputs[10], bump_002_2.inputs[0])
    sandshader_002.links.new(group_001_2.outputs[0], map_range_004_2.inputs[0])
    sandshader_002.links.new(map_range_004_2.outputs[0], mapping_2.inputs[1])
    return sandshader_002

sandshader_002 = sandshader_002_node_group()

def smoothrockshader_node_group():
    smoothrockshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "SmoothRockShader")
    smoothrockshader.color_tag = 'NONE'
    smoothrockshader.default_group_node_width = 140
    bsdf_socket_2 = smoothrockshader.interface.new_socket(name = "BSDF", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    bsdf_socket_2.attribute_domain = 'POINT'
    scale_socket_3 = smoothrockshader.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket_3.default_value = 1.0
    scale_socket_3.min_value = 0.0
    scale_socket_3.max_value = 3.4028234663852886e+38
    scale_socket_3.subtype = 'NONE'
    scale_socket_3.attribute_domain = 'POINT'
    noise_scale_socket = smoothrockshader.interface.new_socket(name = "Noise Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_scale_socket.default_value = 18.0
    noise_scale_socket.min_value = -1000.0
    noise_scale_socket.max_value = 1000.0
    noise_scale_socket.subtype = 'NONE'
    noise_scale_socket.attribute_domain = 'POINT'
    wave_scale_socket = smoothrockshader.interface.new_socket(name = "Wave Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    wave_scale_socket.default_value = 1.0
    wave_scale_socket.min_value = -1000.0
    wave_scale_socket.max_value = 1000.0
    wave_scale_socket.subtype = 'NONE'
    wave_scale_socket.attribute_domain = 'POINT'
    voronoi_scale_socket = smoothrockshader.interface.new_socket(name = "Voronoi Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    voronoi_scale_socket.default_value = 15.0
    voronoi_scale_socket.min_value = -1000.0
    voronoi_scale_socket.max_value = 1000.0
    voronoi_scale_socket.subtype = 'NONE'
    voronoi_scale_socket.attribute_domain = 'POINT'
    color_1_socket_1 = smoothrockshader.interface.new_socket(name = "Color 1", in_out='INPUT', socket_type = 'NodeSocketColor')
    color_1_socket_1.default_value = (0.5, 0.5, 0.5, 1.0)
    color_1_socket_1.attribute_domain = 'POINT'
    color_2_socket_1 = smoothrockshader.interface.new_socket(name = "Color 2", in_out='INPUT', socket_type = 'NodeSocketColor')
    color_2_socket_1.default_value = (0.5, 0.5, 0.5, 1.0)
    color_2_socket_1.attribute_domain = 'POINT'
    distortion_1_socket = smoothrockshader.interface.new_socket(name = "Distortion 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    distortion_1_socket.default_value = 0.05000000074505806
    distortion_1_socket.min_value = 0.0
    distortion_1_socket.max_value = 1.0
    distortion_1_socket.subtype = 'FACTOR'
    distortion_1_socket.attribute_domain = 'POINT'
    distortion_2_socket = smoothrockshader.interface.new_socket(name = "Distortion 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    distortion_2_socket.default_value = 0.019999999552965164
    distortion_2_socket.min_value = 0.0
    distortion_2_socket.max_value = 1.0
    distortion_2_socket.subtype = 'FACTOR'
    distortion_2_socket.attribute_domain = 'POINT'
    detail_1_socket_1 = smoothrockshader.interface.new_socket(name = "Detail 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detail_1_socket_1.default_value = 15.0
    detail_1_socket_1.min_value = 0.0
    detail_1_socket_1.max_value = 15.0
    detail_1_socket_1.subtype = 'NONE'
    detail_1_socket_1.attribute_domain = 'POINT'
    detail_2_socket_1 = smoothrockshader.interface.new_socket(name = "Detail 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detail_2_socket_1.default_value = 0.0
    detail_2_socket_1.min_value = 0.0
    detail_2_socket_1.max_value = 15.0
    detail_2_socket_1.subtype = 'NONE'
    detail_2_socket_1.attribute_domain = 'POINT'
    roughness_socket_3 = smoothrockshader.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket_3.default_value = 0.5
    roughness_socket_3.min_value = 0.0
    roughness_socket_3.max_value = 1.0
    roughness_socket_3.subtype = 'FACTOR'
    roughness_socket_3.attribute_domain = 'POINT'
    bump_strength_socket = smoothrockshader.interface.new_socket(name = "Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    bump_strength_socket.default_value = 0.10000000149011612
    bump_strength_socket.min_value = 0.0
    bump_strength_socket.max_value = 1.0
    bump_strength_socket.subtype = 'FACTOR'
    bump_strength_socket.attribute_domain = 'POINT'
    group_output_5 = smoothrockshader.nodes.new("NodeGroupOutput")
    group_output_5.name = "Group Output"
    group_output_5.is_active_output = True
    group_input_5 = smoothrockshader.nodes.new("NodeGroupInput")
    group_input_5.name = "Group Input"
    principled_bsdf_3 = smoothrockshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_3.name = "Principled BSDF"
    principled_bsdf_3.distribution = 'MULTI_GGX'
    principled_bsdf_3.subsurface_method = 'RANDOM_WALK'
    principled_bsdf_3.inputs[1].default_value = 0.0
    principled_bsdf_3.inputs[3].default_value = 1.5
    principled_bsdf_3.inputs[4].default_value = 1.0
    principled_bsdf_3.inputs[7].default_value = 0.0
    principled_bsdf_3.inputs[8].default_value = 0.0
    principled_bsdf_3.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    principled_bsdf_3.inputs[10].default_value = 0.05000000074505806
    principled_bsdf_3.inputs[12].default_value = 0.0
    principled_bsdf_3.inputs[13].default_value = 0.5
    principled_bsdf_3.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_3.inputs[15].default_value = 0.0
    principled_bsdf_3.inputs[16].default_value = 0.0
    principled_bsdf_3.inputs[17].default_value = (0.0, 0.0, 0.0)
    principled_bsdf_3.inputs[18].default_value = 0.0
    principled_bsdf_3.inputs[19].default_value = 0.0
    principled_bsdf_3.inputs[20].default_value = 0.029999999329447746
    principled_bsdf_3.inputs[21].default_value = 1.5
    principled_bsdf_3.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_3.inputs[23].default_value = (0.0, 0.0, 0.0)
    principled_bsdf_3.inputs[24].default_value = 0.0
    principled_bsdf_3.inputs[25].default_value = 0.5
    principled_bsdf_3.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_3.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_3.inputs[28].default_value = 0.0
    principled_bsdf_3.inputs[29].default_value = 0.0
    principled_bsdf_3.inputs[30].default_value = 1.3300000429153442
    mapping_3 = smoothrockshader.nodes.new("ShaderNodeMapping")
    mapping_3.name = "Mapping"
    mapping_3.vector_type = 'POINT'
    mapping_3.inputs[2].default_value = (0.0, 0.0, 0.0)
    texture_coordinate_3 = smoothrockshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_3.name = "Texture Coordinate"
    texture_coordinate_3.from_instancer = False
    texture_coordinate_3.outputs[0].hide = True
    texture_coordinate_3.outputs[1].hide = True
    texture_coordinate_3.outputs[2].hide = True
    texture_coordinate_3.outputs[4].hide = True
    texture_coordinate_3.outputs[5].hide = True
    texture_coordinate_3.outputs[6].hide = True
    noise_texture_3 = smoothrockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_3.name = "Noise Texture"
    noise_texture_3.noise_dimensions = '3D'
    noise_texture_3.noise_type = 'FBM'
    noise_texture_3.normalize = True
    noise_texture_3.inputs[4].default_value = 0.5
    noise_texture_3.inputs[5].default_value = 2.0
    noise_texture_3.inputs[8].default_value = 0.0
    mix_001_3 = smoothrockshader.nodes.new("ShaderNodeMix")
    mix_001_3.name = "Mix.001"
    mix_001_3.blend_type = 'LINEAR_LIGHT'
    mix_001_3.clamp_factor = True
    mix_001_3.clamp_result = False
    mix_001_3.data_type = 'RGBA'
    mix_001_3.factor_mode = 'UNIFORM'
    mix_001_3.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
    wave_texture = smoothrockshader.nodes.new("ShaderNodeTexWave")
    wave_texture.name = "Wave Texture"
    wave_texture.bands_direction = 'X'
    wave_texture.rings_direction = 'X'
    wave_texture.wave_profile = 'SIN'
    wave_texture.wave_type = 'BANDS'
    wave_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    wave_texture.inputs[2].default_value = 15.0
    wave_texture.inputs[4].default_value = 1.2000000476837158
    wave_texture.inputs[5].default_value = 0.6000000238418579
    wave_texture.inputs[6].default_value = 0.0
    voronoi_texture_3 = smoothrockshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_3.name = "Voronoi Texture"
    voronoi_texture_3.distance = 'EUCLIDEAN'
    voronoi_texture_3.feature = 'F1'
    voronoi_texture_3.normalize = False
    voronoi_texture_3.voronoi_dimensions = '3D'
    voronoi_texture_3.inputs[4].default_value = 0.5
    voronoi_texture_3.inputs[5].default_value = 2.0
    voronoi_texture_3.inputs[8].default_value = 1.0
    mix_003_2 = smoothrockshader.nodes.new("ShaderNodeMix")
    mix_003_2.name = "Mix.003"
    mix_003_2.blend_type = 'LINEAR_LIGHT'
    mix_003_2.clamp_factor = True
    mix_003_2.clamp_result = False
    mix_003_2.data_type = 'RGBA'
    mix_003_2.factor_mode = 'UNIFORM'
    mix_003_2.inputs[7].default_value = (0.5, 0.5, 0.5, 1.0)
    color_ramp_001_3 = smoothrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_001_3.name = "Color Ramp.001"
    color_ramp_001_3.color_ramp.color_mode = 'RGB'
    color_ramp_001_3.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_001_3.color_ramp.interpolation = 'LINEAR'
    color_ramp_001_3.color_ramp.elements.remove(color_ramp_001_3.color_ramp.elements[0])
    color_ramp_001_3_cre_0 = color_ramp_001_3.color_ramp.elements[0]
    color_ramp_001_3_cre_0.position = 0.3590908348560333
    color_ramp_001_3_cre_0.alpha = 1.0
    color_ramp_001_3_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_001_3_cre_1 = color_ramp_001_3.color_ramp.elements.new(0.4045455753803253)
    color_ramp_001_3_cre_1.alpha = 1.0
    color_ramp_001_3_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    bump_3 = smoothrockshader.nodes.new("ShaderNodeBump")
    bump_3.name = "Bump"
    bump_3.invert = False
    bump_3.inputs[1].default_value = 1.0
    bump_3.inputs[3].default_value = (0.0, 0.0, 0.0)
    mix_004_1 = smoothrockshader.nodes.new("ShaderNodeMix")
    mix_004_1.name = "Mix.004"
    mix_004_1.blend_type = 'MIX'
    mix_004_1.clamp_factor = True
    mix_004_1.clamp_result = False
    mix_004_1.data_type = 'RGBA'
    mix_004_1.factor_mode = 'UNIFORM'
    group_001_3 = smoothrockshader.nodes.new("ShaderNodeGroup")
    group_001_3.name = "Group.001"
    group_001_3.node_tree = random_x4___mat_005
    group_001_3.inputs[0].default_value = 0.6341999769210815
    map_range_004_3 = smoothrockshader.nodes.new("ShaderNodeMapRange")
    map_range_004_3.name = "Map Range.004"
    map_range_004_3.clamp = True
    map_range_004_3.data_type = 'FLOAT'
    map_range_004_3.interpolation_type = 'LINEAR'
    map_range_004_3.inputs[1].default_value = 0.0
    map_range_004_3.inputs[2].default_value = 1.0
    map_range_004_3.inputs[3].default_value = -1000.0
    map_range_004_3.inputs[4].default_value = 1000.0
    smoothrockshader.links.new(voronoi_texture_3.outputs[0], bump_3.inputs[2])
    smoothrockshader.links.new(mix_003_2.outputs[2], voronoi_texture_3.inputs[0])
    smoothrockshader.links.new(mapping_3.outputs[0], mix_001_3.inputs[6])
    smoothrockshader.links.new(voronoi_texture_3.outputs[0], color_ramp_001_3.inputs[0])
    smoothrockshader.links.new(bump_3.outputs[0], principled_bsdf_3.inputs[5])
    smoothrockshader.links.new(texture_coordinate_3.outputs[3], mapping_3.inputs[0])
    smoothrockshader.links.new(mix_004_1.outputs[2], principled_bsdf_3.inputs[0])
    smoothrockshader.links.new(color_ramp_001_3.outputs[0], mix_004_1.inputs[0])
    smoothrockshader.links.new(mapping_3.outputs[0], noise_texture_3.inputs[0])
    smoothrockshader.links.new(mapping_3.outputs[0], mix_003_2.inputs[6])
    smoothrockshader.links.new(principled_bsdf_3.outputs[0], group_output_5.inputs[0])
    smoothrockshader.links.new(group_input_5.outputs[0], mapping_3.inputs[3])
    smoothrockshader.links.new(group_input_5.outputs[1], noise_texture_3.inputs[2])
    smoothrockshader.links.new(group_input_5.outputs[2], wave_texture.inputs[1])
    smoothrockshader.links.new(group_input_5.outputs[3], voronoi_texture_3.inputs[2])
    smoothrockshader.links.new(group_input_5.outputs[4], mix_004_1.inputs[6])
    smoothrockshader.links.new(group_input_5.outputs[5], mix_004_1.inputs[7])
    smoothrockshader.links.new(group_input_5.outputs[6], mix_001_3.inputs[0])
    smoothrockshader.links.new(group_input_5.outputs[7], mix_003_2.inputs[0])
    smoothrockshader.links.new(group_input_5.outputs[8], wave_texture.inputs[3])
    smoothrockshader.links.new(group_input_5.outputs[8], noise_texture_3.inputs[3])
    smoothrockshader.links.new(group_input_5.outputs[9], voronoi_texture_3.inputs[3])
    smoothrockshader.links.new(group_input_5.outputs[10], principled_bsdf_3.inputs[2])
    smoothrockshader.links.new(group_input_5.outputs[11], bump_3.inputs[0])
    smoothrockshader.links.new(group_001_3.outputs[0], map_range_004_3.inputs[0])
    smoothrockshader.links.new(map_range_004_3.outputs[0], mapping_3.inputs[1])
    return smoothrockshader

smoothrockshader = smoothrockshader_node_group()

def random_x2___mat_003_node_group():
    random_x2___mat_003 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "Random x2 | Mat.003")
    random_x2___mat_003.color_tag = 'NONE'
    random_x2___mat_003.default_group_node_width = 140
    _0_socket_2 = random_x2___mat_003.interface.new_socket(name = "0", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _0_socket_2.default_value = 0.0
    _0_socket_2.min_value = 0.0
    _0_socket_2.max_value = 1.0
    _0_socket_2.subtype = 'NONE'
    _0_socket_2.attribute_domain = 'POINT'
    _1_socket_2 = random_x2___mat_003.interface.new_socket(name = "1", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _1_socket_2.default_value = 0.0
    _1_socket_2.min_value = 0.0
    _1_socket_2.max_value = 1.0
    _1_socket_2.subtype = 'NONE'
    _1_socket_2.attribute_domain = 'POINT'
    _2_socket_2 = random_x2___mat_003.interface.new_socket(name = "2", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _2_socket_2.default_value = 0.0
    _2_socket_2.min_value = -3.4028234663852886e+38
    _2_socket_2.max_value = 3.4028234663852886e+38
    _2_socket_2.subtype = 'NONE'
    _2_socket_2.attribute_domain = 'POINT'
    seed_socket_2 = random_x2___mat_003.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketFloat')
    seed_socket_2.default_value = 0.0
    seed_socket_2.min_value = 0.0
    seed_socket_2.max_value = 1.0
    seed_socket_2.subtype = 'NONE'
    seed_socket_2.attribute_domain = 'POINT'
    group_output_6 = random_x2___mat_003.nodes.new("NodeGroupOutput")
    group_output_6.name = "Group Output"
    group_output_6.is_active_output = True
    group_input_6 = random_x2___mat_003.nodes.new("NodeGroupInput")
    group_input_6.name = "Group Input"
    object_info_2 = random_x2___mat_003.nodes.new("ShaderNodeObjectInfo")
    object_info_2.name = "Object Info"
    math_3 = random_x2___mat_003.nodes.new("ShaderNodeMath")
    math_3.name = "Math"
    math_3.operation = 'ADD'
    math_3.use_clamp = False
    white_noise_texture_2 = random_x2___mat_003.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture_2.name = "White Noise Texture"
    white_noise_texture_2.noise_dimensions = '4D'
    separate_color_2 = random_x2___mat_003.nodes.new("ShaderNodeSeparateColor")
    separate_color_2.name = "Separate Color"
    separate_color_2.mode = 'RGB'
    random_x2___mat_003.links.new(object_info_2.outputs[5], white_noise_texture_2.inputs[1])
    random_x2___mat_003.links.new(math_3.outputs[0], white_noise_texture_2.inputs[0])
    random_x2___mat_003.links.new(white_noise_texture_2.outputs[1], separate_color_2.inputs[0])
    random_x2___mat_003.links.new(object_info_2.outputs[3], math_3.inputs[1])
    random_x2___mat_003.links.new(group_input_6.outputs[0], math_3.inputs[0])
    random_x2___mat_003.links.new(separate_color_2.outputs[0], group_output_6.inputs[0])
    random_x2___mat_003.links.new(separate_color_2.outputs[1], group_output_6.inputs[1])
    random_x2___mat_003.links.new(separate_color_2.outputs[2], group_output_6.inputs[2])
    return random_x2___mat_003

random_x2___mat_003 = random_x2___mat_003_node_group()

def moonrockshader_004_node_group():
    moonrockshader_004 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "MoonRockShader.004")
    moonrockshader_004.color_tag = 'NONE'
    moonrockshader_004.default_group_node_width = 140
    bsdf_socket_3 = moonrockshader_004.interface.new_socket(name = "BSDF", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    bsdf_socket_3.attribute_domain = 'POINT'
    scale_socket_4 = moonrockshader_004.interface.new_socket(name = "scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket_4.default_value = 16.0
    scale_socket_4.min_value = 0.0
    scale_socket_4.max_value = 3.4028234663852886e+38
    scale_socket_4.subtype = 'NONE'
    scale_socket_4.attribute_domain = 'POINT'
    color1_socket = moonrockshader_004.interface.new_socket(name = "color1", in_out='INPUT', socket_type = 'NodeSocketColor')
    color1_socket.default_value = (0.24619978666305542, 0.24620160460472107, 0.2462015002965927, 1.0)
    color1_socket.attribute_domain = 'POINT'
    color2_socket = moonrockshader_004.interface.new_socket(name = "color2", in_out='INPUT', socket_type = 'NodeSocketColor')
    color2_socket.default_value = (0.005181482061743736, 0.005181520711630583, 0.005181518383324146, 1.0)
    color2_socket.attribute_domain = 'POINT'
    edge_color_socket = moonrockshader_004.interface.new_socket(name = "edge_color", in_out='INPUT', socket_type = 'NodeSocketColor')
    edge_color_socket.default_value = (0.4000000059604645, 0.4000000059604645, 0.4000000059604645, 1.0)
    edge_color_socket.attribute_domain = 'POINT'
    noise_scale_socket_1 = moonrockshader_004.interface.new_socket(name = "noise_scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_scale_socket_1.default_value = 7.0
    noise_scale_socket_1.min_value = -1000.0
    noise_scale_socket_1.max_value = 1000.0
    noise_scale_socket_1.subtype = 'NONE'
    noise_scale_socket_1.attribute_domain = 'POINT'
    noise_detail_socket = moonrockshader_004.interface.new_socket(name = "noise_detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_detail_socket.default_value = 15.0
    noise_detail_socket.min_value = 0.0
    noise_detail_socket.max_value = 15.0
    noise_detail_socket.subtype = 'NONE'
    noise_detail_socket.attribute_domain = 'POINT'
    noise_roughness_socket = moonrockshader_004.interface.new_socket(name = "noise_roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_roughness_socket.default_value = 0.25
    noise_roughness_socket.min_value = 0.0
    noise_roughness_socket.max_value = 1.0
    noise_roughness_socket.subtype = 'FACTOR'
    noise_roughness_socket.attribute_domain = 'POINT'
    light_noise_scale_socket = moonrockshader_004.interface.new_socket(name = "light_noise_scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    light_noise_scale_socket.default_value = 5.0
    light_noise_scale_socket.min_value = 0.0
    light_noise_scale_socket.max_value = 15.0
    light_noise_scale_socket.subtype = 'NONE'
    light_noise_scale_socket.attribute_domain = 'POINT'
    light_noise_roughness_socket = moonrockshader_004.interface.new_socket(name = "light_noise_roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    light_noise_roughness_socket.default_value = 0.800000011920929
    light_noise_roughness_socket.min_value = 0.0
    light_noise_roughness_socket.max_value = 1.0
    light_noise_roughness_socket.subtype = 'FACTOR'
    light_noise_roughness_socket.attribute_domain = 'POINT'
    roughness_socket_4 = moonrockshader_004.interface.new_socket(name = "roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket_4.default_value = 1.0
    roughness_socket_4.min_value = 0.0
    roughness_socket_4.max_value = 2.0
    roughness_socket_4.subtype = 'NONE'
    roughness_socket_4.attribute_domain = 'POINT'
    noise_bump_scale_socket = moonrockshader_004.interface.new_socket(name = "noise_bump_scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_scale_socket.default_value = 15.0
    noise_bump_scale_socket.min_value = -1000.0
    noise_bump_scale_socket.max_value = 1000.0
    noise_bump_scale_socket.subtype = 'NONE'
    noise_bump_scale_socket.attribute_domain = 'POINT'
    noise_bump_strength_socket = moonrockshader_004.interface.new_socket(name = "noise_bump_strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_strength_socket.default_value = 0.05000000074505806
    noise_bump_strength_socket.min_value = 0.0
    noise_bump_strength_socket.max_value = 1.0
    noise_bump_strength_socket.subtype = 'FACTOR'
    noise_bump_strength_socket.attribute_domain = 'POINT'
    detailed_noise_bump_strength_socket = moonrockshader_004.interface.new_socket(name = "detailed_noise_bump_strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detailed_noise_bump_strength_socket.default_value = 0.25
    detailed_noise_bump_strength_socket.min_value = 0.0
    detailed_noise_bump_strength_socket.max_value = 1.0
    detailed_noise_bump_strength_socket.subtype = 'FACTOR'
    detailed_noise_bump_strength_socket.attribute_domain = 'POINT'
    edge_color_strength_socket = moonrockshader_004.interface.new_socket(name = "edge_color_strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    edge_color_strength_socket.default_value = 0.75
    edge_color_strength_socket.min_value = 0.0
    edge_color_strength_socket.max_value = 1.0
    edge_color_strength_socket.subtype = 'FACTOR'
    edge_color_strength_socket.attribute_domain = 'POINT'
    noise_scale_mixer_socket = moonrockshader_004.interface.new_socket(name = "noise_scale_mixer", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_scale_mixer_socket.default_value = 0.009999999776482582
    noise_scale_mixer_socket.min_value = 0.0
    noise_scale_mixer_socket.max_value = 1.0
    noise_scale_mixer_socket.subtype = 'FACTOR'
    noise_scale_mixer_socket.attribute_domain = 'POINT'
    noise_bump_roughness_socket = moonrockshader_004.interface.new_socket(name = "noise_bump_roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_roughness_socket.default_value = 1.0
    noise_bump_roughness_socket.min_value = 0.0
    noise_bump_roughness_socket.max_value = 1.0
    noise_bump_roughness_socket.subtype = 'FACTOR'
    noise_bump_roughness_socket.attribute_domain = 'POINT'
    voronoi_bump_scale_socket = moonrockshader_004.interface.new_socket(name = "voronoi_bump_scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    voronoi_bump_scale_socket.default_value = 20.0
    voronoi_bump_scale_socket.min_value = -1000.0
    voronoi_bump_scale_socket.max_value = 1000.0
    voronoi_bump_scale_socket.subtype = 'NONE'
    voronoi_bump_scale_socket.attribute_domain = 'POINT'
    voronoi_bump_strength_socket = moonrockshader_004.interface.new_socket(name = "voronoi_bump_strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    voronoi_bump_strength_socket.default_value = 0.75
    voronoi_bump_strength_socket.min_value = 0.0
    voronoi_bump_strength_socket.max_value = 1.0
    voronoi_bump_strength_socket.subtype = 'FACTOR'
    voronoi_bump_strength_socket.attribute_domain = 'POINT'
    group_output_7 = moonrockshader_004.nodes.new("NodeGroupOutput")
    group_output_7.name = "Group Output"
    group_output_7.is_active_output = True
    group_input_7 = moonrockshader_004.nodes.new("NodeGroupInput")
    group_input_7.name = "Group Input"
    noise_texture_4 = moonrockshader_004.nodes.new("ShaderNodeTexNoise")
    noise_texture_4.name = "Noise Texture"
    noise_texture_4.noise_dimensions = '4D'
    noise_texture_4.noise_type = 'FBM'
    noise_texture_4.normalize = True
    noise_texture_4.inputs[5].default_value = 20.0
    noise_texture_4.inputs[8].default_value = 0.0
    mapping_001 = moonrockshader_004.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = 'POINT'
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    texture_coordinate_001 = moonrockshader_004.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_001.name = "Texture Coordinate.001"
    texture_coordinate_001.from_instancer = False
    texture_coordinate_001.outputs[0].hide = True
    texture_coordinate_001.outputs[1].hide = True
    texture_coordinate_001.outputs[2].hide = True
    texture_coordinate_001.outputs[4].hide = True
    texture_coordinate_001.outputs[5].hide = True
    texture_coordinate_001.outputs[6].hide = True
    bump_4 = moonrockshader_004.nodes.new("ShaderNodeBump")
    bump_4.name = "Bump"
    bump_4.invert = False
    bump_4.inputs[1].default_value = 1.0
    color_ramp_2 = moonrockshader_004.nodes.new("ShaderNodeValToRGB")
    color_ramp_2.name = "Color Ramp"
    color_ramp_2.color_ramp.color_mode = 'RGB'
    color_ramp_2.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_2.color_ramp.interpolation = 'LINEAR'
    color_ramp_2.color_ramp.elements.remove(color_ramp_2.color_ramp.elements[0])
    color_ramp_2_cre_0 = color_ramp_2.color_ramp.elements[0]
    color_ramp_2_cre_0.position = 0.30181822180747986
    color_ramp_2_cre_0.alpha = 1.0
    color_ramp_2_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_2_cre_1 = color_ramp_2.color_ramp.elements.new(0.3945455849170685)
    color_ramp_2_cre_1.alpha = 1.0
    color_ramp_2_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    noise_texture_001_3 = moonrockshader_004.nodes.new("ShaderNodeTexNoise")
    noise_texture_001_3.name = "Noise Texture.001"
    noise_texture_001_3.noise_dimensions = '4D'
    noise_texture_001_3.noise_type = 'FBM'
    noise_texture_001_3.normalize = True
    noise_texture_001_3.inputs[5].default_value = 2.0
    noise_texture_001_3.inputs[8].default_value = 0.0
    color_ramp_001_4 = moonrockshader_004.nodes.new("ShaderNodeValToRGB")
    color_ramp_001_4.name = "Color Ramp.001"
    color_ramp_001_4.color_ramp.color_mode = 'RGB'
    color_ramp_001_4.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_001_4.color_ramp.interpolation = 'LINEAR'
    color_ramp_001_4.color_ramp.elements.remove(color_ramp_001_4.color_ramp.elements[0])
    color_ramp_001_4_cre_0 = color_ramp_001_4.color_ramp.elements[0]
    color_ramp_001_4_cre_0.position = 0.4054546356201172
    color_ramp_001_4_cre_0.alpha = 1.0
    color_ramp_001_4_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_001_4_cre_1 = color_ramp_001_4.color_ramp.elements.new(0.64090895652771)
    color_ramp_001_4_cre_1.alpha = 1.0
    color_ramp_001_4_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    mix_2 = moonrockshader_004.nodes.new("ShaderNodeMix")
    mix_2.name = "Mix"
    mix_2.blend_type = 'MIX'
    mix_2.clamp_factor = True
    mix_2.clamp_result = False
    mix_2.data_type = 'RGBA'
    mix_2.factor_mode = 'UNIFORM'
    mix_001_4 = moonrockshader_004.nodes.new("ShaderNodeMix")
    mix_001_4.name = "Mix.001"
    mix_001_4.blend_type = 'MIX'
    mix_001_4.clamp_factor = True
    mix_001_4.clamp_result = False
    mix_001_4.data_type = 'RGBA'
    mix_001_4.factor_mode = 'UNIFORM'
    geometry = moonrockshader_004.nodes.new("ShaderNodeNewGeometry")
    geometry.name = "Geometry"
    geometry.outputs[0].hide = True
    geometry.outputs[1].hide = True
    geometry.outputs[2].hide = True
    geometry.outputs[3].hide = True
    geometry.outputs[4].hide = True
    geometry.outputs[5].hide = True
    geometry.outputs[6].hide = True
    geometry.outputs[8].hide = True
    color_ramp_002_2 = moonrockshader_004.nodes.new("ShaderNodeValToRGB")
    color_ramp_002_2.name = "Color Ramp.002"
    color_ramp_002_2.color_ramp.color_mode = 'RGB'
    color_ramp_002_2.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_002_2.color_ramp.interpolation = 'EASE'
    color_ramp_002_2.color_ramp.elements.remove(color_ramp_002_2.color_ramp.elements[0])
    color_ramp_002_2_cre_0 = color_ramp_002_2.color_ramp.elements[0]
    color_ramp_002_2_cre_0.position = 0.5186362266540527
    color_ramp_002_2_cre_0.alpha = 1.0
    color_ramp_002_2_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_002_2_cre_1 = color_ramp_002_2.color_ramp.elements.new(0.6045457124710083)
    color_ramp_002_2_cre_1.alpha = 1.0
    color_ramp_002_2_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    mix_003_3 = moonrockshader_004.nodes.new("ShaderNodeMix")
    mix_003_3.name = "Mix.003"
    mix_003_3.blend_type = 'MIX'
    mix_003_3.clamp_factor = True
    mix_003_3.clamp_result = False
    mix_003_3.data_type = 'RGBA'
    mix_003_3.factor_mode = 'UNIFORM'
    color_ramp_004_1 = moonrockshader_004.nodes.new("ShaderNodeValToRGB")
    color_ramp_004_1.name = "Color Ramp.004"
    color_ramp_004_1.color_ramp.color_mode = 'RGB'
    color_ramp_004_1.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_004_1.color_ramp.interpolation = 'LINEAR'
    color_ramp_004_1.color_ramp.elements.remove(color_ramp_004_1.color_ramp.elements[0])
    color_ramp_004_1_cre_0 = color_ramp_004_1.color_ramp.elements[0]
    color_ramp_004_1_cre_0.position = 0.0
    color_ramp_004_1_cre_0.alpha = 1.0
    color_ramp_004_1_cre_0.color = (0.6514015197753906, 0.6514063477516174, 0.6514060497283936, 1.0)
    color_ramp_004_1_cre_1 = color_ramp_004_1.color_ramp.elements.new(1.0)
    color_ramp_004_1_cre_1.alpha = 1.0
    color_ramp_004_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    noise_texture_003_1 = moonrockshader_004.nodes.new("ShaderNodeTexNoise")
    noise_texture_003_1.name = "Noise Texture.003"
    noise_texture_003_1.noise_dimensions = '4D'
    noise_texture_003_1.noise_type = 'FBM'
    noise_texture_003_1.normalize = True
    noise_texture_003_1.inputs[3].default_value = 15.0
    noise_texture_003_1.inputs[5].default_value = 0.0
    noise_texture_003_1.inputs[8].default_value = 0.0
    bump_001_3 = moonrockshader_004.nodes.new("ShaderNodeBump")
    bump_001_3.name = "Bump.001"
    bump_001_3.invert = False
    bump_001_3.inputs[1].default_value = 1.0
    frame_001_1 = moonrockshader_004.nodes.new("NodeFrame")
    frame_001_1.name = "Frame.001"
    frame_002_1 = moonrockshader_004.nodes.new("NodeFrame")
    frame_002_1.name = "Frame.002"
    frame_1 = moonrockshader_004.nodes.new("NodeFrame")
    frame_1.name = "Frame"
    hue_saturation_value_3 = moonrockshader_004.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_3.name = "Hue/Saturation/Value"
    hue_saturation_value_3.inputs[0].default_value = 0.5
    hue_saturation_value_3.inputs[1].default_value = 1.0
    hue_saturation_value_3.inputs[3].default_value = 1.0
    frame_003_1 = moonrockshader_004.nodes.new("NodeFrame")
    frame_003_1.name = "Frame.003"
    principled_bsdf_4 = moonrockshader_004.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_4.name = "Principled BSDF"
    principled_bsdf_4.distribution = 'MULTI_GGX'
    principled_bsdf_4.subsurface_method = 'RANDOM_WALK'
    principled_bsdf_4.inputs[1].default_value = 0.0
    principled_bsdf_4.inputs[3].default_value = 1.5
    principled_bsdf_4.inputs[4].default_value = 1.0
    principled_bsdf_4.inputs[7].default_value = 0.0
    principled_bsdf_4.inputs[8].default_value = 0.0
    principled_bsdf_4.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    principled_bsdf_4.inputs[10].default_value = 0.05000000074505806
    principled_bsdf_4.inputs[12].default_value = 0.0
    principled_bsdf_4.inputs[13].default_value = 0.5
    principled_bsdf_4.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_4.inputs[15].default_value = 0.0
    principled_bsdf_4.inputs[16].default_value = 0.0
    principled_bsdf_4.inputs[17].default_value = (0.0, 0.0, 0.0)
    principled_bsdf_4.inputs[18].default_value = 0.0
    principled_bsdf_4.inputs[19].default_value = 0.0
    principled_bsdf_4.inputs[20].default_value = 0.029999999329447746
    principled_bsdf_4.inputs[21].default_value = 1.5
    principled_bsdf_4.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_4.inputs[23].default_value = (0.0, 0.0, 0.0)
    principled_bsdf_4.inputs[24].default_value = 0.0
    principled_bsdf_4.inputs[25].default_value = 0.5
    principled_bsdf_4.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_4.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_4.inputs[28].default_value = 0.0
    principled_bsdf_4.inputs[29].default_value = 0.0
    principled_bsdf_4.inputs[30].default_value = 1.3300000429153442
    math_4 = moonrockshader_004.nodes.new("ShaderNodeMath")
    math_4.name = "Math"
    math_4.operation = 'MULTIPLY'
    math_4.use_clamp = False
    math_4.inputs[1].default_value = 10.0
    group_001_4 = moonrockshader_004.nodes.new("ShaderNodeGroup")
    group_001_4.name = "Group.001"
    group_001_4.node_tree = random_x4___mat_005
    group_001_4.inputs[0].default_value = 0.5213124752044678
    voronoi_texture_4 = moonrockshader_004.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_4.name = "Voronoi Texture"
    voronoi_texture_4.distance = 'EUCLIDEAN'
    voronoi_texture_4.feature = 'F1'
    voronoi_texture_4.normalize = True
    voronoi_texture_4.voronoi_dimensions = '4D'
    voronoi_texture_4.inputs[3].default_value = 0.0
    voronoi_texture_4.inputs[4].default_value = 1.0
    voronoi_texture_4.inputs[5].default_value = 2.0
    voronoi_texture_4.inputs[8].default_value = 1.0
    bump_002_3 = moonrockshader_004.nodes.new("ShaderNodeBump")
    bump_002_3.name = "Bump.002"
    bump_002_3.invert = False
    bump_002_3.inputs[1].default_value = 1.0
    color_ramp_005_1 = moonrockshader_004.nodes.new("ShaderNodeValToRGB")
    color_ramp_005_1.name = "Color Ramp.005"
    color_ramp_005_1.color_ramp.color_mode = 'RGB'
    color_ramp_005_1.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_005_1.color_ramp.interpolation = 'EASE'
    color_ramp_005_1.color_ramp.elements.remove(color_ramp_005_1.color_ramp.elements[0])
    color_ramp_005_1_cre_0 = color_ramp_005_1.color_ramp.elements[0]
    color_ramp_005_1_cre_0.position = 0.0
    color_ramp_005_1_cre_0.alpha = 1.0
    color_ramp_005_1_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_005_1_cre_1 = color_ramp_005_1.color_ramp.elements.new(0.15909108519554138)
    color_ramp_005_1_cre_1.alpha = 1.0
    color_ramp_005_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    voronoi_texture_001_1 = moonrockshader_004.nodes.new("ShaderNodeTexVoronoi")
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
    color_ramp_006_1 = moonrockshader_004.nodes.new("ShaderNodeValToRGB")
    color_ramp_006_1.name = "Color Ramp.006"
    color_ramp_006_1.color_ramp.color_mode = 'RGB'
    color_ramp_006_1.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_006_1.color_ramp.interpolation = 'CARDINAL'
    color_ramp_006_1.color_ramp.elements.remove(color_ramp_006_1.color_ramp.elements[0])
    color_ramp_006_1_cre_0 = color_ramp_006_1.color_ramp.elements[0]
    color_ramp_006_1_cre_0.position = 0.0
    color_ramp_006_1_cre_0.alpha = 1.0
    color_ramp_006_1_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_006_1_cre_1 = color_ramp_006_1.color_ramp.elements.new(0.13181859254837036)
    color_ramp_006_1_cre_1.alpha = 1.0
    color_ramp_006_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    math_001_2 = moonrockshader_004.nodes.new("ShaderNodeMath")
    math_001_2.name = "Math.001"
    math_001_2.operation = 'DIVIDE'
    math_001_2.use_clamp = False
    bump_003_1 = moonrockshader_004.nodes.new("ShaderNodeBump")
    bump_003_1.name = "Bump.003"
    bump_003_1.invert = False
    bump_003_1.inputs[1].default_value = 1.0
    bump_003_1.inputs[3].default_value = (0.0, 0.0, 0.0)
    map_range_004_4 = moonrockshader_004.nodes.new("ShaderNodeMapRange")
    map_range_004_4.name = "Map Range.004"
    map_range_004_4.clamp = True
    map_range_004_4.data_type = 'FLOAT'
    map_range_004_4.interpolation_type = 'LINEAR'
    map_range_004_4.inputs[1].default_value = 0.0
    map_range_004_4.inputs[2].default_value = 1.0
    map_range_004_4.inputs[3].default_value = -1000.0
    map_range_004_4.inputs[4].default_value = 1000.0
    group_002 = moonrockshader_004.nodes.new("ShaderNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = random_x4___mat_005
    math_002_1 = moonrockshader_004.nodes.new("ShaderNodeMath")
    math_002_1.name = "Math.002"
    math_002_1.operation = 'MULTIPLY'
    math_002_1.use_clamp = False
    math_003_1 = moonrockshader_004.nodes.new("ShaderNodeMath")
    math_003_1.name = "Math.003"
    math_003_1.operation = 'MULTIPLY'
    math_003_1.use_clamp = False
    math_003_1.inputs[1].default_value = 5.0
    math_004 = moonrockshader_004.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'MULTIPLY'
    math_004.use_clamp = False
    moonrockshader_004.links.new(mapping_001.outputs[0], noise_texture_001_3.inputs[0])
    moonrockshader_004.links.new(noise_texture_001_3.outputs[0], color_ramp_001_4.inputs[0])
    moonrockshader_004.links.new(color_ramp_001_4.outputs[0], mix_2.inputs[7])
    moonrockshader_004.links.new(color_ramp_004_1.outputs[0], hue_saturation_value_3.inputs[4])
    moonrockshader_004.links.new(mix_001_4.outputs[2], mix_003_3.inputs[6])
    moonrockshader_004.links.new(mix_003_3.outputs[2], principled_bsdf_4.inputs[0])
    moonrockshader_004.links.new(color_ramp_002_2.outputs[0], mix_003_3.inputs[0])
    moonrockshader_004.links.new(hue_saturation_value_3.outputs[0], principled_bsdf_4.inputs[2])
    moonrockshader_004.links.new(color_ramp_2.outputs[0], mix_2.inputs[6])
    moonrockshader_004.links.new(mix_2.outputs[2], color_ramp_004_1.inputs[0])
    moonrockshader_004.links.new(mapping_001.outputs[0], noise_texture_003_1.inputs[0])
    moonrockshader_004.links.new(bump_4.outputs[0], bump_001_3.inputs[3])
    moonrockshader_004.links.new(mix_2.outputs[2], mix_001_4.inputs[0])
    moonrockshader_004.links.new(mapping_001.outputs[0], noise_texture_4.inputs[0])
    moonrockshader_004.links.new(geometry.outputs[7], color_ramp_002_2.inputs[0])
    moonrockshader_004.links.new(mix_2.outputs[2], bump_001_3.inputs[2])
    moonrockshader_004.links.new(noise_texture_4.outputs[0], color_ramp_2.inputs[0])
    moonrockshader_004.links.new(texture_coordinate_001.outputs[3], mapping_001.inputs[0])
    moonrockshader_004.links.new(principled_bsdf_4.outputs[0], group_output_7.inputs[0])
    moonrockshader_004.links.new(group_input_7.outputs[0], mapping_001.inputs[3])
    moonrockshader_004.links.new(group_input_7.outputs[1], mix_001_4.inputs[6])
    moonrockshader_004.links.new(group_input_7.outputs[2], mix_001_4.inputs[7])
    moonrockshader_004.links.new(group_input_7.outputs[3], mix_003_3.inputs[7])
    moonrockshader_004.links.new(group_input_7.outputs[5], noise_texture_4.inputs[3])
    moonrockshader_004.links.new(group_input_7.outputs[6], noise_texture_4.inputs[4])
    moonrockshader_004.links.new(group_input_7.outputs[5], noise_texture_001_3.inputs[3])
    moonrockshader_004.links.new(group_input_7.outputs[6], noise_texture_001_3.inputs[4])
    moonrockshader_004.links.new(group_input_7.outputs[9], hue_saturation_value_3.inputs[2])
    moonrockshader_004.links.new(group_input_7.outputs[11], bump_4.inputs[0])
    moonrockshader_004.links.new(group_input_7.outputs[10], noise_texture_003_1.inputs[2])
    moonrockshader_004.links.new(group_input_7.outputs[12], bump_001_3.inputs[0])
    moonrockshader_004.links.new(group_input_7.outputs[4], noise_texture_001_3.inputs[2])
    moonrockshader_004.links.new(group_input_7.outputs[14], mix_2.inputs[0])
    moonrockshader_004.links.new(group_input_7.outputs[4], math_4.inputs[0])
    moonrockshader_004.links.new(math_4.outputs[0], noise_texture_4.inputs[2])
    moonrockshader_004.links.new(group_input_7.outputs[15], noise_texture_003_1.inputs[4])
    moonrockshader_004.links.new(group_001_4.outputs[4], noise_texture_001_3.inputs[1])
    moonrockshader_004.links.new(group_001_4.outputs[3], noise_texture_4.inputs[1])
    moonrockshader_004.links.new(group_001_4.outputs[1], noise_texture_003_1.inputs[1])
    moonrockshader_004.links.new(bump_001_3.outputs[0], principled_bsdf_4.inputs[5])
    moonrockshader_004.links.new(noise_texture_003_1.outputs[0], bump_4.inputs[2])
    moonrockshader_004.links.new(mapping_001.outputs[0], voronoi_texture_4.inputs[0])
    moonrockshader_004.links.new(group_001_4.outputs[1], voronoi_texture_4.inputs[1])
    moonrockshader_004.links.new(color_ramp_005_1.outputs[0], bump_002_3.inputs[2])
    moonrockshader_004.links.new(bump_002_3.outputs[0], bump_4.inputs[3])
    moonrockshader_004.links.new(voronoi_texture_4.outputs[0], color_ramp_005_1.inputs[0])
    moonrockshader_004.links.new(group_input_7.outputs[16], voronoi_texture_4.inputs[2])
    moonrockshader_004.links.new(mapping_001.outputs[0], voronoi_texture_001_1.inputs[0])
    moonrockshader_004.links.new(group_001_4.outputs[1], voronoi_texture_001_1.inputs[1])
    moonrockshader_004.links.new(math_001_2.outputs[0], voronoi_texture_001_1.inputs[2])
    moonrockshader_004.links.new(voronoi_texture_001_1.outputs[0], color_ramp_006_1.inputs[0])
    moonrockshader_004.links.new(group_input_7.outputs[16], math_001_2.inputs[0])
    moonrockshader_004.links.new(color_ramp_006_1.outputs[0], bump_003_1.inputs[2])
    moonrockshader_004.links.new(bump_003_1.outputs[0], bump_002_3.inputs[3])
    moonrockshader_004.links.new(map_range_004_4.outputs[0], mapping_001.inputs[1])
    moonrockshader_004.links.new(group_001_4.outputs[0], map_range_004_4.inputs[0])
    moonrockshader_004.links.new(group_002.outputs[0], math_002_1.inputs[1])
    moonrockshader_004.links.new(group_input_7.outputs[17], math_002_1.inputs[0])
    moonrockshader_004.links.new(math_002_1.outputs[0], bump_003_1.inputs[0])
    moonrockshader_004.links.new(group_001_4.outputs[2], group_002.inputs[0])
    moonrockshader_004.links.new(math_003_1.outputs[0], math_001_2.inputs[1])
    moonrockshader_004.links.new(group_002.outputs[1], math_003_1.inputs[0])
    moonrockshader_004.links.new(group_input_7.outputs[17], math_004.inputs[0])
    moonrockshader_004.links.new(group_002.outputs[2], math_004.inputs[1])
    moonrockshader_004.links.new(math_004.outputs[0], bump_002_3.inputs[0])
    return moonrockshader_004

moonrockshader_004 = moonrockshader_004_node_group()

def moonsurfaceshader_node_group():
    moonsurfaceshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "MoonSurfaceShader")
    moonsurfaceshader.color_tag = 'NONE'
    moonsurfaceshader.default_group_node_width = 140
    shader_socket_1 = moonsurfaceshader.interface.new_socket(name = "Shader", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    shader_socket_1.attribute_domain = 'POINT'
    group_output_8 = moonsurfaceshader.nodes.new("NodeGroupOutput")
    group_output_8.name = "Group Output"
    group_output_8.is_active_output = True
    group_input_8 = moonsurfaceshader.nodes.new("NodeGroupInput")
    group_input_8.name = "Group Input"
    mix_shader = moonsurfaceshader.nodes.new("ShaderNodeMixShader")
    mix_shader.name = "Mix Shader"
    geometry_1 = moonsurfaceshader.nodes.new("ShaderNodeNewGeometry")
    geometry_1.name = "Geometry"
    color_ramp_3 = moonsurfaceshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_3.name = "Color Ramp"
    color_ramp_3.color_ramp.color_mode = 'RGB'
    color_ramp_3.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_3.color_ramp.interpolation = 'CARDINAL'
    color_ramp_3.color_ramp.elements.remove(color_ramp_3.color_ramp.elements[0])
    color_ramp_3_cre_0 = color_ramp_3.color_ramp.elements[0]
    color_ramp_3_cre_0.position = 0.5818178653717041
    color_ramp_3_cre_0.alpha = 1.0
    color_ramp_3_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_3_cre_1 = color_ramp_3.color_ramp.elements.new(0.9000000953674316)
    color_ramp_3_cre_1.alpha = 1.0
    color_ramp_3_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    mapping_001_1 = moonsurfaceshader.nodes.new("ShaderNodeMapping")
    mapping_001_1.name = "Mapping.001"
    mapping_001_1.vector_type = 'POINT'
    mapping_001_1.inputs[2].default_value = (0.0, 0.0, 0.0)
    mapping_001_1.inputs[3].default_value = (1.0, 1.0, 1.0)
    texture_coordinate_001_1 = moonsurfaceshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_001_1.name = "Texture Coordinate.001"
    texture_coordinate_001_1.from_instancer = False
    texture_coordinate_001_1.outputs[0].hide = True
    texture_coordinate_001_1.outputs[1].hide = True
    texture_coordinate_001_1.outputs[2].hide = True
    texture_coordinate_001_1.outputs[4].hide = True
    texture_coordinate_001_1.outputs[5].hide = True
    texture_coordinate_001_1.outputs[6].hide = True
    noise_texture_002_1 = moonsurfaceshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_002_1.name = "Noise Texture.002"
    noise_texture_002_1.noise_dimensions = '3D'
    noise_texture_002_1.noise_type = 'FBM'
    noise_texture_002_1.normalize = True
    noise_texture_002_1.inputs[3].default_value = 15.0
    noise_texture_002_1.inputs[4].default_value = 0.6000000238418579
    noise_texture_002_1.inputs[5].default_value = 2.5
    noise_texture_002_1.inputs[8].default_value = 0.25
    color_ramp_003_1 = moonsurfaceshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_003_1.name = "Color Ramp.003"
    color_ramp_003_1.color_ramp.color_mode = 'RGB'
    color_ramp_003_1.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_003_1.color_ramp.interpolation = 'EASE'
    color_ramp_003_1.color_ramp.elements.remove(color_ramp_003_1.color_ramp.elements[0])
    color_ramp_003_1_cre_0 = color_ramp_003_1.color_ramp.elements[0]
    color_ramp_003_1_cre_0.position = 0.5018180012702942
    color_ramp_003_1_cre_0.alpha = 1.0
    color_ramp_003_1_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_003_1_cre_1 = color_ramp_003_1.color_ramp.elements.new(0.7140910029411316)
    color_ramp_003_1_cre_1.alpha = 1.0
    color_ramp_003_1_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    mix_002_2 = moonsurfaceshader.nodes.new("ShaderNodeMix")
    mix_002_2.name = "Mix.002"
    mix_002_2.blend_type = 'LINEAR_LIGHT'
    mix_002_2.clamp_factor = True
    mix_002_2.clamp_result = False
    mix_002_2.data_type = 'RGBA'
    mix_002_2.factor_mode = 'UNIFORM'
    math_5 = moonsurfaceshader.nodes.new("ShaderNodeMath")
    math_5.name = "Math"
    math_5.operation = 'ADD'
    math_5.use_clamp = False
    separate_xyz = moonsurfaceshader.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.outputs[2].hide = True
    mix_3 = moonsurfaceshader.nodes.new("ShaderNodeMix")
    mix_3.name = "Mix"
    mix_3.blend_type = 'MIX'
    mix_3.clamp_factor = True
    mix_3.clamp_result = False
    mix_3.data_type = 'FLOAT'
    mix_3.factor_mode = 'UNIFORM'
    mix_3.inputs[0].hide = True
    mix_3.inputs[1].hide = True
    mix_3.inputs[4].hide = True
    mix_3.inputs[5].hide = True
    mix_3.inputs[6].hide = True
    mix_3.inputs[7].hide = True
    mix_3.inputs[8].hide = True
    mix_3.inputs[9].hide = True
    mix_3.outputs[1].hide = True
    mix_3.outputs[2].hide = True
    mix_3.outputs[3].hide = True
    mix_3.inputs[0].default_value = 0.5
    vector_math = moonsurfaceshader.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'ABSOLUTE'
    math_001_3 = moonsurfaceshader.nodes.new("ShaderNodeMath")
    math_001_3.name = "Math.001"
    math_001_3.operation = 'MULTIPLY'
    math_001_3.use_clamp = False
    math_001_3.inputs[1].default_value = 0.5
    map_range_1 = moonsurfaceshader.nodes.new("ShaderNodeMapRange")
    map_range_1.name = "Map Range"
    map_range_1.clamp = True
    map_range_1.data_type = 'FLOAT'
    map_range_1.interpolation_type = 'LINEAR'
    map_range_1.inputs[1].default_value = 0.0
    map_range_1.inputs[2].default_value = 1.0
    map_range_1.inputs[3].default_value = 0.03333333507180214
    map_range_1.inputs[4].default_value = 0.10000000149011612
    map_range_001 = moonsurfaceshader.nodes.new("ShaderNodeMapRange")
    map_range_001.name = "Map Range.001"
    map_range_001.clamp = True
    map_range_001.data_type = 'FLOAT'
    map_range_001.interpolation_type = 'LINEAR'
    map_range_001.inputs[1].default_value = 0.0
    map_range_001.inputs[2].default_value = 1.0
    map_range_001.inputs[3].default_value = 0.4000000059604645
    map_range_001.inputs[4].default_value = 0.6000000238418579
    group_002_1 = moonsurfaceshader.nodes.new("ShaderNodeGroup")
    group_002_1.name = "Group.002"
    group_002_1.node_tree = rockygroundshader_002
    group_002_1.inputs[0].default_value = 1.0
    group_002_1.inputs[1].default_value = 1.0
    group_002_1.inputs[4].default_value = 0.5
    group_002_1.inputs[5].default_value = 0.25
    group_002_1.inputs[6].default_value = 5.0
    group_002_1.inputs[10].default_value = 1.0
    group_002_1.inputs[11].default_value = 0.10000000149011612
    group_002_1.inputs[12].default_value = 0.25
    group_002_1.inputs[13].default_value = 0.4000000059604645
    group_003 = moonsurfaceshader.nodes.new("ShaderNodeGroup")
    group_003.name = "Group.003"
    group_003.node_tree = lunarsurfaceshader
    group_003.inputs[0].default_value = 2.5
    group_003.inputs[1].default_value = 5.0
    group_003.inputs[2].default_value = 7.5
    group_003.inputs[5].default_value = 1.1099998950958252
    group_003.inputs[6].default_value = 0.75
    group_003.inputs[7].default_value = 15.0
    group_003.inputs[8].default_value = 0.824999988079071
    group_003.inputs[9].default_value = 15.0
    group_003.inputs[10].default_value = 0.29999998211860657
    group_003.inputs[11].default_value = 1.9999998807907104
    group_003.inputs[12].default_value = 0.07500001788139343
    group_003.inputs[13].default_value = 0.2250000238418579
    group_003.inputs[14].default_value = 0.1666666865348816
    group_007 = moonsurfaceshader.nodes.new("ShaderNodeGroup")
    group_007.name = "Group.007"
    group_007.node_tree = random_x8___mat
    group_007.inputs[0].default_value = 0.5126323103904724
    combine_color_001 = moonsurfaceshader.nodes.new("ShaderNodeCombineColor")
    combine_color_001.name = "Combine Color.001"
    combine_color_001.mode = 'HSV'
    combine_color_001.inputs[0].default_value = 0.0
    combine_color_001.inputs[1].default_value = 0.0
    map_range_005 = moonsurfaceshader.nodes.new("ShaderNodeMapRange")
    map_range_005.name = "Map Range.005"
    map_range_005.clamp = True
    map_range_005.data_type = 'FLOAT'
    map_range_005.interpolation_type = 'LINEAR'
    map_range_005.inputs[1].default_value = 0.0
    map_range_005.inputs[2].default_value = 1.0
    map_range_005.inputs[3].default_value = 0.20000000298023224
    map_range_005.inputs[4].default_value = 0.3499999940395355
    mix_shader_001 = moonsurfaceshader.nodes.new("ShaderNodeMixShader")
    mix_shader_001.name = "Mix Shader.001"
    noise_texture_003_2 = moonsurfaceshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_003_2.name = "Noise Texture.003"
    noise_texture_003_2.noise_dimensions = '3D'
    noise_texture_003_2.noise_type = 'HETERO_TERRAIN'
    noise_texture_003_2.normalize = True
    noise_texture_003_2.inputs[3].default_value = 15.0
    noise_texture_003_2.inputs[4].default_value = 0.5166667103767395
    noise_texture_003_2.inputs[5].default_value = 15.179998397827148
    noise_texture_003_2.inputs[6].default_value = 0.14000000059604645
    noise_texture_003_2.inputs[8].default_value = 0.12000000476837158
    color_ramp_004_2 = moonsurfaceshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_004_2.name = "Color Ramp.004"
    color_ramp_004_2.color_ramp.color_mode = 'RGB'
    color_ramp_004_2.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_004_2.color_ramp.interpolation = 'EASE'
    color_ramp_004_2.color_ramp.elements.remove(color_ramp_004_2.color_ramp.elements[0])
    color_ramp_004_2_cre_0 = color_ramp_004_2.color_ramp.elements[0]
    color_ramp_004_2_cre_0.position = 0.18636341392993927
    color_ramp_004_2_cre_0.alpha = 1.0
    color_ramp_004_2_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_004_2_cre_1 = color_ramp_004_2.color_ramp.elements.new(0.9186362028121948)
    color_ramp_004_2_cre_1.alpha = 1.0
    color_ramp_004_2_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    map_range_002 = moonsurfaceshader.nodes.new("ShaderNodeMapRange")
    map_range_002.name = "Map Range.002"
    map_range_002.clamp = True
    map_range_002.data_type = 'FLOAT'
    map_range_002.interpolation_type = 'LINEAR'
    map_range_002.inputs[1].default_value = 0.0
    map_range_002.inputs[2].default_value = 1.0
    map_range_002.inputs[3].default_value = 0.020000003278255463
    map_range_002.inputs[4].default_value = 0.08000001311302185
    group_004 = moonsurfaceshader.nodes.new("ShaderNodeGroup")
    group_004.name = "Group.004"
    group_004.node_tree = sandshader_002
    group_004.inputs[0].default_value = 4.0
    group_004.inputs[1].default_value = 135.0
    group_004.inputs[2].default_value = 0.800000011920929
    group_004.inputs[6].default_value = 15.0
    group_004.inputs[7].default_value = 1.0
    group_004.inputs[8].default_value = 0.009999999776482582
    group_004.inputs[9].default_value = 0.25
    group_004.inputs[10].default_value = 0.75
    noise_texture_004_1 = moonsurfaceshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_004_1.name = "Noise Texture.004"
    noise_texture_004_1.noise_dimensions = '3D'
    noise_texture_004_1.noise_type = 'RIDGED_MULTIFRACTAL'
    noise_texture_004_1.normalize = True
    noise_texture_004_1.inputs[3].default_value = 15.0
    noise_texture_004_1.inputs[4].default_value = 1.0
    noise_texture_004_1.inputs[5].default_value = 0.0
    noise_texture_004_1.inputs[6].default_value = 0.0
    noise_texture_004_1.inputs[7].default_value = 0.0
    noise_texture_004_1.inputs[8].default_value = 0.25
    map_range_003 = moonsurfaceshader.nodes.new("ShaderNodeMapRange")
    map_range_003.name = "Map Range.003"
    map_range_003.clamp = True
    map_range_003.data_type = 'FLOAT'
    map_range_003.interpolation_type = 'LINEAR'
    map_range_003.inputs[1].default_value = 0.0
    map_range_003.inputs[2].default_value = 1.0
    map_range_003.inputs[3].default_value = 0.019999999552965164
    map_range_003.inputs[4].default_value = 0.03999999910593033
    mix_shader_002 = moonsurfaceshader.nodes.new("ShaderNodeMixShader")
    mix_shader_002.name = "Mix Shader.002"
    group_001_5 = moonsurfaceshader.nodes.new("ShaderNodeGroup")
    group_001_5.name = "Group.001"
    group_001_5.node_tree = smoothrockshader
    group_001_5.inputs[0].default_value = 1.0
    group_001_5.inputs[1].default_value = 0.20000000298023224
    group_001_5.inputs[2].default_value = 0.20000000298023224
    group_001_5.inputs[3].default_value = 3.0
    group_001_5.inputs[6].default_value = 0.699999988079071
    group_001_5.inputs[7].default_value = 0.699999988079071
    group_001_5.inputs[8].default_value = 15.0
    group_001_5.inputs[9].default_value = 4.0
    group_001_5.inputs[10].default_value = 1.0
    group_001_5.inputs[11].default_value = 0.05000000074505806
    noise_texture_005_1 = moonsurfaceshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_005_1.name = "Noise Texture.005"
    noise_texture_005_1.noise_dimensions = '3D'
    noise_texture_005_1.noise_type = 'FBM'
    noise_texture_005_1.normalize = True
    noise_texture_005_1.inputs[3].default_value = 5.0
    noise_texture_005_1.inputs[4].default_value = 0.6670835614204407
    noise_texture_005_1.inputs[5].default_value = 5.0
    noise_texture_005_1.inputs[8].default_value = 0.10000000149011612
    color_ramp_006_2 = moonsurfaceshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_006_2.name = "Color Ramp.006"
    color_ramp_006_2.color_ramp.color_mode = 'RGB'
    color_ramp_006_2.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_006_2.color_ramp.interpolation = 'EASE'
    color_ramp_006_2.color_ramp.elements.remove(color_ramp_006_2.color_ramp.elements[0])
    color_ramp_006_2_cre_0 = color_ramp_006_2.color_ramp.elements[0]
    color_ramp_006_2_cre_0.position = 0.5681818127632141
    color_ramp_006_2_cre_0.alpha = 1.0
    color_ramp_006_2_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_006_2_cre_1 = color_ramp_006_2.color_ramp.elements.new(0.7000001072883606)
    color_ramp_006_2_cre_1.alpha = 1.0
    color_ramp_006_2_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    map_range_007 = moonsurfaceshader.nodes.new("ShaderNodeMapRange")
    map_range_007.name = "Map Range.007"
    map_range_007.clamp = True
    map_range_007.data_type = 'FLOAT'
    map_range_007.interpolation_type = 'LINEAR'
    map_range_007.inputs[1].default_value = 0.0
    map_range_007.inputs[2].default_value = 1.0
    map_range_007.inputs[3].default_value = 0.02500000037252903
    map_range_007.inputs[4].default_value = 0.07500000298023224
    mix_shader_003 = moonsurfaceshader.nodes.new("ShaderNodeMixShader")
    mix_shader_003.name = "Mix Shader.003"
    combine_color_002 = moonsurfaceshader.nodes.new("ShaderNodeCombineColor")
    combine_color_002.name = "Combine Color.002"
    combine_color_002.mode = 'HSV'
    combine_color_002.inputs[0].default_value = 0.0
    combine_color_002.inputs[1].default_value = 0.0
    map_range_006 = moonsurfaceshader.nodes.new("ShaderNodeMapRange")
    map_range_006.name = "Map Range.006"
    map_range_006.clamp = True
    map_range_006.data_type = 'FLOAT'
    map_range_006.interpolation_type = 'LINEAR'
    map_range_006.inputs[1].default_value = 0.0
    map_range_006.inputs[2].default_value = 1.0
    map_range_006.inputs[3].default_value = 0.17499999701976776
    map_range_006.inputs[4].default_value = 0.25
    combine_color_003 = moonsurfaceshader.nodes.new("ShaderNodeCombineColor")
    combine_color_003.name = "Combine Color.003"
    combine_color_003.mode = 'HSV'
    combine_color_003.inputs[0].default_value = 0.0
    combine_color_003.inputs[1].default_value = 0.0
    map_range_008 = moonsurfaceshader.nodes.new("ShaderNodeMapRange")
    map_range_008.name = "Map Range.008"
    map_range_008.clamp = True
    map_range_008.data_type = 'FLOAT'
    map_range_008.interpolation_type = 'LINEAR'
    map_range_008.inputs[1].default_value = 0.0
    map_range_008.inputs[2].default_value = 1.0
    map_range_008.inputs[3].default_value = 0.10000000149011612
    map_range_008.inputs[4].default_value = 0.17499999701976776
    combine_color_004 = moonsurfaceshader.nodes.new("ShaderNodeCombineColor")
    combine_color_004.name = "Combine Color.004"
    combine_color_004.mode = 'HSV'
    combine_color_004.inputs[0].default_value = 0.0
    combine_color_004.inputs[1].default_value = 0.0
    map_range_009 = moonsurfaceshader.nodes.new("ShaderNodeMapRange")
    map_range_009.name = "Map Range.009"
    map_range_009.clamp = True
    map_range_009.data_type = 'FLOAT'
    map_range_009.interpolation_type = 'LINEAR'
    map_range_009.inputs[1].default_value = 0.0
    map_range_009.inputs[2].default_value = 1.0
    map_range_009.inputs[3].default_value = 0.02500000037252903
    map_range_009.inputs[4].default_value = 0.10000000149011612
    combine_color_005 = moonsurfaceshader.nodes.new("ShaderNodeCombineColor")
    combine_color_005.name = "Combine Color.005"
    combine_color_005.mode = 'HSV'
    combine_color_005.inputs[0].default_value = 0.0
    combine_color_005.inputs[1].default_value = 0.0
    map_range_010 = moonsurfaceshader.nodes.new("ShaderNodeMapRange")
    map_range_010.name = "Map Range.010"
    map_range_010.clamp = True
    map_range_010.data_type = 'FLOAT'
    map_range_010.interpolation_type = 'LINEAR'
    map_range_010.inputs[1].default_value = 0.0
    map_range_010.inputs[2].default_value = 1.0
    map_range_010.inputs[3].default_value = 0.0
    map_range_010.inputs[4].default_value = 0.02500000037252903
    mix_shader_004 = moonsurfaceshader.nodes.new("ShaderNodeMixShader")
    mix_shader_004.name = "Mix Shader.004"
    map_range_011 = moonsurfaceshader.nodes.new("ShaderNodeMapRange")
    map_range_011.name = "Map Range.011"
    map_range_011.clamp = True
    map_range_011.data_type = 'FLOAT'
    map_range_011.interpolation_type = 'LINEAR'
    map_range_011.inputs[1].default_value = 0.0
    map_range_011.inputs[2].default_value = 1.0
    map_range_011.inputs[3].default_value = -1000.0
    map_range_011.inputs[4].default_value = 1000.0
    group = moonsurfaceshader.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = random_x2___mat_003
    group_008 = moonsurfaceshader.nodes.new("ShaderNodeGroup")
    group_008.name = "Group.008"
    group_008.node_tree = moonrockshader_004
    group_008.inputs[0].default_value = 4.0
    group_008.inputs[4].default_value = 7.0
    group_008.inputs[5].default_value = 15.0
    group_008.inputs[6].default_value = 0.25
    group_008.inputs[7].default_value = 5.0
    group_008.inputs[8].default_value = 0.800000011920929
    group_008.inputs[9].default_value = 1.0
    group_008.inputs[10].default_value = 15.0
    group_008.inputs[11].default_value = 0.05000000074505806
    group_008.inputs[12].default_value = 0.25
    group_008.inputs[13].default_value = 0.75
    group_008.inputs[14].default_value = 0.009999999776482582
    group_008.inputs[15].default_value = 1.0
    group_008.inputs[16].default_value = 20.0
    group_008.inputs[17].default_value = 0.75
    moonsurfaceshader.links.new(texture_coordinate_001_1.outputs[3], mapping_001_1.inputs[0])
    moonsurfaceshader.links.new(combine_color_005.outputs[0], group_001_5.inputs[4])
    moonsurfaceshader.links.new(color_ramp_3.outputs[0], mix_002_2.inputs[6])
    moonsurfaceshader.links.new(combine_color_004.outputs[0], group_001_5.inputs[5])
    moonsurfaceshader.links.new(vector_math.outputs[0], separate_xyz.inputs[0])
    moonsurfaceshader.links.new(map_range_007.outputs[0], noise_texture_005_1.inputs[2])
    moonsurfaceshader.links.new(geometry_1.outputs[7], math_5.inputs[1])
    moonsurfaceshader.links.new(group_007.outputs[0], map_range_011.inputs[0])
    moonsurfaceshader.links.new(math_5.outputs[0], color_ramp_3.inputs[0])
    moonsurfaceshader.links.new(group_004.outputs[0], mix_shader_004.inputs[2])
    moonsurfaceshader.links.new(separate_xyz.outputs[0], mix_3.inputs[2])
    moonsurfaceshader.links.new(color_ramp_004_2.outputs[0], mix_shader_004.inputs[0])
    moonsurfaceshader.links.new(separate_xyz.outputs[1], mix_3.inputs[3])
    moonsurfaceshader.links.new(mix_shader_004.outputs[0], mix_shader_001.inputs[2])
    moonsurfaceshader.links.new(math_001_3.outputs[0], math_5.inputs[0])
    moonsurfaceshader.links.new(mix_shader_003.outputs[0], mix_shader_001.inputs[1])
    moonsurfaceshader.links.new(geometry_1.outputs[1], vector_math.inputs[0])
    moonsurfaceshader.links.new(group_001_5.outputs[0], mix_shader_002.inputs[2])
    moonsurfaceshader.links.new(mix_3.outputs[0], math_001_3.inputs[0])
    moonsurfaceshader.links.new(group_004.outputs[0], mix_shader_003.inputs[2])
    moonsurfaceshader.links.new(map_range_1.outputs[0], noise_texture_002_1.inputs[2])
    moonsurfaceshader.links.new(color_ramp_006_2.outputs[0], mix_shader_003.inputs[0])
    moonsurfaceshader.links.new(map_range_001.outputs[0], mix_002_2.inputs[0])
    moonsurfaceshader.links.new(noise_texture_004_1.outputs[0], mix_shader_002.inputs[0])
    moonsurfaceshader.links.new(map_range_005.outputs[0], combine_color_001.inputs[2])
    moonsurfaceshader.links.new(color_ramp_004_2.outputs[0], mix_shader.inputs[0])
    moonsurfaceshader.links.new(noise_texture_003_2.outputs[0], color_ramp_004_2.inputs[0])
    moonsurfaceshader.links.new(group_003.outputs[0], mix_shader.inputs[1])
    moonsurfaceshader.links.new(mapping_001_1.outputs[0], noise_texture_003_2.inputs[0])
    moonsurfaceshader.links.new(group_002_1.outputs[0], mix_shader.inputs[2])
    moonsurfaceshader.links.new(map_range_002.outputs[0], noise_texture_003_2.inputs[2])
    moonsurfaceshader.links.new(mix_002_2.outputs[2], mix_shader_001.inputs[0])
    moonsurfaceshader.links.new(group_007.outputs[7], map_range_006.inputs[0])
    moonsurfaceshader.links.new(mapping_001_1.outputs[0], noise_texture_004_1.inputs[0])
    moonsurfaceshader.links.new(group.outputs[0], map_range_008.inputs[0])
    moonsurfaceshader.links.new(mix_shader.outputs[0], mix_shader_002.inputs[1])
    moonsurfaceshader.links.new(group.outputs[1], map_range_009.inputs[0])
    moonsurfaceshader.links.new(map_range_011.outputs[0], mapping_001_1.inputs[1])
    moonsurfaceshader.links.new(group.outputs[2], map_range_010.inputs[0])
    moonsurfaceshader.links.new(group_007.outputs[1], map_range_001.inputs[0])
    moonsurfaceshader.links.new(group_007.outputs[8], group.inputs[0])
    moonsurfaceshader.links.new(group_007.outputs[2], map_range_002.inputs[0])
    moonsurfaceshader.links.new(group_008.outputs[0], mix_shader_004.inputs[1])
    moonsurfaceshader.links.new(group_007.outputs[4], map_range_003.inputs[0])
    moonsurfaceshader.links.new(combine_color_001.outputs[0], group_008.inputs[3])
    moonsurfaceshader.links.new(group_007.outputs[3], map_range_1.inputs[0])
    moonsurfaceshader.links.new(combine_color_005.outputs[0], group_008.inputs[2])
    moonsurfaceshader.links.new(noise_texture_005_1.outputs[0], color_ramp_006_2.inputs[0])
    moonsurfaceshader.links.new(combine_color_004.outputs[0], group_008.inputs[1])
    moonsurfaceshader.links.new(mapping_001_1.outputs[0], noise_texture_005_1.inputs[0])
    moonsurfaceshader.links.new(map_range_003.outputs[0], noise_texture_004_1.inputs[2])
    moonsurfaceshader.links.new(group_007.outputs[5], map_range_007.inputs[0])
    moonsurfaceshader.links.new(mix_shader_002.outputs[0], mix_shader_003.inputs[1])
    moonsurfaceshader.links.new(group_007.outputs[6], map_range_005.inputs[0])
    moonsurfaceshader.links.new(map_range_006.outputs[0], combine_color_002.inputs[2])
    moonsurfaceshader.links.new(map_range_008.outputs[0], combine_color_003.inputs[2])
    moonsurfaceshader.links.new(map_range_009.outputs[0], combine_color_004.inputs[2])
    moonsurfaceshader.links.new(map_range_010.outputs[0], combine_color_005.inputs[2])
    moonsurfaceshader.links.new(combine_color_001.outputs[0], group_002_1.inputs[2])
    moonsurfaceshader.links.new(combine_color_003.outputs[0], group_002_1.inputs[3])
    moonsurfaceshader.links.new(combine_color_002.outputs[0], group_002_1.inputs[7])
    moonsurfaceshader.links.new(combine_color_005.outputs[0], group_002_1.inputs[9])
    moonsurfaceshader.links.new(combine_color_004.outputs[0], group_002_1.inputs[8])
    moonsurfaceshader.links.new(combine_color_004.outputs[0], group_003.inputs[4])
    moonsurfaceshader.links.new(combine_color_003.outputs[0], group_003.inputs[3])
    moonsurfaceshader.links.new(noise_texture_002_1.outputs[0], color_ramp_003_1.inputs[0])
    moonsurfaceshader.links.new(combine_color_004.outputs[0], group_004.inputs[4])
    moonsurfaceshader.links.new(color_ramp_003_1.outputs[0], mix_002_2.inputs[7])
    moonsurfaceshader.links.new(combine_color_005.outputs[0], group_004.inputs[3])
    moonsurfaceshader.links.new(mapping_001_1.outputs[0], noise_texture_002_1.inputs[0])
    moonsurfaceshader.links.new(combine_color_003.outputs[0], group_004.inputs[5])
    moonsurfaceshader.links.new(mix_shader_001.outputs[0], group_output_8.inputs[0])
    return moonsurfaceshader

moonsurfaceshader = moonsurfaceshader_node_group()

def moonsurfacemat_node_group():
    moonsurfacemat = mat.node_tree
    for node in moonsurfacemat.nodes:
        moonsurfacemat.nodes.remove(node)
    moonsurfacemat.color_tag = 'NONE'
    moonsurfacemat.default_group_node_width = 140
    material_output = moonsurfacemat.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    material_output.inputs[3].default_value = 0.0
    group_005 = moonsurfacemat.nodes.new("ShaderNodeGroup")
    group_005.name = "Group.005"
    group_005.node_tree = moonsurfaceshader
    moonsurfacemat.links.new(group_005.outputs[0], material_output.inputs[0])
    return moonsurfacemat

moonsurfacemat = moonsurfacemat_node_group()


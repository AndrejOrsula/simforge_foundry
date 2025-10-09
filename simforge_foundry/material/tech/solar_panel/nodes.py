import bpy, mathutils

mat = bpy.data.materials.new(name = "SolarPanelMat")
mat.use_nodes = True
#initialize Random x4 | Mat.006 node group
def random_x4___mat_006_node_group():

    random_x4___mat_006 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "Random x4 | Mat.006")

    random_x4___mat_006.color_tag = 'NONE'
    random_x4___mat_006.description = ""
    random_x4___mat_006.default_group_node_width = 140
    

    #random_x4___mat_006 interface
    #Socket 0
    _0_socket = random_x4___mat_006.interface.new_socket(name = "0", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _0_socket.default_value = 0.0
    _0_socket.min_value = 0.0
    _0_socket.max_value = 1.0
    _0_socket.subtype = 'NONE'
    _0_socket.attribute_domain = 'POINT'
    _0_socket.default_input = 'VALUE'
    _0_socket.structure_type = 'AUTO'

    #Socket 1
    _1_socket = random_x4___mat_006.interface.new_socket(name = "1", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _1_socket.default_value = 0.0
    _1_socket.min_value = 0.0
    _1_socket.max_value = 1.0
    _1_socket.subtype = 'NONE'
    _1_socket.attribute_domain = 'POINT'
    _1_socket.default_input = 'VALUE'
    _1_socket.structure_type = 'AUTO'

    #Socket 2
    _2_socket = random_x4___mat_006.interface.new_socket(name = "2", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _2_socket.default_value = 0.0
    _2_socket.min_value = 0.0
    _2_socket.max_value = 1.0
    _2_socket.subtype = 'NONE'
    _2_socket.attribute_domain = 'POINT'
    _2_socket.default_input = 'VALUE'
    _2_socket.structure_type = 'AUTO'

    #Socket 3
    _3_socket = random_x4___mat_006.interface.new_socket(name = "3", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _3_socket.default_value = 0.0
    _3_socket.min_value = 0.0
    _3_socket.max_value = 1.0
    _3_socket.subtype = 'NONE'
    _3_socket.attribute_domain = 'POINT'
    _3_socket.default_input = 'VALUE'
    _3_socket.structure_type = 'AUTO'

    #Socket 4
    _4_socket = random_x4___mat_006.interface.new_socket(name = "4", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _4_socket.default_value = 0.0
    _4_socket.min_value = -3.4028234663852886e+38
    _4_socket.max_value = 3.4028234663852886e+38
    _4_socket.subtype = 'NONE'
    _4_socket.attribute_domain = 'POINT'
    _4_socket.default_input = 'VALUE'
    _4_socket.structure_type = 'AUTO'

    #Socket Seed
    seed_socket = random_x4___mat_006.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketFloat')
    seed_socket.default_value = 0.0
    seed_socket.min_value = 0.0
    seed_socket.max_value = 1.0
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'


    #initialize random_x4___mat_006 nodes
    #node Group Output
    group_output = random_x4___mat_006.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = random_x4___mat_006.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Object Info
    object_info = random_x4___mat_006.nodes.new("ShaderNodeObjectInfo")
    object_info.name = "Object Info"

    #node Math
    math = random_x4___mat_006.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'ADD'
    math.use_clamp = False

    #node White Noise Texture
    white_noise_texture = random_x4___mat_006.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture.name = "White Noise Texture"
    white_noise_texture.noise_dimensions = '4D'

    #node Separate Color
    separate_color = random_x4___mat_006.nodes.new("ShaderNodeSeparateColor")
    separate_color.name = "Separate Color"
    separate_color.mode = 'RGB'

    #node Math.001
    math_001 = random_x4___mat_006.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'ADD'
    math_001.use_clamp = False

    #node White Noise Texture.001
    white_noise_texture_001 = random_x4___mat_006.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture_001.name = "White Noise Texture.001"
    white_noise_texture_001.noise_dimensions = '4D'

    #node Separate Color.001
    separate_color_001 = random_x4___mat_006.nodes.new("ShaderNodeSeparateColor")
    separate_color_001.name = "Separate Color.001"
    separate_color_001.mode = 'RGB'


    #Set locations
    group_output.location = (0.0, 0.0)
    group_input.location = (0.0, 0.0)
    object_info.location = (0.0, 0.0)
    math.location = (0.0, 0.0)
    white_noise_texture.location = (0.0, 0.0)
    separate_color.location = (0.0, 0.0)
    math_001.location = (0.0, 0.0)
    white_noise_texture_001.location = (0.0, 0.0)
    separate_color_001.location = (0.0, 0.0)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    object_info.width, object_info.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    white_noise_texture.width, white_noise_texture.height = 140.0, 100.0
    separate_color.width, separate_color.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    white_noise_texture_001.width, white_noise_texture_001.height = 140.0, 100.0
    separate_color_001.width, separate_color_001.height = 140.0, 100.0

    #initialize random_x4___mat_006 links
    #object_info.Random -> white_noise_texture.W
    random_x4___mat_006.links.new(object_info.outputs[5], white_noise_texture.inputs[1])
    #math.Value -> white_noise_texture.Vector
    random_x4___mat_006.links.new(math.outputs[0], white_noise_texture.inputs[0])
    #white_noise_texture.Color -> separate_color.Color
    random_x4___mat_006.links.new(white_noise_texture.outputs[1], separate_color.inputs[0])
    #object_info.Object Index -> math.Value
    random_x4___mat_006.links.new(object_info.outputs[3], math.inputs[1])
    #group_input.Seed -> math.Value
    random_x4___mat_006.links.new(group_input.outputs[0], math.inputs[0])
    #separate_color.Red -> group_output.0
    random_x4___mat_006.links.new(separate_color.outputs[0], group_output.inputs[0])
    #separate_color.Green -> group_output.1
    random_x4___mat_006.links.new(separate_color.outputs[1], group_output.inputs[1])
    #math_001.Value -> white_noise_texture_001.Vector
    random_x4___mat_006.links.new(math_001.outputs[0], white_noise_texture_001.inputs[0])
    #white_noise_texture_001.Color -> separate_color_001.Color
    random_x4___mat_006.links.new(white_noise_texture_001.outputs[1], separate_color_001.inputs[0])
    #separate_color.Blue -> math_001.Value
    random_x4___mat_006.links.new(separate_color.outputs[2], math_001.inputs[1])
    #math.Value -> math_001.Value
    random_x4___mat_006.links.new(math.outputs[0], math_001.inputs[0])
    #separate_color_001.Red -> group_output.2
    random_x4___mat_006.links.new(separate_color_001.outputs[0], group_output.inputs[2])
    #separate_color_001.Green -> group_output.3
    random_x4___mat_006.links.new(separate_color_001.outputs[1], group_output.inputs[3])
    #object_info.Random -> white_noise_texture_001.W
    random_x4___mat_006.links.new(object_info.outputs[5], white_noise_texture_001.inputs[1])
    #separate_color_001.Blue -> group_output.4
    random_x4___mat_006.links.new(separate_color_001.outputs[2], group_output.inputs[4])
    return random_x4___mat_006

random_x4___mat_006 = random_x4___mat_006_node_group()

#initialize SolarPanelShader node group
def solarpanelshader_node_group():

    solarpanelshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "SolarPanelShader")

    solarpanelshader.color_tag = 'NONE'
    solarpanelshader.description = ""
    solarpanelshader.default_group_node_width = 140
    

    #solarpanelshader interface
    #Socket BSDF
    bsdf_socket = solarpanelshader.interface.new_socket(name = "BSDF", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    bsdf_socket.attribute_domain = 'POINT'
    bsdf_socket.default_input = 'VALUE'
    bsdf_socket.structure_type = 'AUTO'

    #Socket color1
    color1_socket = solarpanelshader.interface.new_socket(name = "color1", in_out='INPUT', socket_type = 'NodeSocketColor')
    color1_socket.default_value = (0.0013056989992037416, 0.012050267308950424, 0.1727084219455719, 1.0)
    color1_socket.attribute_domain = 'POINT'
    color1_socket.default_input = 'VALUE'
    color1_socket.structure_type = 'AUTO'

    #Socket color2
    color2_socket = solarpanelshader.interface.new_socket(name = "color2", in_out='INPUT', socket_type = 'NodeSocketColor')
    color2_socket.default_value = (0.0027601474430412054, 0.0037171675357967615, 0.1186249703168869, 1.0)
    color2_socket.attribute_domain = 'POINT'
    color2_socket.default_input = 'VALUE'
    color2_socket.structure_type = 'AUTO'


    #initialize solarpanelshader nodes
    #node Group Output
    group_output_1 = solarpanelshader.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    #node Frame.002
    frame_002 = solarpanelshader.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    #node Frame.003
    frame_003 = solarpanelshader.nodes.new("NodeFrame")
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    #node Frame.001
    frame_001 = solarpanelshader.nodes.new("NodeFrame")
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    #node Frame
    frame = solarpanelshader.nodes.new("NodeFrame")
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    #node Noise Texture
    noise_texture = solarpanelshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '4D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    #Scale
    noise_texture.inputs[2].default_value = 6.0
    #Detail
    noise_texture.inputs[3].default_value = 14.999999046325684
    #Roughness
    noise_texture.inputs[4].default_value = 0.550000011920929
    #Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    #Distortion
    noise_texture.inputs[8].default_value = 0.0

    #node Mix.001
    mix_001 = solarpanelshader.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'DARKEN'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'RGBA'
    mix_001.factor_mode = 'UNIFORM'
    #B_Color
    mix_001.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)

    #node Bump.001
    bump_001 = solarpanelshader.nodes.new("ShaderNodeBump")
    bump_001.name = "Bump.001"
    bump_001.invert = True
    #Distance
    bump_001.inputs[1].default_value = 1.0
    #Filter Width
    bump_001.inputs[2].default_value = 0.10000000149011612
    #Normal
    bump_001.inputs[4].default_value = (0.0, 0.0, 0.0)

    #node ColorRamp.004
    colorramp_004 = solarpanelshader.nodes.new("ShaderNodeValToRGB")
    colorramp_004.name = "ColorRamp.004"
    colorramp_004.color_ramp.color_mode = 'RGB'
    colorramp_004.color_ramp.hue_interpolation = 'NEAR'
    colorramp_004.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    colorramp_004.color_ramp.elements.remove(colorramp_004.color_ramp.elements[0])
    colorramp_004_cre_0 = colorramp_004.color_ramp.elements[0]
    colorramp_004_cre_0.position = 0.24025972187519073
    colorramp_004_cre_0.alpha = 1.0
    colorramp_004_cre_0.color = (0.20731863379478455, 0.20731863379478455, 0.20731863379478455, 1.0)

    colorramp_004_cre_1 = colorramp_004.color_ramp.elements.new(0.8545454740524292)
    colorramp_004_cre_1.alpha = 1.0
    colorramp_004_cre_1.color = (0.9054436087608337, 0.9054436087608337, 0.9054436087608337, 1.0)


    #node Reroute.001
    reroute_001 = solarpanelshader.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketVector"
    #node Reroute
    reroute = solarpanelshader.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketVector"
    #node ColorRamp.001
    colorramp_001 = solarpanelshader.nodes.new("ShaderNodeValToRGB")
    colorramp_001.name = "ColorRamp.001"
    colorramp_001.color_ramp.color_mode = 'RGB'
    colorramp_001.color_ramp.hue_interpolation = 'NEAR'
    colorramp_001.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    colorramp_001.color_ramp.elements.remove(colorramp_001.color_ramp.elements[0])
    colorramp_001_cre_0 = colorramp_001.color_ramp.elements[0]
    colorramp_001_cre_0.position = 0.13333334028720856
    colorramp_001_cre_0.alpha = 1.0
    colorramp_001_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    colorramp_001_cre_1 = colorramp_001.color_ramp.elements.new(0.15000000596046448)
    colorramp_001_cre_1.alpha = 1.0
    colorramp_001_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Voronoi Texture
    voronoi_texture = solarpanelshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = 'CHEBYCHEV'
    voronoi_texture.feature = 'F1'
    voronoi_texture.normalize = False
    voronoi_texture.voronoi_dimensions = '3D'
    #Scale
    voronoi_texture.inputs[2].default_value = 2.0
    #Detail
    voronoi_texture.inputs[3].default_value = 0.0
    #Roughness
    voronoi_texture.inputs[4].default_value = 0.5
    #Lacunarity
    voronoi_texture.inputs[5].default_value = 2.0
    #Randomness
    voronoi_texture.inputs[8].default_value = 0.0

    #node Voronoi Texture.001
    voronoi_texture_001 = solarpanelshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001.name = "Voronoi Texture.001"
    voronoi_texture_001.distance = 'MANHATTAN'
    voronoi_texture_001.feature = 'F1'
    voronoi_texture_001.normalize = False
    voronoi_texture_001.voronoi_dimensions = '3D'
    #Scale
    voronoi_texture_001.inputs[2].default_value = 2.0
    #Detail
    voronoi_texture_001.inputs[3].default_value = 0.0
    #Roughness
    voronoi_texture_001.inputs[4].default_value = 0.5
    #Lacunarity
    voronoi_texture_001.inputs[5].default_value = 2.0
    #Randomness
    voronoi_texture_001.inputs[8].default_value = 0.0

    #node ColorRamp
    colorramp = solarpanelshader.nodes.new("ShaderNodeValToRGB")
    colorramp.name = "ColorRamp"
    colorramp.color_ramp.color_mode = 'RGB'
    colorramp.color_ramp.hue_interpolation = 'NEAR'
    colorramp.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    colorramp.color_ramp.elements.remove(colorramp.color_ramp.elements[0])
    colorramp_cre_0 = colorramp.color_ramp.elements[0]
    colorramp_cre_0.position = 0.4749999940395355
    colorramp_cre_0.alpha = 1.0
    colorramp_cre_0.color = (1.0, 1.0, 1.0, 1.0)

    colorramp_cre_1 = colorramp.color_ramp.elements.new(0.48500001430511475)
    colorramp_cre_1.alpha = 1.0
    colorramp_cre_1.color = (0.0, 0.0, 0.0, 1.0)


    #node Vector Math
    vector_math = solarpanelshader.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'ADD'
    #Vector_001
    vector_math.inputs[1].default_value = (0.75, 0.75, 0.0)

    #node Mix
    mix = solarpanelshader.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'DARKEN'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'
    #Factor_Float
    mix.inputs[0].default_value = 1.0

    #node Voronoi Texture.002
    voronoi_texture_002 = solarpanelshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_002.name = "Voronoi Texture.002"
    voronoi_texture_002.distance = 'EUCLIDEAN'
    voronoi_texture_002.feature = 'F1'
    voronoi_texture_002.normalize = False
    voronoi_texture_002.voronoi_dimensions = '4D'
    #Scale
    voronoi_texture_002.inputs[2].default_value = 50.0
    #Detail
    voronoi_texture_002.inputs[3].default_value = 0.5
    #Roughness
    voronoi_texture_002.inputs[4].default_value = 0.5
    #Lacunarity
    voronoi_texture_002.inputs[5].default_value = 2.0
    #Randomness
    voronoi_texture_002.inputs[8].default_value = 0.0

    #node Noise Texture.001
    noise_texture_001 = solarpanelshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = '4D'
    noise_texture_001.noise_type = 'FBM'
    noise_texture_001.normalize = True
    #Scale
    noise_texture_001.inputs[2].default_value = 2.0
    #Detail
    noise_texture_001.inputs[3].default_value = 15.0
    #Roughness
    noise_texture_001.inputs[4].default_value = 0.5
    #Lacunarity
    noise_texture_001.inputs[5].default_value = 2.0
    #Distortion
    noise_texture_001.inputs[8].default_value = 0.0

    #node Brick Texture
    brick_texture = solarpanelshader.nodes.new("ShaderNodeTexBrick")
    brick_texture.name = "Brick Texture"
    brick_texture.offset = 0.0
    brick_texture.offset_frequency = 2
    brick_texture.squash = 1.0
    brick_texture.squash_frequency = 2
    #Color1
    brick_texture.inputs[1].default_value = (0.0, 0.0, 0.0, 1.0)
    #Color2
    brick_texture.inputs[2].default_value = (0.0, 0.0, 0.0, 1.0)
    #Mortar
    brick_texture.inputs[3].default_value = (1.0, 1.0, 1.0, 1.0)
    #Scale
    brick_texture.inputs[4].default_value = 5.0
    #Mortar Size
    brick_texture.inputs[5].default_value = 0.009999999776482582
    #Mortar Smooth
    brick_texture.inputs[6].default_value = 0.49000000953674316
    #Bias
    brick_texture.inputs[7].default_value = 0.0
    #Brick Width
    brick_texture.inputs[8].default_value = 0.625
    #Row Height
    brick_texture.inputs[9].default_value = 0.20000000298023224

    #node Mix.003
    mix_003 = solarpanelshader.nodes.new("ShaderNodeMix")
    mix_003.name = "Mix.003"
    mix_003.blend_type = 'LIGHTEN'
    mix_003.clamp_factor = True
    mix_003.clamp_result = False
    mix_003.data_type = 'RGBA'
    mix_003.factor_mode = 'UNIFORM'
    #B_Color
    mix_003.inputs[7].default_value = (0.22322650253772736, 0.22322815656661987, 0.2232280671596527, 1.0)

    #node Mix.002
    mix_002 = solarpanelshader.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = 'MIX'
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = 'RGBA'
    mix_002.factor_mode = 'UNIFORM'
    #A_Color
    mix_002.inputs[6].default_value = (0.22322650253772736, 0.22322815656661987, 0.2232280671596527, 1.0)

    #node ColorRamp.003
    colorramp_003 = solarpanelshader.nodes.new("ShaderNodeValToRGB")
    colorramp_003.name = "ColorRamp.003"
    colorramp_003.color_ramp.color_mode = 'RGB'
    colorramp_003.color_ramp.hue_interpolation = 'NEAR'
    colorramp_003.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    colorramp_003.color_ramp.elements.remove(colorramp_003.color_ramp.elements[0])
    colorramp_003_cre_0 = colorramp_003.color_ramp.elements[0]
    colorramp_003_cre_0.position = 0.14025971293449402
    colorramp_003_cre_0.alpha = 1.0
    colorramp_003_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    colorramp_003_cre_1 = colorramp_003.color_ramp.elements.new(0.8181816935539246)
    colorramp_003_cre_1.alpha = 1.0
    colorramp_003_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Reroute.002
    reroute_002 = solarpanelshader.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.socket_idname = "NodeSocketVector"
    #node Texture Coordinate
    texture_coordinate = solarpanelshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False

    #node Mapping
    mapping = solarpanelshader.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = 'POINT'
    #Location
    mapping.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    mapping.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Value
    value = solarpanelshader.nodes.new("ShaderNodeValue")
    value.name = "Value"

    value.outputs[0].default_value = 10.0
    #node Mix.004
    mix_004 = solarpanelshader.nodes.new("ShaderNodeMix")
    mix_004.name = "Mix.004"
    mix_004.blend_type = 'DARKEN'
    mix_004.clamp_factor = True
    mix_004.clamp_result = False
    mix_004.data_type = 'RGBA'
    mix_004.factor_mode = 'UNIFORM'
    #B_Color
    mix_004.inputs[7].default_value = (0.05000000074505806, 0.05000000074505806, 0.05000000074505806, 1.0)

    #node Vector Math.001
    vector_math_001 = solarpanelshader.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'MULTIPLY'
    #Vector_001
    vector_math_001.inputs[1].default_value = (1.0, 0.6399999856948853, 1.0)

    #node Group
    group = solarpanelshader.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = random_x4___mat_006
    #Socket_5
    group.inputs[0].default_value = 0.521340012550354

    #node Principled BSDF.001
    principled_bsdf_001 = solarpanelshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_001.name = "Principled BSDF.001"
    principled_bsdf_001.distribution = 'MULTI_GGX'
    principled_bsdf_001.subsurface_method = 'RANDOM_WALK'
    #Metallic
    principled_bsdf_001.inputs[1].default_value = 1.0
    #IOR
    principled_bsdf_001.inputs[3].default_value = 1.5
    #Alpha
    principled_bsdf_001.inputs[4].default_value = 1.0
    #Diffuse Roughness
    principled_bsdf_001.inputs[7].default_value = 0.0
    #Subsurface Weight
    principled_bsdf_001.inputs[8].default_value = 0.0
    #Subsurface Radius
    principled_bsdf_001.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    #Subsurface Scale
    principled_bsdf_001.inputs[10].default_value = 0.05000000074505806
    #Subsurface Anisotropy
    principled_bsdf_001.inputs[12].default_value = 0.0
    #Specular IOR Level
    principled_bsdf_001.inputs[13].default_value = 0.5
    #Specular Tint
    principled_bsdf_001.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    #Anisotropic
    principled_bsdf_001.inputs[15].default_value = 0.0
    #Anisotropic Rotation
    principled_bsdf_001.inputs[16].default_value = 0.0
    #Tangent
    principled_bsdf_001.inputs[17].default_value = (0.0, 0.0, 0.0)
    #Transmission Weight
    principled_bsdf_001.inputs[18].default_value = 0.0
    #Coat Weight
    principled_bsdf_001.inputs[19].default_value = 0.0
    #Coat Roughness
    principled_bsdf_001.inputs[20].default_value = 0.029999999329447746
    #Coat IOR
    principled_bsdf_001.inputs[21].default_value = 1.5
    #Coat Tint
    principled_bsdf_001.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    #Coat Normal
    principled_bsdf_001.inputs[23].default_value = (0.0, 0.0, 0.0)
    #Sheen Weight
    principled_bsdf_001.inputs[24].default_value = 0.0
    #Sheen Roughness
    principled_bsdf_001.inputs[25].default_value = 0.5
    #Sheen Tint
    principled_bsdf_001.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    #Emission Color
    principled_bsdf_001.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    #Emission Strength
    principled_bsdf_001.inputs[28].default_value = 0.0
    #Thin Film Thickness
    principled_bsdf_001.inputs[29].default_value = 0.0
    #Thin Film IOR
    principled_bsdf_001.inputs[30].default_value = 1.3300000429153442

    #node Map Range
    map_range = solarpanelshader.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = True
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    #From Min
    map_range.inputs[1].default_value = 0.0
    #From Max
    map_range.inputs[2].default_value = 1.0
    #To Min
    map_range.inputs[3].default_value = 0.25
    #To Max
    map_range.inputs[4].default_value = 0.550000011920929

    #node Mix.005
    mix_005 = solarpanelshader.nodes.new("ShaderNodeMix")
    mix_005.name = "Mix.005"
    mix_005.blend_type = 'MIX'
    mix_005.clamp_factor = True
    mix_005.clamp_result = False
    mix_005.data_type = 'RGBA'
    mix_005.factor_mode = 'UNIFORM'

    #node Group Input
    group_input_1 = solarpanelshader.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"


    #Set locations
    group_output_1.location = (0.0, 0.0)
    frame_002.location = (0.0, 0.0)
    frame_003.location = (0.0, 0.0)
    frame_001.location = (0.0, 0.0)
    frame.location = (0.0, 0.0)
    noise_texture.location = (0.0, 0.0)
    mix_001.location = (0.0, 0.0)
    bump_001.location = (0.0, 0.0)
    colorramp_004.location = (0.0, 0.0)
    reroute_001.location = (0.0, 0.0)
    reroute.location = (0.0, 0.0)
    colorramp_001.location = (0.0, 0.0)
    voronoi_texture.location = (0.0, 0.0)
    voronoi_texture_001.location = (0.0, 0.0)
    colorramp.location = (0.0, 0.0)
    vector_math.location = (0.0, 0.0)
    mix.location = (0.0, 0.0)
    voronoi_texture_002.location = (0.0, 0.0)
    noise_texture_001.location = (0.0, 0.0)
    brick_texture.location = (0.0, 0.0)
    mix_003.location = (0.0, 0.0)
    mix_002.location = (0.0, 0.0)
    colorramp_003.location = (0.0, 0.0)
    reroute_002.location = (0.0, 0.0)
    texture_coordinate.location = (0.0, 0.0)
    mapping.location = (0.0, 0.0)
    value.location = (0.0, 0.0)
    mix_004.location = (0.0, 0.0)
    vector_math_001.location = (0.0, 0.0)
    group.location = (0.0, 0.0)
    principled_bsdf_001.location = (0.0, 0.0)
    map_range.location = (0.0, 0.0)
    mix_005.location = (0.0, 0.0)
    group_input_1.location = (0.0, 0.0)

    #Set dimensions
    group_output_1.width, group_output_1.height = 140.0, 100.0
    frame_002.width, frame_002.height = 150.0, 100.0
    frame_003.width, frame_003.height = 150.0, 100.0
    frame_001.width, frame_001.height = 150.0, 100.0
    frame.width, frame.height = 150.0, 100.0
    noise_texture.width, noise_texture.height = 140.0, 100.0
    mix_001.width, mix_001.height = 140.0, 100.0
    bump_001.width, bump_001.height = 140.0, 100.0
    colorramp_004.width, colorramp_004.height = 240.0, 100.0
    reroute_001.width, reroute_001.height = 140.0, 100.0
    reroute.width, reroute.height = 140.0, 100.0
    colorramp_001.width, colorramp_001.height = 240.0, 100.0
    voronoi_texture.width, voronoi_texture.height = 140.0, 100.0
    voronoi_texture_001.width, voronoi_texture_001.height = 140.0, 100.0
    colorramp.width, colorramp.height = 240.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    mix.width, mix.height = 140.0, 100.0
    voronoi_texture_002.width, voronoi_texture_002.height = 140.0, 100.0
    noise_texture_001.width, noise_texture_001.height = 140.0, 100.0
    brick_texture.width, brick_texture.height = 150.0, 100.0
    mix_003.width, mix_003.height = 140.0, 100.0
    mix_002.width, mix_002.height = 140.0, 100.0
    colorramp_003.width, colorramp_003.height = 240.0, 100.0
    reroute_002.width, reroute_002.height = 140.0, 100.0
    texture_coordinate.width, texture_coordinate.height = 140.0, 100.0
    mapping.width, mapping.height = 140.0, 100.0
    value.width, value.height = 140.0, 100.0
    mix_004.width, mix_004.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0
    principled_bsdf_001.width, principled_bsdf_001.height = 240.0, 100.0
    map_range.width, map_range.height = 140.0, 100.0
    mix_005.width, mix_005.height = 140.0, 100.0
    group_input_1.width, group_input_1.height = 140.0, 100.0

    #initialize solarpanelshader links
    #noise_texture.Fac -> colorramp_004.Fac
    solarpanelshader.links.new(noise_texture.outputs[0], colorramp_004.inputs[0])
    #voronoi_texture_001.Distance -> colorramp_001.Fac
    solarpanelshader.links.new(voronoi_texture_001.outputs[0], colorramp_001.inputs[0])
    #reroute.Output -> voronoi_texture_002.Vector
    solarpanelshader.links.new(reroute.outputs[0], voronoi_texture_002.inputs[0])
    #value.Value -> mapping.Scale
    solarpanelshader.links.new(value.outputs[0], mapping.inputs[3])
    #colorramp.Color -> mix.A
    solarpanelshader.links.new(colorramp.outputs[0], mix.inputs[6])
    #mix.Result -> mix_002.Factor
    solarpanelshader.links.new(mix.outputs[2], mix_002.inputs[0])
    #reroute.Output -> noise_texture_001.Vector
    solarpanelshader.links.new(reroute.outputs[0], noise_texture_001.inputs[0])
    #colorramp_001.Color -> mix.B
    solarpanelshader.links.new(colorramp_001.outputs[0], mix.inputs[7])
    #brick_texture.Color -> mix_003.Factor
    solarpanelshader.links.new(brick_texture.outputs[0], mix_003.inputs[0])
    #colorramp_003.Color -> mix_004.Factor
    solarpanelshader.links.new(colorramp_003.outputs[0], mix_004.inputs[0])
    #mix_003.Result -> mix_002.B
    solarpanelshader.links.new(mix_003.outputs[2], mix_002.inputs[7])
    #noise_texture_001.Fac -> colorramp_003.Fac
    solarpanelshader.links.new(noise_texture_001.outputs[0], colorramp_003.inputs[0])
    #vector_math_001.Vector -> brick_texture.Vector
    solarpanelshader.links.new(vector_math_001.outputs[0], brick_texture.inputs[0])
    #mix_004.Result -> mix_003.A
    solarpanelshader.links.new(mix_004.outputs[2], mix_003.inputs[6])
    #mapping.Vector -> reroute_002.Input
    solarpanelshader.links.new(mapping.outputs[0], reroute_002.inputs[0])
    #reroute_002.Output -> voronoi_texture.Vector
    solarpanelshader.links.new(reroute_002.outputs[0], voronoi_texture.inputs[0])
    #reroute_001.Output -> noise_texture.Vector
    solarpanelshader.links.new(reroute_001.outputs[0], noise_texture.inputs[0])
    #mix_001.Result -> bump_001.Height
    solarpanelshader.links.new(mix_001.outputs[2], bump_001.inputs[3])
    #vector_math.Vector -> voronoi_texture_001.Vector
    solarpanelshader.links.new(vector_math.outputs[0], voronoi_texture_001.inputs[0])
    #reroute_002.Output -> reroute.Input
    solarpanelshader.links.new(reroute_002.outputs[0], reroute.inputs[0])
    #brick_texture.Color -> mix_001.Factor
    solarpanelshader.links.new(brick_texture.outputs[0], mix_001.inputs[0])
    #voronoi_texture.Distance -> colorramp.Fac
    solarpanelshader.links.new(voronoi_texture.outputs[0], colorramp.inputs[0])
    #reroute_002.Output -> reroute_001.Input
    solarpanelshader.links.new(reroute_002.outputs[0], reroute_001.inputs[0])
    #mix.Result -> mix_001.A
    solarpanelshader.links.new(mix.outputs[2], mix_001.inputs[6])
    #reroute_002.Output -> vector_math.Vector
    solarpanelshader.links.new(reroute_002.outputs[0], vector_math.inputs[0])
    #reroute.Output -> vector_math_001.Vector
    solarpanelshader.links.new(reroute.outputs[0], vector_math_001.inputs[0])
    #group.0 -> noise_texture_001.W
    solarpanelshader.links.new(group.outputs[0], noise_texture_001.inputs[1])
    #group.1 -> voronoi_texture_002.W
    solarpanelshader.links.new(group.outputs[1], voronoi_texture_002.inputs[1])
    #principled_bsdf_001.BSDF -> group_output_1.BSDF
    solarpanelshader.links.new(principled_bsdf_001.outputs[0], group_output_1.inputs[0])
    #mix_002.Result -> principled_bsdf_001.Base Color
    solarpanelshader.links.new(mix_002.outputs[2], principled_bsdf_001.inputs[0])
    #colorramp_004.Color -> principled_bsdf_001.Roughness
    solarpanelshader.links.new(colorramp_004.outputs[0], principled_bsdf_001.inputs[2])
    #bump_001.Normal -> principled_bsdf_001.Normal
    solarpanelshader.links.new(bump_001.outputs[0], principled_bsdf_001.inputs[5])
    #group.2 -> noise_texture.W
    solarpanelshader.links.new(group.outputs[2], noise_texture.inputs[1])
    #group.3 -> map_range.Value
    solarpanelshader.links.new(group.outputs[3], map_range.inputs[0])
    #map_range.Result -> bump_001.Strength
    solarpanelshader.links.new(map_range.outputs[0], bump_001.inputs[0])
    #mix_005.Result -> mix_004.A
    solarpanelshader.links.new(mix_005.outputs[2], mix_004.inputs[6])
    #voronoi_texture_002.Distance -> mix_005.Factor
    solarpanelshader.links.new(voronoi_texture_002.outputs[0], mix_005.inputs[0])
    #group_input_1.color1 -> mix_005.A
    solarpanelshader.links.new(group_input_1.outputs[0], mix_005.inputs[6])
    #group_input_1.color2 -> mix_005.B
    solarpanelshader.links.new(group_input_1.outputs[1], mix_005.inputs[7])
    #texture_coordinate.UV -> mapping.Vector
    solarpanelshader.links.new(texture_coordinate.outputs[2], mapping.inputs[0])
    return solarpanelshader

solarpanelshader = solarpanelshader_node_group()

#initialize SolarPanelMat node group
def solarpanelmat_node_group():

    solarpanelmat = mat.node_tree
    #start with a clean node tree
    for node in solarpanelmat.nodes:
        solarpanelmat.nodes.remove(node)
    solarpanelmat.color_tag = 'NONE'
    solarpanelmat.description = ""
    solarpanelmat.default_group_node_width = 140
    

    #solarpanelmat interface

    #initialize solarpanelmat nodes
    #node Material Output
    material_output = solarpanelmat.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    #Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Thickness
    material_output.inputs[3].default_value = 0.0

    #node Group
    group_1 = solarpanelmat.nodes.new("ShaderNodeGroup")
    group_1.name = "Group"
    group_1.node_tree = solarpanelshader
    #Socket_1
    group_1.inputs[0].default_value = (0.0013056989992037416, 0.012050267308950424, 0.1727084219455719, 1.0)
    #Socket_2
    group_1.inputs[1].default_value = (0.0027601474430412054, 0.0037171675357967615, 0.1186249703168869, 1.0)


    #Set locations
    material_output.location = (0.0, 0.0)
    group_1.location = (0.0, 0.0)

    #Set dimensions
    material_output.width, material_output.height = 140.0, 100.0
    group_1.width, group_1.height = 140.0, 100.0

    #initialize solarpanelmat links
    #group_1.BSDF -> material_output.Surface
    solarpanelmat.links.new(group_1.outputs[0], material_output.inputs[0])
    return solarpanelmat

solarpanelmat = solarpanelmat_node_group()


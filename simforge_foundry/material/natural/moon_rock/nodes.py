import bpy, mathutils

mat = bpy.data.materials.new(name = "MoonRockMat")
mat.use_nodes = True
#initialize Random x4 | Mat.003 node group
def random_x4___mat_003_node_group():

    random_x4___mat_003 = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "Random x4 | Mat.003")

    random_x4___mat_003.color_tag = 'NONE'
    random_x4___mat_003.description = ""
    random_x4___mat_003.default_group_node_width = 140
    

    #random_x4___mat_003 interface
    #Socket 0
    _0_socket = random_x4___mat_003.interface.new_socket(name = "0", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _0_socket.default_value = 0.0
    _0_socket.min_value = 0.0
    _0_socket.max_value = 1.0
    _0_socket.subtype = 'NONE'
    _0_socket.attribute_domain = 'POINT'
    _0_socket.default_input = 'VALUE'
    _0_socket.structure_type = 'AUTO'

    #Socket 1
    _1_socket = random_x4___mat_003.interface.new_socket(name = "1", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _1_socket.default_value = 0.0
    _1_socket.min_value = 0.0
    _1_socket.max_value = 1.0
    _1_socket.subtype = 'NONE'
    _1_socket.attribute_domain = 'POINT'
    _1_socket.default_input = 'VALUE'
    _1_socket.structure_type = 'AUTO'

    #Socket 2
    _2_socket = random_x4___mat_003.interface.new_socket(name = "2", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _2_socket.default_value = 0.0
    _2_socket.min_value = 0.0
    _2_socket.max_value = 1.0
    _2_socket.subtype = 'NONE'
    _2_socket.attribute_domain = 'POINT'
    _2_socket.default_input = 'VALUE'
    _2_socket.structure_type = 'AUTO'

    #Socket 3
    _3_socket = random_x4___mat_003.interface.new_socket(name = "3", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _3_socket.default_value = 0.0
    _3_socket.min_value = 0.0
    _3_socket.max_value = 1.0
    _3_socket.subtype = 'NONE'
    _3_socket.attribute_domain = 'POINT'
    _3_socket.default_input = 'VALUE'
    _3_socket.structure_type = 'AUTO'

    #Socket 4
    _4_socket = random_x4___mat_003.interface.new_socket(name = "4", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    _4_socket.default_value = 0.0
    _4_socket.min_value = -3.4028234663852886e+38
    _4_socket.max_value = 3.4028234663852886e+38
    _4_socket.subtype = 'NONE'
    _4_socket.attribute_domain = 'POINT'
    _4_socket.default_input = 'VALUE'
    _4_socket.structure_type = 'AUTO'

    #Socket Seed
    seed_socket = random_x4___mat_003.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketFloat')
    seed_socket.default_value = 0.0
    seed_socket.min_value = 0.0
    seed_socket.max_value = 1.0
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'


    #initialize random_x4___mat_003 nodes
    #node Group Output
    group_output = random_x4___mat_003.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = random_x4___mat_003.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Object Info
    object_info = random_x4___mat_003.nodes.new("ShaderNodeObjectInfo")
    object_info.name = "Object Info"

    #node Math
    math = random_x4___mat_003.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'ADD'
    math.use_clamp = False

    #node White Noise Texture
    white_noise_texture = random_x4___mat_003.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture.name = "White Noise Texture"
    white_noise_texture.noise_dimensions = '4D'

    #node Separate Color
    separate_color = random_x4___mat_003.nodes.new("ShaderNodeSeparateColor")
    separate_color.name = "Separate Color"
    separate_color.mode = 'RGB'

    #node Math.001
    math_001 = random_x4___mat_003.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'ADD'
    math_001.use_clamp = False

    #node White Noise Texture.001
    white_noise_texture_001 = random_x4___mat_003.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture_001.name = "White Noise Texture.001"
    white_noise_texture_001.noise_dimensions = '4D'

    #node Separate Color.001
    separate_color_001 = random_x4___mat_003.nodes.new("ShaderNodeSeparateColor")
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

    #initialize random_x4___mat_003 links
    #object_info.Random -> white_noise_texture.W
    random_x4___mat_003.links.new(object_info.outputs[5], white_noise_texture.inputs[1])
    #math.Value -> white_noise_texture.Vector
    random_x4___mat_003.links.new(math.outputs[0], white_noise_texture.inputs[0])
    #white_noise_texture.Color -> separate_color.Color
    random_x4___mat_003.links.new(white_noise_texture.outputs[1], separate_color.inputs[0])
    #object_info.Object Index -> math.Value
    random_x4___mat_003.links.new(object_info.outputs[3], math.inputs[1])
    #group_input.Seed -> math.Value
    random_x4___mat_003.links.new(group_input.outputs[0], math.inputs[0])
    #separate_color.Red -> group_output.0
    random_x4___mat_003.links.new(separate_color.outputs[0], group_output.inputs[0])
    #separate_color.Green -> group_output.1
    random_x4___mat_003.links.new(separate_color.outputs[1], group_output.inputs[1])
    #math_001.Value -> white_noise_texture_001.Vector
    random_x4___mat_003.links.new(math_001.outputs[0], white_noise_texture_001.inputs[0])
    #white_noise_texture_001.Color -> separate_color_001.Color
    random_x4___mat_003.links.new(white_noise_texture_001.outputs[1], separate_color_001.inputs[0])
    #separate_color.Blue -> math_001.Value
    random_x4___mat_003.links.new(separate_color.outputs[2], math_001.inputs[1])
    #math.Value -> math_001.Value
    random_x4___mat_003.links.new(math.outputs[0], math_001.inputs[0])
    #separate_color_001.Red -> group_output.2
    random_x4___mat_003.links.new(separate_color_001.outputs[0], group_output.inputs[2])
    #separate_color_001.Green -> group_output.3
    random_x4___mat_003.links.new(separate_color_001.outputs[1], group_output.inputs[3])
    #object_info.Random -> white_noise_texture_001.W
    random_x4___mat_003.links.new(object_info.outputs[5], white_noise_texture_001.inputs[1])
    #separate_color_001.Blue -> group_output.4
    random_x4___mat_003.links.new(separate_color_001.outputs[2], group_output.inputs[4])
    return random_x4___mat_003

random_x4___mat_003 = random_x4___mat_003_node_group()

#initialize MoonRockShader node group
def moonrockshader_node_group():

    moonrockshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "MoonRockShader")

    moonrockshader.color_tag = 'NONE'
    moonrockshader.description = ""
    moonrockshader.default_group_node_width = 140
    

    #moonrockshader interface
    #Socket BSDF
    bsdf_socket = moonrockshader.interface.new_socket(name = "BSDF", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    bsdf_socket.attribute_domain = 'POINT'
    bsdf_socket.default_input = 'VALUE'
    bsdf_socket.structure_type = 'AUTO'

    #Socket scale
    scale_socket = moonrockshader.interface.new_socket(name = "scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 16.0
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    #Socket color1
    color1_socket = moonrockshader.interface.new_socket(name = "color1", in_out='INPUT', socket_type = 'NodeSocketColor')
    color1_socket.default_value = (0.24619978666305542, 0.24620160460472107, 0.2462015002965927, 1.0)
    color1_socket.attribute_domain = 'POINT'
    color1_socket.default_input = 'VALUE'
    color1_socket.structure_type = 'AUTO'

    #Socket color2
    color2_socket = moonrockshader.interface.new_socket(name = "color2", in_out='INPUT', socket_type = 'NodeSocketColor')
    color2_socket.default_value = (0.005181482061743736, 0.005181520711630583, 0.005181518383324146, 1.0)
    color2_socket.attribute_domain = 'POINT'
    color2_socket.default_input = 'VALUE'
    color2_socket.structure_type = 'AUTO'

    #Socket edge_color
    edge_color_socket = moonrockshader.interface.new_socket(name = "edge_color", in_out='INPUT', socket_type = 'NodeSocketColor')
    edge_color_socket.default_value = (0.4000000059604645, 0.4000000059604645, 0.4000000059604645, 1.0)
    edge_color_socket.attribute_domain = 'POINT'
    edge_color_socket.default_input = 'VALUE'
    edge_color_socket.structure_type = 'AUTO'

    #Socket noise_scale
    noise_scale_socket = moonrockshader.interface.new_socket(name = "noise_scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_scale_socket.default_value = 7.0
    noise_scale_socket.min_value = -1000.0
    noise_scale_socket.max_value = 1000.0
    noise_scale_socket.subtype = 'NONE'
    noise_scale_socket.attribute_domain = 'POINT'
    noise_scale_socket.default_input = 'VALUE'
    noise_scale_socket.structure_type = 'AUTO'

    #Socket noise_detail
    noise_detail_socket = moonrockshader.interface.new_socket(name = "noise_detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_detail_socket.default_value = 15.0
    noise_detail_socket.min_value = 0.0
    noise_detail_socket.max_value = 15.0
    noise_detail_socket.subtype = 'NONE'
    noise_detail_socket.attribute_domain = 'POINT'
    noise_detail_socket.default_input = 'VALUE'
    noise_detail_socket.structure_type = 'AUTO'

    #Socket noise_roughness
    noise_roughness_socket = moonrockshader.interface.new_socket(name = "noise_roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_roughness_socket.default_value = 0.25
    noise_roughness_socket.min_value = 0.0
    noise_roughness_socket.max_value = 1.0
    noise_roughness_socket.subtype = 'FACTOR'
    noise_roughness_socket.attribute_domain = 'POINT'
    noise_roughness_socket.default_input = 'VALUE'
    noise_roughness_socket.structure_type = 'AUTO'

    #Socket light_noise_scale
    light_noise_scale_socket = moonrockshader.interface.new_socket(name = "light_noise_scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    light_noise_scale_socket.default_value = 5.0
    light_noise_scale_socket.min_value = 0.0
    light_noise_scale_socket.max_value = 15.0
    light_noise_scale_socket.subtype = 'NONE'
    light_noise_scale_socket.attribute_domain = 'POINT'
    light_noise_scale_socket.default_input = 'VALUE'
    light_noise_scale_socket.structure_type = 'AUTO'

    #Socket light_noise_roughness
    light_noise_roughness_socket = moonrockshader.interface.new_socket(name = "light_noise_roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    light_noise_roughness_socket.default_value = 0.800000011920929
    light_noise_roughness_socket.min_value = 0.0
    light_noise_roughness_socket.max_value = 1.0
    light_noise_roughness_socket.subtype = 'FACTOR'
    light_noise_roughness_socket.attribute_domain = 'POINT'
    light_noise_roughness_socket.default_input = 'VALUE'
    light_noise_roughness_socket.structure_type = 'AUTO'

    #Socket roughness
    roughness_socket = moonrockshader.interface.new_socket(name = "roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = 'NONE'
    roughness_socket.attribute_domain = 'POINT'
    roughness_socket.default_input = 'VALUE'
    roughness_socket.structure_type = 'AUTO'

    #Socket noise_bump_scale
    noise_bump_scale_socket = moonrockshader.interface.new_socket(name = "noise_bump_scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_scale_socket.default_value = 15.0
    noise_bump_scale_socket.min_value = -1000.0
    noise_bump_scale_socket.max_value = 1000.0
    noise_bump_scale_socket.subtype = 'NONE'
    noise_bump_scale_socket.attribute_domain = 'POINT'
    noise_bump_scale_socket.default_input = 'VALUE'
    noise_bump_scale_socket.structure_type = 'AUTO'

    #Socket noise_bump_strength
    noise_bump_strength_socket = moonrockshader.interface.new_socket(name = "noise_bump_strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_strength_socket.default_value = 0.05000000074505806
    noise_bump_strength_socket.min_value = 0.0
    noise_bump_strength_socket.max_value = 1.0
    noise_bump_strength_socket.subtype = 'FACTOR'
    noise_bump_strength_socket.attribute_domain = 'POINT'
    noise_bump_strength_socket.default_input = 'VALUE'
    noise_bump_strength_socket.structure_type = 'AUTO'

    #Socket detailed_noise_bump_strength
    detailed_noise_bump_strength_socket = moonrockshader.interface.new_socket(name = "detailed_noise_bump_strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detailed_noise_bump_strength_socket.default_value = 0.25
    detailed_noise_bump_strength_socket.min_value = 0.0
    detailed_noise_bump_strength_socket.max_value = 1.0
    detailed_noise_bump_strength_socket.subtype = 'FACTOR'
    detailed_noise_bump_strength_socket.attribute_domain = 'POINT'
    detailed_noise_bump_strength_socket.default_input = 'VALUE'
    detailed_noise_bump_strength_socket.structure_type = 'AUTO'

    #Socket edge_color_strength
    edge_color_strength_socket = moonrockshader.interface.new_socket(name = "edge_color_strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    edge_color_strength_socket.default_value = 0.75
    edge_color_strength_socket.min_value = 0.0
    edge_color_strength_socket.max_value = 1.0
    edge_color_strength_socket.subtype = 'FACTOR'
    edge_color_strength_socket.attribute_domain = 'POINT'
    edge_color_strength_socket.default_input = 'VALUE'
    edge_color_strength_socket.structure_type = 'AUTO'

    #Socket noise_scale_mixer
    noise_scale_mixer_socket = moonrockshader.interface.new_socket(name = "noise_scale_mixer", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_scale_mixer_socket.default_value = 0.009999999776482582
    noise_scale_mixer_socket.min_value = 0.0
    noise_scale_mixer_socket.max_value = 1.0
    noise_scale_mixer_socket.subtype = 'FACTOR'
    noise_scale_mixer_socket.attribute_domain = 'POINT'
    noise_scale_mixer_socket.default_input = 'VALUE'
    noise_scale_mixer_socket.structure_type = 'AUTO'

    #Socket noise_bump_roughness
    noise_bump_roughness_socket = moonrockshader.interface.new_socket(name = "noise_bump_roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_roughness_socket.default_value = 1.0
    noise_bump_roughness_socket.min_value = 0.0
    noise_bump_roughness_socket.max_value = 1.0
    noise_bump_roughness_socket.subtype = 'FACTOR'
    noise_bump_roughness_socket.attribute_domain = 'POINT'
    noise_bump_roughness_socket.default_input = 'VALUE'
    noise_bump_roughness_socket.structure_type = 'AUTO'

    #Socket voronoi_bump_scale
    voronoi_bump_scale_socket = moonrockshader.interface.new_socket(name = "voronoi_bump_scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    voronoi_bump_scale_socket.default_value = 20.0
    voronoi_bump_scale_socket.min_value = -1000.0
    voronoi_bump_scale_socket.max_value = 1000.0
    voronoi_bump_scale_socket.subtype = 'NONE'
    voronoi_bump_scale_socket.attribute_domain = 'POINT'
    voronoi_bump_scale_socket.default_input = 'VALUE'
    voronoi_bump_scale_socket.structure_type = 'AUTO'

    #Socket voronoi_bump_strength
    voronoi_bump_strength_socket = moonrockshader.interface.new_socket(name = "voronoi_bump_strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    voronoi_bump_strength_socket.default_value = 0.75
    voronoi_bump_strength_socket.min_value = 0.0
    voronoi_bump_strength_socket.max_value = 1.0
    voronoi_bump_strength_socket.subtype = 'FACTOR'
    voronoi_bump_strength_socket.attribute_domain = 'POINT'
    voronoi_bump_strength_socket.default_input = 'VALUE'
    voronoi_bump_strength_socket.structure_type = 'AUTO'


    #initialize moonrockshader nodes
    #node Group Output
    group_output_1 = moonrockshader.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    #node Group Input
    group_input_1 = moonrockshader.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"

    #node Noise Texture
    noise_texture = moonrockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '4D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    #Lacunarity
    noise_texture.inputs[5].default_value = 20.0
    #Distortion
    noise_texture.inputs[8].default_value = 0.0

    #node Mapping.001
    mapping_001 = moonrockshader.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = 'POINT'
    #Rotation
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Texture Coordinate.001
    texture_coordinate_001 = moonrockshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_001.name = "Texture Coordinate.001"
    texture_coordinate_001.from_instancer = False
    texture_coordinate_001.outputs[0].hide = True
    texture_coordinate_001.outputs[1].hide = True
    texture_coordinate_001.outputs[2].hide = True
    texture_coordinate_001.outputs[4].hide = True
    texture_coordinate_001.outputs[5].hide = True
    texture_coordinate_001.outputs[6].hide = True

    #node Bump
    bump = moonrockshader.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    #Distance
    bump.inputs[1].default_value = 1.0
    #Filter Width
    bump.inputs[2].default_value = 0.10000000149011612

    #node Color Ramp
    color_ramp = moonrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp.name = "Color Ramp"
    color_ramp.color_ramp.color_mode = 'RGB'
    color_ramp.color_ramp.hue_interpolation = 'NEAR'
    color_ramp.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
    color_ramp_cre_0 = color_ramp.color_ramp.elements[0]
    color_ramp_cre_0.position = 0.30181822180747986
    color_ramp_cre_0.alpha = 1.0
    color_ramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_cre_1 = color_ramp.color_ramp.elements.new(0.3945455849170685)
    color_ramp_cre_1.alpha = 1.0
    color_ramp_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Noise Texture.001
    noise_texture_001 = moonrockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = '4D'
    noise_texture_001.noise_type = 'FBM'
    noise_texture_001.normalize = True
    #Lacunarity
    noise_texture_001.inputs[5].default_value = 2.0
    #Distortion
    noise_texture_001.inputs[8].default_value = 0.0

    #node Color Ramp.001
    color_ramp_001 = moonrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_001.name = "Color Ramp.001"
    color_ramp_001.color_ramp.color_mode = 'RGB'
    color_ramp_001.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_001.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    color_ramp_001.color_ramp.elements.remove(color_ramp_001.color_ramp.elements[0])
    color_ramp_001_cre_0 = color_ramp_001.color_ramp.elements[0]
    color_ramp_001_cre_0.position = 0.4054546356201172
    color_ramp_001_cre_0.alpha = 1.0
    color_ramp_001_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_001_cre_1 = color_ramp_001.color_ramp.elements.new(0.64090895652771)
    color_ramp_001_cre_1.alpha = 1.0
    color_ramp_001_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Mix
    mix = moonrockshader.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'MIX'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'

    #node Mix.001
    mix_001 = moonrockshader.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'MIX'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'RGBA'
    mix_001.factor_mode = 'UNIFORM'

    #node Geometry
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

    #node Color Ramp.002
    color_ramp_002 = moonrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_002.name = "Color Ramp.002"
    color_ramp_002.color_ramp.color_mode = 'RGB'
    color_ramp_002.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_002.color_ramp.interpolation = 'EASE'

    #initialize color ramp elements
    color_ramp_002.color_ramp.elements.remove(color_ramp_002.color_ramp.elements[0])
    color_ramp_002_cre_0 = color_ramp_002.color_ramp.elements[0]
    color_ramp_002_cre_0.position = 0.5186362266540527
    color_ramp_002_cre_0.alpha = 1.0
    color_ramp_002_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_002_cre_1 = color_ramp_002.color_ramp.elements.new(0.6045457124710083)
    color_ramp_002_cre_1.alpha = 1.0
    color_ramp_002_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Mix.003
    mix_003 = moonrockshader.nodes.new("ShaderNodeMix")
    mix_003.name = "Mix.003"
    mix_003.blend_type = 'MIX'
    mix_003.clamp_factor = True
    mix_003.clamp_result = False
    mix_003.data_type = 'RGBA'
    mix_003.factor_mode = 'UNIFORM'

    #node Color Ramp.004
    color_ramp_004 = moonrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_004.name = "Color Ramp.004"
    color_ramp_004.color_ramp.color_mode = 'RGB'
    color_ramp_004.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_004.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    color_ramp_004.color_ramp.elements.remove(color_ramp_004.color_ramp.elements[0])
    color_ramp_004_cre_0 = color_ramp_004.color_ramp.elements[0]
    color_ramp_004_cre_0.position = 0.0
    color_ramp_004_cre_0.alpha = 1.0
    color_ramp_004_cre_0.color = (0.6514015197753906, 0.6514063477516174, 0.6514060497283936, 1.0)

    color_ramp_004_cre_1 = color_ramp_004.color_ramp.elements.new(1.0)
    color_ramp_004_cre_1.alpha = 1.0
    color_ramp_004_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Noise Texture.003
    noise_texture_003 = moonrockshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_003.name = "Noise Texture.003"
    noise_texture_003.noise_dimensions = '4D'
    noise_texture_003.noise_type = 'FBM'
    noise_texture_003.normalize = True
    #Detail
    noise_texture_003.inputs[3].default_value = 15.0
    #Lacunarity
    noise_texture_003.inputs[5].default_value = 0.0
    #Distortion
    noise_texture_003.inputs[8].default_value = 0.0

    #node Bump.001
    bump_001 = moonrockshader.nodes.new("ShaderNodeBump")
    bump_001.name = "Bump.001"
    bump_001.invert = False
    #Distance
    bump_001.inputs[1].default_value = 1.0
    #Filter Width
    bump_001.inputs[2].default_value = 0.10000000149011612

    #node Frame.001
    frame_001 = moonrockshader.nodes.new("NodeFrame")
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    #node Frame.002
    frame_002 = moonrockshader.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    #node Frame
    frame = moonrockshader.nodes.new("NodeFrame")
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    #node Hue/Saturation/Value
    hue_saturation_value = moonrockshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    #Hue
    hue_saturation_value.inputs[0].default_value = 0.5
    #Saturation
    hue_saturation_value.inputs[1].default_value = 1.0
    #Fac
    hue_saturation_value.inputs[3].default_value = 1.0

    #node Frame.003
    frame_003 = moonrockshader.nodes.new("NodeFrame")
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    #node Principled BSDF
    principled_bsdf = moonrockshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    #Metallic
    principled_bsdf.inputs[1].default_value = 0.0
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

    #node Math
    math_1 = moonrockshader.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = 'MULTIPLY'
    math_1.use_clamp = False
    #Value_001
    math_1.inputs[1].default_value = 10.0

    #node Group.001
    group_001 = moonrockshader.nodes.new("ShaderNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = random_x4___mat_003
    #Socket_5
    group_001.inputs[0].default_value = 0.5213124752044678

    #node Voronoi Texture
    voronoi_texture = moonrockshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = 'EUCLIDEAN'
    voronoi_texture.feature = 'F1'
    voronoi_texture.normalize = True
    voronoi_texture.voronoi_dimensions = '4D'
    #Detail
    voronoi_texture.inputs[3].default_value = 0.0
    #Roughness
    voronoi_texture.inputs[4].default_value = 1.0
    #Lacunarity
    voronoi_texture.inputs[5].default_value = 2.0
    #Randomness
    voronoi_texture.inputs[8].default_value = 1.0

    #node Bump.002
    bump_002 = moonrockshader.nodes.new("ShaderNodeBump")
    bump_002.name = "Bump.002"
    bump_002.invert = False
    #Distance
    bump_002.inputs[1].default_value = 1.0
    #Filter Width
    bump_002.inputs[2].default_value = 0.10000000149011612

    #node Color Ramp.005
    color_ramp_005 = moonrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_005.name = "Color Ramp.005"
    color_ramp_005.color_ramp.color_mode = 'RGB'
    color_ramp_005.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_005.color_ramp.interpolation = 'EASE'

    #initialize color ramp elements
    color_ramp_005.color_ramp.elements.remove(color_ramp_005.color_ramp.elements[0])
    color_ramp_005_cre_0 = color_ramp_005.color_ramp.elements[0]
    color_ramp_005_cre_0.position = 0.0
    color_ramp_005_cre_0.alpha = 1.0
    color_ramp_005_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_005_cre_1 = color_ramp_005.color_ramp.elements.new(0.15909108519554138)
    color_ramp_005_cre_1.alpha = 1.0
    color_ramp_005_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Voronoi Texture.001
    voronoi_texture_001 = moonrockshader.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001.name = "Voronoi Texture.001"
    voronoi_texture_001.distance = 'EUCLIDEAN'
    voronoi_texture_001.feature = 'SMOOTH_F1'
    voronoi_texture_001.normalize = True
    voronoi_texture_001.voronoi_dimensions = '4D'
    #Detail
    voronoi_texture_001.inputs[3].default_value = 0.0
    #Roughness
    voronoi_texture_001.inputs[4].default_value = 1.0
    #Lacunarity
    voronoi_texture_001.inputs[5].default_value = 2.0
    #Smoothness
    voronoi_texture_001.inputs[6].default_value = 1.0
    #Randomness
    voronoi_texture_001.inputs[8].default_value = 1.0

    #node Color Ramp.006
    color_ramp_006 = moonrockshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_006.name = "Color Ramp.006"
    color_ramp_006.color_ramp.color_mode = 'RGB'
    color_ramp_006.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_006.color_ramp.interpolation = 'CARDINAL'

    #initialize color ramp elements
    color_ramp_006.color_ramp.elements.remove(color_ramp_006.color_ramp.elements[0])
    color_ramp_006_cre_0 = color_ramp_006.color_ramp.elements[0]
    color_ramp_006_cre_0.position = 0.0
    color_ramp_006_cre_0.alpha = 1.0
    color_ramp_006_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_006_cre_1 = color_ramp_006.color_ramp.elements.new(0.13181859254837036)
    color_ramp_006_cre_1.alpha = 1.0
    color_ramp_006_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Math.001
    math_001_1 = moonrockshader.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = 'DIVIDE'
    math_001_1.use_clamp = False

    #node Bump.003
    bump_003 = moonrockshader.nodes.new("ShaderNodeBump")
    bump_003.name = "Bump.003"
    bump_003.invert = False
    #Distance
    bump_003.inputs[1].default_value = 1.0
    #Filter Width
    bump_003.inputs[2].default_value = 0.10000000149011612
    #Normal
    bump_003.inputs[4].default_value = (0.0, 0.0, 0.0)

    #node Map Range.004
    map_range_004 = moonrockshader.nodes.new("ShaderNodeMapRange")
    map_range_004.name = "Map Range.004"
    map_range_004.clamp = True
    map_range_004.data_type = 'FLOAT'
    map_range_004.interpolation_type = 'LINEAR'
    #From Min
    map_range_004.inputs[1].default_value = 0.0
    #From Max
    map_range_004.inputs[2].default_value = 1.0
    #To Min
    map_range_004.inputs[3].default_value = -1000.0
    #To Max
    map_range_004.inputs[4].default_value = 1000.0

    #node Group.002
    group_002 = moonrockshader.nodes.new("ShaderNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = random_x4___mat_003

    #node Math.002
    math_002 = moonrockshader.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'MULTIPLY'
    math_002.use_clamp = False

    #node Math.003
    math_003 = moonrockshader.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'MULTIPLY'
    math_003.use_clamp = False
    #Value_001
    math_003.inputs[1].default_value = 5.0

    #node Math.004
    math_004 = moonrockshader.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'MULTIPLY'
    math_004.use_clamp = False


    #Set locations
    group_output_1.location = (0.0, 0.0)
    group_input_1.location = (0.0, 0.0)
    noise_texture.location = (0.0, 0.0)
    mapping_001.location = (0.0, 0.0)
    texture_coordinate_001.location = (0.0, 0.0)
    bump.location = (0.0, 0.0)
    color_ramp.location = (0.0, 0.0)
    noise_texture_001.location = (0.0, 0.0)
    color_ramp_001.location = (0.0, 0.0)
    mix.location = (0.0, 0.0)
    mix_001.location = (0.0, 0.0)
    geometry.location = (0.0, 0.0)
    color_ramp_002.location = (0.0, 0.0)
    mix_003.location = (0.0, 0.0)
    color_ramp_004.location = (0.0, 0.0)
    noise_texture_003.location = (0.0, 0.0)
    bump_001.location = (0.0, 0.0)
    frame_001.location = (0.0, 0.0)
    frame_002.location = (0.0, 0.0)
    frame.location = (0.0, 0.0)
    hue_saturation_value.location = (0.0, 0.0)
    frame_003.location = (0.0, 0.0)
    principled_bsdf.location = (0.0, 0.0)
    math_1.location = (0.0, 0.0)
    group_001.location = (0.0, 0.0)
    voronoi_texture.location = (0.0, 0.0)
    bump_002.location = (0.0, 0.0)
    color_ramp_005.location = (0.0, 0.0)
    voronoi_texture_001.location = (0.0, 0.0)
    color_ramp_006.location = (0.0, 0.0)
    math_001_1.location = (0.0, 0.0)
    bump_003.location = (0.0, 0.0)
    map_range_004.location = (0.0, 0.0)
    group_002.location = (0.0, 0.0)
    math_002.location = (0.0, 0.0)
    math_003.location = (0.0, 0.0)
    math_004.location = (0.0, 0.0)

    #Set dimensions
    group_output_1.width, group_output_1.height = 140.0, 100.0
    group_input_1.width, group_input_1.height = 140.0, 100.0
    noise_texture.width, noise_texture.height = 140.0, 100.0
    mapping_001.width, mapping_001.height = 140.0, 100.0
    texture_coordinate_001.width, texture_coordinate_001.height = 140.0, 100.0
    bump.width, bump.height = 140.0, 100.0
    color_ramp.width, color_ramp.height = 240.0, 100.0
    noise_texture_001.width, noise_texture_001.height = 140.0, 100.0
    color_ramp_001.width, color_ramp_001.height = 240.0, 100.0
    mix.width, mix.height = 140.0, 100.0
    mix_001.width, mix_001.height = 140.0, 100.0
    geometry.width, geometry.height = 140.0, 100.0
    color_ramp_002.width, color_ramp_002.height = 240.0, 100.0
    mix_003.width, mix_003.height = 140.0, 100.0
    color_ramp_004.width, color_ramp_004.height = 240.0, 100.0
    noise_texture_003.width, noise_texture_003.height = 140.0, 100.0
    bump_001.width, bump_001.height = 140.0, 100.0
    frame_001.width, frame_001.height = 150.0, 100.0
    frame_002.width, frame_002.height = 150.0, 100.0
    frame.width, frame.height = 150.0, 100.0
    hue_saturation_value.width, hue_saturation_value.height = 150.0, 100.0
    frame_003.width, frame_003.height = 150.0, 100.0
    principled_bsdf.width, principled_bsdf.height = 240.0, 100.0
    math_1.width, math_1.height = 140.0, 100.0
    group_001.width, group_001.height = 140.0, 100.0
    voronoi_texture.width, voronoi_texture.height = 140.0, 100.0
    bump_002.width, bump_002.height = 140.0, 100.0
    color_ramp_005.width, color_ramp_005.height = 240.0, 100.0
    voronoi_texture_001.width, voronoi_texture_001.height = 140.0, 100.0
    color_ramp_006.width, color_ramp_006.height = 240.0, 100.0
    math_001_1.width, math_001_1.height = 140.0, 100.0
    bump_003.width, bump_003.height = 140.0, 100.0
    map_range_004.width, map_range_004.height = 140.0, 100.0
    group_002.width, group_002.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0

    #initialize moonrockshader links
    #mapping_001.Vector -> noise_texture_001.Vector
    moonrockshader.links.new(mapping_001.outputs[0], noise_texture_001.inputs[0])
    #noise_texture_001.Fac -> color_ramp_001.Fac
    moonrockshader.links.new(noise_texture_001.outputs[0], color_ramp_001.inputs[0])
    #color_ramp_001.Color -> mix.B
    moonrockshader.links.new(color_ramp_001.outputs[0], mix.inputs[7])
    #color_ramp_004.Color -> hue_saturation_value.Color
    moonrockshader.links.new(color_ramp_004.outputs[0], hue_saturation_value.inputs[4])
    #mix_001.Result -> mix_003.A
    moonrockshader.links.new(mix_001.outputs[2], mix_003.inputs[6])
    #mix_003.Result -> principled_bsdf.Base Color
    moonrockshader.links.new(mix_003.outputs[2], principled_bsdf.inputs[0])
    #color_ramp_002.Color -> mix_003.Factor
    moonrockshader.links.new(color_ramp_002.outputs[0], mix_003.inputs[0])
    #hue_saturation_value.Color -> principled_bsdf.Roughness
    moonrockshader.links.new(hue_saturation_value.outputs[0], principled_bsdf.inputs[2])
    #color_ramp.Color -> mix.A
    moonrockshader.links.new(color_ramp.outputs[0], mix.inputs[6])
    #mix.Result -> color_ramp_004.Fac
    moonrockshader.links.new(mix.outputs[2], color_ramp_004.inputs[0])
    #mapping_001.Vector -> noise_texture_003.Vector
    moonrockshader.links.new(mapping_001.outputs[0], noise_texture_003.inputs[0])
    #bump.Normal -> bump_001.Normal
    moonrockshader.links.new(bump.outputs[0], bump_001.inputs[4])
    #mix.Result -> mix_001.Factor
    moonrockshader.links.new(mix.outputs[2], mix_001.inputs[0])
    #mapping_001.Vector -> noise_texture.Vector
    moonrockshader.links.new(mapping_001.outputs[0], noise_texture.inputs[0])
    #geometry.Pointiness -> color_ramp_002.Fac
    moonrockshader.links.new(geometry.outputs[7], color_ramp_002.inputs[0])
    #mix.Result -> bump_001.Height
    moonrockshader.links.new(mix.outputs[2], bump_001.inputs[3])
    #noise_texture.Fac -> color_ramp.Fac
    moonrockshader.links.new(noise_texture.outputs[0], color_ramp.inputs[0])
    #texture_coordinate_001.Object -> mapping_001.Vector
    moonrockshader.links.new(texture_coordinate_001.outputs[3], mapping_001.inputs[0])
    #principled_bsdf.BSDF -> group_output_1.BSDF
    moonrockshader.links.new(principled_bsdf.outputs[0], group_output_1.inputs[0])
    #group_input_1.scale -> mapping_001.Scale
    moonrockshader.links.new(group_input_1.outputs[0], mapping_001.inputs[3])
    #group_input_1.color1 -> mix_001.A
    moonrockshader.links.new(group_input_1.outputs[1], mix_001.inputs[6])
    #group_input_1.color2 -> mix_001.B
    moonrockshader.links.new(group_input_1.outputs[2], mix_001.inputs[7])
    #group_input_1.edge_color -> mix_003.B
    moonrockshader.links.new(group_input_1.outputs[3], mix_003.inputs[7])
    #group_input_1.noise_detail -> noise_texture.Detail
    moonrockshader.links.new(group_input_1.outputs[5], noise_texture.inputs[3])
    #group_input_1.noise_roughness -> noise_texture.Roughness
    moonrockshader.links.new(group_input_1.outputs[6], noise_texture.inputs[4])
    #group_input_1.noise_detail -> noise_texture_001.Detail
    moonrockshader.links.new(group_input_1.outputs[5], noise_texture_001.inputs[3])
    #group_input_1.noise_roughness -> noise_texture_001.Roughness
    moonrockshader.links.new(group_input_1.outputs[6], noise_texture_001.inputs[4])
    #group_input_1.roughness -> hue_saturation_value.Value
    moonrockshader.links.new(group_input_1.outputs[9], hue_saturation_value.inputs[2])
    #group_input_1.noise_bump_strength -> bump.Strength
    moonrockshader.links.new(group_input_1.outputs[11], bump.inputs[0])
    #group_input_1.noise_bump_scale -> noise_texture_003.Scale
    moonrockshader.links.new(group_input_1.outputs[10], noise_texture_003.inputs[2])
    #group_input_1.detailed_noise_bump_strength -> bump_001.Strength
    moonrockshader.links.new(group_input_1.outputs[12], bump_001.inputs[0])
    #group_input_1.noise_scale -> noise_texture_001.Scale
    moonrockshader.links.new(group_input_1.outputs[4], noise_texture_001.inputs[2])
    #group_input_1.noise_scale_mixer -> mix.Factor
    moonrockshader.links.new(group_input_1.outputs[14], mix.inputs[0])
    #group_input_1.noise_scale -> math_1.Value
    moonrockshader.links.new(group_input_1.outputs[4], math_1.inputs[0])
    #math_1.Value -> noise_texture.Scale
    moonrockshader.links.new(math_1.outputs[0], noise_texture.inputs[2])
    #group_input_1.noise_bump_roughness -> noise_texture_003.Roughness
    moonrockshader.links.new(group_input_1.outputs[15], noise_texture_003.inputs[4])
    #group_001.4 -> noise_texture_001.W
    moonrockshader.links.new(group_001.outputs[4], noise_texture_001.inputs[1])
    #group_001.3 -> noise_texture.W
    moonrockshader.links.new(group_001.outputs[3], noise_texture.inputs[1])
    #group_001.1 -> noise_texture_003.W
    moonrockshader.links.new(group_001.outputs[1], noise_texture_003.inputs[1])
    #bump_001.Normal -> principled_bsdf.Normal
    moonrockshader.links.new(bump_001.outputs[0], principled_bsdf.inputs[5])
    #noise_texture_003.Fac -> bump.Height
    moonrockshader.links.new(noise_texture_003.outputs[0], bump.inputs[3])
    #mapping_001.Vector -> voronoi_texture.Vector
    moonrockshader.links.new(mapping_001.outputs[0], voronoi_texture.inputs[0])
    #group_001.1 -> voronoi_texture.W
    moonrockshader.links.new(group_001.outputs[1], voronoi_texture.inputs[1])
    #color_ramp_005.Color -> bump_002.Height
    moonrockshader.links.new(color_ramp_005.outputs[0], bump_002.inputs[3])
    #bump_002.Normal -> bump.Normal
    moonrockshader.links.new(bump_002.outputs[0], bump.inputs[4])
    #voronoi_texture.Distance -> color_ramp_005.Fac
    moonrockshader.links.new(voronoi_texture.outputs[0], color_ramp_005.inputs[0])
    #group_input_1.voronoi_bump_scale -> voronoi_texture.Scale
    moonrockshader.links.new(group_input_1.outputs[16], voronoi_texture.inputs[2])
    #mapping_001.Vector -> voronoi_texture_001.Vector
    moonrockshader.links.new(mapping_001.outputs[0], voronoi_texture_001.inputs[0])
    #group_001.1 -> voronoi_texture_001.W
    moonrockshader.links.new(group_001.outputs[1], voronoi_texture_001.inputs[1])
    #math_001_1.Value -> voronoi_texture_001.Scale
    moonrockshader.links.new(math_001_1.outputs[0], voronoi_texture_001.inputs[2])
    #voronoi_texture_001.Distance -> color_ramp_006.Fac
    moonrockshader.links.new(voronoi_texture_001.outputs[0], color_ramp_006.inputs[0])
    #group_input_1.voronoi_bump_scale -> math_001_1.Value
    moonrockshader.links.new(group_input_1.outputs[16], math_001_1.inputs[0])
    #color_ramp_006.Color -> bump_003.Height
    moonrockshader.links.new(color_ramp_006.outputs[0], bump_003.inputs[3])
    #bump_003.Normal -> bump_002.Normal
    moonrockshader.links.new(bump_003.outputs[0], bump_002.inputs[4])
    #map_range_004.Result -> mapping_001.Location
    moonrockshader.links.new(map_range_004.outputs[0], mapping_001.inputs[1])
    #group_001.0 -> map_range_004.Value
    moonrockshader.links.new(group_001.outputs[0], map_range_004.inputs[0])
    #group_002.0 -> math_002.Value
    moonrockshader.links.new(group_002.outputs[0], math_002.inputs[1])
    #group_input_1.voronoi_bump_strength -> math_002.Value
    moonrockshader.links.new(group_input_1.outputs[17], math_002.inputs[0])
    #math_002.Value -> bump_003.Strength
    moonrockshader.links.new(math_002.outputs[0], bump_003.inputs[0])
    #group_001.2 -> group_002.Seed
    moonrockshader.links.new(group_001.outputs[2], group_002.inputs[0])
    #math_003.Value -> math_001_1.Value
    moonrockshader.links.new(math_003.outputs[0], math_001_1.inputs[1])
    #group_002.1 -> math_003.Value
    moonrockshader.links.new(group_002.outputs[1], math_003.inputs[0])
    #group_input_1.voronoi_bump_strength -> math_004.Value
    moonrockshader.links.new(group_input_1.outputs[17], math_004.inputs[0])
    #group_002.2 -> math_004.Value
    moonrockshader.links.new(group_002.outputs[2], math_004.inputs[1])
    #math_004.Value -> bump_002.Strength
    moonrockshader.links.new(math_004.outputs[0], bump_002.inputs[0])
    return moonrockshader

moonrockshader = moonrockshader_node_group()

#initialize MoonRockMat node group
def moonrockmat_node_group():

    moonrockmat = mat.node_tree
    #start with a clean node tree
    for node in moonrockmat.nodes:
        moonrockmat.nodes.remove(node)
    moonrockmat.color_tag = 'NONE'
    moonrockmat.description = ""
    moonrockmat.default_group_node_width = 140
    

    #moonrockmat interface

    #initialize moonrockmat nodes
    #node Material Output
    material_output = moonrockmat.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    #Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Thickness
    material_output.inputs[3].default_value = 0.0

    #node Group.006
    group_006 = moonrockmat.nodes.new("ShaderNodeGroup")
    group_006.name = "Group.006"
    group_006.node_tree = moonrockshader
    #Socket_1
    group_006.inputs[0].default_value = 16.0
    #Socket_2
    group_006.inputs[1].default_value = (0.24619978666305542, 0.24620160460472107, 0.2462015002965927, 1.0)
    #Socket_3
    group_006.inputs[2].default_value = (0.005181482061743736, 0.005181520711630583, 0.005181518383324146, 1.0)
    #Socket_4
    group_006.inputs[3].default_value = (0.4000000059604645, 0.4000000059604645, 0.4000000059604645, 1.0)
    #Socket_5
    group_006.inputs[4].default_value = 7.0
    #Socket_6
    group_006.inputs[5].default_value = 15.0
    #Socket_7
    group_006.inputs[6].default_value = 0.25
    #Socket_8
    group_006.inputs[7].default_value = 5.0
    #Socket_9
    group_006.inputs[8].default_value = 0.800000011920929
    #Socket_10
    group_006.inputs[9].default_value = 1.0
    #Socket_11
    group_006.inputs[10].default_value = 15.0
    #Socket_12
    group_006.inputs[11].default_value = 0.05000000074505806
    #Socket_13
    group_006.inputs[12].default_value = 0.25
    #Socket_14
    group_006.inputs[13].default_value = 0.75
    #Socket_15
    group_006.inputs[14].default_value = 0.009999999776482582
    #Socket_16
    group_006.inputs[15].default_value = 1.0
    #Socket_17
    group_006.inputs[16].default_value = 20.0
    #Socket_18
    group_006.inputs[17].default_value = 0.75


    #Set locations
    material_output.location = (0.0, 0.0)
    group_006.location = (0.0, 0.0)

    #Set dimensions
    material_output.width, material_output.height = 140.0, 100.0
    group_006.width, group_006.height = 140.0, 100.0

    #initialize moonrockmat links
    #group_006.BSDF -> material_output.Surface
    moonrockmat.links.new(group_006.outputs[0], material_output.inputs[0])
    return moonrockmat

moonrockmat = moonrockmat_node_group()


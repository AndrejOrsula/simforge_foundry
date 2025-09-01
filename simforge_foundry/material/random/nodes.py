import bpy, mathutils

#initialize random__uniform_ node group
def random__uniform__node_group():
    random__uniform_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Random (Uniform)")

    random__uniform_.color_tag = 'NONE'
    random__uniform_.description = ""
    random__uniform_.default_group_node_width = 140
    


    #random__uniform_ interface
    #Socket Value
    value_socket = random__uniform_.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket.default_value = 0.0
    value_socket.min_value = -3.4028234663852886e+38
    value_socket.max_value = 3.4028234663852886e+38
    value_socket.subtype = 'NONE'
    value_socket.attribute_domain = 'POINT'
    value_socket.default_input = 'VALUE'
    value_socket.structure_type = 'AUTO'

    #Socket Min
    min_socket = random__uniform_.interface.new_socket(name = "Min", in_out='INPUT', socket_type = 'NodeSocketFloat')
    min_socket.default_value = 0.0
    min_socket.min_value = -3.4028234663852886e+38
    min_socket.max_value = 3.4028234663852886e+38
    min_socket.subtype = 'NONE'
    min_socket.attribute_domain = 'POINT'
    min_socket.default_input = 'VALUE'
    min_socket.structure_type = 'AUTO'

    #Socket Max
    max_socket = random__uniform_.interface.new_socket(name = "Max", in_out='INPUT', socket_type = 'NodeSocketFloat')
    max_socket.default_value = 1.0
    max_socket.min_value = -3.4028234663852886e+38
    max_socket.max_value = 3.4028234663852886e+38
    max_socket.subtype = 'NONE'
    max_socket.attribute_domain = 'POINT'
    max_socket.default_input = 'VALUE'
    max_socket.structure_type = 'AUTO'

    #Socket Seed
    seed_socket = random__uniform_.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket.default_value = 0
    seed_socket.min_value = -2147483648
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.hide_value = True
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'

    #Socket Offset
    offset_socket = random__uniform_.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
    offset_socket.default_value = 0
    offset_socket.min_value = 0
    offset_socket.max_value = 2147483647
    offset_socket.subtype = 'NONE'
    offset_socket.attribute_domain = 'POINT'
    offset_socket.default_input = 'VALUE'
    offset_socket.structure_type = 'AUTO'


    #initialize random__uniform_ nodes
    #node Group Output
    group_output = random__uniform_.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = random__uniform_.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Random Value.011
    random_value_011 = random__uniform_.nodes.new("FunctionNodeRandomValue")
    random_value_011.name = "Random Value.011"
    random_value_011.data_type = 'FLOAT'





    #Set locations
    group_output.location = (190.0, 0.0)
    group_input.location = (-200.0, 0.0)
    random_value_011.location = (0.0, 0.0)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    random_value_011.width, random_value_011.height = 140.0, 100.0

    #initialize random__uniform_ links
    #random_value_011.Value -> group_output.Value
    random__uniform_.links.new(random_value_011.outputs[1], group_output.inputs[0])
    #group_input.Min -> random_value_011.Min
    random__uniform_.links.new(group_input.outputs[0], random_value_011.inputs[2])
    #group_input.Max -> random_value_011.Max
    random__uniform_.links.new(group_input.outputs[1], random_value_011.inputs[3])
    #group_input.Offset -> random_value_011.ID
    random__uniform_.links.new(group_input.outputs[3], random_value_011.inputs[7])
    #group_input.Seed -> random_value_011.Seed
    random__uniform_.links.new(group_input.outputs[2], random_value_011.inputs[8])
    return random__uniform_

random__uniform_ = random__uniform__node_group()

#initialize random_material node group
def random_material_node_group():
    random_material = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "random_material")

    random_material.color_tag = 'NONE'
    random_material.description = ""
    random_material.default_group_node_width = 140
    

    random_material.is_modifier = True

    #random_material interface
    #Socket Geometry
    geometry_socket = random_material.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_1 = random_material.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket seed
    seed_socket_1 = random_material.interface.new_socket(name = "seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket_1.default_value = 0
    seed_socket_1.min_value = 0
    seed_socket_1.max_value = 2147483647
    seed_socket_1.subtype = 'NONE'
    seed_socket_1.attribute_domain = 'POINT'
    seed_socket_1.hide_value = True
    seed_socket_1.force_non_field = True
    seed_socket_1.default_input = 'VALUE'
    seed_socket_1.structure_type = 'SINGLE'

    #Socket mat_count
    mat_count_socket = random_material.interface.new_socket(name = "mat_count", in_out='INPUT', socket_type = 'NodeSocketInt')
    mat_count_socket.default_value = 2
    mat_count_socket.min_value = 2
    mat_count_socket.max_value = 2147483647
    mat_count_socket.subtype = 'NONE'
    mat_count_socket.attribute_domain = 'POINT'
    mat_count_socket.force_non_field = True
    mat_count_socket.default_input = 'VALUE'
    mat_count_socket.structure_type = 'SINGLE'

    #Socket mat0
    mat0_socket = random_material.interface.new_socket(name = "mat0", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat0_socket.attribute_domain = 'POINT'
    mat0_socket.default_input = 'VALUE'
    mat0_socket.structure_type = 'AUTO'

    #Socket mat1
    mat1_socket = random_material.interface.new_socket(name = "mat1", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat1_socket.attribute_domain = 'POINT'
    mat1_socket.default_input = 'VALUE'
    mat1_socket.structure_type = 'AUTO'

    #Socket mat2
    mat2_socket = random_material.interface.new_socket(name = "mat2", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat2_socket.attribute_domain = 'POINT'
    mat2_socket.default_input = 'VALUE'
    mat2_socket.structure_type = 'AUTO'

    #Socket mat3
    mat3_socket = random_material.interface.new_socket(name = "mat3", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat3_socket.attribute_domain = 'POINT'
    mat3_socket.default_input = 'VALUE'
    mat3_socket.structure_type = 'AUTO'

    #Socket mat4
    mat4_socket = random_material.interface.new_socket(name = "mat4", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat4_socket.attribute_domain = 'POINT'
    mat4_socket.default_input = 'VALUE'
    mat4_socket.structure_type = 'AUTO'

    #Socket mat5
    mat5_socket = random_material.interface.new_socket(name = "mat5", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat5_socket.attribute_domain = 'POINT'
    mat5_socket.default_input = 'VALUE'
    mat5_socket.structure_type = 'AUTO'

    #Socket mat6
    mat6_socket = random_material.interface.new_socket(name = "mat6", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat6_socket.attribute_domain = 'POINT'
    mat6_socket.default_input = 'VALUE'
    mat6_socket.structure_type = 'AUTO'

    #Socket mat7
    mat7_socket = random_material.interface.new_socket(name = "mat7", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat7_socket.attribute_domain = 'POINT'
    mat7_socket.default_input = 'VALUE'
    mat7_socket.structure_type = 'AUTO'

    #Socket mat8
    mat8_socket = random_material.interface.new_socket(name = "mat8", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat8_socket.attribute_domain = 'POINT'
    mat8_socket.default_input = 'VALUE'
    mat8_socket.structure_type = 'AUTO'

    #Socket mat9
    mat9_socket = random_material.interface.new_socket(name = "mat9", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat9_socket.attribute_domain = 'POINT'
    mat9_socket.default_input = 'VALUE'
    mat9_socket.structure_type = 'AUTO'

    #Socket mat10
    mat10_socket = random_material.interface.new_socket(name = "mat10", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat10_socket.attribute_domain = 'POINT'
    mat10_socket.default_input = 'VALUE'
    mat10_socket.structure_type = 'AUTO'

    #Socket mat11
    mat11_socket = random_material.interface.new_socket(name = "mat11", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat11_socket.attribute_domain = 'POINT'
    mat11_socket.default_input = 'VALUE'
    mat11_socket.structure_type = 'AUTO'

    #Socket mat12
    mat12_socket = random_material.interface.new_socket(name = "mat12", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat12_socket.attribute_domain = 'POINT'
    mat12_socket.default_input = 'VALUE'
    mat12_socket.structure_type = 'AUTO'

    #Socket mat13
    mat13_socket = random_material.interface.new_socket(name = "mat13", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat13_socket.attribute_domain = 'POINT'
    mat13_socket.default_input = 'VALUE'
    mat13_socket.structure_type = 'AUTO'

    #Socket mat14
    mat14_socket = random_material.interface.new_socket(name = "mat14", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat14_socket.attribute_domain = 'POINT'
    mat14_socket.default_input = 'VALUE'
    mat14_socket.structure_type = 'AUTO'

    #Socket mat15
    mat15_socket = random_material.interface.new_socket(name = "mat15", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat15_socket.attribute_domain = 'POINT'
    mat15_socket.default_input = 'VALUE'
    mat15_socket.structure_type = 'AUTO'

    #Socket mat16
    mat16_socket = random_material.interface.new_socket(name = "mat16", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat16_socket.attribute_domain = 'POINT'
    mat16_socket.default_input = 'VALUE'
    mat16_socket.structure_type = 'AUTO'

    #Socket mat17
    mat17_socket = random_material.interface.new_socket(name = "mat17", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat17_socket.attribute_domain = 'POINT'
    mat17_socket.default_input = 'VALUE'
    mat17_socket.structure_type = 'AUTO'

    #Socket mat18
    mat18_socket = random_material.interface.new_socket(name = "mat18", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat18_socket.attribute_domain = 'POINT'
    mat18_socket.default_input = 'VALUE'
    mat18_socket.structure_type = 'AUTO'

    #Socket mat19
    mat19_socket = random_material.interface.new_socket(name = "mat19", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat19_socket.attribute_domain = 'POINT'
    mat19_socket.default_input = 'VALUE'
    mat19_socket.structure_type = 'AUTO'

    #Socket mat20
    mat20_socket = random_material.interface.new_socket(name = "mat20", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat20_socket.attribute_domain = 'POINT'
    mat20_socket.default_input = 'VALUE'
    mat20_socket.structure_type = 'AUTO'

    #Socket mat21
    mat21_socket = random_material.interface.new_socket(name = "mat21", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat21_socket.attribute_domain = 'POINT'
    mat21_socket.default_input = 'VALUE'
    mat21_socket.structure_type = 'AUTO'

    #Socket mat22
    mat22_socket = random_material.interface.new_socket(name = "mat22", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat22_socket.attribute_domain = 'POINT'
    mat22_socket.default_input = 'VALUE'
    mat22_socket.structure_type = 'AUTO'

    #Socket mat23
    mat23_socket = random_material.interface.new_socket(name = "mat23", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat23_socket.attribute_domain = 'POINT'
    mat23_socket.default_input = 'VALUE'
    mat23_socket.structure_type = 'AUTO'

    #Socket mat24
    mat24_socket = random_material.interface.new_socket(name = "mat24", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat24_socket.attribute_domain = 'POINT'
    mat24_socket.default_input = 'VALUE'
    mat24_socket.structure_type = 'AUTO'

    #Socket mat25
    mat25_socket = random_material.interface.new_socket(name = "mat25", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat25_socket.attribute_domain = 'POINT'
    mat25_socket.default_input = 'VALUE'
    mat25_socket.structure_type = 'AUTO'

    #Socket mat26
    mat26_socket = random_material.interface.new_socket(name = "mat26", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat26_socket.attribute_domain = 'POINT'
    mat26_socket.default_input = 'VALUE'
    mat26_socket.structure_type = 'AUTO'

    #Socket mat27
    mat27_socket = random_material.interface.new_socket(name = "mat27", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat27_socket.attribute_domain = 'POINT'
    mat27_socket.default_input = 'VALUE'
    mat27_socket.structure_type = 'AUTO'

    #Socket mat28
    mat28_socket = random_material.interface.new_socket(name = "mat28", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat28_socket.attribute_domain = 'POINT'
    mat28_socket.default_input = 'VALUE'
    mat28_socket.structure_type = 'AUTO'

    #Socket mat29
    mat29_socket = random_material.interface.new_socket(name = "mat29", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat29_socket.attribute_domain = 'POINT'
    mat29_socket.default_input = 'VALUE'
    mat29_socket.structure_type = 'AUTO'

    #Socket mat30
    mat30_socket = random_material.interface.new_socket(name = "mat30", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat30_socket.attribute_domain = 'POINT'
    mat30_socket.default_input = 'VALUE'
    mat30_socket.structure_type = 'AUTO'

    #Socket mat31
    mat31_socket = random_material.interface.new_socket(name = "mat31", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat31_socket.attribute_domain = 'POINT'
    mat31_socket.default_input = 'VALUE'
    mat31_socket.structure_type = 'AUTO'


    #initialize random_material nodes
    #node Group Input
    group_input_1 = random_material.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"

    #node Group Output
    group_output_1 = random_material.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    #node Index Switch
    index_switch = random_material.nodes.new("GeometryNodeIndexSwitch")
    index_switch.name = "Index Switch"
    index_switch.data_type = 'MATERIAL'
    index_switch.index_switch_items.clear()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()

    #node Random (Uniform)
    random__uniform__1 = random_material.nodes.new("GeometryNodeGroup")
    random__uniform__1.name = "Random (Uniform)"
    random__uniform__1.node_tree = random__uniform_
    #Socket_1
    random__uniform__1.inputs[0].default_value = 0.0
    #Socket_4
    random__uniform__1.inputs[3].default_value = 512

    #node Float to Integer
    float_to_integer = random_material.nodes.new("FunctionNodeFloatToInt")
    float_to_integer.name = "Float to Integer"
    float_to_integer.rounding_mode = 'ROUND'

    #node Set Material
    set_material = random_material.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    #Selection
    set_material.inputs[1].default_value = True

    #node Math
    math = random_material.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'SUBTRACT'
    math.use_clamp = False
    #Value_001
    math.inputs[1].default_value = 1.0





    #Set locations
    group_input_1.location = (-1158.7518310546875, -179.41915893554688)
    group_output_1.location = (200.0, 0.0)
    index_switch.location = (-288.44879150390625, -176.91915893554688)
    random__uniform__1.location = (-723.098876953125, -26.492406845092773)
    float_to_integer.location = (-533.098876953125, -57.992408752441406)
    set_material.location = (10.0, 10.0)
    math.location = (-913.098876953125, -33.492408752441406)

    #Set dimensions
    group_input_1.width, group_input_1.height = 140.0, 100.0
    group_output_1.width, group_output_1.height = 140.0, 100.0
    index_switch.width, index_switch.height = 140.0, 100.0
    random__uniform__1.width, random__uniform__1.height = 140.0, 100.0
    float_to_integer.width, float_to_integer.height = 140.0, 100.0
    set_material.width, set_material.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0

    #initialize random_material links
    #set_material.Geometry -> group_output_1.Geometry
    random_material.links.new(set_material.outputs[0], group_output_1.inputs[0])
    #float_to_integer.Integer -> index_switch.Index
    random_material.links.new(float_to_integer.outputs[0], index_switch.inputs[0])
    #random__uniform__1.Value -> float_to_integer.Float
    random_material.links.new(random__uniform__1.outputs[0], float_to_integer.inputs[0])
    #math.Value -> random__uniform__1.Max
    random_material.links.new(math.outputs[0], random__uniform__1.inputs[1])
    #group_input_1.mat0 -> index_switch.0
    random_material.links.new(group_input_1.outputs[3], index_switch.inputs[1])
    #group_input_1.mat1 -> index_switch.1
    random_material.links.new(group_input_1.outputs[4], index_switch.inputs[2])
    #group_input_1.mat2 -> index_switch.2
    random_material.links.new(group_input_1.outputs[5], index_switch.inputs[3])
    #group_input_1.mat3 -> index_switch.3
    random_material.links.new(group_input_1.outputs[6], index_switch.inputs[4])
    #group_input_1.mat4 -> index_switch.4
    random_material.links.new(group_input_1.outputs[7], index_switch.inputs[5])
    #group_input_1.mat5 -> index_switch.5
    random_material.links.new(group_input_1.outputs[8], index_switch.inputs[6])
    #group_input_1.mat6 -> index_switch.6
    random_material.links.new(group_input_1.outputs[9], index_switch.inputs[7])
    #group_input_1.mat7 -> index_switch.7
    random_material.links.new(group_input_1.outputs[10], index_switch.inputs[8])
    #group_input_1.mat8 -> index_switch.8
    random_material.links.new(group_input_1.outputs[11], index_switch.inputs[9])
    #group_input_1.mat9 -> index_switch.9
    random_material.links.new(group_input_1.outputs[12], index_switch.inputs[10])
    #group_input_1.mat10 -> index_switch.10
    random_material.links.new(group_input_1.outputs[13], index_switch.inputs[11])
    #group_input_1.mat11 -> index_switch.11
    random_material.links.new(group_input_1.outputs[14], index_switch.inputs[12])
    #group_input_1.mat12 -> index_switch.12
    random_material.links.new(group_input_1.outputs[15], index_switch.inputs[13])
    #group_input_1.mat13 -> index_switch.13
    random_material.links.new(group_input_1.outputs[16], index_switch.inputs[14])
    #group_input_1.mat14 -> index_switch.14
    random_material.links.new(group_input_1.outputs[17], index_switch.inputs[15])
    #group_input_1.mat15 -> index_switch.15
    random_material.links.new(group_input_1.outputs[18], index_switch.inputs[16])
    #group_input_1.Geometry -> set_material.Geometry
    random_material.links.new(group_input_1.outputs[0], set_material.inputs[0])
    #index_switch.Output -> set_material.Material
    random_material.links.new(index_switch.outputs[0], set_material.inputs[2])
    #group_input_1.mat_count -> math.Value
    random_material.links.new(group_input_1.outputs[2], math.inputs[0])
    #group_input_1.seed -> random__uniform__1.Seed
    random_material.links.new(group_input_1.outputs[1], random__uniform__1.inputs[2])
    #group_input_1.mat16 -> index_switch.16
    random_material.links.new(group_input_1.outputs[19], index_switch.inputs[17])
    #group_input_1.mat17 -> index_switch.17
    random_material.links.new(group_input_1.outputs[20], index_switch.inputs[18])
    #group_input_1.mat18 -> index_switch.18
    random_material.links.new(group_input_1.outputs[21], index_switch.inputs[19])
    #group_input_1.mat19 -> index_switch.19
    random_material.links.new(group_input_1.outputs[22], index_switch.inputs[20])
    #group_input_1.mat20 -> index_switch.20
    random_material.links.new(group_input_1.outputs[23], index_switch.inputs[21])
    #group_input_1.mat21 -> index_switch.21
    random_material.links.new(group_input_1.outputs[24], index_switch.inputs[22])
    #group_input_1.mat22 -> index_switch.22
    random_material.links.new(group_input_1.outputs[25], index_switch.inputs[23])
    #group_input_1.mat23 -> index_switch.23
    random_material.links.new(group_input_1.outputs[26], index_switch.inputs[24])
    #group_input_1.mat24 -> index_switch.24
    random_material.links.new(group_input_1.outputs[27], index_switch.inputs[25])
    #group_input_1.mat25 -> index_switch.25
    random_material.links.new(group_input_1.outputs[28], index_switch.inputs[26])
    #group_input_1.mat26 -> index_switch.26
    random_material.links.new(group_input_1.outputs[29], index_switch.inputs[27])
    #group_input_1.mat27 -> index_switch.27
    random_material.links.new(group_input_1.outputs[30], index_switch.inputs[28])
    #group_input_1.mat28 -> index_switch.28
    random_material.links.new(group_input_1.outputs[31], index_switch.inputs[29])
    #group_input_1.mat29 -> index_switch.29
    random_material.links.new(group_input_1.outputs[32], index_switch.inputs[30])
    #group_input_1.mat30 -> index_switch.30
    random_material.links.new(group_input_1.outputs[33], index_switch.inputs[31])
    #group_input_1.mat31 -> index_switch.31
    random_material.links.new(group_input_1.outputs[34], index_switch.inputs[32])
    return random_material

random_material = random_material_node_group()


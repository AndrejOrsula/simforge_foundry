import bpy, mathutils

#initialize shape_scoop_profile_x node group
def shape_scoop_profile_x_node_group():
    shape_scoop_profile_x = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "shape_scoop_profile_x")

    shape_scoop_profile_x.color_tag = 'NONE'
    shape_scoop_profile_x.description = ""
    shape_scoop_profile_x.default_group_node_width = 140
    


    #shape_scoop_profile_x interface
    #Socket Geometry
    geometry_socket = shape_scoop_profile_x.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_1 = shape_scoop_profile_x.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    #Socket B
    b_socket = shape_scoop_profile_x.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketFloat')
    b_socket.default_value = 0.0
    b_socket.min_value = -10000.0
    b_socket.max_value = 10000.0
    b_socket.subtype = 'NONE'
    b_socket.attribute_domain = 'POINT'
    b_socket.default_input = 'VALUE'
    b_socket.structure_type = 'AUTO'

    #Socket Value
    value_socket = shape_scoop_profile_x.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
    value_socket.default_value = 0.5
    value_socket.min_value = -10000.0
    value_socket.max_value = 10000.0
    value_socket.subtype = 'NONE'
    value_socket.attribute_domain = 'POINT'
    value_socket.default_input = 'VALUE'
    value_socket.structure_type = 'AUTO'

    #Socket B
    b_socket_1 = shape_scoop_profile_x.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketFloat')
    b_socket_1.default_value = 0.0
    b_socket_1.min_value = -10000.0
    b_socket_1.max_value = 10000.0
    b_socket_1.subtype = 'NONE'
    b_socket_1.attribute_domain = 'POINT'
    b_socket_1.default_input = 'VALUE'
    b_socket_1.structure_type = 'AUTO'

    #Socket Value
    value_socket_1 = shape_scoop_profile_x.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
    value_socket_1.default_value = 1.0
    value_socket_1.min_value = -10000.0
    value_socket_1.max_value = 10000.0
    value_socket_1.subtype = 'NONE'
    value_socket_1.attribute_domain = 'POINT'
    value_socket_1.default_input = 'VALUE'
    value_socket_1.structure_type = 'AUTO'

    #Socket Value
    value_socket_2 = shape_scoop_profile_x.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
    value_socket_2.default_value = 0.0
    value_socket_2.min_value = -10000.0
    value_socket_2.max_value = 10000.0
    value_socket_2.subtype = 'NONE'
    value_socket_2.attribute_domain = 'POINT'
    value_socket_2.default_input = 'VALUE'
    value_socket_2.structure_type = 'AUTO'

    #Socket Value
    value_socket_3 = shape_scoop_profile_x.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
    value_socket_3.default_value = 1.0
    value_socket_3.min_value = -10000.0
    value_socket_3.max_value = 10000.0
    value_socket_3.subtype = 'NONE'
    value_socket_3.attribute_domain = 'POINT'
    value_socket_3.default_input = 'VALUE'
    value_socket_3.structure_type = 'AUTO'


    #initialize shape_scoop_profile_x nodes
    #node Group Output
    group_output = shape_scoop_profile_x.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = shape_scoop_profile_x.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Position
    position = shape_scoop_profile_x.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    #node Set Position.002
    set_position_002 = shape_scoop_profile_x.nodes.new("GeometryNodeSetPosition")
    set_position_002.name = "Set Position.002"
    #Position
    set_position_002.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Compare.001
    compare_001 = shape_scoop_profile_x.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = 'FLOAT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'
    #Epsilon
    compare_001.inputs[12].default_value = 0.0010000000474974513

    #node Separate XYZ
    separate_xyz = shape_scoop_profile_x.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"

    #node Math.001
    math_001 = shape_scoop_profile_x.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False

    #node Combine XYZ.003
    combine_xyz_003 = shape_scoop_profile_x.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"
    #Y
    combine_xyz_003.inputs[1].default_value = 0.0
    #Z
    combine_xyz_003.inputs[2].default_value = 0.0

    #node Math.002
    math_002 = shape_scoop_profile_x.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'MULTIPLY'
    math_002.use_clamp = False

    #node Math.004
    math_004 = shape_scoop_profile_x.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'MULTIPLY'
    math_004.use_clamp = False

    #node Math.006
    math_006 = shape_scoop_profile_x.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'DIVIDE'
    math_006.use_clamp = False

    #node Math.009
    math_009 = shape_scoop_profile_x.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.operation = 'SUBTRACT'
    math_009.use_clamp = False

    #node Math.007
    math_007 = shape_scoop_profile_x.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = 'POWER'
    math_007.use_clamp = False

    #node Math
    math = shape_scoop_profile_x.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'ADD'
    math.use_clamp = False

    #node Math.003
    math_003 = shape_scoop_profile_x.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'MAXIMUM'
    math_003.use_clamp = False
    #Value_001
    math_003.inputs[1].default_value = 0.0010000000474974513





    #Set locations
    group_output.location = (1025.1484375, 0.0)
    group_input.location = (-1370.8817138671875, 312.69720458984375)
    position.location = (-835.1494140625, -280.25518798828125)
    set_position_002.location = (812.584228515625, 173.17274475097656)
    compare_001.location = (1.802957534790039, -143.3256072998047)
    separate_xyz.location = (-657.9013671875, -226.158935546875)
    math_001.location = (-408.0556640625, 251.9854736328125)
    combine_xyz_003.location = (671.637939453125, 70.95906829833984)
    math_002.location = (-620.5380859375, 324.1671142578125)
    math_004.location = (18.1953125, 226.4578857421875)
    math_006.location = (228.814453125, 118.0130615234375)
    math_009.location = (-356.7545471191406, -107.78096008300781)
    math_007.location = (-162.1494140625, 48.4927978515625)
    math.location = (491.6842041015625, 76.58377075195312)
    math_003.location = (-1116.0667724609375, 128.42837524414062)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    position.width, position.height = 140.0, 100.0
    set_position_002.width, set_position_002.height = 140.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    combine_xyz_003.width, combine_xyz_003.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    math_009.width, math_009.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0

    #initialize shape_scoop_profile_x links
    #math_007.Value -> math_004.Value
    shape_scoop_profile_x.links.new(math_007.outputs[0], math_004.inputs[1])
    #separate_xyz.Z -> math_009.Value
    shape_scoop_profile_x.links.new(separate_xyz.outputs[2], math_009.inputs[1])
    #compare_001.Result -> set_position_002.Selection
    shape_scoop_profile_x.links.new(compare_001.outputs[0], set_position_002.inputs[1])
    #math.Value -> combine_xyz_003.X
    shape_scoop_profile_x.links.new(math.outputs[0], combine_xyz_003.inputs[0])
    #combine_xyz_003.Vector -> set_position_002.Offset
    shape_scoop_profile_x.links.new(combine_xyz_003.outputs[0], set_position_002.inputs[3])
    #math_001.Value -> math_004.Value
    shape_scoop_profile_x.links.new(math_001.outputs[0], math_004.inputs[0])
    #separate_xyz.X -> compare_001.A
    shape_scoop_profile_x.links.new(separate_xyz.outputs[0], compare_001.inputs[0])
    #math_004.Value -> math_006.Value
    shape_scoop_profile_x.links.new(math_004.outputs[0], math_006.inputs[0])
    #math_009.Value -> math_007.Value
    shape_scoop_profile_x.links.new(math_009.outputs[0], math_007.inputs[0])
    #position.Position -> separate_xyz.Vector
    shape_scoop_profile_x.links.new(position.outputs[0], separate_xyz.inputs[0])
    #math_002.Value -> math_001.Value
    shape_scoop_profile_x.links.new(math_002.outputs[0], math_001.inputs[0])
    #group_input.Geometry -> set_position_002.Geometry
    shape_scoop_profile_x.links.new(group_input.outputs[0], set_position_002.inputs[0])
    #group_input.Value -> math_002.Value
    shape_scoop_profile_x.links.new(group_input.outputs[2], math_002.inputs[0])
    #group_input.B -> compare_001.B
    shape_scoop_profile_x.links.new(group_input.outputs[1], compare_001.inputs[1])
    #group_input.B -> math_001.Value
    shape_scoop_profile_x.links.new(group_input.outputs[1], math_001.inputs[1])
    #group_input.B -> math_006.Value
    shape_scoop_profile_x.links.new(group_input.outputs[3], math_006.inputs[1])
    #group_input.B -> math_009.Value
    shape_scoop_profile_x.links.new(group_input.outputs[3], math_009.inputs[0])
    #math_003.Value -> math_007.Value
    shape_scoop_profile_x.links.new(math_003.outputs[0], math_007.inputs[1])
    #set_position_002.Geometry -> group_output.Geometry
    shape_scoop_profile_x.links.new(set_position_002.outputs[0], group_output.inputs[0])
    #math_006.Value -> math.Value
    shape_scoop_profile_x.links.new(math_006.outputs[0], math.inputs[0])
    #group_input.Value -> math.Value
    shape_scoop_profile_x.links.new(group_input.outputs[5], math.inputs[1])
    #group_input.Value -> math_002.Value
    shape_scoop_profile_x.links.new(group_input.outputs[6], math_002.inputs[1])
    #group_input.Value -> math_003.Value
    shape_scoop_profile_x.links.new(group_input.outputs[4], math_003.inputs[0])
    return shape_scoop_profile_x

shape_scoop_profile_x = shape_scoop_profile_x_node_group()

#initialize shape_scoop_profile_y node group
def shape_scoop_profile_y_node_group():
    shape_scoop_profile_y = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "shape_scoop_profile_y")

    shape_scoop_profile_y.color_tag = 'NONE'
    shape_scoop_profile_y.description = ""
    shape_scoop_profile_y.default_group_node_width = 140
    


    #shape_scoop_profile_y interface
    #Socket Geometry
    geometry_socket_2 = shape_scoop_profile_y.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_2.attribute_domain = 'POINT'
    geometry_socket_2.default_input = 'VALUE'
    geometry_socket_2.structure_type = 'AUTO'

    #Socket Geometry
    geometry_socket_3 = shape_scoop_profile_y.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_3.attribute_domain = 'POINT'
    geometry_socket_3.default_input = 'VALUE'
    geometry_socket_3.structure_type = 'AUTO'

    #Socket B
    b_socket_2 = shape_scoop_profile_y.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketFloat')
    b_socket_2.default_value = 0.0
    b_socket_2.min_value = -10000.0
    b_socket_2.max_value = 10000.0
    b_socket_2.subtype = 'NONE'
    b_socket_2.attribute_domain = 'POINT'
    b_socket_2.default_input = 'VALUE'
    b_socket_2.structure_type = 'AUTO'

    #Socket Value
    value_socket_4 = shape_scoop_profile_y.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
    value_socket_4.default_value = 0.5
    value_socket_4.min_value = -10000.0
    value_socket_4.max_value = 10000.0
    value_socket_4.subtype = 'NONE'
    value_socket_4.attribute_domain = 'POINT'
    value_socket_4.default_input = 'VALUE'
    value_socket_4.structure_type = 'AUTO'

    #Socket B
    b_socket_3 = shape_scoop_profile_y.interface.new_socket(name = "B", in_out='INPUT', socket_type = 'NodeSocketFloat')
    b_socket_3.default_value = 0.0
    b_socket_3.min_value = -10000.0
    b_socket_3.max_value = 10000.0
    b_socket_3.subtype = 'NONE'
    b_socket_3.attribute_domain = 'POINT'
    b_socket_3.default_input = 'VALUE'
    b_socket_3.structure_type = 'AUTO'

    #Socket Value
    value_socket_5 = shape_scoop_profile_y.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
    value_socket_5.default_value = 1.0
    value_socket_5.min_value = -10000.0
    value_socket_5.max_value = 10000.0
    value_socket_5.subtype = 'NONE'
    value_socket_5.attribute_domain = 'POINT'
    value_socket_5.default_input = 'VALUE'
    value_socket_5.structure_type = 'AUTO'

    #Socket Value
    value_socket_6 = shape_scoop_profile_y.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
    value_socket_6.default_value = 0.0
    value_socket_6.min_value = -10000.0
    value_socket_6.max_value = 10000.0
    value_socket_6.subtype = 'NONE'
    value_socket_6.attribute_domain = 'POINT'
    value_socket_6.default_input = 'VALUE'
    value_socket_6.structure_type = 'AUTO'

    #Socket Value
    value_socket_7 = shape_scoop_profile_y.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
    value_socket_7.default_value = 1.0
    value_socket_7.min_value = -10000.0
    value_socket_7.max_value = 10000.0
    value_socket_7.subtype = 'NONE'
    value_socket_7.attribute_domain = 'POINT'
    value_socket_7.default_input = 'VALUE'
    value_socket_7.structure_type = 'AUTO'


    #initialize shape_scoop_profile_y nodes
    #node Group Output
    group_output_1 = shape_scoop_profile_y.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    #node Group Input
    group_input_1 = shape_scoop_profile_y.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"

    #node Position
    position_1 = shape_scoop_profile_y.nodes.new("GeometryNodeInputPosition")
    position_1.name = "Position"

    #node Set Position.002
    set_position_002_1 = shape_scoop_profile_y.nodes.new("GeometryNodeSetPosition")
    set_position_002_1.name = "Set Position.002"
    #Position
    set_position_002_1.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Compare.001
    compare_001_1 = shape_scoop_profile_y.nodes.new("FunctionNodeCompare")
    compare_001_1.name = "Compare.001"
    compare_001_1.data_type = 'FLOAT'
    compare_001_1.mode = 'ELEMENT'
    compare_001_1.operation = 'EQUAL'
    #Epsilon
    compare_001_1.inputs[12].default_value = 0.0010000000474974513

    #node Separate XYZ
    separate_xyz_1 = shape_scoop_profile_y.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_1.name = "Separate XYZ"

    #node Math.001
    math_001_1 = shape_scoop_profile_y.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = 'MULTIPLY'
    math_001_1.use_clamp = False

    #node Combine XYZ.003
    combine_xyz_003_1 = shape_scoop_profile_y.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003_1.name = "Combine XYZ.003"
    #X
    combine_xyz_003_1.inputs[0].default_value = 0.0
    #Z
    combine_xyz_003_1.inputs[2].default_value = 0.0

    #node Math.002
    math_002_1 = shape_scoop_profile_y.nodes.new("ShaderNodeMath")
    math_002_1.name = "Math.002"
    math_002_1.operation = 'MULTIPLY'
    math_002_1.use_clamp = False

    #node Math.004
    math_004_1 = shape_scoop_profile_y.nodes.new("ShaderNodeMath")
    math_004_1.name = "Math.004"
    math_004_1.operation = 'MULTIPLY'
    math_004_1.use_clamp = False

    #node Math.006
    math_006_1 = shape_scoop_profile_y.nodes.new("ShaderNodeMath")
    math_006_1.name = "Math.006"
    math_006_1.operation = 'DIVIDE'
    math_006_1.use_clamp = False

    #node Math.009
    math_009_1 = shape_scoop_profile_y.nodes.new("ShaderNodeMath")
    math_009_1.name = "Math.009"
    math_009_1.operation = 'SUBTRACT'
    math_009_1.use_clamp = False

    #node Math.007
    math_007_1 = shape_scoop_profile_y.nodes.new("ShaderNodeMath")
    math_007_1.name = "Math.007"
    math_007_1.operation = 'POWER'
    math_007_1.use_clamp = False

    #node Math
    math_1 = shape_scoop_profile_y.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = 'ADD'
    math_1.use_clamp = False

    #node Math.003
    math_003_1 = shape_scoop_profile_y.nodes.new("ShaderNodeMath")
    math_003_1.name = "Math.003"
    math_003_1.operation = 'ABSOLUTE'
    math_003_1.use_clamp = False

    #node Math.005
    math_005 = shape_scoop_profile_y.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'SIGN'
    math_005.use_clamp = False

    #node Math.008
    math_008 = shape_scoop_profile_y.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = 'MULTIPLY'
    math_008.use_clamp = False

    #node Math.010
    math_010 = shape_scoop_profile_y.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.operation = 'MAXIMUM'
    math_010.use_clamp = False
    #Value_001
    math_010.inputs[1].default_value = 0.0010000000474974513





    #Set locations
    group_output_1.location = (1025.1484375, 0.0)
    group_input_1.location = (-1370.8817138671875, 312.69720458984375)
    position_1.location = (-1429.69140625, -346.23590087890625)
    set_position_002_1.location = (812.584228515625, 173.17274475097656)
    compare_001_1.location = (-375.1546936035156, -137.08633422851562)
    separate_xyz_1.location = (-1252.4434814453125, -292.1396789550781)
    math_001_1.location = (-785.0133666992188, 258.2247619628906)
    combine_xyz_003_1.location = (671.637939453125, 70.95906829833984)
    math_002_1.location = (-997.4957885742188, 330.4064025878906)
    math_004_1.location = (-358.7623596191406, 232.69715881347656)
    math_006_1.location = (-148.1432342529297, 124.25234985351562)
    math_009_1.location = (-733.7122192382812, -101.54167175292969)
    math_007_1.location = (-539.1071166992188, 54.732086181640625)
    math_1.location = (114.72652435302734, 82.82305908203125)
    math_003_1.location = (-782.2991943359375, -271.58685302734375)
    math_005.location = (-56.789154052734375, -271.25396728515625)
    math_008.location = (454.55279541015625, 11.940895080566406)
    math_010.location = (-1076.9453125, 109.70730590820312)

    #Set dimensions
    group_output_1.width, group_output_1.height = 140.0, 100.0
    group_input_1.width, group_input_1.height = 140.0, 100.0
    position_1.width, position_1.height = 140.0, 100.0
    set_position_002_1.width, set_position_002_1.height = 140.0, 100.0
    compare_001_1.width, compare_001_1.height = 140.0, 100.0
    separate_xyz_1.width, separate_xyz_1.height = 140.0, 100.0
    math_001_1.width, math_001_1.height = 140.0, 100.0
    combine_xyz_003_1.width, combine_xyz_003_1.height = 140.0, 100.0
    math_002_1.width, math_002_1.height = 140.0, 100.0
    math_004_1.width, math_004_1.height = 140.0, 100.0
    math_006_1.width, math_006_1.height = 140.0, 100.0
    math_009_1.width, math_009_1.height = 140.0, 100.0
    math_007_1.width, math_007_1.height = 140.0, 100.0
    math_1.width, math_1.height = 140.0, 100.0
    math_003_1.width, math_003_1.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    math_010.width, math_010.height = 140.0, 100.0

    #initialize shape_scoop_profile_y links
    #math_007_1.Value -> math_004_1.Value
    shape_scoop_profile_y.links.new(math_007_1.outputs[0], math_004_1.inputs[1])
    #separate_xyz_1.Z -> math_009_1.Value
    shape_scoop_profile_y.links.new(separate_xyz_1.outputs[2], math_009_1.inputs[1])
    #compare_001_1.Result -> set_position_002_1.Selection
    shape_scoop_profile_y.links.new(compare_001_1.outputs[0], set_position_002_1.inputs[1])
    #combine_xyz_003_1.Vector -> set_position_002_1.Offset
    shape_scoop_profile_y.links.new(combine_xyz_003_1.outputs[0], set_position_002_1.inputs[3])
    #math_001_1.Value -> math_004_1.Value
    shape_scoop_profile_y.links.new(math_001_1.outputs[0], math_004_1.inputs[0])
    #math_004_1.Value -> math_006_1.Value
    shape_scoop_profile_y.links.new(math_004_1.outputs[0], math_006_1.inputs[0])
    #math_009_1.Value -> math_007_1.Value
    shape_scoop_profile_y.links.new(math_009_1.outputs[0], math_007_1.inputs[0])
    #position_1.Position -> separate_xyz_1.Vector
    shape_scoop_profile_y.links.new(position_1.outputs[0], separate_xyz_1.inputs[0])
    #math_002_1.Value -> math_001_1.Value
    shape_scoop_profile_y.links.new(math_002_1.outputs[0], math_001_1.inputs[0])
    #group_input_1.Geometry -> set_position_002_1.Geometry
    shape_scoop_profile_y.links.new(group_input_1.outputs[0], set_position_002_1.inputs[0])
    #group_input_1.Value -> math_002_1.Value
    shape_scoop_profile_y.links.new(group_input_1.outputs[2], math_002_1.inputs[0])
    #group_input_1.B -> compare_001_1.B
    shape_scoop_profile_y.links.new(group_input_1.outputs[1], compare_001_1.inputs[1])
    #group_input_1.B -> math_001_1.Value
    shape_scoop_profile_y.links.new(group_input_1.outputs[1], math_001_1.inputs[1])
    #group_input_1.B -> math_006_1.Value
    shape_scoop_profile_y.links.new(group_input_1.outputs[3], math_006_1.inputs[1])
    #group_input_1.B -> math_009_1.Value
    shape_scoop_profile_y.links.new(group_input_1.outputs[3], math_009_1.inputs[0])
    #math_010.Value -> math_007_1.Value
    shape_scoop_profile_y.links.new(math_010.outputs[0], math_007_1.inputs[1])
    #set_position_002_1.Geometry -> group_output_1.Geometry
    shape_scoop_profile_y.links.new(set_position_002_1.outputs[0], group_output_1.inputs[0])
    #math_006_1.Value -> math_1.Value
    shape_scoop_profile_y.links.new(math_006_1.outputs[0], math_1.inputs[0])
    #group_input_1.Value -> math_1.Value
    shape_scoop_profile_y.links.new(group_input_1.outputs[5], math_1.inputs[1])
    #group_input_1.Value -> math_002_1.Value
    shape_scoop_profile_y.links.new(group_input_1.outputs[6], math_002_1.inputs[1])
    #math_008.Value -> combine_xyz_003_1.Y
    shape_scoop_profile_y.links.new(math_008.outputs[0], combine_xyz_003_1.inputs[1])
    #math_003_1.Value -> compare_001_1.A
    shape_scoop_profile_y.links.new(math_003_1.outputs[0], compare_001_1.inputs[0])
    #separate_xyz_1.Y -> math_003_1.Value
    shape_scoop_profile_y.links.new(separate_xyz_1.outputs[1], math_003_1.inputs[0])
    #separate_xyz_1.Y -> math_005.Value
    shape_scoop_profile_y.links.new(separate_xyz_1.outputs[1], math_005.inputs[0])
    #math_1.Value -> math_008.Value
    shape_scoop_profile_y.links.new(math_1.outputs[0], math_008.inputs[0])
    #math_005.Value -> math_008.Value
    shape_scoop_profile_y.links.new(math_005.outputs[0], math_008.inputs[1])
    #group_input_1.Value -> math_010.Value
    shape_scoop_profile_y.links.new(group_input_1.outputs[4], math_010.inputs[0])
    return shape_scoop_profile_y

shape_scoop_profile_y = shape_scoop_profile_y_node_group()

#initialize scoop node group
def scoop_node_group():
    scoop = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "scoop")

    scoop.color_tag = 'NONE'
    scoop.description = ""
    scoop.default_group_node_width = 140
    

    scoop.is_modifier = True

    #scoop interface
    #Socket Geometry
    geometry_socket_4 = scoop.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_4.attribute_domain = 'POINT'
    geometry_socket_4.default_input = 'VALUE'
    geometry_socket_4.structure_type = 'AUTO'

    #Socket scale
    scale_socket = scoop.interface.new_socket(name = "scale", in_out='INPUT', socket_type = 'NodeSocketVector')
    scale_socket.default_value = (0.17499999701976776, 0.15000000596046448, 0.20000000298023224)
    scale_socket.min_value = 0.0
    scale_socket.max_value = 10000.0
    scale_socket.subtype = 'TRANSLATION'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    #Socket base_vertices
    base_vertices_socket = scoop.interface.new_socket(name = "base_vertices", in_out='INPUT', socket_type = 'NodeSocketVector')
    base_vertices_socket.default_value = (2.0, 2.0, 3.0)
    base_vertices_socket.min_value = 2.0
    base_vertices_socket.max_value = 10.0
    base_vertices_socket.subtype = 'XYZ'
    base_vertices_socket.attribute_domain = 'POINT'
    base_vertices_socket.force_non_field = True
    base_vertices_socket.default_input = 'VALUE'
    base_vertices_socket.structure_type = 'SINGLE'

    #Socket mouth_open
    mouth_open_socket = scoop.interface.new_socket(name = "mouth_open", in_out='INPUT', socket_type = 'NodeSocketFloat')
    mouth_open_socket.default_value = 1.0
    mouth_open_socket.min_value = 0.0
    mouth_open_socket.max_value = 1.0
    mouth_open_socket.subtype = 'FACTOR'
    mouth_open_socket.attribute_domain = 'POINT'
    mouth_open_socket.force_non_field = True
    mouth_open_socket.default_input = 'VALUE'
    mouth_open_socket.structure_type = 'SINGLE'

    #Socket wall_thickness
    wall_thickness_socket = scoop.interface.new_socket(name = "wall_thickness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    wall_thickness_socket.default_value = 0.004000000189989805
    wall_thickness_socket.min_value = 0.0
    wall_thickness_socket.max_value = 3.4028234663852886e+38
    wall_thickness_socket.subtype = 'DISTANCE'
    wall_thickness_socket.attribute_domain = 'POINT'
    wall_thickness_socket.force_non_field = True
    wall_thickness_socket.default_input = 'VALUE'
    wall_thickness_socket.structure_type = 'SINGLE'

    #Socket subdivisions
    subdivisions_socket = scoop.interface.new_socket(name = "subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt')
    subdivisions_socket.default_value = 2
    subdivisions_socket.min_value = 0
    subdivisions_socket.max_value = 6
    subdivisions_socket.subtype = 'NONE'
    subdivisions_socket.attribute_domain = 'POINT'
    subdivisions_socket.force_non_field = True
    subdivisions_socket.default_input = 'VALUE'
    subdivisions_socket.structure_type = 'SINGLE'

    #Socket edge_crease
    edge_crease_socket = scoop.interface.new_socket(name = "edge_crease", in_out='INPUT', socket_type = 'NodeSocketFloat')
    edge_crease_socket.default_value = 0.10000000149011612
    edge_crease_socket.min_value = 0.0
    edge_crease_socket.max_value = 1.0
    edge_crease_socket.subtype = 'FACTOR'
    edge_crease_socket.attribute_domain = 'POINT'
    edge_crease_socket.force_non_field = True
    edge_crease_socket.default_input = 'VALUE'
    edge_crease_socket.structure_type = 'SINGLE'

    #Socket vertex_crease
    vertex_crease_socket = scoop.interface.new_socket(name = "vertex_crease", in_out='INPUT', socket_type = 'NodeSocketFloat')
    vertex_crease_socket.default_value = 0.05000000074505806
    vertex_crease_socket.min_value = 0.0
    vertex_crease_socket.max_value = 1.0
    vertex_crease_socket.subtype = 'FACTOR'
    vertex_crease_socket.attribute_domain = 'POINT'
    vertex_crease_socket.force_non_field = True
    vertex_crease_socket.default_input = 'VALUE'
    vertex_crease_socket.structure_type = 'SINGLE'

    #Socket material
    material_socket = scoop.interface.new_socket(name = "material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    material_socket.attribute_domain = 'POINT'
    material_socket.default_input = 'VALUE'
    material_socket.structure_type = 'AUTO'

    #Panel shape_
    shape__panel = scoop.interface.new_panel("shape_")
    #Panel shape_front_
    shape_front__panel = scoop.interface.new_panel("shape_front_")
    #Socket shape_front_lin
    shape_front_lin_socket = scoop.interface.new_socket(name = "shape_front_lin", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = shape_front__panel)
    shape_front_lin_socket.default_value = 0.0
    shape_front_lin_socket.min_value = -10000.0
    shape_front_lin_socket.max_value = 10000.0
    shape_front_lin_socket.subtype = 'NONE'
    shape_front_lin_socket.attribute_domain = 'POINT'
    shape_front_lin_socket.force_non_field = True
    shape_front_lin_socket.default_input = 'VALUE'
    shape_front_lin_socket.structure_type = 'SINGLE'

    #Socket shape_front_exp
    shape_front_exp_socket = scoop.interface.new_socket(name = "shape_front_exp", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = shape_front__panel)
    shape_front_exp_socket.default_value = 0.5
    shape_front_exp_socket.min_value = 0.0
    shape_front_exp_socket.max_value = 10000.0
    shape_front_exp_socket.subtype = 'NONE'
    shape_front_exp_socket.attribute_domain = 'POINT'
    shape_front_exp_socket.force_non_field = True
    shape_front_exp_socket.default_input = 'VALUE'
    shape_front_exp_socket.structure_type = 'SINGLE'

    #Socket shape_front_offset
    shape_front_offset_socket = scoop.interface.new_socket(name = "shape_front_offset", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = shape_front__panel)
    shape_front_offset_socket.default_value = 0.0
    shape_front_offset_socket.min_value = -10000.0
    shape_front_offset_socket.max_value = 10000.0
    shape_front_offset_socket.subtype = 'DISTANCE'
    shape_front_offset_socket.attribute_domain = 'POINT'
    shape_front_offset_socket.force_non_field = True
    shape_front_offset_socket.default_input = 'VALUE'
    shape_front_offset_socket.structure_type = 'SINGLE'


    scoop.interface.move_to_parent(shape_front__panel, shape__panel, 10)
    #Panel shape_back_
    shape_back__panel = scoop.interface.new_panel("shape_back_")
    #Socket shape_back_lin
    shape_back_lin_socket = scoop.interface.new_socket(name = "shape_back_lin", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = shape_back__panel)
    shape_back_lin_socket.default_value = 0.0
    shape_back_lin_socket.min_value = -10000.0
    shape_back_lin_socket.max_value = 10000.0
    shape_back_lin_socket.subtype = 'NONE'
    shape_back_lin_socket.attribute_domain = 'POINT'
    shape_back_lin_socket.force_non_field = True
    shape_back_lin_socket.default_input = 'VALUE'
    shape_back_lin_socket.structure_type = 'SINGLE'

    #Socket shape_back_exp
    shape_back_exp_socket = scoop.interface.new_socket(name = "shape_back_exp", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = shape_back__panel)
    shape_back_exp_socket.default_value = 0.5
    shape_back_exp_socket.min_value = -10000.0
    shape_back_exp_socket.max_value = 10000.0
    shape_back_exp_socket.subtype = 'NONE'
    shape_back_exp_socket.attribute_domain = 'POINT'
    shape_back_exp_socket.force_non_field = True
    shape_back_exp_socket.default_input = 'VALUE'
    shape_back_exp_socket.structure_type = 'SINGLE'

    #Socket shape_back_offset
    shape_back_offset_socket = scoop.interface.new_socket(name = "shape_back_offset", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = shape_back__panel)
    shape_back_offset_socket.default_value = 0.0
    shape_back_offset_socket.min_value = -10000.0
    shape_back_offset_socket.max_value = 10000.0
    shape_back_offset_socket.subtype = 'DISTANCE'
    shape_back_offset_socket.attribute_domain = 'POINT'
    shape_back_offset_socket.force_non_field = True
    shape_back_offset_socket.default_input = 'VALUE'
    shape_back_offset_socket.structure_type = 'SINGLE'


    scoop.interface.move_to_parent(shape_back__panel, shape__panel, 14)
    #Panel shape_sides_
    shape_sides__panel = scoop.interface.new_panel("shape_sides_")
    #Socket shape_sides_dir_out
    shape_sides_dir_out_socket = scoop.interface.new_socket(name = "shape_sides_dir_out", in_out='INPUT', socket_type = 'NodeSocketBool', parent = shape_sides__panel)
    shape_sides_dir_out_socket.default_value = True
    shape_sides_dir_out_socket.attribute_domain = 'POINT'
    shape_sides_dir_out_socket.force_non_field = True
    shape_sides_dir_out_socket.default_input = 'VALUE'
    shape_sides_dir_out_socket.structure_type = 'SINGLE'

    #Socket shape_sides_lin
    shape_sides_lin_socket = scoop.interface.new_socket(name = "shape_sides_lin", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = shape_sides__panel)
    shape_sides_lin_socket.default_value = 0.0
    shape_sides_lin_socket.min_value = -10000.0
    shape_sides_lin_socket.max_value = 10000.0
    shape_sides_lin_socket.subtype = 'NONE'
    shape_sides_lin_socket.attribute_domain = 'POINT'
    shape_sides_lin_socket.force_non_field = True
    shape_sides_lin_socket.default_input = 'VALUE'
    shape_sides_lin_socket.structure_type = 'SINGLE'

    #Socket shape_sides_exp
    shape_sides_exp_socket = scoop.interface.new_socket(name = "shape_sides_exp", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = shape_sides__panel)
    shape_sides_exp_socket.default_value = 0.5
    shape_sides_exp_socket.min_value = -10000.0
    shape_sides_exp_socket.max_value = 10000.0
    shape_sides_exp_socket.subtype = 'NONE'
    shape_sides_exp_socket.attribute_domain = 'POINT'
    shape_sides_exp_socket.force_non_field = True
    shape_sides_exp_socket.default_input = 'VALUE'
    shape_sides_exp_socket.structure_type = 'SINGLE'

    #Socket shape_sides_offset
    shape_sides_offset_socket = scoop.interface.new_socket(name = "shape_sides_offset", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = shape_sides__panel)
    shape_sides_offset_socket.default_value = 0.0
    shape_sides_offset_socket.min_value = -10000.0
    shape_sides_offset_socket.max_value = 10000.0
    shape_sides_offset_socket.subtype = 'DISTANCE'
    shape_sides_offset_socket.attribute_domain = 'POINT'
    shape_sides_offset_socket.force_non_field = True
    shape_sides_offset_socket.default_input = 'VALUE'
    shape_sides_offset_socket.structure_type = 'SINGLE'


    scoop.interface.move_to_parent(shape_sides__panel, shape__panel, 18)

    #Panel lip_
    lip__panel = scoop.interface.new_panel("lip_")
    #Socket lip_len
    lip_len_socket = scoop.interface.new_socket(name = "lip_len", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = lip__panel)
    lip_len_socket.default_value = 0.02500000037252903
    lip_len_socket.min_value = 0.0
    lip_len_socket.max_value = 3.4028234663852886e+38
    lip_len_socket.subtype = 'DISTANCE'
    lip_len_socket.attribute_domain = 'POINT'
    lip_len_socket.force_non_field = True
    lip_len_socket.default_input = 'VALUE'
    lip_len_socket.structure_type = 'SINGLE'

    #Socket lip_dir
    lip_dir_socket = scoop.interface.new_socket(name = "lip_dir", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = lip__panel)
    lip_dir_socket.default_value = -0.25
    lip_dir_socket.min_value = -3.4028234663852886e+38
    lip_dir_socket.max_value = 3.4028234663852886e+38
    lip_dir_socket.subtype = 'NONE'
    lip_dir_socket.attribute_domain = 'POINT'
    lip_dir_socket.force_non_field = True
    lip_dir_socket.default_input = 'VALUE'
    lip_dir_socket.structure_type = 'SINGLE'

    #Socket lip_width
    lip_width_socket = scoop.interface.new_socket(name = "lip_width", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = lip__panel)
    lip_width_socket.default_value = 0.800000011920929
    lip_width_socket.min_value = 0.0
    lip_width_socket.max_value = 1.0
    lip_width_socket.subtype = 'FACTOR'
    lip_width_socket.attribute_domain = 'POINT'
    lip_width_socket.force_non_field = True
    lip_width_socket.default_input = 'VALUE'
    lip_width_socket.structure_type = 'SINGLE'


    #Panel tooth_
    tooth__panel = scoop.interface.new_panel("tooth_")
    #Socket tooth_count
    tooth_count_socket = scoop.interface.new_socket(name = "tooth_count", in_out='INPUT', socket_type = 'NodeSocketInt', parent = tooth__panel)
    tooth_count_socket.default_value = 8
    tooth_count_socket.min_value = 0
    tooth_count_socket.max_value = 2147483647
    tooth_count_socket.subtype = 'NONE'
    tooth_count_socket.attribute_domain = 'POINT'
    tooth_count_socket.force_non_field = True
    tooth_count_socket.default_input = 'VALUE'
    tooth_count_socket.structure_type = 'SINGLE'

    #Socket tooth_scale
    tooth_scale_socket = scoop.interface.new_socket(name = "tooth_scale", in_out='INPUT', socket_type = 'NodeSocketVector', parent = tooth__panel)
    tooth_scale_socket.default_value = (0.019999999552965164, 0.009999999776482582, 0.0010000000474974513)
    tooth_scale_socket.min_value = 0.0
    tooth_scale_socket.max_value = 10000.0
    tooth_scale_socket.subtype = 'NONE'
    tooth_scale_socket.attribute_domain = 'POINT'
    tooth_scale_socket.force_non_field = True
    tooth_scale_socket.default_input = 'VALUE'
    tooth_scale_socket.structure_type = 'SINGLE'

    #Socket tooth_taper_scale
    tooth_taper_scale_socket = scoop.interface.new_socket(name = "tooth_taper_scale", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = tooth__panel)
    tooth_taper_scale_socket.default_value = 2.0
    tooth_taper_scale_socket.min_value = 1.0
    tooth_taper_scale_socket.max_value = 3.4028234663852886e+38
    tooth_taper_scale_socket.subtype = 'FACTOR'
    tooth_taper_scale_socket.attribute_domain = 'POINT'
    tooth_taper_scale_socket.force_non_field = True
    tooth_taper_scale_socket.default_input = 'VALUE'
    tooth_taper_scale_socket.structure_type = 'SINGLE'

    #Socket tooth_base_vertices
    tooth_base_vertices_socket = scoop.interface.new_socket(name = "tooth_base_vertices", in_out='INPUT', socket_type = 'NodeSocketVector', parent = tooth__panel)
    tooth_base_vertices_socket.default_value = (2.0, 2.0, 2.0)
    tooth_base_vertices_socket.min_value = 2.0
    tooth_base_vertices_socket.max_value = 5.0
    tooth_base_vertices_socket.subtype = 'XYZ'
    tooth_base_vertices_socket.attribute_domain = 'POINT'
    tooth_base_vertices_socket.force_non_field = True
    tooth_base_vertices_socket.default_input = 'VALUE'
    tooth_base_vertices_socket.structure_type = 'SINGLE'

    #Socket tooth_inset_dist
    tooth_inset_dist_socket = scoop.interface.new_socket(name = "tooth_inset_dist", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = tooth__panel)
    tooth_inset_dist_socket.default_value = 0.004999999888241291
    tooth_inset_dist_socket.min_value = 0.0
    tooth_inset_dist_socket.max_value = 3.4028234663852886e+38
    tooth_inset_dist_socket.subtype = 'DISTANCE'
    tooth_inset_dist_socket.attribute_domain = 'POINT'
    tooth_inset_dist_socket.force_non_field = True
    tooth_inset_dist_socket.default_input = 'VALUE'
    tooth_inset_dist_socket.structure_type = 'SINGLE'

    #Socket tooth_validity
    tooth_validity_socket = scoop.interface.new_socket(name = "tooth_validity", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = tooth__panel)
    tooth_validity_socket.default_value = 1.0
    tooth_validity_socket.min_value = 0.0
    tooth_validity_socket.max_value = 5.0
    tooth_validity_socket.subtype = 'FACTOR'
    tooth_validity_socket.attribute_domain = 'POINT'
    tooth_validity_socket.force_non_field = True
    tooth_validity_socket.default_input = 'VALUE'
    tooth_validity_socket.structure_type = 'SINGLE'

    #Socket tooth_subdivisions_offset
    tooth_subdivisions_offset_socket = scoop.interface.new_socket(name = "tooth_subdivisions_offset", in_out='INPUT', socket_type = 'NodeSocketInt', parent = tooth__panel)
    tooth_subdivisions_offset_socket.default_value = -1
    tooth_subdivisions_offset_socket.min_value = -10
    tooth_subdivisions_offset_socket.max_value = 2
    tooth_subdivisions_offset_socket.subtype = 'NONE'
    tooth_subdivisions_offset_socket.attribute_domain = 'POINT'
    tooth_subdivisions_offset_socket.force_non_field = True
    tooth_subdivisions_offset_socket.default_input = 'VALUE'
    tooth_subdivisions_offset_socket.structure_type = 'SINGLE'

    #Socket tooth_edge_crease
    tooth_edge_crease_socket = scoop.interface.new_socket(name = "tooth_edge_crease", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = tooth__panel)
    tooth_edge_crease_socket.default_value = 0.20000000298023224
    tooth_edge_crease_socket.min_value = 0.0
    tooth_edge_crease_socket.max_value = 1.0
    tooth_edge_crease_socket.subtype = 'FACTOR'
    tooth_edge_crease_socket.attribute_domain = 'POINT'
    tooth_edge_crease_socket.force_non_field = True
    tooth_edge_crease_socket.default_input = 'VALUE'
    tooth_edge_crease_socket.structure_type = 'SINGLE'

    #Socket tooth_vertex_crease
    tooth_vertex_crease_socket = scoop.interface.new_socket(name = "tooth_vertex_crease", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = tooth__panel)
    tooth_vertex_crease_socket.default_value = 0.10000000149011612
    tooth_vertex_crease_socket.min_value = 0.0
    tooth_vertex_crease_socket.max_value = 1.0
    tooth_vertex_crease_socket.subtype = 'FACTOR'
    tooth_vertex_crease_socket.attribute_domain = 'POINT'
    tooth_vertex_crease_socket.force_non_field = True
    tooth_vertex_crease_socket.default_input = 'VALUE'
    tooth_vertex_crease_socket.structure_type = 'SINGLE'


    #Panel mount_
    mount__panel = scoop.interface.new_panel("mount_")
    #Socket mount_radius
    mount_radius_socket = scoop.interface.new_socket(name = "mount_radius", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = mount__panel)
    mount_radius_socket.default_value = 0.02500000037252903
    mount_radius_socket.min_value = 0.0
    mount_radius_socket.max_value = 3.4028234663852886e+38
    mount_radius_socket.subtype = 'DISTANCE'
    mount_radius_socket.attribute_domain = 'POINT'
    mount_radius_socket.force_non_field = True
    mount_radius_socket.default_input = 'VALUE'
    mount_radius_socket.structure_type = 'SINGLE'

    #Socket mount_offset_lin
    mount_offset_lin_socket = scoop.interface.new_socket(name = "mount_offset_lin", in_out='INPUT', socket_type = 'NodeSocketVector', parent = mount__panel)
    mount_offset_lin_socket.default_value = (0.0, 0.0, 0.014999999664723873)
    mount_offset_lin_socket.min_value = -10000.0
    mount_offset_lin_socket.max_value = 10000.0
    mount_offset_lin_socket.subtype = 'TRANSLATION'
    mount_offset_lin_socket.attribute_domain = 'POINT'
    mount_offset_lin_socket.force_non_field = True
    mount_offset_lin_socket.default_input = 'VALUE'
    mount_offset_lin_socket.structure_type = 'SINGLE'

    #Socket mount_offset_ang
    mount_offset_ang_socket = scoop.interface.new_socket(name = "mount_offset_ang", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = mount__panel)
    mount_offset_ang_socket.default_value = 0.0
    mount_offset_ang_socket.min_value = -0.5235987901687622
    mount_offset_ang_socket.max_value = 0.5235987901687622
    mount_offset_ang_socket.subtype = 'ANGLE'
    mount_offset_ang_socket.attribute_domain = 'POINT'
    mount_offset_ang_socket.force_non_field = True
    mount_offset_ang_socket.default_input = 'VALUE'
    mount_offset_ang_socket.structure_type = 'SINGLE'

    #Socket mount_vertices_ratio
    mount_vertices_ratio_socket = scoop.interface.new_socket(name = "mount_vertices_ratio", in_out='INPUT', socket_type = 'NodeSocketFloat', parent = mount__panel)
    mount_vertices_ratio_socket.default_value = 1.0
    mount_vertices_ratio_socket.min_value = 0.0
    mount_vertices_ratio_socket.max_value = 5.0
    mount_vertices_ratio_socket.subtype = 'FACTOR'
    mount_vertices_ratio_socket.attribute_domain = 'POINT'
    mount_vertices_ratio_socket.force_non_field = True
    mount_vertices_ratio_socket.default_input = 'VALUE'
    mount_vertices_ratio_socket.structure_type = 'SINGLE'



    #initialize scoop nodes
    #node Group Output
    group_output_2 = scoop.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True

    #node Cube
    cube = scoop.nodes.new("GeometryNodeMeshCube")
    cube.name = "Cube"

    #node Set Position
    set_position = scoop.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    #Selection
    set_position.inputs[1].default_value = True
    #Position
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Delete Geometry
    delete_geometry = scoop.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'FACE'
    delete_geometry.mode = 'ALL'

    #node Compare
    compare = scoop.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'EQUAL'
    #Epsilon
    compare.inputs[12].default_value = 0.0010000000474974513

    #node Math
    math_2 = scoop.nodes.new("ShaderNodeMath")
    math_2.name = "Math"
    math_2.operation = 'DIVIDE'
    math_2.use_clamp = False
    #Value_001
    math_2.inputs[1].default_value = 2.0

    #node Combine XYZ.002
    combine_xyz_002 = scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    combine_xyz_002.inputs[0].hide = True
    combine_xyz_002.inputs[1].hide = True
    #X
    combine_xyz_002.inputs[0].default_value = 0.0
    #Y
    combine_xyz_002.inputs[1].default_value = 0.0

    #node Position.001
    position_001 = scoop.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"

    #node Separate XYZ.001
    separate_xyz_001 = scoop.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"
    separate_xyz_001.outputs[1].hide = True

    #node Subdivision Surface
    subdivision_surface = scoop.nodes.new("GeometryNodeSubdivisionSurface")
    subdivision_surface.name = "Subdivision Surface"
    subdivision_surface.boundary_smooth = 'ALL'
    subdivision_surface.uv_smooth = 'PRESERVE_BOUNDARIES'
    #Limit Surface
    subdivision_surface.inputs[4].default_value = True

    #node Math.008
    math_008_1 = scoop.nodes.new("ShaderNodeMath")
    math_008_1.name = "Math.008"
    math_008_1.operation = 'DIVIDE'
    math_008_1.use_clamp = False
    #Value_001
    math_008_1.inputs[1].default_value = 2.0

    #node Math.010
    math_010_1 = scoop.nodes.new("ShaderNodeMath")
    math_010_1.name = "Math.010"
    math_010_1.operation = 'MULTIPLY'
    math_010_1.use_clamp = False

    #node Combine XYZ
    combine_xyz = scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.inputs[1].hide = True
    #Y
    combine_xyz.inputs[1].default_value = 0.0

    #node Extrude Mesh
    extrude_mesh = scoop.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh.name = "Extrude Mesh"
    extrude_mesh.mode = 'FACES'
    #Selection
    extrude_mesh.inputs[1].default_value = True
    #Offset
    extrude_mesh.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Individual
    extrude_mesh.inputs[4].default_value = False

    #node Boolean Math.001
    boolean_math_001 = scoop.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.operation = 'AND'

    #node Compare.004
    compare_004 = scoop.nodes.new("FunctionNodeCompare")
    compare_004.name = "Compare.004"
    compare_004.data_type = 'FLOAT'
    compare_004.mode = 'ELEMENT'
    compare_004.operation = 'GREATER_THAN'

    #node Math.011
    math_011 = scoop.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.operation = 'MULTIPLY'
    math_011.use_clamp = False

    #node Group
    group = scoop.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = shape_scoop_profile_x
    #Socket_7
    group.inputs[6].default_value = -1.0

    #node Group.001
    group_001 = scoop.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = shape_scoop_profile_x
    #Socket_7
    group_001.inputs[6].default_value = 1.0

    #node Math.006
    math_006_2 = scoop.nodes.new("ShaderNodeMath")
    math_006_2.name = "Math.006"
    math_006_2.operation = 'MULTIPLY'
    math_006_2.use_clamp = False
    #Value_001
    math_006_2.inputs[1].default_value = -1.0

    #node Group.002
    group_002 = scoop.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = shape_scoop_profile_y

    #node Math.001
    math_001_2 = scoop.nodes.new("ShaderNodeMath")
    math_001_2.name = "Math.001"
    math_001_2.operation = 'DIVIDE'
    math_001_2.use_clamp = False
    #Value_001
    math_001_2.inputs[1].default_value = 2.0

    #node Reroute
    reroute = scoop.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketFloat"
    #node Math.002
    math_002_2 = scoop.nodes.new("ShaderNodeMath")
    math_002_2.name = "Math.002"
    math_002_2.operation = 'MULTIPLY'
    math_002_2.use_clamp = False

    #node Euler to Rotation
    euler_to_rotation = scoop.nodes.new("FunctionNodeEulerToRotation")
    euler_to_rotation.name = "Euler to Rotation"

    #node Combine XYZ.003
    combine_xyz_003_2 = scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003_2.name = "Combine XYZ.003"
    combine_xyz_003_2.inputs[0].hide = True
    combine_xyz_003_2.inputs[2].hide = True
    #X
    combine_xyz_003_2.inputs[0].default_value = 0.0
    #Z
    combine_xyz_003_2.inputs[2].default_value = 0.0

    #node Mesh Boolean.002
    mesh_boolean_002 = scoop.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_002.name = "Mesh Boolean.002"
    mesh_boolean_002.operation = 'DIFFERENCE'
    mesh_boolean_002.solver = 'EXACT'
    #Self Intersection
    mesh_boolean_002.inputs[2].default_value = False
    #Hole Tolerant
    mesh_boolean_002.inputs[3].default_value = True

    #node Cylinder.002
    cylinder_002 = scoop.nodes.new("GeometryNodeMeshCylinder")
    cylinder_002.name = "Cylinder.002"
    cylinder_002.fill_type = 'TRIANGLE_FAN'
    #Side Segments
    cylinder_002.inputs[1].default_value = 1
    #Fill Segments
    cylinder_002.inputs[2].default_value = 1

    #node Mesh Boolean.003
    mesh_boolean_003 = scoop.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_003.name = "Mesh Boolean.003"
    mesh_boolean_003.operation = 'UNION'
    mesh_boolean_003.solver = 'EXACT'
    #Self Intersection
    mesh_boolean_003.inputs[2].default_value = False
    #Hole Tolerant
    mesh_boolean_003.inputs[3].default_value = True

    #node Transform Geometry.001
    transform_geometry_001 = scoop.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    #Translation
    transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_001.inputs[3].default_value = (1.0, -1.0, 1.0)

    #node Set Shade Smooth
    set_shade_smooth = scoop.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    #Selection
    set_shade_smooth.inputs[1].default_value = True
    #Shade Smooth
    set_shade_smooth.inputs[2].default_value = True

    #node Join Geometry.001
    join_geometry_001 = scoop.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"

    #node Transform Geometry.002
    transform_geometry_002 = scoop.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.mode = 'COMPONENTS'
    transform_geometry_002.inputs[2].hide = True
    transform_geometry_002.inputs[3].hide = True
    transform_geometry_002.inputs[4].hide = True
    #Rotation
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Combine XYZ.004
    combine_xyz_004 = scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004.name = "Combine XYZ.004"
    combine_xyz_004.inputs[0].hide = True
    combine_xyz_004.inputs[1].hide = True
    #X
    combine_xyz_004.inputs[0].default_value = 0.0
    #Y
    combine_xyz_004.inputs[1].default_value = 0.0

    #node Math.003
    math_003_2 = scoop.nodes.new("ShaderNodeMath")
    math_003_2.name = "Math.003"
    math_003_2.operation = 'DIVIDE'
    math_003_2.use_clamp = False
    #Value_001
    math_003_2.inputs[1].default_value = 2.0

    #node Merge by Distance
    merge_by_distance = scoop.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = 'ALL'

    #node Merge by Distance.001
    merge_by_distance_001 = scoop.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_001.name = "Merge by Distance.001"
    merge_by_distance_001.mode = 'ALL'
    #Selection
    merge_by_distance_001.inputs[1].default_value = True
    #Distance
    merge_by_distance_001.inputs[2].default_value = 9.999999747378752e-06

    #node Integer Math
    integer_math = scoop.nodes.new("FunctionNodeIntegerMath")
    integer_math.name = "Integer Math"
    integer_math.operation = 'MAXIMUM'

    #node Integer Math.001
    integer_math_001 = scoop.nodes.new("FunctionNodeIntegerMath")
    integer_math_001.name = "Integer Math.001"
    integer_math_001.operation = 'MAXIMUM'

    #node Math.005
    math_005_1 = scoop.nodes.new("ShaderNodeMath")
    math_005_1.name = "Math.005"
    math_005_1.operation = 'MAXIMUM'
    math_005_1.use_clamp = False

    #node Math.007
    math_007_2 = scoop.nodes.new("ShaderNodeMath")
    math_007_2.name = "Math.007"
    math_007_2.operation = 'DIVIDE'
    math_007_2.use_clamp = False

    #node Integer Math.002
    integer_math_002 = scoop.nodes.new("FunctionNodeIntegerMath")
    integer_math_002.name = "Integer Math.002"
    integer_math_002.operation = 'POWER'

    #node Math.012
    math_012 = scoop.nodes.new("ShaderNodeMath")
    math_012.name = "Math.012"
    math_012.operation = 'MULTIPLY'
    math_012.use_clamp = False

    #node Float to Integer
    float_to_integer = scoop.nodes.new("FunctionNodeFloatToInt")
    float_to_integer.name = "Float to Integer"
    float_to_integer.rounding_mode = 'ROUND'

    #node Math.013
    math_013 = scoop.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.operation = 'MULTIPLY'
    math_013.use_clamp = False
    #Value_001
    math_013.inputs[1].default_value = 3.1415927410125732

    #node Integer Math.004
    integer_math_004 = scoop.nodes.new("FunctionNodeIntegerMath")
    integer_math_004.name = "Integer Math.004"
    integer_math_004.operation = 'MODULO'
    #Value_001
    integer_math_004.inputs[1].default_value = 2

    #node Integer Math.005
    integer_math_005 = scoop.nodes.new("FunctionNodeIntegerMath")
    integer_math_005.name = "Integer Math.005"
    integer_math_005.operation = 'ADD'

    #node Transform Geometry.003
    transform_geometry_003 = scoop.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.mode = 'COMPONENTS'
    transform_geometry_003.inputs[2].hide = True
    transform_geometry_003.inputs[3].hide = True
    transform_geometry_003.inputs[4].hide = True
    #Rotation
    transform_geometry_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Math.014
    math_014 = scoop.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.operation = 'DIVIDE'
    math_014.use_clamp = False
    #Value_001
    math_014.inputs[1].default_value = 2.0

    #node Combine XYZ.005
    combine_xyz_005 = scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_005.name = "Combine XYZ.005"
    combine_xyz_005.inputs[0].hide = True
    combine_xyz_005.inputs[1].hide = True
    #X
    combine_xyz_005.inputs[0].default_value = 0.0
    #Y
    combine_xyz_005.inputs[1].default_value = 0.0

    #node Math.015
    math_015 = scoop.nodes.new("ShaderNodeMath")
    math_015.name = "Math.015"
    math_015.operation = 'ADD'
    math_015.use_clamp = False

    #node Math.016
    math_016 = scoop.nodes.new("ShaderNodeMath")
    math_016.name = "Math.016"
    math_016.operation = 'SUBTRACT'
    math_016.use_clamp = False

    #node Set Mesh Normal
    set_mesh_normal = scoop.nodes.new("GeometryNodeSetMeshNormal")
    set_mesh_normal.name = "Set Mesh Normal"
    set_mesh_normal.domain = 'POINT'
    set_mesh_normal.mode = 'SHARPNESS'
    #Remove Custom
    set_mesh_normal.inputs[1].default_value = False
    #Face Sharpness
    set_mesh_normal.inputs[3].default_value = False

    #node Boolean Math
    boolean_math = scoop.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.hide = True
    boolean_math.operation = 'OR'

    #node Math.017
    math_017 = scoop.nodes.new("ShaderNodeMath")
    math_017.name = "Math.017"
    math_017.operation = 'ADD'
    math_017.use_clamp = False

    #node Math.009
    math_009_2 = scoop.nodes.new("ShaderNodeMath")
    math_009_2.name = "Math.009"
    math_009_2.operation = 'DIVIDE'
    math_009_2.use_clamp = False
    #Value_001
    math_009_2.inputs[1].default_value = 4.0

    #node Position.002
    position_002 = scoop.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"

    #node Compare.003
    compare_003 = scoop.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.data_type = 'FLOAT'
    compare_003.mode = 'ELEMENT'
    compare_003.operation = 'GREATER_EQUAL'

    #node Separate XYZ.002
    separate_xyz_002 = scoop.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002.name = "Separate XYZ.002"

    #node Boolean Math.003
    boolean_math_003 = scoop.nodes.new("FunctionNodeBooleanMath")
    boolean_math_003.name = "Boolean Math.003"
    boolean_math_003.operation = 'AND'

    #node Compare.005
    compare_005 = scoop.nodes.new("FunctionNodeCompare")
    compare_005.name = "Compare.005"
    compare_005.data_type = 'FLOAT'
    compare_005.mode = 'ELEMENT'
    compare_005.operation = 'EQUAL'
    #Epsilon
    compare_005.inputs[12].default_value = 0.0010000000474974513

    #node Extrude Mesh.002
    extrude_mesh_002 = scoop.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_002.name = "Extrude Mesh.002"
    extrude_mesh_002.mode = 'EDGES'

    #node Math.019
    math_019 = scoop.nodes.new("ShaderNodeMath")
    math_019.name = "Math.019"
    math_019.operation = 'ADD'
    math_019.use_clamp = False

    #node Boolean Math.002
    boolean_math_002 = scoop.nodes.new("FunctionNodeBooleanMath")
    boolean_math_002.name = "Boolean Math.002"
    boolean_math_002.operation = 'AND'

    #node Compare.001
    compare_001_2 = scoop.nodes.new("FunctionNodeCompare")
    compare_001_2.name = "Compare.001"
    compare_001_2.data_type = 'FLOAT'
    compare_001_2.mode = 'ELEMENT'
    compare_001_2.operation = 'GREATER_THAN'
    #B
    compare_001_2.inputs[1].default_value = 0.0

    #node Combine XYZ.006
    combine_xyz_006 = scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_006.name = "Combine XYZ.006"
    #X
    combine_xyz_006.inputs[0].default_value = 1.0
    #Y
    combine_xyz_006.inputs[1].default_value = 0.0

    #node Scale Elements
    scale_elements = scoop.nodes.new("GeometryNodeScaleElements")
    scale_elements.name = "Scale Elements"
    scale_elements.domain = 'EDGE'
    scale_elements.scale_mode = 'SINGLE_AXIS'
    #Center
    scale_elements.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Axis
    scale_elements.inputs[4].default_value = (0.0, 1.0, 0.0)

    #node Cube.001
    cube_001 = scoop.nodes.new("GeometryNodeMeshCube")
    cube_001.name = "Cube.001"

    #node Transform Geometry.004
    transform_geometry_004 = scoop.nodes.new("GeometryNodeTransform")
    transform_geometry_004.name = "Transform Geometry.004"
    transform_geometry_004.mode = 'COMPONENTS'
    transform_geometry_004.inputs[2].hide = True
    transform_geometry_004.inputs[3].hide = True
    transform_geometry_004.inputs[4].hide = True
    #Rotation
    transform_geometry_004.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_004.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Combine XYZ.007
    combine_xyz_007 = scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_007.name = "Combine XYZ.007"

    #node Math.020
    math_020 = scoop.nodes.new("ShaderNodeMath")
    math_020.name = "Math.020"
    math_020.operation = 'ADD'
    math_020.use_clamp = False

    #node Transform Geometry.005
    transform_geometry_005 = scoop.nodes.new("GeometryNodeTransform")
    transform_geometry_005.name = "Transform Geometry.005"
    transform_geometry_005.mode = 'COMPONENTS'
    transform_geometry_005.inputs[3].hide = True
    transform_geometry_005.inputs[4].hide = True
    #Scale
    transform_geometry_005.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Transform Geometry.006
    transform_geometry_006 = scoop.nodes.new("GeometryNodeTransform")
    transform_geometry_006.name = "Transform Geometry.006"
    transform_geometry_006.mode = 'COMPONENTS'
    #Scale
    transform_geometry_006.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Mesh Boolean
    mesh_boolean = scoop.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.operation = 'UNION'
    mesh_boolean.solver = 'EXACT'
    #Self Intersection
    mesh_boolean.inputs[2].default_value = False
    #Hole Tolerant
    mesh_boolean.inputs[3].default_value = True

    #node Combine XYZ.008
    combine_xyz_008 = scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_008.name = "Combine XYZ.008"

    #node Math.021
    math_021 = scoop.nodes.new("ShaderNodeMath")
    math_021.name = "Math.021"
    math_021.operation = 'ADD'
    math_021.use_clamp = False

    #node Math.022
    math_022 = scoop.nodes.new("ShaderNodeMath")
    math_022.name = "Math.022"
    math_022.operation = 'DIVIDE'
    math_022.use_clamp = False
    #Value_001
    math_022.inputs[1].default_value = 2.0

    #node Repeat Input
    repeat_input = scoop.nodes.new("GeometryNodeRepeatInput")
    repeat_input.name = "Repeat Input"
    #node Repeat Output
    repeat_output = scoop.nodes.new("GeometryNodeRepeatOutput")
    repeat_output.name = "Repeat Output"
    repeat_output.active_index = 1
    repeat_output.inspection_index = 0
    repeat_output.repeat_items.clear()
    # Create item "Geometry"
    repeat_output.repeat_items.new('GEOMETRY', "Geometry")
    # Create item "Integer"
    repeat_output.repeat_items.new('INT', "Integer")

    #node Vector Math
    vector_math = scoop.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'ADD'

    #node Combine XYZ.009
    combine_xyz_009 = scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_009.name = "Combine XYZ.009"
    combine_xyz_009.inputs[0].hide = True
    combine_xyz_009.inputs[2].hide = True
    #X
    combine_xyz_009.inputs[0].default_value = 0.0
    #Z
    combine_xyz_009.inputs[2].default_value = 0.0

    #node Math.025
    math_025 = scoop.nodes.new("ShaderNodeMath")
    math_025.name = "Math.025"
    math_025.operation = 'MULTIPLY'
    math_025.use_clamp = False

    #node Math.026
    math_026 = scoop.nodes.new("ShaderNodeMath")
    math_026.name = "Math.026"
    math_026.operation = 'DIVIDE'
    math_026.use_clamp = False
    #Value_001
    math_026.inputs[1].default_value = -2.0

    #node Math.027
    math_027 = scoop.nodes.new("ShaderNodeMath")
    math_027.name = "Math.027"
    math_027.operation = 'DIVIDE'
    math_027.use_clamp = False

    #node Bounding Box
    bounding_box = scoop.nodes.new("GeometryNodeBoundBox")
    bounding_box.name = "Bounding Box"
    #Use Radius
    bounding_box.inputs[1].default_value = False

    #node Separate XYZ
    separate_xyz_2 = scoop.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_2.name = "Separate XYZ"
    separate_xyz_2.outputs[0].hide = True
    separate_xyz_2.outputs[2].hide = True

    #node Separate XYZ.003
    separate_xyz_003 = scoop.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_003.name = "Separate XYZ.003"
    separate_xyz_003.outputs[0].hide = True
    separate_xyz_003.outputs[2].hide = True

    #node Math.028
    math_028 = scoop.nodes.new("ShaderNodeMath")
    math_028.name = "Math.028"
    math_028.operation = 'SUBTRACT'
    math_028.use_clamp = False

    #node Math.029
    math_029 = scoop.nodes.new("ShaderNodeMath")
    math_029.name = "Math.029"
    math_029.operation = 'ABSOLUTE'
    math_029.use_clamp = False

    #node Integer Math.007
    integer_math_007 = scoop.nodes.new("FunctionNodeIntegerMath")
    integer_math_007.name = "Integer Math.007"
    integer_math_007.operation = 'SUBTRACT'
    #Value_001
    integer_math_007.inputs[1].default_value = 1

    #node Geometry Proximity
    geometry_proximity = scoop.nodes.new("GeometryNodeProximity")
    geometry_proximity.name = "Geometry Proximity"
    geometry_proximity.target_element = 'FACES'
    #Group ID
    geometry_proximity.inputs[1].default_value = 0
    #Sample Group ID
    geometry_proximity.inputs[3].default_value = 0

    #node Transform Geometry.007
    transform_geometry_007 = scoop.nodes.new("GeometryNodeTransform")
    transform_geometry_007.name = "Transform Geometry.007"
    transform_geometry_007.mode = 'COMPONENTS'
    transform_geometry_007.inputs[2].hide = True
    transform_geometry_007.inputs[3].hide = True
    transform_geometry_007.inputs[4].hide = True
    #Rotation
    transform_geometry_007.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    transform_geometry_007.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Vector Math.001
    vector_math_001 = scoop.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'SUBTRACT'

    #node Switch
    switch = scoop.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'GEOMETRY'

    #node Compare.002
    compare_002 = scoop.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = 'FLOAT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'GREATER_THAN'

    #node Math.030
    math_030 = scoop.nodes.new("ShaderNodeMath")
    math_030.name = "Math.030"
    math_030.operation = 'DIVIDE'
    math_030.use_clamp = False
    #Value_001
    math_030.inputs[1].default_value = 2.0

    #node Vector Math.002
    vector_math_002 = scoop.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'ADD'

    #node Combine XYZ.010
    combine_xyz_010 = scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_010.name = "Combine XYZ.010"
    combine_xyz_010.inputs[1].hide = True
    #Y
    combine_xyz_010.inputs[1].default_value = 0.0

    #node Vector Math.003
    vector_math_003 = scoop.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = 'MULTIPLY'
    #Vector_001
    vector_math_003.inputs[1].default_value = (1.0, 0.0, 1.0)

    #node Subdivision Surface.001
    subdivision_surface_001 = scoop.nodes.new("GeometryNodeSubdivisionSurface")
    subdivision_surface_001.name = "Subdivision Surface.001"
    subdivision_surface_001.boundary_smooth = 'ALL'
    subdivision_surface_001.uv_smooth = 'PRESERVE_BOUNDARIES'
    #Limit Surface
    subdivision_surface_001.inputs[4].default_value = True

    #node Integer Math.008
    integer_math_008 = scoop.nodes.new("FunctionNodeIntegerMath")
    integer_math_008.name = "Integer Math.008"
    integer_math_008.operation = 'ADD'

    #node Separate XYZ.004
    separate_xyz_004 = scoop.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_004.name = "Separate XYZ.004"
    separate_xyz_004.hide = True

    #node Group Input.001
    group_input_001 = scoop.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"

    #node Separate XYZ.005
    separate_xyz_005 = scoop.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_005.name = "Separate XYZ.005"
    separate_xyz_005.hide = True

    #node Float to Integer.001
    float_to_integer_001 = scoop.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_001.name = "Float to Integer.001"
    float_to_integer_001.hide = True
    float_to_integer_001.rounding_mode = 'ROUND'

    #node Float to Integer.002
    float_to_integer_002 = scoop.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_002.name = "Float to Integer.002"
    float_to_integer_002.hide = True
    float_to_integer_002.rounding_mode = 'ROUND'

    #node Float to Integer.003
    float_to_integer_003 = scoop.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_003.name = "Float to Integer.003"
    float_to_integer_003.hide = True
    float_to_integer_003.rounding_mode = 'ROUND'

    #node Group Input
    group_input_2 = scoop.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"

    #node Math.023
    math_023 = scoop.nodes.new("ShaderNodeMath")
    math_023.name = "Math.023"
    math_023.operation = 'SUBTRACT'
    math_023.use_clamp = False
    #Value
    math_023.inputs[0].default_value = 1.0

    #node Group Input.002
    group_input_002 = scoop.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"

    #node Group Input.003
    group_input_003 = scoop.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"

    #node Math.024
    math_024 = scoop.nodes.new("ShaderNodeMath")
    math_024.name = "Math.024"
    math_024.operation = 'SUBTRACT'
    math_024.use_clamp = False
    #Value_001
    math_024.inputs[1].default_value = 0.5

    #node Math.032
    math_032 = scoop.nodes.new("ShaderNodeMath")
    math_032.name = "Math.032"
    math_032.operation = 'MULTIPLY'
    math_032.use_clamp = False
    #Value_001
    math_032.inputs[1].default_value = 2.0

    #node Group Input.004
    group_input_004 = scoop.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"

    #node Math.004
    math_004_2 = scoop.nodes.new("ShaderNodeMath")
    math_004_2.name = "Math.004"
    math_004_2.operation = 'MULTIPLY'
    math_004_2.use_clamp = False
    #Value_001
    math_004_2.inputs[1].default_value = -1.0

    #node Group Input.005
    group_input_005 = scoop.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"

    #node Math.033
    math_033 = scoop.nodes.new("ShaderNodeMath")
    math_033.name = "Math.033"
    math_033.operation = 'ADD'
    math_033.use_clamp = False

    #node Math.035
    math_035 = scoop.nodes.new("ShaderNodeMath")
    math_035.name = "Math.035"
    math_035.operation = 'MULTIPLY'
    math_035.use_clamp = False

    #node Group Input.006
    group_input_006 = scoop.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"

    #node Triangulate
    triangulate = scoop.nodes.new("GeometryNodeTriangulate")
    triangulate.name = "Triangulate"
    triangulate.ngon_method = 'BEAUTY'
    triangulate.quad_method = 'BEAUTY'
    #Selection
    triangulate.inputs[1].default_value = True

    #node Group Input.007
    group_input_007 = scoop.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"

    #node Separate XYZ.006
    separate_xyz_006 = scoop.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_006.name = "Separate XYZ.006"
    separate_xyz_006.outputs[1].hide = True

    #node Math.031
    math_031 = scoop.nodes.new("ShaderNodeMath")
    math_031.name = "Math.031"
    math_031.operation = 'SUBTRACT'
    math_031.use_clamp = False

    #node Math.036
    math_036 = scoop.nodes.new("ShaderNodeMath")
    math_036.name = "Math.036"
    math_036.operation = 'ADD'
    math_036.use_clamp = False

    #node Math.034
    math_034 = scoop.nodes.new("ShaderNodeMath")
    math_034.name = "Math.034"
    math_034.operation = 'SUBTRACT'
    math_034.use_clamp = False

    #node Group Input.008
    group_input_008 = scoop.nodes.new("NodeGroupInput")
    group_input_008.name = "Group Input.008"

    #node Separate XYZ.007
    separate_xyz_007 = scoop.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_007.name = "Separate XYZ.007"

    #node Math.037
    math_037 = scoop.nodes.new("ShaderNodeMath")
    math_037.name = "Math.037"
    math_037.operation = 'MULTIPLY'
    math_037.use_clamp = False

    #node Math.038
    math_038 = scoop.nodes.new("ShaderNodeMath")
    math_038.name = "Math.038"
    math_038.operation = 'ADD'
    math_038.use_clamp = False

    #node Math.039
    math_039 = scoop.nodes.new("ShaderNodeMath")
    math_039.name = "Math.039"
    math_039.operation = 'DIVIDE'
    math_039.use_clamp = False
    #Value_001
    math_039.inputs[1].default_value = 2.0

    #node Separate XYZ.008
    separate_xyz_008 = scoop.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_008.name = "Separate XYZ.008"
    separate_xyz_008.hide = True

    #node Float to Integer.004
    float_to_integer_004 = scoop.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_004.name = "Float to Integer.004"
    float_to_integer_004.hide = True
    float_to_integer_004.rounding_mode = 'ROUND'

    #node Float to Integer.005
    float_to_integer_005 = scoop.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_005.name = "Float to Integer.005"
    float_to_integer_005.hide = True
    float_to_integer_005.rounding_mode = 'ROUND'

    #node Float to Integer.006
    float_to_integer_006 = scoop.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_006.name = "Float to Integer.006"
    float_to_integer_006.hide = True
    float_to_integer_006.rounding_mode = 'ROUND'

    #node Group Input.009
    group_input_009 = scoop.nodes.new("NodeGroupInput")
    group_input_009.name = "Group Input.009"

    #node Math.018
    math_018 = scoop.nodes.new("ShaderNodeMath")
    math_018.name = "Math.018"
    math_018.operation = 'MULTIPLY'
    math_018.use_clamp = False

    #node Float to Integer.007
    float_to_integer_007 = scoop.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_007.name = "Float to Integer.007"
    float_to_integer_007.rounding_mode = 'ROUND'

    #node Integer Math.006
    integer_math_006 = scoop.nodes.new("FunctionNodeIntegerMath")
    integer_math_006.name = "Integer Math.006"
    integer_math_006.operation = 'MAXIMUM'
    #Value_001
    integer_math_006.inputs[1].default_value = 4

    #node Set Material
    set_material = scoop.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    #Selection
    set_material.inputs[1].default_value = True

    #node Group Input.010
    group_input_010 = scoop.nodes.new("NodeGroupInput")
    group_input_010.name = "Group Input.010"

    #node Math.040
    math_040 = scoop.nodes.new("ShaderNodeMath")
    math_040.name = "Math.040"
    math_040.operation = 'DIVIDE'
    math_040.use_clamp = False
    #Value
    math_040.inputs[0].default_value = 0.05000000074505806

    #node Integer
    integer = scoop.nodes.new("FunctionNodeInputInt")
    integer.name = "Integer"
    integer.integer = 0

    #node Integer Math.003
    integer_math_003 = scoop.nodes.new("FunctionNodeIntegerMath")
    integer_math_003.name = "Integer Math.003"
    integer_math_003.operation = 'ADD'

    #node Compare.006
    compare_006 = scoop.nodes.new("FunctionNodeCompare")
    compare_006.name = "Compare.006"
    compare_006.data_type = 'INT'
    compare_006.mode = 'ELEMENT'
    compare_006.operation = 'GREATER_THAN'
    #B_INT
    compare_006.inputs[3].default_value = 3

    #node Switch.002
    switch_002 = scoop.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.input_type = 'GEOMETRY'

    #node Normal
    normal = scoop.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    normal.legacy_corner_normals = False

    #node Scale Elements.001
    scale_elements_001 = scoop.nodes.new("GeometryNodeScaleElements")
    scale_elements_001.name = "Scale Elements.001"
    scale_elements_001.domain = 'FACE'
    scale_elements_001.scale_mode = 'SINGLE_AXIS'
    #Center
    scale_elements_001.inputs[3].default_value = (0.0, 0.0, 0.0)
    #Axis
    scale_elements_001.inputs[4].default_value = (0.0, 1.0, 0.0)

    #node Compare.007
    compare_007 = scoop.nodes.new("FunctionNodeCompare")
    compare_007.name = "Compare.007"
    compare_007.data_type = 'VECTOR'
    compare_007.mode = 'ELEMENT'
    compare_007.operation = 'EQUAL'
    #B_VEC3
    compare_007.inputs[5].default_value = (-1.0, 0.0, 0.0)
    #Epsilon
    compare_007.inputs[12].default_value = 0.0010000000474974513

    #node Mesh Boolean.001
    mesh_boolean_001 = scoop.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_001.name = "Mesh Boolean.001"
    mesh_boolean_001.operation = 'UNION'
    mesh_boolean_001.solver = 'EXACT'
    #Self Intersection
    mesh_boolean_001.inputs[2].default_value = False
    #Hole Tolerant
    mesh_boolean_001.inputs[3].default_value = True


    #Process zone input Repeat Input
    repeat_input.pair_with_output(repeat_output)





    #Set locations
    group_output_2.location = (1646.5234375, 0.0)
    cube.location = (-16463.912109375, 1209.670166015625)
    set_position.location = (-15365.298828125, 1151.986328125)
    delete_geometry.location = (-13908.2392578125, 1242.215087890625)
    compare.location = (-14348.7646484375, 1129.43359375)
    math_2.location = (-16661.732421875, 516.6614379882812)
    combine_xyz_002.location = (-15599.5751953125, 1052.93896484375)
    position_001.location = (-14811.802734375, 986.0975952148438)
    separate_xyz_001.location = (-14621.1455078125, 1074.134521484375)
    subdivision_surface.location = (-8605.9921875, 865.0498046875)
    math_008_1.location = (-15844.640625, 1074.54931640625)
    math_010_1.location = (-7467.5419921875, 379.7145080566406)
    combine_xyz.location = (-7224.1474609375, 381.5315246582031)
    extrude_mesh.location = (-6911.97265625, 646.4930419921875)
    boolean_math_001.location = (-14137.283203125, 1128.01171875)
    compare_004.location = (-14357.1298828125, 956.2731323242188)
    math_011.location = (-14615.3310546875, 931.33984375)
    group.location = (-13418.1787109375, 1241.914306640625)
    group_001.location = (-12454.3427734375, 1242.7265625)
    math_006_2.location = (-12817.8017578125, 1188.65869140625)
    group_002.location = (-11548.263671875, 1270.08984375)
    math_001_2.location = (-16662.779296875, 341.75579833984375)
    reroute.location = (-13613.125, 318.4184265136719)
    math_002_2.location = (-11710.955078125, 894.5932006835938)
    euler_to_rotation.location = (-6911.15283203125, 342.2460632324219)
    combine_xyz_003_2.location = (-7219.1328125, 262.5845031738281)
    mesh_boolean_002.location = (-223.22398376464844, 145.22886657714844)
    cylinder_002.location = (-710.0294799804688, -54.864837646484375)
    mesh_boolean_003.location = (337.4268493652344, 99.16914367675781)
    transform_geometry_001.location = (-6919.736328125, 1019.0140991210938)
    set_shade_smooth.location = (1235.30078125, 33.419376373291016)
    join_geometry_001.location = (-6564.486328125, 902.8873901367188)
    transform_geometry_002.location = (126.22764587402344, -20.379852294921875)
    combine_xyz_004.location = (-222.3509521484375, -94.42425537109375)
    math_003_2.location = (-2686.9248046875, -150.08607482910156)
    merge_by_distance.location = (527.4267578125, 63.16914367675781)
    merge_by_distance_001.location = (-6296.0888671875, 905.8449096679688)
    integer_math.location = (-3312.88916015625, -324.76446533203125)
    integer_math_001.location = (-3129.0302734375, -328.82733154296875)
    math_005_1.location = (-16663.73828125, -125.78334045410156)
    math_007_2.location = (-2701.80224609375, -360.01092529296875)
    integer_math_002.location = (-2938.28564453125, -317.67706298828125)
    math_012.location = (-2375.371337890625, -222.3110809326172)
    float_to_integer.location = (-2010.887939453125, -269.1275634765625)
    math_013.location = (-2189.239013671875, -261.56591796875)
    integer_math_004.location = (-1821.99853515625, -321.230712890625)
    integer_math_005.location = (-1636.3787841796875, -236.61204528808594)
    transform_geometry_003.location = (-485.4715576171875, -37.3489990234375)
    math_014.location = (-1652.76416015625, -509.0677490234375)
    combine_xyz_005.location = (-713.73681640625, -351.91534423828125)
    math_015.location = (-2000.8970947265625, -492.3504638671875)
    math_016.location = (-1397.7186279296875, -417.998291015625)
    set_mesh_normal.location = (850.5841064453125, 44.419376373291016)
    boolean_math.location = (685.583984375, -48.886314392089844)
    math_017.location = (-1817.273193359375, -487.21270751953125)
    math_009_2.location = (-2265.3359375, -489.20709228515625)
    position_002.location = (-11010.0283203125, 835.2235107421875)
    compare_003.location = (-10635.4580078125, 919.3062133789062)
    separate_xyz_002.location = (-10833.2138671875, 887.3621215820312)
    boolean_math_003.location = (-10224.1591796875, 1099.2349853515625)
    compare_005.location = (-10642.662109375, 740.242919921875)
    extrude_mesh_002.location = (-9426.4931640625, 830.1807861328125)
    math_019.location = (-10855.2021484375, 716.6009521484375)
    boolean_math_002.location = (-9746.291015625, 868.26123046875)
    compare_001_2.location = (-10021.689453125, 759.7686767578125)
    combine_xyz_006.location = (-9789.642578125, 695.2613525390625)
    scale_elements.location = (-9099.3896484375, 864.2587890625)
    cube_001.location = (-3937.34375, 1928.05224609375)
    transform_geometry_004.location = (-2521.107666015625, 1826.431884765625)
    combine_xyz_007.location = (-4312.2744140625, 1485.4375)
    math_020.location = (-4538.19775390625, 1663.552001953125)
    transform_geometry_005.location = (83.13150024414062, 370.1809387207031)
    transform_geometry_006.location = (-6508.0205078125, 591.0820922851562)
    mesh_boolean.location = (-393.976806640625, 513.5941162109375)
    combine_xyz_008.location = (-4396.0439453125, 1890.5888671875)
    math_021.location = (-4739.53125, 1143.7259521484375)
    math_022.location = (-5991.34521484375, 1600.486083984375)
    repeat_input.location = (-6200.818359375, 1779.32275390625)
    repeat_output.location = (-890.72998046875, 1344.295654296875)
    vector_math.location = (-4107.224609375, 1273.778076171875)
    combine_xyz_009.location = (-4303.32275390625, 1285.224853515625)
    math_025.location = (-4515.7900390625, 1325.89208984375)
    math_026.location = (-4513.41162109375, 1504.197998046875)
    math_027.location = (-4758.5751953125, 1369.2607421875)
    bounding_box.location = (-5686.01318359375, 1570.69140625)
    separate_xyz_2.location = (-5457.93212890625, 1639.443359375)
    separate_xyz_003.location = (-5472.35595703125, 1529.75537109375)
    math_028.location = (-5277.1630859375, 1653.974609375)
    math_029.location = (-5061.4375, 1650.599853515625)
    integer_math_007.location = (-5087.85595703125, 1439.98486328125)
    geometry_proximity.location = (-3757.46337890625, 1267.86474609375)
    transform_geometry_007.location = (-2141.484375, 1738.7169189453125)
    vector_math_001.location = (-3172.283203125, 1610.7529296875)
    switch.location = (-1484.2930908203125, 1896.383544921875)
    compare_002.location = (-1928.0863037109375, 2045.2783203125)
    math_030.location = (-3163.482177734375, 1460.089111328125)
    vector_math_002.location = (-2375.738525390625, 1688.629150390625)
    combine_xyz_010.location = (-2572.106689453125, 1584.1181640625)
    vector_math_003.location = (-2929.99365234375, 1663.208740234375)
    subdivision_surface_001.location = (-3400.9931640625, 1908.673583984375)
    integer_math_008.location = (-4073.895751953125, 1724.454833984375)
    separate_xyz_004.location = (-17025.380859375, 664.3370361328125)
    group_input_001.location = (-17226.203125, 1163.084716796875)
    separate_xyz_005.location = (-17002.16796875, 930.2216796875)
    float_to_integer_001.location = (-16843.1015625, 967.6404418945312)
    float_to_integer_002.location = (-16843.1015625, 930.140380859375)
    float_to_integer_003.location = (-16843.1015625, 892.640380859375)
    group_input_2.location = (-15007.7041015625, 802.4547729492188)
    math_023.location = (-14816.1015625, 854.7529907226562)
    group_input_002.location = (-13666.8291015625, 1076.246337890625)
    group_input_003.location = (-12826.9765625, 1010.5554809570312)
    math_024.location = (-12056.6416015625, 966.7897338867188)
    math_032.location = (-11881.1416015625, 988.4938354492188)
    group_input_004.location = (-12277.6767578125, 1147.51611328125)
    math_004_2.location = (-11714.015625, 1064.821533203125)
    group_input_005.location = (-10211.724609375, 748.60107421875)
    math_033.location = (-4499.26611328125, 1151.7750244140625)
    math_035.location = (-4735.5009765625, 978.3331298828125)
    group_input_006.location = (-8839.9560546875, 1302.407958984375)
    triangulate.location = (1040.8056640625, 37.1114501953125)
    group_input_007.location = (-7903.9970703125, 446.0409240722656)
    separate_xyz_006.location = (-7664.39453125, 195.1447296142578)
    math_031.location = (-2752.616943359375, 1432.5692138671875)
    math_036.location = (-6161.8095703125, 1601.6041259765625)
    math_034.location = (-2936.515625, 1462.8858642578125)
    group_input_008.location = (-6814.2431640625, 2170.47607421875)
    separate_xyz_007.location = (-6547.4306640625, 1923.91845703125)
    math_037.location = (-2166.469970703125, 2042.356689453125)
    math_038.location = (-2505.350830078125, 2026.0965576171875)
    math_039.location = (-2351.754638671875, 2033.3782958984375)
    separate_xyz_008.location = (-4417.34228515625, 2004.9248046875)
    float_to_integer_004.location = (-4258.27587890625, 2042.34326171875)
    float_to_integer_005.location = (-4258.27587890625, 2004.84326171875)
    float_to_integer_006.location = (-4258.27587890625, 1967.34326171875)
    group_input_009.location = (-4651.275390625, 2677.646240234375)
    math_018.location = (-1356.0833740234375, -136.80751037597656)
    float_to_integer_007.location = (-1111.0953369140625, -163.7201385498047)
    integer_math_006.location = (-902.4392700195312, -156.32003784179688)
    set_material.location = (1445.728271484375, 10.635771751403809)
    group_input_010.location = (1239.758544921875, 848.69287109375)
    math_040.location = (220.9090576171875, -156.16989135742188)
    integer.location = (-6412.185546875, 1748.154296875)
    integer_math_003.location = (-1479.1517333984375, 1645.21923828125)
    compare_006.location = (-394.5124206542969, 735.2470703125)
    switch_002.location = (-199.32272338867188, 650.8265380859375)
    normal.location = (-4039.239013671875, 1584.3704833984375)
    scale_elements_001.location = (-3588.631103515625, 1899.1796875)
    compare_007.location = (-3825.60107421875, 1750.65234375)
    mesh_boolean_001.location = (-1917.6973876953125, 1857.1673583984375)

    #Set dimensions
    group_output_2.width, group_output_2.height = 140.0, 100.0
    cube.width, cube.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    delete_geometry.width, delete_geometry.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    math_2.width, math_2.height = 140.0, 100.0
    combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
    position_001.width, position_001.height = 140.0, 100.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    subdivision_surface.width, subdivision_surface.height = 150.0, 100.0
    math_008_1.width, math_008_1.height = 140.0, 100.0
    math_010_1.width, math_010_1.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    extrude_mesh.width, extrude_mesh.height = 140.0, 100.0
    boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
    compare_004.width, compare_004.height = 140.0, 100.0
    math_011.width, math_011.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0
    group_001.width, group_001.height = 140.0, 100.0
    math_006_2.width, math_006_2.height = 140.0, 100.0
    group_002.width, group_002.height = 140.0, 100.0
    math_001_2.width, math_001_2.height = 140.0, 100.0
    reroute.width, reroute.height = 10.0, 100.0
    math_002_2.width, math_002_2.height = 140.0, 100.0
    euler_to_rotation.width, euler_to_rotation.height = 140.0, 100.0
    combine_xyz_003_2.width, combine_xyz_003_2.height = 140.0, 100.0
    mesh_boolean_002.width, mesh_boolean_002.height = 140.0, 100.0
    cylinder_002.width, cylinder_002.height = 140.0, 100.0
    mesh_boolean_003.width, mesh_boolean_003.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
    transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
    combine_xyz_004.width, combine_xyz_004.height = 140.0, 100.0
    math_003_2.width, math_003_2.height = 140.0, 100.0
    merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
    merge_by_distance_001.width, merge_by_distance_001.height = 140.0, 100.0
    integer_math.width, integer_math.height = 140.0, 100.0
    integer_math_001.width, integer_math_001.height = 140.0, 100.0
    math_005_1.width, math_005_1.height = 140.0, 100.0
    math_007_2.width, math_007_2.height = 140.0, 100.0
    integer_math_002.width, integer_math_002.height = 140.0, 100.0
    math_012.width, math_012.height = 140.0, 100.0
    float_to_integer.width, float_to_integer.height = 140.0, 100.0
    math_013.width, math_013.height = 140.0, 100.0
    integer_math_004.width, integer_math_004.height = 140.0, 100.0
    integer_math_005.width, integer_math_005.height = 140.0, 100.0
    transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
    math_014.width, math_014.height = 140.0, 100.0
    combine_xyz_005.width, combine_xyz_005.height = 140.0, 100.0
    math_015.width, math_015.height = 140.0, 100.0
    math_016.width, math_016.height = 140.0, 100.0
    set_mesh_normal.width, set_mesh_normal.height = 140.0, 100.0
    boolean_math.width, boolean_math.height = 140.0, 100.0
    math_017.width, math_017.height = 140.0, 100.0
    math_009_2.width, math_009_2.height = 140.0, 100.0
    position_002.width, position_002.height = 140.0, 100.0
    compare_003.width, compare_003.height = 140.0, 100.0
    separate_xyz_002.width, separate_xyz_002.height = 140.0, 100.0
    boolean_math_003.width, boolean_math_003.height = 140.0, 100.0
    compare_005.width, compare_005.height = 140.0, 100.0
    extrude_mesh_002.width, extrude_mesh_002.height = 140.0, 100.0
    math_019.width, math_019.height = 140.0, 100.0
    boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
    compare_001_2.width, compare_001_2.height = 140.0, 100.0
    combine_xyz_006.width, combine_xyz_006.height = 140.0, 100.0
    scale_elements.width, scale_elements.height = 140.0, 100.0
    cube_001.width, cube_001.height = 140.0, 100.0
    transform_geometry_004.width, transform_geometry_004.height = 140.0, 100.0
    combine_xyz_007.width, combine_xyz_007.height = 140.0, 100.0
    math_020.width, math_020.height = 140.0, 100.0
    transform_geometry_005.width, transform_geometry_005.height = 140.0, 100.0
    transform_geometry_006.width, transform_geometry_006.height = 140.0, 100.0
    mesh_boolean.width, mesh_boolean.height = 140.0, 100.0
    combine_xyz_008.width, combine_xyz_008.height = 140.0, 100.0
    math_021.width, math_021.height = 140.0, 100.0
    math_022.width, math_022.height = 140.0, 100.0
    repeat_input.width, repeat_input.height = 140.0, 100.0
    repeat_output.width, repeat_output.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    combine_xyz_009.width, combine_xyz_009.height = 140.0, 100.0
    math_025.width, math_025.height = 140.0, 100.0
    math_026.width, math_026.height = 140.0, 100.0
    math_027.width, math_027.height = 140.0, 100.0
    bounding_box.width, bounding_box.height = 140.0, 100.0
    separate_xyz_2.width, separate_xyz_2.height = 140.0, 100.0
    separate_xyz_003.width, separate_xyz_003.height = 140.0, 100.0
    math_028.width, math_028.height = 140.0, 100.0
    math_029.width, math_029.height = 140.0, 100.0
    integer_math_007.width, integer_math_007.height = 140.0, 100.0
    geometry_proximity.width, geometry_proximity.height = 140.0, 100.0
    transform_geometry_007.width, transform_geometry_007.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    compare_002.width, compare_002.height = 140.0, 100.0
    math_030.width, math_030.height = 140.0, 100.0
    vector_math_002.width, vector_math_002.height = 140.0, 100.0
    combine_xyz_010.width, combine_xyz_010.height = 140.0, 100.0
    vector_math_003.width, vector_math_003.height = 140.0, 100.0
    subdivision_surface_001.width, subdivision_surface_001.height = 150.0, 100.0
    integer_math_008.width, integer_math_008.height = 140.0, 100.0
    separate_xyz_004.width, separate_xyz_004.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    separate_xyz_005.width, separate_xyz_005.height = 140.0, 100.0
    float_to_integer_001.width, float_to_integer_001.height = 140.0, 100.0
    float_to_integer_002.width, float_to_integer_002.height = 140.0, 100.0
    float_to_integer_003.width, float_to_integer_003.height = 140.0, 100.0
    group_input_2.width, group_input_2.height = 140.0, 100.0
    math_023.width, math_023.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    math_024.width, math_024.height = 140.0, 100.0
    math_032.width, math_032.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    math_004_2.width, math_004_2.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    math_033.width, math_033.height = 140.0, 100.0
    math_035.width, math_035.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    triangulate.width, triangulate.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    separate_xyz_006.width, separate_xyz_006.height = 140.0, 100.0
    math_031.width, math_031.height = 140.0, 100.0
    math_036.width, math_036.height = 140.0, 100.0
    math_034.width, math_034.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0
    separate_xyz_007.width, separate_xyz_007.height = 140.0, 100.0
    math_037.width, math_037.height = 140.0, 100.0
    math_038.width, math_038.height = 140.0, 100.0
    math_039.width, math_039.height = 140.0, 100.0
    separate_xyz_008.width, separate_xyz_008.height = 140.0, 100.0
    float_to_integer_004.width, float_to_integer_004.height = 140.0, 100.0
    float_to_integer_005.width, float_to_integer_005.height = 140.0, 100.0
    float_to_integer_006.width, float_to_integer_006.height = 140.0, 100.0
    group_input_009.width, group_input_009.height = 140.0, 100.0
    math_018.width, math_018.height = 140.0, 100.0
    float_to_integer_007.width, float_to_integer_007.height = 140.0, 100.0
    integer_math_006.width, integer_math_006.height = 140.0, 100.0
    set_material.width, set_material.height = 140.0, 100.0
    group_input_010.width, group_input_010.height = 140.0, 100.0
    math_040.width, math_040.height = 140.0, 100.0
    integer.width, integer.height = 140.0, 100.0
    integer_math_003.width, integer_math_003.height = 140.0, 100.0
    compare_006.width, compare_006.height = 140.0, 100.0
    switch_002.width, switch_002.height = 140.0, 100.0
    normal.width, normal.height = 140.0, 100.0
    scale_elements_001.width, scale_elements_001.height = 140.0, 100.0
    compare_007.width, compare_007.height = 140.0, 100.0
    mesh_boolean_001.width, mesh_boolean_001.height = 140.0, 100.0

    #initialize scoop links
    #cube.Mesh -> set_position.Geometry
    scoop.links.new(cube.outputs[0], set_position.inputs[0])
    #set_position.Geometry -> delete_geometry.Geometry
    scoop.links.new(set_position.outputs[0], delete_geometry.inputs[0])
    #boolean_math_001.Boolean -> delete_geometry.Selection
    scoop.links.new(boolean_math_001.outputs[0], delete_geometry.inputs[1])
    #separate_xyz_004.X -> math_2.Value
    scoop.links.new(separate_xyz_004.outputs[0], math_2.inputs[0])
    #combine_xyz_002.Vector -> set_position.Offset
    scoop.links.new(combine_xyz_002.outputs[0], set_position.inputs[3])
    #position_001.Position -> compare.A
    scoop.links.new(position_001.outputs[0], compare.inputs[4])
    #position_001.Position -> separate_xyz_001.Vector
    scoop.links.new(position_001.outputs[0], separate_xyz_001.inputs[0])
    #math_2.Value -> compare.B
    scoop.links.new(math_2.outputs[0], compare.inputs[1])
    #separate_xyz_001.X -> compare.A
    scoop.links.new(separate_xyz_001.outputs[0], compare.inputs[0])
    #scale_elements.Geometry -> subdivision_surface.Mesh
    scoop.links.new(scale_elements.outputs[0], subdivision_surface.inputs[0])
    #group_input_006.edge_crease -> subdivision_surface.Edge Crease
    scoop.links.new(group_input_006.outputs[5], subdivision_surface.inputs[2])
    #group_input_006.subdivisions -> subdivision_surface.Level
    scoop.links.new(group_input_006.outputs[4], subdivision_surface.inputs[1])
    #group_input_006.vertex_crease -> subdivision_surface.Vertex Crease
    scoop.links.new(group_input_006.outputs[6], subdivision_surface.inputs[3])
    #separate_xyz_004.Z -> math_008_1.Value
    scoop.links.new(separate_xyz_004.outputs[2], math_008_1.inputs[0])
    #math_008_1.Value -> combine_xyz_002.Z
    scoop.links.new(math_008_1.outputs[0], combine_xyz_002.inputs[2])
    #separate_xyz_006.X -> math_010_1.Value
    scoop.links.new(separate_xyz_006.outputs[0], math_010_1.inputs[1])
    #math_2.Value -> math_010_1.Value
    scoop.links.new(math_2.outputs[0], math_010_1.inputs[0])
    #math_010_1.Value -> combine_xyz.X
    scoop.links.new(math_010_1.outputs[0], combine_xyz.inputs[0])
    #float_to_integer_001.Integer -> cube.Vertices X
    scoop.links.new(float_to_integer_001.outputs[0], cube.inputs[1])
    #float_to_integer_002.Integer -> cube.Vertices Y
    scoop.links.new(float_to_integer_002.outputs[0], cube.inputs[2])
    #float_to_integer_003.Integer -> cube.Vertices Z
    scoop.links.new(float_to_integer_003.outputs[0], cube.inputs[3])
    #group_input_007.wall_thickness -> extrude_mesh.Offset Scale
    scoop.links.new(group_input_007.outputs[3], extrude_mesh.inputs[3])
    #compare.Result -> boolean_math_001.Boolean
    scoop.links.new(compare.outputs[0], boolean_math_001.inputs[0])
    #separate_xyz_001.Z -> compare_004.A
    scoop.links.new(separate_xyz_001.outputs[2], compare_004.inputs[0])
    #compare_004.Result -> boolean_math_001.Boolean
    scoop.links.new(compare_004.outputs[0], boolean_math_001.inputs[1])
    #math_011.Value -> compare_004.B
    scoop.links.new(math_011.outputs[0], compare_004.inputs[1])
    #separate_xyz_004.Z -> math_011.Value
    scoop.links.new(separate_xyz_004.outputs[2], math_011.inputs[1])
    #delete_geometry.Geometry -> group.Geometry
    scoop.links.new(delete_geometry.outputs[0], group.inputs[0])
    #math_2.Value -> group.B
    scoop.links.new(math_2.outputs[0], group.inputs[1])
    #separate_xyz_004.Z -> group.B
    scoop.links.new(separate_xyz_004.outputs[2], group.inputs[3])
    #group.Geometry -> group_001.Geometry
    scoop.links.new(group.outputs[0], group_001.inputs[0])
    #separate_xyz_004.Z -> group_001.B
    scoop.links.new(separate_xyz_004.outputs[2], group_001.inputs[3])
    #math_006_2.Value -> group_001.B
    scoop.links.new(math_006_2.outputs[0], group_001.inputs[1])
    #math_2.Value -> math_006_2.Value
    scoop.links.new(math_2.outputs[0], math_006_2.inputs[0])
    #group_001.Geometry -> group_002.Geometry
    scoop.links.new(group_001.outputs[0], group_002.inputs[0])
    #separate_xyz_004.Z -> group_002.B
    scoop.links.new(separate_xyz_004.outputs[2], group_002.inputs[3])
    #separate_xyz_004.Y -> math_001_2.Value
    scoop.links.new(separate_xyz_004.outputs[1], math_001_2.inputs[0])
    #math_001_2.Value -> reroute.Input
    scoop.links.new(math_001_2.outputs[0], reroute.inputs[0])
    #reroute.Output -> group_002.B
    scoop.links.new(reroute.outputs[0], group_002.inputs[1])
    #combine_xyz_003_2.Vector -> euler_to_rotation.Euler
    scoop.links.new(combine_xyz_003_2.outputs[0], euler_to_rotation.inputs[0])
    #group_input_007.mount_offset_ang -> combine_xyz_003_2.Y
    scoop.links.new(group_input_007.outputs[32], combine_xyz_003_2.inputs[1])
    #subdivision_surface.Mesh -> extrude_mesh.Mesh
    scoop.links.new(subdivision_surface.outputs[0], extrude_mesh.inputs[0])
    #subdivision_surface.Mesh -> transform_geometry_001.Geometry
    scoop.links.new(subdivision_surface.outputs[0], transform_geometry_001.inputs[0])
    #set_material.Geometry -> group_output_2.Geometry
    scoop.links.new(set_material.outputs[0], group_output_2.inputs[0])
    #transform_geometry_002.Geometry -> mesh_boolean_003.Mesh
    scoop.links.new(transform_geometry_002.outputs[0], mesh_boolean_003.inputs[1])
    #transform_geometry_003.Geometry -> mesh_boolean_002.Mesh 1
    scoop.links.new(transform_geometry_003.outputs[0], mesh_boolean_002.inputs[0])
    #extrude_mesh.Mesh -> join_geometry_001.Geometry
    scoop.links.new(extrude_mesh.outputs[0], join_geometry_001.inputs[0])
    #mesh_boolean_002.Mesh -> transform_geometry_002.Geometry
    scoop.links.new(mesh_boolean_002.outputs[0], transform_geometry_002.inputs[0])
    #group_input_007.wall_thickness -> math_003_2.Value
    scoop.links.new(group_input_007.outputs[3], math_003_2.inputs[0])
    #math_003_2.Value -> combine_xyz_004.Z
    scoop.links.new(math_003_2.outputs[0], combine_xyz_004.inputs[2])
    #combine_xyz_004.Vector -> transform_geometry_002.Translation
    scoop.links.new(combine_xyz_004.outputs[0], transform_geometry_002.inputs[1])
    #mesh_boolean_003.Mesh -> merge_by_distance.Geometry
    scoop.links.new(mesh_boolean_003.outputs[0], merge_by_distance.inputs[0])
    #triangulate.Mesh -> set_shade_smooth.Geometry
    scoop.links.new(triangulate.outputs[0], set_shade_smooth.inputs[0])
    #join_geometry_001.Geometry -> merge_by_distance_001.Geometry
    scoop.links.new(join_geometry_001.outputs[0], merge_by_distance_001.inputs[0])
    #float_to_integer_001.Integer -> integer_math.Value
    scoop.links.new(float_to_integer_001.outputs[0], integer_math.inputs[0])
    #integer_math.Value -> integer_math_001.Value
    scoop.links.new(integer_math.outputs[0], integer_math_001.inputs[0])
    #float_to_integer_003.Integer -> integer_math_001.Value
    scoop.links.new(float_to_integer_003.outputs[0], integer_math_001.inputs[1])
    #float_to_integer_002.Integer -> integer_math.Value
    scoop.links.new(float_to_integer_002.outputs[0], integer_math.inputs[1])
    #separate_xyz_004.X -> math_005_1.Value
    scoop.links.new(separate_xyz_004.outputs[0], math_005_1.inputs[0])
    #separate_xyz_004.Y -> math_005_1.Value
    scoop.links.new(separate_xyz_004.outputs[1], math_005_1.inputs[1])
    #group_input_006.subdivisions -> integer_math_002.Value
    scoop.links.new(group_input_006.outputs[4], integer_math_002.inputs[1])
    #integer_math_001.Value -> integer_math_002.Value
    scoop.links.new(integer_math_001.outputs[0], integer_math_002.inputs[0])
    #group_input_007.mount_radius -> cylinder_002.Radius
    scoop.links.new(group_input_007.outputs[30], cylinder_002.inputs[3])
    #math_007_2.Value -> math_012.Value
    scoop.links.new(math_007_2.outputs[0], math_012.inputs[1])
    #group_input_007.mount_radius -> math_012.Value
    scoop.links.new(group_input_007.outputs[30], math_012.inputs[0])
    #math_013.Value -> float_to_integer.Float
    scoop.links.new(math_013.outputs[0], float_to_integer.inputs[0])
    #math_005_1.Value -> math_007_2.Value
    scoop.links.new(math_005_1.outputs[0], math_007_2.inputs[1])
    #integer_math_002.Value -> math_007_2.Value
    scoop.links.new(integer_math_002.outputs[0], math_007_2.inputs[0])
    #math_012.Value -> math_013.Value
    scoop.links.new(math_012.outputs[0], math_013.inputs[0])
    #float_to_integer.Integer -> integer_math_004.Value
    scoop.links.new(float_to_integer.outputs[0], integer_math_004.inputs[0])
    #integer_math_004.Value -> integer_math_005.Value
    scoop.links.new(integer_math_004.outputs[0], integer_math_005.inputs[1])
    #float_to_integer.Integer -> integer_math_005.Value
    scoop.links.new(float_to_integer.outputs[0], integer_math_005.inputs[0])
    #cylinder_002.Mesh -> transform_geometry_003.Geometry
    scoop.links.new(cylinder_002.outputs[0], transform_geometry_003.inputs[0])
    #math_017.Value -> math_014.Value
    scoop.links.new(math_017.outputs[0], math_014.inputs[0])
    #combine_xyz_005.Vector -> transform_geometry_003.Translation
    scoop.links.new(combine_xyz_005.outputs[0], transform_geometry_003.inputs[1])
    #math_017.Value -> cylinder_002.Depth
    scoop.links.new(math_017.outputs[0], cylinder_002.inputs[4])
    #math_016.Value -> combine_xyz_005.Z
    scoop.links.new(math_016.outputs[0], combine_xyz_005.inputs[2])
    #separate_xyz_006.Z -> combine_xyz.Z
    scoop.links.new(separate_xyz_006.outputs[2], combine_xyz.inputs[2])
    #math_009_2.Value -> math_015.Value
    scoop.links.new(math_009_2.outputs[0], math_015.inputs[0])
    #math_003_2.Value -> math_015.Value
    scoop.links.new(math_003_2.outputs[0], math_015.inputs[1])
    #math_014.Value -> math_016.Value
    scoop.links.new(math_014.outputs[0], math_016.inputs[0])
    #math_003_2.Value -> math_016.Value
    scoop.links.new(math_003_2.outputs[0], math_016.inputs[1])
    #merge_by_distance.Geometry -> set_mesh_normal.Mesh
    scoop.links.new(merge_by_distance.outputs[0], set_mesh_normal.inputs[0])
    #cylinder_002.Bottom -> boolean_math.Boolean
    scoop.links.new(cylinder_002.outputs[3], boolean_math.inputs[1])
    #mesh_boolean_003.Intersecting Edges -> boolean_math.Boolean
    scoop.links.new(mesh_boolean_003.outputs[1], boolean_math.inputs[0])
    #boolean_math.Boolean -> set_mesh_normal.Edge Sharpness
    scoop.links.new(boolean_math.outputs[0], set_mesh_normal.inputs[2])
    #math_015.Value -> math_017.Value
    scoop.links.new(math_015.outputs[0], math_017.inputs[0])
    #separate_xyz_006.Z -> math_017.Value
    scoop.links.new(separate_xyz_006.outputs[2], math_017.inputs[1])
    #separate_xyz_004.Z -> math_009_2.Value
    scoop.links.new(separate_xyz_004.outputs[2], math_009_2.inputs[0])
    #separate_xyz_002.X -> compare_003.A
    scoop.links.new(separate_xyz_002.outputs[0], compare_003.inputs[0])
    #position_002.Position -> separate_xyz_002.Vector
    scoop.links.new(position_002.outputs[0], separate_xyz_002.inputs[0])
    #math_019.Value -> compare_003.B
    scoop.links.new(math_019.outputs[0], compare_003.inputs[1])
    #separate_xyz_002.Z -> compare_005.A
    scoop.links.new(separate_xyz_002.outputs[2], compare_005.inputs[0])
    #separate_xyz_004.Z -> compare_005.B
    scoop.links.new(separate_xyz_004.outputs[2], compare_005.inputs[1])
    #compare_005.Result -> boolean_math_003.Boolean
    scoop.links.new(compare_005.outputs[0], boolean_math_003.inputs[1])
    #compare_003.Result -> boolean_math_003.Boolean
    scoop.links.new(compare_003.outputs[0], boolean_math_003.inputs[0])
    #group_002.Geometry -> extrude_mesh_002.Mesh
    scoop.links.new(group_002.outputs[0], extrude_mesh_002.inputs[0])
    #math_2.Value -> math_019.Value
    scoop.links.new(math_2.outputs[0], math_019.inputs[0])
    #group_input_002.shape_front_offset -> math_019.Value
    scoop.links.new(group_input_002.outputs[10], math_019.inputs[1])
    #group_input_005.lip_len -> extrude_mesh_002.Offset Scale
    scoop.links.new(group_input_005.outputs[18], extrude_mesh_002.inputs[3])
    #boolean_math_003.Boolean -> boolean_math_002.Boolean
    scoop.links.new(boolean_math_003.outputs[0], boolean_math_002.inputs[0])
    #boolean_math_002.Boolean -> extrude_mesh_002.Selection
    scoop.links.new(boolean_math_002.outputs[0], extrude_mesh_002.inputs[1])
    #group_input_005.lip_len -> compare_001_2.A
    scoop.links.new(group_input_005.outputs[18], compare_001_2.inputs[0])
    #compare_001_2.Result -> boolean_math_002.Boolean
    scoop.links.new(compare_001_2.outputs[0], boolean_math_002.inputs[1])
    #combine_xyz_006.Vector -> extrude_mesh_002.Offset
    scoop.links.new(combine_xyz_006.outputs[0], extrude_mesh_002.inputs[2])
    #group_input_005.lip_dir -> combine_xyz_006.Z
    scoop.links.new(group_input_005.outputs[19], combine_xyz_006.inputs[2])
    #extrude_mesh_002.Mesh -> scale_elements.Geometry
    scoop.links.new(extrude_mesh_002.outputs[0], scale_elements.inputs[0])
    #extrude_mesh_002.Top -> scale_elements.Selection
    scoop.links.new(extrude_mesh_002.outputs[1], scale_elements.inputs[1])
    #subdivision_surface_001.Mesh -> transform_geometry_004.Geometry
    scoop.links.new(subdivision_surface_001.outputs[0], transform_geometry_004.inputs[0])
    #vector_math.Vector -> transform_geometry_004.Translation
    scoop.links.new(vector_math.outputs[0], transform_geometry_004.inputs[1])
    #math_020.Value -> combine_xyz_007.X
    scoop.links.new(math_020.outputs[0], combine_xyz_007.inputs[0])
    #math_019.Value -> math_020.Value
    scoop.links.new(math_019.outputs[0], math_020.inputs[0])
    #group_input_005.lip_len -> math_020.Value
    scoop.links.new(group_input_005.outputs[18], math_020.inputs[1])
    #math_026.Value -> combine_xyz_007.Y
    scoop.links.new(math_026.outputs[0], combine_xyz_007.inputs[1])
    #combine_xyz.Vector -> transform_geometry_005.Translation
    scoop.links.new(combine_xyz.outputs[0], transform_geometry_005.inputs[1])
    #euler_to_rotation.Rotation -> transform_geometry_005.Rotation
    scoop.links.new(euler_to_rotation.outputs[0], transform_geometry_005.inputs[2])
    #combine_xyz.Vector -> transform_geometry_006.Translation
    scoop.links.new(combine_xyz.outputs[0], transform_geometry_006.inputs[1])
    #euler_to_rotation.Rotation -> transform_geometry_006.Rotation
    scoop.links.new(euler_to_rotation.outputs[0], transform_geometry_006.inputs[2])
    #extrude_mesh.Mesh -> transform_geometry_006.Geometry
    scoop.links.new(extrude_mesh.outputs[0], transform_geometry_006.inputs[0])
    #transform_geometry_006.Geometry -> mesh_boolean_002.Mesh 2
    scoop.links.new(transform_geometry_006.outputs[0], mesh_boolean_002.inputs[1])
    #merge_by_distance_001.Geometry -> mesh_boolean.Mesh
    scoop.links.new(merge_by_distance_001.outputs[0], mesh_boolean.inputs[1])
    #combine_xyz_008.Vector -> cube_001.Size
    scoop.links.new(combine_xyz_008.outputs[0], cube_001.inputs[0])
    #math_036.Value -> combine_xyz_008.Z
    scoop.links.new(math_036.outputs[0], combine_xyz_008.inputs[2])
    #separate_xyz_004.Z -> math_021.Value
    scoop.links.new(separate_xyz_004.outputs[2], math_021.inputs[0])
    #math_036.Value -> math_022.Value
    scoop.links.new(math_036.outputs[0], math_022.inputs[0])
    #math_022.Value -> math_021.Value
    scoop.links.new(math_022.outputs[0], math_021.inputs[1])
    #math_033.Value -> combine_xyz_007.Z
    scoop.links.new(math_033.outputs[0], combine_xyz_007.inputs[2])
    #switch.Output -> repeat_output.Geometry
    scoop.links.new(switch.outputs[0], repeat_output.inputs[0])
    #combine_xyz_007.Vector -> vector_math.Vector
    scoop.links.new(combine_xyz_007.outputs[0], vector_math.inputs[0])
    #combine_xyz_009.Vector -> vector_math.Vector
    scoop.links.new(combine_xyz_009.outputs[0], vector_math.inputs[1])
    #repeat_input.Iteration -> math_025.Value
    scoop.links.new(repeat_input.outputs[0], math_025.inputs[0])
    #math_025.Value -> combine_xyz_009.Y
    scoop.links.new(math_025.outputs[0], combine_xyz_009.inputs[1])
    #math_027.Value -> math_025.Value
    scoop.links.new(math_027.outputs[0], math_025.inputs[1])
    #math_029.Value -> math_026.Value
    scoop.links.new(math_029.outputs[0], math_026.inputs[0])
    #group_input_008.tooth_count -> repeat_input.Iterations
    scoop.links.new(group_input_008.outputs[21], repeat_input.inputs[0])
    #integer_math_007.Value -> math_027.Value
    scoop.links.new(integer_math_007.outputs[0], math_027.inputs[1])
    #bounding_box.Min -> separate_xyz_2.Vector
    scoop.links.new(bounding_box.outputs[1], separate_xyz_2.inputs[0])
    #bounding_box.Max -> separate_xyz_003.Vector
    scoop.links.new(bounding_box.outputs[2], separate_xyz_003.inputs[0])
    #separate_xyz_2.Y -> math_028.Value
    scoop.links.new(separate_xyz_2.outputs[1], math_028.inputs[0])
    #separate_xyz_003.Y -> math_028.Value
    scoop.links.new(separate_xyz_003.outputs[1], math_028.inputs[1])
    #math_028.Value -> math_029.Value
    scoop.links.new(math_028.outputs[0], math_029.inputs[0])
    #math_029.Value -> math_027.Value
    scoop.links.new(math_029.outputs[0], math_027.inputs[0])
    #transform_geometry_001.Geometry -> bounding_box.Geometry
    scoop.links.new(transform_geometry_001.outputs[0], bounding_box.inputs[0])
    #group_input_008.tooth_count -> integer_math_007.Value
    scoop.links.new(group_input_008.outputs[21], integer_math_007.inputs[0])
    #transform_geometry_001.Geometry -> geometry_proximity.Geometry
    scoop.links.new(transform_geometry_001.outputs[0], geometry_proximity.inputs[0])
    #vector_math.Vector -> geometry_proximity.Sample Position
    scoop.links.new(vector_math.outputs[0], geometry_proximity.inputs[2])
    #transform_geometry_004.Geometry -> transform_geometry_007.Geometry
    scoop.links.new(transform_geometry_004.outputs[0], transform_geometry_007.inputs[0])
    #geometry_proximity.Position -> vector_math_001.Vector
    scoop.links.new(geometry_proximity.outputs[0], vector_math_001.inputs[0])
    #vector_math.Vector -> vector_math_001.Vector
    scoop.links.new(vector_math.outputs[0], vector_math_001.inputs[1])
    #geometry_proximity.Distance -> compare_002.A
    scoop.links.new(geometry_proximity.outputs[1], compare_002.inputs[0])
    #compare_002.Result -> switch.Switch
    scoop.links.new(compare_002.outputs[0], switch.inputs[0])
    #separate_xyz_007.X -> combine_xyz_008.X
    scoop.links.new(separate_xyz_007.outputs[0], combine_xyz_008.inputs[0])
    #separate_xyz_007.X -> math_030.Value
    scoop.links.new(separate_xyz_007.outputs[0], math_030.inputs[0])
    #repeat_input.Geometry -> switch.True
    scoop.links.new(repeat_input.outputs[1], switch.inputs[2])
    #vector_math_001.Vector -> vector_math_003.Vector
    scoop.links.new(vector_math_001.outputs[0], vector_math_003.inputs[0])
    #vector_math_003.Vector -> vector_math_002.Vector
    scoop.links.new(vector_math_003.outputs[0], vector_math_002.inputs[0])
    #combine_xyz_010.Vector -> vector_math_002.Vector
    scoop.links.new(combine_xyz_010.outputs[0], vector_math_002.inputs[1])
    #vector_math_002.Vector -> transform_geometry_007.Translation
    scoop.links.new(vector_math_002.outputs[0], transform_geometry_007.inputs[1])
    #separate_xyz_007.Y -> combine_xyz_008.Y
    scoop.links.new(separate_xyz_007.outputs[1], combine_xyz_008.inputs[1])
    #scale_elements_001.Geometry -> subdivision_surface_001.Mesh
    scoop.links.new(scale_elements_001.outputs[0], subdivision_surface_001.inputs[0])
    #integer_math_008.Value -> subdivision_surface_001.Level
    scoop.links.new(integer_math_008.outputs[0], subdivision_surface_001.inputs[1])
    #group_input_006.subdivisions -> integer_math_008.Value
    scoop.links.new(group_input_006.outputs[4], integer_math_008.inputs[0])
    #group_input_009.tooth_edge_crease -> subdivision_surface_001.Edge Crease
    scoop.links.new(group_input_009.outputs[28], subdivision_surface_001.inputs[2])
    #group_input_009.tooth_vertex_crease -> subdivision_surface_001.Vertex Crease
    scoop.links.new(group_input_009.outputs[29], subdivision_surface_001.inputs[3])
    #float_to_integer_004.Integer -> cube_001.Vertices X
    scoop.links.new(float_to_integer_004.outputs[0], cube_001.inputs[1])
    #float_to_integer_005.Integer -> cube_001.Vertices Y
    scoop.links.new(float_to_integer_005.outputs[0], cube_001.inputs[2])
    #float_to_integer_006.Integer -> cube_001.Vertices Z
    scoop.links.new(float_to_integer_006.outputs[0], cube_001.inputs[3])
    #group_input_001.base_vertices -> separate_xyz_005.Vector
    scoop.links.new(group_input_001.outputs[1], separate_xyz_005.inputs[0])
    #separate_xyz_005.X -> float_to_integer_001.Float
    scoop.links.new(separate_xyz_005.outputs[0], float_to_integer_001.inputs[0])
    #separate_xyz_005.Y -> float_to_integer_002.Float
    scoop.links.new(separate_xyz_005.outputs[1], float_to_integer_002.inputs[0])
    #separate_xyz_005.Z -> float_to_integer_003.Float
    scoop.links.new(separate_xyz_005.outputs[2], float_to_integer_003.inputs[0])
    #group_input_001.scale -> cube.Size
    scoop.links.new(group_input_001.outputs[0], cube.inputs[0])
    #group_input_001.scale -> separate_xyz_004.Vector
    scoop.links.new(group_input_001.outputs[0], separate_xyz_004.inputs[0])
    #math_023.Value -> math_011.Value
    scoop.links.new(math_023.outputs[0], math_011.inputs[0])
    #group_input_2.mouth_open -> math_023.Value
    scoop.links.new(group_input_2.outputs[2], math_023.inputs[1])
    #group_input_002.shape_front_lin -> group.Value
    scoop.links.new(group_input_002.outputs[8], group.inputs[2])
    #group_input_002.shape_front_exp -> group.Value
    scoop.links.new(group_input_002.outputs[9], group.inputs[4])
    #group_input_002.shape_front_offset -> group.Value
    scoop.links.new(group_input_002.outputs[10], group.inputs[5])
    #group_input_003.shape_back_lin -> group_001.Value
    scoop.links.new(group_input_003.outputs[11], group_001.inputs[2])
    #group_input_003.shape_back_exp -> group_001.Value
    scoop.links.new(group_input_003.outputs[12], group_001.inputs[4])
    #group_input_003.shape_back_offset -> group_001.Value
    scoop.links.new(group_input_003.outputs[13], group_001.inputs[5])
    #group_input_004.shape_sides_dir_out -> math_024.Value
    scoop.links.new(group_input_004.outputs[14], math_024.inputs[0])
    #math_024.Value -> math_032.Value
    scoop.links.new(math_024.outputs[0], math_032.inputs[0])
    #group_input_004.shape_sides_lin -> group_002.Value
    scoop.links.new(group_input_004.outputs[15], group_002.inputs[2])
    #group_input_004.shape_sides_exp -> group_002.Value
    scoop.links.new(group_input_004.outputs[16], group_002.inputs[4])
    #math_002_2.Value -> group_002.Value
    scoop.links.new(math_002_2.outputs[0], group_002.inputs[5])
    #math_004_2.Value -> group_002.Value
    scoop.links.new(math_004_2.outputs[0], group_002.inputs[6])
    #group_input_004.shape_sides_offset -> math_002_2.Value
    scoop.links.new(group_input_004.outputs[17], math_002_2.inputs[1])
    #math_032.Value -> math_002_2.Value
    scoop.links.new(math_032.outputs[0], math_002_2.inputs[0])
    #math_032.Value -> math_004_2.Value
    scoop.links.new(math_032.outputs[0], math_004_2.inputs[0])
    #math_021.Value -> math_033.Value
    scoop.links.new(math_021.outputs[0], math_033.inputs[0])
    #group_input_005.lip_len -> math_035.Value
    scoop.links.new(group_input_005.outputs[18], math_035.inputs[0])
    #group_input_005.lip_dir -> math_035.Value
    scoop.links.new(group_input_005.outputs[19], math_035.inputs[1])
    #math_035.Value -> math_033.Value
    scoop.links.new(math_035.outputs[0], math_033.inputs[1])
    #group_input_005.lip_width -> scale_elements.Scale
    scoop.links.new(group_input_005.outputs[20], scale_elements.inputs[2])
    #set_mesh_normal.Mesh -> triangulate.Mesh
    scoop.links.new(set_mesh_normal.outputs[0], triangulate.inputs[0])
    #group_input_007.mount_offset_lin -> separate_xyz_006.Vector
    scoop.links.new(group_input_007.outputs[31], separate_xyz_006.inputs[0])
    #separate_xyz_007.Z -> math_031.Value
    scoop.links.new(separate_xyz_007.outputs[2], math_031.inputs[1])
    #math_034.Value -> combine_xyz_010.X
    scoop.links.new(math_034.outputs[0], combine_xyz_010.inputs[0])
    #math_022.Value -> math_031.Value
    scoop.links.new(math_022.outputs[0], math_031.inputs[0])
    #math_031.Value -> combine_xyz_010.Z
    scoop.links.new(math_031.outputs[0], combine_xyz_010.inputs[2])
    #math_030.Value -> math_034.Value
    scoop.links.new(math_030.outputs[0], math_034.inputs[0])
    #group_input_008.tooth_inset_dist -> math_034.Value
    scoop.links.new(group_input_008.outputs[25], math_034.inputs[1])
    #math_037.Value -> compare_002.B
    scoop.links.new(math_037.outputs[0], compare_002.inputs[1])
    #group_input_008.tooth_scale -> separate_xyz_007.Vector
    scoop.links.new(group_input_008.outputs[22], separate_xyz_007.inputs[0])
    #group_input_008.tooth_validity -> math_037.Value
    scoop.links.new(group_input_008.outputs[26], math_037.inputs[0])
    #math_039.Value -> math_037.Value
    scoop.links.new(math_039.outputs[0], math_037.inputs[1])
    #separate_xyz_007.Z -> math_038.Value
    scoop.links.new(separate_xyz_007.outputs[2], math_038.inputs[0])
    #separate_xyz_007.Y -> math_038.Value
    scoop.links.new(separate_xyz_007.outputs[1], math_038.inputs[1])
    #math_038.Value -> math_039.Value
    scoop.links.new(math_038.outputs[0], math_039.inputs[0])
    #group_input_007.wall_thickness -> math_036.Value
    scoop.links.new(group_input_007.outputs[3], math_036.inputs[1])
    #separate_xyz_007.Z -> math_036.Value
    scoop.links.new(separate_xyz_007.outputs[2], math_036.inputs[0])
    #separate_xyz_008.X -> float_to_integer_004.Float
    scoop.links.new(separate_xyz_008.outputs[0], float_to_integer_004.inputs[0])
    #separate_xyz_008.Y -> float_to_integer_005.Float
    scoop.links.new(separate_xyz_008.outputs[1], float_to_integer_005.inputs[0])
    #separate_xyz_008.Z -> float_to_integer_006.Float
    scoop.links.new(separate_xyz_008.outputs[2], float_to_integer_006.inputs[0])
    #group_input_009.tooth_base_vertices -> separate_xyz_008.Vector
    scoop.links.new(group_input_009.outputs[24], separate_xyz_008.inputs[0])
    #group_input_009.tooth_subdivisions_offset -> integer_math_008.Value
    scoop.links.new(group_input_009.outputs[27], integer_math_008.inputs[1])
    #integer_math_005.Value -> math_018.Value
    scoop.links.new(integer_math_005.outputs[0], math_018.inputs[1])
    #math_018.Value -> float_to_integer_007.Float
    scoop.links.new(math_018.outputs[0], float_to_integer_007.inputs[0])
    #integer_math_006.Value -> cylinder_002.Vertices
    scoop.links.new(integer_math_006.outputs[0], cylinder_002.inputs[0])
    #group_input_007.mount_vertices_ratio -> math_018.Value
    scoop.links.new(group_input_007.outputs[33], math_018.inputs[0])
    #float_to_integer_007.Integer -> integer_math_006.Value
    scoop.links.new(float_to_integer_007.outputs[0], integer_math_006.inputs[0])
    #set_shade_smooth.Geometry -> set_material.Geometry
    scoop.links.new(set_shade_smooth.outputs[0], set_material.inputs[0])
    #group_input_010.material -> set_material.Material
    scoop.links.new(group_input_010.outputs[7], set_material.inputs[2])
    #integer_math_006.Value -> math_040.Value
    scoop.links.new(integer_math_006.outputs[0], math_040.inputs[1])
    #math_040.Value -> merge_by_distance.Distance
    scoop.links.new(math_040.outputs[0], merge_by_distance.inputs[2])
    #mesh_boolean_003.Intersecting Edges -> merge_by_distance.Selection
    scoop.links.new(mesh_boolean_003.outputs[1], merge_by_distance.inputs[1])
    #integer.Integer -> repeat_input.Integer
    scoop.links.new(integer.outputs[0], repeat_input.inputs[2])
    #repeat_input.Integer -> integer_math_003.Value
    scoop.links.new(repeat_input.outputs[2], integer_math_003.inputs[0])
    #compare_002.Result -> integer_math_003.Value
    scoop.links.new(compare_002.outputs[0], integer_math_003.inputs[1])
    #integer_math_003.Value -> repeat_output.Integer
    scoop.links.new(integer_math_003.outputs[0], repeat_output.inputs[1])
    #repeat_output.Integer -> compare_006.A
    scoop.links.new(repeat_output.outputs[1], compare_006.inputs[2])
    #switch_002.Output -> transform_geometry_005.Geometry
    scoop.links.new(switch_002.outputs[0], transform_geometry_005.inputs[0])
    #mesh_boolean.Mesh -> switch_002.True
    scoop.links.new(mesh_boolean.outputs[0], switch_002.inputs[2])
    #merge_by_distance_001.Geometry -> switch_002.False
    scoop.links.new(merge_by_distance_001.outputs[0], switch_002.inputs[1])
    #compare_006.Result -> switch_002.Switch
    scoop.links.new(compare_006.outputs[0], switch_002.inputs[0])
    #cube_001.Mesh -> scale_elements_001.Geometry
    scoop.links.new(cube_001.outputs[0], scale_elements_001.inputs[0])
    #normal.True Normal -> compare_007.A
    scoop.links.new(normal.outputs[1], compare_007.inputs[4])
    #compare_007.Result -> scale_elements_001.Selection
    scoop.links.new(compare_007.outputs[0], scale_elements_001.inputs[1])
    #transform_geometry_007.Geometry -> mesh_boolean_001.Mesh
    scoop.links.new(transform_geometry_007.outputs[0], mesh_boolean_001.inputs[1])
    #mesh_boolean_001.Mesh -> switch.False
    scoop.links.new(mesh_boolean_001.outputs[0], switch.inputs[1])
    #group_input_009.tooth_taper_scale -> scale_elements_001.Scale
    scoop.links.new(group_input_009.outputs[23], scale_elements_001.inputs[2])
    #transform_geometry_001.Geometry -> join_geometry_001.Geometry
    scoop.links.new(transform_geometry_001.outputs[0], join_geometry_001.inputs[0])
    #transform_geometry_005.Geometry -> mesh_boolean_003.Mesh
    scoop.links.new(transform_geometry_005.outputs[0], mesh_boolean_003.inputs[1])
    #repeat_output.Geometry -> mesh_boolean.Mesh
    scoop.links.new(repeat_output.outputs[0], mesh_boolean.inputs[1])
    #repeat_input.Geometry -> mesh_boolean_001.Mesh
    scoop.links.new(repeat_input.outputs[1], mesh_boolean_001.inputs[1])
    return scoop

scoop = scoop_node_group()

#initialize random__normal_ node group
def random__normal__node_group():
    random__normal_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Random (Normal)")

    random__normal_.color_tag = 'NONE'
    random__normal_.description = ""
    random__normal_.default_group_node_width = 140
    


    #random__normal_ interface
    #Socket Value
    value_socket_8 = random__normal_.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket_8.default_value = 0.0
    value_socket_8.min_value = -3.4028234663852886e+38
    value_socket_8.max_value = 3.4028234663852886e+38
    value_socket_8.subtype = 'NONE'
    value_socket_8.attribute_domain = 'POINT'
    value_socket_8.default_input = 'VALUE'
    value_socket_8.structure_type = 'AUTO'

    #Socket Non-Negative
    non_negative_socket = random__normal_.interface.new_socket(name = "Non-Negative", in_out='INPUT', socket_type = 'NodeSocketBool')
    non_negative_socket.default_value = True
    non_negative_socket.attribute_domain = 'POINT'
    non_negative_socket.default_input = 'VALUE'
    non_negative_socket.structure_type = 'AUTO'

    #Socket Mean
    mean_socket = random__normal_.interface.new_socket(name = "Mean", in_out='INPUT', socket_type = 'NodeSocketFloat')
    mean_socket.default_value = 0.0
    mean_socket.min_value = -3.4028234663852886e+38
    mean_socket.max_value = 3.4028234663852886e+38
    mean_socket.subtype = 'NONE'
    mean_socket.attribute_domain = 'POINT'
    mean_socket.default_input = 'VALUE'
    mean_socket.structure_type = 'AUTO'

    #Socket Std. Dev.
    std__dev__socket = random__normal_.interface.new_socket(name = "Std. Dev.", in_out='INPUT', socket_type = 'NodeSocketFloat')
    std__dev__socket.default_value = 1.0
    std__dev__socket.min_value = 0.0
    std__dev__socket.max_value = 3.4028234663852886e+38
    std__dev__socket.subtype = 'NONE'
    std__dev__socket.attribute_domain = 'POINT'
    std__dev__socket.default_input = 'VALUE'
    std__dev__socket.structure_type = 'AUTO'

    #Socket Seed
    seed_socket = random__normal_.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket.default_value = 0
    seed_socket.min_value = 0
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.hide_value = True
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'

    #Socket Offset
    offset_socket = random__normal_.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
    offset_socket.default_value = 0
    offset_socket.min_value = 0
    offset_socket.max_value = 2147483647
    offset_socket.subtype = 'NONE'
    offset_socket.attribute_domain = 'POINT'
    offset_socket.default_input = 'VALUE'
    offset_socket.structure_type = 'AUTO'


    #initialize random__normal_ nodes
    #node Frame
    frame = random__normal_.nodes.new("NodeFrame")
    frame.label = "2 * pi * U_2"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    #node Frame.003
    frame_003 = random__normal_.nodes.new("NodeFrame")
    frame_003.label = "X_1"
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    #node Frame.001
    frame_001 = random__normal_.nodes.new("NodeFrame")
    frame_001.label = "sqrt(-2 * ln(U_1))"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    #node Math.002
    math_002_3 = random__normal_.nodes.new("ShaderNodeMath")
    math_002_3.name = "Math.002"
    math_002_3.operation = 'MULTIPLY'
    math_002_3.use_clamp = False
    #Value_001
    math_002_3.inputs[1].default_value = 6.2831854820251465

    #node Random Value.001
    random_value_001 = random__normal_.nodes.new("FunctionNodeRandomValue")
    random_value_001.label = "U_2"
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = 'FLOAT'
    #Min_001
    random_value_001.inputs[2].default_value = 0.0
    #Max_001
    random_value_001.inputs[3].default_value = 1.0

    #node Math.010
    math_010_2 = random__normal_.nodes.new("ShaderNodeMath")
    math_010_2.name = "Math.010"
    math_010_2.operation = 'ADD'
    math_010_2.use_clamp = False
    math_010_2.inputs[1].hide = True
    math_010_2.inputs[2].hide = True
    #Value_001
    math_010_2.inputs[1].default_value = 1.0

    #node Math.005
    math_005_2 = random__normal_.nodes.new("ShaderNodeMath")
    math_005_2.name = "Math.005"
    math_005_2.operation = 'MULTIPLY'
    math_005_2.use_clamp = False

    #node Math.004
    math_004_3 = random__normal_.nodes.new("ShaderNodeMath")
    math_004_3.name = "Math.004"
    math_004_3.operation = 'COSINE'
    math_004_3.use_clamp = False

    #node Math.008
    math_008_2 = random__normal_.nodes.new("ShaderNodeMath")
    math_008_2.name = "Math.008"
    math_008_2.operation = 'MULTIPLY'
    math_008_2.use_clamp = False

    #node Math.007
    math_007_3 = random__normal_.nodes.new("ShaderNodeMath")
    math_007_3.name = "Math.007"
    math_007_3.operation = 'ADD'
    math_007_3.use_clamp = False

    #node Math
    math_3 = random__normal_.nodes.new("ShaderNodeMath")
    math_3.name = "Math"
    math_3.operation = 'LOGARITHM'
    math_3.use_clamp = False
    #Value_001
    math_3.inputs[1].default_value = 2.7182817459106445

    #node Random Value.002
    random_value_002 = random__normal_.nodes.new("FunctionNodeRandomValue")
    random_value_002.label = "U_1"
    random_value_002.name = "Random Value.002"
    random_value_002.data_type = 'FLOAT'
    #Min_001
    random_value_002.inputs[2].default_value = 0.0
    #Max_001
    random_value_002.inputs[3].default_value = 1.0

    #node Math.001
    math_001_3 = random__normal_.nodes.new("ShaderNodeMath")
    math_001_3.name = "Math.001"
    math_001_3.operation = 'MULTIPLY'
    math_001_3.use_clamp = False
    #Value_001
    math_001_3.inputs[1].default_value = -2.0

    #node Math.003
    math_003_3 = random__normal_.nodes.new("ShaderNodeMath")
    math_003_3.name = "Math.003"
    math_003_3.operation = 'SQRT'
    math_003_3.use_clamp = False

    #node Group Output
    group_output_3 = random__normal_.nodes.new("NodeGroupOutput")
    group_output_3.name = "Group Output"
    group_output_3.is_active_output = True

    #node Group Input
    group_input_3 = random__normal_.nodes.new("NodeGroupInput")
    group_input_3.name = "Group Input"

    #node Switch
    switch_1 = random__normal_.nodes.new("GeometryNodeSwitch")
    switch_1.name = "Switch"
    switch_1.input_type = 'FLOAT'

    #node Math.006
    math_006_3 = random__normal_.nodes.new("ShaderNodeMath")
    math_006_3.name = "Math.006"
    math_006_3.operation = 'MAXIMUM'
    math_006_3.use_clamp = False
    #Value_001
    math_006_3.inputs[1].default_value = 0.0




    #Set parents
    math_002_3.parent = frame
    random_value_001.parent = frame
    math_010_2.parent = frame
    math_005_2.parent = frame_003
    math_004_3.parent = frame_003
    math_3.parent = frame_001
    random_value_002.parent = frame_001
    math_001_3.parent = frame_001
    math_003_3.parent = frame_001

    #Set locations
    frame.location = (-1061.0, -451.0)
    frame_003.location = (-211.0, -297.0)
    frame_001.location = (-1063.0, -200.0)
    math_002_3.location = (409.9722900390625, -45.65386962890625)
    random_value_001.location = (219.9722900390625, -36.15386962890625)
    math_010_2.location = (29.9722900390625, -153.2261962890625)
    math_005_2.location = (219.63975524902344, -36.41009521484375)
    math_004_3.location = (29.639755249023438, -126.29949951171875)
    math_008_2.location = (210.5360565185547, -105.03559112548828)
    math_007_3.location = (400.53607177734375, 29.03577995300293)
    math_3.location = (219.6490478515625, -45.28599548339844)
    random_value_002.location = (29.6490478515625, -35.78599548339844)
    math_001_3.location = (409.6490478515625, -45.28599548339844)
    math_003_3.location = (599.6490478515625, -56.2860107421875)
    group_output_3.location = (970.5360717773438, -8.96422004699707)
    group_input_3.location = (-1399.3758544921875, -91.58724975585938)
    switch_1.location = (780.5360717773438, 26.53577995300293)
    math_006_3.location = (590.5360717773438, -88.39610290527344)

    #Set dimensions
    frame.width, frame.height = 580.0, 309.0
    frame_003.width, frame_003.height = 390.0, 282.0
    frame_001.width, frame_001.height = 770.0, 233.0
    math_002_3.width, math_002_3.height = 140.0, 100.0
    random_value_001.width, random_value_001.height = 140.0, 100.0
    math_010_2.width, math_010_2.height = 140.0, 100.0
    math_005_2.width, math_005_2.height = 140.0, 100.0
    math_004_3.width, math_004_3.height = 140.0, 100.0
    math_008_2.width, math_008_2.height = 140.0, 100.0
    math_007_3.width, math_007_3.height = 140.0, 100.0
    math_3.width, math_3.height = 140.0, 100.0
    random_value_002.width, random_value_002.height = 140.0, 100.0
    math_001_3.width, math_001_3.height = 140.0, 100.0
    math_003_3.width, math_003_3.height = 140.0, 100.0
    group_output_3.width, group_output_3.height = 140.0, 100.0
    group_input_3.width, group_input_3.height = 140.0, 100.0
    switch_1.width, switch_1.height = 140.0, 100.0
    math_006_3.width, math_006_3.height = 140.0, 100.0

    #initialize random__normal_ links
    #random_value_002.Value -> math_3.Value
    random__normal_.links.new(random_value_002.outputs[1], math_3.inputs[0])
    #math_3.Value -> math_001_3.Value
    random__normal_.links.new(math_3.outputs[0], math_001_3.inputs[0])
    #random_value_001.Value -> math_002_3.Value
    random__normal_.links.new(random_value_001.outputs[1], math_002_3.inputs[0])
    #math_002_3.Value -> math_004_3.Value
    random__normal_.links.new(math_002_3.outputs[0], math_004_3.inputs[0])
    #math_003_3.Value -> math_005_2.Value
    random__normal_.links.new(math_003_3.outputs[0], math_005_2.inputs[0])
    #group_input_3.Seed -> random_value_002.Seed
    random__normal_.links.new(group_input_3.outputs[3], random_value_002.inputs[8])
    #group_input_3.Seed -> math_010_2.Value
    random__normal_.links.new(group_input_3.outputs[3], math_010_2.inputs[0])
    #math_010_2.Value -> random_value_001.Seed
    random__normal_.links.new(math_010_2.outputs[0], random_value_001.inputs[8])
    #group_input_3.Std. Dev. -> math_008_2.Value
    random__normal_.links.new(group_input_3.outputs[2], math_008_2.inputs[0])
    #group_input_3.Mean -> math_007_3.Value
    random__normal_.links.new(group_input_3.outputs[1], math_007_3.inputs[0])
    #math_008_2.Value -> math_007_3.Value
    random__normal_.links.new(math_008_2.outputs[0], math_007_3.inputs[1])
    #math_005_2.Value -> math_008_2.Value
    random__normal_.links.new(math_005_2.outputs[0], math_008_2.inputs[1])
    #math_004_3.Value -> math_005_2.Value
    random__normal_.links.new(math_004_3.outputs[0], math_005_2.inputs[1])
    #math_001_3.Value -> math_003_3.Value
    random__normal_.links.new(math_001_3.outputs[0], math_003_3.inputs[0])
    #group_input_3.Offset -> random_value_001.ID
    random__normal_.links.new(group_input_3.outputs[4], random_value_001.inputs[7])
    #group_input_3.Offset -> random_value_002.ID
    random__normal_.links.new(group_input_3.outputs[4], random_value_002.inputs[7])
    #group_input_3.Non-Negative -> switch_1.Switch
    random__normal_.links.new(group_input_3.outputs[0], switch_1.inputs[0])
    #math_007_3.Value -> math_006_3.Value
    random__normal_.links.new(math_007_3.outputs[0], math_006_3.inputs[0])
    #switch_1.Output -> group_output_3.Value
    random__normal_.links.new(switch_1.outputs[0], group_output_3.inputs[0])
    #math_007_3.Value -> switch_1.False
    random__normal_.links.new(math_007_3.outputs[0], switch_1.inputs[1])
    #math_006_3.Value -> switch_1.True
    random__normal_.links.new(math_006_3.outputs[0], switch_1.inputs[2])
    return random__normal_

random__normal_ = random__normal__node_group()

#initialize random__uniform_ node group
def random__uniform__node_group():
    random__uniform_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Random (Uniform)")

    random__uniform_.color_tag = 'NONE'
    random__uniform_.description = ""
    random__uniform_.default_group_node_width = 140
    


    #random__uniform_ interface
    #Socket Value
    value_socket_9 = random__uniform_.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket_9.default_value = 0.0
    value_socket_9.min_value = -3.4028234663852886e+38
    value_socket_9.max_value = 3.4028234663852886e+38
    value_socket_9.subtype = 'NONE'
    value_socket_9.attribute_domain = 'POINT'
    value_socket_9.default_input = 'VALUE'
    value_socket_9.structure_type = 'AUTO'

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
    seed_socket_1 = random__uniform_.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket_1.default_value = 0
    seed_socket_1.min_value = -2147483648
    seed_socket_1.max_value = 2147483647
    seed_socket_1.subtype = 'NONE'
    seed_socket_1.attribute_domain = 'POINT'
    seed_socket_1.hide_value = True
    seed_socket_1.default_input = 'VALUE'
    seed_socket_1.structure_type = 'AUTO'

    #Socket Offset
    offset_socket_1 = random__uniform_.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
    offset_socket_1.default_value = 0
    offset_socket_1.min_value = 0
    offset_socket_1.max_value = 2147483647
    offset_socket_1.subtype = 'NONE'
    offset_socket_1.attribute_domain = 'POINT'
    offset_socket_1.default_input = 'VALUE'
    offset_socket_1.structure_type = 'AUTO'


    #initialize random__uniform_ nodes
    #node Group Output
    group_output_4 = random__uniform_.nodes.new("NodeGroupOutput")
    group_output_4.name = "Group Output"
    group_output_4.is_active_output = True

    #node Group Input
    group_input_4 = random__uniform_.nodes.new("NodeGroupInput")
    group_input_4.name = "Group Input"

    #node Random Value.011
    random_value_011 = random__uniform_.nodes.new("FunctionNodeRandomValue")
    random_value_011.name = "Random Value.011"
    random_value_011.data_type = 'FLOAT'





    #Set locations
    group_output_4.location = (190.0, 0.0)
    group_input_4.location = (-200.0, 0.0)
    random_value_011.location = (0.0, 0.0)

    #Set dimensions
    group_output_4.width, group_output_4.height = 140.0, 100.0
    group_input_4.width, group_input_4.height = 140.0, 100.0
    random_value_011.width, random_value_011.height = 140.0, 100.0

    #initialize random__uniform_ links
    #random_value_011.Value -> group_output_4.Value
    random__uniform_.links.new(random_value_011.outputs[1], group_output_4.inputs[0])
    #group_input_4.Min -> random_value_011.Min
    random__uniform_.links.new(group_input_4.outputs[0], random_value_011.inputs[2])
    #group_input_4.Max -> random_value_011.Max
    random__uniform_.links.new(group_input_4.outputs[1], random_value_011.inputs[3])
    #group_input_4.Offset -> random_value_011.ID
    random__uniform_.links.new(group_input_4.outputs[3], random_value_011.inputs[7])
    #group_input_4.Seed -> random_value_011.Seed
    random__uniform_.links.new(group_input_4.outputs[2], random_value_011.inputs[8])
    return random__uniform_

random__uniform_ = random__uniform__node_group()

#initialize random_scoop node group
def random_scoop_node_group():
    random_scoop = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "random_scoop")

    random_scoop.color_tag = 'NONE'
    random_scoop.description = ""
    random_scoop.default_group_node_width = 140
    

    random_scoop.is_modifier = True

    #random_scoop interface
    #Socket Geometry
    geometry_socket_5 = random_scoop.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_5.attribute_domain = 'POINT'
    geometry_socket_5.default_input = 'VALUE'
    geometry_socket_5.structure_type = 'AUTO'

    #Socket seed
    seed_socket_2 = random_scoop.interface.new_socket(name = "seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket_2.default_value = 0
    seed_socket_2.min_value = 0
    seed_socket_2.max_value = 2147483647
    seed_socket_2.subtype = 'NONE'
    seed_socket_2.attribute_domain = 'POINT'
    seed_socket_2.force_non_field = True
    seed_socket_2.default_input = 'VALUE'
    seed_socket_2.structure_type = 'SINGLE'

    #Socket subdivisions
    subdivisions_socket_1 = random_scoop.interface.new_socket(name = "subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt')
    subdivisions_socket_1.default_value = 2
    subdivisions_socket_1.min_value = 0
    subdivisions_socket_1.max_value = 6
    subdivisions_socket_1.subtype = 'NONE'
    subdivisions_socket_1.attribute_domain = 'POINT'
    subdivisions_socket_1.force_non_field = True
    subdivisions_socket_1.default_input = 'VALUE'
    subdivisions_socket_1.structure_type = 'SINGLE'

    #Socket material
    material_socket_1 = random_scoop.interface.new_socket(name = "material", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    material_socket_1.attribute_domain = 'POINT'
    material_socket_1.default_input = 'VALUE'
    material_socket_1.structure_type = 'AUTO'

    #Socket tooth_subdivisions_offset
    tooth_subdivisions_offset_socket_1 = random_scoop.interface.new_socket(name = "tooth_subdivisions_offset", in_out='INPUT', socket_type = 'NodeSocketInt')
    tooth_subdivisions_offset_socket_1.default_value = -1
    tooth_subdivisions_offset_socket_1.min_value = -10
    tooth_subdivisions_offset_socket_1.max_value = 2
    tooth_subdivisions_offset_socket_1.subtype = 'NONE'
    tooth_subdivisions_offset_socket_1.attribute_domain = 'POINT'
    tooth_subdivisions_offset_socket_1.force_non_field = True
    tooth_subdivisions_offset_socket_1.default_input = 'VALUE'
    tooth_subdivisions_offset_socket_1.structure_type = 'SINGLE'

    #Socket mount_radius
    mount_radius_socket_1 = random_scoop.interface.new_socket(name = "mount_radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
    mount_radius_socket_1.default_value = 0.02500000037252903
    mount_radius_socket_1.min_value = 0.0
    mount_radius_socket_1.max_value = 3.4028234663852886e+38
    mount_radius_socket_1.subtype = 'DISTANCE'
    mount_radius_socket_1.attribute_domain = 'POINT'
    mount_radius_socket_1.force_non_field = True
    mount_radius_socket_1.default_input = 'VALUE'
    mount_radius_socket_1.structure_type = 'SINGLE'

    #Socket mount_vertices_ratio
    mount_vertices_ratio_socket_1 = random_scoop.interface.new_socket(name = "mount_vertices_ratio", in_out='INPUT', socket_type = 'NodeSocketFloat')
    mount_vertices_ratio_socket_1.default_value = 1.0
    mount_vertices_ratio_socket_1.min_value = 0.0
    mount_vertices_ratio_socket_1.max_value = 5.0
    mount_vertices_ratio_socket_1.subtype = 'FACTOR'
    mount_vertices_ratio_socket_1.attribute_domain = 'POINT'
    mount_vertices_ratio_socket_1.force_non_field = True
    mount_vertices_ratio_socket_1.default_input = 'VALUE'
    mount_vertices_ratio_socket_1.structure_type = 'SINGLE'


    #initialize random_scoop nodes
    #node Group Output
    group_output_5 = random_scoop.nodes.new("NodeGroupOutput")
    group_output_5.name = "Group Output"
    group_output_5.is_active_output = True

    #node scoop
    scoop_1 = random_scoop.nodes.new("GeometryNodeGroup")
    scoop_1.name = "scoop"
    scoop_1.node_tree = scoop

    #node Random (Normal)
    random__normal__1 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__1.name = "Random (Normal)"
    random__normal__1.node_tree = random__normal_
    #Socket_1
    random__normal__1.inputs[0].default_value = True
    #Socket_2
    random__normal__1.inputs[1].default_value = 0.125
    #Socket_3
    random__normal__1.inputs[2].default_value = 0.009999999776482582
    #Socket_5
    random__normal__1.inputs[4].default_value = 1

    #node Combine XYZ
    combine_xyz_1 = random_scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_1.name = "Combine XYZ"

    #node Integer Math
    integer_math_1 = random_scoop.nodes.new("FunctionNodeIntegerMath")
    integer_math_1.name = "Integer Math"
    integer_math_1.operation = 'ADD'

    #node Group Input
    group_input_5 = random_scoop.nodes.new("NodeGroupInput")
    group_input_5.name = "Group Input"

    #node Integer
    integer_1 = random_scoop.nodes.new("FunctionNodeInputInt")
    integer_1.label = "Seed Offset"
    integer_1.name = "Integer"
    integer_1.integer = 0

    #node Reroute.001
    reroute_001 = random_scoop.nodes.new("NodeReroute")
    reroute_001.label = "seed"
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketInt"
    #node Random (Normal).001
    random__normal__001 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__001.name = "Random (Normal).001"
    random__normal__001.node_tree = random__normal_
    #Socket_1
    random__normal__001.inputs[0].default_value = True
    #Socket_2
    random__normal__001.inputs[1].default_value = 0.15000000596046448
    #Socket_3
    random__normal__001.inputs[2].default_value = 0.009999999776482582
    #Socket_5
    random__normal__001.inputs[4].default_value = 2

    #node Random (Normal).002
    random__normal__002 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__002.name = "Random (Normal).002"
    random__normal__002.node_tree = random__normal_
    #Socket_1
    random__normal__002.inputs[0].default_value = True
    #Socket_2
    random__normal__002.inputs[1].default_value = 0.15000000596046448
    #Socket_3
    random__normal__002.inputs[2].default_value = 0.009999999776482582
    #Socket_5
    random__normal__002.inputs[4].default_value = 3

    #node Combine XYZ.001
    combine_xyz_001 = random_scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"

    #node Random (Uniform).001
    random__uniform__001 = random_scoop.nodes.new("GeometryNodeGroup")
    random__uniform__001.name = "Random (Uniform).001"
    random__uniform__001.node_tree = random__uniform_
    #Socket_1
    random__uniform__001.inputs[0].default_value = 2.0
    #Socket_2
    random__uniform__001.inputs[1].default_value = 2.75
    #Socket_4
    random__uniform__001.inputs[3].default_value = 4

    #node Random (Uniform).002
    random__uniform__002 = random_scoop.nodes.new("GeometryNodeGroup")
    random__uniform__002.name = "Random (Uniform).002"
    random__uniform__002.node_tree = random__uniform_
    #Socket_1
    random__uniform__002.inputs[0].default_value = 2.0
    #Socket_2
    random__uniform__002.inputs[1].default_value = 2.75
    #Socket_4
    random__uniform__002.inputs[3].default_value = 5

    #node Random (Normal).003
    random__normal__003 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__003.name = "Random (Normal).003"
    random__normal__003.node_tree = random__normal_
    #Socket_1
    random__normal__003.inputs[0].default_value = True
    #Socket_2
    random__normal__003.inputs[1].default_value = 0.0
    #Socket_3
    random__normal__003.inputs[2].default_value = 1.0
    #Socket_5
    random__normal__003.inputs[4].default_value = 6

    #node Math
    math_4 = random_scoop.nodes.new("ShaderNodeMath")
    math_4.name = "Math"
    math_4.operation = 'ADD'
    math_4.use_clamp = False
    #Value_001
    math_4.inputs[1].default_value = 3.0

    #node Random (Normal).004
    random__normal__004 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__004.name = "Random (Normal).004"
    random__normal__004.node_tree = random__normal_
    #Socket_1
    random__normal__004.inputs[0].default_value = False
    #Socket_2
    random__normal__004.inputs[1].default_value = 1.0
    #Socket_3
    random__normal__004.inputs[2].default_value = 0.20000000298023224
    #Socket_5
    random__normal__004.inputs[4].default_value = 7

    #node Clamp
    clamp = random_scoop.nodes.new("ShaderNodeClamp")
    clamp.name = "Clamp"
    clamp.clamp_type = 'MINMAX'
    #Max
    clamp.inputs[2].default_value = 1.0

    #node Math.001
    math_001_4 = random_scoop.nodes.new("ShaderNodeMath")
    math_001_4.name = "Math.001"
    math_001_4.operation = 'DIVIDE'
    math_001_4.use_clamp = False
    #Value
    math_001_4.inputs[0].default_value = 1.0

    #node Float to Integer
    float_to_integer_1 = random_scoop.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_1.name = "Float to Integer"
    float_to_integer_1.rounding_mode = 'ROUND'

    #node Math.002
    math_002_4 = random_scoop.nodes.new("ShaderNodeMath")
    math_002_4.name = "Math.002"
    math_002_4.operation = 'ADD'
    math_002_4.use_clamp = False
    #Value_001
    math_002_4.inputs[1].default_value = 0.9990000128746033

    #node Random (Uniform).003
    random__uniform__003 = random_scoop.nodes.new("GeometryNodeGroup")
    random__uniform__003.name = "Random (Uniform).003"
    random__uniform__003.node_tree = random__uniform_
    #Socket_1
    random__uniform__003.inputs[0].default_value = 0.0020000000949949026
    #Socket_2
    random__uniform__003.inputs[1].default_value = 0.006000000052154064
    #Socket_4
    random__uniform__003.inputs[3].default_value = 8

    #node Random (Normal).005
    random__normal__005 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__005.name = "Random (Normal).005"
    random__normal__005.node_tree = random__normal_
    #Socket_1
    random__normal__005.inputs[0].default_value = True
    #Socket_2
    random__normal__005.inputs[1].default_value = 0.05000000074505806
    #Socket_3
    random__normal__005.inputs[2].default_value = 0.20000000298023224
    #Socket_5
    random__normal__005.inputs[4].default_value = 9

    #node Random (Normal).006
    random__normal__006 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__006.name = "Random (Normal).006"
    random__normal__006.node_tree = random__normal_
    #Socket_1
    random__normal__006.inputs[0].default_value = True
    #Socket_2
    random__normal__006.inputs[1].default_value = 0.02500000037252903
    #Socket_3
    random__normal__006.inputs[2].default_value = 0.10000000149011612
    #Socket_5
    random__normal__006.inputs[4].default_value = 10

    #node Random (Normal).007
    random__normal__007 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__007.name = "Random (Normal).007"
    random__normal__007.node_tree = random__normal_
    #Socket_1
    random__normal__007.inputs[0].default_value = False
    #Socket_2
    random__normal__007.inputs[1].default_value = 0.0
    #Socket_3
    random__normal__007.inputs[2].default_value = 0.03999999910593033
    #Socket_5
    random__normal__007.inputs[4].default_value = 11

    #node Random (Normal).008
    random__normal__008 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__008.name = "Random (Normal).008"
    random__normal__008.node_tree = random__normal_
    #Socket_1
    random__normal__008.inputs[0].default_value = True
    #Socket_2
    random__normal__008.inputs[1].default_value = 0.6000000238418579
    #Socket_3
    random__normal__008.inputs[2].default_value = 0.3330000042915344
    #Socket_5
    random__normal__008.inputs[4].default_value = 12

    #node Random (Normal).009
    random__normal__009 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__009.name = "Random (Normal).009"
    random__normal__009.node_tree = random__normal_
    #Socket_1
    random__normal__009.inputs[0].default_value = True
    #Socket_2
    random__normal__009.inputs[1].default_value = 0.0
    #Socket_3
    random__normal__009.inputs[2].default_value = 0.009999999776482582
    #Socket_5
    random__normal__009.inputs[4].default_value = 13

    #node Random (Normal).010
    random__normal__010 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__010.name = "Random (Normal).010"
    random__normal__010.node_tree = random__normal_
    #Socket_1
    random__normal__010.inputs[0].default_value = False
    #Socket_2
    random__normal__010.inputs[1].default_value = 0.0
    #Socket_3
    random__normal__010.inputs[2].default_value = 0.03999999910593033
    #Socket_5
    random__normal__010.inputs[4].default_value = 14

    #node Random (Normal).011
    random__normal__011 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__011.name = "Random (Normal).011"
    random__normal__011.node_tree = random__normal_
    #Socket_1
    random__normal__011.inputs[0].default_value = True
    #Socket_2
    random__normal__011.inputs[1].default_value = 0.5
    #Socket_3
    random__normal__011.inputs[2].default_value = 0.3330000042915344
    #Socket_5
    random__normal__011.inputs[4].default_value = 15

    #node Random (Normal).012
    random__normal__012 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__012.name = "Random (Normal).012"
    random__normal__012.node_tree = random__normal_
    #Socket_1
    random__normal__012.inputs[0].default_value = True
    #Socket_2
    random__normal__012.inputs[1].default_value = 0.0
    #Socket_3
    random__normal__012.inputs[2].default_value = 0.009999999776482582
    #Socket_5
    random__normal__012.inputs[4].default_value = 16

    #node Random (Normal).013
    random__normal__013 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__013.name = "Random (Normal).013"
    random__normal__013.node_tree = random__normal_
    #Socket_1
    random__normal__013.inputs[0].default_value = False
    #Socket_2
    random__normal__013.inputs[1].default_value = 0.0
    #Socket_3
    random__normal__013.inputs[2].default_value = 0.055000003427267075
    #Socket_5
    random__normal__013.inputs[4].default_value = 18

    #node Random (Normal).014
    random__normal__014 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__014.name = "Random (Normal).014"
    random__normal__014.node_tree = random__normal_
    #Socket_1
    random__normal__014.inputs[0].default_value = True
    #Socket_2
    random__normal__014.inputs[1].default_value = 0.5
    #Socket_3
    random__normal__014.inputs[2].default_value = 0.25
    #Socket_5
    random__normal__014.inputs[4].default_value = 19

    #node Random (Normal).015
    random__normal__015 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__015.name = "Random (Normal).015"
    random__normal__015.node_tree = random__normal_
    #Socket_1
    random__normal__015.inputs[0].default_value = True
    #Socket_2
    random__normal__015.inputs[1].default_value = 0.0
    #Socket_3
    random__normal__015.inputs[2].default_value = 0.009999999776482582
    #Socket_5
    random__normal__015.inputs[4].default_value = 20

    #node Random (Uniform).004
    random__uniform__004 = random_scoop.nodes.new("GeometryNodeGroup")
    random__uniform__004.name = "Random (Uniform).004"
    random__uniform__004.node_tree = random__uniform_
    #Socket_1
    random__uniform__004.inputs[0].default_value = 0.0
    #Socket_2
    random__uniform__004.inputs[1].default_value = 1.0
    #Socket_4
    random__uniform__004.inputs[3].default_value = 17

    #node Compare
    compare_1 = random_scoop.nodes.new("FunctionNodeCompare")
    compare_1.name = "Compare"
    compare_1.data_type = 'FLOAT'
    compare_1.mode = 'ELEMENT'
    compare_1.operation = 'GREATER_THAN'
    #B
    compare_1.inputs[1].default_value = 0.5

    #node Random (Normal).016
    random__normal__016 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__016.name = "Random (Normal).016"
    random__normal__016.node_tree = random__normal_
    #Socket_1
    random__normal__016.inputs[0].default_value = True
    #Socket_2
    random__normal__016.inputs[1].default_value = 0.019999999552965164
    #Socket_3
    random__normal__016.inputs[2].default_value = 0.009999999776482582
    #Socket_5
    random__normal__016.inputs[4].default_value = 22

    #node Random (Uniform).005
    random__uniform__005 = random_scoop.nodes.new("GeometryNodeGroup")
    random__uniform__005.name = "Random (Uniform).005"
    random__uniform__005.node_tree = random__uniform_
    #Socket_1
    random__uniform__005.inputs[0].default_value = 0.0
    #Socket_2
    random__uniform__005.inputs[1].default_value = 1.0
    #Socket_4
    random__uniform__005.inputs[3].default_value = 21

    #node Compare.001
    compare_001_3 = random_scoop.nodes.new("FunctionNodeCompare")
    compare_001_3.name = "Compare.001"
    compare_001_3.data_type = 'FLOAT'
    compare_001_3.mode = 'ELEMENT'
    compare_001_3.operation = 'GREATER_THAN'
    #B
    compare_001_3.inputs[1].default_value = 0.75

    #node Math.003
    math_003_4 = random_scoop.nodes.new("ShaderNodeMath")
    math_003_4.name = "Math.003"
    math_003_4.operation = 'MULTIPLY'
    math_003_4.use_clamp = False

    #node Random (Normal).017
    random__normal__017 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__017.name = "Random (Normal).017"
    random__normal__017.node_tree = random__normal_
    #Socket_1
    random__normal__017.inputs[0].default_value = False
    #Socket_2
    random__normal__017.inputs[1].default_value = -0.25
    #Socket_3
    random__normal__017.inputs[2].default_value = 0.10000000149011612
    #Socket_5
    random__normal__017.inputs[4].default_value = 23

    #node Random (Normal).018
    random__normal__018 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__018.name = "Random (Normal).018"
    random__normal__018.node_tree = random__normal_
    #Socket_1
    random__normal__018.inputs[0].default_value = True
    #Socket_2
    random__normal__018.inputs[1].default_value = 0.6000000238418579
    #Socket_3
    random__normal__018.inputs[2].default_value = 0.20000000298023224
    #Socket_5
    random__normal__018.inputs[4].default_value = 24

    #node Random (Uniform).006
    random__uniform__006 = random_scoop.nodes.new("GeometryNodeGroup")
    random__uniform__006.name = "Random (Uniform).006"
    random__uniform__006.node_tree = random__uniform_
    #Socket_1
    random__uniform__006.inputs[0].default_value = 0.0
    #Socket_2
    random__uniform__006.inputs[1].default_value = 1.0
    #Socket_4
    random__uniform__006.inputs[3].default_value = 25

    #node Compare.002
    compare_002_1 = random_scoop.nodes.new("FunctionNodeCompare")
    compare_002_1.name = "Compare.002"
    compare_002_1.data_type = 'FLOAT'
    compare_002_1.mode = 'ELEMENT'
    compare_002_1.operation = 'GREATER_THAN'
    #B
    compare_002_1.inputs[1].default_value = 0.8999999761581421

    #node Random (Normal).019
    random__normal__019 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__019.name = "Random (Normal).019"
    random__normal__019.node_tree = random__normal_
    #Socket_1
    random__normal__019.inputs[0].default_value = True
    #Socket_2
    random__normal__019.inputs[1].default_value = 6.0
    #Socket_3
    random__normal__019.inputs[2].default_value = 2.0
    #Socket_5
    random__normal__019.inputs[4].default_value = 26

    #node Math.004
    math_004_4 = random_scoop.nodes.new("ShaderNodeMath")
    math_004_4.name = "Math.004"
    math_004_4.operation = 'MULTIPLY'
    math_004_4.use_clamp = False

    #node Math.005
    math_005_3 = random_scoop.nodes.new("ShaderNodeMath")
    math_005_3.name = "Math.005"
    math_005_3.operation = 'ADD'
    math_005_3.use_clamp = False
    #Value_001
    math_005_3.inputs[1].default_value = 5.0

    #node Random (Normal).020
    random__normal__020 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__020.name = "Random (Normal).020"
    random__normal__020.node_tree = random__normal_
    #Socket_1
    random__normal__020.inputs[0].default_value = True
    #Socket_2
    random__normal__020.inputs[1].default_value = 0.012000000104308128
    #Socket_3
    random__normal__020.inputs[2].default_value = 0.0020000000949949026
    #Socket_5
    random__normal__020.inputs[4].default_value = 27

    #node Combine XYZ.002
    combine_xyz_002_1 = random_scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002_1.name = "Combine XYZ.002"

    #node Random (Normal).021
    random__normal__021 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__021.name = "Random (Normal).021"
    random__normal__021.node_tree = random__normal_
    #Socket_1
    random__normal__021.inputs[0].default_value = True
    #Socket_2
    random__normal__021.inputs[1].default_value = 0.004999999888241291
    #Socket_3
    random__normal__021.inputs[2].default_value = 0.0010000000474974513
    #Socket_5
    random__normal__021.inputs[4].default_value = 28

    #node Random (Normal).022
    random__normal__022 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__022.name = "Random (Normal).022"
    random__normal__022.node_tree = random__normal_
    #Socket_1
    random__normal__022.inputs[0].default_value = True
    #Socket_2
    random__normal__022.inputs[1].default_value = 0.0020000000949949026
    #Socket_3
    random__normal__022.inputs[2].default_value = 0.0005000000237487257
    #Socket_5
    random__normal__022.inputs[4].default_value = 29

    #node Random (Uniform).007
    random__uniform__007 = random_scoop.nodes.new("GeometryNodeGroup")
    random__uniform__007.name = "Random (Uniform).007"
    random__uniform__007.node_tree = random__uniform_
    #Socket_1
    random__uniform__007.inputs[0].default_value = 2.0
    #Socket_2
    random__uniform__007.inputs[1].default_value = 2.5999999046325684
    #Socket_4
    random__uniform__007.inputs[3].default_value = 30

    #node Random (Uniform).008
    random__uniform__008 = random_scoop.nodes.new("GeometryNodeGroup")
    random__uniform__008.name = "Random (Uniform).008"
    random__uniform__008.node_tree = random__uniform_
    #Socket_1
    random__uniform__008.inputs[0].default_value = 2.0
    #Socket_2
    random__uniform__008.inputs[1].default_value = 2.5999999046325684
    #Socket_4
    random__uniform__008.inputs[3].default_value = 31

    #node Random (Uniform).009
    random__uniform__009 = random_scoop.nodes.new("GeometryNodeGroup")
    random__uniform__009.name = "Random (Uniform).009"
    random__uniform__009.node_tree = random__uniform_
    #Socket_1
    random__uniform__009.inputs[0].default_value = 2.0
    #Socket_2
    random__uniform__009.inputs[1].default_value = 2.5999999046325684
    #Socket_4
    random__uniform__009.inputs[3].default_value = 32

    #node Combine XYZ.003
    combine_xyz_003_3 = random_scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003_3.name = "Combine XYZ.003"

    #node Random (Normal).023
    random__normal__023 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__023.name = "Random (Normal).023"
    random__normal__023.node_tree = random__normal_
    #Socket_1
    random__normal__023.inputs[0].default_value = True
    #Socket_2
    random__normal__023.inputs[1].default_value = 0.0024999999441206455
    #Socket_3
    random__normal__023.inputs[2].default_value = 0.0024999999441206455
    #Socket_5
    random__normal__023.inputs[4].default_value = 33

    #node Random (Normal).024
    random__normal__024 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__024.name = "Random (Normal).024"
    random__normal__024.node_tree = random__normal_
    #Socket_1
    random__normal__024.inputs[0].default_value = True
    #Socket_2
    random__normal__024.inputs[1].default_value = 2.0
    #Socket_3
    random__normal__024.inputs[2].default_value = 0.10000000149011612
    #Socket_5
    random__normal__024.inputs[4].default_value = 34

    #node Random (Normal).025
    random__normal__025 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__025.name = "Random (Normal).025"
    random__normal__025.node_tree = random__normal_
    #Socket_1
    random__normal__025.inputs[0].default_value = True
    #Socket_2
    random__normal__025.inputs[1].default_value = 0.10000000149011612
    #Socket_3
    random__normal__025.inputs[2].default_value = 0.20000000298023224
    #Socket_5
    random__normal__025.inputs[4].default_value = 35

    #node Random (Normal).026
    random__normal__026 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__026.name = "Random (Normal).026"
    random__normal__026.node_tree = random__normal_
    #Socket_1
    random__normal__026.inputs[0].default_value = True
    #Socket_2
    random__normal__026.inputs[1].default_value = 0.05000000074505806
    #Socket_3
    random__normal__026.inputs[2].default_value = 0.10000000149011612
    #Socket_5
    random__normal__026.inputs[4].default_value = 36

    #node Random (Normal).027
    random__normal__027 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__027.name = "Random (Normal).027"
    random__normal__027.node_tree = random__normal_
    #Socket_1
    random__normal__027.inputs[0].default_value = False
    #Socket_2
    random__normal__027.inputs[1].default_value = 0.0
    #Socket_3
    random__normal__027.inputs[2].default_value = 0.02500000037252903
    #Socket_5
    random__normal__027.inputs[4].default_value = 37

    #node Combine XYZ.004
    combine_xyz_004_1 = random_scoop.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004_1.name = "Combine XYZ.004"
    combine_xyz_004_1.inputs[1].hide = True
    #Y
    combine_xyz_004_1.inputs[1].default_value = 0.0

    #node Random (Normal).029
    random__normal__029 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__029.name = "Random (Normal).029"
    random__normal__029.node_tree = random__normal_
    #Socket_1
    random__normal__029.inputs[0].default_value = True
    #Socket_2
    random__normal__029.inputs[1].default_value = 0.014999999664723873
    #Socket_3
    random__normal__029.inputs[2].default_value = 0.004999999888241291
    #Socket_5
    random__normal__029.inputs[4].default_value = 38

    #node Random (Normal).028
    random__normal__028 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__028.name = "Random (Normal).028"
    random__normal__028.node_tree = random__normal_
    #Socket_1
    random__normal__028.inputs[0].default_value = False
    #Socket_2
    random__normal__028.inputs[1].default_value = 0.0
    #Socket_3
    random__normal__028.inputs[2].default_value = 0.06981316953897476
    #Socket_5
    random__normal__028.inputs[4].default_value = 39

    #node Math.006
    math_006_4 = random_scoop.nodes.new("ShaderNodeMath")
    math_006_4.name = "Math.006"
    math_006_4.operation = 'ADD'
    math_006_4.use_clamp = False
    #Value_001
    math_006_4.inputs[1].default_value = 0.006000000052154064

    #node Math.007
    math_007_4 = random_scoop.nodes.new("ShaderNodeMath")
    math_007_4.name = "Math.007"
    math_007_4.operation = 'ADD'
    math_007_4.use_clamp = False
    #Value_001
    math_007_4.inputs[1].default_value = 0.003000000026077032

    #node Math.008
    math_008_3 = random_scoop.nodes.new("ShaderNodeMath")
    math_008_3.name = "Math.008"
    math_008_3.operation = 'ADD'
    math_008_3.use_clamp = False
    #Value_001
    math_008_3.inputs[1].default_value = 0.004000000189989805

    #node Random (Normal).030
    random__normal__030 = random_scoop.nodes.new("GeometryNodeGroup")
    random__normal__030.name = "Random (Normal).030"
    random__normal__030.node_tree = random__normal_
    #Socket_1
    random__normal__030.inputs[0].default_value = True
    #Socket_2
    random__normal__030.inputs[1].default_value = 1.0
    #Socket_3
    random__normal__030.inputs[2].default_value = 0.5
    #Socket_5
    random__normal__030.inputs[4].default_value = 40

    #node Math.009
    math_009_3 = random_scoop.nodes.new("ShaderNodeMath")
    math_009_3.name = "Math.009"
    math_009_3.operation = 'ADD'
    math_009_3.use_clamp = False
    #Value_001
    math_009_3.inputs[1].default_value = 1.5





    #Set locations
    group_output_5.location = (200.0, 0.0)
    scoop_1.location = (-793.0894165039062, 445.06298828125)
    random__normal__1.location = (-4789.4169921875, 2932.31884765625)
    combine_xyz_1.location = (-4584.435546875, 2763.27685546875)
    integer_math_1.location = (-5235.31884765625, 548.4847412109375)
    group_input_5.location = (-5678.7822265625, 529.905517578125)
    integer_1.location = (-5425.31884765625, 460.6773681640625)
    reroute_001.location = (-5075.3193359375, 513.4847412109375)
    random__normal__001.location = (-4789.4169921875, 2733.31884765625)
    random__normal__002.location = (-4789.4169921875, 2534.319091796875)
    combine_xyz_001.location = (-4010.3173828125, 2385.664794921875)
    random__uniform__001.location = (-4583.583984375, 2517.183349609375)
    random__uniform__002.location = (-4583.583984375, 2340.183349609375)
    random__normal__003.location = (-4583.583984375, 2163.183349609375)
    math_4.location = (-4393.33349609375, 2233.90234375)
    random__normal__004.location = (-4199.7314453125, 2160.6162109375)
    clamp.location = (-3629.7314453125, 2140.1162109375)
    math_001_4.location = (-3819.7314453125, 2142.6162109375)
    float_to_integer_1.location = (-4204.5537109375, 2296.48681640625)
    math_002_4.location = (-4009.7314453125, 2142.6162109375)
    random__uniform__003.location = (-4008.8271484375, 1971.397216796875)
    random__normal__005.location = (-3819.568359375, 1928.38427734375)
    random__normal__006.location = (-3633.74951171875, 1879.19140625)
    random__normal__007.location = (-4002.60546875, 1737.871337890625)
    random__normal__008.location = (-3824.33642578125, 1683.771728515625)
    random__normal__009.location = (-3655.91162109375, 1619.850830078125)
    random__normal__010.location = (-4002.60546875, 1509.00732421875)
    random__normal__011.location = (-3824.33642578125, 1454.907470703125)
    random__normal__012.location = (-3655.91162109375, 1390.9866943359375)
    random__normal__013.location = (-4021.14599609375, 1108.4169921875)
    random__normal__014.location = (-3842.87744140625, 1054.317138671875)
    random__normal__015.location = (-3670.712646484375, 1003.12158203125)
    random__uniform__004.location = (-4022.66943359375, 1299.234130859375)
    compare_1.location = (-3828.17529296875, 1247.76025390625)
    random__normal__016.location = (-3288.9384765625, 756.2977294921875)
    random__uniform__005.location = (-3467.97216796875, 942.53369140625)
    compare_001_3.location = (-3286.4111328125, 915.3310546875)
    math_003_4.location = (-3088.79150390625, 847.0888671875)
    random__normal__017.location = (-3084.86962890625, 680.6522216796875)
    random__normal__018.location = (-2890.24853515625, 623.91796875)
    random__uniform__006.location = (-4024.19580078125, 569.4978637695312)
    compare_002_1.location = (-3844.67724609375, 546.3841552734375)
    random__normal__019.location = (-4029.00146484375, 393.86444091796875)
    math_004_4.location = (-3647.71630859375, 496.38531494140625)
    math_005_3.location = (-3846.458984375, 382.32525634765625)
    random__normal__020.location = (-3494.876708984375, 433.5595397949219)
    combine_xyz_002_1.location = (-3029.281494140625, 262.30706787109375)
    random__normal__021.location = (-3494.876708984375, 234.55953979492188)
    random__normal__022.location = (-3494.876708984375, 35.5596923828125)
    random__uniform__007.location = (-2733.7529296875, 365.63006591796875)
    random__uniform__008.location = (-2733.7529296875, 188.63003540039062)
    random__uniform__009.location = (-2737.46484375, 11.25299072265625)
    combine_xyz_003_3.location = (-2306.78857421875, 265.9139099121094)
    random__normal__023.location = (-2492.9873046875, 117.8866958618164)
    random__normal__024.location = (-2157.05908203125, 33.05975341796875)
    random__normal__025.location = (-1979.1951904296875, -40.56103515625)
    random__normal__026.location = (-1793.3763427734375, -89.75390625)
    random__normal__027.location = (-1573.3060302734375, -215.44781494140625)
    combine_xyz_004_1.location = (-1360.15283203125, -322.1275329589844)
    random__normal__029.location = (-1576.370361328125, -419.20452880859375)
    random__normal__028.location = (-1336.115234375, -436.5528564453125)
    math_006_4.location = (-3293.760009765625, 401.6719970703125)
    math_007_4.location = (-3291.137939453125, 240.71885681152344)
    math_008_3.location = (-2324.608642578125, 95.25886535644531)
    random__normal__030.location = (-1344.379150390625, -661.217041015625)
    math_009_3.location = (-1139.5489501953125, -595.6012573242188)

    #Set dimensions
    group_output_5.width, group_output_5.height = 140.0, 100.0
    scoop_1.width, scoop_1.height = 322.31414794921875, 100.0
    random__normal__1.width, random__normal__1.height = 140.0, 100.0
    combine_xyz_1.width, combine_xyz_1.height = 140.0, 100.0
    integer_math_1.width, integer_math_1.height = 140.0, 100.0
    group_input_5.width, group_input_5.height = 140.0, 100.0
    integer_1.width, integer_1.height = 140.0, 100.0
    reroute_001.width, reroute_001.height = 10.0, 100.0
    random__normal__001.width, random__normal__001.height = 140.0, 100.0
    random__normal__002.width, random__normal__002.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    random__uniform__001.width, random__uniform__001.height = 140.0, 100.0
    random__uniform__002.width, random__uniform__002.height = 140.0, 100.0
    random__normal__003.width, random__normal__003.height = 140.0, 100.0
    math_4.width, math_4.height = 140.0, 100.0
    random__normal__004.width, random__normal__004.height = 140.0, 100.0
    clamp.width, clamp.height = 140.0, 100.0
    math_001_4.width, math_001_4.height = 140.0, 100.0
    float_to_integer_1.width, float_to_integer_1.height = 140.0, 100.0
    math_002_4.width, math_002_4.height = 140.0, 100.0
    random__uniform__003.width, random__uniform__003.height = 140.0, 100.0
    random__normal__005.width, random__normal__005.height = 140.0, 100.0
    random__normal__006.width, random__normal__006.height = 140.0, 100.0
    random__normal__007.width, random__normal__007.height = 140.0, 100.0
    random__normal__008.width, random__normal__008.height = 140.0, 100.0
    random__normal__009.width, random__normal__009.height = 140.0, 100.0
    random__normal__010.width, random__normal__010.height = 140.0, 100.0
    random__normal__011.width, random__normal__011.height = 140.0, 100.0
    random__normal__012.width, random__normal__012.height = 140.0, 100.0
    random__normal__013.width, random__normal__013.height = 140.0, 100.0
    random__normal__014.width, random__normal__014.height = 140.0, 100.0
    random__normal__015.width, random__normal__015.height = 140.0, 100.0
    random__uniform__004.width, random__uniform__004.height = 140.0, 100.0
    compare_1.width, compare_1.height = 140.0, 100.0
    random__normal__016.width, random__normal__016.height = 140.0, 100.0
    random__uniform__005.width, random__uniform__005.height = 140.0, 100.0
    compare_001_3.width, compare_001_3.height = 140.0, 100.0
    math_003_4.width, math_003_4.height = 140.0, 100.0
    random__normal__017.width, random__normal__017.height = 140.0, 100.0
    random__normal__018.width, random__normal__018.height = 140.0, 100.0
    random__uniform__006.width, random__uniform__006.height = 140.0, 100.0
    compare_002_1.width, compare_002_1.height = 140.0, 100.0
    random__normal__019.width, random__normal__019.height = 140.0, 100.0
    math_004_4.width, math_004_4.height = 140.0, 100.0
    math_005_3.width, math_005_3.height = 140.0, 100.0
    random__normal__020.width, random__normal__020.height = 140.0, 100.0
    combine_xyz_002_1.width, combine_xyz_002_1.height = 140.0, 100.0
    random__normal__021.width, random__normal__021.height = 140.0, 100.0
    random__normal__022.width, random__normal__022.height = 140.0, 100.0
    random__uniform__007.width, random__uniform__007.height = 140.0, 100.0
    random__uniform__008.width, random__uniform__008.height = 140.0, 100.0
    random__uniform__009.width, random__uniform__009.height = 140.0, 100.0
    combine_xyz_003_3.width, combine_xyz_003_3.height = 140.0, 100.0
    random__normal__023.width, random__normal__023.height = 140.0, 100.0
    random__normal__024.width, random__normal__024.height = 140.0, 100.0
    random__normal__025.width, random__normal__025.height = 140.0, 100.0
    random__normal__026.width, random__normal__026.height = 140.0, 100.0
    random__normal__027.width, random__normal__027.height = 140.0, 100.0
    combine_xyz_004_1.width, combine_xyz_004_1.height = 140.0, 100.0
    random__normal__029.width, random__normal__029.height = 140.0, 100.0
    random__normal__028.width, random__normal__028.height = 140.0, 100.0
    math_006_4.width, math_006_4.height = 140.0, 100.0
    math_007_4.width, math_007_4.height = 140.0, 100.0
    math_008_3.width, math_008_3.height = 140.0, 100.0
    random__normal__030.width, random__normal__030.height = 140.0, 100.0
    math_009_3.width, math_009_3.height = 140.0, 100.0

    #initialize random_scoop links
    #scoop_1.Geometry -> group_output_5.Geometry
    random_scoop.links.new(scoop_1.outputs[0], group_output_5.inputs[0])
    #group_input_5.seed -> integer_math_1.Value
    random_scoop.links.new(group_input_5.outputs[0], integer_math_1.inputs[0])
    #integer_1.Integer -> integer_math_1.Value
    random_scoop.links.new(integer_1.outputs[0], integer_math_1.inputs[1])
    #integer_math_1.Value -> reroute_001.Input
    random_scoop.links.new(integer_math_1.outputs[0], reroute_001.inputs[0])
    #reroute_001.Output -> random__normal__1.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__1.inputs[3])
    #reroute_001.Output -> random__normal__001.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__001.inputs[3])
    #reroute_001.Output -> random__normal__002.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__002.inputs[3])
    #random__normal__002.Value -> combine_xyz_1.Z
    random_scoop.links.new(random__normal__002.outputs[0], combine_xyz_1.inputs[2])
    #random__normal__001.Value -> combine_xyz_1.Y
    random_scoop.links.new(random__normal__001.outputs[0], combine_xyz_1.inputs[1])
    #random__normal__1.Value -> combine_xyz_1.X
    random_scoop.links.new(random__normal__1.outputs[0], combine_xyz_1.inputs[0])
    #combine_xyz_1.Vector -> scoop_1.scale
    random_scoop.links.new(combine_xyz_1.outputs[0], scoop_1.inputs[0])
    #reroute_001.Output -> random__uniform__001.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__uniform__001.inputs[2])
    #random__uniform__001.Value -> combine_xyz_001.X
    random_scoop.links.new(random__uniform__001.outputs[0], combine_xyz_001.inputs[0])
    #reroute_001.Output -> random__uniform__002.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__uniform__002.inputs[2])
    #random__uniform__002.Value -> combine_xyz_001.Y
    random_scoop.links.new(random__uniform__002.outputs[0], combine_xyz_001.inputs[1])
    #reroute_001.Output -> random__normal__003.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__003.inputs[3])
    #random__normal__003.Value -> math_4.Value
    random_scoop.links.new(random__normal__003.outputs[0], math_4.inputs[0])
    #float_to_integer_1.Integer -> combine_xyz_001.Z
    random_scoop.links.new(float_to_integer_1.outputs[0], combine_xyz_001.inputs[2])
    #combine_xyz_001.Vector -> scoop_1.base_vertices
    random_scoop.links.new(combine_xyz_001.outputs[0], scoop_1.inputs[1])
    #reroute_001.Output -> random__normal__004.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__004.inputs[3])
    #random__normal__004.Value -> clamp.Value
    random_scoop.links.new(random__normal__004.outputs[0], clamp.inputs[0])
    #math_4.Value -> float_to_integer_1.Float
    random_scoop.links.new(math_4.outputs[0], float_to_integer_1.inputs[0])
    #math_001_4.Value -> clamp.Min
    random_scoop.links.new(math_001_4.outputs[0], clamp.inputs[1])
    #float_to_integer_1.Integer -> math_002_4.Value
    random_scoop.links.new(float_to_integer_1.outputs[0], math_002_4.inputs[0])
    #math_002_4.Value -> math_001_4.Value
    random_scoop.links.new(math_002_4.outputs[0], math_001_4.inputs[1])
    #clamp.Result -> scoop_1.mouth_open
    random_scoop.links.new(clamp.outputs[0], scoop_1.inputs[2])
    #reroute_001.Output -> random__uniform__003.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__uniform__003.inputs[2])
    #random__uniform__003.Value -> scoop_1.wall_thickness
    random_scoop.links.new(random__uniform__003.outputs[0], scoop_1.inputs[3])
    #group_input_5.subdivisions -> scoop_1.subdivisions
    random_scoop.links.new(group_input_5.outputs[1], scoop_1.inputs[4])
    #reroute_001.Output -> random__normal__005.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__005.inputs[3])
    #random__normal__005.Value -> scoop_1.edge_crease
    random_scoop.links.new(random__normal__005.outputs[0], scoop_1.inputs[5])
    #reroute_001.Output -> random__normal__006.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__006.inputs[3])
    #random__normal__006.Value -> scoop_1.vertex_crease
    random_scoop.links.new(random__normal__006.outputs[0], scoop_1.inputs[6])
    #group_input_5.material -> scoop_1.material
    random_scoop.links.new(group_input_5.outputs[2], scoop_1.inputs[7])
    #reroute_001.Output -> random__normal__007.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__007.inputs[3])
    #random__normal__007.Value -> scoop_1.shape_front_lin
    random_scoop.links.new(random__normal__007.outputs[0], scoop_1.inputs[8])
    #reroute_001.Output -> random__normal__008.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__008.inputs[3])
    #random__normal__008.Value -> scoop_1.shape_front_exp
    random_scoop.links.new(random__normal__008.outputs[0], scoop_1.inputs[9])
    #reroute_001.Output -> random__normal__009.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__009.inputs[3])
    #random__normal__009.Value -> scoop_1.shape_front_offset
    random_scoop.links.new(random__normal__009.outputs[0], scoop_1.inputs[10])
    #reroute_001.Output -> random__normal__010.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__010.inputs[3])
    #reroute_001.Output -> random__normal__011.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__011.inputs[3])
    #reroute_001.Output -> random__normal__012.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__012.inputs[3])
    #random__normal__010.Value -> scoop_1.shape_back_lin
    random_scoop.links.new(random__normal__010.outputs[0], scoop_1.inputs[11])
    #random__normal__011.Value -> scoop_1.shape_back_exp
    random_scoop.links.new(random__normal__011.outputs[0], scoop_1.inputs[12])
    #random__normal__012.Value -> scoop_1.shape_back_offset
    random_scoop.links.new(random__normal__012.outputs[0], scoop_1.inputs[13])
    #reroute_001.Output -> random__normal__013.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__013.inputs[3])
    #reroute_001.Output -> random__normal__014.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__014.inputs[3])
    #reroute_001.Output -> random__normal__015.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__015.inputs[3])
    #random__normal__015.Value -> scoop_1.shape_sides_offset
    random_scoop.links.new(random__normal__015.outputs[0], scoop_1.inputs[17])
    #random__normal__014.Value -> scoop_1.shape_sides_exp
    random_scoop.links.new(random__normal__014.outputs[0], scoop_1.inputs[16])
    #random__normal__013.Value -> scoop_1.shape_sides_lin
    random_scoop.links.new(random__normal__013.outputs[0], scoop_1.inputs[15])
    #reroute_001.Output -> random__uniform__004.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__uniform__004.inputs[2])
    #random__uniform__004.Value -> compare_1.A
    random_scoop.links.new(random__uniform__004.outputs[0], compare_1.inputs[0])
    #compare_1.Result -> scoop_1.shape_sides_dir_out
    random_scoop.links.new(compare_1.outputs[0], scoop_1.inputs[14])
    #reroute_001.Output -> random__normal__016.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__016.inputs[3])
    #reroute_001.Output -> random__uniform__005.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__uniform__005.inputs[2])
    #random__uniform__005.Value -> compare_001_3.A
    random_scoop.links.new(random__uniform__005.outputs[0], compare_001_3.inputs[0])
    #compare_001_3.Result -> math_003_4.Value
    random_scoop.links.new(compare_001_3.outputs[0], math_003_4.inputs[0])
    #random__normal__016.Value -> math_003_4.Value
    random_scoop.links.new(random__normal__016.outputs[0], math_003_4.inputs[1])
    #math_003_4.Value -> scoop_1.lip_len
    random_scoop.links.new(math_003_4.outputs[0], scoop_1.inputs[18])
    #reroute_001.Output -> random__normal__017.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__017.inputs[3])
    #random__normal__017.Value -> scoop_1.lip_dir
    random_scoop.links.new(random__normal__017.outputs[0], scoop_1.inputs[19])
    #reroute_001.Output -> random__normal__018.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__018.inputs[3])
    #random__normal__018.Value -> scoop_1.lip_width
    random_scoop.links.new(random__normal__018.outputs[0], scoop_1.inputs[20])
    #reroute_001.Output -> random__uniform__006.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__uniform__006.inputs[2])
    #random__uniform__006.Value -> compare_002_1.A
    random_scoop.links.new(random__uniform__006.outputs[0], compare_002_1.inputs[0])
    #reroute_001.Output -> random__normal__019.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__019.inputs[3])
    #compare_002_1.Result -> math_004_4.Value
    random_scoop.links.new(compare_002_1.outputs[0], math_004_4.inputs[0])
    #math_005_3.Value -> math_004_4.Value
    random_scoop.links.new(math_005_3.outputs[0], math_004_4.inputs[1])
    #math_004_4.Value -> scoop_1.tooth_count
    random_scoop.links.new(math_004_4.outputs[0], scoop_1.inputs[21])
    #random__normal__019.Value -> math_005_3.Value
    random_scoop.links.new(random__normal__019.outputs[0], math_005_3.inputs[0])
    #reroute_001.Output -> random__normal__020.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__020.inputs[3])
    #reroute_001.Output -> random__normal__021.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__021.inputs[3])
    #reroute_001.Output -> random__normal__022.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__022.inputs[3])
    #random__normal__022.Value -> combine_xyz_002_1.Z
    random_scoop.links.new(random__normal__022.outputs[0], combine_xyz_002_1.inputs[2])
    #math_007_4.Value -> combine_xyz_002_1.Y
    random_scoop.links.new(math_007_4.outputs[0], combine_xyz_002_1.inputs[1])
    #math_006_4.Value -> combine_xyz_002_1.X
    random_scoop.links.new(math_006_4.outputs[0], combine_xyz_002_1.inputs[0])
    #combine_xyz_002_1.Vector -> scoop_1.tooth_scale
    random_scoop.links.new(combine_xyz_002_1.outputs[0], scoop_1.inputs[22])
    #reroute_001.Output -> random__uniform__007.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__uniform__007.inputs[2])
    #reroute_001.Output -> random__uniform__008.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__uniform__008.inputs[2])
    #reroute_001.Output -> random__uniform__009.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__uniform__009.inputs[2])
    #random__uniform__009.Value -> combine_xyz_003_3.Z
    random_scoop.links.new(random__uniform__009.outputs[0], combine_xyz_003_3.inputs[2])
    #random__uniform__008.Value -> combine_xyz_003_3.Y
    random_scoop.links.new(random__uniform__008.outputs[0], combine_xyz_003_3.inputs[1])
    #random__uniform__007.Value -> combine_xyz_003_3.X
    random_scoop.links.new(random__uniform__007.outputs[0], combine_xyz_003_3.inputs[0])
    #combine_xyz_003_3.Vector -> scoop_1.tooth_base_vertices
    random_scoop.links.new(combine_xyz_003_3.outputs[0], scoop_1.inputs[24])
    #reroute_001.Output -> random__normal__023.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__023.inputs[3])
    #math_008_3.Value -> scoop_1.tooth_inset_dist
    random_scoop.links.new(math_008_3.outputs[0], scoop_1.inputs[25])
    #reroute_001.Output -> random__normal__024.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__024.inputs[3])
    #random__normal__024.Value -> scoop_1.tooth_validity
    random_scoop.links.new(random__normal__024.outputs[0], scoop_1.inputs[26])
    #group_input_5.tooth_subdivisions_offset -> scoop_1.tooth_subdivisions_offset
    random_scoop.links.new(group_input_5.outputs[3], scoop_1.inputs[27])
    #reroute_001.Output -> random__normal__025.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__025.inputs[3])
    #reroute_001.Output -> random__normal__026.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__026.inputs[3])
    #random__normal__025.Value -> scoop_1.tooth_edge_crease
    random_scoop.links.new(random__normal__025.outputs[0], scoop_1.inputs[28])
    #group_input_5.mount_radius -> scoop_1.mount_radius
    random_scoop.links.new(group_input_5.outputs[4], scoop_1.inputs[30])
    #group_input_5.mount_vertices_ratio -> scoop_1.mount_vertices_ratio
    random_scoop.links.new(group_input_5.outputs[5], scoop_1.inputs[33])
    #reroute_001.Output -> random__normal__027.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__027.inputs[3])
    #reroute_001.Output -> random__normal__029.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__029.inputs[3])
    #random__normal__029.Value -> combine_xyz_004_1.Z
    random_scoop.links.new(random__normal__029.outputs[0], combine_xyz_004_1.inputs[2])
    #random__normal__027.Value -> combine_xyz_004_1.X
    random_scoop.links.new(random__normal__027.outputs[0], combine_xyz_004_1.inputs[0])
    #combine_xyz_004_1.Vector -> scoop_1.mount_offset_lin
    random_scoop.links.new(combine_xyz_004_1.outputs[0], scoop_1.inputs[31])
    #reroute_001.Output -> random__normal__028.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__028.inputs[3])
    #random__normal__028.Value -> scoop_1.mount_offset_ang
    random_scoop.links.new(random__normal__028.outputs[0], scoop_1.inputs[32])
    #random__normal__026.Value -> scoop_1.tooth_vertex_crease
    random_scoop.links.new(random__normal__026.outputs[0], scoop_1.inputs[29])
    #random__normal__020.Value -> math_006_4.Value
    random_scoop.links.new(random__normal__020.outputs[0], math_006_4.inputs[0])
    #random__normal__021.Value -> math_007_4.Value
    random_scoop.links.new(random__normal__021.outputs[0], math_007_4.inputs[0])
    #random__normal__023.Value -> math_008_3.Value
    random_scoop.links.new(random__normal__023.outputs[0], math_008_3.inputs[0])
    #reroute_001.Output -> random__normal__030.Seed
    random_scoop.links.new(reroute_001.outputs[0], random__normal__030.inputs[3])
    #random__normal__030.Value -> math_009_3.Value
    random_scoop.links.new(random__normal__030.outputs[0], math_009_3.inputs[0])
    #math_009_3.Value -> scoop_1.tooth_taper_scale
    random_scoop.links.new(math_009_3.outputs[0], scoop_1.inputs[23])
    return random_scoop

random_scoop = random_scoop_node_group()


import bpy

def cubesat_node_group():
    cubesat = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Cubesat")
    cubesat.color_tag = 'GEOMETRY'
    cubesat.default_group_node_width = 140
    cubesat.is_modifier = True
    geometry_socket = cubesat.interface.new_socket(name = "geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    seed_socket = cubesat.interface.new_socket(name = "seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket.default_value = 0
    seed_socket.min_value = 0
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.force_non_field = True
    rail_size_socket = cubesat.interface.new_socket(name = "rail_size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    rail_size_socket.default_value = 0.004999999888241291
    rail_size_socket.min_value = 0.0
    rail_size_socket.max_value = 3.4028234663852886e+38
    rail_size_socket.subtype = 'DISTANCE'
    rail_size_socket.attribute_domain = 'POINT'
    rail_size_socket.force_non_field = True
    rail_end_length_socket = cubesat.interface.new_socket(name = "rail_end_length", in_out='INPUT', socket_type = 'NodeSocketFloat')
    rail_end_length_socket.default_value = 0.009999999776482582
    rail_end_length_socket.min_value = 0.0
    rail_end_length_socket.max_value = 3.4028234663852886e+38
    rail_end_length_socket.subtype = 'DISTANCE'
    rail_end_length_socket.attribute_domain = 'POINT'
    rail_end_length_socket.force_non_field = True
    border_size_socket = cubesat.interface.new_socket(name = "border_size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    border_size_socket.default_value = 0.0020000000949949026
    border_size_socket.min_value = 0.0
    border_size_socket.max_value = 3.4028234663852886e+38
    border_size_socket.subtype = 'DISTANCE'
    border_size_socket.attribute_domain = 'POINT'
    cells_mat1_socket = cubesat.interface.new_socket(name = "cells_mat1", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    cells_mat1_socket.attribute_domain = 'POINT'
    cells_mat2_socket = cubesat.interface.new_socket(name = "cells_mat2", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    cells_mat2_socket.attribute_domain = 'POINT'
    cells_mat3_socket = cubesat.interface.new_socket(name = "cells_mat3", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    cells_mat3_socket.attribute_domain = 'POINT'
    frame_mat1_socket = cubesat.interface.new_socket(name = "frame_mat1", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    frame_mat1_socket.attribute_domain = 'POINT'
    frame_mat2_socket = cubesat.interface.new_socket(name = "frame_mat2", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    frame_mat2_socket.attribute_domain = 'POINT'
    frame_mat3_socket = cubesat.interface.new_socket(name = "frame_mat3", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    frame_mat3_socket.attribute_domain = 'POINT'
    frame_mat4_socket = cubesat.interface.new_socket(name = "frame_mat4", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    frame_mat4_socket.attribute_domain = 'POINT'
    group_input = cubesat.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_output = cubesat.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    set_material = cubesat.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.inputs[1].default_value = True
    integer_001 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_001.name = "Integer.001"
    integer_001.integer = 0
    set_material_002 = cubesat.nodes.new("GeometryNodeSetMaterial")
    set_material_002.name = "Set Material.002"
    set_material_002.inputs[1].default_value = True
    integer_math = cubesat.nodes.new("FunctionNodeIntegerMath")
    integer_math.name = "Integer Math"
    integer_math.operation = 'ADD'
    reroute_006 = cubesat.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.mute = True
    reroute_006.socket_idname = "NodeSocketInt"
    cube = cubesat.nodes.new("GeometryNodeMeshCube")
    cube.name = "Cube"
    cube.inputs[1].default_value = 2
    cube.inputs[2].default_value = 2
    cube.inputs[3].default_value = 2
    random_value = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value.name = "Random Value"
    random_value.data_type = 'FLOAT'
    random_value.inputs[2].default_value = 0.0
    random_value.inputs[3].default_value = 1.0
    index_switch = cubesat.nodes.new("GeometryNodeIndexSwitch")
    index_switch.name = "Index Switch"
    index_switch.data_type = 'VECTOR'
    index_switch.index_switch_items.clear()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    index_switch.index_switch_items.new()
    vector = cubesat.nodes.new("FunctionNodeInputVector")
    vector.name = "Vector"
    vector.vector = (0.10000000149011612, 0.10000000149011612, 0.10000000149011612)
    vector_001 = cubesat.nodes.new("FunctionNodeInputVector")
    vector_001.name = "Vector.001"
    vector_001.vector = (0.10000000149011612, 0.10000000149011612, 0.15000000596046448)
    vector_002 = cubesat.nodes.new("FunctionNodeInputVector")
    vector_002.name = "Vector.002"
    vector_002.vector = (0.10000000149011612, 0.10000000149011612, 0.20000000298023224)
    vector_003 = cubesat.nodes.new("FunctionNodeInputVector")
    vector_003.name = "Vector.003"
    vector_003.vector = (0.10000000149011612, 0.10000000149011612, 0.30000001192092896)
    vector_004 = cubesat.nodes.new("FunctionNodeInputVector")
    vector_004.name = "Vector.004"
    vector_004.vector = (0.20000000298023224, 0.10000000149011612, 0.30000001192092896)
    vector_005 = cubesat.nodes.new("FunctionNodeInputVector")
    vector_005.name = "Vector.005"
    vector_005.vector = (0.20000000298023224, 0.20000000298023224, 0.30000001192092896)
    integer = cubesat.nodes.new("FunctionNodeInputInt")
    integer.name = "Integer"
    integer.integer = 0
    frame = cubesat.nodes.new("NodeFrame")
    frame.name = "Frame"
    float_curve = cubesat.nodes.new("ShaderNodeFloatCurve")
    float_curve.name = "Float Curve"
    float_curve.mapping.extend = 'EXTRAPOLATED'
    float_curve.mapping.tone = 'STANDARD'
    float_curve.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve.mapping.clip_min_x = 0.0
    float_curve.mapping.clip_min_y = 0.0
    float_curve.mapping.clip_max_x = 1.0
    float_curve.mapping.clip_max_y = 1.0
    float_curve.mapping.use_clip = True
    float_curve_curve_0 = float_curve.mapping.curves[0]
    float_curve_curve_0_point_0 = float_curve_curve_0.points[0]
    float_curve_curve_0_point_0.location = (0.0, 0.0)
    float_curve_curve_0_point_0.handle_type = 'AUTO'
    float_curve_curve_0_point_1 = float_curve_curve_0.points[1]
    float_curve_curve_0_point_1.location = (0.75, 0.25)
    float_curve_curve_0_point_1.handle_type = 'AUTO_CLAMPED'
    float_curve_curve_0_point_2 = float_curve_curve_0.points.new(1.0, 1.0)
    float_curve_curve_0_point_2.handle_type = 'AUTO'
    float_curve.mapping.update()
    float_curve.inputs[0].default_value = 1.0
    float_to_integer = cubesat.nodes.new("FunctionNodeFloatToInt")
    float_to_integer.name = "Float to Integer"
    float_to_integer.rounding_mode = 'ROUND'
    math = cubesat.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'MULTIPLY'
    math.use_clamp = False
    integer_002 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_002.name = "Integer.002"
    integer_002.integer = 5
    transform_geometry = cubesat.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mute = True
    transform_geometry.mode = 'COMPONENTS'
    transform_geometry.inputs[1].hide = True
    transform_geometry.inputs[3].hide = True
    transform_geometry.inputs[4].hide = True
    transform_geometry.inputs[1].default_value = (0.0, 0.0, 0.0)
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
    vector_math = cubesat.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.mute = True
    vector_math.operation = 'SNAP'
    vector_math.inputs[1].default_value = (1.5707963705062866, 1.5707963705062866, 1.5707963705062866)
    random_value_001 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.mute = True
    random_value_001.data_type = 'FLOAT_VECTOR'
    random_value_001.inputs[0].default_value = (-3.1415927410125732, -3.1415927410125732, -3.1415927410125732)
    random_value_001.inputs[1].default_value = (3.1415927410125732, 3.1415927410125732, 3.1415927410125732)
    integer_003 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_003.name = "Integer.003"
    integer_003.mute = True
    integer_003.integer = 1457
    reroute_001 = cubesat.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketVector"
    frame_001 = cubesat.nodes.new("NodeFrame")
    frame_001.name = "Frame.001"
    reroute_002 = cubesat.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.mute = True
    reroute_002.socket_idname = "NodeSocketGeometry"
    reroute_003 = cubesat.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.mute = True
    reroute_003.socket_idname = "NodeSocketGeometry"
    reroute_004 = cubesat.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.socket_idname = "NodeSocketInt"
    instance_on_points = cubesat.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.inputs[1].default_value = True
    instance_on_points.inputs[3].default_value = False
    instance_on_points.inputs[4].default_value = 0
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)
    join_geometry = cubesat.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    separate_xyz = cubesat.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    cube_001 = cubesat.nodes.new("GeometryNodeMeshCube")
    cube_001.name = "Cube.001"
    cube_001.inputs[1].default_value = 2
    cube_001.inputs[2].default_value = 2
    cube_001.inputs[3].default_value = 2
    combine_xyz = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    math_002 = cubesat.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'ADD'
    math_002.use_clamp = False
    instance_on_points_001 = cubesat.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    instance_on_points_001.inputs[1].default_value = True
    instance_on_points_001.inputs[3].default_value = False
    instance_on_points_001.inputs[4].default_value = 0
    instance_on_points_001.inputs[5].default_value = (0.0, 0.0, 0.0)
    instance_on_points_001.inputs[6].default_value = (1.0, 1.0, 1.0)
    cube_002 = cubesat.nodes.new("GeometryNodeMeshCube")
    cube_002.name = "Cube.002"
    cube_002.inputs[1].default_value = 2
    cube_002.inputs[2].default_value = 2
    cube_002.inputs[3].default_value = 2
    combine_xyz_001 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    math_003 = cubesat.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'SUBTRACT'
    math_003.use_clamp = False
    instance_on_points_002 = cubesat.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_002.name = "Instance on Points.002"
    instance_on_points_002.inputs[1].default_value = True
    instance_on_points_002.inputs[3].default_value = False
    instance_on_points_002.inputs[4].default_value = 0
    instance_on_points_002.inputs[5].default_value = (0.0, 0.0, 0.0)
    instance_on_points_002.inputs[6].default_value = (1.0, 1.0, 1.0)
    cube_003 = cubesat.nodes.new("GeometryNodeMeshCube")
    cube_003.name = "Cube.003"
    cube_003.inputs[1].default_value = 2
    cube_003.inputs[2].default_value = 2
    cube_003.inputs[3].default_value = 2
    combine_xyz_002 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    math_004 = cubesat.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'SUBTRACT'
    math_004.use_clamp = False
    delete_geometry = cubesat.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'FACE'
    delete_geometry.mode = 'ALL'
    normal = cubesat.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    vector_math_001 = cubesat.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'ABSOLUTE'
    compare_006 = cubesat.nodes.new("FunctionNodeCompare")
    compare_006.name = "Compare.006"
    compare_006.data_type = 'VECTOR'
    compare_006.mode = 'ELEMENT'
    compare_006.operation = 'EQUAL'
    compare_006.inputs[5].default_value = (1.0, 0.0, 0.0)
    compare_006.inputs[12].default_value = 0.0010000000474974513
    delete_geometry_001 = cubesat.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.domain = 'FACE'
    delete_geometry_001.mode = 'ONLY_FACE'
    vector_math_003 = cubesat.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = 'SCALE'
    vector_math_003.inputs[3].default_value = 0.5
    separate_xyz_001 = cubesat.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"
    compare_007 = cubesat.nodes.new("FunctionNodeCompare")
    compare_007.name = "Compare.007"
    compare_007.data_type = 'VECTOR'
    compare_007.mode = 'ELEMENT'
    compare_007.operation = 'EQUAL'
    compare_007.inputs[5].default_value = (0.0, 1.0, 0.0)
    compare_007.inputs[12].default_value = 0.0010000000474974513
    position = cubesat.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    compare = cubesat.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'VECTOR'
    compare.mode = 'ELEMENT'
    compare.operation = 'EQUAL'
    compare.inputs[12].default_value = 0.0010000000474974513
    separate_xyz_002 = cubesat.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002.name = "Separate XYZ.002"
    combine_xyz_003 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"
    combine_xyz_003.inputs[0].hide = True
    combine_xyz_003.inputs[2].hide = True
    combine_xyz_003.inputs[0].default_value = 0.0
    combine_xyz_003.inputs[2].default_value = 0.0
    combine_xyz_004 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004.name = "Combine XYZ.004"
    combine_xyz_004.inputs[0].hide = True
    combine_xyz_004.inputs[2].hide = True
    combine_xyz_004.inputs[0].default_value = 0.0
    combine_xyz_004.inputs[2].default_value = 0.0
    math_001 = cubesat.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'ABSOLUTE'
    math_001.use_clamp = False
    boolean_math = cubesat.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = 'AND'
    compare_001 = cubesat.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = 'FLOAT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'
    compare_001.inputs[1].default_value = 0.0
    compare_001.inputs[12].default_value = 0.0010000000474974513
    compare_002 = cubesat.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = 'VECTOR'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'EQUAL'
    compare_002.inputs[12].default_value = 0.0010000000474974513
    combine_xyz_005 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_005.name = "Combine XYZ.005"
    combine_xyz_005.inputs[1].hide = True
    combine_xyz_005.inputs[2].hide = True
    combine_xyz_005.inputs[1].default_value = 0.0
    combine_xyz_005.inputs[2].default_value = 0.0
    combine_xyz_006 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_006.name = "Combine XYZ.006"
    combine_xyz_006.inputs[1].hide = True
    combine_xyz_006.inputs[2].hide = True
    combine_xyz_006.inputs[1].default_value = 0.0
    combine_xyz_006.inputs[2].default_value = 0.0
    math_005 = cubesat.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'ABSOLUTE'
    math_005.use_clamp = False
    boolean_math_001 = cubesat.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.operation = 'AND'
    compare_003 = cubesat.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.data_type = 'FLOAT'
    compare_003.mode = 'ELEMENT'
    compare_003.operation = 'EQUAL'
    compare_003.inputs[1].default_value = 0.0
    compare_003.inputs[12].default_value = 0.0010000000474974513
    group_input_001 = cubesat.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    reroute_007 = cubesat.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.socket_idname = "NodeSocketFloatDistance"
    switch = cubesat.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'GEOMETRY'
    join_geometry_001 = cubesat.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"
    join_geometry_002 = cubesat.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_002.name = "Join Geometry.002"
    instance_on_points_003 = cubesat.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_003.name = "Instance on Points.003"
    instance_on_points_003.inputs[1].default_value = True
    instance_on_points_003.inputs[3].default_value = False
    instance_on_points_003.inputs[4].default_value = 0
    instance_on_points_003.inputs[6].default_value = (1.0, 1.0, 1.0)
    join_geometry_003 = cubesat.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_003.name = "Join Geometry.003"
    mesh_to_points_001 = cubesat.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points_001.name = "Mesh to Points.001"
    mesh_to_points_001.mode = 'EDGES'
    mesh_to_points_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    mesh_to_points_001.inputs[3].default_value = 0.009999999776482582
    mesh_to_points_002 = cubesat.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points_002.name = "Mesh to Points.002"
    mesh_to_points_002.mode = 'EDGES'
    mesh_to_points_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    mesh_to_points_002.inputs[3].default_value = 0.009999999776482582
    position_001 = cubesat.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    compare_004 = cubesat.nodes.new("FunctionNodeCompare")
    compare_004.name = "Compare.004"
    compare_004.data_type = 'FLOAT'
    compare_004.mode = 'ELEMENT'
    compare_004.operation = 'EQUAL'
    compare_004.inputs[1].default_value = 0.0
    compare_004.inputs[12].default_value = 0.0010000000474974513
    separate_xyz_003 = cubesat.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_003.name = "Separate XYZ.003"
    separate_xyz_003.outputs[0].hide = True
    separate_xyz_003.outputs[1].hide = True
    mesh_to_points_003 = cubesat.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points_003.name = "Mesh to Points.003"
    mesh_to_points_003.mode = 'EDGES'
    mesh_to_points_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    mesh_to_points_003.inputs[3].default_value = 0.009999999776482582
    mesh_to_points_004 = cubesat.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points_004.name = "Mesh to Points.004"
    mesh_to_points_004.mode = 'EDGES'
    mesh_to_points_004.inputs[2].default_value = (0.0, 0.0, 0.0)
    mesh_to_points_004.inputs[3].default_value = 0.009999999776482582
    compare_008 = cubesat.nodes.new("FunctionNodeCompare")
    compare_008.name = "Compare.008"
    compare_008.data_type = 'FLOAT'
    compare_008.mode = 'ELEMENT'
    compare_008.operation = 'LESS_THAN'
    compare_008.inputs[1].default_value = 0.0
    set_position = cubesat.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)
    set_position_001 = cubesat.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    position_002 = cubesat.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"
    separate_xyz_004 = cubesat.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_004.name = "Separate XYZ.004"
    compare_009 = cubesat.nodes.new("FunctionNodeCompare")
    compare_009.name = "Compare.009"
    compare_009.data_type = 'FLOAT'
    compare_009.mode = 'ELEMENT'
    compare_009.operation = 'EQUAL'
    compare_009.inputs[1].default_value = 0.0
    compare_009.inputs[12].default_value = 0.0010000000474974513
    compare_010 = cubesat.nodes.new("FunctionNodeCompare")
    compare_010.name = "Compare.010"
    compare_010.data_type = 'FLOAT'
    compare_010.mode = 'ELEMENT'
    compare_010.operation = 'EQUAL'
    compare_010.inputs[1].default_value = 0.0
    compare_010.inputs[12].default_value = 0.0010000000474974513
    math_007 = cubesat.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = 'SIGN'
    math_007.use_clamp = False
    math_008 = cubesat.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = 'SIGN'
    math_008.use_clamp = False
    math_009 = cubesat.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.operation = 'MULTIPLY'
    math_009.use_clamp = False
    math_009.inputs[1].default_value = -1.0
    math_010 = cubesat.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.operation = 'MULTIPLY'
    math_010.use_clamp = False
    math_010.inputs[1].default_value = -1.0
    combine_xyz_008 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_008.name = "Combine XYZ.008"
    combine_xyz_008.inputs[2].default_value = 0.0
    combine_xyz_009 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_009.name = "Combine XYZ.009"
    combine_xyz_009.inputs[2].default_value = 0.0
    math_011 = cubesat.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.operation = 'MULTIPLY'
    math_011.use_clamp = False
    math_012 = cubesat.nodes.new("ShaderNodeMath")
    math_012.name = "Math.012"
    math_012.operation = 'MULTIPLY'
    math_012.use_clamp = False
    math_012.inputs[1].default_value = -1.0
    random_value_004 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_004.name = "Random Value.004"
    random_value_004.data_type = 'FLOAT'
    integer_006 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_006.name = "Integer.006"
    integer_006.integer = 1324
    math_014 = cubesat.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.operation = 'MAXIMUM'
    math_014.use_clamp = False
    math_013 = cubesat.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.operation = 'MULTIPLY'
    math_013.use_clamp = False
    math_013.inputs[1].default_value = 0.20000000298023224
    math_015 = cubesat.nodes.new("ShaderNodeMath")
    math_015.name = "Math.015"
    math_015.operation = 'MULTIPLY'
    math_015.use_clamp = False
    math_015.inputs[1].default_value = 0.02500000037252903
    math_016 = cubesat.nodes.new("ShaderNodeMath")
    math_016.name = "Math.016"
    math_016.operation = 'MULTIPLY'
    math_016.use_clamp = False
    math_017 = cubesat.nodes.new("ShaderNodeMath")
    math_017.name = "Math.017"
    math_017.operation = 'MULTIPLY'
    math_017.use_clamp = False
    math_017.inputs[1].default_value = -1.0
    switch_002 = cubesat.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.input_type = 'FLOAT'
    switch_003 = cubesat.nodes.new("GeometryNodeSwitch")
    switch_003.name = "Switch.003"
    switch_003.input_type = 'FLOAT'
    random_value_005 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_005.name = "Random Value.005"
    random_value_005.data_type = 'BOOLEAN'
    random_value_005.inputs[6].default_value = 0.5
    integer_007 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_007.name = "Integer.007"
    integer_007.integer = 1793
    random_value_006 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_006.name = "Random Value.006"
    random_value_006.data_type = 'BOOLEAN'
    random_value_006.inputs[6].default_value = 0.5
    integer_008 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_008.name = "Integer.008"
    integer_008.integer = 3374
    random_value_007 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_007.name = "Random Value.007"
    random_value_007.data_type = 'FLOAT'
    random_value_007.inputs[2].default_value = 0.0
    integer_009 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_009.name = "Integer.009"
    integer_009.integer = 3069
    math_018 = cubesat.nodes.new("ShaderNodeMath")
    math_018.name = "Math.018"
    math_018.operation = 'MULTIPLY'
    math_018.use_clamp = False
    math_018.inputs[1].default_value = 0.8999999761581421
    random_value_008 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_008.name = "Random Value.008"
    random_value_008.data_type = 'FLOAT'
    random_value_008.inputs[2].default_value = 0.0
    random_value_008.inputs[8].default_value = 0
    integer_010 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_010.name = "Integer.010"
    integer_010.integer = 3069
    math_019 = cubesat.nodes.new("ShaderNodeMath")
    math_019.name = "Math.019"
    math_019.operation = 'MULTIPLY'
    math_019.use_clamp = False
    math_019.inputs[1].default_value = 0.8999999761581421
    math_020 = cubesat.nodes.new("ShaderNodeMath")
    math_020.name = "Math.020"
    math_020.operation = 'MULTIPLY'
    math_020.use_clamp = False
    math_021 = cubesat.nodes.new("ShaderNodeMath")
    math_021.name = "Math.021"
    math_021.operation = 'MULTIPLY'
    math_021.use_clamp = False
    curve_line = cubesat.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line.name = "Curve Line"
    curve_line.mode = 'POINTS'
    curve_line.inputs[0].default_value = (0.0, 0.0, 0.0)
    capture_attribute = cubesat.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute.name = "Capture Attribute"
    capture_attribute.active_index = 0
    capture_attribute.capture_items.clear()
    capture_attribute.capture_items.new('FLOAT', "Normal")
    capture_attribute.capture_items["Normal"].data_type = 'FLOAT_VECTOR'
    capture_attribute.domain = 'EDGE'
    normal_001 = cubesat.nodes.new("GeometryNodeInputNormal")
    normal_001.name = "Normal.001"
    reroute_005 = cubesat.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.socket_idname = "NodeSocketGeometry"
    axes_to_rotation = cubesat.nodes.new("FunctionNodeAxesToRotation")
    axes_to_rotation.name = "Axes to Rotation"
    axes_to_rotation.hide = True
    axes_to_rotation.primary_axis = 'X'
    axes_to_rotation.secondary_axis = 'Z'
    axes_to_rotation.inputs[0].default_value = (0.0, 0.0, 1.0)
    random_value_009 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_009.name = "Random Value.009"
    random_value_009.data_type = 'FLOAT'
    random_value_009.inputs[2].default_value = -0.34906598925590515
    random_value_009.inputs[3].default_value = 0.0
    integer_011 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_011.name = "Integer.011"
    integer_011.integer = 4724
    rotate_rotation = cubesat.nodes.new("FunctionNodeRotateRotation")
    rotate_rotation.name = "Rotate Rotation"
    rotate_rotation.rotation_space = 'LOCAL'
    combine_xyz_007 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_007.name = "Combine XYZ.007"
    combine_xyz_007.inputs[0].hide = True
    combine_xyz_007.inputs[2].hide = True
    combine_xyz_007.inputs[0].default_value = 0.0
    combine_xyz_007.inputs[2].default_value = 0.0
    set_position_002 = cubesat.nodes.new("GeometryNodeSetPosition")
    set_position_002.name = "Set Position.002"
    set_position_002.inputs[1].default_value = True
    set_position_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    curve_to_mesh = cubesat.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh.name = "Curve to Mesh"
    curve_to_mesh.inputs[2].default_value = True
    curve_circle = cubesat.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle.name = "Curve Circle"
    curve_circle.mode = 'RADIUS'
    curve_circle.inputs[0].default_value = 8
    curve_circle.inputs[4].default_value = 0.0010000000474974513
    delete_geometry_002 = cubesat.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_002.name = "Delete Geometry.002"
    delete_geometry_002.domain = 'FACE'
    delete_geometry_002.mode = 'ONLY_FACE'
    normal_002 = cubesat.nodes.new("GeometryNodeInputNormal")
    normal_002.name = "Normal.002"
    compare_011 = cubesat.nodes.new("FunctionNodeCompare")
    compare_011.name = "Compare.011"
    compare_011.data_type = 'VECTOR'
    compare_011.mode = 'ELEMENT'
    compare_011.operation = 'EQUAL'
    compare_011.inputs[5].default_value = (0.0, 0.0, -1.0)
    compare_011.inputs[12].default_value = 0.0010000000474974513
    join_geometry_004 = cubesat.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_004.name = "Join Geometry.004"
    cube_004 = cubesat.nodes.new("GeometryNodeMeshCube")
    cube_004.name = "Cube.004"
    cube_004.inputs[1].default_value = 2
    cube_004.inputs[2].default_value = 2
    cube_004.inputs[3].default_value = 2
    value = cubesat.nodes.new("ShaderNodeValue")
    value.name = "Value"
    value.outputs[0].default_value = 0.0020000000949949026
    math_006 = cubesat.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'MULTIPLY'
    math_006.use_clamp = False
    math_006.inputs[1].default_value = -1.0
    combine_xyz_010 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_010.name = "Combine XYZ.010"
    combine_xyz_010.inputs[0].hide = True
    combine_xyz_010.inputs[1].hide = True
    combine_xyz_010.inputs[0].default_value = 0.0
    combine_xyz_010.inputs[1].default_value = 0.0
    combine_xyz_011 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_011.name = "Combine XYZ.011"
    math_022 = cubesat.nodes.new("ShaderNodeMath")
    math_022.name = "Math.022"
    math_022.operation = 'MULTIPLY'
    math_022.use_clamp = False
    math_022.inputs[1].default_value = 2.0
    math_023 = cubesat.nodes.new("ShaderNodeMath")
    math_023.name = "Math.023"
    math_023.operation = 'DIVIDE'
    math_023.use_clamp = False
    math_023.inputs[1].default_value = 2.0
    combine_xyz_012 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_012.name = "Combine XYZ.012"
    combine_xyz_012.inputs[0].hide = True
    combine_xyz_012.inputs[1].hide = True
    combine_xyz_012.inputs[0].default_value = 0.0
    combine_xyz_012.inputs[1].default_value = 0.0
    transform_geometry_001 = cubesat.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
    combine_xyz_013 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_013.name = "Combine XYZ.013"
    combine_xyz_013.inputs[0].hide = True
    combine_xyz_013.inputs[1].hide = True
    combine_xyz_013.inputs[0].default_value = 0.0
    combine_xyz_013.inputs[1].default_value = 0.0
    math_024 = cubesat.nodes.new("ShaderNodeMath")
    math_024.name = "Math.024"
    math_024.operation = 'MULTIPLY'
    math_024.use_clamp = False
    math_024.inputs[1].default_value = 0.8999999761581421
    random_value_010 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_010.name = "Random Value.010"
    random_value_010.data_type = 'FLOAT'
    integer_012 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_012.name = "Integer.012"
    integer_012.integer = 2729
    math_025 = cubesat.nodes.new("ShaderNodeMath")
    math_025.name = "Math.025"
    math_025.operation = 'MULTIPLY'
    math_025.use_clamp = False
    math_025.inputs[1].default_value = 0.5
    reroute_008 = cubesat.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.socket_idname = "NodeSocketFloat"
    set_material_001 = cubesat.nodes.new("GeometryNodeSetMaterial")
    set_material_001.name = "Set Material.001"
    set_material_001.inputs[1].default_value = True
    set_material_003 = cubesat.nodes.new("GeometryNodeSetMaterial")
    set_material_003.name = "Set Material.003"
    set_material_003.inputs[1].default_value = True
    set_material_004 = cubesat.nodes.new("GeometryNodeSetMaterial")
    set_material_004.name = "Set Material.004"
    normal_003 = cubesat.nodes.new("GeometryNodeInputNormal")
    normal_003.name = "Normal.003"
    compare_005 = cubesat.nodes.new("FunctionNodeCompare")
    compare_005.name = "Compare.005"
    compare_005.data_type = 'FLOAT'
    compare_005.mode = 'ELEMENT'
    compare_005.operation = 'EQUAL'
    compare_005.inputs[1].default_value = 1.0
    compare_005.inputs[12].default_value = 0.0010000000474974513
    vector_math_002 = cubesat.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'ABSOLUTE'
    separate_xyz_005 = cubesat.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_005.name = "Separate XYZ.005"
    random_value_011 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_011.name = "Random Value.011"
    random_value_011.data_type = 'INT'
    random_value_011.inputs[4].default_value = 0
    random_value_011.inputs[5].default_value = 2
    integer_013 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_013.name = "Integer.013"
    integer_013.integer = 6421
    boolean_math_002 = cubesat.nodes.new("FunctionNodeBooleanMath")
    boolean_math_002.name = "Boolean Math.002"
    boolean_math_002.operation = 'NOT'
    set_material_005 = cubesat.nodes.new("GeometryNodeSetMaterial")
    set_material_005.name = "Set Material.005"
    random_value_012 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_012.name = "Random Value.012"
    random_value_012.data_type = 'INT'
    random_value_012.inputs[4].default_value = 0
    random_value_012.inputs[5].default_value = 4
    integer_014 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_014.name = "Integer.014"
    integer_014.integer = 9337
    index_switch_002 = cubesat.nodes.new("GeometryNodeIndexSwitch")
    index_switch_002.name = "Index Switch.002"
    index_switch_002.data_type = 'MATERIAL'
    index_switch_002.index_switch_items.clear()
    index_switch_002.index_switch_items.new()
    index_switch_002.index_switch_items.new()
    index_switch_002.index_switch_items.new()
    index_switch_002.index_switch_items.new()
    index_switch_002.index_switch_items.new()
    index_switch_002.index_switch_items.new()
    index_switch_002.index_switch_items.new()
    index_switch_002.index_switch_items.new()
    repeat_input = cubesat.nodes.new("GeometryNodeRepeatInput")
    repeat_input.name = "Repeat Input"
    repeat_output = cubesat.nodes.new("GeometryNodeRepeatOutput")
    repeat_output.name = "Repeat Output"
    repeat_output.active_index = 0
    repeat_output.inspection_index = 0
    repeat_output.repeat_items.clear()
    repeat_output.repeat_items.new('GEOMETRY', "Geometry")
    integer_math_001 = cubesat.nodes.new("FunctionNodeIntegerMath")
    integer_math_001.name = "Integer Math.001"
    integer_math_001.operation = 'ADD'
    index = cubesat.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    compare_012 = cubesat.nodes.new("FunctionNodeCompare")
    compare_012.name = "Compare.012"
    compare_012.data_type = 'INT'
    compare_012.mode = 'ELEMENT'
    compare_012.operation = 'EQUAL'
    boolean_math_003 = cubesat.nodes.new("FunctionNodeBooleanMath")
    boolean_math_003.name = "Boolean Math.003"
    boolean_math_003.operation = 'AND'
    random_value_013 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_013.name = "Random Value.013"
    random_value_013.data_type = 'BOOLEAN'
    random_value_013.inputs[6].default_value = 0.5
    integer_015 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_015.name = "Integer.015"
    integer_015.integer = 3957
    collection_info = cubesat.nodes.new("GeometryNodeCollectionInfo")
    collection_info.name = "Collection Info"
    collection_info.mute = True
    collection_info.transform_space = 'ORIGINAL'
    collection_info.inputs[1].default_value = True
    collection_info.inputs[2].default_value = False
    distribute_points_on_faces = cubesat.nodes.new("GeometryNodeDistributePointsOnFaces")
    distribute_points_on_faces.name = "Distribute Points on Faces"
    distribute_points_on_faces.mute = True
    distribute_points_on_faces.distribute_method = 'POISSON'
    distribute_points_on_faces.use_legacy_normal = False
    distribute_points_on_faces.inputs[2].default_value = 0.03999999910593033
    distribute_points_on_faces.inputs[3].default_value = 500000.0
    join_geometry_005 = cubesat.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_005.name = "Join Geometry.005"
    join_geometry_005.mute = True
    instance_on_points_004 = cubesat.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_004.name = "Instance on Points.004"
    instance_on_points_004.mute = True
    instance_on_points_004.inputs[1].default_value = True
    instance_on_points_004.inputs[3].default_value = True
    instance_on_points_004.inputs[4].default_value = 0
    normal_004 = cubesat.nodes.new("GeometryNodeInputNormal")
    normal_004.name = "Normal.004"
    normal_004.mute = True
    align_rotation_to_vector = cubesat.nodes.new("FunctionNodeAlignRotationToVector")
    align_rotation_to_vector.name = "Align Rotation to Vector"
    align_rotation_to_vector.axis = 'Z'
    align_rotation_to_vector.pivot_axis = 'AUTO'
    align_rotation_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
    align_rotation_to_vector.inputs[1].default_value = 1.0
    capture_attribute_001 = cubesat.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_001.name = "Capture Attribute.001"
    capture_attribute_001.active_index = 0
    capture_attribute_001.capture_items.clear()
    capture_attribute_001.capture_items.new('FLOAT', "Normal")
    capture_attribute_001.capture_items["Normal"].data_type = 'FLOAT_VECTOR'
    capture_attribute_001.domain = 'FACE'
    geometry_proximity = cubesat.nodes.new("GeometryNodeProximity")
    geometry_proximity.name = "Geometry Proximity"
    geometry_proximity.mute = True
    geometry_proximity.target_element = 'EDGES'
    geometry_proximity.inputs[1].default_value = 0
    geometry_proximity.inputs[2].default_value = (0.0, 0.0, 0.0)
    geometry_proximity.inputs[3].default_value = 0
    float_curve_001 = cubesat.nodes.new("ShaderNodeFloatCurve")
    float_curve_001.name = "Float Curve.001"
    float_curve_001.mapping.extend = 'EXTRAPOLATED'
    float_curve_001.mapping.tone = 'STANDARD'
    float_curve_001.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_001.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_001.mapping.clip_min_x = 0.0
    float_curve_001.mapping.clip_min_y = 0.0
    float_curve_001.mapping.clip_max_x = 1.0
    float_curve_001.mapping.clip_max_y = 1.0
    float_curve_001.mapping.use_clip = True
    float_curve_001_curve_0 = float_curve_001.mapping.curves[0]
    float_curve_001_curve_0_point_0 = float_curve_001_curve_0.points[0]
    float_curve_001_curve_0_point_0.location = (0.0, 0.0)
    float_curve_001_curve_0_point_0.handle_type = 'VECTOR'
    float_curve_001_curve_0_point_1 = float_curve_001_curve_0.points[1]
    float_curve_001_curve_0_point_1.location = (0.5, 0.0)
    float_curve_001_curve_0_point_1.handle_type = 'AUTO_CLAMPED'
    float_curve_001_curve_0_point_2 = float_curve_001_curve_0.points.new(0.6666666865348816, 1.0)
    float_curve_001_curve_0_point_2.handle_type = 'AUTO_CLAMPED'
    float_curve_001_curve_0_point_3 = float_curve_001_curve_0.points.new(1.0, 1.0)
    float_curve_001_curve_0_point_3.handle_type = 'VECTOR'
    float_curve_001.mapping.update()
    float_curve_001.inputs[0].default_value = 1.0
    subdivide_mesh = cubesat.nodes.new("GeometryNodeSubdivideMesh")
    subdivide_mesh.name = "Subdivide Mesh"
    subdivide_mesh.mute = True
    subdivide_mesh.inputs[1].default_value = 4
    math_026 = cubesat.nodes.new("ShaderNodeMath")
    math_026.name = "Math.026"
    math_026.mute = True
    math_026.operation = 'DIVIDE'
    math_026.use_clamp = True
    math_027 = cubesat.nodes.new("ShaderNodeMath")
    math_027.name = "Math.027"
    math_027.mute = True
    math_027.operation = 'MAXIMUM'
    math_027.use_clamp = False
    math_028 = cubesat.nodes.new("ShaderNodeMath")
    math_028.name = "Math.028"
    math_028.mute = True
    math_028.operation = 'SQRT'
    math_028.use_clamp = False
    random_value_002 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_002.name = "Random Value.002"
    random_value_002.mute = True
    random_value_002.data_type = 'FLOAT'
    random_value_002.inputs[2].default_value = 0.5
    random_value_002.inputs[3].default_value = 1.0
    random_value_002.inputs[7].default_value = 0
    combine_xyz_014 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_014.name = "Combine XYZ.014"
    combine_xyz_014.mute = True
    index_switch_001 = cubesat.nodes.new("GeometryNodeIndexSwitch")
    index_switch_001.name = "Index Switch.001"
    index_switch_001.data_type = 'MATERIAL'
    index_switch_001.index_switch_items.clear()
    index_switch_001.index_switch_items.new()
    index_switch_001.index_switch_items.new()
    index_switch_001.index_switch_items.new()
    join_geometry_006 = cubesat.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_006.name = "Join Geometry.006"
    instance_on_points_005 = cubesat.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_005.name = "Instance on Points.005"
    instance_on_points_005.inputs[3].default_value = False
    instance_on_points_005.inputs[4].default_value = 0
    instance_on_points_005.inputs[6].default_value = (1.0, 1.0, 1.0)
    position_003 = cubesat.nodes.new("GeometryNodeInputPosition")
    position_003.name = "Position.003"
    separate_xyz_006 = cubesat.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_006.name = "Separate XYZ.006"
    separate_xyz_006.outputs[0].hide = True
    separate_xyz_006.outputs[1].hide = True
    mesh_to_points_005 = cubesat.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points_005.name = "Mesh to Points.005"
    mesh_to_points_005.mode = 'EDGES'
    mesh_to_points_005.inputs[2].default_value = (0.0, 0.0, 0.0)
    mesh_to_points_005.inputs[3].default_value = 0.009999999776482582
    compare_013 = cubesat.nodes.new("FunctionNodeCompare")
    compare_013.name = "Compare.013"
    compare_013.data_type = 'FLOAT'
    compare_013.mode = 'ELEMENT'
    compare_013.operation = 'GREATER_THAN'
    compare_013.inputs[1].default_value = 0.0
    set_position_003 = cubesat.nodes.new("GeometryNodeSetPosition")
    set_position_003.name = "Set Position.003"
    set_position_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    set_position_004 = cubesat.nodes.new("GeometryNodeSetPosition")
    set_position_004.name = "Set Position.004"
    set_position_004.inputs[2].default_value = (0.0, 0.0, 0.0)
    position_004 = cubesat.nodes.new("GeometryNodeInputPosition")
    position_004.name = "Position.004"
    separate_xyz_007 = cubesat.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_007.name = "Separate XYZ.007"
    compare_014 = cubesat.nodes.new("FunctionNodeCompare")
    compare_014.name = "Compare.014"
    compare_014.data_type = 'FLOAT'
    compare_014.mode = 'ELEMENT'
    compare_014.operation = 'EQUAL'
    compare_014.inputs[1].default_value = 0.0
    compare_014.inputs[12].default_value = 0.0010000000474974513
    compare_015 = cubesat.nodes.new("FunctionNodeCompare")
    compare_015.name = "Compare.015"
    compare_015.data_type = 'FLOAT'
    compare_015.mode = 'ELEMENT'
    compare_015.operation = 'EQUAL'
    compare_015.inputs[1].default_value = 0.0
    compare_015.inputs[12].default_value = 0.0010000000474974513
    math_029 = cubesat.nodes.new("ShaderNodeMath")
    math_029.name = "Math.029"
    math_029.operation = 'SIGN'
    math_029.use_clamp = False
    math_030 = cubesat.nodes.new("ShaderNodeMath")
    math_030.name = "Math.030"
    math_030.operation = 'SIGN'
    math_030.use_clamp = False
    math_031 = cubesat.nodes.new("ShaderNodeMath")
    math_031.name = "Math.031"
    math_031.operation = 'MULTIPLY'
    math_031.use_clamp = False
    math_031.inputs[1].default_value = -1.0
    math_032 = cubesat.nodes.new("ShaderNodeMath")
    math_032.name = "Math.032"
    math_032.operation = 'MULTIPLY'
    math_032.use_clamp = False
    math_032.inputs[1].default_value = -1.0
    combine_xyz_015 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_015.name = "Combine XYZ.015"
    combine_xyz_015.inputs[2].default_value = 0.0
    combine_xyz_016 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_016.name = "Combine XYZ.016"
    combine_xyz_016.inputs[2].default_value = 0.0
    math_033 = cubesat.nodes.new("ShaderNodeMath")
    math_033.name = "Math.033"
    math_033.operation = 'MULTIPLY'
    math_033.use_clamp = False
    math_034 = cubesat.nodes.new("ShaderNodeMath")
    math_034.name = "Math.034"
    math_034.operation = 'MULTIPLY'
    math_034.use_clamp = False
    math_034.inputs[1].default_value = -1.0
    random_value_014 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_014.name = "Random Value.014"
    random_value_014.data_type = 'FLOAT'
    integer_016 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_016.name = "Integer.016"
    integer_016.integer = 1324
    math_035 = cubesat.nodes.new("ShaderNodeMath")
    math_035.name = "Math.035"
    math_035.operation = 'MAXIMUM'
    math_035.use_clamp = False
    math_036 = cubesat.nodes.new("ShaderNodeMath")
    math_036.name = "Math.036"
    math_036.operation = 'MULTIPLY'
    math_036.use_clamp = False
    math_036.inputs[1].default_value = 0.20000000298023224
    math_037 = cubesat.nodes.new("ShaderNodeMath")
    math_037.name = "Math.037"
    math_037.operation = 'MULTIPLY'
    math_037.use_clamp = False
    math_037.inputs[1].default_value = 0.02500000037252903
    math_038 = cubesat.nodes.new("ShaderNodeMath")
    math_038.name = "Math.038"
    math_038.operation = 'MULTIPLY'
    math_038.use_clamp = False
    math_039 = cubesat.nodes.new("ShaderNodeMath")
    math_039.name = "Math.039"
    math_039.operation = 'MULTIPLY'
    math_039.use_clamp = False
    math_039.inputs[1].default_value = -1.0
    switch_004 = cubesat.nodes.new("GeometryNodeSwitch")
    switch_004.name = "Switch.004"
    switch_004.input_type = 'FLOAT'
    switch_005 = cubesat.nodes.new("GeometryNodeSwitch")
    switch_005.name = "Switch.005"
    switch_005.mute = True
    switch_005.input_type = 'FLOAT'
    random_value_015 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_015.name = "Random Value.015"
    random_value_015.data_type = 'BOOLEAN'
    random_value_015.inputs[6].default_value = 0.5
    integer_017 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_017.name = "Integer.017"
    integer_017.integer = 1793
    random_value_016 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_016.name = "Random Value.016"
    random_value_016.data_type = 'BOOLEAN'
    random_value_016.inputs[6].default_value = 0.5
    integer_018 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_018.name = "Integer.018"
    integer_018.integer = 3374
    random_value_017 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_017.name = "Random Value.017"
    random_value_017.data_type = 'FLOAT'
    random_value_017.inputs[2].default_value = 0.0
    integer_019 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_019.name = "Integer.019"
    integer_019.integer = 3069
    math_040 = cubesat.nodes.new("ShaderNodeMath")
    math_040.name = "Math.040"
    math_040.operation = 'MULTIPLY'
    math_040.use_clamp = False
    math_040.inputs[1].default_value = 0.8999999761581421
    random_value_018 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_018.name = "Random Value.018"
    random_value_018.data_type = 'FLOAT'
    random_value_018.inputs[2].default_value = 0.0
    integer_020 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_020.name = "Integer.020"
    integer_020.integer = 3069
    math_041 = cubesat.nodes.new("ShaderNodeMath")
    math_041.name = "Math.041"
    math_041.operation = 'MULTIPLY'
    math_041.use_clamp = False
    math_041.inputs[1].default_value = 0.8999999761581421
    math_042 = cubesat.nodes.new("ShaderNodeMath")
    math_042.name = "Math.042"
    math_042.operation = 'MULTIPLY'
    math_042.use_clamp = False
    math_043 = cubesat.nodes.new("ShaderNodeMath")
    math_043.name = "Math.043"
    math_043.operation = 'MULTIPLY'
    math_043.use_clamp = False
    curve_line_001 = cubesat.nodes.new("GeometryNodeCurvePrimitiveLine")
    curve_line_001.name = "Curve Line.001"
    curve_line_001.mode = 'POINTS'
    curve_line_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    capture_attribute_002 = cubesat.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_002.name = "Capture Attribute.002"
    capture_attribute_002.active_index = 0
    capture_attribute_002.capture_items.clear()
    capture_attribute_002.capture_items.new('FLOAT', "Normal")
    capture_attribute_002.capture_items["Normal"].data_type = 'FLOAT_VECTOR'
    capture_attribute_002.domain = 'EDGE'
    normal_005 = cubesat.nodes.new("GeometryNodeInputNormal")
    normal_005.name = "Normal.005"
    reroute_009 = cubesat.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.socket_idname = "NodeSocketGeometry"
    axes_to_rotation_001 = cubesat.nodes.new("FunctionNodeAxesToRotation")
    axes_to_rotation_001.name = "Axes to Rotation.001"
    axes_to_rotation_001.hide = True
    axes_to_rotation_001.primary_axis = 'X'
    axes_to_rotation_001.secondary_axis = 'Z'
    axes_to_rotation_001.inputs[0].default_value = (0.0, 0.0, 1.0)
    random_value_019 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_019.name = "Random Value.019"
    random_value_019.data_type = 'FLOAT'
    random_value_019.inputs[2].default_value = 0.17453299462795258
    random_value_019.inputs[3].default_value = 0.0
    integer_021 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_021.name = "Integer.021"
    integer_021.integer = 4724
    rotate_rotation_001 = cubesat.nodes.new("FunctionNodeRotateRotation")
    rotate_rotation_001.name = "Rotate Rotation.001"
    rotate_rotation_001.rotation_space = 'LOCAL'
    combine_xyz_017 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_017.name = "Combine XYZ.017"
    combine_xyz_017.inputs[0].hide = True
    combine_xyz_017.inputs[2].hide = True
    combine_xyz_017.inputs[0].default_value = 0.0
    combine_xyz_017.inputs[2].default_value = 0.0
    set_position_005 = cubesat.nodes.new("GeometryNodeSetPosition")
    set_position_005.name = "Set Position.005"
    set_position_005.inputs[1].default_value = True
    set_position_005.inputs[2].default_value = (0.0, 0.0, 0.0)
    curve_to_mesh_001 = cubesat.nodes.new("GeometryNodeCurveToMesh")
    curve_to_mesh_001.name = "Curve to Mesh.001"
    curve_to_mesh_001.inputs[2].default_value = True
    join_geometry_007 = cubesat.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_007.name = "Join Geometry.007"
    cube_005 = cubesat.nodes.new("GeometryNodeMeshCube")
    cube_005.name = "Cube.005"
    cube_005.inputs[1].default_value = 2
    cube_005.inputs[2].default_value = 2
    cube_005.inputs[3].default_value = 2
    value_001 = cubesat.nodes.new("ShaderNodeValue")
    value_001.name = "Value.001"
    value_001.outputs[0].default_value = 0.004000000189989805
    combine_xyz_018 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_018.name = "Combine XYZ.018"
    combine_xyz_018.inputs[0].hide = True
    combine_xyz_018.inputs[1].hide = True
    combine_xyz_018.inputs[0].default_value = 0.0
    combine_xyz_018.inputs[1].default_value = 0.0
    combine_xyz_019 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_019.name = "Combine XYZ.019"
    math_045 = cubesat.nodes.new("ShaderNodeMath")
    math_045.name = "Math.045"
    math_045.operation = 'MULTIPLY'
    math_045.use_clamp = False
    math_045.inputs[1].default_value = 10.0
    math_046 = cubesat.nodes.new("ShaderNodeMath")
    math_046.name = "Math.046"
    math_046.operation = 'DIVIDE'
    math_046.use_clamp = False
    math_046.inputs[1].default_value = 2.0
    combine_xyz_020 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_020.name = "Combine XYZ.020"
    combine_xyz_020.inputs[0].hide = True
    combine_xyz_020.inputs[1].hide = True
    combine_xyz_020.inputs[0].default_value = 0.0
    combine_xyz_020.inputs[1].default_value = 0.0
    transform_geometry_002 = cubesat.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.mode = 'COMPONENTS'
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)
    combine_xyz_021 = cubesat.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_021.name = "Combine XYZ.021"
    combine_xyz_021.inputs[0].hide = True
    combine_xyz_021.inputs[1].hide = True
    combine_xyz_021.inputs[0].default_value = 0.0
    combine_xyz_021.inputs[1].default_value = 0.0
    math_047 = cubesat.nodes.new("ShaderNodeMath")
    math_047.name = "Math.047"
    math_047.operation = 'MULTIPLY'
    math_047.use_clamp = False
    math_047.inputs[1].default_value = 2.5
    random_value_020 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_020.name = "Random Value.020"
    random_value_020.data_type = 'FLOAT'
    integer_022 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_022.name = "Integer.022"
    integer_022.integer = 2729
    math_048 = cubesat.nodes.new("ShaderNodeMath")
    math_048.name = "Math.048"
    math_048.operation = 'MULTIPLY'
    math_048.use_clamp = False
    math_048.inputs[1].default_value = 1.0
    reroute_010 = cubesat.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.socket_idname = "NodeSocketFloat"
    set_material_006 = cubesat.nodes.new("GeometryNodeSetMaterial")
    set_material_006.name = "Set Material.006"
    set_material_006.inputs[1].default_value = True
    quadrilateral = cubesat.nodes.new("GeometryNodeCurvePrimitiveQuadrilateral")
    quadrilateral.name = "Quadrilateral"
    quadrilateral.mode = 'RECTANGLE'
    quadrilateral.inputs[0].default_value = 0.0010000000474974513
    value_002 = cubesat.nodes.new("ShaderNodeValue")
    value_002.name = "Value.002"
    value_002.outputs[0].default_value = 0.0
    value_003 = cubesat.nodes.new("ShaderNodeValue")
    value_003.name = "Value.003"
    value_003.outputs[0].default_value = 0.0
    math_044 = cubesat.nodes.new("ShaderNodeMath")
    math_044.name = "Math.044"
    math_044.operation = 'MINIMUM'
    math_044.use_clamp = False
    index_switch_003 = cubesat.nodes.new("GeometryNodeIndexSwitch")
    index_switch_003.name = "Index Switch.003"
    index_switch_003.data_type = 'MATERIAL'
    index_switch_003.index_switch_items.clear()
    index_switch_003.index_switch_items.new()
    index_switch_003.index_switch_items.new()
    index_switch_003.index_switch_items.new()
    random_value_021 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_021.name = "Random Value.021"
    random_value_021.data_type = 'INT'
    random_value_021.inputs[4].default_value = 0
    random_value_021.inputs[5].default_value = 2
    integer_023 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_023.name = "Integer.023"
    integer_023.integer = 4827
    index_switch_004 = cubesat.nodes.new("GeometryNodeIndexSwitch")
    index_switch_004.name = "Index Switch.004"
    index_switch_004.data_type = 'BOOLEAN'
    index_switch_004.index_switch_items.clear()
    index_switch_004.index_switch_items.new()
    index_switch_004.index_switch_items.new()
    index_switch_004.index_switch_items.new()
    index_switch_004.inputs[1].default_value = True
    math_050 = cubesat.nodes.new("ShaderNodeMath")
    math_050.name = "Math.050"
    math_050.operation = 'MULTIPLY'
    math_050.use_clamp = False
    math_050.inputs[1].default_value = 0.800000011920929
    random_value_022 = cubesat.nodes.new("FunctionNodeRandomValue")
    random_value_022.name = "Random Value.022"
    random_value_022.data_type = 'FLOAT'
    integer_024 = cubesat.nodes.new("FunctionNodeInputInt")
    integer_024.name = "Integer.024"
    integer_024.integer = 2729
    math_051 = cubesat.nodes.new("ShaderNodeMath")
    math_051.name = "Math.051"
    math_051.operation = 'MULTIPLY'
    math_051.use_clamp = False
    math_051.inputs[1].default_value = 0.6000000238418579
    group_input_002 = cubesat.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    set_shade_smooth = cubesat.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    set_shade_smooth.inputs[1].default_value = True
    set_shade_smooth.inputs[2].default_value = False
    repeat_input.pair_with_output(repeat_output)
    repeat_input.inputs[0].default_value = 6
    cubesat.links.new(set_material_002.outputs[0], set_material.inputs[0])
    cubesat.links.new(integer_001.outputs[0], integer_math.inputs[0])
    cubesat.links.new(group_input.outputs[0], integer_math.inputs[1])
    cubesat.links.new(integer_math.outputs[0], reroute_006.inputs[0])
    cubesat.links.new(group_input.outputs[5], set_material_002.inputs[2])
    cubesat.links.new(group_input.outputs[4], set_material.inputs[2])
    cubesat.links.new(vector.outputs[0], index_switch.inputs[1])
    cubesat.links.new(vector_004.outputs[0], index_switch.inputs[5])
    cubesat.links.new(vector_005.outputs[0], index_switch.inputs[6])
    cubesat.links.new(reroute_006.outputs[0], random_value.inputs[8])
    cubesat.links.new(integer.outputs[0], random_value.inputs[7])
    cubesat.links.new(random_value.outputs[1], float_curve.inputs[1])
    cubesat.links.new(float_curve.outputs[0], math.inputs[0])
    cubesat.links.new(math.outputs[0], float_to_integer.inputs[0])
    cubesat.links.new(integer_002.outputs[0], math.inputs[1])
    cubesat.links.new(reroute_003.outputs[0], transform_geometry.inputs[0])
    cubesat.links.new(random_value_001.outputs[0], vector_math.inputs[0])
    cubesat.links.new(vector_math.outputs[0], transform_geometry.inputs[2])
    cubesat.links.new(reroute_004.outputs[0], random_value_001.inputs[8])
    cubesat.links.new(integer_003.outputs[0], random_value_001.inputs[7])
    cubesat.links.new(float_to_integer.outputs[0], index_switch.inputs[0])
    cubesat.links.new(index_switch.outputs[0], reroute_001.inputs[0])
    cubesat.links.new(reroute_001.outputs[0], cube.inputs[0])
    cubesat.links.new(reroute_002.outputs[0], reroute_003.inputs[0])
    cubesat.links.new(reroute_006.outputs[0], reroute_004.inputs[0])
    cubesat.links.new(cube_001.outputs[0], instance_on_points.inputs[2])
    cubesat.links.new(reroute_001.outputs[0], separate_xyz.inputs[0])
    cubesat.links.new(combine_xyz.outputs[0], cube_001.inputs[0])
    cubesat.links.new(math_002.outputs[0], combine_xyz.inputs[2])
    cubesat.links.new(separate_xyz.outputs[2], math_002.inputs[0])
    cubesat.links.new(delete_geometry_001.outputs[0], instance_on_points_001.inputs[2])
    cubesat.links.new(combine_xyz_001.outputs[0], cube_002.inputs[0])
    cubesat.links.new(math_003.outputs[0], combine_xyz_001.inputs[0])
    cubesat.links.new(separate_xyz.outputs[0], math_003.inputs[0])
    cubesat.links.new(combine_xyz_002.outputs[0], cube_003.inputs[0])
    cubesat.links.new(math_004.outputs[0], combine_xyz_002.inputs[1])
    cubesat.links.new(separate_xyz.outputs[1], math_004.inputs[0])
    cubesat.links.new(delete_geometry.outputs[0], instance_on_points_002.inputs[2])
    cubesat.links.new(cube_003.outputs[0], delete_geometry.inputs[0])
    cubesat.links.new(normal.outputs[0], vector_math_001.inputs[0])
    cubesat.links.new(vector_math_001.outputs[0], compare_006.inputs[4])
    cubesat.links.new(cube_002.outputs[0], delete_geometry_001.inputs[0])
    cubesat.links.new(compare_006.outputs[0], delete_geometry_001.inputs[1])
    cubesat.links.new(reroute_001.outputs[0], vector_math_003.inputs[0])
    cubesat.links.new(vector_math_003.outputs[0], separate_xyz_001.inputs[0])
    cubesat.links.new(compare_007.outputs[0], delete_geometry.inputs[1])
    cubesat.links.new(vector_math_001.outputs[0], compare_007.inputs[4])
    cubesat.links.new(position.outputs[0], separate_xyz_002.inputs[0])
    cubesat.links.new(separate_xyz_002.outputs[1], math_001.inputs[0])
    cubesat.links.new(math_001.outputs[0], combine_xyz_003.inputs[1])
    cubesat.links.new(separate_xyz_001.outputs[1], combine_xyz_004.inputs[1])
    cubesat.links.new(separate_xyz_002.outputs[0], compare_001.inputs[0])
    cubesat.links.new(compare_001.outputs[0], boolean_math.inputs[0])
    cubesat.links.new(compare.outputs[0], boolean_math.inputs[1])
    cubesat.links.new(combine_xyz_004.outputs[0], compare.inputs[4])
    cubesat.links.new(combine_xyz_003.outputs[0], compare.inputs[5])
    cubesat.links.new(compare_003.outputs[0], boolean_math_001.inputs[0])
    cubesat.links.new(compare_002.outputs[0], boolean_math_001.inputs[1])
    cubesat.links.new(combine_xyz_006.outputs[0], compare_002.inputs[4])
    cubesat.links.new(combine_xyz_005.outputs[0], compare_002.inputs[5])
    cubesat.links.new(separate_xyz_002.outputs[0], math_005.inputs[0])
    cubesat.links.new(math_005.outputs[0], combine_xyz_005.inputs[0])
    cubesat.links.new(separate_xyz_002.outputs[1], compare_003.inputs[0])
    cubesat.links.new(separate_xyz_001.outputs[0], combine_xyz_006.inputs[0])
    cubesat.links.new(reroute_007.outputs[0], combine_xyz_001.inputs[1])
    cubesat.links.new(reroute_007.outputs[0], combine_xyz_001.inputs[2])
    cubesat.links.new(reroute_007.outputs[0], combine_xyz_002.inputs[0])
    cubesat.links.new(reroute_007.outputs[0], combine_xyz_002.inputs[2])
    cubesat.links.new(group_input_001.outputs[1], combine_xyz.inputs[0])
    cubesat.links.new(group_input_001.outputs[1], combine_xyz.inputs[1])
    cubesat.links.new(group_input_001.outputs[3], reroute_007.inputs[0])
    cubesat.links.new(group_input_001.outputs[2], math_002.inputs[1])
    cubesat.links.new(group_input_001.outputs[1], math_004.inputs[1])
    cubesat.links.new(group_input_001.outputs[1], math_003.inputs[1])
    cubesat.links.new(vector_001.outputs[0], index_switch.inputs[4])
    cubesat.links.new(vector_003.outputs[0], index_switch.inputs[3])
    cubesat.links.new(vector_002.outputs[0], index_switch.inputs[2])
    cubesat.links.new(instance_on_points_001.outputs[0], join_geometry_001.inputs[0])
    cubesat.links.new(join_geometry_001.outputs[0], switch.inputs[2])
    cubesat.links.new(join_geometry.outputs[0], reroute_002.inputs[0])
    cubesat.links.new(set_shade_smooth.outputs[0], group_output.inputs[0])
    cubesat.links.new(switch.outputs[0], join_geometry_002.inputs[0])
    cubesat.links.new(set_material_001.outputs[0], join_geometry_003.inputs[0])
    cubesat.links.new(cube.outputs[0], mesh_to_points_001.inputs[0])
    cubesat.links.new(cube.outputs[0], mesh_to_points_002.inputs[0])
    cubesat.links.new(position_001.outputs[0], separate_xyz_003.inputs[0])
    cubesat.links.new(separate_xyz_003.outputs[2], compare_004.inputs[0])
    cubesat.links.new(mesh_to_points_002.outputs[0], instance_on_points.inputs[0])
    cubesat.links.new(compare_004.outputs[0], mesh_to_points_002.inputs[1])
    cubesat.links.new(cube.outputs[0], mesh_to_points_004.inputs[0])
    cubesat.links.new(mesh_to_points_004.outputs[0], instance_on_points_001.inputs[0])
    cubesat.links.new(mesh_to_points_001.outputs[0], instance_on_points_002.inputs[0])
    cubesat.links.new(boolean_math_001.outputs[0], mesh_to_points_001.inputs[1])
    cubesat.links.new(boolean_math.outputs[0], mesh_to_points_004.inputs[1])
    cubesat.links.new(separate_xyz_003.outputs[2], compare_008.inputs[0])
    cubesat.links.new(reroute_005.outputs[0], set_position.inputs[0])
    cubesat.links.new(set_position.outputs[0], set_position_001.inputs[0])
    cubesat.links.new(position_002.outputs[0], separate_xyz_004.inputs[0])
    cubesat.links.new(separate_xyz_004.outputs[1], compare_010.inputs[0])
    cubesat.links.new(separate_xyz_004.outputs[0], compare_009.inputs[0])
    cubesat.links.new(compare_009.outputs[0], set_position_001.inputs[1])
    cubesat.links.new(compare_010.outputs[0], set_position.inputs[1])
    cubesat.links.new(separate_xyz_004.outputs[0], math_007.inputs[0])
    cubesat.links.new(separate_xyz_004.outputs[1], math_008.inputs[0])
    cubesat.links.new(math_008.outputs[0], math_009.inputs[0])
    cubesat.links.new(math_007.outputs[0], math_010.inputs[0])
    cubesat.links.new(combine_xyz_008.outputs[0], set_position.inputs[3])
    cubesat.links.new(combine_xyz_009.outputs[0], set_position_001.inputs[3])
    cubesat.links.new(math_010.outputs[0], math_011.inputs[0])
    cubesat.links.new(reroute_006.outputs[0], random_value_004.inputs[8])
    cubesat.links.new(separate_xyz_001.outputs[0], math_014.inputs[0])
    cubesat.links.new(separate_xyz_001.outputs[1], math_014.inputs[1])
    cubesat.links.new(math_013.outputs[0], random_value_004.inputs[3])
    cubesat.links.new(random_value_004.outputs[1], math_011.inputs[1])
    cubesat.links.new(math_014.outputs[0], math_013.inputs[0])
    cubesat.links.new(math_014.outputs[0], math_015.inputs[0])
    cubesat.links.new(math_015.outputs[0], random_value_004.inputs[2])
    cubesat.links.new(math_017.outputs[0], switch_002.inputs[2])
    cubesat.links.new(math_012.outputs[0], switch_003.inputs[2])
    cubesat.links.new(integer_006.outputs[0], random_value_004.inputs[7])
    cubesat.links.new(reroute_006.outputs[0], random_value_005.inputs[8])
    cubesat.links.new(integer_007.outputs[0], random_value_005.inputs[7])
    cubesat.links.new(reroute_006.outputs[0], random_value_006.inputs[8])
    cubesat.links.new(integer_008.outputs[0], random_value_006.inputs[7])
    cubesat.links.new(random_value_006.outputs[3], switch_002.inputs[0])
    cubesat.links.new(math_009.outputs[0], math_016.inputs[0])
    cubesat.links.new(random_value_004.outputs[1], math_016.inputs[1])
    cubesat.links.new(math_016.outputs[0], combine_xyz_009.inputs[1])
    cubesat.links.new(math_011.outputs[0], combine_xyz_008.inputs[0])
    cubesat.links.new(switch_003.outputs[0], combine_xyz_009.inputs[0])
    cubesat.links.new(switch_002.outputs[0], combine_xyz_008.inputs[1])
    cubesat.links.new(reroute_006.outputs[0], random_value_007.inputs[8])
    cubesat.links.new(math_018.outputs[0], random_value_007.inputs[3])
    cubesat.links.new(integer_009.outputs[0], random_value_007.inputs[7])
    cubesat.links.new(separate_xyz_001.outputs[1], math_018.inputs[0])
    cubesat.links.new(math_020.outputs[0], switch_002.inputs[1])
    cubesat.links.new(math_019.outputs[0], random_value_008.inputs[3])
    cubesat.links.new(integer_010.outputs[0], random_value_008.inputs[7])
    cubesat.links.new(separate_xyz_001.outputs[0], math_019.inputs[0])
    cubesat.links.new(math_021.outputs[0], switch_003.inputs[1])
    cubesat.links.new(random_value_005.outputs[3], switch_003.inputs[0])
    cubesat.links.new(math_021.outputs[0], math_012.inputs[0])
    cubesat.links.new(math_020.outputs[0], math_017.inputs[0])
    cubesat.links.new(random_value_007.outputs[1], math_020.inputs[0])
    cubesat.links.new(math_007.outputs[0], math_020.inputs[1])
    cubesat.links.new(random_value_008.outputs[1], math_021.inputs[0])
    cubesat.links.new(math_008.outputs[0], math_021.inputs[1])
    cubesat.links.new(set_position_002.outputs[0], instance_on_points_003.inputs[0])
    cubesat.links.new(normal_001.outputs[0], capture_attribute.inputs[1])
    cubesat.links.new(mesh_to_points_003.outputs[0], reroute_005.inputs[0])
    cubesat.links.new(cube.outputs[0], capture_attribute.inputs[0])
    cubesat.links.new(capture_attribute.outputs[0], mesh_to_points_003.inputs[0])
    cubesat.links.new(capture_attribute.outputs[1], axes_to_rotation.inputs[1])
    cubesat.links.new(reroute_006.outputs[0], random_value_009.inputs[8])
    cubesat.links.new(integer_011.outputs[0], random_value_009.inputs[7])
    cubesat.links.new(axes_to_rotation.outputs[0], rotate_rotation.inputs[0])
    cubesat.links.new(rotate_rotation.outputs[0], instance_on_points_003.inputs[5])
    cubesat.links.new(random_value_009.outputs[1], combine_xyz_007.inputs[1])
    cubesat.links.new(set_position_001.outputs[0], set_position_002.inputs[0])
    cubesat.links.new(join_geometry_004.outputs[0], instance_on_points_003.inputs[2])
    cubesat.links.new(curve_line.outputs[0], curve_to_mesh.inputs[0])
    cubesat.links.new(curve_circle.outputs[0], curve_to_mesh.inputs[1])
    cubesat.links.new(curve_to_mesh.outputs[0], delete_geometry_002.inputs[0])
    cubesat.links.new(normal_002.outputs[0], compare_011.inputs[4])
    cubesat.links.new(compare_011.outputs[0], delete_geometry_002.inputs[1])
    cubesat.links.new(transform_geometry_001.outputs[0], join_geometry_004.inputs[0])
    cubesat.links.new(value.outputs[0], math_006.inputs[0])
    cubesat.links.new(math_006.outputs[0], combine_xyz_010.inputs[2])
    cubesat.links.new(value.outputs[0], combine_xyz_011.inputs[0])
    cubesat.links.new(value.outputs[0], combine_xyz_011.inputs[1])
    cubesat.links.new(value.outputs[0], math_022.inputs[0])
    cubesat.links.new(math_022.outputs[0], combine_xyz_011.inputs[2])
    cubesat.links.new(combine_xyz_011.outputs[0], cube_004.inputs[0])
    cubesat.links.new(math_023.outputs[0], combine_xyz_012.inputs[2])
    cubesat.links.new(combine_xyz_012.outputs[0], set_position_002.inputs[3])
    cubesat.links.new(math_006.outputs[0], math_023.inputs[0])
    cubesat.links.new(compare_008.outputs[0], mesh_to_points_003.inputs[1])
    cubesat.links.new(cube_004.outputs[0], transform_geometry_001.inputs[0])
    cubesat.links.new(combine_xyz_010.outputs[0], transform_geometry_001.inputs[1])
    cubesat.links.new(combine_xyz_007.outputs[0], rotate_rotation.inputs[1])
    cubesat.links.new(combine_xyz_013.outputs[0], curve_line.inputs[1])
    cubesat.links.new(reroute_008.outputs[0], math_024.inputs[0])
    cubesat.links.new(reroute_006.outputs[0], random_value_010.inputs[8])
    cubesat.links.new(integer_012.outputs[0], random_value_010.inputs[7])
    cubesat.links.new(math_024.outputs[0], random_value_010.inputs[3])
    cubesat.links.new(reroute_008.outputs[0], math_025.inputs[0])
    cubesat.links.new(math_025.outputs[0], random_value_010.inputs[2])
    cubesat.links.new(random_value_010.outputs[1], combine_xyz_013.inputs[2])
    cubesat.links.new(separate_xyz.outputs[2], reroute_008.inputs[0])
    cubesat.links.new(instance_on_points_003.outputs[0], set_material_001.inputs[0])
    cubesat.links.new(join_geometry_002.outputs[0], set_material_003.inputs[0])
    cubesat.links.new(normal_003.outputs[0], vector_math_002.inputs[0])
    cubesat.links.new(vector_math_002.outputs[0], separate_xyz_005.inputs[0])
    cubesat.links.new(separate_xyz_005.outputs[2], compare_005.inputs[0])
    cubesat.links.new(compare_005.outputs[0], set_material_004.inputs[1])
    cubesat.links.new(reroute_006.outputs[0], random_value_011.inputs[8])
    cubesat.links.new(integer_013.outputs[0], random_value_011.inputs[7])
    cubesat.links.new(compare_005.outputs[0], boolean_math_002.inputs[0])
    cubesat.links.new(index_switch_002.outputs[0], set_material_005.inputs[2])
    cubesat.links.new(reroute_006.outputs[0], random_value_012.inputs[8])
    cubesat.links.new(set_material_004.outputs[0], repeat_input.inputs[1])
    cubesat.links.new(repeat_input.outputs[1], set_material_005.inputs[0])
    cubesat.links.new(integer_014.outputs[0], integer_math_001.inputs[0])
    cubesat.links.new(repeat_input.outputs[0], integer_math_001.inputs[1])
    cubesat.links.new(integer_math_001.outputs[0], random_value_012.inputs[7])
    cubesat.links.new(index.outputs[0], compare_012.inputs[3])
    cubesat.links.new(compare_012.outputs[0], boolean_math_003.inputs[0])
    cubesat.links.new(boolean_math_003.outputs[0], set_material_005.inputs[1])
    cubesat.links.new(repeat_input.outputs[0], compare_012.inputs[2])
    cubesat.links.new(boolean_math_002.outputs[0], boolean_math_003.inputs[1])
    cubesat.links.new(reroute_006.outputs[0], random_value_013.inputs[8])
    cubesat.links.new(integer_015.outputs[0], random_value_013.inputs[7])
    cubesat.links.new(random_value_013.outputs[3], switch.inputs[0])
    cubesat.links.new(set_material_005.outputs[0], repeat_output.inputs[0])
    cubesat.links.new(cube.outputs[0], set_material_004.inputs[0])
    cubesat.links.new(subdivide_mesh.outputs[0], distribute_points_on_faces.inputs[0])
    cubesat.links.new(collection_info.outputs[0], instance_on_points_004.inputs[2])
    cubesat.links.new(distribute_points_on_faces.outputs[0], instance_on_points_004.inputs[0])
    cubesat.links.new(instance_on_points_004.outputs[0], join_geometry_005.inputs[0])
    cubesat.links.new(align_rotation_to_vector.outputs[0], instance_on_points_004.inputs[5])
    cubesat.links.new(normal_004.outputs[0], capture_attribute_001.inputs[1])
    cubesat.links.new(capture_attribute_001.outputs[1], align_rotation_to_vector.inputs[2])
    cubesat.links.new(repeat_output.outputs[0], capture_attribute_001.inputs[0])
    cubesat.links.new(boolean_math_002.outputs[0], distribute_points_on_faces.inputs[1])
    cubesat.links.new(math_028.outputs[0], float_curve_001.inputs[1])
    cubesat.links.new(capture_attribute_001.outputs[0], geometry_proximity.inputs[0])
    cubesat.links.new(reroute_006.outputs[0], distribute_points_on_faces.inputs[6])
    cubesat.links.new(float_curve_001.outputs[0], distribute_points_on_faces.inputs[5])
    cubesat.links.new(capture_attribute_001.outputs[0], subdivide_mesh.inputs[0])
    cubesat.links.new(geometry_proximity.outputs[1], math_026.inputs[0])
    cubesat.links.new(separate_xyz_001.outputs[0], math_027.inputs[0])
    cubesat.links.new(separate_xyz_001.outputs[1], math_027.inputs[1])
    cubesat.links.new(math_027.outputs[0], math_026.inputs[1])
    cubesat.links.new(math_026.outputs[0], math_028.inputs[0])
    cubesat.links.new(random_value_002.outputs[1], combine_xyz_014.inputs[2])
    cubesat.links.new(random_value_002.outputs[1], combine_xyz_014.inputs[1])
    cubesat.links.new(random_value_002.outputs[1], combine_xyz_014.inputs[0])
    cubesat.links.new(reroute_006.outputs[0], random_value_002.inputs[8])
    cubesat.links.new(combine_xyz_014.outputs[0], instance_on_points_004.inputs[6])
    cubesat.links.new(random_value_012.outputs[2], index_switch_002.inputs[0])
    cubesat.links.new(random_value_011.outputs[2], index_switch_001.inputs[0])
    cubesat.links.new(index_switch_001.outputs[0], index_switch_002.inputs[5])
    cubesat.links.new(join_geometry_003.outputs[0], join_geometry_006.inputs[0])
    cubesat.links.new(position_003.outputs[0], separate_xyz_006.inputs[0])
    cubesat.links.new(separate_xyz_006.outputs[2], compare_013.inputs[0])
    cubesat.links.new(reroute_009.outputs[0], set_position_003.inputs[0])
    cubesat.links.new(set_position_003.outputs[0], set_position_004.inputs[0])
    cubesat.links.new(position_004.outputs[0], separate_xyz_007.inputs[0])
    cubesat.links.new(separate_xyz_007.outputs[1], compare_015.inputs[0])
    cubesat.links.new(separate_xyz_007.outputs[0], compare_014.inputs[0])
    cubesat.links.new(compare_014.outputs[0], set_position_004.inputs[1])
    cubesat.links.new(compare_015.outputs[0], set_position_003.inputs[1])
    cubesat.links.new(separate_xyz_007.outputs[0], math_029.inputs[0])
    cubesat.links.new(separate_xyz_007.outputs[1], math_030.inputs[0])
    cubesat.links.new(math_030.outputs[0], math_031.inputs[0])
    cubesat.links.new(math_029.outputs[0], math_032.inputs[0])
    cubesat.links.new(combine_xyz_015.outputs[0], set_position_003.inputs[3])
    cubesat.links.new(combine_xyz_016.outputs[0], set_position_004.inputs[3])
    cubesat.links.new(math_032.outputs[0], math_033.inputs[0])
    cubesat.links.new(reroute_006.outputs[0], random_value_014.inputs[8])
    cubesat.links.new(separate_xyz_001.outputs[0], math_035.inputs[0])
    cubesat.links.new(separate_xyz_001.outputs[1], math_035.inputs[1])
    cubesat.links.new(math_036.outputs[0], random_value_014.inputs[3])
    cubesat.links.new(random_value_014.outputs[1], math_033.inputs[1])
    cubesat.links.new(math_035.outputs[0], math_036.inputs[0])
    cubesat.links.new(math_035.outputs[0], math_037.inputs[0])
    cubesat.links.new(math_037.outputs[0], random_value_014.inputs[2])
    cubesat.links.new(math_039.outputs[0], switch_004.inputs[2])
    cubesat.links.new(math_034.outputs[0], switch_005.inputs[2])
    cubesat.links.new(integer_016.outputs[0], random_value_014.inputs[7])
    cubesat.links.new(reroute_006.outputs[0], random_value_015.inputs[8])
    cubesat.links.new(integer_017.outputs[0], random_value_015.inputs[7])
    cubesat.links.new(reroute_006.outputs[0], random_value_016.inputs[8])
    cubesat.links.new(integer_018.outputs[0], random_value_016.inputs[7])
    cubesat.links.new(random_value_016.outputs[3], switch_004.inputs[0])
    cubesat.links.new(math_031.outputs[0], math_038.inputs[0])
    cubesat.links.new(random_value_014.outputs[1], math_038.inputs[1])
    cubesat.links.new(math_038.outputs[0], combine_xyz_016.inputs[1])
    cubesat.links.new(math_033.outputs[0], combine_xyz_015.inputs[0])
    cubesat.links.new(reroute_006.outputs[0], random_value_017.inputs[8])
    cubesat.links.new(math_040.outputs[0], random_value_017.inputs[3])
    cubesat.links.new(integer_019.outputs[0], random_value_017.inputs[7])
    cubesat.links.new(separate_xyz_001.outputs[1], math_040.inputs[0])
    cubesat.links.new(math_042.outputs[0], switch_004.inputs[1])
    cubesat.links.new(math_041.outputs[0], random_value_018.inputs[3])
    cubesat.links.new(integer_020.outputs[0], random_value_018.inputs[7])
    cubesat.links.new(separate_xyz_001.outputs[0], math_041.inputs[0])
    cubesat.links.new(math_043.outputs[0], switch_005.inputs[1])
    cubesat.links.new(random_value_015.outputs[3], switch_005.inputs[0])
    cubesat.links.new(math_043.outputs[0], math_034.inputs[0])
    cubesat.links.new(math_042.outputs[0], math_039.inputs[0])
    cubesat.links.new(random_value_017.outputs[1], math_042.inputs[0])
    cubesat.links.new(math_029.outputs[0], math_042.inputs[1])
    cubesat.links.new(random_value_018.outputs[1], math_043.inputs[0])
    cubesat.links.new(math_030.outputs[0], math_043.inputs[1])
    cubesat.links.new(set_position_005.outputs[0], instance_on_points_005.inputs[0])
    cubesat.links.new(normal_005.outputs[0], capture_attribute_002.inputs[1])
    cubesat.links.new(mesh_to_points_005.outputs[0], reroute_009.inputs[0])
    cubesat.links.new(cube.outputs[0], capture_attribute_002.inputs[0])
    cubesat.links.new(capture_attribute_002.outputs[0], mesh_to_points_005.inputs[0])
    cubesat.links.new(capture_attribute_002.outputs[1], axes_to_rotation_001.inputs[1])
    cubesat.links.new(reroute_006.outputs[0], random_value_019.inputs[8])
    cubesat.links.new(integer_021.outputs[0], random_value_019.inputs[7])
    cubesat.links.new(axes_to_rotation_001.outputs[0], rotate_rotation_001.inputs[0])
    cubesat.links.new(rotate_rotation_001.outputs[0], instance_on_points_005.inputs[5])
    cubesat.links.new(random_value_019.outputs[1], combine_xyz_017.inputs[1])
    cubesat.links.new(set_position_004.outputs[0], set_position_005.inputs[0])
    cubesat.links.new(join_geometry_007.outputs[0], instance_on_points_005.inputs[2])
    cubesat.links.new(curve_line_001.outputs[0], curve_to_mesh_001.inputs[0])
    cubesat.links.new(transform_geometry_002.outputs[0], join_geometry_007.inputs[0])
    cubesat.links.new(value_001.outputs[0], combine_xyz_018.inputs[2])
    cubesat.links.new(value_001.outputs[0], combine_xyz_019.inputs[0])
    cubesat.links.new(value_001.outputs[0], combine_xyz_019.inputs[1])
    cubesat.links.new(value_001.outputs[0], math_045.inputs[0])
    cubesat.links.new(math_045.outputs[0], combine_xyz_019.inputs[2])
    cubesat.links.new(combine_xyz_019.outputs[0], cube_005.inputs[0])
    cubesat.links.new(math_046.outputs[0], combine_xyz_020.inputs[2])
    cubesat.links.new(combine_xyz_020.outputs[0], set_position_005.inputs[3])
    cubesat.links.new(value_001.outputs[0], math_046.inputs[0])
    cubesat.links.new(compare_013.outputs[0], mesh_to_points_005.inputs[1])
    cubesat.links.new(cube_005.outputs[0], transform_geometry_002.inputs[0])
    cubesat.links.new(combine_xyz_018.outputs[0], transform_geometry_002.inputs[1])
    cubesat.links.new(combine_xyz_017.outputs[0], rotate_rotation_001.inputs[1])
    cubesat.links.new(combine_xyz_021.outputs[0], curve_line_001.inputs[1])
    cubesat.links.new(reroute_010.outputs[0], math_047.inputs[0])
    cubesat.links.new(reroute_006.outputs[0], random_value_020.inputs[8])
    cubesat.links.new(integer_022.outputs[0], random_value_020.inputs[7])
    cubesat.links.new(math_047.outputs[0], random_value_020.inputs[3])
    cubesat.links.new(reroute_010.outputs[0], math_048.inputs[0])
    cubesat.links.new(math_048.outputs[0], random_value_020.inputs[2])
    cubesat.links.new(random_value_020.outputs[1], combine_xyz_021.inputs[2])
    cubesat.links.new(separate_xyz.outputs[2], reroute_010.inputs[0])
    cubesat.links.new(instance_on_points_005.outputs[0], set_material_006.inputs[0])
    cubesat.links.new(index_switch_001.outputs[0], set_material_006.inputs[2])
    cubesat.links.new(quadrilateral.outputs[0], curve_to_mesh_001.inputs[1])
    cubesat.links.new(value_002.outputs[0], combine_xyz_016.inputs[0])
    cubesat.links.new(value_003.outputs[0], combine_xyz_015.inputs[1])
    cubesat.links.new(separate_xyz.outputs[0], math_044.inputs[0])
    cubesat.links.new(separate_xyz.outputs[1], math_044.inputs[1])
    cubesat.links.new(index_switch_003.outputs[0], set_material_004.inputs[2])
    cubesat.links.new(random_value_011.outputs[2], index_switch_003.inputs[0])
    cubesat.links.new(reroute_006.outputs[0], random_value_018.inputs[8])
    cubesat.links.new(integer_023.outputs[0], random_value_021.inputs[7])
    cubesat.links.new(reroute_006.outputs[0], random_value_021.inputs[8])
    cubesat.links.new(index_switch_004.outputs[0], instance_on_points_005.inputs[1])
    cubesat.links.new(compare_014.outputs[0], index_switch_004.inputs[2])
    cubesat.links.new(compare_015.outputs[0], index_switch_004.inputs[3])
    cubesat.links.new(random_value_021.outputs[2], index_switch_004.inputs[0])
    cubesat.links.new(reroute_006.outputs[0], random_value_022.inputs[8])
    cubesat.links.new(integer_024.outputs[0], random_value_022.inputs[7])
    cubesat.links.new(math_050.outputs[0], random_value_022.inputs[3])
    cubesat.links.new(math_051.outputs[0], random_value_022.inputs[2])
    cubesat.links.new(math_044.outputs[0], math_051.inputs[0])
    cubesat.links.new(math_044.outputs[0], math_050.inputs[0])
    cubesat.links.new(random_value_022.outputs[1], quadrilateral.inputs[1])
    cubesat.links.new(group_input_002.outputs[4], index_switch_003.inputs[1])
    cubesat.links.new(group_input_002.outputs[5], index_switch_003.inputs[2])
    cubesat.links.new(group_input_002.outputs[6], index_switch_003.inputs[3])
    cubesat.links.new(group_input_002.outputs[4], index_switch_001.inputs[1])
    cubesat.links.new(group_input_002.outputs[5], index_switch_001.inputs[2])
    cubesat.links.new(group_input_002.outputs[7], index_switch_002.inputs[1])
    cubesat.links.new(group_input_002.outputs[8], index_switch_002.inputs[2])
    cubesat.links.new(group_input_002.outputs[9], index_switch_002.inputs[3])
    cubesat.links.new(group_input_002.outputs[10], index_switch_002.inputs[4])
    cubesat.links.new(transform_geometry.outputs[0], set_shade_smooth.inputs[0])
    cubesat.links.new(join_geometry_005.outputs[0], join_geometry.inputs[0])
    cubesat.links.new(group_input_002.outputs[7], set_material_001.inputs[2])
    cubesat.links.new(group_input_002.outputs[8], set_material_003.inputs[2])
    cubesat.links.new(group_input_002.outputs[5], index_switch_001.inputs[3])
    cubesat.links.new(instance_on_points_002.outputs[0], join_geometry_001.inputs[0])
    cubesat.links.new(instance_on_points.outputs[0], join_geometry_002.inputs[0])
    cubesat.links.new(set_material_003.outputs[0], join_geometry.inputs[0])
    cubesat.links.new(delete_geometry_002.outputs[0], join_geometry_004.inputs[0])
    cubesat.links.new(capture_attribute_001.outputs[0], join_geometry_005.inputs[0])
    cubesat.links.new(curve_to_mesh_001.outputs[0], join_geometry_007.inputs[0])
    cubesat.links.new(set_material_006.outputs[0], join_geometry_006.inputs[0])
    cubesat.links.new(join_geometry_006.outputs[0], join_geometry.inputs[0])
    return cubesat

cubesat = cubesat_node_group()


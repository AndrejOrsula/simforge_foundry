import bpy

def module_node_group():
    module = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Module")
    module.color_tag = 'NONE'
    module.default_group_node_width = 140
    module.is_modifier = True
    geometry_socket = module.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    module_centering_socket = module.interface.new_socket(name = "module_centering", in_out='INPUT', socket_type = 'NodeSocketBool')
    module_centering_socket.default_value = True
    module_centering_socket.attribute_domain = 'POINT'
    module_size_socket = module.interface.new_socket(name = "module_size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    module_size_socket.default_value = 0.15000000596046448
    module_size_socket.min_value = 0.0
    module_size_socket.max_value = 3.4028234663852886e+38
    module_size_socket.subtype = 'DISTANCE'
    module_size_socket.attribute_domain = 'POINT'
    module_size_socket.description = "Size of a single square module in the XY plane"
    module_thickness_socket = module.interface.new_socket(name = "module_thickness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    module_thickness_socket.default_value = 0.20000000298023224
    module_thickness_socket.min_value = 0.0
    module_thickness_socket.max_value = 3.4028234663852886e+38
    module_thickness_socket.subtype = 'DISTANCE'
    module_thickness_socket.attribute_domain = 'POINT'
    module_thickness_socket.description = "Thickness of module along Z axis"
    module_size_tolerance_socket = module.interface.new_socket(name = "module_size_tolerance", in_out='INPUT', socket_type = 'NodeSocketFloat')
    module_size_tolerance_socket.default_value = 0.0
    module_size_tolerance_socket.min_value = 0.0
    module_size_tolerance_socket.max_value = 3.4028234663852886e+38
    module_size_tolerance_socket.subtype = 'DISTANCE'
    module_size_tolerance_socket.attribute_domain = 'POINT'
    module_count_x_socket = module.interface.new_socket(name = "module_count_x", in_out='INPUT', socket_type = 'NodeSocketInt')
    module_count_x_socket.default_value = 1
    module_count_x_socket.min_value = 1
    module_count_x_socket.max_value = 2147483647
    module_count_x_socket.subtype = 'NONE'
    module_count_x_socket.attribute_domain = 'POINT'
    module_count_x_socket.description = "Number of combined module plates along X axis"
    module_count_y_socket = module.interface.new_socket(name = "module_count_y", in_out='INPUT', socket_type = 'NodeSocketInt')
    module_count_y_socket.default_value = 1
    module_count_y_socket.min_value = 1
    module_count_y_socket.max_value = 2147483647
    module_count_y_socket.subtype = 'NONE'
    module_count_y_socket.attribute_domain = 'POINT'
    module_count_y_socket.description = "Number of combined module plates along Y axis"
    holes_enable_socket = module.interface.new_socket(name = "holes_enable", in_out='INPUT', socket_type = 'NodeSocketBool')
    holes_enable_socket.default_value = False
    holes_enable_socket.attribute_domain = 'POINT'
    holes_vertices_socket = module.interface.new_socket(name = "holes_vertices", in_out='INPUT', socket_type = 'NodeSocketInt')
    holes_vertices_socket.default_value = 16
    holes_vertices_socket.min_value = 3
    holes_vertices_socket.max_value = 2147483647
    holes_vertices_socket.subtype = 'NONE'
    holes_vertices_socket.attribute_domain = 'POINT'
    holes_offset_from_corner_socket = module.interface.new_socket(name = "holes_offset_from_corner", in_out='INPUT', socket_type = 'NodeSocketFloat')
    holes_offset_from_corner_socket.default_value = 0.014999999664723873
    holes_offset_from_corner_socket.min_value = 0.0
    holes_offset_from_corner_socket.max_value = 3.4028234663852886e+38
    holes_offset_from_corner_socket.subtype = 'DISTANCE'
    holes_offset_from_corner_socket.attribute_domain = 'POINT'
    holes_diameter_socket = module.interface.new_socket(name = "holes_diameter", in_out='INPUT', socket_type = 'NodeSocketFloat')
    holes_diameter_socket.default_value = 0.00430000014603138
    holes_diameter_socket.min_value = 0.0
    holes_diameter_socket.max_value = 3.4028234663852886e+38
    holes_diameter_socket.subtype = 'DISTANCE'
    holes_diameter_socket.attribute_domain = 'POINT'
    frame = module.nodes.new("NodeFrame")
    frame.name = "Frame"
    frame_001 = module.nodes.new("NodeFrame")
    frame_001.name = "Frame.001"
    frame_002 = module.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    frame_003 = module.nodes.new("NodeFrame")
    frame_003.name = "Frame.003"
    frame_004 = module.nodes.new("NodeFrame")
    frame_004.name = "Frame.004"
    frame_005 = module.nodes.new("NodeFrame")
    frame_005.name = "Frame.005"
    transform_geometry = module.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = 'COMPONENTS'
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[3].hide = True
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
    group_input = module.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[0].hide = True
    group_input.outputs[4].hide = True
    group_input.outputs[5].hide = True
    group_input.outputs[6].hide = True
    group_input.outputs[7].hide = True
    group_input.outputs[8].hide = True
    group_input.outputs[9].hide = True
    group_input.outputs[10].hide = True
    cube = module.nodes.new("GeometryNodeMeshCube")
    cube.name = "Cube"
    cube.inputs[1].default_value = 2
    cube.inputs[2].default_value = 2
    cube.inputs[3].default_value = 2
    combine_xyz = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz_001 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    combine_xyz_001.inputs[2].hide = True
    combine_xyz_001.inputs[2].default_value = 0.0
    group_input_001 = module.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True
    group_input_001.outputs[4].hide = True
    group_input_001.outputs[5].hide = True
    group_input_001.outputs[6].hide = True
    group_input_001.outputs[7].hide = True
    group_input_001.outputs[8].hide = True
    group_input_001.outputs[9].hide = True
    group_input_001.outputs[10].hide = True
    math = module.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'MULTIPLY'
    math.use_clamp = False
    math.inputs[1].default_value = 0.5
    normal = module.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    separate_xyz = module.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.outputs[2].hide = True
    compare = module.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'GREATER_THAN'
    compare.inputs[1].default_value = 0.0
    group_input_002 = module.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[2].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[6].hide = True
    group_input_002.outputs[7].hide = True
    group_input_002.outputs[8].hide = True
    group_input_002.outputs[9].hide = True
    group_input_002.outputs[10].hide = True
    math_001 = module.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'ADD'
    math_001.use_clamp = False
    math_001.inputs[1].default_value = -1.0
    combine_xyz_002 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    combine_xyz_002.inputs[0].hide = True
    combine_xyz_002.inputs[2].hide = True
    combine_xyz_002.inputs[0].default_value = 0.0
    combine_xyz_002.inputs[2].default_value = 0.0
    math_002 = module.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'MULTIPLY'
    math_002.use_clamp = False
    math_002.inputs[2].hide = True
    math_003 = module.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'MULTIPLY'
    math_003.use_clamp = False
    math_004 = module.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'ADD'
    math_004.use_clamp = False
    math_004.inputs[1].default_value = -1.0
    group_input_003 = module.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[0].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True
    group_input_003.outputs[7].hide = True
    group_input_003.outputs[8].hide = True
    group_input_003.outputs[9].hide = True
    group_input_003.outputs[10].hide = True
    combine_xyz_003 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"
    combine_xyz_003.inputs[1].hide = True
    combine_xyz_003.inputs[2].hide = True
    combine_xyz_003.inputs[1].default_value = 0.0
    combine_xyz_003.inputs[2].default_value = 0.0
    compare_001 = module.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = 'FLOAT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'GREATER_THAN'
    compare_001.inputs[1].default_value = 0.0
    set_position = module.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)
    set_position_001 = module.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    set_position_002 = module.nodes.new("GeometryNodeSetPosition")
    set_position_002.name = "Set Position.002"
    set_position_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    set_position_003 = module.nodes.new("GeometryNodeSetPosition")
    set_position_003.name = "Set Position.003"
    set_position_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    combine_xyz_004 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004.name = "Combine XYZ.004"
    combine_xyz_004.inputs[0].hide = True
    combine_xyz_004.inputs[2].hide = True
    combine_xyz_004.inputs[0].default_value = 0.0
    combine_xyz_004.inputs[2].default_value = 0.0
    combine_xyz_005 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_005.name = "Combine XYZ.005"
    combine_xyz_005.inputs[0].hide = True
    combine_xyz_005.inputs[2].hide = True
    combine_xyz_005.inputs[0].default_value = 0.0
    combine_xyz_005.inputs[2].default_value = 0.0
    math_005 = module.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'MULTIPLY'
    math_005.use_clamp = False
    math_005.inputs[1].default_value = -1.0
    group_input_004 = module.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[4].hide = True
    group_input_004.outputs[5].hide = True
    group_input_004.outputs[6].hide = True
    group_input_004.outputs[7].hide = True
    group_input_004.outputs[8].hide = True
    group_input_004.outputs[9].hide = True
    group_input_004.outputs[10].hide = True
    compare_002 = module.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = 'FLOAT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'GREATER_THAN'
    compare_002.inputs[1].default_value = 0.0
    compare_003 = module.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.data_type = 'FLOAT'
    compare_003.mode = 'ELEMENT'
    compare_003.operation = 'LESS_THAN'
    compare_003.inputs[1].default_value = 0.0
    separate_xyz_001 = module.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"
    separate_xyz_001.outputs[0].hide = True
    separate_xyz_001.outputs[2].hide = True
    normal_001 = module.nodes.new("GeometryNodeInputNormal")
    normal_001.name = "Normal.001"
    separate_xyz_002 = module.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002.name = "Separate XYZ.002"
    separate_xyz_002.outputs[1].hide = True
    separate_xyz_002.outputs[2].hide = True
    compare_004 = module.nodes.new("FunctionNodeCompare")
    compare_004.name = "Compare.004"
    compare_004.data_type = 'FLOAT'
    compare_004.mode = 'ELEMENT'
    compare_004.operation = 'LESS_THAN'
    compare_004.inputs[1].default_value = 0.0
    compare_005 = module.nodes.new("FunctionNodeCompare")
    compare_005.name = "Compare.005"
    compare_005.data_type = 'FLOAT'
    compare_005.mode = 'ELEMENT'
    compare_005.operation = 'GREATER_THAN'
    compare_005.inputs[1].default_value = 0.0
    group_input_005 = module.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.outputs[0].hide = True
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[2].hide = True
    group_input_005.outputs[4].hide = True
    group_input_005.outputs[5].hide = True
    group_input_005.outputs[6].hide = True
    group_input_005.outputs[7].hide = True
    group_input_005.outputs[8].hide = True
    group_input_005.outputs[9].hide = True
    group_input_005.outputs[10].hide = True
    math_006 = module.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'MULTIPLY'
    math_006.use_clamp = False
    math_006.inputs[1].default_value = -1.0
    combine_xyz_006 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_006.name = "Combine XYZ.006"
    combine_xyz_006.inputs[1].hide = True
    combine_xyz_006.inputs[2].hide = True
    combine_xyz_006.inputs[1].default_value = 0.0
    combine_xyz_006.inputs[2].default_value = 0.0
    combine_xyz_007 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_007.name = "Combine XYZ.007"
    combine_xyz_007.inputs[1].hide = True
    combine_xyz_007.inputs[2].hide = True
    combine_xyz_007.inputs[1].default_value = 0.0
    combine_xyz_007.inputs[2].default_value = 0.0
    set_position_004 = module.nodes.new("GeometryNodeSetPosition")
    set_position_004.name = "Set Position.004"
    set_position_004.inputs[2].default_value = (0.0, 0.0, 0.0)
    set_position_005 = module.nodes.new("GeometryNodeSetPosition")
    set_position_005.name = "Set Position.005"
    set_position_005.inputs[2].default_value = (0.0, 0.0, 0.0)
    instance_on_points = module.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.inputs[3].hide = True
    instance_on_points.inputs[4].hide = True
    instance_on_points.inputs[5].hide = True
    instance_on_points.inputs[6].hide = True
    instance_on_points.inputs[3].default_value = False
    instance_on_points.inputs[4].default_value = 0
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)
    group_input_006 = module.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.outputs[0].hide = True
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[4].hide = True
    group_input_006.outputs[5].hide = True
    group_input_006.outputs[7].hide = True
    group_input_006.outputs[8].hide = True
    group_input_006.outputs[9].hide = True
    group_input_006.outputs[10].hide = True
    realize_instances = module.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    realize_instances.inputs[1].default_value = True
    realize_instances.inputs[2].default_value = True
    realize_instances.inputs[3].default_value = 0
    merge_by_distance = module.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = 'ALL'
    merge_by_distance.inputs[1].default_value = True
    merge_by_distance.inputs[2].default_value = 9.999999747378752e-05
    mesh_to_points = module.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points.name = "Mesh to Points"
    mesh_to_points.mode = 'VERTICES'
    mesh_to_points.inputs[1].default_value = True
    mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
    mesh_to_points.inputs[3].default_value = 0.05000000074505806
    mesh_to_points_001 = module.nodes.new("GeometryNodeMeshToPoints")
    mesh_to_points_001.name = "Mesh to Points.001"
    mesh_to_points_001.mode = 'VERTICES'
    mesh_to_points_001.inputs[1].default_value = True
    mesh_to_points_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    mesh_to_points_001.inputs[3].default_value = 0.05000000074505806
    instance_on_points_001 = module.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_001.name = "Instance on Points.001"
    instance_on_points_001.inputs[1].hide = True
    instance_on_points_001.inputs[3].hide = True
    instance_on_points_001.inputs[4].hide = True
    instance_on_points_001.inputs[5].hide = True
    instance_on_points_001.inputs[6].hide = True
    instance_on_points_001.inputs[1].default_value = True
    instance_on_points_001.inputs[3].default_value = False
    instance_on_points_001.inputs[4].default_value = 0
    instance_on_points_001.inputs[5].default_value = (0.0, 0.0, 0.0)
    instance_on_points_001.inputs[6].default_value = (1.0, 1.0, 1.0)
    instance_on_points_002 = module.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points_002.name = "Instance on Points.002"
    instance_on_points_002.inputs[1].hide = True
    instance_on_points_002.inputs[3].hide = True
    instance_on_points_002.inputs[4].hide = True
    instance_on_points_002.inputs[5].hide = True
    instance_on_points_002.inputs[6].hide = True
    instance_on_points_002.inputs[1].default_value = True
    instance_on_points_002.inputs[3].default_value = False
    instance_on_points_002.inputs[4].default_value = 0
    instance_on_points_002.inputs[5].default_value = (0.0, 0.0, 0.0)
    instance_on_points_002.inputs[6].default_value = (1.0, 1.0, 1.0)
    transform_geometry_001 = module.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    transform_geometry_001.inputs[2].hide = True
    transform_geometry_001.inputs[3].hide = True
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
    transform_geometry_002 = module.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.mode = 'COMPONENTS'
    transform_geometry_002.inputs[2].hide = True
    transform_geometry_002.inputs[3].hide = True
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)
    group_input_007 = module.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"
    group_input_007.outputs[0].hide = True
    group_input_007.outputs[2].hide = True
    group_input_007.outputs[5].hide = True
    group_input_007.outputs[6].hide = True
    group_input_007.outputs[7].hide = True
    group_input_007.outputs[9].hide = True
    group_input_007.outputs[10].hide = True
    math_007 = module.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = 'MULTIPLY'
    math_007.use_clamp = False
    math_008 = module.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = 'MULTIPLY'
    math_008.use_clamp = False
    math_008.inputs[1].default_value = 2.0
    math_009 = module.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.operation = 'SUBTRACT'
    math_009.use_clamp = False
    group_input_008 = module.nodes.new("NodeGroupInput")
    group_input_008.name = "Group Input.008"
    group_input_008.outputs[0].hide = True
    group_input_008.outputs[2].hide = True
    group_input_008.outputs[4].hide = True
    group_input_008.outputs[6].hide = True
    group_input_008.outputs[7].hide = True
    group_input_008.outputs[9].hide = True
    group_input_008.outputs[10].hide = True
    math_010 = module.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.operation = 'MULTIPLY'
    math_010.use_clamp = False
    math_011 = module.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.operation = 'MULTIPLY'
    math_011.use_clamp = False
    math_011.inputs[1].default_value = 2.0
    math_012 = module.nodes.new("ShaderNodeMath")
    math_012.name = "Math.012"
    math_012.operation = 'SUBTRACT'
    math_012.use_clamp = False
    combine_xyz_008 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_008.name = "Combine XYZ.008"
    combine_xyz_008.inputs[0].hide = True
    combine_xyz_008.inputs[2].hide = True
    combine_xyz_008.inputs[0].default_value = 0.0
    combine_xyz_008.inputs[2].default_value = 0.0
    combine_xyz_009 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_009.name = "Combine XYZ.009"
    combine_xyz_009.inputs[1].hide = True
    combine_xyz_009.inputs[2].hide = True
    combine_xyz_009.inputs[1].default_value = 0.0
    combine_xyz_009.inputs[2].default_value = 0.0
    duplicate_elements = module.nodes.new("GeometryNodeDuplicateElements")
    duplicate_elements.name = "Duplicate Elements"
    duplicate_elements.domain = 'POINT'
    duplicate_elements.inputs[1].default_value = True
    duplicate_elements.inputs[2].default_value = 1
    group_input_009 = module.nodes.new("NodeGroupInput")
    group_input_009.name = "Group Input.009"
    group_input_009.outputs[0].hide = True
    group_input_009.outputs[2].hide = True
    group_input_009.outputs[4].hide = True
    group_input_009.outputs[5].hide = True
    group_input_009.outputs[6].hide = True
    group_input_009.outputs[7].hide = True
    group_input_009.outputs[9].hide = True
    group_input_009.outputs[10].hide = True
    math_013 = module.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.operation = 'SUBTRACT'
    math_013.use_clamp = False
    points = module.nodes.new("GeometryNodePoints")
    points.name = "Points"
    points.inputs[0].default_value = 1
    points.inputs[2].default_value = 0.05000000074505806
    points_001 = module.nodes.new("GeometryNodePoints")
    points_001.name = "Points.001"
    points_001.inputs[0].default_value = 1
    points_001.inputs[2].default_value = 0.05000000074505806
    math_014 = module.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.operation = 'MULTIPLY'
    math_014.use_clamp = False
    math_014.inputs[1].default_value = 2.0
    combine_xyz_010 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_010.name = "Combine XYZ.010"
    combine_xyz_010.inputs[0].hide = True
    combine_xyz_010.inputs[2].hide = True
    combine_xyz_010.inputs[0].default_value = 0.0
    combine_xyz_010.inputs[2].default_value = 0.0
    combine_xyz_011 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_011.name = "Combine XYZ.011"
    combine_xyz_011.inputs[1].hide = True
    combine_xyz_011.inputs[2].hide = True
    combine_xyz_011.inputs[1].default_value = 0.0
    combine_xyz_011.inputs[2].default_value = 0.0
    points_002 = module.nodes.new("GeometryNodePoints")
    points_002.name = "Points.002"
    points_002.inputs[0].default_value = 1
    points_002.inputs[1].default_value = (0.0, 0.0, 0.0)
    points_002.inputs[2].default_value = 0.05000000074505806
    join_geometry = module.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    transform_geometry_003 = module.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.mode = 'COMPONENTS'
    transform_geometry_003.inputs[2].hide = True
    transform_geometry_003.inputs[3].hide = True
    transform_geometry_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)
    transform_geometry_004 = module.nodes.new("GeometryNodeTransform")
    transform_geometry_004.name = "Transform Geometry.004"
    transform_geometry_004.mode = 'COMPONENTS'
    transform_geometry_004.inputs[2].hide = True
    transform_geometry_004.inputs[3].hide = True
    transform_geometry_004.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_004.inputs[3].default_value = (1.0, 1.0, 1.0)
    combine_xyz_012 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_012.name = "Combine XYZ.012"
    combine_xyz_012.inputs[2].hide = True
    combine_xyz_012.inputs[2].default_value = 0.0
    mesh_line = module.nodes.new("GeometryNodeMeshLine")
    mesh_line.name = "Mesh Line"
    mesh_line.count_mode = 'TOTAL'
    mesh_line.mode = 'OFFSET'
    mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)
    mesh_line_001 = module.nodes.new("GeometryNodeMeshLine")
    mesh_line_001.name = "Mesh Line.001"
    mesh_line_001.count_mode = 'TOTAL'
    mesh_line_001.mode = 'OFFSET'
    mesh_line_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    combine_xyz_013 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_013.name = "Combine XYZ.013"
    combine_xyz_013.inputs[1].hide = True
    combine_xyz_013.inputs[2].hide = True
    combine_xyz_013.inputs[1].default_value = 0.0
    combine_xyz_013.inputs[2].default_value = 0.0
    combine_xyz_014 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_014.name = "Combine XYZ.014"
    combine_xyz_014.inputs[0].hide = True
    combine_xyz_014.inputs[2].hide = True
    combine_xyz_014.inputs[0].default_value = 0.0
    combine_xyz_014.inputs[2].default_value = 0.0
    group_input_010 = module.nodes.new("NodeGroupInput")
    group_input_010.name = "Group Input.010"
    group_input_010.outputs[0].hide = True
    group_input_010.outputs[2].hide = True
    group_input_010.outputs[6].hide = True
    group_input_010.outputs[7].hide = True
    group_input_010.outputs[8].hide = True
    group_input_010.outputs[9].hide = True
    group_input_010.outputs[10].hide = True
    duplicate_elements_001 = module.nodes.new("GeometryNodeDuplicateElements")
    duplicate_elements_001.name = "Duplicate Elements.001"
    duplicate_elements_001.domain = 'POINT'
    duplicate_elements_001.inputs[1].default_value = True
    duplicate_elements_001.inputs[2].default_value = 1
    join_geometry_001 = module.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"
    join_geometry_002 = module.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_002.name = "Join Geometry.002"
    math_015 = module.nodes.new("ShaderNodeMath")
    math_015.name = "Math.015"
    math_015.operation = 'MULTIPLY'
    math_015.use_clamp = False
    math_016 = module.nodes.new("ShaderNodeMath")
    math_016.name = "Math.016"
    math_016.operation = 'MULTIPLY'
    math_016.use_clamp = False
    group_input_011 = module.nodes.new("NodeGroupInput")
    group_input_011.name = "Group Input.011"
    group_input_011.outputs[0].hide = True
    group_input_011.outputs[2].hide = True
    group_input_011.outputs[6].hide = True
    group_input_011.outputs[7].hide = True
    group_input_011.outputs[8].hide = True
    group_input_011.outputs[9].hide = True
    group_input_011.outputs[10].hide = True
    math_017 = module.nodes.new("ShaderNodeMath")
    math_017.name = "Math.017"
    math_017.operation = 'MULTIPLY'
    math_017.use_clamp = False
    math_017.inputs[1].default_value = -0.5
    math_018 = module.nodes.new("ShaderNodeMath")
    math_018.name = "Math.018"
    math_018.operation = 'MULTIPLY'
    math_018.use_clamp = False
    math_018.inputs[1].default_value = -0.5
    combine_xyz_015 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_015.name = "Combine XYZ.015"
    combine_xyz_015.inputs[2].hide = True
    combine_xyz_015.inputs[2].default_value = 0.0
    vector_math = module.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'MULTIPLY'
    group_input_012 = module.nodes.new("NodeGroupInput")
    group_input_012.name = "Group Input.012"
    group_input_012.outputs[1].hide = True
    group_input_012.outputs[2].hide = True
    group_input_012.outputs[4].hide = True
    group_input_012.outputs[5].hide = True
    group_input_012.outputs[6].hide = True
    group_input_012.outputs[7].hide = True
    group_input_012.outputs[8].hide = True
    group_input_012.outputs[9].hide = True
    group_input_012.outputs[10].hide = True
    math_019 = module.nodes.new("ShaderNodeMath")
    math_019.name = "Math.019"
    math_019.operation = 'MULTIPLY'
    math_019.use_clamp = False
    math_019.inputs[1].default_value = -0.5
    combine_xyz_016 = module.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_016.name = "Combine XYZ.016"
    combine_xyz_016.inputs[0].hide = True
    combine_xyz_016.inputs[1].hide = True
    combine_xyz_016.inputs[0].default_value = 0.0
    combine_xyz_016.inputs[1].default_value = 0.0
    group_input_013 = module.nodes.new("NodeGroupInput")
    group_input_013.name = "Group Input.013"
    group_input_013.outputs[0].hide = True
    group_input_013.outputs[1].hide = True
    group_input_013.outputs[4].hide = True
    group_input_013.outputs[5].hide = True
    group_input_013.outputs[6].hide = True
    group_input_013.outputs[7].hide = True
    group_input_013.outputs[8].hide = True
    group_input_013.outputs[9].hide = True
    group_input_013.outputs[10].hide = True
    vector_math_001 = module.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'ADD'
    mesh_boolean = module.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.operation = 'DIFFERENCE'
    mesh_boolean.solver = 'EXACT'
    mesh_boolean.inputs[2].default_value = False
    mesh_boolean.inputs[3].default_value = False
    math_020 = module.nodes.new("ShaderNodeMath")
    math_020.name = "Math.020"
    math_020.operation = 'MULTIPLY'
    math_020.use_clamp = False
    math_020.inputs[1].default_value = 0.5
    group_input_014 = module.nodes.new("NodeGroupInput")
    group_input_014.name = "Group Input.014"
    group_input_014.outputs[0].hide = True
    group_input_014.outputs[1].hide = True
    group_input_014.outputs[4].hide = True
    group_input_014.outputs[5].hide = True
    group_input_014.outputs[6].hide = True
    group_input_014.outputs[8].hide = True
    group_input_014.outputs[10].hide = True
    compare_006 = module.nodes.new("FunctionNodeCompare")
    compare_006.name = "Compare.006"
    compare_006.data_type = 'FLOAT'
    compare_006.mode = 'ELEMENT'
    compare_006.operation = 'EQUAL'
    compare_006.inputs[1].default_value = 1.0
    compare_006.inputs[12].default_value = 0.0
    separate_xyz_003 = module.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_003.name = "Separate XYZ.003"
    separate_xyz_003.outputs[1].hide = True
    separate_xyz_003.outputs[2].hide = True
    normal_002 = module.nodes.new("GeometryNodeInputNormal")
    normal_002.name = "Normal.002"
    geometry_to_instance = module.nodes.new("GeometryNodeGeometryToInstance")
    geometry_to_instance.name = "Geometry to Instance"
    transform_geometry_005 = module.nodes.new("GeometryNodeTransform")
    transform_geometry_005.name = "Transform Geometry.005"
    transform_geometry_005.mode = 'COMPONENTS'
    transform_geometry_005.inputs[2].hide = True
    transform_geometry_005.inputs[3].hide = True
    transform_geometry_005.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_005.inputs[3].default_value = (1.0, 1.0, 1.0)
    group_output = module.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    store_named_attribute = module.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.data_type = 'BOOLEAN'
    store_named_attribute.domain = 'EDGE'
    store_named_attribute.inputs[2].default_value = "seam_holes"
    store_named_attribute.inputs[3].default_value = True
    cylinder = module.nodes.new("GeometryNodeMeshCylinder")
    cylinder.name = "Cylinder"
    cylinder.fill_type = 'NONE'
    cylinder.inputs[1].default_value = 1
    set_shade_smooth = module.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    set_shade_smooth.inputs[2].default_value = True
    join_geometry_003 = module.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_003.name = "Join Geometry.003"
    frame.width, frame.height = 150.0, 100.0
    frame_001.width, frame_001.height = 150.0, 100.0
    frame_002.width, frame_002.height = 150.0, 100.0
    frame_003.width, frame_003.height = 150.0, 100.0
    frame_004.width, frame_004.height = 150.0, 100.0
    frame_005.width, frame_005.height = 150.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    cube.width, cube.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    normal.width, normal.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    combine_xyz_003.width, combine_xyz_003.height = 140.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    set_position_001.width, set_position_001.height = 140.0, 100.0
    set_position_002.width, set_position_002.height = 140.0, 100.0
    set_position_003.width, set_position_003.height = 140.0, 100.0
    combine_xyz_004.width, combine_xyz_004.height = 140.0, 100.0
    combine_xyz_005.width, combine_xyz_005.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    compare_002.width, compare_002.height = 140.0, 100.0
    compare_003.width, compare_003.height = 140.0, 100.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    normal_001.width, normal_001.height = 140.0, 100.0
    separate_xyz_002.width, separate_xyz_002.height = 140.0, 100.0
    compare_004.width, compare_004.height = 140.0, 100.0
    compare_005.width, compare_005.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    combine_xyz_006.width, combine_xyz_006.height = 140.0, 100.0
    combine_xyz_007.width, combine_xyz_007.height = 140.0, 100.0
    set_position_004.width, set_position_004.height = 140.0, 100.0
    set_position_005.width, set_position_005.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
    mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
    mesh_to_points_001.width, mesh_to_points_001.height = 140.0, 100.0
    instance_on_points_001.width, instance_on_points_001.height = 140.0, 100.0
    instance_on_points_002.width, instance_on_points_002.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    math_009.width, math_009.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0
    math_010.width, math_010.height = 140.0, 100.0
    math_011.width, math_011.height = 140.0, 100.0
    math_012.width, math_012.height = 140.0, 100.0
    combine_xyz_008.width, combine_xyz_008.height = 140.0, 100.0
    combine_xyz_009.width, combine_xyz_009.height = 140.0, 100.0
    duplicate_elements.width, duplicate_elements.height = 140.0, 100.0
    group_input_009.width, group_input_009.height = 140.0, 100.0
    math_013.width, math_013.height = 140.0, 100.0
    points.width, points.height = 140.0, 100.0
    points_001.width, points_001.height = 140.0, 100.0
    math_014.width, math_014.height = 140.0, 100.0
    combine_xyz_010.width, combine_xyz_010.height = 140.0, 100.0
    combine_xyz_011.width, combine_xyz_011.height = 140.0, 100.0
    points_002.width, points_002.height = 140.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
    transform_geometry_004.width, transform_geometry_004.height = 140.0, 100.0
    combine_xyz_012.width, combine_xyz_012.height = 140.0, 100.0
    mesh_line.width, mesh_line.height = 140.0, 100.0
    mesh_line_001.width, mesh_line_001.height = 140.0, 100.0
    combine_xyz_013.width, combine_xyz_013.height = 140.0, 100.0
    combine_xyz_014.width, combine_xyz_014.height = 140.0, 100.0
    group_input_010.width, group_input_010.height = 140.0, 100.0
    duplicate_elements_001.width, duplicate_elements_001.height = 140.0, 100.0
    join_geometry_001.width, join_geometry_001.height = 140.0, 100.0
    join_geometry_002.width, join_geometry_002.height = 140.0, 100.0
    math_015.width, math_015.height = 140.0, 100.0
    math_016.width, math_016.height = 140.0, 100.0
    group_input_011.width, group_input_011.height = 140.0, 100.0
    math_017.width, math_017.height = 140.0, 100.0
    math_018.width, math_018.height = 140.0, 100.0
    combine_xyz_015.width, combine_xyz_015.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    group_input_012.width, group_input_012.height = 140.0, 100.0
    math_019.width, math_019.height = 140.0, 100.0
    combine_xyz_016.width, combine_xyz_016.height = 140.0, 100.0
    group_input_013.width, group_input_013.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    mesh_boolean.width, mesh_boolean.height = 140.0, 100.0
    math_020.width, math_020.height = 140.0, 100.0
    group_input_014.width, group_input_014.height = 140.0, 100.0
    compare_006.width, compare_006.height = 140.0, 100.0
    separate_xyz_003.width, separate_xyz_003.height = 140.0, 100.0
    normal_002.width, normal_002.height = 140.0, 100.0
    geometry_to_instance.width, geometry_to_instance.height = 160.0, 100.0
    transform_geometry_005.width, transform_geometry_005.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
    cylinder.width, cylinder.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    join_geometry_003.width, join_geometry_003.height = 140.0, 100.0
    module.links.new(combine_xyz.outputs[0], cube.inputs[0])
    module.links.new(group_input.outputs[1], combine_xyz.inputs[0])
    module.links.new(group_input.outputs[1], combine_xyz.inputs[1])
    module.links.new(group_input.outputs[2], combine_xyz.inputs[2])
    module.links.new(cube.outputs[0], transform_geometry.inputs[0])
    module.links.new(combine_xyz_001.outputs[0], transform_geometry.inputs[1])
    module.links.new(normal.outputs[0], compare_001.inputs[4])
    module.links.new(normal.outputs[0], separate_xyz.inputs[0])
    module.links.new(separate_xyz.outputs[0], compare_001.inputs[0])
    module.links.new(math_004.outputs[0], math_003.inputs[1])
    module.links.new(group_input_003.outputs[1], math_003.inputs[0])
    module.links.new(group_input_003.outputs[4], math_004.inputs[0])
    module.links.new(math_001.outputs[0], math_002.inputs[1])
    module.links.new(group_input_002.outputs[1], math_002.inputs[0])
    module.links.new(group_input_002.outputs[5], math_001.inputs[0])
    module.links.new(separate_xyz.outputs[1], compare.inputs[0])
    module.links.new(transform_geometry.outputs[0], set_position.inputs[0])
    module.links.new(math_003.outputs[0], combine_xyz_003.inputs[0])
    module.links.new(combine_xyz_003.outputs[0], set_position.inputs[3])
    module.links.new(compare_001.outputs[0], set_position.inputs[1])
    module.links.new(math_002.outputs[0], combine_xyz_002.inputs[1])
    module.links.new(combine_xyz_002.outputs[0], set_position_001.inputs[3])
    module.links.new(set_position.outputs[0], set_position_001.inputs[0])
    module.links.new(compare.outputs[0], set_position_001.inputs[1])
    module.links.new(geometry_to_instance.outputs[0], instance_on_points.inputs[2])
    module.links.new(instance_on_points.outputs[0], mesh_boolean.inputs[1])
    module.links.new(group_input_014.outputs[7], cylinder.inputs[0])
    module.links.new(math_014.outputs[0], math_013.inputs[1])
    module.links.new(group_input_009.outputs[1], math_013.inputs[0])
    module.links.new(group_input_009.outputs[8], math_014.inputs[0])
    module.links.new(math_013.outputs[0], combine_xyz_011.inputs[0])
    module.links.new(combine_xyz_011.outputs[0], points.inputs[1])
    module.links.new(points_002.outputs[0], join_geometry.inputs[0])
    module.links.new(join_geometry.outputs[0], transform_geometry_004.inputs[0])
    module.links.new(group_input_006.outputs[6], instance_on_points.inputs[1])
    module.links.new(combine_xyz_012.outputs[0], transform_geometry_004.inputs[1])
    module.links.new(mesh_line_001.outputs[0], mesh_to_points_001.inputs[0])
    module.links.new(mesh_to_points_001.outputs[0], instance_on_points_002.inputs[0])
    module.links.new(transform_geometry_004.outputs[0], instance_on_points_002.inputs[2])
    module.links.new(group_input_010.outputs[4], mesh_line_001.inputs[0])
    module.links.new(group_input_010.outputs[1], combine_xyz_013.inputs[0])
    module.links.new(combine_xyz_013.outputs[0], mesh_line_001.inputs[3])
    module.links.new(points_002.outputs[0], join_geometry_003.inputs[0])
    module.links.new(math_013.outputs[0], combine_xyz_010.inputs[1])
    module.links.new(combine_xyz_010.outputs[0], points_001.inputs[1])
    module.links.new(combine_xyz_012.outputs[0], transform_geometry_003.inputs[1])
    module.links.new(join_geometry_003.outputs[0], transform_geometry_003.inputs[0])
    module.links.new(transform_geometry_003.outputs[0], instance_on_points_001.inputs[0])
    module.links.new(mesh_line.outputs[0], mesh_to_points.inputs[0])
    module.links.new(combine_xyz_014.outputs[0], mesh_line.inputs[3])
    module.links.new(mesh_to_points.outputs[0], instance_on_points_001.inputs[2])
    module.links.new(merge_by_distance.outputs[0], instance_on_points.inputs[0])
    module.links.new(instance_on_points_001.outputs[0], duplicate_elements_001.inputs[0])
    module.links.new(duplicate_elements_001.outputs[0], transform_geometry_001.inputs[0])
    module.links.new(combine_xyz_009.outputs[0], transform_geometry_001.inputs[1])
    module.links.new(group_input_007.outputs[1], math_007.inputs[0])
    module.links.new(math_009.outputs[0], combine_xyz_009.inputs[0])
    module.links.new(math_007.outputs[0], math_009.inputs[0])
    module.links.new(group_input_007.outputs[8], math_008.inputs[0])
    module.links.new(math_008.outputs[0], math_009.inputs[1])
    module.links.new(group_input_007.outputs[4], math_007.inputs[1])
    module.links.new(duplicate_elements.outputs[0], transform_geometry_002.inputs[0])
    module.links.new(combine_xyz_008.outputs[0], transform_geometry_002.inputs[1])
    module.links.new(group_input_008.outputs[1], math_010.inputs[0])
    module.links.new(math_010.outputs[0], math_012.inputs[0])
    module.links.new(group_input_008.outputs[8], math_011.inputs[0])
    module.links.new(math_011.outputs[0], math_012.inputs[1])
    module.links.new(instance_on_points_002.outputs[0], duplicate_elements.inputs[0])
    module.links.new(group_input_008.outputs[5], math_010.inputs[1])
    module.links.new(math_012.outputs[0], combine_xyz_008.inputs[1])
    module.links.new(realize_instances.outputs[0], merge_by_distance.inputs[0])
    module.links.new(join_geometry_001.outputs[0], realize_instances.inputs[0])
    module.links.new(group_input_014.outputs[9], math_020.inputs[0])
    module.links.new(math_020.outputs[0], cylinder.inputs[3])
    module.links.new(math.outputs[0], combine_xyz_001.inputs[0])
    module.links.new(math.outputs[0], combine_xyz_001.inputs[1])
    module.links.new(group_input_009.outputs[8], combine_xyz_012.inputs[0])
    module.links.new(group_input_009.outputs[8], combine_xyz_012.inputs[1])
    module.links.new(mesh_boolean.outputs[0], transform_geometry_005.inputs[0])
    module.links.new(group_input_011.outputs[4], math_016.inputs[1])
    module.links.new(group_input_011.outputs[1], math_016.inputs[0])
    module.links.new(math_016.outputs[0], math_018.inputs[0])
    module.links.new(math_018.outputs[0], combine_xyz_015.inputs[0])
    module.links.new(math_015.outputs[0], math_017.inputs[0])
    module.links.new(group_input_011.outputs[5], math_015.inputs[1])
    module.links.new(group_input_011.outputs[1], math_015.inputs[0])
    module.links.new(math_017.outputs[0], combine_xyz_015.inputs[1])
    module.links.new(compare_002.outputs[0], set_position_003.inputs[1])
    module.links.new(group_input_004.outputs[3], math_005.inputs[0])
    module.links.new(combine_xyz_004.outputs[0], set_position_003.inputs[3])
    module.links.new(compare_003.outputs[0], set_position_002.inputs[1])
    module.links.new(combine_xyz_005.outputs[0], set_position_002.inputs[3])
    module.links.new(set_position_003.outputs[0], set_position_002.inputs[0])
    module.links.new(separate_xyz_001.outputs[1], compare_003.inputs[0])
    module.links.new(separate_xyz_001.outputs[1], compare_002.inputs[0])
    module.links.new(group_input_004.outputs[3], combine_xyz_005.inputs[1])
    module.links.new(math_005.outputs[0], combine_xyz_004.inputs[1])
    module.links.new(set_position_002.outputs[0], mesh_boolean.inputs[0])
    module.links.new(group_input_014.outputs[2], cylinder.inputs[4])
    module.links.new(normal_001.outputs[0], separate_xyz_001.inputs[0])
    module.links.new(math_019.outputs[0], combine_xyz_016.inputs[2])
    module.links.new(vector_math_001.outputs[0], transform_geometry_005.inputs[1])
    module.links.new(group_input_001.outputs[1], math.inputs[0])
    module.links.new(compare_005.outputs[0], set_position_004.inputs[1])
    module.links.new(group_input_005.outputs[3], math_006.inputs[0])
    module.links.new(combine_xyz_007.outputs[0], set_position_004.inputs[3])
    module.links.new(compare_004.outputs[0], set_position_005.inputs[1])
    module.links.new(combine_xyz_006.outputs[0], set_position_005.inputs[3])
    module.links.new(set_position_004.outputs[0], set_position_005.inputs[0])
    module.links.new(set_position_005.outputs[0], set_position_003.inputs[0])
    module.links.new(set_position_001.outputs[0], set_position_004.inputs[0])
    module.links.new(math_006.outputs[0], combine_xyz_007.inputs[0])
    module.links.new(group_input_005.outputs[3], combine_xyz_006.inputs[0])
    module.links.new(separate_xyz_002.outputs[0], compare_005.inputs[0])
    module.links.new(separate_xyz_002.outputs[0], compare_004.inputs[0])
    module.links.new(normal_001.outputs[0], separate_xyz_002.inputs[0])
    module.links.new(group_input_010.outputs[1], combine_xyz_014.inputs[1])
    module.links.new(group_input_010.outputs[5], mesh_line.inputs[0])
    module.links.new(instance_on_points_001.outputs[0], join_geometry_002.inputs[0])
    module.links.new(transform_geometry_002.outputs[0], join_geometry_001.inputs[0])
    module.links.new(group_input_013.outputs[2], math_019.inputs[0])
    module.links.new(combine_xyz_015.outputs[0], vector_math.inputs[1])
    module.links.new(vector_math.outputs[0], vector_math_001.inputs[1])
    module.links.new(combine_xyz_016.outputs[0], vector_math_001.inputs[0])
    module.links.new(group_input_012.outputs[0], vector_math.inputs[0])
    module.links.new(store_named_attribute.outputs[0], geometry_to_instance.inputs[0])
    module.links.new(set_shade_smooth.outputs[0], store_named_attribute.inputs[0])
    module.links.new(compare_006.outputs[0], store_named_attribute.inputs[1])
    module.links.new(separate_xyz_003.outputs[0], compare_006.inputs[0])
    module.links.new(normal_002.outputs[0], separate_xyz_003.inputs[0])
    module.links.new(transform_geometry_005.outputs[0], group_output.inputs[0])
    module.links.new(cylinder.outputs[0], set_shade_smooth.inputs[0])
    module.links.new(cylinder.outputs[2], set_shade_smooth.inputs[1])
    module.links.new(points_001.outputs[0], join_geometry_003.inputs[0])
    module.links.new(points.outputs[0], join_geometry.inputs[0])
    module.links.new(instance_on_points_002.outputs[0], join_geometry_002.inputs[0])
    module.links.new(join_geometry_002.outputs[0], join_geometry_001.inputs[0])
    module.links.new(transform_geometry_001.outputs[0], join_geometry_001.inputs[0])
    return module

module = module_node_group()


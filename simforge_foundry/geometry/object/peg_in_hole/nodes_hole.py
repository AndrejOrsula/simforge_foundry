import bpy

def _get_parallel_vectors_node_group():
    _get_parallel_vectors = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "_get_parallel_vectors")
    _get_parallel_vectors.color_tag = 'NONE'
    _get_parallel_vectors.default_group_node_width = 140
    output_x_socket = _get_parallel_vectors.interface.new_socket(name = "output_x", in_out='OUTPUT', socket_type = 'NodeSocketVector')
    output_x_socket.default_value = (0.0, 0.0, 0.0)
    output_x_socket.min_value = -3.4028234663852886e+38
    output_x_socket.max_value = 3.4028234663852886e+38
    output_x_socket.subtype = 'XYZ'
    output_x_socket.attribute_domain = 'POINT'
    output_y_socket = _get_parallel_vectors.interface.new_socket(name = "output_y", in_out='OUTPUT', socket_type = 'NodeSocketVector')
    output_y_socket.default_value = (0.0, 0.0, 0.0)
    output_y_socket.min_value = -3.4028234663852886e+38
    output_y_socket.max_value = 3.4028234663852886e+38
    output_y_socket.subtype = 'XYZ'
    output_y_socket.attribute_domain = 'POINT'
    input_z_socket = _get_parallel_vectors.interface.new_socket(name = "input_z", in_out='INPUT', socket_type = 'NodeSocketVector')
    input_z_socket.default_value = (0.0, 0.0, 0.0)
    input_z_socket.min_value = -10000.0
    input_z_socket.max_value = 10000.0
    input_z_socket.subtype = 'XYZ'
    input_z_socket.attribute_domain = 'POINT'
    group_input = _get_parallel_vectors.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[1].hide = True
    math = _get_parallel_vectors.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'DIVIDE'
    math.use_clamp = False
    combine_xyz = _get_parallel_vectors.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.inputs[0].default_value = 1.0
    combine_xyz.inputs[1].default_value = 0.0
    separate_xyz = _get_parallel_vectors.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.outputs[1].hide = True
    vector_math = _get_parallel_vectors.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'NORMALIZE'
    vector_math_001 = _get_parallel_vectors.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'CROSS_PRODUCT'
    math_001 = _get_parallel_vectors.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False
    math_001.inputs[1].default_value = -1.0
    group_output = _get_parallel_vectors.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    group_output.inputs[2].hide = True
    group_input.width, group_input.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    _get_parallel_vectors.links.new(math_001.outputs[0], math.inputs[0])
    _get_parallel_vectors.links.new(math.outputs[0], combine_xyz.inputs[2])
    _get_parallel_vectors.links.new(separate_xyz.outputs[0], math_001.inputs[0])
    _get_parallel_vectors.links.new(separate_xyz.outputs[2], math.inputs[1])
    _get_parallel_vectors.links.new(vector_math.outputs[0], group_output.inputs[0])
    _get_parallel_vectors.links.new(vector_math_001.outputs[0], group_output.inputs[1])
    _get_parallel_vectors.links.new(group_input.outputs[0], separate_xyz.inputs[0])
    _get_parallel_vectors.links.new(group_input.outputs[0], vector_math_001.inputs[1])
    _get_parallel_vectors.links.new(combine_xyz.outputs[0], vector_math.inputs[0])
    _get_parallel_vectors.links.new(vector_math.outputs[0], vector_math_001.inputs[0])
    return _get_parallel_vectors

_get_parallel_vectors = _get_parallel_vectors_node_group()

def _decimate_planar_node_group():
    _decimate_planar = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "_decimate_planar")
    _decimate_planar.color_tag = 'NONE'
    _decimate_planar.default_group_node_width = 140
    _decimate_planar.is_modifier = True
    geometry_socket = _decimate_planar.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket_1 = _decimate_planar.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    frame = _decimate_planar.nodes.new("NodeFrame")
    frame.name = "Frame"
    frame_001 = _decimate_planar.nodes.new("NodeFrame")
    frame_001.name = "Frame.001"
    frame_002 = _decimate_planar.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    frame_003 = _decimate_planar.nodes.new("NodeFrame")
    frame_003.name = "Frame.003"
    frame_004 = _decimate_planar.nodes.new("NodeFrame")
    frame_004.name = "Frame.004"
    frame_005 = _decimate_planar.nodes.new("NodeFrame")
    frame_005.name = "Frame.005"
    frame_006 = _decimate_planar.nodes.new("NodeFrame")
    frame_006.name = "Frame.006"
    frame_007 = _decimate_planar.nodes.new("NodeFrame")
    frame_007.name = "Frame.007"
    frame_008 = _decimate_planar.nodes.new("NodeFrame")
    frame_008.name = "Frame.008"
    join_geometry = _decimate_planar.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    merge_by_distance = _decimate_planar.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = 'ALL'
    merge_by_distance.inputs[1].default_value = True
    merge_by_distance.inputs[2].default_value = 0.0010000000474974513
    reroute = _decimate_planar.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketGeometry"
    reroute_001 = _decimate_planar.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketGeometry"
    compare = _decimate_planar.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'VECTOR'
    compare.mode = 'DOT_PRODUCT'
    compare.operation = 'LESS_THAN'
    compare.inputs[10].default_value = 0.0
    normal = _decimate_planar.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    position = _decimate_planar.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    normal_001 = _decimate_planar.nodes.new("GeometryNodeInputNormal")
    normal_001.name = "Normal.001"
    sample_nearest = _decimate_planar.nodes.new("GeometryNodeSampleNearest")
    sample_nearest.name = "Sample Nearest"
    sample_nearest.domain = 'FACE'
    sample_index = _decimate_planar.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'FACE'
    group_output_1 = _decimate_planar.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True
    reroute_002 = _decimate_planar.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.socket_idname = "NodeSocketGeometry"
    mesh_line = _decimate_planar.nodes.new("GeometryNodeMeshLine")
    mesh_line.name = "Mesh Line"
    mesh_line.count_mode = 'TOTAL'
    mesh_line.mode = 'OFFSET'
    mesh_line.inputs[1].hide = True
    mesh_line.inputs[2].hide = True
    mesh_line.inputs[2].default_value = (0.0, 0.0, 0.0)
    mesh_line.inputs[3].default_value = (1.0, 0.0, 0.0)
    domain_size = _decimate_planar.nodes.new("GeometryNodeAttributeDomainSize")
    domain_size.name = "Domain Size"
    domain_size.component = 'CURVE'
    domain_size.outputs[0].hide = True
    domain_size.outputs[1].hide = True
    domain_size.outputs[2].hide = True
    domain_size.outputs[3].hide = True
    domain_size.outputs[5].hide = True
    sample_index_001 = _decimate_planar.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.clamp = False
    sample_index_001.data_type = 'INT'
    sample_index_001.domain = 'CURVE'
    resample_curve = _decimate_planar.nodes.new("GeometryNodeResampleCurve")
    resample_curve.name = "Resample Curve"
    resample_curve.mode = 'COUNT'
    resample_curve.inputs[1].default_value = True
    index = _decimate_planar.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    spline_length = _decimate_planar.nodes.new("GeometryNodeSplineLength")
    spline_length.name = "Spline Length"
    spline_length.outputs[0].hide = True
    fill_curve = _decimate_planar.nodes.new("GeometryNodeFillCurve")
    fill_curve.name = "Fill Curve"
    fill_curve.mode = 'NGONS'
    fill_curve.inputs[1].default_value = 0
    sample_index_002 = _decimate_planar.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.clamp = False
    sample_index_002.data_type = 'FLOAT_VECTOR'
    sample_index_002.domain = 'POINT'
    position_001 = _decimate_planar.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    index_001 = _decimate_planar.nodes.new("GeometryNodeInputIndex")
    index_001.name = "Index.001"
    set_position = _decimate_planar.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.inputs[1].hide = True
    set_position.inputs[3].hide = True
    set_position.inputs[1].default_value = True
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
    realize_instances = _decimate_planar.nodes.new("GeometryNodeRealizeInstances")
    realize_instances.name = "Realize Instances"
    realize_instances.inputs[1].default_value = True
    realize_instances.inputs[2].default_value = True
    realize_instances.inputs[3].default_value = 0
    instance_on_points = _decimate_planar.nodes.new("GeometryNodeInstanceOnPoints")
    instance_on_points.name = "Instance on Points"
    instance_on_points.inputs[1].hide = True
    instance_on_points.inputs[3].hide = True
    instance_on_points.inputs[4].hide = True
    instance_on_points.inputs[5].hide = True
    instance_on_points.inputs[6].hide = True
    instance_on_points.inputs[1].default_value = True
    instance_on_points.inputs[3].default_value = False
    instance_on_points.inputs[4].default_value = 0
    instance_on_points.inputs[5].default_value = (0.0, 0.0, 0.0)
    instance_on_points.inputs[6].default_value = (1.0, 1.0, 1.0)
    reroute_003 = _decimate_planar.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.socket_idname = "NodeSocketGeometry"
    reroute_004 = _decimate_planar.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.socket_idname = "NodeSocketGeometry"
    reroute_005 = _decimate_planar.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.socket_idname = "NodeSocketGeometry"
    evaluate_at_index = _decimate_planar.nodes.new("GeometryNodeFieldAtIndex")
    evaluate_at_index.name = "Evaluate at Index"
    evaluate_at_index.data_type = 'FLOAT_VECTOR'
    evaluate_at_index.domain = 'POINT'
    evaluate_at_index_001 = _decimate_planar.nodes.new("GeometryNodeFieldAtIndex")
    evaluate_at_index_001.name = "Evaluate at Index.001"
    evaluate_at_index_001.data_type = 'FLOAT_VECTOR'
    evaluate_at_index_001.domain = 'POINT'
    edge_neighbors = _decimate_planar.nodes.new("GeometryNodeInputMeshEdgeNeighbors")
    edge_neighbors.name = "Edge Neighbors"
    compare_001 = _decimate_planar.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = 'INT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'
    compare_001.inputs[3].default_value = 0
    compare_002 = _decimate_planar.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = 'INT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'GREATER_THAN'
    compare_002.inputs[3].default_value = 1
    delete_geometry = _decimate_planar.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'EDGE'
    delete_geometry.mode = 'EDGE_FACE'
    separate_geometry = _decimate_planar.nodes.new("GeometryNodeSeparateGeometry")
    separate_geometry.name = "Separate Geometry"
    separate_geometry.domain = 'EDGE'
    reroute_006 = _decimate_planar.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.socket_idname = "NodeSocketGeometry"
    spline_parameter = _decimate_planar.nodes.new("GeometryNodeSplineParameter")
    spline_parameter.name = "Spline Parameter"
    spline_parameter.outputs[0].hide = True
    spline_parameter.outputs[1].hide = True
    position_002 = _decimate_planar.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"
    math_1 = _decimate_planar.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = 'SUBTRACT'
    math_1.use_clamp = False
    math_1.inputs[1].default_value = 1.0
    spline_length_001 = _decimate_planar.nodes.new("GeometryNodeSplineLength")
    spline_length_001.name = "Spline Length.001"
    spline_length_001.outputs[0].hide = True
    math_001_1 = _decimate_planar.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = 'ADD'
    math_001_1.use_clamp = False
    math_001_1.inputs[1].default_value = 1.0
    accumulate_field = _decimate_planar.nodes.new("GeometryNodeAccumulateField")
    accumulate_field.name = "Accumulate Field"
    accumulate_field.data_type = 'INT'
    accumulate_field.domain = 'CURVE'
    accumulate_field.inputs[1].hide = True
    accumulate_field.outputs[0].hide = True
    accumulate_field.outputs[2].hide = True
    accumulate_field.inputs[1].default_value = 0
    math_002 = _decimate_planar.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'WRAP'
    math_002.use_clamp = False
    math_002.inputs[2].default_value = 0.0
    math_003 = _decimate_planar.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'WRAP'
    math_003.use_clamp = False
    math_003.inputs[2].default_value = 0.0
    curve_circle = _decimate_planar.nodes.new("GeometryNodeCurvePrimitiveCircle")
    curve_circle.name = "Curve Circle"
    curve_circle.mode = 'RADIUS'
    curve_circle.inputs[0].default_value = 4
    curve_circle.inputs[4].default_value = 0.4000000059604645
    reroute_007 = _decimate_planar.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.socket_idname = "NodeSocketGeometry"
    math_004 = _decimate_planar.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'ADD'
    math_004.use_clamp = False
    mesh_to_curve = _decimate_planar.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    mesh_to_curve.inputs[1].hide = True
    mesh_to_curve.inputs[1].default_value = True
    math_005 = _decimate_planar.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'ADD'
    math_005.use_clamp = False
    position_003 = _decimate_planar.nodes.new("GeometryNodeInputPosition")
    position_003.name = "Position.003"
    vector_math_1 = _decimate_planar.nodes.new("ShaderNodeVectorMath")
    vector_math_1.name = "Vector Math"
    vector_math_1.operation = 'SUBTRACT'
    vector_math_001_1 = _decimate_planar.nodes.new("ShaderNodeVectorMath")
    vector_math_001_1.name = "Vector Math.001"
    vector_math_001_1.operation = 'SUBTRACT'
    compare_003 = _decimate_planar.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.data_type = 'VECTOR'
    compare_003.mode = 'DIRECTION'
    compare_003.operation = 'EQUAL'
    compare_003.inputs[11].default_value = 0.0
    compare_003.inputs[12].default_value = 0.0010000000474974513
    delete_geometry_001 = _decimate_planar.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.domain = 'POINT'
    delete_geometry_001.mode = 'ALL'
    flip_faces = _decimate_planar.nodes.new("GeometryNodeFlipFaces")
    flip_faces.name = "Flip Faces"
    edge_angle = _decimate_planar.nodes.new("GeometryNodeInputMeshEdgeAngle")
    edge_angle.name = "Edge Angle"
    edge_angle.outputs[1].hide = True
    split_edges = _decimate_planar.nodes.new("GeometryNodeSplitEdges")
    split_edges.name = "Split Edges"
    group_input_1 = _decimate_planar.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"
    group_input_1.outputs[1].hide = True
    compare_004 = _decimate_planar.nodes.new("FunctionNodeCompare")
    compare_004.name = "Compare.004"
    compare_004.data_type = 'FLOAT'
    compare_004.mode = 'ELEMENT'
    compare_004.operation = 'NOT_EQUAL'
    compare_004.inputs[1].default_value = 0.0
    compare_004.inputs[12].default_value = 0.0010000000474974513
    frame.width, frame.height = 150.0, 100.0
    frame_001.width, frame_001.height = 150.0, 100.0
    frame_002.width, frame_002.height = 150.0, 100.0
    frame_003.width, frame_003.height = 150.0, 100.0
    frame_004.width, frame_004.height = 150.0, 100.0
    frame_005.width, frame_005.height = 150.0, 100.0
    frame_006.width, frame_006.height = 150.0, 100.0
    frame_007.width, frame_007.height = 150.0, 100.0
    frame_008.width, frame_008.height = 150.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
    reroute.width, reroute.height = 140.0, 100.0
    reroute_001.width, reroute_001.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    normal.width, normal.height = 140.0, 100.0
    position.width, position.height = 140.0, 100.0
    normal_001.width, normal_001.height = 140.0, 100.0
    sample_nearest.width, sample_nearest.height = 140.0, 100.0
    sample_index.width, sample_index.height = 140.0, 100.0
    group_output_1.width, group_output_1.height = 140.0, 100.0
    reroute_002.width, reroute_002.height = 140.0, 100.0
    mesh_line.width, mesh_line.height = 140.0, 100.0
    domain_size.width, domain_size.height = 140.0, 100.0
    sample_index_001.width, sample_index_001.height = 140.0, 100.0
    resample_curve.width, resample_curve.height = 140.0, 100.0
    index.width, index.height = 140.0, 100.0
    spline_length.width, spline_length.height = 140.0, 100.0
    fill_curve.width, fill_curve.height = 140.0, 100.0
    sample_index_002.width, sample_index_002.height = 140.0, 100.0
    position_001.width, position_001.height = 140.0, 100.0
    index_001.width, index_001.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    realize_instances.width, realize_instances.height = 140.0, 100.0
    instance_on_points.width, instance_on_points.height = 140.0, 100.0
    reroute_003.width, reroute_003.height = 140.0, 100.0
    reroute_004.width, reroute_004.height = 140.0, 100.0
    reroute_005.width, reroute_005.height = 140.0, 100.0
    evaluate_at_index.width, evaluate_at_index.height = 140.0, 100.0
    evaluate_at_index_001.width, evaluate_at_index_001.height = 140.0, 100.0
    edge_neighbors.width, edge_neighbors.height = 140.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    compare_002.width, compare_002.height = 140.0, 100.0
    delete_geometry.width, delete_geometry.height = 140.0, 100.0
    separate_geometry.width, separate_geometry.height = 140.0, 100.0
    reroute_006.width, reroute_006.height = 140.0, 100.0
    spline_parameter.width, spline_parameter.height = 140.0, 100.0
    position_002.width, position_002.height = 140.0, 100.0
    math_1.width, math_1.height = 140.0, 100.0
    spline_length_001.width, spline_length_001.height = 140.0, 100.0
    math_001_1.width, math_001_1.height = 140.0, 100.0
    accumulate_field.width, accumulate_field.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    curve_circle.width, curve_circle.height = 140.0, 100.0
    reroute_007.width, reroute_007.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    position_003.width, position_003.height = 140.0, 100.0
    vector_math_1.width, vector_math_1.height = 140.0, 100.0
    vector_math_001_1.width, vector_math_001_1.height = 140.0, 100.0
    compare_003.width, compare_003.height = 140.0, 100.0
    delete_geometry_001.width, delete_geometry_001.height = 140.0, 100.0
    flip_faces.width, flip_faces.height = 140.0, 100.0
    edge_angle.width, edge_angle.height = 140.0, 100.0
    split_edges.width, split_edges.height = 140.0, 100.0
    group_input_1.width, group_input_1.height = 140.0, 100.0
    compare_004.width, compare_004.height = 140.0, 100.0
    _decimate_planar.links.new(flip_faces.outputs[0], group_output_1.inputs[0])
    _decimate_planar.links.new(edge_angle.outputs[0], compare_004.inputs[0])
    _decimate_planar.links.new(group_input_1.outputs[0], split_edges.inputs[0])
    _decimate_planar.links.new(compare_004.outputs[0], split_edges.inputs[1])
    _decimate_planar.links.new(split_edges.outputs[0], delete_geometry.inputs[0])
    _decimate_planar.links.new(edge_neighbors.outputs[0], compare_002.inputs[2])
    _decimate_planar.links.new(compare_002.outputs[0], delete_geometry.inputs[1])
    _decimate_planar.links.new(edge_neighbors.outputs[0], compare_001.inputs[2])
    _decimate_planar.links.new(separate_geometry.outputs[0], mesh_to_curve.inputs[0])
    _decimate_planar.links.new(delete_geometry.outputs[0], separate_geometry.inputs[0])
    _decimate_planar.links.new(compare_001.outputs[0], separate_geometry.inputs[1])
    _decimate_planar.links.new(spline_parameter.outputs[2], math_001_1.inputs[0])
    _decimate_planar.links.new(math_001_1.outputs[0], math_003.inputs[0])
    _decimate_planar.links.new(math_003.outputs[0], math_005.inputs[1])
    _decimate_planar.links.new(spline_length_001.outputs[1], math_003.inputs[1])
    _decimate_planar.links.new(spline_length_001.outputs[1], accumulate_field.inputs[0])
    _decimate_planar.links.new(accumulate_field.outputs[1], math_005.inputs[0])
    _decimate_planar.links.new(position_002.outputs[0], evaluate_at_index.inputs[1])
    _decimate_planar.links.new(math_005.outputs[0], evaluate_at_index.inputs[0])
    _decimate_planar.links.new(spline_parameter.outputs[2], math_1.inputs[0])
    _decimate_planar.links.new(math_1.outputs[0], math_002.inputs[0])
    _decimate_planar.links.new(spline_length_001.outputs[1], math_002.inputs[1])
    _decimate_planar.links.new(math_002.outputs[0], math_004.inputs[0])
    _decimate_planar.links.new(accumulate_field.outputs[1], math_004.inputs[1])
    _decimate_planar.links.new(math_004.outputs[0], evaluate_at_index_001.inputs[0])
    _decimate_planar.links.new(position_002.outputs[0], evaluate_at_index_001.inputs[1])
    _decimate_planar.links.new(position_003.outputs[0], vector_math_1.inputs[1])
    _decimate_planar.links.new(evaluate_at_index_001.outputs[0], vector_math_1.inputs[0])
    _decimate_planar.links.new(vector_math_1.outputs[0], compare_003.inputs[4])
    _decimate_planar.links.new(vector_math_001_1.outputs[0], compare_003.inputs[5])
    _decimate_planar.links.new(mesh_to_curve.outputs[0], delete_geometry_001.inputs[0])
    _decimate_planar.links.new(compare_003.outputs[0], delete_geometry_001.inputs[1])
    _decimate_planar.links.new(reroute_005.outputs[0], domain_size.inputs[0])
    _decimate_planar.links.new(position_001.outputs[0], sample_index_002.inputs[1])
    _decimate_planar.links.new(reroute_004.outputs[0], sample_index_002.inputs[0])
    _decimate_planar.links.new(sample_index_002.outputs[0], set_position.inputs[2])
    _decimate_planar.links.new(index_001.outputs[0], sample_index_002.inputs[2])
    _decimate_planar.links.new(set_position.outputs[0], join_geometry.inputs[0])
    _decimate_planar.links.new(join_geometry.outputs[0], merge_by_distance.inputs[0])
    _decimate_planar.links.new(separate_geometry.outputs[1], reroute_006.inputs[0])
    _decimate_planar.links.new(reroute_006.outputs[0], reroute.inputs[0])
    _decimate_planar.links.new(reroute_001.outputs[0], sample_index.inputs[0])
    _decimate_planar.links.new(position.outputs[0], sample_nearest.inputs[1])
    _decimate_planar.links.new(normal_001.outputs[0], sample_index.inputs[1])
    _decimate_planar.links.new(sample_nearest.outputs[0], sample_index.inputs[2])
    _decimate_planar.links.new(reroute_001.outputs[0], sample_nearest.inputs[0])
    _decimate_planar.links.new(merge_by_distance.outputs[0], flip_faces.inputs[0])
    _decimate_planar.links.new(compare.outputs[0], flip_faces.inputs[1])
    _decimate_planar.links.new(normal.outputs[0], compare.inputs[4])
    _decimate_planar.links.new(sample_index.outputs[0], compare.inputs[5])
    _decimate_planar.links.new(split_edges.outputs[0], reroute_002.inputs[0])
    _decimate_planar.links.new(reroute_002.outputs[0], reroute_001.inputs[0])
    _decimate_planar.links.new(curve_circle.outputs[0], instance_on_points.inputs[2])
    _decimate_planar.links.new(mesh_line.outputs[0], instance_on_points.inputs[0])
    _decimate_planar.links.new(instance_on_points.outputs[0], realize_instances.inputs[0])
    _decimate_planar.links.new(realize_instances.outputs[0], resample_curve.inputs[0])
    _decimate_planar.links.new(reroute_007.outputs[0], sample_index_001.inputs[0])
    _decimate_planar.links.new(spline_length.outputs[1], sample_index_001.inputs[1])
    _decimate_planar.links.new(index.outputs[0], sample_index_001.inputs[2])
    _decimate_planar.links.new(sample_index_001.outputs[0], resample_curve.inputs[2])
    _decimate_planar.links.new(fill_curve.outputs[0], set_position.inputs[0])
    _decimate_planar.links.new(resample_curve.outputs[0], fill_curve.inputs[0])
    _decimate_planar.links.new(domain_size.outputs[4], mesh_line.inputs[0])
    _decimate_planar.links.new(reroute_005.outputs[0], reroute_003.inputs[0])
    _decimate_planar.links.new(reroute_003.outputs[0], reroute_004.inputs[0])
    _decimate_planar.links.new(delete_geometry_001.outputs[0], reroute_005.inputs[0])
    _decimate_planar.links.new(reroute_005.outputs[0], reroute_007.inputs[0])
    _decimate_planar.links.new(position_003.outputs[0], vector_math_001_1.inputs[0])
    _decimate_planar.links.new(evaluate_at_index.outputs[0], vector_math_001_1.inputs[1])
    _decimate_planar.links.new(reroute.outputs[0], join_geometry.inputs[0])
    return _decimate_planar

_decimate_planar = _decimate_planar_node_group()

def peg_node_group():
    peg = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Peg")
    peg.color_tag = 'NONE'
    peg.default_group_node_width = 140
    peg.is_modifier = True
    geometry_socket_2 = peg.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_2.attribute_domain = 'POINT'
    random_seed_socket = peg.interface.new_socket(name = "random_seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    random_seed_socket.default_value = 0
    random_seed_socket.min_value = 0
    random_seed_socket.max_value = 2147483647
    random_seed_socket.subtype = 'NONE'
    random_seed_socket.attribute_domain = 'POINT'
    profile_p_circle_socket = peg.interface.new_socket(name = "profile_p_circle", in_out='INPUT', socket_type = 'NodeSocketFloat')
    profile_p_circle_socket.default_value = 0.3333333432674408
    profile_p_circle_socket.min_value = 0.0
    profile_p_circle_socket.max_value = 1.0
    profile_p_circle_socket.subtype = 'FACTOR'
    profile_p_circle_socket.attribute_domain = 'POINT'
    profile_n_vertices_circle_socket = peg.interface.new_socket(name = "profile_n_vertices_circle", in_out='INPUT', socket_type = 'NodeSocketInt')
    profile_n_vertices_circle_socket.default_value = 48
    profile_n_vertices_circle_socket.min_value = 3
    profile_n_vertices_circle_socket.max_value = 2147483647
    profile_n_vertices_circle_socket.subtype = 'NONE'
    profile_n_vertices_circle_socket.attribute_domain = 'POINT'
    profile_n_vertices_ngon_min_socket = peg.interface.new_socket(name = "profile_n_vertices_ngon_min", in_out='INPUT', socket_type = 'NodeSocketInt')
    profile_n_vertices_ngon_min_socket.default_value = 3
    profile_n_vertices_ngon_min_socket.min_value = 3
    profile_n_vertices_ngon_min_socket.max_value = 2147483647
    profile_n_vertices_ngon_min_socket.subtype = 'NONE'
    profile_n_vertices_ngon_min_socket.attribute_domain = 'POINT'
    profile_n_vertices_ngon_max_socket = peg.interface.new_socket(name = "profile_n_vertices_ngon_max", in_out='INPUT', socket_type = 'NodeSocketInt')
    profile_n_vertices_ngon_max_socket.default_value = 12
    profile_n_vertices_ngon_max_socket.min_value = 3
    profile_n_vertices_ngon_max_socket.max_value = 2147483647
    profile_n_vertices_ngon_max_socket.subtype = 'NONE'
    profile_n_vertices_ngon_max_socket.attribute_domain = 'POINT'
    radius_min_socket = peg.interface.new_socket(name = "radius_min", in_out='INPUT', socket_type = 'NodeSocketFloat')
    radius_min_socket.default_value = 0.009999999776482582
    radius_min_socket.min_value = 0.0
    radius_min_socket.max_value = 3.4028234663852886e+38
    radius_min_socket.subtype = 'DISTANCE'
    radius_min_socket.attribute_domain = 'POINT'
    radius_max_socket = peg.interface.new_socket(name = "radius_max", in_out='INPUT', socket_type = 'NodeSocketFloat')
    radius_max_socket.default_value = 0.02500000037252903
    radius_max_socket.min_value = 0.0
    radius_max_socket.max_value = 3.4028234663852886e+38
    radius_max_socket.subtype = 'DISTANCE'
    radius_max_socket.attribute_domain = 'POINT'
    height_min_socket = peg.interface.new_socket(name = "height_min", in_out='INPUT', socket_type = 'NodeSocketFloat')
    height_min_socket.default_value = 0.03999999910593033
    height_min_socket.min_value = 0.0
    height_min_socket.max_value = 3.4028234663852886e+38
    height_min_socket.subtype = 'DISTANCE'
    height_min_socket.attribute_domain = 'POINT'
    height_max_socket = peg.interface.new_socket(name = "height_max", in_out='INPUT', socket_type = 'NodeSocketFloat')
    height_max_socket.default_value = 0.07999999821186066
    height_max_socket.min_value = 0.0
    height_max_socket.max_value = 3.4028234663852886e+38
    height_max_socket.subtype = 'DISTANCE'
    height_max_socket.attribute_domain = 'POINT'
    aspect_ratio_min_socket = peg.interface.new_socket(name = "aspect_ratio_min", in_out='INPUT', socket_type = 'NodeSocketFloat')
    aspect_ratio_min_socket.default_value = 0.25
    aspect_ratio_min_socket.min_value = 0.0
    aspect_ratio_min_socket.max_value = 1.0
    aspect_ratio_min_socket.subtype = 'FACTOR'
    aspect_ratio_min_socket.attribute_domain = 'POINT'
    aspect_ratio_max_socket = peg.interface.new_socket(name = "aspect_ratio_max", in_out='INPUT', socket_type = 'NodeSocketFloat')
    aspect_ratio_max_socket.default_value = 1.0
    aspect_ratio_max_socket.min_value = 0.0
    aspect_ratio_max_socket.max_value = 1.0
    aspect_ratio_max_socket.subtype = 'FACTOR'
    aspect_ratio_max_socket.attribute_domain = 'POINT'
    taper_factor_min_socket = peg.interface.new_socket(name = "taper_factor_min", in_out='INPUT', socket_type = 'NodeSocketFloat')
    taper_factor_min_socket.default_value = 0.0
    taper_factor_min_socket.min_value = 0.0
    taper_factor_min_socket.max_value = 0.9990000128746033
    taper_factor_min_socket.subtype = 'FACTOR'
    taper_factor_min_socket.attribute_domain = 'POINT'
    taper_factor_max_socket = peg.interface.new_socket(name = "taper_factor_max", in_out='INPUT', socket_type = 'NodeSocketFloat')
    taper_factor_max_socket.default_value = 0.0
    taper_factor_max_socket.min_value = 0.0
    taper_factor_max_socket.max_value = 0.9990000128746033
    taper_factor_max_socket.subtype = 'FACTOR'
    taper_factor_max_socket.attribute_domain = 'POINT'
    use_uniform_geometry_socket = peg.interface.new_socket(name = "use_uniform_geometry", in_out='INPUT', socket_type = 'NodeSocketBool')
    use_uniform_geometry_socket.default_value = False
    use_uniform_geometry_socket.attribute_domain = 'POINT'
    frame_1 = peg.nodes.new("NodeFrame")
    frame_1.name = "Frame"
    frame_001_1 = peg.nodes.new("NodeFrame")
    frame_001_1.name = "Frame.001"
    frame_002_1 = peg.nodes.new("NodeFrame")
    frame_002_1.name = "Frame.002"
    frame_003_1 = peg.nodes.new("NodeFrame")
    frame_003_1.name = "Frame.003"
    frame_004_1 = peg.nodes.new("NodeFrame")
    frame_004_1.name = "Frame.004"
    frame_005_1 = peg.nodes.new("NodeFrame")
    frame_005_1.name = "Frame.005"
    frame_006_1 = peg.nodes.new("NodeFrame")
    frame_006_1.name = "Frame.006"
    switch = peg.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'INT'
    group_input_2 = peg.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"
    group_input_2.outputs[1].hide = True
    group_input_2.outputs[2].hide = True
    group_input_2.outputs[3].hide = True
    group_input_2.outputs[4].hide = True
    group_input_2.outputs[5].hide = True
    group_input_2.outputs[6].hide = True
    group_input_2.outputs[7].hide = True
    group_input_2.outputs[8].hide = True
    group_input_2.outputs[9].hide = True
    group_input_2.outputs[10].hide = True
    group_input_2.outputs[11].hide = True
    group_input_2.outputs[12].hide = True
    group_input_2.outputs[13].hide = True
    group_input_2.outputs[14].hide = True
    integer = peg.nodes.new("FunctionNodeInputInt")
    integer.name = "Integer"
    integer.integer = 0
    group_input_001 = peg.nodes.new("NodeGroupInput")
    group_input_001.name = "Group Input.001"
    group_input_001.outputs[0].hide = True
    group_input_001.outputs[2].hide = True
    group_input_001.outputs[3].hide = True
    group_input_001.outputs[4].hide = True
    group_input_001.outputs[5].hide = True
    group_input_001.outputs[6].hide = True
    group_input_001.outputs[7].hide = True
    group_input_001.outputs[8].hide = True
    group_input_001.outputs[9].hide = True
    group_input_001.outputs[10].hide = True
    group_input_001.outputs[11].hide = True
    group_input_001.outputs[12].hide = True
    group_input_001.outputs[13].hide = True
    group_input_001.outputs[14].hide = True
    random_value = peg.nodes.new("FunctionNodeRandomValue")
    random_value.name = "Random Value"
    random_value.data_type = 'BOOLEAN'
    group_input_002 = peg.nodes.new("NodeGroupInput")
    group_input_002.name = "Group Input.002"
    group_input_002.outputs[0].hide = True
    group_input_002.outputs[1].hide = True
    group_input_002.outputs[3].hide = True
    group_input_002.outputs[4].hide = True
    group_input_002.outputs[5].hide = True
    group_input_002.outputs[6].hide = True
    group_input_002.outputs[7].hide = True
    group_input_002.outputs[8].hide = True
    group_input_002.outputs[9].hide = True
    group_input_002.outputs[10].hide = True
    group_input_002.outputs[11].hide = True
    group_input_002.outputs[12].hide = True
    group_input_002.outputs[13].hide = True
    group_input_002.outputs[14].hide = True
    random_value_001 = peg.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = 'INT'
    group_input_003 = peg.nodes.new("NodeGroupInput")
    group_input_003.name = "Group Input.003"
    group_input_003.outputs[1].hide = True
    group_input_003.outputs[2].hide = True
    group_input_003.outputs[3].hide = True
    group_input_003.outputs[4].hide = True
    group_input_003.outputs[5].hide = True
    group_input_003.outputs[6].hide = True
    group_input_003.outputs[7].hide = True
    group_input_003.outputs[8].hide = True
    group_input_003.outputs[9].hide = True
    group_input_003.outputs[10].hide = True
    group_input_003.outputs[11].hide = True
    group_input_003.outputs[12].hide = True
    group_input_003.outputs[13].hide = True
    group_input_003.outputs[14].hide = True
    integer_001 = peg.nodes.new("FunctionNodeInputInt")
    integer_001.name = "Integer.001"
    integer_001.integer = 1
    group_input_004 = peg.nodes.new("NodeGroupInput")
    group_input_004.name = "Group Input.004"
    group_input_004.outputs[0].hide = True
    group_input_004.outputs[1].hide = True
    group_input_004.outputs[2].hide = True
    group_input_004.outputs[5].hide = True
    group_input_004.outputs[6].hide = True
    group_input_004.outputs[7].hide = True
    group_input_004.outputs[8].hide = True
    group_input_004.outputs[9].hide = True
    group_input_004.outputs[10].hide = True
    group_input_004.outputs[11].hide = True
    group_input_004.outputs[12].hide = True
    group_input_004.outputs[13].hide = True
    group_input_004.outputs[14].hide = True
    reroute_1 = peg.nodes.new("NodeReroute")
    reroute_1.name = "Reroute"
    reroute_1.socket_idname = "NodeSocketBool"
    math_2 = peg.nodes.new("ShaderNodeMath")
    math_2.name = "Math"
    math_2.operation = 'MULTIPLY'
    math_2.use_clamp = False
    math_2.inputs[0].hide = True
    math_2.inputs[2].hide = True
    math_2.inputs[0].default_value = -0.5
    combine_xyz_1 = peg.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_1.name = "Combine XYZ"
    combine_xyz_1.inputs[0].hide = True
    combine_xyz_1.inputs[1].hide = True
    combine_xyz_1.inputs[0].default_value = 0.0
    combine_xyz_1.inputs[1].default_value = 0.0
    scale_elements = peg.nodes.new("GeometryNodeScaleElements")
    scale_elements.name = "Scale Elements"
    scale_elements.domain = 'FACE'
    scale_elements.scale_mode = 'SINGLE_AXIS'
    scale_elements.inputs[1].default_value = True
    scale_elements.inputs[3].default_value = (0.0, 0.0, 0.0)
    integer_002 = peg.nodes.new("FunctionNodeInputInt")
    integer_002.name = "Integer.002"
    integer_002.integer = 5
    group_input_005 = peg.nodes.new("NodeGroupInput")
    group_input_005.name = "Group Input.005"
    group_input_005.outputs[1].hide = True
    group_input_005.outputs[2].hide = True
    group_input_005.outputs[3].hide = True
    group_input_005.outputs[4].hide = True
    group_input_005.outputs[5].hide = True
    group_input_005.outputs[6].hide = True
    group_input_005.outputs[7].hide = True
    group_input_005.outputs[8].hide = True
    group_input_005.outputs[9].hide = True
    group_input_005.outputs[10].hide = True
    group_input_005.outputs[11].hide = True
    group_input_005.outputs[12].hide = True
    group_input_005.outputs[13].hide = True
    group_input_005.outputs[14].hide = True
    random_value_002 = peg.nodes.new("FunctionNodeRandomValue")
    random_value_002.name = "Random Value.002"
    random_value_002.data_type = 'FLOAT'
    group_input_006 = peg.nodes.new("NodeGroupInput")
    group_input_006.name = "Group Input.006"
    group_input_006.outputs[1].hide = True
    group_input_006.outputs[2].hide = True
    group_input_006.outputs[3].hide = True
    group_input_006.outputs[4].hide = True
    group_input_006.outputs[5].hide = True
    group_input_006.outputs[6].hide = True
    group_input_006.outputs[7].hide = True
    group_input_006.outputs[8].hide = True
    group_input_006.outputs[9].hide = True
    group_input_006.outputs[10].hide = True
    group_input_006.outputs[11].hide = True
    group_input_006.outputs[12].hide = True
    group_input_006.outputs[13].hide = True
    group_input_006.outputs[14].hide = True
    random_value_003 = peg.nodes.new("FunctionNodeRandomValue")
    random_value_003.name = "Random Value.003"
    random_value_003.data_type = 'FLOAT_VECTOR'
    random_value_003.inputs[0].default_value = (-1.0, -1.0, 0.0)
    random_value_003.inputs[1].default_value = (1.0, 1.0, 0.0)
    group_input_007 = peg.nodes.new("NodeGroupInput")
    group_input_007.name = "Group Input.007"
    group_input_007.outputs[0].hide = True
    group_input_007.outputs[1].hide = True
    group_input_007.outputs[2].hide = True
    group_input_007.outputs[3].hide = True
    group_input_007.outputs[4].hide = True
    group_input_007.outputs[5].hide = True
    group_input_007.outputs[6].hide = True
    group_input_007.outputs[7].hide = True
    group_input_007.outputs[8].hide = True
    group_input_007.outputs[11].hide = True
    group_input_007.outputs[12].hide = True
    group_input_007.outputs[13].hide = True
    group_input_007.outputs[14].hide = True
    group_output_2 = peg.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True
    group_output_2.inputs[1].hide = True
    set_shade_smooth = peg.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    integer_003 = peg.nodes.new("FunctionNodeInputInt")
    integer_003.name = "Integer.003"
    integer_003.integer = 6
    transform_geometry = peg.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mute = True
    transform_geometry.mode = 'COMPONENTS'
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[3].hide = True
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)
    cone = peg.nodes.new("GeometryNodeMeshCone")
    cone.name = "Cone"
    cone.fill_type = 'NGON'
    group_input_008 = peg.nodes.new("NodeGroupInput")
    group_input_008.name = "Group Input.008"
    group_input_008.outputs[0].hide = True
    group_input_008.outputs[1].hide = True
    group_input_008.outputs[2].hide = True
    group_input_008.outputs[3].hide = True
    group_input_008.outputs[4].hide = True
    group_input_008.outputs[5].hide = True
    group_input_008.outputs[6].hide = True
    group_input_008.outputs[9].hide = True
    group_input_008.outputs[10].hide = True
    group_input_008.outputs[11].hide = True
    group_input_008.outputs[12].hide = True
    group_input_008.outputs[13].hide = True
    group_input_008.outputs[14].hide = True
    integer_004 = peg.nodes.new("FunctionNodeInputInt")
    integer_004.name = "Integer.004"
    integer_004.integer = 3
    group_input_009 = peg.nodes.new("NodeGroupInput")
    group_input_009.name = "Group Input.009"
    group_input_009.outputs[1].hide = True
    group_input_009.outputs[2].hide = True
    group_input_009.outputs[3].hide = True
    group_input_009.outputs[4].hide = True
    group_input_009.outputs[5].hide = True
    group_input_009.outputs[6].hide = True
    group_input_009.outputs[7].hide = True
    group_input_009.outputs[8].hide = True
    group_input_009.outputs[9].hide = True
    group_input_009.outputs[10].hide = True
    group_input_009.outputs[11].hide = True
    group_input_009.outputs[12].hide = True
    group_input_009.outputs[13].hide = True
    group_input_009.outputs[14].hide = True
    random_value_004 = peg.nodes.new("FunctionNodeRandomValue")
    random_value_004.name = "Random Value.004"
    random_value_004.data_type = 'FLOAT'
    group_input_010 = peg.nodes.new("NodeGroupInput")
    group_input_010.name = "Group Input.010"
    group_input_010.outputs[1].hide = True
    group_input_010.outputs[2].hide = True
    group_input_010.outputs[3].hide = True
    group_input_010.outputs[4].hide = True
    group_input_010.outputs[5].hide = True
    group_input_010.outputs[6].hide = True
    group_input_010.outputs[7].hide = True
    group_input_010.outputs[8].hide = True
    group_input_010.outputs[9].hide = True
    group_input_010.outputs[10].hide = True
    group_input_010.outputs[11].hide = True
    group_input_010.outputs[12].hide = True
    group_input_010.outputs[13].hide = True
    group_input_010.outputs[14].hide = True
    integer_005 = peg.nodes.new("FunctionNodeInputInt")
    integer_005.name = "Integer.005"
    integer_005.integer = 2
    group_input_011 = peg.nodes.new("NodeGroupInput")
    group_input_011.name = "Group Input.011"
    group_input_011.outputs[0].hide = True
    group_input_011.outputs[1].hide = True
    group_input_011.outputs[2].hide = True
    group_input_011.outputs[3].hide = True
    group_input_011.outputs[4].hide = True
    group_input_011.outputs[7].hide = True
    group_input_011.outputs[8].hide = True
    group_input_011.outputs[9].hide = True
    group_input_011.outputs[10].hide = True
    group_input_011.outputs[11].hide = True
    group_input_011.outputs[12].hide = True
    group_input_011.outputs[13].hide = True
    group_input_011.outputs[14].hide = True
    random_value_005 = peg.nodes.new("FunctionNodeRandomValue")
    random_value_005.name = "Random Value.005"
    random_value_005.data_type = 'FLOAT'
    math_001_2 = peg.nodes.new("ShaderNodeMath")
    math_001_2.name = "Math.001"
    math_001_2.operation = 'SUBTRACT'
    math_001_2.use_clamp = False
    math_001_2.inputs[0].default_value = 1.0
    math_002_1 = peg.nodes.new("ShaderNodeMath")
    math_002_1.name = "Math.002"
    math_002_1.operation = 'MULTIPLY'
    math_002_1.use_clamp = False
    group_input_012 = peg.nodes.new("NodeGroupInput")
    group_input_012.name = "Group Input.012"
    group_input_012.outputs[0].hide = True
    group_input_012.outputs[1].hide = True
    group_input_012.outputs[2].hide = True
    group_input_012.outputs[3].hide = True
    group_input_012.outputs[4].hide = True
    group_input_012.outputs[5].hide = True
    group_input_012.outputs[6].hide = True
    group_input_012.outputs[7].hide = True
    group_input_012.outputs[8].hide = True
    group_input_012.outputs[9].hide = True
    group_input_012.outputs[10].hide = True
    group_input_012.outputs[13].hide = True
    group_input_012.outputs[14].hide = True
    integer_006 = peg.nodes.new("FunctionNodeInputInt")
    integer_006.name = "Integer.006"
    integer_006.integer = 4
    group_input_013 = peg.nodes.new("NodeGroupInput")
    group_input_013.name = "Group Input.013"
    group_input_013.outputs[1].hide = True
    group_input_013.outputs[2].hide = True
    group_input_013.outputs[3].hide = True
    group_input_013.outputs[4].hide = True
    group_input_013.outputs[5].hide = True
    group_input_013.outputs[6].hide = True
    group_input_013.outputs[7].hide = True
    group_input_013.outputs[8].hide = True
    group_input_013.outputs[9].hide = True
    group_input_013.outputs[10].hide = True
    group_input_013.outputs[11].hide = True
    group_input_013.outputs[12].hide = True
    group_input_013.outputs[13].hide = True
    group_input_013.outputs[14].hide = True
    random_value_006 = peg.nodes.new("FunctionNodeRandomValue")
    random_value_006.name = "Random Value.006"
    random_value_006.data_type = 'FLOAT'
    reroute_001_1 = peg.nodes.new("NodeReroute")
    reroute_001_1.name = "Reroute.001"
    reroute_001_1.socket_idname = "NodeSocketFloat"
    reroute_002_1 = peg.nodes.new("NodeReroute")
    reroute_002_1.name = "Reroute.002"
    reroute_002_1.socket_idname = "NodeSocketInt"
    reroute_003_1 = peg.nodes.new("NodeReroute")
    reroute_003_1.name = "Reroute.003"
    reroute_003_1.socket_idname = "NodeSocketInt"
    reroute_004_1 = peg.nodes.new("NodeReroute")
    reroute_004_1.name = "Reroute.004"
    reroute_004_1.socket_idname = "NodeSocketFloat"
    reroute_005_1 = peg.nodes.new("NodeReroute")
    reroute_005_1.name = "Reroute.005"
    reroute_005_1.socket_idname = "NodeSocketFloat"
    reroute_006_1 = peg.nodes.new("NodeReroute")
    reroute_006_1.name = "Reroute.006"
    reroute_006_1.socket_idname = "NodeSocketFloat"
    math_003_1 = peg.nodes.new("ShaderNodeMath")
    math_003_1.name = "Math.003"
    math_003_1.operation = 'DIVIDE'
    math_003_1.use_clamp = False
    math_004_1 = peg.nodes.new("ShaderNodeMath")
    math_004_1.name = "Math.004"
    math_004_1.operation = 'DIVIDE'
    math_004_1.use_clamp = False
    math_005_1 = peg.nodes.new("ShaderNodeMath")
    math_005_1.name = "Math.005"
    math_005_1.operation = 'CEIL'
    math_005_1.use_clamp = False
    switch_001 = peg.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.input_type = 'INT'
    switch_001.inputs[1].default_value = 1
    math_006 = peg.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'CEIL'
    math_006.use_clamp = False
    group_input_014 = peg.nodes.new("NodeGroupInput")
    group_input_014.name = "Group Input.014"
    group_input_014.outputs[0].hide = True
    group_input_014.outputs[1].hide = True
    group_input_014.outputs[2].hide = True
    group_input_014.outputs[3].hide = True
    group_input_014.outputs[4].hide = True
    group_input_014.outputs[5].hide = True
    group_input_014.outputs[6].hide = True
    group_input_014.outputs[7].hide = True
    group_input_014.outputs[8].hide = True
    group_input_014.outputs[9].hide = True
    group_input_014.outputs[10].hide = True
    group_input_014.outputs[11].hide = True
    group_input_014.outputs[12].hide = True
    group_input_014.outputs[14].hide = True
    switch_002 = peg.nodes.new("GeometryNodeSwitch")
    switch_002.name = "Switch.002"
    switch_002.input_type = 'INT'
    switch_002.inputs[1].default_value = 1
    math_007 = peg.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = 'MULTIPLY'
    math_007.use_clamp = False
    math_007.inputs[1].default_value = 6.2831854820251465
    math_008 = peg.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = 'DIVIDE'
    math_008.use_clamp = False
    reroute_007_1 = peg.nodes.new("NodeReroute")
    reroute_007_1.name = "Reroute.007"
    reroute_007_1.socket_idname = "NodeSocketFloat"
    reroute_008 = peg.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.socket_idname = "NodeSocketFloat"
    set_material = peg.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.inputs[1].default_value = True
    frame_1.width, frame_1.height = 150.0, 100.0
    frame_001_1.width, frame_001_1.height = 150.0, 100.0
    frame_002_1.width, frame_002_1.height = 150.0, 100.0
    frame_003_1.width, frame_003_1.height = 150.0, 100.0
    frame_004_1.width, frame_004_1.height = 150.0, 100.0
    frame_005_1.width, frame_005_1.height = 150.0, 100.0
    frame_006_1.width, frame_006_1.height = 150.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    group_input_2.width, group_input_2.height = 140.0, 100.0
    integer.width, integer.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    random_value.width, random_value.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    random_value_001.width, random_value_001.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    integer_001.width, integer_001.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    reroute_1.width, reroute_1.height = 140.0, 100.0
    math_2.width, math_2.height = 140.0, 100.0
    combine_xyz_1.width, combine_xyz_1.height = 140.0, 100.0
    scale_elements.width, scale_elements.height = 140.0, 100.0
    integer_002.width, integer_002.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    random_value_002.width, random_value_002.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    random_value_003.width, random_value_003.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    group_output_2.width, group_output_2.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    integer_003.width, integer_003.height = 140.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    cone.width, cone.height = 140.0, 100.0
    group_input_008.width, group_input_008.height = 140.0, 100.0
    integer_004.width, integer_004.height = 140.0, 100.0
    group_input_009.width, group_input_009.height = 140.0, 100.0
    random_value_004.width, random_value_004.height = 140.0, 100.0
    group_input_010.width, group_input_010.height = 140.0, 100.0
    integer_005.width, integer_005.height = 140.0, 100.0
    group_input_011.width, group_input_011.height = 140.0, 100.0
    random_value_005.width, random_value_005.height = 140.0, 100.0
    math_001_2.width, math_001_2.height = 140.0, 100.0
    math_002_1.width, math_002_1.height = 140.0, 100.0
    group_input_012.width, group_input_012.height = 140.0, 100.0
    integer_006.width, integer_006.height = 140.0, 100.0
    group_input_013.width, group_input_013.height = 140.0, 100.0
    random_value_006.width, random_value_006.height = 140.0, 100.0
    reroute_001_1.width, reroute_001_1.height = 140.0, 100.0
    reroute_002_1.width, reroute_002_1.height = 140.0, 100.0
    reroute_003_1.width, reroute_003_1.height = 140.0, 100.0
    reroute_004_1.width, reroute_004_1.height = 140.0, 100.0
    reroute_005_1.width, reroute_005_1.height = 140.0, 100.0
    reroute_006_1.width, reroute_006_1.height = 140.0, 100.0
    math_003_1.width, math_003_1.height = 140.0, 100.0
    math_004_1.width, math_004_1.height = 140.0, 100.0
    math_005_1.width, math_005_1.height = 140.0, 100.0
    switch_001.width, switch_001.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    group_input_014.width, group_input_014.height = 140.0, 100.0
    switch_002.width, switch_002.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    reroute_007_1.width, reroute_007_1.height = 140.0, 100.0
    reroute_008.width, reroute_008.height = 140.0, 100.0
    set_material.width, set_material.height = 140.0, 100.0
    peg.links.new(group_input_003.outputs[0], random_value_001.inputs[8])
    peg.links.new(integer_001.outputs[0], random_value_001.inputs[7])
    peg.links.new(group_input_2.outputs[0], random_value.inputs[8])
    peg.links.new(integer.outputs[0], random_value.inputs[7])
    peg.links.new(random_value_001.outputs[2], switch.inputs[1])
    peg.links.new(random_value.outputs[3], switch.inputs[0])
    peg.links.new(integer_005.outputs[0], random_value_006.inputs[7])
    peg.links.new(group_input_010.outputs[0], random_value_006.inputs[8])
    peg.links.new(integer_004.outputs[0], random_value_004.inputs[7])
    peg.links.new(group_input_009.outputs[0], random_value_004.inputs[8])
    peg.links.new(group_input_011.outputs[5], random_value_006.inputs[2])
    peg.links.new(group_input_008.outputs[7], random_value_004.inputs[2])
    peg.links.new(group_input_002.outputs[2], switch.inputs[2])
    peg.links.new(group_input_001.outputs[1], random_value.inputs[6])
    peg.links.new(group_input_004.outputs[3], random_value_001.inputs[4])
    peg.links.new(random_value.outputs[3], reroute_1.inputs[0])
    peg.links.new(reroute_1.outputs[0], set_shade_smooth.inputs[2])
    peg.links.new(transform_geometry.outputs[0], set_shade_smooth.inputs[0])
    peg.links.new(math_001_2.outputs[0], math_002_1.inputs[1])
    peg.links.new(math_002_1.outputs[0], cone.inputs[4])
    peg.links.new(cone.outputs[3], set_shade_smooth.inputs[1])
    peg.links.new(cone.outputs[0], transform_geometry.inputs[0])
    peg.links.new(combine_xyz_1.outputs[0], transform_geometry.inputs[1])
    peg.links.new(math_2.outputs[0], combine_xyz_1.inputs[2])
    peg.links.new(random_value_004.outputs[1], reroute_004_1.inputs[0])
    peg.links.new(reroute_005_1.outputs[0], math_2.inputs[1])
    peg.links.new(reroute_005_1.outputs[0], cone.inputs[5])
    peg.links.new(reroute_006_1.outputs[0], cone.inputs[3])
    peg.links.new(random_value_006.outputs[1], reroute_001_1.inputs[0])
    peg.links.new(switch.outputs[0], reroute_003_1.inputs[0])
    peg.links.new(reroute_002_1.outputs[0], cone.inputs[0])
    peg.links.new(reroute_006_1.outputs[0], math_002_1.inputs[0])
    peg.links.new(set_material.outputs[0], group_output_2.inputs[0])
    peg.links.new(integer_002.outputs[0], random_value_002.inputs[7])
    peg.links.new(group_input_005.outputs[0], random_value_002.inputs[8])
    peg.links.new(group_input_007.outputs[9], random_value_002.inputs[2])
    peg.links.new(group_input_007.outputs[10], random_value_002.inputs[3])
    peg.links.new(group_input_008.outputs[8], random_value_004.inputs[3])
    peg.links.new(group_input_011.outputs[6], random_value_006.inputs[3])
    peg.links.new(group_input_004.outputs[4], random_value_001.inputs[5])
    peg.links.new(set_shade_smooth.outputs[0], scale_elements.inputs[0])
    peg.links.new(random_value_002.outputs[1], scale_elements.inputs[2])
    peg.links.new(integer_003.outputs[0], random_value_003.inputs[7])
    peg.links.new(group_input_006.outputs[0], random_value_003.inputs[8])
    peg.links.new(random_value_003.outputs[0], scale_elements.inputs[4])
    peg.links.new(integer_006.outputs[0], random_value_005.inputs[7])
    peg.links.new(group_input_013.outputs[0], random_value_005.inputs[8])
    peg.links.new(group_input_012.outputs[11], random_value_005.inputs[2])
    peg.links.new(group_input_012.outputs[12], random_value_005.inputs[3])
    peg.links.new(random_value_005.outputs[1], math_001_2.inputs[1])
    peg.links.new(reroute_001_1.outputs[0], reroute_006_1.inputs[0])
    peg.links.new(reroute_007_1.outputs[0], math_008.inputs[0])
    peg.links.new(reroute_003_1.outputs[0], math_008.inputs[1])
    peg.links.new(reroute_005_1.outputs[0], math_003_1.inputs[0])
    peg.links.new(reroute_008.outputs[0], math_003_1.inputs[1])
    peg.links.new(math_003_1.outputs[0], math_005_1.inputs[0])
    peg.links.new(switch_001.outputs[0], cone.inputs[1])
    peg.links.new(reroute_008.outputs[0], math_004_1.inputs[1])
    peg.links.new(math_004_1.outputs[0], math_006.inputs[0])
    peg.links.new(math_005_1.outputs[0], switch_001.inputs[2])
    peg.links.new(math_006.outputs[0], switch_002.inputs[2])
    peg.links.new(switch_002.outputs[0], cone.inputs[2])
    peg.links.new(group_input_014.outputs[13], switch_001.inputs[0])
    peg.links.new(group_input_014.outputs[13], switch_002.inputs[0])
    peg.links.new(reroute_003_1.outputs[0], reroute_002_1.inputs[0])
    peg.links.new(math_007.outputs[0], reroute_007_1.inputs[0])
    peg.links.new(reroute_006_1.outputs[0], math_007.inputs[0])
    peg.links.new(reroute_006_1.outputs[0], math_004_1.inputs[0])
    peg.links.new(reroute_004_1.outputs[0], reroute_005_1.inputs[0])
    peg.links.new(math_008.outputs[0], reroute_008.inputs[0])
    peg.links.new(scale_elements.outputs[0], set_material.inputs[0])
    return peg

peg = peg_node_group()

def hole_node_group():
    hole = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Hole")
    hole.color_tag = 'NONE'
    hole.default_group_node_width = 140
    hole.is_modifier = True
    geometry_socket_3 = hole.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_3.attribute_domain = 'POINT'
    entrance_position_socket = hole.interface.new_socket(name = "entrance_position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
    entrance_position_socket.default_value = (0.0, 0.0, 0.0)
    entrance_position_socket.min_value = -3.4028234663852886e+38
    entrance_position_socket.max_value = 3.4028234663852886e+38
    entrance_position_socket.subtype = 'XYZ'
    entrance_position_socket.attribute_domain = 'POINT'
    entrance_orientation_socket = hole.interface.new_socket(name = "entrance_orientation", in_out='OUTPUT', socket_type = 'NodeSocketVector')
    entrance_orientation_socket.default_value = (0.0, 0.0, 0.0)
    entrance_orientation_socket.min_value = -3.4028234663852886e+38
    entrance_orientation_socket.max_value = 3.4028234663852886e+38
    entrance_orientation_socket.subtype = 'EULER'
    entrance_orientation_socket.attribute_domain = 'POINT'
    bottom_position_socket = hole.interface.new_socket(name = "bottom_position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
    bottom_position_socket.default_value = (0.0, 0.0, 0.0)
    bottom_position_socket.min_value = -3.4028234663852886e+38
    bottom_position_socket.max_value = 3.4028234663852886e+38
    bottom_position_socket.subtype = 'XYZ'
    bottom_position_socket.attribute_domain = 'POINT'
    bottom_orientation_socket = hole.interface.new_socket(name = "bottom_orientation", in_out='OUTPUT', socket_type = 'NodeSocketVector')
    bottom_orientation_socket.default_value = (0.0, 0.0, 0.0)
    bottom_orientation_socket.min_value = -3.4028234663852886e+38
    bottom_orientation_socket.max_value = 3.4028234663852886e+38
    bottom_orientation_socket.subtype = 'EULER'
    bottom_orientation_socket.attribute_domain = 'POINT'
    geometry_socket_4 = hole.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_4.attribute_domain = 'POINT'
    random_seed_socket_1 = hole.interface.new_socket(name = "random_seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    random_seed_socket_1.default_value = 0
    random_seed_socket_1.min_value = 0
    random_seed_socket_1.max_value = 2147483647
    random_seed_socket_1.subtype = 'NONE'
    random_seed_socket_1.attribute_domain = 'POINT'
    peg_socket = hole.interface.new_socket(name = "peg", in_out='INPUT', socket_type = 'NodeSocketObject')
    peg_socket.attribute_domain = 'POINT'
    hole_position_handle_socket = hole.interface.new_socket(name = "hole_position_handle", in_out='INPUT', socket_type = 'NodeSocketObject')
    hole_position_handle_socket.attribute_domain = 'POINT'
    hole_position_offset_min_socket = hole.interface.new_socket(name = "hole_position_offset_min", in_out='INPUT', socket_type = 'NodeSocketVector')
    hole_position_offset_min_socket.default_value = (-0.05000000074505806, -0.05000000074505806, -0.05000000074505806)
    hole_position_offset_min_socket.min_value = -3.4028234663852886e+38
    hole_position_offset_min_socket.max_value = 3.4028234663852886e+38
    hole_position_offset_min_socket.subtype = 'TRANSLATION'
    hole_position_offset_min_socket.attribute_domain = 'POINT'
    hole_position_offset_max_socket = hole.interface.new_socket(name = "hole_position_offset_max", in_out='INPUT', socket_type = 'NodeSocketVector')
    hole_position_offset_max_socket.default_value = (0.05000000074505806, 0.05000000074505806, 0.05000000074505806)
    hole_position_offset_max_socket.min_value = -3.4028234663852886e+38
    hole_position_offset_max_socket.max_value = 3.4028234663852886e+38
    hole_position_offset_max_socket.subtype = 'TRANSLATION'
    hole_position_offset_max_socket.attribute_domain = 'POINT'
    hole_orientation_offset_min_socket = hole.interface.new_socket(name = "hole_orientation_offset_min", in_out='INPUT', socket_type = 'NodeSocketVector')
    hole_orientation_offset_min_socket.default_value = (-0.34906598925590515, -0.34906598925590515, -3.1415927410125732)
    hole_orientation_offset_min_socket.min_value = -3.4028234663852886e+38
    hole_orientation_offset_min_socket.max_value = 3.4028234663852886e+38
    hole_orientation_offset_min_socket.subtype = 'EULER'
    hole_orientation_offset_min_socket.attribute_domain = 'POINT'
    hole_orientation_offset_max_socket = hole.interface.new_socket(name = "hole_orientation_offset_max", in_out='INPUT', socket_type = 'NodeSocketVector')
    hole_orientation_offset_max_socket.default_value = (0.34906598925590515, 0.34906598925590515, 3.1415927410125732)
    hole_orientation_offset_max_socket.min_value = -3.4028234663852886e+38
    hole_orientation_offset_max_socket.max_value = 3.4028234663852886e+38
    hole_orientation_offset_max_socket.subtype = 'EULER'
    hole_orientation_offset_max_socket.attribute_domain = 'POINT'
    hole_insertion_angle_min_socket = hole.interface.new_socket(name = "hole_insertion_angle_min", in_out='INPUT', socket_type = 'NodeSocketFloat')
    hole_insertion_angle_min_socket.default_value = 0.0
    hole_insertion_angle_min_socket.min_value = -3.4028234663852886e+38
    hole_insertion_angle_min_socket.max_value = 3.4028234663852886e+38
    hole_insertion_angle_min_socket.subtype = 'ANGLE'
    hole_insertion_angle_min_socket.attribute_domain = 'POINT'
    hole_insertion_angle_max_socket = hole.interface.new_socket(name = "hole_insertion_angle_max", in_out='INPUT', socket_type = 'NodeSocketFloat')
    hole_insertion_angle_max_socket.default_value = 6.2831854820251465
    hole_insertion_angle_max_socket.min_value = -3.4028234663852886e+38
    hole_insertion_angle_max_socket.max_value = 3.4028234663852886e+38
    hole_insertion_angle_max_socket.subtype = 'ANGLE'
    hole_insertion_angle_max_socket.attribute_domain = 'POINT'
    hole_depth_factor_min_socket = hole.interface.new_socket(name = "hole_depth_factor_min", in_out='INPUT', socket_type = 'NodeSocketFloat')
    hole_depth_factor_min_socket.default_value = 0.25
    hole_depth_factor_min_socket.min_value = 0.0
    hole_depth_factor_min_socket.max_value = 1.0
    hole_depth_factor_min_socket.subtype = 'FACTOR'
    hole_depth_factor_min_socket.attribute_domain = 'POINT'
    hole_depth_factor_max_socket = hole.interface.new_socket(name = "hole_depth_factor_max", in_out='INPUT', socket_type = 'NodeSocketFloat')
    hole_depth_factor_max_socket.default_value = 0.75
    hole_depth_factor_max_socket.min_value = 0.0
    hole_depth_factor_max_socket.max_value = 1.0
    hole_depth_factor_max_socket.subtype = 'FACTOR'
    hole_depth_factor_max_socket.attribute_domain = 'POINT'
    hole_size_tolerance_socket = hole.interface.new_socket(name = "hole_size_tolerance", in_out='INPUT', socket_type = 'NodeSocketFloat')
    hole_size_tolerance_socket.default_value = 0.0010000000474974513
    hole_size_tolerance_socket.min_value = 0.0
    hole_size_tolerance_socket.max_value = 3.4028234663852886e+38
    hole_size_tolerance_socket.subtype = 'DISTANCE'
    hole_size_tolerance_socket.attribute_domain = 'POINT'
    wall_enable_socket = hole.interface.new_socket(name = "wall_enable", in_out='INPUT', socket_type = 'NodeSocketBool')
    wall_enable_socket.default_value = True
    wall_enable_socket.attribute_domain = 'POINT'
    wall_remove_inner_holes_socket = hole.interface.new_socket(name = "wall_remove_inner_holes", in_out='INPUT', socket_type = 'NodeSocketBool')
    wall_remove_inner_holes_socket.default_value = False
    wall_remove_inner_holes_socket.attribute_domain = 'POINT'
    wall_thickness_socket = hole.interface.new_socket(name = "wall_thickness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    wall_thickness_socket.default_value = 0.005000000353902578
    wall_thickness_socket.min_value = 9.999999747378752e-05
    wall_thickness_socket.max_value = 10000.0
    wall_thickness_socket.subtype = 'DISTANCE'
    wall_thickness_socket.attribute_domain = 'POINT'
    wall_include_bottom_socket = hole.interface.new_socket(name = "wall_include_bottom", in_out='INPUT', socket_type = 'NodeSocketBool')
    wall_include_bottom_socket.default_value = True
    wall_include_bottom_socket.attribute_domain = 'POINT'
    frame_001_2 = hole.nodes.new("NodeFrame")
    frame_001_2.name = "Frame.001"
    frame_001_2.use_custom_color = True
    frame_001_2.color = (0.1600000113248825, 0.17599999904632568, 0.20000000298023224)
    frame_002_2 = hole.nodes.new("NodeFrame")
    frame_002_2.name = "Frame.002"
    frame_002_2.use_custom_color = True
    frame_002_2.color = (0.16862745583057404, 0.20000001788139343, 0.16078431904315948)
    frame_003_2 = hole.nodes.new("NodeFrame")
    frame_003_2.name = "Frame.003"
    frame_004_2 = hole.nodes.new("NodeFrame")
    frame_004_2.name = "Frame.004"
    frame_005_2 = hole.nodes.new("NodeFrame")
    frame_005_2.name = "Frame.005"
    frame_006_2 = hole.nodes.new("NodeFrame")
    frame_006_2.name = "Frame.006"
    frame_007_1 = hole.nodes.new("NodeFrame")
    frame_007_1.name = "Frame.007"
    frame_008_1 = hole.nodes.new("NodeFrame")
    frame_008_1.name = "Frame.008"
    frame_009 = hole.nodes.new("NodeFrame")
    frame_009.name = "Frame.009"
    frame_010 = hole.nodes.new("NodeFrame")
    frame_010.name = "Frame.010"
    frame_011 = hole.nodes.new("NodeFrame")
    frame_011.name = "Frame.011"
    frame_012 = hole.nodes.new("NodeFrame")
    frame_012.name = "Frame.012"
    frame_013 = hole.nodes.new("NodeFrame")
    frame_013.name = "Frame.013"
    frame_014 = hole.nodes.new("NodeFrame")
    frame_014.name = "Frame.014"
    frame_2 = hole.nodes.new("NodeFrame")
    frame_2.name = "Frame"
    reroute_2 = hole.nodes.new("NodeReroute")
    reroute_2.name = "Reroute"
    reroute_2.socket_idname = "NodeSocketVector"
    reroute_001_2 = hole.nodes.new("NodeReroute")
    reroute_001_2.name = "Reroute.001"
    reroute_001_2.socket_idname = "NodeSocketVector"
    reroute_002_2 = hole.nodes.new("NodeReroute")
    reroute_002_2.name = "Reroute.002"
    reroute_002_2.socket_idname = "NodeSocketVector"
    reroute_003_2 = hole.nodes.new("NodeReroute")
    reroute_003_2.name = "Reroute.003"
    reroute_003_2.socket_idname = "NodeSocketVector"
    reroute_006_2 = hole.nodes.new("NodeReroute")
    reroute_006_2.name = "Reroute.006"
    reroute_006_2.socket_idname = "NodeSocketVector"
    reroute_007_2 = hole.nodes.new("NodeReroute")
    reroute_007_2.name = "Reroute.007"
    reroute_007_2.socket_idname = "NodeSocketVector"
    reroute_008_1 = hole.nodes.new("NodeReroute")
    reroute_008_1.name = "Reroute.008"
    reroute_008_1.socket_idname = "NodeSocketVector"
    group_input_001_1 = hole.nodes.new("NodeGroupInput")
    group_input_001_1.name = "Group Input.001"
    group_input_001_1.outputs[0].hide = True
    group_input_001_1.outputs[1].hide = True
    group_input_001_1.outputs[3].hide = True
    group_input_001_1.outputs[4].hide = True
    group_input_001_1.outputs[5].hide = True
    group_input_001_1.outputs[6].hide = True
    group_input_001_1.outputs[7].hide = True
    group_input_001_1.outputs[8].hide = True
    group_input_001_1.outputs[9].hide = True
    group_input_001_1.outputs[10].hide = True
    group_input_001_1.outputs[11].hide = True
    group_input_001_1.outputs[12].hide = True
    group_input_001_1.outputs[13].hide = True
    group_input_001_1.outputs[14].hide = True
    group_input_001_1.outputs[15].hide = True
    group_input_001_1.outputs[16].hide = True
    group_input_001_1.outputs[17].hide = True
    position_1 = hole.nodes.new("GeometryNodeInputPosition")
    position_1.name = "Position"
    object_info = hole.nodes.new("GeometryNodeObjectInfo")
    object_info.name = "Object Info"
    object_info.transform_space = 'ORIGINAL'
    object_info.inputs[1].hide = True
    object_info.outputs[1].hide = True
    object_info.outputs[2].hide = True
    object_info.outputs[3].hide = True
    object_info.inputs[1].default_value = False
    attribute_statistic = hole.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic.name = "Attribute Statistic"
    attribute_statistic.data_type = 'FLOAT_VECTOR'
    attribute_statistic.domain = 'POINT'
    attribute_statistic.inputs[1].hide = True
    attribute_statistic.outputs[0].hide = True
    attribute_statistic.outputs[1].hide = True
    attribute_statistic.outputs[2].hide = True
    attribute_statistic.outputs[4].hide = True
    attribute_statistic.outputs[6].hide = True
    attribute_statistic.outputs[7].hide = True
    attribute_statistic.inputs[1].default_value = True
    vector_math_2 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_2.name = "Vector Math"
    vector_math_2.operation = 'MULTIPLY'
    vector_math_2.inputs[1].default_value = (0.0, 0.0, -1.0)
    align_euler_to_vector = hole.nodes.new("FunctionNodeAlignEulerToVector")
    align_euler_to_vector.name = "Align Euler to Vector"
    align_euler_to_vector.axis = 'Z'
    align_euler_to_vector.pivot_axis = 'AUTO'
    align_euler_to_vector.inputs[0].hide = True
    align_euler_to_vector.inputs[1].hide = True
    align_euler_to_vector.inputs[0].default_value = (0.0, 0.0, 0.0)
    align_euler_to_vector.inputs[1].default_value = 1.0
    reroute_009 = hole.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.socket_idname = "NodeSocketVector"
    separate_xyz_1 = hole.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_1.name = "Separate XYZ"
    separate_xyz_1.outputs[0].hide = True
    separate_xyz_1.outputs[1].hide = True
    vector_rotate = hole.nodes.new("ShaderNodeVectorRotate")
    vector_rotate.name = "Vector Rotate"
    vector_rotate.invert = False
    vector_rotate.rotation_type = 'EULER_XYZ'
    vector_rotate.inputs[1].hide = True
    vector_rotate.inputs[2].hide = True
    vector_rotate.inputs[3].hide = True
    vector_rotate.inputs[1].default_value = (0.0, 0.0, 0.0)
    vector_math_001_2 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_001_2.name = "Vector Math.001"
    vector_math_001_2.operation = 'ADD'
    reroute_010 = hole.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.socket_idname = "NodeSocketFloat"
    transform_geometry_1 = hole.nodes.new("GeometryNodeTransform")
    transform_geometry_1.name = "Transform Geometry"
    transform_geometry_1.mode = 'COMPONENTS'
    transform_geometry_1.inputs[3].hide = True
    transform_geometry_1.inputs[3].default_value = (1.0, 1.0, 1.0)
    group_input_002_1 = hole.nodes.new("NodeGroupInput")
    group_input_002_1.name = "Group Input.002"
    group_input_002_1.outputs[0].hide = True
    group_input_002_1.outputs[2].hide = True
    group_input_002_1.outputs[3].hide = True
    group_input_002_1.outputs[4].hide = True
    group_input_002_1.outputs[5].hide = True
    group_input_002_1.outputs[6].hide = True
    group_input_002_1.outputs[7].hide = True
    group_input_002_1.outputs[8].hide = True
    group_input_002_1.outputs[9].hide = True
    group_input_002_1.outputs[10].hide = True
    group_input_002_1.outputs[11].hide = True
    group_input_002_1.outputs[12].hide = True
    group_input_002_1.outputs[13].hide = True
    group_input_002_1.outputs[14].hide = True
    group_input_002_1.outputs[15].hide = True
    group_input_002_1.outputs[16].hide = True
    group_input_002_1.outputs[17].hide = True
    random_value_1 = hole.nodes.new("FunctionNodeRandomValue")
    random_value_1.name = "Random Value"
    random_value_1.data_type = 'FLOAT'
    group_input_003_1 = hole.nodes.new("NodeGroupInput")
    group_input_003_1.name = "Group Input.003"
    group_input_003_1.outputs[0].hide = True
    group_input_003_1.outputs[1].hide = True
    group_input_003_1.outputs[2].hide = True
    group_input_003_1.outputs[3].hide = True
    group_input_003_1.outputs[4].hide = True
    group_input_003_1.outputs[5].hide = True
    group_input_003_1.outputs[6].hide = True
    group_input_003_1.outputs[7].hide = True
    group_input_003_1.outputs[8].hide = True
    group_input_003_1.outputs[9].hide = True
    group_input_003_1.outputs[12].hide = True
    group_input_003_1.outputs[13].hide = True
    group_input_003_1.outputs[14].hide = True
    group_input_003_1.outputs[15].hide = True
    group_input_003_1.outputs[16].hide = True
    group_input_003_1.outputs[17].hide = True
    integer_1 = hole.nodes.new("FunctionNodeInputInt")
    integer_1.name = "Integer"
    integer_1.integer = 3
    reroute_011 = hole.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    reroute_011.socket_idname = "NodeSocketGeometry"
    math_3 = hole.nodes.new("ShaderNodeMath")
    math_3.name = "Math"
    math_3.operation = 'MULTIPLY'
    math_3.use_clamp = False
    transform_geometry_001 = hole.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    transform_geometry_001.inputs[2].hide = True
    transform_geometry_001.inputs[3].hide = True
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
    capture_attribute = hole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute.name = "Capture Attribute"
    capture_attribute.active_index = 0
    capture_attribute.capture_items.clear()
    capture_attribute.capture_items.new('FLOAT', "Value")
    capture_attribute.capture_items["Value"].data_type = 'FLOAT_VECTOR'
    capture_attribute.domain = 'FACE'
    normal_1 = hole.nodes.new("GeometryNodeInputNormal")
    normal_1.name = "Normal"
    reroute_012 = hole.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.socket_idname = "NodeSocketGeometry"
    vector_math_003 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = 'NORMALIZE'
    vector_math_004 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.operation = 'SCALE'
    vector_math_005 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_005.name = "Vector Math.005"
    vector_math_005.operation = 'DOT_PRODUCT'
    reroute_013 = hole.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.socket_idname = "NodeSocketVector"
    normal_001_1 = hole.nodes.new("GeometryNodeInputNormal")
    normal_001_1.name = "Normal.001"
    math_001_3 = hole.nodes.new("ShaderNodeMath")
    math_001_3.name = "Math.001"
    math_001_3.operation = 'MULTIPLY'
    math_001_3.use_clamp = False
    math_001_3.inputs[1].default_value = 0.5
    vector_math_006 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_006.name = "Vector Math.006"
    vector_math_006.operation = 'SUBTRACT'
    group_input_004_1 = hole.nodes.new("NodeGroupInput")
    group_input_004_1.name = "Group Input.004"
    group_input_004_1.outputs[0].hide = True
    group_input_004_1.outputs[1].hide = True
    group_input_004_1.outputs[2].hide = True
    group_input_004_1.outputs[3].hide = True
    group_input_004_1.outputs[4].hide = True
    group_input_004_1.outputs[5].hide = True
    group_input_004_1.outputs[6].hide = True
    group_input_004_1.outputs[7].hide = True
    group_input_004_1.outputs[8].hide = True
    group_input_004_1.outputs[9].hide = True
    group_input_004_1.outputs[10].hide = True
    group_input_004_1.outputs[11].hide = True
    group_input_004_1.outputs[13].hide = True
    group_input_004_1.outputs[14].hide = True
    group_input_004_1.outputs[15].hide = True
    group_input_004_1.outputs[16].hide = True
    group_input_004_1.outputs[17].hide = True
    vector_math_007 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_007.name = "Vector Math.007"
    vector_math_007.operation = 'SCALE'
    capture_attribute_001 = hole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_001.name = "Capture Attribute.001"
    capture_attribute_001.active_index = 0
    capture_attribute_001.capture_items.clear()
    capture_attribute_001.capture_items.new('FLOAT', "Value")
    capture_attribute_001.capture_items["Value"].data_type = 'FLOAT_VECTOR'
    capture_attribute_001.domain = 'FACE'
    vector_rotate_001 = hole.nodes.new("ShaderNodeVectorRotate")
    vector_rotate_001.name = "Vector Rotate.001"
    vector_rotate_001.invert = False
    vector_rotate_001.rotation_type = 'EULER_XYZ'
    vector_math_008 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_008.name = "Vector Math.008"
    vector_math_008.operation = 'ADD'
    vector_math_009 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_009.name = "Vector Math.009"
    vector_math_009.operation = 'ADD'
    reroute_014 = hole.nodes.new("NodeReroute")
    reroute_014.name = "Reroute.014"
    reroute_014.socket_idname = "NodeSocketVectorEuler"
    group_input_005_1 = hole.nodes.new("NodeGroupInput")
    group_input_005_1.name = "Group Input.005"
    group_input_005_1.outputs[0].hide = True
    group_input_005_1.outputs[1].hide = True
    group_input_005_1.outputs[2].hide = True
    group_input_005_1.outputs[4].hide = True
    group_input_005_1.outputs[5].hide = True
    group_input_005_1.outputs[6].hide = True
    group_input_005_1.outputs[7].hide = True
    group_input_005_1.outputs[8].hide = True
    group_input_005_1.outputs[9].hide = True
    group_input_005_1.outputs[10].hide = True
    group_input_005_1.outputs[11].hide = True
    group_input_005_1.outputs[12].hide = True
    group_input_005_1.outputs[13].hide = True
    group_input_005_1.outputs[14].hide = True
    group_input_005_1.outputs[15].hide = True
    group_input_005_1.outputs[16].hide = True
    group_input_005_1.outputs[17].hide = True
    object_info_001 = hole.nodes.new("GeometryNodeObjectInfo")
    object_info_001.name = "Object Info.001"
    object_info_001.transform_space = 'RELATIVE'
    object_info_001.inputs[1].hide = True
    object_info_001.outputs[3].hide = True
    object_info_001.outputs[4].hide = True
    object_info_001.inputs[1].default_value = False
    vector_math_010 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_010.name = "Vector Math.010"
    vector_math_010.operation = 'MULTIPLY'
    vector_math_011 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_011.name = "Vector Math.011"
    vector_math_011.operation = 'MULTIPLY'
    combine_xyz_2 = hole.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_2.name = "Combine XYZ"
    combine_xyz_2.inputs[0].hide = True
    combine_xyz_2.inputs[2].hide = True
    combine_xyz_2.inputs[0].default_value = 0.0
    combine_xyz_2.inputs[2].default_value = 0.0
    combine_xyz_001 = hole.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    combine_xyz_001.inputs[1].hide = True
    combine_xyz_001.inputs[2].hide = True
    combine_xyz_001.inputs[1].default_value = 0.0
    combine_xyz_001.inputs[2].default_value = 0.0
    separate_xyz_001 = hole.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"
    integer_001_1 = hole.nodes.new("FunctionNodeInputInt")
    integer_001_1.name = "Integer.001"
    integer_001_1.integer = 0
    group_input_006_1 = hole.nodes.new("NodeGroupInput")
    group_input_006_1.name = "Group Input.006"
    group_input_006_1.outputs[0].hide = True
    group_input_006_1.outputs[1].hide = True
    group_input_006_1.outputs[2].hide = True
    group_input_006_1.outputs[3].hide = True
    group_input_006_1.outputs[6].hide = True
    group_input_006_1.outputs[7].hide = True
    group_input_006_1.outputs[8].hide = True
    group_input_006_1.outputs[9].hide = True
    group_input_006_1.outputs[10].hide = True
    group_input_006_1.outputs[11].hide = True
    group_input_006_1.outputs[12].hide = True
    group_input_006_1.outputs[13].hide = True
    group_input_006_1.outputs[14].hide = True
    group_input_006_1.outputs[15].hide = True
    group_input_006_1.outputs[16].hide = True
    group_input_006_1.outputs[17].hide = True
    group_input_007_1 = hole.nodes.new("NodeGroupInput")
    group_input_007_1.name = "Group Input.007"
    group_input_007_1.outputs[0].hide = True
    group_input_007_1.outputs[2].hide = True
    group_input_007_1.outputs[3].hide = True
    group_input_007_1.outputs[4].hide = True
    group_input_007_1.outputs[5].hide = True
    group_input_007_1.outputs[6].hide = True
    group_input_007_1.outputs[7].hide = True
    group_input_007_1.outputs[8].hide = True
    group_input_007_1.outputs[9].hide = True
    group_input_007_1.outputs[10].hide = True
    group_input_007_1.outputs[11].hide = True
    group_input_007_1.outputs[12].hide = True
    group_input_007_1.outputs[13].hide = True
    group_input_007_1.outputs[14].hide = True
    group_input_007_1.outputs[15].hide = True
    group_input_007_1.outputs[16].hide = True
    group_input_007_1.outputs[17].hide = True
    random_value_001_1 = hole.nodes.new("FunctionNodeRandomValue")
    random_value_001_1.name = "Random Value.001"
    random_value_001_1.data_type = 'FLOAT_VECTOR'
    group = hole.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = _get_parallel_vectors
    group_input_008_1 = hole.nodes.new("NodeGroupInput")
    group_input_008_1.name = "Group Input.008"
    group_input_008_1.outputs[0].hide = True
    group_input_008_1.outputs[2].hide = True
    group_input_008_1.outputs[3].hide = True
    group_input_008_1.outputs[4].hide = True
    group_input_008_1.outputs[5].hide = True
    group_input_008_1.outputs[6].hide = True
    group_input_008_1.outputs[7].hide = True
    group_input_008_1.outputs[8].hide = True
    group_input_008_1.outputs[9].hide = True
    group_input_008_1.outputs[10].hide = True
    group_input_008_1.outputs[11].hide = True
    group_input_008_1.outputs[12].hide = True
    group_input_008_1.outputs[13].hide = True
    group_input_008_1.outputs[14].hide = True
    group_input_008_1.outputs[15].hide = True
    group_input_008_1.outputs[16].hide = True
    group_input_008_1.outputs[17].hide = True
    integer_002_1 = hole.nodes.new("FunctionNodeInputInt")
    integer_002_1.name = "Integer.002"
    integer_002_1.integer = 1
    group_input_009_1 = hole.nodes.new("NodeGroupInput")
    group_input_009_1.name = "Group Input.009"
    group_input_009_1.outputs[0].hide = True
    group_input_009_1.outputs[1].hide = True
    group_input_009_1.outputs[2].hide = True
    group_input_009_1.outputs[3].hide = True
    group_input_009_1.outputs[4].hide = True
    group_input_009_1.outputs[5].hide = True
    group_input_009_1.outputs[8].hide = True
    group_input_009_1.outputs[9].hide = True
    group_input_009_1.outputs[10].hide = True
    group_input_009_1.outputs[11].hide = True
    group_input_009_1.outputs[12].hide = True
    group_input_009_1.outputs[13].hide = True
    group_input_009_1.outputs[14].hide = True
    group_input_009_1.outputs[15].hide = True
    group_input_009_1.outputs[16].hide = True
    group_input_009_1.outputs[17].hide = True
    random_value_002_1 = hole.nodes.new("FunctionNodeRandomValue")
    random_value_002_1.name = "Random Value.002"
    random_value_002_1.data_type = 'FLOAT_VECTOR'
    normal_002 = hole.nodes.new("GeometryNodeInputNormal")
    normal_002.name = "Normal.002"
    group_input_010_1 = hole.nodes.new("NodeGroupInput")
    group_input_010_1.name = "Group Input.010"
    group_input_010_1.outputs[1].hide = True
    group_input_010_1.outputs[2].hide = True
    group_input_010_1.outputs[3].hide = True
    group_input_010_1.outputs[4].hide = True
    group_input_010_1.outputs[5].hide = True
    group_input_010_1.outputs[6].hide = True
    group_input_010_1.outputs[7].hide = True
    group_input_010_1.outputs[8].hide = True
    group_input_010_1.outputs[9].hide = True
    group_input_010_1.outputs[10].hide = True
    group_input_010_1.outputs[11].hide = True
    group_input_010_1.outputs[12].hide = True
    group_input_010_1.outputs[13].hide = True
    group_input_010_1.outputs[14].hide = True
    group_input_010_1.outputs[15].hide = True
    group_input_010_1.outputs[16].hide = True
    group_input_010_1.outputs[17].hide = True
    sample_nearest_surface = hole.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface.name = "Sample Nearest Surface"
    sample_nearest_surface.data_type = 'FLOAT_VECTOR'
    sample_nearest_surface.inputs[2].default_value = 0
    sample_nearest_surface.inputs[4].default_value = 0
    vector_math_012 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_012.name = "Vector Math.012"
    vector_math_012.operation = 'ADD'
    reroute_015 = hole.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    reroute_015.socket_idname = "NodeSocketVector"
    group_input_011_1 = hole.nodes.new("NodeGroupInput")
    group_input_011_1.name = "Group Input.011"
    group_input_011_1.outputs[0].hide = True
    group_input_011_1.outputs[2].hide = True
    group_input_011_1.outputs[3].hide = True
    group_input_011_1.outputs[4].hide = True
    group_input_011_1.outputs[5].hide = True
    group_input_011_1.outputs[6].hide = True
    group_input_011_1.outputs[7].hide = True
    group_input_011_1.outputs[8].hide = True
    group_input_011_1.outputs[9].hide = True
    group_input_011_1.outputs[10].hide = True
    group_input_011_1.outputs[11].hide = True
    group_input_011_1.outputs[12].hide = True
    group_input_011_1.outputs[13].hide = True
    group_input_011_1.outputs[14].hide = True
    group_input_011_1.outputs[15].hide = True
    group_input_011_1.outputs[16].hide = True
    group_input_011_1.outputs[17].hide = True
    group_input_012_1 = hole.nodes.new("NodeGroupInput")
    group_input_012_1.name = "Group Input.012"
    group_input_012_1.outputs[0].hide = True
    group_input_012_1.outputs[1].hide = True
    group_input_012_1.outputs[2].hide = True
    group_input_012_1.outputs[3].hide = True
    group_input_012_1.outputs[4].hide = True
    group_input_012_1.outputs[5].hide = True
    group_input_012_1.outputs[6].hide = True
    group_input_012_1.outputs[7].hide = True
    group_input_012_1.outputs[10].hide = True
    group_input_012_1.outputs[11].hide = True
    group_input_012_1.outputs[12].hide = True
    group_input_012_1.outputs[13].hide = True
    group_input_012_1.outputs[14].hide = True
    group_input_012_1.outputs[15].hide = True
    group_input_012_1.outputs[16].hide = True
    group_input_012_1.outputs[17].hide = True
    integer_003_1 = hole.nodes.new("FunctionNodeInputInt")
    integer_003_1.name = "Integer.003"
    integer_003_1.integer = 2
    random_value_003_1 = hole.nodes.new("FunctionNodeRandomValue")
    random_value_003_1.name = "Random Value.003"
    random_value_003_1.data_type = 'FLOAT'
    combine_xyz_002 = hole.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    combine_xyz_002.inputs[0].hide = True
    combine_xyz_002.inputs[1].hide = True
    combine_xyz_002.inputs[0].default_value = 0.0
    combine_xyz_002.inputs[1].default_value = 0.0
    normal_003 = hole.nodes.new("GeometryNodeInputNormal")
    normal_003.name = "Normal.003"
    capture_attribute_002 = hole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_002.name = "Capture Attribute.002"
    capture_attribute_002.active_index = 0
    capture_attribute_002.capture_items.clear()
    capture_attribute_002.capture_items.new('FLOAT', "Value")
    capture_attribute_002.capture_items["Value"].data_type = 'FLOAT_VECTOR'
    capture_attribute_002.domain = 'FACE'
    transform_geometry_002 = hole.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.mode = 'COMPONENTS'
    transform_geometry_002.inputs[2].hide = True
    transform_geometry_002.inputs[3].hide = True
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)
    group_input_013_1 = hole.nodes.new("NodeGroupInput")
    group_input_013_1.name = "Group Input.013"
    group_input_013_1.outputs[0].hide = True
    group_input_013_1.outputs[1].hide = True
    group_input_013_1.outputs[2].hide = True
    group_input_013_1.outputs[3].hide = True
    group_input_013_1.outputs[4].hide = True
    group_input_013_1.outputs[5].hide = True
    group_input_013_1.outputs[6].hide = True
    group_input_013_1.outputs[7].hide = True
    group_input_013_1.outputs[8].hide = True
    group_input_013_1.outputs[9].hide = True
    group_input_013_1.outputs[10].hide = True
    group_input_013_1.outputs[11].hide = True
    group_input_013_1.outputs[12].hide = True
    group_input_013_1.outputs[13].hide = True
    group_input_013_1.outputs[15].hide = True
    group_input_013_1.outputs[16].hide = True
    group_input_013_1.outputs[17].hide = True
    vector_math_013 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_013.name = "Vector Math.013"
    vector_math_013.operation = 'SCALE'
    compare_1 = hole.nodes.new("FunctionNodeCompare")
    compare_1.name = "Compare"
    compare_1.data_type = 'VECTOR'
    compare_1.mode = 'DIRECTION'
    compare_1.operation = 'LESS_THAN'
    compare_1.inputs[11].default_value = 1.5620696544647217
    transform_geometry_003 = hole.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.mode = 'COMPONENTS'
    transform_geometry_003.inputs[3].hide = True
    transform_geometry_003.inputs[3].default_value = (1.0, 1.0, 1.0)
    reroute_016 = hole.nodes.new("NodeReroute")
    reroute_016.name = "Reroute.016"
    reroute_016.socket_idname = "NodeSocketGeometry"
    vector_math_014 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_014.name = "Vector Math.014"
    vector_math_014.operation = 'SCALE'
    vector_math_015 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_015.name = "Vector Math.015"
    vector_math_015.operation = 'NORMALIZE'
    vector_math_016 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_016.name = "Vector Math.016"
    vector_math_016.operation = 'SUBTRACT'
    vector_math_017 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_017.name = "Vector Math.017"
    vector_math_017.operation = 'SCALE'
    vector_math_018 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_018.name = "Vector Math.018"
    vector_math_018.operation = 'DOT_PRODUCT'
    reroute_017 = hole.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    reroute_017.socket_idname = "NodeSocketVector"
    capture_attribute_003 = hole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_003.name = "Capture Attribute.003"
    capture_attribute_003.active_index = 0
    capture_attribute_003.capture_items.clear()
    capture_attribute_003.capture_items.new('FLOAT', "Value")
    capture_attribute_003.capture_items["Value"].data_type = 'FLOAT_VECTOR'
    capture_attribute_003.domain = 'FACE'
    normal_004 = hole.nodes.new("GeometryNodeInputNormal")
    normal_004.name = "Normal.004"
    math_002_2 = hole.nodes.new("ShaderNodeMath")
    math_002_2.name = "Math.002"
    math_002_2.operation = 'ADD'
    math_002_2.use_clamp = False
    group_input_014_1 = hole.nodes.new("NodeGroupInput")
    group_input_014_1.name = "Group Input.014"
    group_input_014_1.outputs[0].hide = True
    group_input_014_1.outputs[1].hide = True
    group_input_014_1.outputs[2].hide = True
    group_input_014_1.outputs[3].hide = True
    group_input_014_1.outputs[4].hide = True
    group_input_014_1.outputs[5].hide = True
    group_input_014_1.outputs[6].hide = True
    group_input_014_1.outputs[7].hide = True
    group_input_014_1.outputs[8].hide = True
    group_input_014_1.outputs[9].hide = True
    group_input_014_1.outputs[10].hide = True
    group_input_014_1.outputs[11].hide = True
    group_input_014_1.outputs[12].hide = True
    group_input_014_1.outputs[13].hide = True
    group_input_014_1.outputs[14].hide = True
    group_input_014_1.outputs[16].hide = True
    group_input_014_1.outputs[17].hide = True
    compare_001_1 = hole.nodes.new("FunctionNodeCompare")
    compare_001_1.name = "Compare.001"
    compare_001_1.data_type = 'VECTOR'
    compare_001_1.mode = 'DIRECTION'
    compare_001_1.operation = 'LESS_THAN'
    compare_001_1.inputs[11].default_value = 3.1328659057617188
    capture_attribute_004 = hole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_004.name = "Capture Attribute.004"
    capture_attribute_004.active_index = 0
    capture_attribute_004.capture_items.clear()
    capture_attribute_004.capture_items.new('FLOAT', "Value")
    capture_attribute_004.capture_items["Value"].data_type = 'FLOAT_VECTOR'
    capture_attribute_004.domain = 'FACE'
    normal_005 = hole.nodes.new("GeometryNodeInputNormal")
    normal_005.name = "Normal.005"
    group_input_015 = hole.nodes.new("NodeGroupInput")
    group_input_015.name = "Group Input.015"
    group_input_015.outputs[0].hide = True
    group_input_015.outputs[1].hide = True
    group_input_015.outputs[2].hide = True
    group_input_015.outputs[3].hide = True
    group_input_015.outputs[4].hide = True
    group_input_015.outputs[5].hide = True
    group_input_015.outputs[6].hide = True
    group_input_015.outputs[7].hide = True
    group_input_015.outputs[8].hide = True
    group_input_015.outputs[9].hide = True
    group_input_015.outputs[10].hide = True
    group_input_015.outputs[11].hide = True
    group_input_015.outputs[12].hide = True
    group_input_015.outputs[13].hide = True
    group_input_015.outputs[14].hide = True
    group_input_015.outputs[15].hide = True
    group_input_015.outputs[17].hide = True
    capture_attribute_005 = hole.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute_005.name = "Capture Attribute.005"
    capture_attribute_005.active_index = 0
    capture_attribute_005.capture_items.clear()
    capture_attribute_005.capture_items.new('FLOAT', "Value")
    capture_attribute_005.capture_items["Value"].data_type = 'FLOAT_VECTOR'
    capture_attribute_005.domain = 'FACE'
    normal_006 = hole.nodes.new("GeometryNodeInputNormal")
    normal_006.name = "Normal.006"
    group_input_016 = hole.nodes.new("NodeGroupInput")
    group_input_016.name = "Group Input.016"
    group_input_016.outputs[1].hide = True
    group_input_016.outputs[2].hide = True
    group_input_016.outputs[3].hide = True
    group_input_016.outputs[4].hide = True
    group_input_016.outputs[5].hide = True
    group_input_016.outputs[6].hide = True
    group_input_016.outputs[7].hide = True
    group_input_016.outputs[8].hide = True
    group_input_016.outputs[9].hide = True
    group_input_016.outputs[10].hide = True
    group_input_016.outputs[11].hide = True
    group_input_016.outputs[12].hide = True
    group_input_016.outputs[13].hide = True
    group_input_016.outputs[14].hide = True
    group_input_016.outputs[15].hide = True
    group_input_016.outputs[16].hide = True
    group_input_016.outputs[17].hide = True
    sample_nearest_surface_001 = hole.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface_001.name = "Sample Nearest Surface.001"
    sample_nearest_surface_001.data_type = 'FLOAT_VECTOR'
    sample_nearest_surface_001.inputs[2].default_value = 0
    sample_nearest_surface_001.inputs[4].default_value = 0
    delete_geometry_1 = hole.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_1.name = "Delete Geometry"
    delete_geometry_1.domain = 'FACE'
    delete_geometry_1.mode = 'ALL'
    compare_002_1 = hole.nodes.new("FunctionNodeCompare")
    compare_002_1.name = "Compare.002"
    compare_002_1.data_type = 'VECTOR'
    compare_002_1.mode = 'DIRECTION'
    compare_002_1.operation = 'NOT_EQUAL'
    compare_002_1.inputs[11].default_value = 3.1415927410125732
    compare_002_1.inputs[12].default_value = 0.10000000149011612
    mesh_boolean = hole.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.operation = 'DIFFERENCE'
    mesh_boolean.solver = 'EXACT'
    mesh_boolean.inputs[2].default_value = False
    mesh_boolean.inputs[3].default_value = False
    mesh_boolean_001 = hole.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_001.name = "Mesh Boolean.001"
    mesh_boolean_001.operation = 'UNION'
    mesh_boolean_001.solver = 'EXACT'
    mesh_boolean_001.inputs[2].default_value = False
    mesh_boolean_001.inputs[3].default_value = False
    group_input_017 = hole.nodes.new("NodeGroupInput")
    group_input_017.name = "Group Input.017"
    group_input_017.outputs[1].hide = True
    group_input_017.outputs[2].hide = True
    group_input_017.outputs[3].hide = True
    group_input_017.outputs[4].hide = True
    group_input_017.outputs[5].hide = True
    group_input_017.outputs[6].hide = True
    group_input_017.outputs[7].hide = True
    group_input_017.outputs[8].hide = True
    group_input_017.outputs[9].hide = True
    group_input_017.outputs[10].hide = True
    group_input_017.outputs[11].hide = True
    group_input_017.outputs[12].hide = True
    group_input_017.outputs[13].hide = True
    group_input_017.outputs[14].hide = True
    group_input_017.outputs[15].hide = True
    group_input_017.outputs[16].hide = True
    group_input_017.outputs[17].hide = True
    transform_geometry_004 = hole.nodes.new("GeometryNodeTransform")
    transform_geometry_004.name = "Transform Geometry.004"
    transform_geometry_004.mode = 'COMPONENTS'
    transform_geometry_004.inputs[1].hide = True
    transform_geometry_004.inputs[3].hide = True
    transform_geometry_004.inputs[1].default_value = (0.0, 0.0, 0.0)
    transform_geometry_004.inputs[3].default_value = (1.0, 1.0, 1.0)
    group_input_018 = hole.nodes.new("NodeGroupInput")
    group_input_018.name = "Group Input.018"
    group_input_018.outputs[0].hide = True
    group_input_018.outputs[1].hide = True
    group_input_018.outputs[3].hide = True
    group_input_018.outputs[4].hide = True
    group_input_018.outputs[5].hide = True
    group_input_018.outputs[6].hide = True
    group_input_018.outputs[7].hide = True
    group_input_018.outputs[8].hide = True
    group_input_018.outputs[9].hide = True
    group_input_018.outputs[10].hide = True
    group_input_018.outputs[11].hide = True
    group_input_018.outputs[12].hide = True
    group_input_018.outputs[13].hide = True
    group_input_018.outputs[14].hide = True
    group_input_018.outputs[15].hide = True
    group_input_018.outputs[16].hide = True
    group_input_018.outputs[17].hide = True
    object_info_002 = hole.nodes.new("GeometryNodeObjectInfo")
    object_info_002.name = "Object Info.002"
    object_info_002.transform_space = 'ORIGINAL'
    object_info_002.inputs[1].hide = True
    object_info_002.outputs[1].hide = True
    object_info_002.outputs[2].hide = True
    object_info_002.outputs[3].hide = True
    object_info_002.inputs[1].default_value = False
    convex_hull = hole.nodes.new("GeometryNodeConvexHull")
    convex_hull.name = "Convex Hull"
    compare_003_1 = hole.nodes.new("FunctionNodeCompare")
    compare_003_1.name = "Compare.003"
    compare_003_1.data_type = 'VECTOR'
    compare_003_1.mode = 'DIRECTION'
    compare_003_1.operation = 'LESS_THAN'
    compare_003_1.inputs[11].default_value = 1.5620696544647217
    reroute_018 = hole.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    reroute_018.socket_idname = "NodeSocketVector"
    attribute_statistic_001 = hole.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic_001.name = "Attribute Statistic.001"
    attribute_statistic_001.data_type = 'FLOAT'
    attribute_statistic_001.domain = 'FACE'
    attribute_statistic_001.inputs[1].hide = True
    attribute_statistic_001.outputs[0].hide = True
    attribute_statistic_001.outputs[2].hide = True
    attribute_statistic_001.outputs[3].hide = True
    attribute_statistic_001.outputs[4].hide = True
    attribute_statistic_001.outputs[5].hide = True
    attribute_statistic_001.outputs[6].hide = True
    attribute_statistic_001.outputs[7].hide = True
    attribute_statistic_001.inputs[1].default_value = True
    object_info_003 = hole.nodes.new("GeometryNodeObjectInfo")
    object_info_003.name = "Object Info.003"
    object_info_003.transform_space = 'ORIGINAL'
    object_info_003.inputs[1].hide = True
    object_info_003.outputs[1].hide = True
    object_info_003.outputs[2].hide = True
    object_info_003.outputs[3].hide = True
    object_info_003.inputs[1].default_value = False
    is_shade_smooth = hole.nodes.new("GeometryNodeInputShadeSmooth")
    is_shade_smooth.name = "Is Shade Smooth"
    group_input_019 = hole.nodes.new("NodeGroupInput")
    group_input_019.name = "Group Input.019"
    group_input_019.outputs[0].hide = True
    group_input_019.outputs[1].hide = True
    group_input_019.outputs[3].hide = True
    group_input_019.outputs[4].hide = True
    group_input_019.outputs[5].hide = True
    group_input_019.outputs[6].hide = True
    group_input_019.outputs[7].hide = True
    group_input_019.outputs[8].hide = True
    group_input_019.outputs[9].hide = True
    group_input_019.outputs[10].hide = True
    group_input_019.outputs[11].hide = True
    group_input_019.outputs[12].hide = True
    group_input_019.outputs[13].hide = True
    group_input_019.outputs[14].hide = True
    group_input_019.outputs[15].hide = True
    group_input_019.outputs[16].hide = True
    group_input_019.outputs[17].hide = True
    compare_004_1 = hole.nodes.new("FunctionNodeCompare")
    compare_004_1.name = "Compare.004"
    compare_004_1.data_type = 'VECTOR'
    compare_004_1.mode = 'DIRECTION'
    compare_004_1.operation = 'GREATER_THAN'
    compare_004_1.inputs[11].default_value = 1.579522967338562
    reroute_019 = hole.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    reroute_019.socket_idname = "NodeSocketVector"
    group_input_020 = hole.nodes.new("NodeGroupInput")
    group_input_020.name = "Group Input.020"
    group_input_020.outputs[0].hide = True
    group_input_020.outputs[1].hide = True
    group_input_020.outputs[2].hide = True
    group_input_020.outputs[3].hide = True
    group_input_020.outputs[4].hide = True
    group_input_020.outputs[5].hide = True
    group_input_020.outputs[6].hide = True
    group_input_020.outputs[7].hide = True
    group_input_020.outputs[8].hide = True
    group_input_020.outputs[9].hide = True
    group_input_020.outputs[10].hide = True
    group_input_020.outputs[11].hide = True
    group_input_020.outputs[12].hide = True
    group_input_020.outputs[13].hide = True
    group_input_020.outputs[14].hide = True
    group_input_020.outputs[16].hide = True
    group_input_020.outputs[17].hide = True
    vector_math_019 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_019.name = "Vector Math.019"
    vector_math_019.operation = 'SCALE'
    group_001 = hole.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = _decimate_planar
    set_shade_smooth_1 = hole.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth_1.name = "Set Shade Smooth"
    set_shade_smooth_1.domain = 'FACE'
    boolean_math = hole.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = 'NOR'
    switch_001_1 = hole.nodes.new("GeometryNodeSwitch")
    switch_001_1.name = "Switch.001"
    switch_001_1.input_type = 'GEOMETRY'
    set_position_001 = hole.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.inputs[1].default_value = True
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    set_position_002 = hole.nodes.new("GeometryNodeSetPosition")
    set_position_002.name = "Set Position.002"
    set_position_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    switch_002_1 = hole.nodes.new("GeometryNodeSwitch")
    switch_002_1.name = "Switch.002"
    switch_002_1.input_type = 'GEOMETRY'
    reroute_020 = hole.nodes.new("NodeReroute")
    reroute_020.name = "Reroute.020"
    reroute_020.socket_idname = "NodeSocketVector"
    vector_math_020 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_020.name = "Vector Math.020"
    vector_math_020.operation = 'SCALE'
    group_input_021 = hole.nodes.new("NodeGroupInput")
    group_input_021.name = "Group Input.021"
    group_input_021.outputs[1].hide = True
    group_input_021.outputs[2].hide = True
    group_input_021.outputs[3].hide = True
    group_input_021.outputs[4].hide = True
    group_input_021.outputs[5].hide = True
    group_input_021.outputs[6].hide = True
    group_input_021.outputs[7].hide = True
    group_input_021.outputs[8].hide = True
    group_input_021.outputs[9].hide = True
    group_input_021.outputs[10].hide = True
    group_input_021.outputs[11].hide = True
    group_input_021.outputs[12].hide = True
    group_input_021.outputs[13].hide = True
    group_input_021.outputs[14].hide = True
    group_input_021.outputs[15].hide = True
    group_input_021.outputs[16].hide = True
    group_input_021.outputs[17].hide = True
    position_001_1 = hole.nodes.new("GeometryNodeInputPosition")
    position_001_1.name = "Position.001"
    sample_nearest_surface_002 = hole.nodes.new("GeometryNodeSampleNearestSurface")
    sample_nearest_surface_002.name = "Sample Nearest Surface.002"
    sample_nearest_surface_002.data_type = 'FLOAT_VECTOR'
    sample_nearest_surface_002.inputs[2].default_value = 0
    sample_nearest_surface_002.inputs[4].default_value = 0
    reroute_021 = hole.nodes.new("NodeReroute")
    reroute_021.name = "Reroute.021"
    reroute_021.socket_idname = "NodeSocketVector"
    vector_math_021 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_021.name = "Vector Math.021"
    vector_math_021.operation = 'SCALE'
    vector_math_021.inputs[3].default_value = -1.0
    reroute_022 = hole.nodes.new("NodeReroute")
    reroute_022.name = "Reroute.022"
    reroute_022.socket_idname = "NodeSocketVector"
    reroute_023 = hole.nodes.new("NodeReroute")
    reroute_023.name = "Reroute.023"
    reroute_023.socket_idname = "NodeSocketVector"
    reroute_024 = hole.nodes.new("NodeReroute")
    reroute_024.name = "Reroute.024"
    reroute_024.socket_idname = "NodeSocketVector"
    vector_math_002 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'SCALE'
    reroute_005_2 = hole.nodes.new("NodeReroute")
    reroute_005_2.name = "Reroute.005"
    reroute_005_2.socket_idname = "NodeSocketVector"
    reroute_026 = hole.nodes.new("NodeReroute")
    reroute_026.name = "Reroute.026"
    reroute_026.socket_idname = "NodeSocketVector"
    reroute_004_2 = hole.nodes.new("NodeReroute")
    reroute_004_2.name = "Reroute.004"
    reroute_004_2.socket_idname = "NodeSocketGeometry"
    switch_1 = hole.nodes.new("GeometryNodeSwitch")
    switch_1.name = "Switch"
    switch_1.input_type = 'GEOMETRY'
    group_input_3 = hole.nodes.new("NodeGroupInput")
    group_input_3.name = "Group Input"
    group_input_3.outputs[1].hide = True
    group_input_3.outputs[2].hide = True
    group_input_3.outputs[3].hide = True
    group_input_3.outputs[4].hide = True
    group_input_3.outputs[5].hide = True
    group_input_3.outputs[6].hide = True
    group_input_3.outputs[7].hide = True
    group_input_3.outputs[8].hide = True
    group_input_3.outputs[9].hide = True
    group_input_3.outputs[10].hide = True
    group_input_3.outputs[11].hide = True
    group_input_3.outputs[12].hide = True
    group_input_3.outputs[14].hide = True
    group_input_3.outputs[15].hide = True
    group_input_3.outputs[16].hide = True
    group_input_3.outputs[17].hide = True
    mesh_boolean_002 = hole.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_002.name = "Mesh Boolean.002"
    mesh_boolean_002.operation = 'DIFFERENCE'
    mesh_boolean_002.solver = 'EXACT'
    mesh_boolean_002.inputs[2].default_value = False
    mesh_boolean_002.inputs[3].default_value = False
    reroute_025 = hole.nodes.new("NodeReroute")
    reroute_025.name = "Reroute.025"
    reroute_025.socket_idname = "NodeSocketVector"
    reroute_028 = hole.nodes.new("NodeReroute")
    reroute_028.name = "Reroute.028"
    reroute_028.hide = True
    reroute_028.socket_idname = "NodeSocketVector"
    group_output_3 = hole.nodes.new("NodeGroupOutput")
    group_output_3.name = "Group Output"
    group_output_3.is_active_output = True
    raycast_001 = hole.nodes.new("GeometryNodeRaycast")
    raycast_001.name = "Raycast.001"
    raycast_001.data_type = 'FLOAT'
    raycast_001.mapping = 'INTERPOLATED'
    raycast_001.inputs[1].default_value = 0.0
    raycast_001.inputs[4].default_value = 100.0
    align_euler_to_vector_001 = hole.nodes.new("FunctionNodeAlignEulerToVector")
    align_euler_to_vector_001.name = "Align Euler to Vector.001"
    align_euler_to_vector_001.axis = 'Z'
    align_euler_to_vector_001.pivot_axis = 'AUTO'
    align_euler_to_vector_001.inputs[1].default_value = 1.0
    vector_math_022 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_022.name = "Vector Math.022"
    vector_math_022.operation = 'ADD'
    vector_math_023 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_023.name = "Vector Math.023"
    vector_math_023.operation = 'SCALE'
    vector_math_023.inputs[3].default_value = -1.0
    group_input_022 = hole.nodes.new("NodeGroupInput")
    group_input_022.name = "Group Input.022"
    group_input_022.outputs[1].hide = True
    group_input_022.outputs[2].hide = True
    group_input_022.outputs[3].hide = True
    group_input_022.outputs[4].hide = True
    group_input_022.outputs[5].hide = True
    group_input_022.outputs[6].hide = True
    group_input_022.outputs[7].hide = True
    group_input_022.outputs[8].hide = True
    group_input_022.outputs[9].hide = True
    group_input_022.outputs[10].hide = True
    group_input_022.outputs[11].hide = True
    group_input_022.outputs[12].hide = True
    group_input_022.outputs[13].hide = True
    group_input_022.outputs[14].hide = True
    group_input_022.outputs[15].hide = True
    group_input_022.outputs[16].hide = True
    group_input_022.outputs[17].hide = True
    raycast = hole.nodes.new("GeometryNodeRaycast")
    raycast.name = "Raycast"
    raycast.data_type = 'FLOAT'
    raycast.mapping = 'INTERPOLATED'
    raycast.inputs[1].default_value = 0.0
    raycast.inputs[4].default_value = 100.0
    extrude_mesh = hole.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh.name = "Extrude Mesh"
    extrude_mesh.mode = 'FACES'
    extrude_mesh.inputs[3].default_value = 1.0
    extrude_mesh.inputs[4].default_value = False
    set_position_1 = hole.nodes.new("GeometryNodeSetPosition")
    set_position_1.name = "Set Position"
    set_position_1.inputs[1].default_value = True
    set_position_1.inputs[2].default_value = (0.0, 0.0, 0.0)
    set_position_003 = hole.nodes.new("GeometryNodeSetPosition")
    set_position_003.name = "Set Position.003"
    set_position_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    rotation_to_euler = hole.nodes.new("FunctionNodeRotationToEuler")
    rotation_to_euler.name = "Rotation to Euler"
    euler_to_rotation = hole.nodes.new("FunctionNodeEulerToRotation")
    euler_to_rotation.name = "Euler to Rotation"
    group_002 = hole.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = peg
    group_002.inputs[1].default_value = 0.3333333432674408
    group_002.inputs[2].default_value = 48
    group_002.inputs[3].default_value = 3
    group_002.inputs[4].default_value = 12
    group_002.inputs[5].default_value = 0.009999999776482582
    group_002.inputs[6].default_value = 0.02500000037252903
    group_002.inputs[7].default_value = 0.03999999910593033
    group_002.inputs[8].default_value = 0.07999999821186066
    group_002.inputs[9].default_value = 0.25
    group_002.inputs[10].default_value = 1.0
    group_002.inputs[11].default_value = 0.0
    group_002.inputs[12].default_value = 0.0
    group_002.inputs[13].default_value = False
    group_input_024 = hole.nodes.new("NodeGroupInput")
    group_input_024.name = "Group Input.024"
    vector_math_024 = hole.nodes.new("ShaderNodeVectorMath")
    vector_math_024.name = "Vector Math.024"
    vector_math_024.operation = 'SCALE'
    vector_math_024.inputs[3].default_value = -1.0
    set_material_1 = hole.nodes.new("GeometryNodeSetMaterial")
    set_material_1.name = "Set Material"
    set_material_1.inputs[1].default_value = True
    frame_001_2.width, frame_001_2.height = 150.0, 100.0
    frame_002_2.width, frame_002_2.height = 150.0, 100.0
    frame_003_2.width, frame_003_2.height = 150.0, 100.0
    frame_004_2.width, frame_004_2.height = 150.0, 100.0
    frame_005_2.width, frame_005_2.height = 150.0, 100.0
    frame_006_2.width, frame_006_2.height = 150.0, 100.0
    frame_007_1.width, frame_007_1.height = 150.0, 100.0
    frame_008_1.width, frame_008_1.height = 150.0, 100.0
    frame_009.width, frame_009.height = 150.0, 100.0
    frame_010.width, frame_010.height = 150.0, 100.0
    frame_011.width, frame_011.height = 150.0, 100.0
    frame_012.width, frame_012.height = 150.0, 100.0
    frame_013.width, frame_013.height = 150.0, 100.0
    frame_014.width, frame_014.height = 150.0, 100.0
    frame_2.width, frame_2.height = 150.0, 100.0
    reroute_2.width, reroute_2.height = 140.0, 100.0
    reroute_001_2.width, reroute_001_2.height = 140.0, 100.0
    reroute_002_2.width, reroute_002_2.height = 140.0, 100.0
    reroute_003_2.width, reroute_003_2.height = 140.0, 100.0
    reroute_006_2.width, reroute_006_2.height = 140.0, 100.0
    reroute_007_2.width, reroute_007_2.height = 140.0, 100.0
    reroute_008_1.width, reroute_008_1.height = 140.0, 100.0
    group_input_001_1.width, group_input_001_1.height = 140.0, 100.0
    position_1.width, position_1.height = 140.0, 100.0
    object_info.width, object_info.height = 140.0, 100.0
    attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
    vector_math_2.width, vector_math_2.height = 140.0, 100.0
    align_euler_to_vector.width, align_euler_to_vector.height = 140.0, 100.0
    reroute_009.width, reroute_009.height = 140.0, 100.0
    separate_xyz_1.width, separate_xyz_1.height = 140.0, 100.0
    vector_rotate.width, vector_rotate.height = 140.0, 100.0
    vector_math_001_2.width, vector_math_001_2.height = 140.0, 100.0
    reroute_010.width, reroute_010.height = 140.0, 100.0
    transform_geometry_1.width, transform_geometry_1.height = 140.0, 100.0
    group_input_002_1.width, group_input_002_1.height = 140.0, 100.0
    random_value_1.width, random_value_1.height = 140.0, 100.0
    group_input_003_1.width, group_input_003_1.height = 140.0, 100.0
    integer_1.width, integer_1.height = 140.0, 100.0
    reroute_011.width, reroute_011.height = 140.0, 100.0
    math_3.width, math_3.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    capture_attribute.width, capture_attribute.height = 140.0, 100.0
    normal_1.width, normal_1.height = 140.0, 100.0
    reroute_012.width, reroute_012.height = 140.0, 100.0
    vector_math_003.width, vector_math_003.height = 140.0, 100.0
    vector_math_004.width, vector_math_004.height = 140.0, 100.0
    vector_math_005.width, vector_math_005.height = 140.0, 100.0
    reroute_013.width, reroute_013.height = 140.0, 100.0
    normal_001_1.width, normal_001_1.height = 140.0, 100.0
    math_001_3.width, math_001_3.height = 140.0, 100.0
    vector_math_006.width, vector_math_006.height = 140.0, 100.0
    group_input_004_1.width, group_input_004_1.height = 140.0, 100.0
    vector_math_007.width, vector_math_007.height = 140.0, 100.0
    capture_attribute_001.width, capture_attribute_001.height = 140.0, 100.0
    vector_rotate_001.width, vector_rotate_001.height = 140.0, 100.0
    vector_math_008.width, vector_math_008.height = 140.0, 100.0
    vector_math_009.width, vector_math_009.height = 140.0, 100.0
    reroute_014.width, reroute_014.height = 140.0, 100.0
    group_input_005_1.width, group_input_005_1.height = 140.0, 100.0
    object_info_001.width, object_info_001.height = 140.0, 100.0
    vector_math_010.width, vector_math_010.height = 140.0, 100.0
    vector_math_011.width, vector_math_011.height = 140.0, 100.0
    combine_xyz_2.width, combine_xyz_2.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    integer_001_1.width, integer_001_1.height = 140.0, 100.0
    group_input_006_1.width, group_input_006_1.height = 140.0, 100.0
    group_input_007_1.width, group_input_007_1.height = 140.0, 100.0
    random_value_001_1.width, random_value_001_1.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0
    group_input_008_1.width, group_input_008_1.height = 140.0, 100.0
    integer_002_1.width, integer_002_1.height = 140.0, 100.0
    group_input_009_1.width, group_input_009_1.height = 140.0, 100.0
    random_value_002_1.width, random_value_002_1.height = 140.0, 100.0
    normal_002.width, normal_002.height = 140.0, 100.0
    group_input_010_1.width, group_input_010_1.height = 140.0, 100.0
    sample_nearest_surface.width, sample_nearest_surface.height = 150.0, 100.0
    vector_math_012.width, vector_math_012.height = 140.0, 100.0
    reroute_015.width, reroute_015.height = 140.0, 100.0
    group_input_011_1.width, group_input_011_1.height = 140.0, 100.0
    group_input_012_1.width, group_input_012_1.height = 140.0, 100.0
    integer_003_1.width, integer_003_1.height = 140.0, 100.0
    random_value_003_1.width, random_value_003_1.height = 140.0, 100.0
    combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
    normal_003.width, normal_003.height = 140.0, 100.0
    capture_attribute_002.width, capture_attribute_002.height = 140.0, 100.0
    transform_geometry_002.width, transform_geometry_002.height = 140.0, 100.0
    group_input_013_1.width, group_input_013_1.height = 140.0, 100.0
    vector_math_013.width, vector_math_013.height = 140.0, 100.0
    compare_1.width, compare_1.height = 140.0, 100.0
    transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
    reroute_016.width, reroute_016.height = 140.0, 100.0
    vector_math_014.width, vector_math_014.height = 140.0, 100.0
    vector_math_015.width, vector_math_015.height = 140.0, 100.0
    vector_math_016.width, vector_math_016.height = 140.0, 100.0
    vector_math_017.width, vector_math_017.height = 140.0, 100.0
    vector_math_018.width, vector_math_018.height = 140.0, 100.0
    reroute_017.width, reroute_017.height = 140.0, 100.0
    capture_attribute_003.width, capture_attribute_003.height = 140.0, 100.0
    normal_004.width, normal_004.height = 140.0, 100.0
    math_002_2.width, math_002_2.height = 140.0, 100.0
    group_input_014_1.width, group_input_014_1.height = 140.0, 100.0
    compare_001_1.width, compare_001_1.height = 140.0, 100.0
    capture_attribute_004.width, capture_attribute_004.height = 140.0, 100.0
    normal_005.width, normal_005.height = 140.0, 100.0
    group_input_015.width, group_input_015.height = 140.0, 100.0
    capture_attribute_005.width, capture_attribute_005.height = 140.0, 100.0
    normal_006.width, normal_006.height = 140.0, 100.0
    group_input_016.width, group_input_016.height = 140.0, 100.0
    sample_nearest_surface_001.width, sample_nearest_surface_001.height = 150.0, 100.0
    delete_geometry_1.width, delete_geometry_1.height = 140.0, 100.0
    compare_002_1.width, compare_002_1.height = 140.0, 100.0
    mesh_boolean.width, mesh_boolean.height = 140.0, 100.0
    mesh_boolean_001.width, mesh_boolean_001.height = 140.0, 100.0
    group_input_017.width, group_input_017.height = 140.0, 100.0
    transform_geometry_004.width, transform_geometry_004.height = 140.0, 100.0
    group_input_018.width, group_input_018.height = 140.0, 100.0
    object_info_002.width, object_info_002.height = 140.0, 100.0
    convex_hull.width, convex_hull.height = 140.0, 100.0
    compare_003_1.width, compare_003_1.height = 140.0, 100.0
    reroute_018.width, reroute_018.height = 140.0, 100.0
    attribute_statistic_001.width, attribute_statistic_001.height = 140.0, 100.0
    object_info_003.width, object_info_003.height = 140.0, 100.0
    is_shade_smooth.width, is_shade_smooth.height = 140.0, 100.0
    group_input_019.width, group_input_019.height = 140.0, 100.0
    compare_004_1.width, compare_004_1.height = 140.0, 100.0
    reroute_019.width, reroute_019.height = 140.0, 100.0
    group_input_020.width, group_input_020.height = 140.0, 100.0
    vector_math_019.width, vector_math_019.height = 140.0, 100.0
    group_001.width, group_001.height = 140.0, 100.0
    set_shade_smooth_1.width, set_shade_smooth_1.height = 140.0, 100.0
    boolean_math.width, boolean_math.height = 140.0, 100.0
    switch_001_1.width, switch_001_1.height = 140.0, 100.0
    set_position_001.width, set_position_001.height = 140.0, 100.0
    set_position_002.width, set_position_002.height = 140.0, 100.0
    switch_002_1.width, switch_002_1.height = 140.0, 100.0
    reroute_020.width, reroute_020.height = 140.0, 100.0
    vector_math_020.width, vector_math_020.height = 140.0, 100.0
    group_input_021.width, group_input_021.height = 140.0, 100.0
    position_001_1.width, position_001_1.height = 140.0, 100.0
    sample_nearest_surface_002.width, sample_nearest_surface_002.height = 150.0, 100.0
    reroute_021.width, reroute_021.height = 140.0, 100.0
    vector_math_021.width, vector_math_021.height = 140.0, 100.0
    reroute_022.width, reroute_022.height = 140.0, 100.0
    reroute_023.width, reroute_023.height = 140.0, 100.0
    reroute_024.width, reroute_024.height = 140.0, 100.0
    vector_math_002.width, vector_math_002.height = 140.0, 100.0
    reroute_005_2.width, reroute_005_2.height = 140.0, 100.0
    reroute_026.width, reroute_026.height = 140.0, 100.0
    reroute_004_2.width, reroute_004_2.height = 140.0, 100.0
    switch_1.width, switch_1.height = 140.0, 100.0
    group_input_3.width, group_input_3.height = 140.0, 100.0
    mesh_boolean_002.width, mesh_boolean_002.height = 140.0, 100.0
    reroute_025.width, reroute_025.height = 140.0, 100.0
    reroute_028.width, reroute_028.height = 140.0, 100.0
    group_output_3.width, group_output_3.height = 140.0, 100.0
    raycast_001.width, raycast_001.height = 150.0, 100.0
    align_euler_to_vector_001.width, align_euler_to_vector_001.height = 140.0, 100.0
    vector_math_022.width, vector_math_022.height = 140.0, 100.0
    vector_math_023.width, vector_math_023.height = 140.0, 100.0
    group_input_022.width, group_input_022.height = 140.0, 100.0
    raycast.width, raycast.height = 150.0, 100.0
    extrude_mesh.width, extrude_mesh.height = 140.0, 100.0
    set_position_1.width, set_position_1.height = 140.0, 100.0
    set_position_003.width, set_position_003.height = 140.0, 100.0
    rotation_to_euler.width, rotation_to_euler.height = 140.0, 100.0
    euler_to_rotation.width, euler_to_rotation.height = 140.0, 100.0
    group_002.width, group_002.height = 140.0, 100.0
    group_input_024.width, group_input_024.height = 140.0, 100.0
    vector_math_024.width, vector_math_024.height = 140.0, 100.0
    set_material_1.width, set_material_1.height = 140.0, 100.0
    hole.links.new(group_input_001_1.outputs[2], object_info.inputs[0])
    hole.links.new(position_1.outputs[0], attribute_statistic.inputs[2])
    hole.links.new(position_001_1.outputs[0], sample_nearest_surface_002.inputs[1])
    hole.links.new(object_info_001.outputs[1], sample_nearest_surface.inputs[3])
    hole.links.new(normal_002.outputs[0], sample_nearest_surface.inputs[1])
    hole.links.new(reroute_2.outputs[0], align_euler_to_vector.inputs[2])
    hole.links.new(group_input_021.outputs[0], sample_nearest_surface_002.inputs[0])
    hole.links.new(align_euler_to_vector.outputs[0], transform_geometry_1.inputs[2])
    hole.links.new(align_euler_to_vector.outputs[0], vector_rotate.inputs[4])
    hole.links.new(vector_rotate.outputs[0], vector_math_001_2.inputs[0])
    hole.links.new(group_input_005_1.outputs[3], object_info_001.inputs[0])
    hole.links.new(vector_math_2.outputs[0], vector_rotate.inputs[0])
    hole.links.new(attribute_statistic.outputs[3], vector_math_2.inputs[0])
    hole.links.new(vector_math_001_2.outputs[0], transform_geometry_1.inputs[1])
    hole.links.new(attribute_statistic.outputs[5], reroute_009.inputs[0])
    hole.links.new(reroute_011.outputs[0], transform_geometry_001.inputs[0])
    hole.links.new(separate_xyz_1.outputs[2], reroute_010.inputs[0])
    hole.links.new(reroute_009.outputs[0], separate_xyz_1.inputs[0])
    hole.links.new(group_input_002_1.outputs[1], random_value_1.inputs[8])
    hole.links.new(integer_1.outputs[0], random_value_1.inputs[7])
    hole.links.new(group_input_003_1.outputs[10], random_value_1.inputs[2])
    hole.links.new(reroute_010.outputs[0], math_3.inputs[1])
    hole.links.new(random_value_1.outputs[1], math_3.inputs[0])
    hole.links.new(normal_005.outputs[0], capture_attribute_004.inputs[1])
    hole.links.new(group_input_015.outputs[16], switch_002_1.inputs[0])
    hole.links.new(mesh_boolean.outputs[0], mesh_boolean_001.inputs[1])
    hole.links.new(switch_002_1.outputs[0], mesh_boolean.inputs[0])
    hole.links.new(reroute_006_2.outputs[0], reroute_005_2.inputs[0])
    hole.links.new(reroute_019.outputs[0], compare_001_1.inputs[5])
    hole.links.new(capture_attribute_004.outputs[1], compare_001_1.inputs[4])
    hole.links.new(reroute_002_2.outputs[0], reroute_003_2.inputs[0])
    hole.links.new(reroute_001_2.outputs[0], reroute_002_2.inputs[0])
    hole.links.new(normal_1.outputs[0], capture_attribute.inputs[1])
    hole.links.new(capture_attribute.outputs[1], compare_003_1.inputs[4])
    hole.links.new(transform_geometry_001.outputs[0], capture_attribute.inputs[0])
    hole.links.new(reroute_020.outputs[0], reroute_007_2.inputs[0])
    hole.links.new(transform_geometry_1.outputs[0], reroute_011.inputs[0])
    hole.links.new(reroute_005_2.outputs[0], reroute_019.inputs[0])
    hole.links.new(set_position_1.outputs[0], reroute_004_2.inputs[0])
    hole.links.new(group_input_007_1.outputs[1], random_value_001_1.inputs[8])
    hole.links.new(integer_001_1.outputs[0], random_value_001_1.inputs[7])
    hole.links.new(group_input_003_1.outputs[11], random_value_1.inputs[3])
    hole.links.new(group_input_006_1.outputs[5], random_value_001_1.inputs[1])
    hole.links.new(group_input_006_1.outputs[4], random_value_001_1.inputs[0])
    hole.links.new(object_info_001.outputs[1], vector_math_012.inputs[0])
    hole.links.new(sample_nearest_surface.outputs[0], group.inputs[0])
    hole.links.new(random_value_001_1.outputs[0], separate_xyz_001.inputs[0])
    hole.links.new(separate_xyz_001.outputs[0], combine_xyz_001.inputs[0])
    hole.links.new(combine_xyz_001.outputs[0], vector_math_010.inputs[1])
    hole.links.new(group.outputs[0], vector_math_010.inputs[0])
    hole.links.new(vector_math_010.outputs[0], vector_math_009.inputs[0])
    hole.links.new(combine_xyz_2.outputs[0], vector_math_011.inputs[1])
    hole.links.new(separate_xyz_001.outputs[1], combine_xyz_2.inputs[1])
    hole.links.new(group.outputs[1], vector_math_011.inputs[0])
    hole.links.new(vector_math_011.outputs[0], vector_math_009.inputs[1])
    hole.links.new(vector_math_009.outputs[0], vector_math_012.inputs[1])
    hole.links.new(vector_math_012.outputs[0], sample_nearest_surface_002.inputs[3])
    hole.links.new(group_input_008_1.outputs[1], random_value_002_1.inputs[8])
    hole.links.new(integer_002_1.outputs[0], random_value_002_1.inputs[7])
    hole.links.new(group_input_009_1.outputs[6], random_value_002_1.inputs[0])
    hole.links.new(group_input_009_1.outputs[7], random_value_002_1.inputs[1])
    hole.links.new(vector_math_012.outputs[0], vector_rotate_001.inputs[1])
    hole.links.new(normal_006.outputs[0], sample_nearest_surface_001.inputs[1])
    hole.links.new(vector_math_008.outputs[0], vector_rotate_001.inputs[4])
    hole.links.new(reroute_014.outputs[0], vector_math_008.inputs[0])
    hole.links.new(random_value_002_1.outputs[0], vector_math_008.inputs[1])
    hole.links.new(rotation_to_euler.outputs[0], reroute_014.inputs[0])
    hole.links.new(sample_nearest_surface.outputs[0], reroute_015.inputs[0])
    hole.links.new(reroute_021.outputs[0], reroute_020.inputs[0])
    hole.links.new(vector_math_021.outputs[0], reroute_023.inputs[0])
    hole.links.new(sample_nearest_surface_002.outputs[0], reroute_022.inputs[0])
    hole.links.new(group_input_010_1.outputs[0], sample_nearest_surface.inputs[0])
    hole.links.new(vector_rotate_001.outputs[0], reroute_021.inputs[0])
    hole.links.new(reroute_023.outputs[0], reroute_2.inputs[0])
    hole.links.new(reroute_022.outputs[0], reroute_001_2.inputs[0])
    hole.links.new(reroute_001_2.outputs[0], vector_math_001_2.inputs[1])
    hole.links.new(reroute_2.outputs[0], reroute_008_1.inputs[0])
    hole.links.new(reroute_008_1.outputs[0], vector_math_020.inputs[0])
    hole.links.new(group_input_016.outputs[0], sample_nearest_surface_001.inputs[0])
    hole.links.new(capture_attribute_005.outputs[0], delete_geometry_1.inputs[0])
    hole.links.new(sample_nearest_surface_001.outputs[0], compare_002_1.inputs[5])
    hole.links.new(capture_attribute_005.outputs[1], compare_002_1.inputs[4])
    hole.links.new(compare_002_1.outputs[0], delete_geometry_1.inputs[1])
    hole.links.new(delete_geometry_1.outputs[0], mesh_boolean.inputs[1])
    hole.links.new(group_input_016.outputs[0], capture_attribute_005.inputs[0])
    hole.links.new(normal_006.outputs[0], capture_attribute_005.inputs[1])
    hole.links.new(reroute_021.outputs[0], vector_math_021.inputs[0])
    hole.links.new(reroute_015.outputs[0], vector_rotate_001.inputs[0])
    hole.links.new(reroute_003_2.outputs[0], sample_nearest_surface_001.inputs[3])
    hole.links.new(reroute_007_2.outputs[0], reroute_006_2.inputs[0])
    hole.links.new(vector_math_004.outputs[0], set_position_1.inputs[3])
    hole.links.new(math_001_3.outputs[0], vector_math_004.inputs[3])
    hole.links.new(group_input_004_1.outputs[12], math_001_3.inputs[0])
    hole.links.new(normal_001_1.outputs[0], capture_attribute_001.inputs[1])
    hole.links.new(set_shade_smooth_1.outputs[0], capture_attribute_001.inputs[0])
    hole.links.new(reroute_012.outputs[0], set_position_1.inputs[0])
    hole.links.new(capture_attribute_004.outputs[0], switch_002_1.inputs[1])
    hole.links.new(mesh_boolean_001.outputs[0], switch_1.inputs[2])
    hole.links.new(group_input_3.outputs[0], switch_1.inputs[1])
    hole.links.new(group_input_3.outputs[13], switch_1.inputs[0])
    hole.links.new(vector_math_014.outputs[0], set_position_001.inputs[3])
    hole.links.new(normal_004.outputs[0], capture_attribute_003.inputs[1])
    hole.links.new(reroute_016.outputs[0], set_position_001.inputs[0])
    hole.links.new(vector_math_015.outputs[0], vector_math_014.inputs[0])
    hole.links.new(group_input_014_1.outputs[15], math_002_2.inputs[1])
    hole.links.new(math_002_2.outputs[0], vector_math_014.inputs[3])
    hole.links.new(set_position_001.outputs[0], capture_attribute_004.inputs[0])
    hole.links.new(capture_attribute_003.outputs[0], reroute_016.inputs[0])
    hole.links.new(capture_attribute_001.outputs[0], reroute_012.inputs[0])
    hole.links.new(reroute_007_2.outputs[0], vector_math_002.inputs[0])
    hole.links.new(math_3.outputs[0], vector_math_002.inputs[3])
    hole.links.new(vector_math_002.outputs[0], transform_geometry_001.inputs[1])
    hole.links.new(set_position_002.outputs[0], switch_002_1.inputs[2])
    hole.links.new(reroute_010.outputs[0], vector_math_020.inputs[3])
    hole.links.new(reroute_017.outputs[0], vector_math_018.inputs[1])
    hole.links.new(capture_attribute_003.outputs[1], vector_math_018.inputs[0])
    hole.links.new(capture_attribute_003.outputs[1], vector_math_016.inputs[0])
    hole.links.new(vector_math_016.outputs[0], vector_math_015.inputs[0])
    hole.links.new(reroute_017.outputs[0], vector_math_017.inputs[0])
    hole.links.new(vector_math_017.outputs[0], vector_math_016.inputs[1])
    hole.links.new(vector_math_018.outputs[1], vector_math_017.inputs[3])
    hole.links.new(vector_math_006.outputs[0], vector_math_003.inputs[0])
    hole.links.new(vector_math_007.outputs[0], vector_math_006.inputs[1])
    hole.links.new(vector_math_005.outputs[1], vector_math_007.inputs[3])
    hole.links.new(vector_math_003.outputs[0], vector_math_004.inputs[0])
    hole.links.new(capture_attribute_001.outputs[1], vector_math_005.inputs[0])
    hole.links.new(reroute_013.outputs[0], vector_math_005.inputs[1])
    hole.links.new(reroute_013.outputs[0], vector_math_007.inputs[0])
    hole.links.new(reroute_006_2.outputs[0], reroute_017.inputs[0])
    hole.links.new(reroute_006_2.outputs[0], reroute_013.inputs[0])
    hole.links.new(math_001_3.outputs[0], math_002_2.inputs[0])
    hole.links.new(convex_hull.outputs[0], transform_geometry_003.inputs[0])
    hole.links.new(transform_geometry_003.outputs[0], transform_geometry_002.inputs[0])
    hole.links.new(vector_math_002.outputs[0], transform_geometry_002.inputs[1])
    hole.links.new(vector_math_001_2.outputs[0], transform_geometry_003.inputs[1])
    hole.links.new(align_euler_to_vector.outputs[0], transform_geometry_003.inputs[2])
    hole.links.new(is_shade_smooth.outputs[0], attribute_statistic_001.inputs[2])
    hole.links.new(attribute_statistic_001.outputs[1], set_shade_smooth_1.inputs[2])
    hole.links.new(capture_attribute_001.outputs[1], vector_math_006.inputs[0])
    hole.links.new(normal_003.outputs[0], capture_attribute_002.inputs[1])
    hole.links.new(capture_attribute_002.outputs[1], compare_1.inputs[4])
    hole.links.new(capture_attribute_002.outputs[0], extrude_mesh.inputs[0])
    hole.links.new(compare_1.outputs[0], extrude_mesh.inputs[1])
    hole.links.new(vector_math_013.outputs[0], extrude_mesh.inputs[2])
    hole.links.new(reroute_008_1.outputs[0], vector_math_013.inputs[0])
    hole.links.new(reroute_010.outputs[0], vector_math_013.inputs[3])
    hole.links.new(transform_geometry_002.outputs[0], capture_attribute_002.inputs[0])
    hole.links.new(set_shade_smooth_1.outputs[0], switch_001_1.inputs[1])
    hole.links.new(switch_001_1.outputs[0], capture_attribute_003.inputs[0])
    hole.links.new(group_input_013_1.outputs[14], switch_001_1.inputs[0])
    hole.links.new(reroute_018.outputs[0], compare_003_1.inputs[5])
    hole.links.new(reroute_008_1.outputs[0], compare_1.inputs[5])
    hole.links.new(extrude_mesh.outputs[0], switch_001_1.inputs[2])
    hole.links.new(group_input_011_1.outputs[1], random_value_003_1.inputs[8])
    hole.links.new(integer_003_1.outputs[0], random_value_003_1.inputs[7])
    hole.links.new(random_value_003_1.outputs[1], combine_xyz_002.inputs[2])
    hole.links.new(combine_xyz_002.outputs[0], euler_to_rotation.inputs[0])
    hole.links.new(group_input_018.outputs[2], object_info_002.inputs[0])
    hole.links.new(group_001.outputs[0], transform_geometry_004.inputs[0])
    hole.links.new(group_input_012_1.outputs[8], random_value_003_1.inputs[2])
    hole.links.new(group_input_012_1.outputs[9], random_value_003_1.inputs[3])
    hole.links.new(transform_geometry_004.outputs[0], transform_geometry_1.inputs[0])
    hole.links.new(transform_geometry_004.outputs[0], convex_hull.inputs[0])
    hole.links.new(group_input_019.outputs[2], object_info_003.inputs[0])
    hole.links.new(capture_attribute.outputs[1], compare_004_1.inputs[4])
    hole.links.new(compare_003_1.outputs[0], boolean_math.inputs[1])
    hole.links.new(compare_004_1.outputs[0], boolean_math.inputs[0])
    hole.links.new(reroute_008_1.outputs[0], reroute_018.inputs[0])
    hole.links.new(reroute_018.outputs[0], compare_004_1.inputs[5])
    hole.links.new(capture_attribute_004.outputs[0], set_position_002.inputs[0])
    hole.links.new(compare_001_1.outputs[0], set_position_002.inputs[1])
    hole.links.new(group_input_020.outputs[15], vector_math_019.inputs[3])
    hole.links.new(reroute_019.outputs[0], vector_math_019.inputs[0])
    hole.links.new(vector_math_024.outputs[0], set_position_002.inputs[3])
    hole.links.new(reroute_026.outputs[0], vector_math_022.inputs[1])
    hole.links.new(vector_math_002.outputs[0], reroute_024.inputs[0])
    hole.links.new(reroute_024.outputs[0], reroute_025.inputs[0])
    hole.links.new(set_material_1.outputs[0], group_output_3.inputs[0])
    hole.links.new(reroute_022.outputs[0], vector_math_022.inputs[0])
    hole.links.new(reroute_023.outputs[0], reroute_026.inputs[0])
    hole.links.new(group_input_022.outputs[0], raycast.inputs[0])
    hole.links.new(reroute_026.outputs[0], vector_math_023.inputs[0])
    hole.links.new(vector_math_023.outputs[0], raycast.inputs[3])
    hole.links.new(vector_math_022.outputs[0], raycast.inputs[2])
    hole.links.new(raycast.outputs[1], group_output_3.inputs[1])
    hole.links.new(combine_xyz_002.outputs[0], reroute_028.inputs[0])
    hole.links.new(mesh_boolean_002.outputs[0], raycast_001.inputs[0])
    hole.links.new(reroute_025.outputs[0], raycast_001.inputs[3])
    hole.links.new(raycast.outputs[1], raycast_001.inputs[2])
    hole.links.new(raycast_001.outputs[2], align_euler_to_vector_001.inputs[2])
    hole.links.new(reroute_028.outputs[0], align_euler_to_vector_001.inputs[0])
    hole.links.new(reroute_028.outputs[0], group_output_3.inputs[2])
    hole.links.new(align_euler_to_vector_001.outputs[0], group_output_3.inputs[4])
    hole.links.new(raycast_001.outputs[1], group_output_3.inputs[3])
    hole.links.new(capture_attribute.outputs[0], set_position_003.inputs[0])
    hole.links.new(compare_003_1.outputs[0], set_position_003.inputs[1])
    hole.links.new(vector_math_020.outputs[0], set_position_003.inputs[3])
    hole.links.new(set_position_003.outputs[0], set_shade_smooth_1.inputs[0])
    hole.links.new(boolean_math.outputs[0], set_shade_smooth_1.inputs[1])
    hole.links.new(object_info_001.outputs[2], rotation_to_euler.inputs[0])
    hole.links.new(euler_to_rotation.outputs[0], transform_geometry_004.inputs[2])
    hole.links.new(group_002.outputs[0], attribute_statistic.inputs[0])
    hole.links.new(group_002.outputs[0], attribute_statistic_001.inputs[0])
    hole.links.new(group_002.outputs[0], group_001.inputs[0])
    hole.links.new(group_input_024.outputs[1], group_002.inputs[0])
    hole.links.new(switch_1.outputs[0], mesh_boolean_002.inputs[0])
    hole.links.new(reroute_004_2.outputs[0], mesh_boolean_002.inputs[1])
    hole.links.new(vector_math_019.outputs[0], vector_math_024.inputs[0])
    hole.links.new(mesh_boolean_002.outputs[0], set_material_1.inputs[0])
    hole.links.new(group_input_017.outputs[0], mesh_boolean_001.inputs[1])
    return hole

hole = hole_node_group()


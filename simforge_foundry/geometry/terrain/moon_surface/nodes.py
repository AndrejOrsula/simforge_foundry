import bpy

def random__uniform__node_group():
    random__uniform_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Random (Uniform)")
    random__uniform_.color_tag = 'NONE'
    random__uniform_.default_group_node_width = 140
    value_socket = random__uniform_.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket.default_value = 0.0
    value_socket.min_value = -3.4028234663852886e+38
    value_socket.max_value = 3.4028234663852886e+38
    value_socket.subtype = 'NONE'
    value_socket.attribute_domain = 'POINT'
    min_socket = random__uniform_.interface.new_socket(name = "Min", in_out='INPUT', socket_type = 'NodeSocketFloat')
    min_socket.default_value = 0.0
    min_socket.min_value = -3.4028234663852886e+38
    min_socket.max_value = 3.4028234663852886e+38
    min_socket.subtype = 'NONE'
    min_socket.attribute_domain = 'POINT'
    max_socket = random__uniform_.interface.new_socket(name = "Max", in_out='INPUT', socket_type = 'NodeSocketFloat')
    max_socket.default_value = 1.0
    max_socket.min_value = -3.4028234663852886e+38
    max_socket.max_value = 3.4028234663852886e+38
    max_socket.subtype = 'NONE'
    max_socket.attribute_domain = 'POINT'
    seed_socket = random__uniform_.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket.default_value = 0
    seed_socket.min_value = -2147483648
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.hide_value = True
    offset_socket = random__uniform_.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
    offset_socket.default_value = 0
    offset_socket.min_value = 0
    offset_socket.max_value = 2147483647
    offset_socket.subtype = 'NONE'
    offset_socket.attribute_domain = 'POINT'
    group_output = random__uniform_.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    group_input = random__uniform_.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    random_value_011 = random__uniform_.nodes.new("FunctionNodeRandomValue")
    random_value_011.name = "Random Value.011"
    random_value_011.data_type = 'FLOAT'
    random__uniform_.links.new(random_value_011.outputs[1], group_output.inputs[0])
    random__uniform_.links.new(group_input.outputs[0], random_value_011.inputs[2])
    random__uniform_.links.new(group_input.outputs[1], random_value_011.inputs[3])
    random__uniform_.links.new(group_input.outputs[3], random_value_011.inputs[7])
    random__uniform_.links.new(group_input.outputs[2], random_value_011.inputs[8])
    return random__uniform_

random__uniform_ = random__uniform__node_group()

def random__normal__node_group():
    random__normal_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Random (Normal)")
    random__normal_.color_tag = 'NONE'
    random__normal_.default_group_node_width = 140
    value_socket_1 = random__normal_.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket_1.default_value = 0.0
    value_socket_1.min_value = -3.4028234663852886e+38
    value_socket_1.max_value = 3.4028234663852886e+38
    value_socket_1.subtype = 'NONE'
    value_socket_1.attribute_domain = 'POINT'
    non_negative_socket = random__normal_.interface.new_socket(name = "Non-Negative", in_out='INPUT', socket_type = 'NodeSocketBool')
    non_negative_socket.default_value = True
    non_negative_socket.attribute_domain = 'POINT'
    mean_socket = random__normal_.interface.new_socket(name = "Mean", in_out='INPUT', socket_type = 'NodeSocketFloat')
    mean_socket.default_value = 0.0
    mean_socket.min_value = -3.4028234663852886e+38
    mean_socket.max_value = 3.4028234663852886e+38
    mean_socket.subtype = 'NONE'
    mean_socket.attribute_domain = 'POINT'
    std__dev__socket = random__normal_.interface.new_socket(name = "Std. Dev.", in_out='INPUT', socket_type = 'NodeSocketFloat')
    std__dev__socket.default_value = 1.0
    std__dev__socket.min_value = 0.0
    std__dev__socket.max_value = 3.4028234663852886e+38
    std__dev__socket.subtype = 'NONE'
    std__dev__socket.attribute_domain = 'POINT'
    seed_socket_1 = random__normal_.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket_1.default_value = 0
    seed_socket_1.min_value = 0
    seed_socket_1.max_value = 2147483647
    seed_socket_1.subtype = 'NONE'
    seed_socket_1.attribute_domain = 'POINT'
    seed_socket_1.hide_value = True
    offset_socket_1 = random__normal_.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
    offset_socket_1.default_value = 0
    offset_socket_1.min_value = 0
    offset_socket_1.max_value = 2147483647
    offset_socket_1.subtype = 'NONE'
    offset_socket_1.attribute_domain = 'POINT'
    frame = random__normal_.nodes.new("NodeFrame")
    frame.name = "Frame"
    frame_003 = random__normal_.nodes.new("NodeFrame")
    frame_003.name = "Frame.003"
    frame_001 = random__normal_.nodes.new("NodeFrame")
    frame_001.name = "Frame.001"
    math_002 = random__normal_.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'MULTIPLY'
    math_002.use_clamp = False
    math_002.inputs[1].default_value = 6.2831854820251465
    random_value_001 = random__normal_.nodes.new("FunctionNodeRandomValue")
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = 'FLOAT'
    random_value_001.inputs[2].default_value = 0.0
    random_value_001.inputs[3].default_value = 1.0
    math_010 = random__normal_.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.operation = 'ADD'
    math_010.use_clamp = False
    math_010.inputs[1].hide = True
    math_010.inputs[2].hide = True
    math_010.inputs[1].default_value = 1.0
    math_005 = random__normal_.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'MULTIPLY'
    math_005.use_clamp = False
    math_004 = random__normal_.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'COSINE'
    math_004.use_clamp = False
    math_008 = random__normal_.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.operation = 'MULTIPLY'
    math_008.use_clamp = False
    math_007 = random__normal_.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = 'ADD'
    math_007.use_clamp = False
    math = random__normal_.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'LOGARITHM'
    math.use_clamp = False
    math.inputs[1].default_value = 2.7182817459106445
    random_value_002 = random__normal_.nodes.new("FunctionNodeRandomValue")
    random_value_002.name = "Random Value.002"
    random_value_002.data_type = 'FLOAT'
    random_value_002.inputs[2].default_value = 0.0
    random_value_002.inputs[3].default_value = 1.0
    math_001 = random__normal_.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'MULTIPLY'
    math_001.use_clamp = False
    math_001.inputs[1].default_value = -2.0
    math_003 = random__normal_.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'SQRT'
    math_003.use_clamp = False
    group_output_1 = random__normal_.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True
    group_input_1 = random__normal_.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"
    switch = random__normal_.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'FLOAT'
    math_006 = random__normal_.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'MAXIMUM'
    math_006.use_clamp = False
    math_006.inputs[1].default_value = 0.0
    math_002.parent = frame
    random_value_001.parent = frame
    math_010.parent = frame
    math_005.parent = frame_003
    math_004.parent = frame_003
    math.parent = frame_001
    random_value_002.parent = frame_001
    math_001.parent = frame_001
    math_003.parent = frame_001
    random__normal_.links.new(random_value_002.outputs[1], math.inputs[0])
    random__normal_.links.new(math.outputs[0], math_001.inputs[0])
    random__normal_.links.new(random_value_001.outputs[1], math_002.inputs[0])
    random__normal_.links.new(math_002.outputs[0], math_004.inputs[0])
    random__normal_.links.new(math_003.outputs[0], math_005.inputs[0])
    random__normal_.links.new(group_input_1.outputs[3], random_value_002.inputs[8])
    random__normal_.links.new(group_input_1.outputs[3], math_010.inputs[0])
    random__normal_.links.new(math_010.outputs[0], random_value_001.inputs[8])
    random__normal_.links.new(group_input_1.outputs[2], math_008.inputs[0])
    random__normal_.links.new(group_input_1.outputs[1], math_007.inputs[0])
    random__normal_.links.new(math_008.outputs[0], math_007.inputs[1])
    random__normal_.links.new(math_005.outputs[0], math_008.inputs[1])
    random__normal_.links.new(math_004.outputs[0], math_005.inputs[1])
    random__normal_.links.new(math_001.outputs[0], math_003.inputs[0])
    random__normal_.links.new(group_input_1.outputs[4], random_value_001.inputs[7])
    random__normal_.links.new(group_input_1.outputs[4], random_value_002.inputs[7])
    random__normal_.links.new(group_input_1.outputs[0], switch.inputs[0])
    random__normal_.links.new(math_007.outputs[0], math_006.inputs[0])
    random__normal_.links.new(switch.outputs[0], group_output_1.inputs[0])
    random__normal_.links.new(math_007.outputs[0], switch.inputs[1])
    random__normal_.links.new(math_006.outputs[0], switch.inputs[2])
    return random__normal_

random__normal_ = random__normal__node_group()

def lunarrock_node_group():
    lunarrock = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "LunarRock")
    lunarrock.color_tag = 'GEOMETRY'
    lunarrock.default_group_node_width = 140
    lunarrock.is_modifier = True
    geometry_socket = lunarrock.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    seed_socket_2 = lunarrock.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket_2.default_value = 0
    seed_socket_2.min_value = 0
    seed_socket_2.max_value = 2147483647
    seed_socket_2.subtype = 'NONE'
    seed_socket_2.attribute_domain = 'POINT'
    seed_socket_2.force_non_field = True
    subdivisions_socket = lunarrock.interface.new_socket(name = "Subdivisions", in_out='INPUT', socket_type = 'NodeSocketInt')
    subdivisions_socket.default_value = 4
    subdivisions_socket.min_value = 0
    subdivisions_socket.max_value = 10
    subdivisions_socket.subtype = 'NONE'
    subdivisions_socket.attribute_domain = 'POINT'
    subdivisions_socket.force_non_field = True
    scale_socket = lunarrock.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketVector')
    scale_socket.default_value = (1.0, 1.0, 1.0)
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'XYZ'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.force_non_field = True
    scale_std_socket = lunarrock.interface.new_socket(name = "Scale STD", in_out='INPUT', socket_type = 'NodeSocketVector')
    scale_std_socket.default_value = (0.0, 0.0, 0.0)
    scale_std_socket.min_value = 0.0
    scale_std_socket.max_value = 3.4028234663852886e+38
    scale_std_socket.subtype = 'XYZ'
    scale_std_socket.attribute_domain = 'POINT'
    scale_std_socket.force_non_field = True
    horizontal_cut_socket = lunarrock.interface.new_socket(name = "Horizontal Cut", in_out='INPUT', socket_type = 'NodeSocketBool')
    horizontal_cut_socket.default_value = False
    horizontal_cut_socket.attribute_domain = 'POINT'
    horizontal_cut_socket.force_non_field = True
    horizontal_cut_offset_socket = lunarrock.interface.new_socket(name = "Horizontal Cut Offset", in_out='INPUT', socket_type = 'NodeSocketFloat')
    horizontal_cut_offset_socket.default_value = 0.0
    horizontal_cut_offset_socket.min_value = -3.4028234663852886e+38
    horizontal_cut_offset_socket.max_value = 3.4028234663852886e+38
    horizontal_cut_offset_socket.subtype = 'DISTANCE'
    horizontal_cut_offset_socket.attribute_domain = 'POINT'
    horizontal_cut_offset_socket.force_non_field = True
    group_input_2 = lunarrock.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"
    group_output_2 = lunarrock.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True
    set_material = lunarrock.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.inputs[1].default_value = True
    if "MoonRockMat" in bpy.data.materials:
        set_material.inputs[2].default_value = bpy.data.materials["MoonRockMat"]
    cube = lunarrock.nodes.new("GeometryNodeMeshCube")
    cube.name = "Cube"
    cube.inputs[0].default_value = (1.0, 1.0, 1.0)
    cube.inputs[1].default_value = 2
    cube.inputs[2].default_value = 2
    cube.inputs[3].default_value = 2
    subdivision_surface = lunarrock.nodes.new("GeometryNodeSubdivisionSurface")
    subdivision_surface.name = "Subdivision Surface"
    subdivision_surface.boundary_smooth = 'ALL'
    subdivision_surface.uv_smooth = 'PRESERVE_BOUNDARIES'
    set_position = lunarrock.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.inputs[1].hide = True
    set_position.inputs[3].hide = True
    set_position.inputs[1].default_value = True
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
    voronoi_texture = lunarrock.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = 'EUCLIDEAN'
    voronoi_texture.feature = 'SMOOTH_F1'
    voronoi_texture.normalize = True
    voronoi_texture.voronoi_dimensions = '4D'
    voronoi_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    voronoi_texture.inputs[6].default_value = 0.0
    voronoi_texture.inputs[8].default_value = 1.0
    vector_math = lunarrock.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'MULTIPLY'
    position = lunarrock.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    map_range = lunarrock.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = False
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    map_range.inputs[1].default_value = 0.0
    map_range.inputs[2].default_value = 1.0
    map_range.inputs[3].default_value = 0.3333333432674408
    map_range.inputs[4].default_value = 1.0
    set_position_001 = lunarrock.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.inputs[1].hide = True
    set_position_001.inputs[3].hide = True
    set_position_001.inputs[1].default_value = True
    set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)
    vector_math_001 = lunarrock.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'MULTIPLY'
    position_001 = lunarrock.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    noise_texture = lunarrock.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '4D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    noise_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    noise_texture.inputs[3].default_value = 15.0
    set_shade_smooth = lunarrock.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    set_shade_smooth.inputs[1].default_value = True
    set_shade_smooth.inputs[2].default_value = True
    frame_1 = lunarrock.nodes.new("NodeFrame")
    frame_1.name = "Frame"
    frame_001_1 = lunarrock.nodes.new("NodeFrame")
    frame_001_1.name = "Frame.001"
    frame_001_1.hide = True
    frame_002 = lunarrock.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    reroute_001 = lunarrock.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketFloat"
    transform_geometry = lunarrock.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = 'COMPONENTS'
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[4].hide = True
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    reroute_002 = lunarrock.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.socket_idname = "NodeSocketInt"
    attribute_statistic = lunarrock.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic.name = "Attribute Statistic"
    attribute_statistic.data_type = 'FLOAT_VECTOR'
    attribute_statistic.domain = 'POINT'
    attribute_statistic.inputs[1].hide = True
    attribute_statistic.outputs[0].hide = True
    attribute_statistic.outputs[1].hide = True
    attribute_statistic.outputs[2].hide = True
    attribute_statistic.outputs[6].hide = True
    attribute_statistic.outputs[7].hide = True
    attribute_statistic.inputs[1].default_value = True
    position_002 = lunarrock.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"
    reroute_003 = lunarrock.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.socket_idname = "NodeSocketGeometry"
    vector_math_002 = lunarrock.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'DIVIDE'
    vector_math_002.inputs[0].default_value = (1.0, 1.0, 1.0)
    vector_math_003 = lunarrock.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = 'ADD'
    vector_math_004 = lunarrock.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.operation = 'SCALE'
    vector_math_004.inputs[3].default_value = -0.5
    group = lunarrock.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = random__normal_
    group.inputs[0].default_value = True
    group.inputs[1].default_value = 2.25
    group.inputs[2].default_value = 0.3333333432674408
    group.inputs[4].default_value = 9799
    group_001 = lunarrock.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = random__uniform_
    group_001.inputs[0].default_value = -100000000.0
    group_001.inputs[1].default_value = 1000000000.0
    group_001.inputs[3].default_value = 10074
    group_002 = lunarrock.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = random__normal_
    group_002.inputs[0].default_value = True
    group_002.inputs[1].default_value = 1.0
    group_002.inputs[2].default_value = 0.25
    group_002.inputs[4].default_value = 8856
    group_004 = lunarrock.nodes.new("GeometryNodeGroup")
    group_004.name = "Group.004"
    group_004.node_tree = random__normal_
    group_004.inputs[0].default_value = True
    group_004.inputs[1].default_value = 1.25
    group_004.inputs[2].default_value = 0.25
    group_004.inputs[4].default_value = 2182
    float_curve = lunarrock.nodes.new("ShaderNodeFloatCurve")
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
    float_curve_curve_0_point_1.location = (0.3333333432674408, 0.10000000149011612)
    float_curve_curve_0_point_1.handle_type = 'AUTO_CLAMPED'
    float_curve_curve_0_point_2 = float_curve_curve_0.points.new(1.0, 1.0)
    float_curve_curve_0_point_2.handle_type = 'AUTO'
    float_curve.mapping.update()
    float_curve.inputs[0].default_value = 1.0
    group_005 = lunarrock.nodes.new("GeometryNodeGroup")
    group_005.name = "Group.005"
    group_005.node_tree = random__normal_
    group_005.inputs[0].default_value = True
    group_005.inputs[1].default_value = 0.25
    group_005.inputs[2].default_value = 0.10000000149011612
    group_005.inputs[4].default_value = 2227
    reroute_005 = lunarrock.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.socket_idname = "NodeSocketFloat"
    group_003 = lunarrock.nodes.new("GeometryNodeGroup")
    group_003.name = "Group.003"
    group_003.node_tree = random__normal_
    group_003.inputs[0].default_value = True
    group_003.inputs[1].default_value = 0.15000000596046448
    group_003.inputs[2].default_value = 0.02500000037252903
    group_003.inputs[4].default_value = 21973
    group_006 = lunarrock.nodes.new("GeometryNodeGroup")
    group_006.name = "Group.006"
    group_006.node_tree = random__normal_
    group_006.inputs[0].default_value = True
    group_006.inputs[1].default_value = 0.20000000298023224
    group_006.inputs[2].default_value = 0.05000000074505806
    group_006.inputs[4].default_value = 14855
    reroute_006 = lunarrock.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.socket_idname = "NodeSocketFloat"
    reroute = lunarrock.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketVectorXYZ"
    group_007 = lunarrock.nodes.new("GeometryNodeGroup")
    group_007.name = "Group.007"
    group_007.node_tree = random__uniform_
    group_007.inputs[0].default_value = -100000000.0
    group_007.inputs[1].default_value = 1000000000.0
    group_007.inputs[3].default_value = 10781
    group_008 = lunarrock.nodes.new("GeometryNodeGroup")
    group_008.name = "Group.008"
    group_008.node_tree = random__normal_
    group_008.inputs[0].default_value = True
    group_008.inputs[1].default_value = 0.07500000298023224
    group_008.inputs[2].default_value = 0.02500000037252903
    group_008.inputs[4].default_value = 3267
    group_010 = lunarrock.nodes.new("GeometryNodeGroup")
    group_010.name = "Group.010"
    group_010.node_tree = random__normal_
    group_010.inputs[0].default_value = True
    group_010.inputs[1].default_value = 0.5600000023841858
    group_010.inputs[2].default_value = 0.019999999552965164
    group_010.inputs[4].default_value = 5038
    group_011 = lunarrock.nodes.new("GeometryNodeGroup")
    group_011.name = "Group.011"
    group_011.node_tree = random__normal_
    group_011.inputs[0].default_value = True
    group_011.inputs[1].default_value = 2.4000000953674316
    group_011.inputs[2].default_value = 0.20000000298023224
    group_011.inputs[4].default_value = 3147
    group_012 = lunarrock.nodes.new("GeometryNodeGroup")
    group_012.name = "Group.012"
    group_012.node_tree = random__normal_
    group_012.inputs[0].default_value = True
    group_012.inputs[1].default_value = 0.05000000074505806
    group_012.inputs[2].default_value = 0.009999999776482582
    group_012.inputs[4].default_value = 3622
    frame_003_1 = lunarrock.nodes.new("NodeFrame")
    frame_003_1.name = "Frame.003"
    transform_geometry_001 = lunarrock.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    transform_geometry_001.inputs[1].hide = True
    transform_geometry_001.inputs[3].hide = True
    transform_geometry_001.inputs[4].hide = True
    transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
    random_value = lunarrock.nodes.new("FunctionNodeRandomValue")
    random_value.name = "Random Value"
    random_value.data_type = 'FLOAT_VECTOR'
    random_value.inputs[0].hide = True
    random_value.inputs[1].hide = True
    random_value.inputs[2].hide = True
    random_value.inputs[3].hide = True
    random_value.inputs[4].hide = True
    random_value.inputs[5].hide = True
    random_value.inputs[6].hide = True
    random_value.outputs[1].hide = True
    random_value.outputs[2].hide = True
    random_value.outputs[3].hide = True
    random_value.inputs[0].default_value = (-3.1415927410125732, -3.1415927410125732, -3.1415927410125732)
    random_value.inputs[1].default_value = (3.1415927410125732, 3.1415927410125732, 3.1415927410125732)
    integer = lunarrock.nodes.new("FunctionNodeInputInt")
    integer.name = "Integer"
    integer.integer = 424242
    delete_geometry = lunarrock.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'FACE'
    delete_geometry.mode = 'ALL'
    compare = lunarrock.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'EQUAL'
    compare.inputs[12].default_value = 0.0010000000474974513
    position_004 = lunarrock.nodes.new("GeometryNodeInputPosition")
    position_004.name = "Position.004"
    separate_xyz_001 = lunarrock.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"
    separate_xyz_001.outputs[0].hide = True
    separate_xyz_001.outputs[1].hide = True
    normal_001 = lunarrock.nodes.new("GeometryNodeInputNormal")
    normal_001.name = "Normal.001"
    boolean_math = lunarrock.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = 'AND'
    separate_xyz_002 = lunarrock.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002.name = "Separate XYZ.002"
    separate_xyz_002.outputs[0].hide = True
    separate_xyz_002.outputs[1].hide = True
    compare_001 = lunarrock.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = 'FLOAT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'
    compare_001.inputs[1].default_value = -1.0
    compare_001.inputs[12].default_value = 0.0010000000474974513
    mesh_boolean = lunarrock.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean.name = "Mesh Boolean"
    mesh_boolean.operation = 'DIFFERENCE'
    mesh_boolean.solver = 'FLOAT'
    mesh_boolean.inputs[2].default_value = False
    mesh_boolean.inputs[3].default_value = False
    switch_1 = lunarrock.nodes.new("GeometryNodeSwitch")
    switch_1.name = "Switch"
    switch_1.input_type = 'GEOMETRY'
    transform_geometry_002 = lunarrock.nodes.new("GeometryNodeTransform")
    transform_geometry_002.name = "Transform Geometry.002"
    transform_geometry_002.mode = 'COMPONENTS'
    transform_geometry_002.inputs[2].hide = True
    transform_geometry_002.inputs[3].hide = True
    transform_geometry_002.inputs[4].hide = True
    transform_geometry_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_002.inputs[3].default_value = (1.0, 1.0, 1.0)
    combine_xyz = lunarrock.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.inputs[0].default_value = 0.0
    combine_xyz.inputs[1].default_value = 0.0
    reroute_010 = lunarrock.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.socket_idname = "NodeSocketBool"
    cube_001 = lunarrock.nodes.new("GeometryNodeMeshCube")
    cube_001.name = "Cube.001"
    cube_001.inputs[0].default_value = (2.0, 2.0, 2.0)
    cube_001.inputs[1].default_value = 2
    cube_001.inputs[2].default_value = 2
    cube_001.inputs[3].default_value = 2
    math_1 = lunarrock.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = 'SUBTRACT'
    math_1.use_clamp = False
    math_1.inputs[1].default_value = 1.0
    reroute_004 = lunarrock.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.socket_idname = "NodeSocketGeometry"
    frame_004 = lunarrock.nodes.new("NodeFrame")
    frame_004.name = "Frame.004"
    reroute_012 = lunarrock.nodes.new("NodeReroute")
    reroute_012.name = "Reroute.012"
    reroute_012.socket_idname = "NodeSocketFloatDistance"
    reroute_013 = lunarrock.nodes.new("NodeReroute")
    reroute_013.name = "Reroute.013"
    reroute_013.socket_idname = "NodeSocketFloatDistance"
    transform_geometry_003 = lunarrock.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.mode = 'COMPONENTS'
    transform_geometry_003.inputs[1].hide = True
    transform_geometry_003.inputs[2].hide = True
    transform_geometry_003.inputs[4].hide = True
    transform_geometry_003.inputs[1].default_value = (0.0, 0.0, 0.0)
    transform_geometry_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    combine_xyz_001 = lunarrock.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    group_009 = lunarrock.nodes.new("GeometryNodeGroup")
    group_009.name = "Group.009"
    group_009.node_tree = random__normal_
    group_009.inputs[0].default_value = True
    group_009.inputs[4].default_value = 31680
    group_013 = lunarrock.nodes.new("GeometryNodeGroup")
    group_013.name = "Group.013"
    group_013.node_tree = random__normal_
    group_013.inputs[0].default_value = True
    group_013.inputs[4].default_value = 32260
    group_014 = lunarrock.nodes.new("GeometryNodeGroup")
    group_014.name = "Group.014"
    group_014.node_tree = random__normal_
    group_014.inputs[0].default_value = True
    group_014.inputs[4].default_value = 40590
    reroute_015 = lunarrock.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    reroute_015.socket_idname = "NodeSocketFloat"
    separate_xyz = lunarrock.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz_003 = lunarrock.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_003.name = "Separate XYZ.003"
    reroute_017 = lunarrock.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    reroute_017.socket_idname = "NodeSocketVectorXYZ"
    reroute_018 = lunarrock.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    reroute_018.socket_idname = "NodeSocketVectorXYZ"
    reroute_019 = lunarrock.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    reroute_019.socket_idname = "NodeSocketVectorXYZ"
    reroute_020 = lunarrock.nodes.new("NodeReroute")
    reroute_020.name = "Reroute.020"
    reroute_020.socket_idname = "NodeSocketFloat"
    reroute_021 = lunarrock.nodes.new("NodeReroute")
    reroute_021.name = "Reroute.021"
    reroute_021.socket_idname = "NodeSocketBool"
    reroute_022 = lunarrock.nodes.new("NodeReroute")
    reroute_022.name = "Reroute.022"
    reroute_022.socket_idname = "NodeSocketFloatDistance"
    frame_005 = lunarrock.nodes.new("NodeFrame")
    frame_005.name = "Frame.005"
    math_001_1 = lunarrock.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = 'ADD'
    math_001_1.use_clamp = False
    integer_001 = lunarrock.nodes.new("FunctionNodeInputInt")
    integer_001.name = "Integer.001"
    integer_001.integer = 0
    cube.parent = frame_002
    subdivision_surface.parent = frame_002
    set_position.parent = frame_1
    voronoi_texture.parent = frame_1
    vector_math.parent = frame_1
    position.parent = frame_1
    map_range.parent = frame_1
    set_position_001.parent = frame_001_1
    vector_math_001.parent = frame_001_1
    position_001.parent = frame_001_1
    noise_texture.parent = frame_001_1
    reroute_001.parent = frame_001_1
    transform_geometry.parent = frame_003_1
    reroute_002.parent = frame_002
    attribute_statistic.parent = frame_003_1
    position_002.parent = frame_003_1
    reroute_003.parent = frame_003_1
    vector_math_002.parent = frame_003_1
    vector_math_003.parent = frame_003_1
    vector_math_004.parent = frame_003_1
    group.parent = frame_1
    group_001.parent = frame_1
    group_002.parent = frame_1
    group_004.parent = frame_1
    float_curve.parent = frame_1
    group_005.parent = frame_1
    reroute_005.parent = frame_1
    group_003.parent = frame_002
    group_006.parent = frame_002
    reroute_006.parent = frame_002
    group_007.parent = frame_001_1
    group_008.parent = frame_001_1
    group_010.parent = frame_001_1
    group_011.parent = frame_001_1
    group_012.parent = frame_001_1
    transform_geometry_001.parent = frame_002
    random_value.parent = frame_002
    integer.parent = frame_002
    delete_geometry.parent = frame_004
    compare.parent = frame_004
    position_004.parent = frame_004
    separate_xyz_001.parent = frame_004
    normal_001.parent = frame_004
    boolean_math.parent = frame_004
    separate_xyz_002.parent = frame_004
    compare_001.parent = frame_004
    mesh_boolean.parent = frame_004
    switch_1.parent = frame_004
    transform_geometry_002.parent = frame_004
    combine_xyz.parent = frame_004
    cube_001.parent = frame_004
    math_1.parent = frame_004
    reroute_004.parent = frame_004
    reroute_012.parent = frame_004
    transform_geometry_003.parent = frame_005
    combine_xyz_001.parent = frame_005
    group_009.parent = frame_005
    group_013.parent = frame_005
    group_014.parent = frame_005
    separate_xyz.parent = frame_005
    separate_xyz_003.parent = frame_005
    lunarrock.links.new(set_material.outputs[0], group_output_2.inputs[0])
    lunarrock.links.new(set_shade_smooth.outputs[0], set_material.inputs[0])
    lunarrock.links.new(reroute_002.outputs[0], subdivision_surface.inputs[1])
    lunarrock.links.new(position.outputs[0], vector_math.inputs[0])
    lunarrock.links.new(map_range.outputs[0], vector_math.inputs[1])
    lunarrock.links.new(vector_math.outputs[0], set_position.inputs[2])
    lunarrock.links.new(position_001.outputs[0], vector_math_001.inputs[0])
    lunarrock.links.new(noise_texture.outputs[0], vector_math_001.inputs[1])
    lunarrock.links.new(reroute_003.outputs[0], transform_geometry.inputs[0])
    lunarrock.links.new(math_001_1.outputs[0], reroute_001.inputs[0])
    lunarrock.links.new(position_002.outputs[0], attribute_statistic.inputs[2])
    lunarrock.links.new(set_position_001.outputs[0], reroute_003.inputs[0])
    lunarrock.links.new(reroute_003.outputs[0], attribute_statistic.inputs[0])
    lunarrock.links.new(vector_math_002.outputs[0], transform_geometry.inputs[3])
    lunarrock.links.new(attribute_statistic.outputs[5], vector_math_002.inputs[1])
    lunarrock.links.new(vector_math_004.outputs[0], transform_geometry.inputs[1])
    lunarrock.links.new(vector_math_003.outputs[0], vector_math_004.inputs[0])
    lunarrock.links.new(attribute_statistic.outputs[3], vector_math_003.inputs[0])
    lunarrock.links.new(attribute_statistic.outputs[4], vector_math_003.inputs[1])
    lunarrock.links.new(group_001.outputs[0], voronoi_texture.inputs[1])
    lunarrock.links.new(reroute_005.outputs[0], group_001.inputs[2])
    lunarrock.links.new(group.outputs[0], voronoi_texture.inputs[2])
    lunarrock.links.new(group_002.outputs[0], voronoi_texture.inputs[3])
    lunarrock.links.new(group_004.outputs[0], voronoi_texture.inputs[5])
    lunarrock.links.new(reroute_005.outputs[0], group.inputs[3])
    lunarrock.links.new(reroute_005.outputs[0], group_002.inputs[3])
    lunarrock.links.new(reroute_005.outputs[0], group_004.inputs[3])
    lunarrock.links.new(subdivision_surface.outputs[0], set_position.inputs[0])
    lunarrock.links.new(set_position.outputs[0], set_position_001.inputs[0])
    lunarrock.links.new(float_curve.outputs[0], map_range.inputs[0])
    lunarrock.links.new(voronoi_texture.outputs[0], float_curve.inputs[1])
    lunarrock.links.new(reroute_005.outputs[0], group_005.inputs[3])
    lunarrock.links.new(group_005.outputs[0], voronoi_texture.inputs[4])
    lunarrock.links.new(math_001_1.outputs[0], reroute_005.inputs[0])
    lunarrock.links.new(reroute_006.outputs[0], group_003.inputs[3])
    lunarrock.links.new(reroute_006.outputs[0], group_006.inputs[3])
    lunarrock.links.new(group_003.outputs[0], subdivision_surface.inputs[3])
    lunarrock.links.new(group_006.outputs[0], subdivision_surface.inputs[2])
    lunarrock.links.new(math_001_1.outputs[0], reroute_006.inputs[0])
    lunarrock.links.new(group_input_2.outputs[2], reroute.inputs[0])
    lunarrock.links.new(group_input_2.outputs[1], reroute_002.inputs[0])
    lunarrock.links.new(vector_math_001.outputs[0], set_position_001.inputs[2])
    lunarrock.links.new(reroute_001.outputs[0], group_007.inputs[2])
    lunarrock.links.new(group_007.outputs[0], noise_texture.inputs[1])
    lunarrock.links.new(reroute_001.outputs[0], group_008.inputs[3])
    lunarrock.links.new(reroute_001.outputs[0], group_010.inputs[3])
    lunarrock.links.new(reroute_001.outputs[0], group_011.inputs[3])
    lunarrock.links.new(reroute_001.outputs[0], group_012.inputs[3])
    lunarrock.links.new(group_012.outputs[0], noise_texture.inputs[8])
    lunarrock.links.new(group_010.outputs[0], noise_texture.inputs[4])
    lunarrock.links.new(group_011.outputs[0], noise_texture.inputs[5])
    lunarrock.links.new(group_008.outputs[0], noise_texture.inputs[2])
    lunarrock.links.new(integer.outputs[0], random_value.inputs[7])
    lunarrock.links.new(random_value.outputs[0], transform_geometry_001.inputs[2])
    lunarrock.links.new(transform_geometry_001.outputs[0], subdivision_surface.inputs[0])
    lunarrock.links.new(cube.outputs[0], transform_geometry_001.inputs[0])
    lunarrock.links.new(math_001_1.outputs[0], random_value.inputs[8])
    lunarrock.links.new(mesh_boolean.outputs[0], delete_geometry.inputs[0])
    lunarrock.links.new(position_004.outputs[0], compare.inputs[4])
    lunarrock.links.new(separate_xyz_001.outputs[2], compare.inputs[0])
    lunarrock.links.new(normal_001.outputs[0], separate_xyz_002.inputs[0])
    lunarrock.links.new(separate_xyz_002.outputs[2], compare_001.inputs[0])
    lunarrock.links.new(boolean_math.outputs[0], delete_geometry.inputs[1])
    lunarrock.links.new(reroute_004.outputs[0], mesh_boolean.inputs[0])
    lunarrock.links.new(transform_geometry_002.outputs[0], mesh_boolean.inputs[1])
    lunarrock.links.new(position_004.outputs[0], separate_xyz_001.inputs[0])
    lunarrock.links.new(reroute_021.outputs[0], switch_1.inputs[0])
    lunarrock.links.new(transform_geometry_003.outputs[0], set_shade_smooth.inputs[0])
    lunarrock.links.new(reroute_004.outputs[0], switch_1.inputs[1])
    lunarrock.links.new(delete_geometry.outputs[0], switch_1.inputs[2])
    lunarrock.links.new(math_1.outputs[0], combine_xyz.inputs[2])
    lunarrock.links.new(reroute_012.outputs[0], compare.inputs[1])
    lunarrock.links.new(group_input_2.outputs[4], reroute_010.inputs[0])
    lunarrock.links.new(compare_001.outputs[0], boolean_math.inputs[0])
    lunarrock.links.new(compare.outputs[0], boolean_math.inputs[1])
    lunarrock.links.new(cube_001.outputs[0], transform_geometry_002.inputs[0])
    lunarrock.links.new(combine_xyz.outputs[0], transform_geometry_002.inputs[1])
    lunarrock.links.new(reroute_012.outputs[0], math_1.inputs[0])
    lunarrock.links.new(transform_geometry.outputs[0], reroute_004.inputs[0])
    lunarrock.links.new(reroute_022.outputs[0], reroute_012.inputs[0])
    lunarrock.links.new(group_input_2.outputs[5], reroute_013.inputs[0])
    lunarrock.links.new(switch_1.outputs[0], transform_geometry_003.inputs[0])
    lunarrock.links.new(group_009.outputs[0], combine_xyz_001.inputs[0])
    lunarrock.links.new(group_013.outputs[0], combine_xyz_001.inputs[1])
    lunarrock.links.new(group_014.outputs[0], combine_xyz_001.inputs[2])
    lunarrock.links.new(combine_xyz_001.outputs[0], transform_geometry_003.inputs[3])
    lunarrock.links.new(math_001_1.outputs[0], reroute_015.inputs[0])
    lunarrock.links.new(reroute_020.outputs[0], group_013.inputs[3])
    lunarrock.links.new(reroute_020.outputs[0], group_009.inputs[3])
    lunarrock.links.new(reroute_020.outputs[0], group_014.inputs[3])
    lunarrock.links.new(reroute_019.outputs[0], separate_xyz_003.inputs[0])
    lunarrock.links.new(separate_xyz_003.outputs[0], group_009.inputs[2])
    lunarrock.links.new(separate_xyz_003.outputs[1], group_013.inputs[2])
    lunarrock.links.new(separate_xyz_003.outputs[2], group_014.inputs[2])
    lunarrock.links.new(separate_xyz.outputs[0], group_009.inputs[1])
    lunarrock.links.new(separate_xyz.outputs[1], group_013.inputs[1])
    lunarrock.links.new(separate_xyz.outputs[2], group_014.inputs[1])
    lunarrock.links.new(reroute_018.outputs[0], separate_xyz.inputs[0])
    lunarrock.links.new(group_input_2.outputs[3], reroute_017.inputs[0])
    lunarrock.links.new(reroute.outputs[0], reroute_018.inputs[0])
    lunarrock.links.new(reroute_017.outputs[0], reroute_019.inputs[0])
    lunarrock.links.new(reroute_015.outputs[0], reroute_020.inputs[0])
    lunarrock.links.new(reroute_010.outputs[0], reroute_021.inputs[0])
    lunarrock.links.new(reroute_013.outputs[0], reroute_022.inputs[0])
    lunarrock.links.new(group_input_2.outputs[0], math_001_1.inputs[0])
    lunarrock.links.new(integer_001.outputs[0], math_001_1.inputs[1])
    return lunarrock

lunarrock = lunarrock_node_group()

def crater_profile_node_group():
    crater_profile = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Crater Profile")
    crater_profile.color_tag = 'NONE'
    crater_profile.default_group_node_width = 140
    value_socket_2 = crater_profile.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket_2.default_value = 0.0
    value_socket_2.min_value = -3.4028234663852886e+38
    value_socket_2.max_value = 3.4028234663852886e+38
    value_socket_2.subtype = 'NONE'
    value_socket_2.attribute_domain = 'POINT'
    value_socket_3 = crater_profile.interface.new_socket(name = "Value", in_out='INPUT', socket_type = 'NodeSocketFloat')
    value_socket_3.default_value = 1.0
    value_socket_3.min_value = -3.4028234663852886e+38
    value_socket_3.max_value = 3.4028234663852886e+38
    value_socket_3.subtype = 'NONE'
    value_socket_3.attribute_domain = 'POINT'
    crater_radius_fraction_socket = crater_profile.interface.new_socket(name = "Crater Radius Fraction", in_out='INPUT', socket_type = 'NodeSocketFloat')
    crater_radius_fraction_socket.default_value = 0.0
    crater_radius_fraction_socket.min_value = 1.0
    crater_radius_fraction_socket.max_value = 3.4028234663852886e+38
    crater_radius_fraction_socket.subtype = 'FACTOR'
    crater_radius_fraction_socket.attribute_domain = 'POINT'
    max_crater_radius_socket = crater_profile.interface.new_socket(name = "Max Crater Radius", in_out='INPUT', socket_type = 'NodeSocketFloat')
    max_crater_radius_socket.default_value = 0.0
    max_crater_radius_socket.min_value = -3.4028234663852886e+38
    max_crater_radius_socket.max_value = 3.4028234663852886e+38
    max_crater_radius_socket.subtype = 'NONE'
    max_crater_radius_socket.attribute_domain = 'POINT'
    seed_socket_3 = crater_profile.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket_3.default_value = 0
    seed_socket_3.min_value = 0
    seed_socket_3.max_value = 2147483647
    seed_socket_3.subtype = 'NONE'
    seed_socket_3.attribute_domain = 'POINT'
    seed_socket_3.force_non_field = True
    group_output_3 = crater_profile.nodes.new("NodeGroupOutput")
    group_output_3.name = "Group Output"
    group_output_3.is_active_output = True
    group_input_3 = crater_profile.nodes.new("NodeGroupInput")
    group_input_3.name = "Group Input"
    noise_texture_011 = crater_profile.nodes.new("ShaderNodeTexNoise")
    noise_texture_011.name = "Noise Texture.011"
    noise_texture_011.noise_dimensions = '4D'
    noise_texture_011.noise_type = 'FBM'
    noise_texture_011.normalize = True
    noise_texture_011.inputs[0].default_value = (0.0, 0.0, 0.0)
    noise_texture_011.inputs[2].default_value = 0.05000000074505806
    noise_texture_011.inputs[3].default_value = 15.0
    noise_texture_011.inputs[8].default_value = 0.0
    group_019 = crater_profile.nodes.new("GeometryNodeGroup")
    group_019.name = "Group.019"
    group_019.node_tree = random__uniform_
    group_019.inputs[0].default_value = -100000000.0
    group_019.inputs[1].default_value = 1000000000.0
    group_019.inputs[3].default_value = 46364
    group_022 = crater_profile.nodes.new("GeometryNodeGroup")
    group_022.name = "Group.022"
    group_022.node_tree = random__normal_
    group_022.inputs[0].default_value = False
    group_022.inputs[1].default_value = 0.0
    group_022.inputs[4].default_value = 2808
    group_023 = crater_profile.nodes.new("GeometryNodeGroup")
    group_023.name = "Group.023"
    group_023.node_tree = random__normal_
    group_023.inputs[0].default_value = True
    group_023.inputs[1].default_value = 0.10000000149011612
    group_023.inputs[2].default_value = 0.02500000037252903
    group_023.inputs[4].default_value = 8508
    group_024 = crater_profile.nodes.new("GeometryNodeGroup")
    group_024.name = "Group.024"
    group_024.node_tree = random__normal_
    group_024.inputs[0].default_value = True
    group_024.inputs[1].default_value = 1.0
    group_024.inputs[2].default_value = 0.25
    group_024.inputs[4].default_value = 141
    float_to_integer = crater_profile.nodes.new("FunctionNodeFloatToInt")
    float_to_integer.name = "Float to Integer"
    float_to_integer.rounding_mode = 'ROUND'
    math_001_2 = crater_profile.nodes.new("ShaderNodeMath")
    math_001_2.name = "Math.001"
    math_001_2.operation = 'MULTIPLY'
    math_001_2.use_clamp = False
    math_001_2.inputs[2].hide = True
    reroute_002_1 = crater_profile.nodes.new("NodeReroute")
    reroute_002_1.name = "Reroute.002"
    reroute_002_1.socket_idname = "NodeSocketInt"
    integer_1 = crater_profile.nodes.new("FunctionNodeInputInt")
    integer_1.name = "Integer"
    integer_1.integer = 4
    math_003_1 = crater_profile.nodes.new("ShaderNodeMath")
    math_003_1.name = "Math.003"
    math_003_1.operation = 'ADD'
    math_003_1.use_clamp = False
    map_range_1 = crater_profile.nodes.new("ShaderNodeMapRange")
    map_range_1.name = "Map Range"
    map_range_1.clamp = True
    map_range_1.data_type = 'FLOAT'
    map_range_1.interpolation_type = 'LINEAR'
    map_range_1.inputs[1].default_value = 0.0
    map_range_1.inputs[2].default_value = 1.0
    map_range_1.inputs[3].default_value = 0.0
    group_1 = crater_profile.nodes.new("GeometryNodeGroup")
    group_1.name = "Group"
    group_1.node_tree = random__normal_
    group_1.inputs[0].default_value = True
    group_1.inputs[1].default_value = 0.0
    group_1.inputs[2].default_value = 0.25
    group_1.inputs[4].default_value = 24183
    float_curve_004 = crater_profile.nodes.new("ShaderNodeFloatCurve")
    float_curve_004.name = "Float Curve.004"
    float_curve_004.mapping.extend = 'EXTRAPOLATED'
    float_curve_004.mapping.tone = 'STANDARD'
    float_curve_004.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_004.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_004.mapping.clip_min_x = 0.0
    float_curve_004.mapping.clip_min_y = 0.0
    float_curve_004.mapping.clip_max_x = 1.0
    float_curve_004.mapping.clip_max_y = 1.0
    float_curve_004.mapping.use_clip = True
    float_curve_004_curve_0 = float_curve_004.mapping.curves[0]
    float_curve_004_curve_0_point_0 = float_curve_004_curve_0.points[0]
    float_curve_004_curve_0_point_0.location = (0.0, 0.6302875280380249)
    float_curve_004_curve_0_point_0.handle_type = 'AUTO'
    float_curve_004_curve_0_point_1 = float_curve_004_curve_0.points[1]
    float_curve_004_curve_0_point_1.location = (0.20408575236797333, 0.6508127450942993)
    float_curve_004_curve_0_point_1.handle_type = 'AUTO'
    float_curve_004_curve_0_point_2 = float_curve_004_curve_0.points.new(0.3318162262439728, 0.7192298769950867)
    float_curve_004_curve_0_point_2.handle_type = 'AUTO'
    float_curve_004_curve_0_point_3 = float_curve_004_curve_0.points.new(0.4255254566669464, 0.7699005007743835)
    float_curve_004_curve_0_point_3.handle_type = 'AUTO'
    float_curve_004_curve_0_point_4 = float_curve_004_curve_0.points.new(0.5083944797515869, 0.5437449216842651)
    float_curve_004_curve_0_point_4.handle_type = 'AUTO'
    float_curve_004_curve_0_point_5 = float_curve_004_curve_0.points.new(0.7643035054206848, 0.13317757844924927)
    float_curve_004_curve_0_point_5.handle_type = 'AUTO'
    float_curve_004_curve_0_point_6 = float_curve_004_curve_0.points.new(1.0, 0.056249916553497314)
    float_curve_004_curve_0_point_6.handle_type = 'AUTO'
    float_curve_004.mapping.update()
    float_curve_004.inputs[0].default_value = 1.0
    float_curve_005 = crater_profile.nodes.new("ShaderNodeFloatCurve")
    float_curve_005.name = "Float Curve.005"
    float_curve_005.mapping.extend = 'EXTRAPOLATED'
    float_curve_005.mapping.tone = 'STANDARD'
    float_curve_005.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_005.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_005.mapping.clip_min_x = 0.0
    float_curve_005.mapping.clip_min_y = 0.0
    float_curve_005.mapping.clip_max_x = 1.0
    float_curve_005.mapping.clip_max_y = 1.0
    float_curve_005.mapping.use_clip = True
    float_curve_005_curve_0 = float_curve_005.mapping.curves[0]
    float_curve_005_curve_0_point_0 = float_curve_005_curve_0.points[0]
    float_curve_005_curve_0_point_0.location = (0.0, 0.6241841912269592)
    float_curve_005_curve_0_point_0.handle_type = 'AUTO'
    float_curve_005_curve_0_point_1 = float_curve_005_curve_0.points[1]
    float_curve_005_curve_0_point_1.location = (0.20329293608665466, 0.6318109631538391)
    float_curve_005_curve_0_point_1.handle_type = 'AUTO'
    float_curve_005_curve_0_point_2 = float_curve_005_curve_0.points.new(0.3409092426300049, 0.6676813960075378)
    float_curve_005_curve_0_point_2.handle_type = 'AUTO_CLAMPED'
    float_curve_005_curve_0_point_3 = float_curve_005_curve_0.points.new(0.5181822776794434, 0.4260922968387604)
    float_curve_005_curve_0_point_3.handle_type = 'AUTO'
    float_curve_005_curve_0_point_4 = float_curve_005_curve_0.points.new(0.7181820273399353, 0.2250000238418579)
    float_curve_005_curve_0_point_4.handle_type = 'AUTO'
    float_curve_005_curve_0_point_5 = float_curve_005_curve_0.points.new(1.0, 0.16875003278255463)
    float_curve_005_curve_0_point_5.handle_type = 'AUTO'
    float_curve_005.mapping.update()
    float_curve_005.inputs[0].default_value = 1.0
    float_curve_006 = crater_profile.nodes.new("ShaderNodeFloatCurve")
    float_curve_006.name = "Float Curve.006"
    float_curve_006.mapping.extend = 'EXTRAPOLATED'
    float_curve_006.mapping.tone = 'STANDARD'
    float_curve_006.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_006.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_006.mapping.clip_min_x = 0.0
    float_curve_006.mapping.clip_min_y = 0.0
    float_curve_006.mapping.clip_max_x = 1.0
    float_curve_006.mapping.clip_max_y = 1.0
    float_curve_006.mapping.use_clip = True
    float_curve_006_curve_0 = float_curve_006.mapping.curves[0]
    float_curve_006_curve_0_point_0 = float_curve_006_curve_0.points[0]
    float_curve_006_curve_0_point_0.location = (0.0, 0.6725000739097595)
    float_curve_006_curve_0_point_0.handle_type = 'AUTO'
    float_curve_006_curve_0_point_1 = float_curve_006_curve_0.points[1]
    float_curve_006_curve_0_point_1.location = (0.18717996776103973, 0.6866194605827332)
    float_curve_006_curve_0_point_1.handle_type = 'AUTO'
    float_curve_006_curve_0_point_2 = float_curve_006_curve_0.points.new(0.38181814551353455, 0.7312501072883606)
    float_curve_006_curve_0_point_2.handle_type = 'AUTO'
    float_curve_006_curve_0_point_3 = float_curve_006_curve_0.points.new(0.47272729873657227, 0.7426979541778564)
    float_curve_006_curve_0_point_3.handle_type = 'AUTO'
    float_curve_006_curve_0_point_4 = float_curve_006_curve_0.points.new(0.6454547047615051, 0.24985311925411224)
    float_curve_006_curve_0_point_4.handle_type = 'AUTO'
    float_curve_006_curve_0_point_5 = float_curve_006_curve_0.points.new(1.0, 0.13730427622795105)
    float_curve_006_curve_0_point_5.handle_type = 'AUTO'
    float_curve_006.mapping.update()
    float_curve_006.inputs[0].default_value = 1.0
    float_curve_007 = crater_profile.nodes.new("ShaderNodeFloatCurve")
    float_curve_007.name = "Float Curve.007"
    float_curve_007.mapping.extend = 'EXTRAPOLATED'
    float_curve_007.mapping.tone = 'STANDARD'
    float_curve_007.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_007.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_007.mapping.clip_min_x = 0.0
    float_curve_007.mapping.clip_min_y = 0.0
    float_curve_007.mapping.clip_max_x = 1.0
    float_curve_007.mapping.clip_max_y = 1.0
    float_curve_007.mapping.use_clip = True
    float_curve_007_curve_0 = float_curve_007.mapping.curves[0]
    float_curve_007_curve_0_point_0 = float_curve_007_curve_0.points[0]
    float_curve_007_curve_0_point_0.location = (0.0, 0.7124999761581421)
    float_curve_007_curve_0_point_0.handle_type = 'AUTO'
    float_curve_007_curve_0_point_1 = float_curve_007_curve_0.points[1]
    float_curve_007_curve_0_point_1.location = (0.2611362040042877, 0.7326563000679016)
    float_curve_007_curve_0_point_1.handle_type = 'AUTO'
    float_curve_007_curve_0_point_2 = float_curve_007_curve_0.points.new(0.4363635778427124, 0.7750000953674316)
    float_curve_007_curve_0_point_2.handle_type = 'AUTO'
    float_curve_007_curve_0_point_3 = float_curve_007_curve_0.points.new(0.5954543352127075, 0.8114726543426514)
    float_curve_007_curve_0_point_3.handle_type = 'AUTO'
    float_curve_007_curve_0_point_4 = float_curve_007_curve_0.points.new(0.6954542994499207, 0.5309724807739258)
    float_curve_007_curve_0_point_4.handle_type = 'AUTO'
    float_curve_007_curve_0_point_5 = float_curve_007_curve_0.points.new(0.8590908646583557, 0.2937498986721039)
    float_curve_007_curve_0_point_5.handle_type = 'AUTO'
    float_curve_007_curve_0_point_6 = float_curve_007_curve_0.points.new(1.0, 0.24999989569187164)
    float_curve_007_curve_0_point_6.handle_type = 'AUTO'
    float_curve_007.mapping.update()
    float_curve_007.inputs[0].default_value = 1.0
    reroute_003_1 = crater_profile.nodes.new("NodeReroute")
    reroute_003_1.name = "Reroute.003"
    reroute_003_1.socket_idname = "NodeSocketFloat"
    math_005_1 = crater_profile.nodes.new("ShaderNodeMath")
    math_005_1.name = "Math.005"
    math_005_1.operation = 'MULTIPLY'
    math_005_1.use_clamp = False
    math_005_1.inputs[1].default_value = 0.5
    index_switch_001 = crater_profile.nodes.new("GeometryNodeIndexSwitch")
    index_switch_001.name = "Index Switch.001"
    index_switch_001.data_type = 'FLOAT'
    index_switch_001.index_switch_items.clear()
    index_switch_001.index_switch_items.new()
    index_switch_001.index_switch_items.new()
    index_switch_001.index_switch_items.new()
    index_switch_001.index_switch_items.new()
    index_switch_001.index_switch_items.new()
    math_2 = crater_profile.nodes.new("ShaderNodeMath")
    math_2.name = "Math"
    math_2.operation = 'MULTIPLY'
    math_2.use_clamp = False
    math_2.inputs[1].default_value = 0.05000000074505806
    math_002_1 = crater_profile.nodes.new("ShaderNodeMath")
    math_002_1.name = "Math.002"
    math_002_1.operation = 'MULTIPLY'
    math_002_1.use_clamp = False
    math_002_1.inputs[1].default_value = 0.019999999552965164
    float_curve_008 = crater_profile.nodes.new("ShaderNodeFloatCurve")
    float_curve_008.name = "Float Curve.008"
    float_curve_008.mapping.extend = 'EXTRAPOLATED'
    float_curve_008.mapping.tone = 'STANDARD'
    float_curve_008.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_008.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_008.mapping.clip_min_x = 0.0
    float_curve_008.mapping.clip_min_y = 0.0
    float_curve_008.mapping.clip_max_x = 1.0
    float_curve_008.mapping.clip_max_y = 1.0
    float_curve_008.mapping.use_clip = True
    float_curve_008_curve_0 = float_curve_008.mapping.curves[0]
    float_curve_008_curve_0_point_0 = float_curve_008_curve_0.points[0]
    float_curve_008_curve_0_point_0.location = (0.0, 0.6662500500679016)
    float_curve_008_curve_0_point_0.handle_type = 'AUTO'
    float_curve_008_curve_0_point_1 = float_curve_008_curve_0.points[1]
    float_curve_008_curve_0_point_1.location = (0.1954544186592102, 0.672716498374939)
    float_curve_008_curve_0_point_1.handle_type = 'AUTO'
    float_curve_008_curve_0_point_2 = float_curve_008_curve_0.points.new(0.38636353611946106, 0.7116192579269409)
    float_curve_008_curve_0_point_2.handle_type = 'AUTO'
    float_curve_008_curve_0_point_3 = float_curve_008_curve_0.points.new(0.7363638877868652, 0.3500000238418579)
    float_curve_008_curve_0_point_3.handle_type = 'AUTO'
    float_curve_008_curve_0_point_4 = float_curve_008_curve_0.points.new(1.0, 0.29374992847442627)
    float_curve_008_curve_0_point_4.handle_type = 'AUTO'
    float_curve_008.mapping.update()
    float_curve_008.inputs[0].default_value = 1.0
    math_004_1 = crater_profile.nodes.new("ShaderNodeMath")
    math_004_1.name = "Math.004"
    math_004_1.mute = True
    math_004_1.operation = 'INVERSE_SQRT'
    math_004_1.use_clamp = False
    crater_profile.links.new(group_019.outputs[0], noise_texture_011.inputs[1])
    crater_profile.links.new(reroute_002_1.outputs[0], group_019.inputs[2])
    crater_profile.links.new(reroute_002_1.outputs[0], group_022.inputs[3])
    crater_profile.links.new(reroute_002_1.outputs[0], group_023.inputs[3])
    crater_profile.links.new(reroute_002_1.outputs[0], group_024.inputs[3])
    crater_profile.links.new(group_input_3.outputs[1], math_001_2.inputs[0])
    crater_profile.links.new(group_input_3.outputs[2], math_001_2.inputs[1])
    crater_profile.links.new(math_005_1.outputs[0], group_output_3.inputs[0])
    crater_profile.links.new(group_input_3.outputs[3], reroute_002_1.inputs[0])
    crater_profile.links.new(integer_1.outputs[0], map_range_1.inputs[4])
    crater_profile.links.new(map_range_1.outputs[0], float_to_integer.inputs[0])
    crater_profile.links.new(group_input_3.outputs[3], group_1.inputs[3])
    crater_profile.links.new(group_1.outputs[0], math_003_1.inputs[1])
    crater_profile.links.new(math_003_1.outputs[0], map_range_1.inputs[0])
    crater_profile.links.new(group_input_3.outputs[1], math_003_1.inputs[0])
    crater_profile.links.new(group_023.outputs[0], noise_texture_011.inputs[4])
    crater_profile.links.new(group_024.outputs[0], noise_texture_011.inputs[5])
    crater_profile.links.new(reroute_003_1.outputs[0], float_curve_004.inputs[1])
    crater_profile.links.new(reroute_003_1.outputs[0], float_curve_005.inputs[1])
    crater_profile.links.new(reroute_003_1.outputs[0], float_curve_006.inputs[1])
    crater_profile.links.new(reroute_003_1.outputs[0], float_curve_007.inputs[1])
    crater_profile.links.new(group_input_3.outputs[0], reroute_003_1.inputs[0])
    crater_profile.links.new(float_curve_007.outputs[0], index_switch_001.inputs[1])
    crater_profile.links.new(float_curve_004.outputs[0], index_switch_001.inputs[2])
    crater_profile.links.new(float_curve_005.outputs[0], index_switch_001.inputs[3])
    crater_profile.links.new(float_curve_006.outputs[0], index_switch_001.inputs[4])
    crater_profile.links.new(index_switch_001.outputs[0], math_005_1.inputs[0])
    crater_profile.links.new(math_001_2.outputs[0], math_2.inputs[0])
    crater_profile.links.new(math_2.outputs[0], math_002_1.inputs[0])
    crater_profile.links.new(math_002_1.outputs[0], group_022.inputs[2])
    crater_profile.links.new(reroute_003_1.outputs[0], float_curve_008.inputs[1])
    crater_profile.links.new(float_curve_008.outputs[0], index_switch_001.inputs[5])
    crater_profile.links.new(float_to_integer.outputs[0], index_switch_001.inputs[0])
    crater_profile.links.new(math_2.outputs[0], math_004_1.inputs[0])
    return crater_profile

crater_profile = crater_profile_node_group()

def moonsurface_node_group():
    moonsurface = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "MoonSurface")
    moonsurface.color_tag = 'NONE'
    moonsurface.default_group_node_width = 140
    moonsurface.is_modifier = True
    geometry_socket_1 = moonsurface.interface.new_socket(name = "geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    seed_socket_4 = moonsurface.interface.new_socket(name = "seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket_4.default_value = 0
    seed_socket_4.min_value = 0
    seed_socket_4.max_value = 2147483647
    seed_socket_4.subtype = 'NONE'
    seed_socket_4.attribute_domain = 'POINT'
    seed_socket_4.force_non_field = True
    scale_socket_1 = moonsurface.interface.new_socket(name = "scale", in_out='INPUT', socket_type = 'NodeSocketVector')
    scale_socket_1.default_value = (10.0, 10.0, 1.0)
    scale_socket_1.min_value = 0.0
    scale_socket_1.max_value = 3.4028234663852886e+38
    scale_socket_1.subtype = 'XYZ'
    scale_socket_1.attribute_domain = 'POINT'
    scale_socket_1.force_non_field = True
    density_socket = moonsurface.interface.new_socket(name = "density", in_out='INPUT', socket_type = 'NodeSocketFloat')
    density_socket.default_value = 0.10000000149011612
    density_socket.min_value = 0.009999999776482582
    density_socket.max_value = 3.4028234663852886e+38
    density_socket.subtype = 'NONE'
    density_socket.attribute_domain = 'POINT'
    density_socket.force_non_field = True
    flat_area_size_socket = moonsurface.interface.new_socket(name = "flat_area_size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    flat_area_size_socket.default_value = 0.0
    flat_area_size_socket.min_value = 0.0
    flat_area_size_socket.max_value = 3.4028234663852886e+38
    flat_area_size_socket.subtype = 'NONE'
    flat_area_size_socket.attribute_domain = 'POINT'
    rock_mesh_boolean_enable_socket = moonsurface.interface.new_socket(name = "rock_mesh_boolean_enable", in_out='INPUT', socket_type = 'NodeSocketBool')
    rock_mesh_boolean_enable_socket.default_value = False
    rock_mesh_boolean_enable_socket.attribute_domain = 'POINT'
    rock_mesh_boolean_enable_socket.force_non_field = True
    rock_mesh_boolean_enable_socket.description = "Note: Slow"
    mat_socket = moonsurface.interface.new_socket(name = "mat", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat_socket.attribute_domain = 'POINT'
    group_input_4 = moonsurface.nodes.new("NodeGroupInput")
    group_input_4.name = "Group Input"
    group_output_4 = moonsurface.nodes.new("NodeGroupOutput")
    group_output_4.name = "Group Output"
    group_output_4.is_active_output = True
    grid = moonsurface.nodes.new("GeometryNodeMeshGrid")
    grid.name = "Grid"
    set_material_1 = moonsurface.nodes.new("GeometryNodeSetMaterial")
    set_material_1.name = "Set Material"
    set_material_1.inputs[1].default_value = True
    set_shade_smooth_1 = moonsurface.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth_1.name = "Set Shade Smooth"
    set_shade_smooth_1.domain = 'FACE'
    set_shade_smooth_1.inputs[1].default_value = True
    set_shade_smooth_1.inputs[2].default_value = True
    vector_math_012 = moonsurface.nodes.new("ShaderNodeVectorMath")
    vector_math_012.name = "Vector Math.012"
    vector_math_012.operation = 'SCALE'
    vector_math_012.inputs[3].default_value = -1.0
    raycast = moonsurface.nodes.new("GeometryNodeRaycast")
    raycast.name = "Raycast"
    raycast.data_type = 'FLOAT'
    raycast.mapping = 'NEAREST'
    raycast.inputs[1].default_value = 0.0
    raycast.inputs[3].default_value = (0.0, 0.0, -1.0)
    raycast.inputs[4].default_value = 10.0
    frame_002_1 = moonsurface.nodes.new("NodeFrame")
    frame_002_1.name = "Frame.002"
    vector_math_017 = moonsurface.nodes.new("ShaderNodeVectorMath")
    vector_math_017.name = "Vector Math.017"
    vector_math_017.operation = 'MULTIPLY'
    gradient_texture_001 = moonsurface.nodes.new("ShaderNodeTexGradient")
    gradient_texture_001.name = "Gradient Texture.001"
    gradient_texture_001.gradient_type = 'QUADRATIC_SPHERE'
    position_002_1 = moonsurface.nodes.new("GeometryNodeInputPosition")
    position_002_1.name = "Position.002"
    vector_math_019 = moonsurface.nodes.new("ShaderNodeVectorMath")
    vector_math_019.name = "Vector Math.019"
    vector_math_019.operation = 'DIVIDE'
    set_position_001_1 = moonsurface.nodes.new("GeometryNodeSetPosition")
    set_position_001_1.name = "Set Position.001"
    set_position_001_1.inputs[3].default_value = (0.0, 0.0, 0.0)
    position_003 = moonsurface.nodes.new("GeometryNodeInputPosition")
    position_003.name = "Position.003"
    combine_xyz_1 = moonsurface.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_1.name = "Combine XYZ"
    combine_xyz_1.inputs[0].default_value = 1.0
    combine_xyz_1.inputs[1].default_value = 1.0
    math_3 = moonsurface.nodes.new("ShaderNodeMath")
    math_3.name = "Math"
    math_3.operation = 'MULTIPLY'
    math_3.use_clamp = False
    math_3.inputs[1].default_value = 1.0
    frame_2 = moonsurface.nodes.new("NodeFrame")
    frame_2.name = "Frame"
    reroute_001_1 = moonsurface.nodes.new("NodeReroute")
    reroute_001_1.name = "Reroute.001"
    reroute_001_1.socket_idname = "NodeSocketGeometry"
    vector_math_002_1 = moonsurface.nodes.new("ShaderNodeVectorMath")
    vector_math_002_1.name = "Vector Math.002"
    vector_math_002_1.operation = 'DIVIDE'
    vector_math_021 = moonsurface.nodes.new("ShaderNodeVectorMath")
    vector_math_021.name = "Vector Math.021"
    vector_math_021.operation = 'CEIL'
    separate_xyz_1 = moonsurface.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_1.name = "Separate XYZ"
    separate_xyz_1.outputs[2].hide = True
    vector_math_023 = moonsurface.nodes.new("ShaderNodeVectorMath")
    vector_math_023.name = "Vector Math.023"
    vector_math_023.operation = 'MAXIMUM'
    vector_math_023.inputs[1].default_value = (2.0, 2.0, 0.0)
    frame_001_2 = moonsurface.nodes.new("NodeFrame")
    frame_001_2.name = "Frame.001"
    reroute_003_2 = moonsurface.nodes.new("NodeReroute")
    reroute_003_2.name = "Reroute.003"
    reroute_003_2.socket_idname = "NodeSocketFloat"
    compare_1 = moonsurface.nodes.new("FunctionNodeCompare")
    compare_1.name = "Compare"
    compare_1.data_type = 'FLOAT'
    compare_1.mode = 'ELEMENT'
    compare_1.operation = 'NOT_EQUAL'
    compare_1.inputs[1].default_value = 0.0
    compare_1.inputs[12].default_value = 0.0010000000474974513
    math_001_3 = moonsurface.nodes.new("ShaderNodeMath")
    math_001_3.name = "Math.001"
    math_001_3.operation = 'ADD'
    math_001_3.use_clamp = False
    math_001_3.inputs[2].hide = True
    integer_012 = moonsurface.nodes.new("FunctionNodeInputInt")
    integer_012.name = "Integer.012"
    integer_012.integer = 0
    reroute_005_1 = moonsurface.nodes.new("NodeReroute")
    reroute_005_1.name = "Reroute.005"
    reroute_005_1.socket_idname = "NodeSocketVectorXYZ"
    float_to_integer_1 = moonsurface.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_1.name = "Float to Integer"
    float_to_integer_1.rounding_mode = 'FLOOR'
    transform_geometry_001_1 = moonsurface.nodes.new("GeometryNodeTransform")
    transform_geometry_001_1.name = "Transform Geometry.001"
    transform_geometry_001_1.mode = 'COMPONENTS'
    transform_geometry_001_1.inputs[1].hide = True
    transform_geometry_001_1.inputs[2].hide = True
    transform_geometry_001_1.inputs[4].hide = True
    transform_geometry_001_1.inputs[1].default_value = (0.0, 0.0, 0.0)
    transform_geometry_001_1.inputs[2].default_value = (0.0, 0.0, 0.0)
    attribute_statistic_001 = moonsurface.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic_001.name = "Attribute Statistic.001"
    attribute_statistic_001.data_type = 'FLOAT_VECTOR'
    attribute_statistic_001.domain = 'POINT'
    attribute_statistic_001.inputs[1].hide = True
    attribute_statistic_001.outputs[0].hide = True
    attribute_statistic_001.outputs[1].hide = True
    attribute_statistic_001.outputs[2].hide = True
    attribute_statistic_001.outputs[3].hide = True
    attribute_statistic_001.outputs[4].hide = True
    attribute_statistic_001.outputs[6].hide = True
    attribute_statistic_001.outputs[7].hide = True
    attribute_statistic_001.inputs[1].default_value = True
    position_004_1 = moonsurface.nodes.new("GeometryNodeInputPosition")
    position_004_1.name = "Position.004"
    reroute_007 = moonsurface.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.socket_idname = "NodeSocketGeometry"
    vector_math_028 = moonsurface.nodes.new("ShaderNodeVectorMath")
    vector_math_028.name = "Vector Math.028"
    vector_math_028.operation = 'DIVIDE'
    frame_003_2 = moonsurface.nodes.new("NodeFrame")
    frame_003_2.name = "Frame.003"
    reroute_008 = moonsurface.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.socket_idname = "NodeSocketVectorXYZ"
    reroute_006_1 = moonsurface.nodes.new("NodeReroute")
    reroute_006_1.name = "Reroute.006"
    reroute_006_1.socket_idname = "NodeSocketFloat"
    reroute_004_1 = moonsurface.nodes.new("NodeReroute")
    reroute_004_1.name = "Reroute.004"
    reroute_004_1.socket_idname = "NodeSocketFloat"
    noise_texture_009 = moonsurface.nodes.new("ShaderNodeTexNoise")
    noise_texture_009.name = "Noise Texture.009"
    noise_texture_009.noise_dimensions = '4D'
    noise_texture_009.noise_type = 'MULTIFRACTAL'
    noise_texture_009.normalize = True
    noise_texture_009.inputs[0].default_value = (0.0, 0.0, 0.0)
    noise_texture_009.inputs[8].default_value = 0.0
    group_013_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_013_1.name = "Group.013"
    group_013_1.node_tree = random__uniform_
    group_013_1.inputs[0].default_value = -100000000.0
    group_013_1.inputs[1].default_value = 1000000000.0
    group_013_1.inputs[3].default_value = 90878
    reroute_009 = moonsurface.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.socket_idname = "NodeSocketInt"
    group_2 = moonsurface.nodes.new("GeometryNodeGroup")
    group_2.name = "Group"
    group_2.node_tree = random__normal_
    group_2.inputs[0].default_value = True
    group_2.inputs[1].default_value = 0.15000000596046448
    group_2.inputs[2].default_value = 0.02500000037252903
    group_2.inputs[4].default_value = 53330
    group_014_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_014_1.name = "Group.014"
    group_014_1.node_tree = random__normal_
    group_014_1.inputs[0].default_value = True
    group_014_1.inputs[1].default_value = 4.0
    group_014_1.inputs[2].default_value = 0.20000000298023224
    group_014_1.inputs[4].default_value = 48802
    group_015 = moonsurface.nodes.new("GeometryNodeGroup")
    group_015.name = "Group.015"
    group_015.node_tree = random__normal_
    group_015.inputs[0].default_value = True
    group_015.inputs[1].default_value = 0.699999988079071
    group_015.inputs[2].default_value = 0.10000000149011612
    group_015.inputs[4].default_value = 99201
    group_016 = moonsurface.nodes.new("GeometryNodeGroup")
    group_016.name = "Group.016"
    group_016.node_tree = random__normal_
    group_016.inputs[0].default_value = True
    group_016.inputs[1].default_value = 2.200000047683716
    group_016.inputs[2].default_value = 0.07500000298023224
    group_016.inputs[4].default_value = 6506
    frame_004_1 = moonsurface.nodes.new("NodeFrame")
    frame_004_1.name = "Frame.004"
    noise_texture_010 = moonsurface.nodes.new("ShaderNodeTexNoise")
    noise_texture_010.name = "Noise Texture.010"
    noise_texture_010.noise_dimensions = '4D'
    noise_texture_010.noise_type = 'HETERO_TERRAIN'
    noise_texture_010.normalize = True
    noise_texture_010.inputs[0].default_value = (0.0, 0.0, 0.0)
    noise_texture_010.inputs[3].default_value = 15.0
    noise_texture_010.inputs[8].default_value = 0.0
    group_017 = moonsurface.nodes.new("GeometryNodeGroup")
    group_017.name = "Group.017"
    group_017.node_tree = random__uniform_
    group_017.inputs[0].default_value = -100000000.0
    group_017.inputs[1].default_value = 1000000000.0
    group_017.inputs[3].default_value = 7859
    reroute_010_1 = moonsurface.nodes.new("NodeReroute")
    reroute_010_1.name = "Reroute.010"
    reroute_010_1.socket_idname = "NodeSocketInt"
    group_018 = moonsurface.nodes.new("GeometryNodeGroup")
    group_018.name = "Group.018"
    group_018.node_tree = random__normal_
    group_018.inputs[0].default_value = True
    group_018.inputs[1].default_value = 1.5
    group_018.inputs[2].default_value = 0.25
    group_018.inputs[4].default_value = 543
    group_020 = moonsurface.nodes.new("GeometryNodeGroup")
    group_020.name = "Group.020"
    group_020.node_tree = random__normal_
    group_020.inputs[0].default_value = True
    group_020.inputs[1].default_value = 0.22499999403953552
    group_020.inputs[2].default_value = 0.02500000037252903
    group_020.inputs[4].default_value = 10032
    group_021 = moonsurface.nodes.new("GeometryNodeGroup")
    group_021.name = "Group.021"
    group_021.node_tree = random__normal_
    group_021.inputs[0].default_value = True
    group_021.inputs[1].default_value = 3.0
    group_021.inputs[2].default_value = 0.5
    group_021.inputs[4].default_value = 6515
    frame_005_1 = moonsurface.nodes.new("NodeFrame")
    frame_005_1.name = "Frame.005"
    noise_texture_011_1 = moonsurface.nodes.new("ShaderNodeTexNoise")
    noise_texture_011_1.name = "Noise Texture.011"
    noise_texture_011_1.noise_dimensions = '4D'
    noise_texture_011_1.noise_type = 'FBM'
    noise_texture_011_1.normalize = True
    noise_texture_011_1.inputs[0].default_value = (0.0, 0.0, 0.0)
    noise_texture_011_1.inputs[3].default_value = 15.0
    noise_texture_011_1.inputs[8].default_value = 0.0
    group_019_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_019_1.name = "Group.019"
    group_019_1.node_tree = random__uniform_
    group_019_1.inputs[0].default_value = -100000000.0
    group_019_1.inputs[1].default_value = 1000000000.0
    group_019_1.inputs[3].default_value = 76322
    reroute_011 = moonsurface.nodes.new("NodeReroute")
    reroute_011.name = "Reroute.011"
    reroute_011.socket_idname = "NodeSocketInt"
    group_022_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_022_1.name = "Group.022"
    group_022_1.node_tree = random__normal_
    group_022_1.inputs[0].default_value = True
    group_022_1.inputs[1].default_value = 2.0
    group_022_1.inputs[2].default_value = 0.10000000149011612
    group_022_1.inputs[4].default_value = 23556
    group_023_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_023_1.name = "Group.023"
    group_023_1.node_tree = random__normal_
    group_023_1.inputs[0].default_value = True
    group_023_1.inputs[1].default_value = 0.18000000715255737
    group_023_1.inputs[2].default_value = 0.03999999910593033
    group_023_1.inputs[4].default_value = 8479
    group_024_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_024_1.name = "Group.024"
    group_024_1.node_tree = random__normal_
    group_024_1.inputs[0].default_value = True
    group_024_1.inputs[1].default_value = 3.25
    group_024_1.inputs[2].default_value = 0.25
    group_024_1.inputs[4].default_value = 12594
    frame_006 = moonsurface.nodes.new("NodeFrame")
    frame_006.name = "Frame.006"
    group_026 = moonsurface.nodes.new("GeometryNodeGroup")
    group_026.name = "Group.026"
    group_026.node_tree = random__normal_
    group_026.inputs[0].default_value = True
    group_026.inputs[1].default_value = 0.5
    group_026.inputs[2].default_value = 0.20000000298023224
    group_026.inputs[4].default_value = 521
    set_position_005 = moonsurface.nodes.new("GeometryNodeSetPosition")
    set_position_005.name = "Set Position.005"
    set_position_005.inputs[1].hide = True
    set_position_005.inputs[2].hide = True
    set_position_005.inputs[1].default_value = True
    set_position_005.inputs[2].default_value = (0.0, 0.0, 0.0)
    math_002_2 = moonsurface.nodes.new("ShaderNodeMath")
    math_002_2.name = "Math.002"
    math_002_2.operation = 'ADD'
    math_002_2.use_clamp = False
    math_003_2 = moonsurface.nodes.new("ShaderNodeMath")
    math_003_2.name = "Math.003"
    math_003_2.operation = 'ADD'
    math_003_2.use_clamp = False
    combine_xyz_002 = moonsurface.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"
    combine_xyz_002.inputs[0].default_value = 0.0
    combine_xyz_002.inputs[1].default_value = 0.0
    vector = moonsurface.nodes.new("FunctionNodeInputVector")
    vector.name = "Vector"
    vector.vector = (0.0, 0.0, 5.0)
    transform_geometry_1 = moonsurface.nodes.new("GeometryNodeTransform")
    transform_geometry_1.name = "Transform Geometry"
    transform_geometry_1.mode = 'COMPONENTS'
    transform_geometry_1.inputs[2].hide = True
    transform_geometry_1.inputs[3].hide = True
    transform_geometry_1.inputs[4].hide = True
    transform_geometry_1.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_1.inputs[3].default_value = (1.0, 1.0, 1.0)
    float_curve_1 = moonsurface.nodes.new("ShaderNodeFloatCurve")
    float_curve_1.name = "Float Curve"
    float_curve_1.mapping.extend = 'EXTRAPOLATED'
    float_curve_1.mapping.tone = 'STANDARD'
    float_curve_1.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_1.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_1.mapping.clip_min_x = 0.0
    float_curve_1.mapping.clip_min_y = 0.0
    float_curve_1.mapping.clip_max_x = 1.0
    float_curve_1.mapping.clip_max_y = 1.0
    float_curve_1.mapping.use_clip = True
    float_curve_1_curve_0 = float_curve_1.mapping.curves[0]
    float_curve_1_curve_0_point_0 = float_curve_1_curve_0.points[0]
    float_curve_1_curve_0_point_0.location = (0.0, 1.0)
    float_curve_1_curve_0_point_0.handle_type = 'AUTO'
    float_curve_1_curve_0_point_1 = float_curve_1_curve_0.points[1]
    float_curve_1_curve_0_point_1.location = (0.02500000037252903, 0.9750000238418579)
    float_curve_1_curve_0_point_1.handle_type = 'AUTO'
    float_curve_1_curve_0_point_2 = float_curve_1_curve_0.points.new(0.5, 0.10000000149011612)
    float_curve_1_curve_0_point_2.handle_type = 'AUTO_CLAMPED'
    float_curve_1_curve_0_point_3 = float_curve_1_curve_0.points.new(1.0, 0.0)
    float_curve_1_curve_0_point_3.handle_type = 'AUTO'
    float_curve_1.mapping.update()
    float_curve_1.inputs[0].default_value = 1.0
    reroute_1 = moonsurface.nodes.new("NodeReroute")
    reroute_1.name = "Reroute"
    reroute_1.socket_idname = "NodeSocketVectorXYZ"
    frame_007 = moonsurface.nodes.new("NodeFrame")
    frame_007.name = "Frame.007"
    reroute_012_1 = moonsurface.nodes.new("NodeReroute")
    reroute_012_1.name = "Reroute.012"
    reroute_012_1.socket_idname = "NodeSocketInt"
    transform_geometry_002_1 = moonsurface.nodes.new("GeometryNodeTransform")
    transform_geometry_002_1.name = "Transform Geometry.002"
    transform_geometry_002_1.mode = 'COMPONENTS'
    transform_geometry_002_1.inputs[1].hide = True
    transform_geometry_002_1.inputs[2].hide = True
    transform_geometry_002_1.inputs[4].hide = True
    transform_geometry_002_1.inputs[1].default_value = (0.0, 0.0, 0.0)
    transform_geometry_002_1.inputs[2].default_value = (0.0, 0.0, 0.0)
    attribute_statistic_002 = moonsurface.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic_002.name = "Attribute Statistic.002"
    attribute_statistic_002.data_type = 'FLOAT_VECTOR'
    attribute_statistic_002.domain = 'POINT'
    attribute_statistic_002.inputs[1].hide = True
    attribute_statistic_002.outputs[0].hide = True
    attribute_statistic_002.outputs[1].hide = True
    attribute_statistic_002.outputs[2].hide = True
    attribute_statistic_002.outputs[3].hide = True
    attribute_statistic_002.outputs[4].hide = True
    attribute_statistic_002.outputs[6].hide = True
    attribute_statistic_002.outputs[7].hide = True
    attribute_statistic_002.inputs[1].default_value = True
    position_005 = moonsurface.nodes.new("GeometryNodeInputPosition")
    position_005.name = "Position.005"
    reroute_013_1 = moonsurface.nodes.new("NodeReroute")
    reroute_013_1.name = "Reroute.013"
    reroute_013_1.socket_idname = "NodeSocketGeometry"
    vector_math_030 = moonsurface.nodes.new("ShaderNodeVectorMath")
    vector_math_030.name = "Vector Math.030"
    vector_math_030.operation = 'DIVIDE'
    vector_math_030.inputs[0].default_value = (1.0, 1.0, 1.0)
    frame_008 = moonsurface.nodes.new("NodeFrame")
    frame_008.name = "Frame.008"
    separate_xyz_001_1 = moonsurface.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001_1.name = "Separate XYZ.001"
    separate_xyz_001_1.outputs[2].hide = True
    math_006_1 = moonsurface.nodes.new("ShaderNodeMath")
    math_006_1.name = "Math.006"
    math_006_1.operation = 'MULTIPLY'
    math_006_1.use_clamp = False
    math_009 = moonsurface.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.operation = 'MAXIMUM'
    math_009.use_clamp = False
    math_010_1 = moonsurface.nodes.new("ShaderNodeMath")
    math_010_1.name = "Math.010"
    math_010_1.operation = 'DIVIDE'
    math_010_1.use_clamp = False
    math_011 = moonsurface.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.operation = 'DIVIDE'
    math_011.use_clamp = False
    mix = moonsurface.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'MIX'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'FLOAT'
    mix.factor_mode = 'UNIFORM'
    mix.inputs[0].hide = True
    mix.inputs[1].hide = True
    mix.inputs[4].hide = True
    mix.inputs[5].hide = True
    mix.inputs[6].hide = True
    mix.inputs[7].hide = True
    mix.inputs[8].hide = True
    mix.inputs[9].hide = True
    mix.outputs[1].hide = True
    mix.outputs[2].hide = True
    mix.outputs[3].hide = True
    mix.inputs[0].default_value = 0.5
    math_007_1 = moonsurface.nodes.new("ShaderNodeMath")
    math_007_1.name = "Math.007"
    math_007_1.operation = 'MULTIPLY'
    math_007_1.use_clamp = False
    reroute_002_2 = moonsurface.nodes.new("NodeReroute")
    reroute_002_2.name = "Reroute.002"
    reroute_002_2.socket_idname = "NodeSocketInt"
    reroute_014 = moonsurface.nodes.new("NodeReroute")
    reroute_014.name = "Reroute.014"
    reroute_014.socket_idname = "NodeSocketInt"
    reroute_015_1 = moonsurface.nodes.new("NodeReroute")
    reroute_015_1.name = "Reroute.015"
    reroute_015_1.socket_idname = "NodeSocketFloat"
    group_002_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_002_1.name = "Group.002"
    group_002_1.node_tree = random__normal_
    group_002_1.inputs[0].default_value = True
    group_002_1.inputs[1].default_value = 1.0
    group_002_1.inputs[2].default_value = 0.20000000298023224
    group_002_1.inputs[4].default_value = 65241
    group_003_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_003_1.name = "Group.003"
    group_003_1.node_tree = random__normal_
    group_003_1.inputs[0].default_value = True
    group_003_1.inputs[1].default_value = 0.3333333432674408
    group_003_1.inputs[2].default_value = 0.0833333358168602
    group_003_1.inputs[4].default_value = 87654
    group_004_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_004_1.name = "Group.004"
    group_004_1.node_tree = random__normal_
    group_004_1.inputs[0].default_value = True
    group_004_1.inputs[1].default_value = 0.8999999761581421
    group_004_1.inputs[2].default_value = 0.20000000298023224
    group_004_1.inputs[4].default_value = 521
    group_005_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_005_1.name = "Group.005"
    group_005_1.node_tree = random__normal_
    group_005_1.inputs[0].default_value = True
    group_005_1.inputs[1].default_value = 0.75
    group_005_1.inputs[2].default_value = 0.25
    group_005_1.inputs[4].default_value = 215
    reroute_016 = moonsurface.nodes.new("NodeReroute")
    reroute_016.name = "Reroute.016"
    reroute_016.socket_idname = "NodeSocketInt"
    group_001_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_001_1.name = "Group.001"
    group_001_1.node_tree = lunarrock
    group_001_1.inputs[2].default_value = (1.0, 1.0, 1.0)
    group_001_1.inputs[3].default_value = (0.25, 0.25, 0.10000000149011612)
    group_001_1.inputs[4].default_value = True
    group_001_1.inputs[5].default_value = -0.25
    distribute_points_on_faces = moonsurface.nodes.new("GeometryNodeDistributePointsOnFaces")
    distribute_points_on_faces.name = "Distribute Points on Faces"
    distribute_points_on_faces.distribute_method = 'POISSON'
    distribute_points_on_faces.use_legacy_normal = False
    distribute_points_on_faces.inputs[1].default_value = True
    distribute_points_on_faces.inputs[3].default_value = 0.10000000149011612
    repeat_input = moonsurface.nodes.new("GeometryNodeRepeatInput")
    repeat_input.name = "Repeat Input"
    repeat_output = moonsurface.nodes.new("GeometryNodeRepeatOutput")
    repeat_output.name = "Repeat Output"
    repeat_output.active_index = 1
    repeat_output.inspection_index = 0
    repeat_output.repeat_items.clear()
    repeat_output.repeat_items.new('GEOMETRY', "Geometry")
    repeat_output.repeat_items.new('INT', "Point Index")
    math_004_2 = moonsurface.nodes.new("ShaderNodeMath")
    math_004_2.name = "Math.004"
    math_004_2.operation = 'ADD'
    math_004_2.use_clamp = False
    math_004_2.inputs[1].default_value = 1.0
    domain_size = moonsurface.nodes.new("GeometryNodeAttributeDomainSize")
    domain_size.name = "Domain Size"
    domain_size.component = 'POINTCLOUD'
    join_geometry_001 = moonsurface.nodes.new("GeometryNodeJoinGeometry")
    join_geometry_001.name = "Join Geometry.001"
    join_geometry = moonsurface.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    sample_index = moonsurface.nodes.new("GeometryNodeSampleIndex")
    sample_index.name = "Sample Index"
    sample_index.clamp = False
    sample_index.data_type = 'FLOAT_VECTOR'
    sample_index.domain = 'POINT'
    position_1 = moonsurface.nodes.new("GeometryNodeInputPosition")
    position_1.name = "Position"
    transform_geometry_003_1 = moonsurface.nodes.new("GeometryNodeTransform")
    transform_geometry_003_1.name = "Transform Geometry.003"
    transform_geometry_003_1.mode = 'COMPONENTS'
    transform_geometry_003_1.inputs[2].hide = True
    transform_geometry_003_1.inputs[4].hide = True
    transform_geometry_003_1.inputs[2].default_value = (0.0, 0.0, 0.0)
    transform_geometry_003_1.inputs[3].default_value = (1.0, 1.0, 1.0)
    group_006_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_006_1.name = "Group.006"
    group_006_1.node_tree = random__uniform_
    group_006_1.inputs[0].default_value = 0.0
    group_006_1.inputs[1].default_value = 100000.0
    group_006_1.inputs[3].default_value = 434
    float_to_integer_002 = moonsurface.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_002.name = "Float to Integer.002"
    float_to_integer_002.rounding_mode = 'ROUND'
    math_005_2 = moonsurface.nodes.new("ShaderNodeMath")
    math_005_2.name = "Math.005"
    math_005_2.operation = 'ADD'
    math_005_2.use_clamp = False
    reroute_018_1 = moonsurface.nodes.new("NodeReroute")
    reroute_018_1.name = "Reroute.018"
    reroute_018_1.socket_idname = "NodeSocketFloat"
    reroute_019_1 = moonsurface.nodes.new("NodeReroute")
    reroute_019_1.name = "Reroute.019"
    reroute_019_1.socket_idname = "NodeSocketFloat"
    group_007_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_007_1.name = "Group.007"
    group_007_1.node_tree = random__uniform_
    group_007_1.inputs[0].default_value = 0.0
    group_007_1.inputs[1].default_value = 1.0
    group_007_1.inputs[3].default_value = 76543
    float_curve_001 = moonsurface.nodes.new("ShaderNodeFloatCurve")
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
    float_curve_001_curve_0_point_0.location = (0.0, 0.01875000074505806)
    float_curve_001_curve_0_point_0.handle_type = 'AUTO_CLAMPED'
    float_curve_001_curve_0_point_1 = float_curve_001_curve_0.points[1]
    float_curve_001_curve_0_point_1.location = (0.3090907037258148, 0.03749999776482582)
    float_curve_001_curve_0_point_1.handle_type = 'AUTO'
    float_curve_001_curve_0_point_2 = float_curve_001_curve_0.points.new(0.6181817650794983, 0.04249997437000275)
    float_curve_001_curve_0_point_2.handle_type = 'AUTO_CLAMPED'
    float_curve_001_curve_0_point_3 = float_curve_001_curve_0.points.new(0.9681816101074219, 0.050000037997961044)
    float_curve_001_curve_0_point_3.handle_type = 'AUTO_CLAMPED'
    float_curve_001_curve_0_point_4 = float_curve_001_curve_0.points.new(0.9854545593261719, 0.21874994039535522)
    float_curve_001_curve_0_point_4.handle_type = 'AUTO_CLAMPED'
    float_curve_001_curve_0_point_5 = float_curve_001_curve_0.points.new(1.0, 1.0)
    float_curve_001_curve_0_point_5.handle_type = 'AUTO_CLAMPED'
    float_curve_001.mapping.update()
    float_curve_001.inputs[0].default_value = 1.0
    delete_geometry_1 = moonsurface.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_1.name = "Delete Geometry"
    delete_geometry_1.mute = True
    delete_geometry_1.domain = 'POINT'
    delete_geometry_1.mode = 'ALL'
    position_001_1 = moonsurface.nodes.new("GeometryNodeInputPosition")
    position_001_1.name = "Position.001"
    compare_001_1 = moonsurface.nodes.new("FunctionNodeCompare")
    compare_001_1.name = "Compare.001"
    compare_001_1.data_type = 'FLOAT'
    compare_001_1.mode = 'ELEMENT'
    compare_001_1.operation = 'GREATER_THAN'
    separate_xyz_002_1 = moonsurface.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002_1.name = "Separate XYZ.002"
    separate_xyz_002_1.outputs[2].hide = True
    compare_002 = moonsurface.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = 'FLOAT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'GREATER_THAN'
    math_008_1 = moonsurface.nodes.new("ShaderNodeMath")
    math_008_1.name = "Math.008"
    math_008_1.operation = 'ABSOLUTE'
    math_008_1.use_clamp = False
    math_012 = moonsurface.nodes.new("ShaderNodeMath")
    math_012.name = "Math.012"
    math_012.operation = 'ABSOLUTE'
    math_012.use_clamp = False
    boolean_math_1 = moonsurface.nodes.new("FunctionNodeBooleanMath")
    boolean_math_1.name = "Boolean Math"
    boolean_math_1.operation = 'OR'
    separate_xyz_003_1 = moonsurface.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_003_1.name = "Separate XYZ.003"
    separate_xyz_003_1.outputs[2].hide = True
    math_013 = moonsurface.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.operation = 'MULTIPLY'
    math_013.use_clamp = False
    math_013.inputs[1].default_value = 0.44999998807907104
    math_014 = moonsurface.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.operation = 'MULTIPLY'
    math_014.use_clamp = False
    math_014.inputs[1].default_value = 0.3499999940395355
    vector_math_1 = moonsurface.nodes.new("ShaderNodeVectorMath")
    vector_math_1.name = "Vector Math"
    vector_math_1.operation = 'ADD'
    frame_010 = moonsurface.nodes.new("NodeFrame")
    frame_010.name = "Frame.010"
    frame_011 = moonsurface.nodes.new("NodeFrame")
    frame_011.name = "Frame.011"
    frame_012 = moonsurface.nodes.new("NodeFrame")
    frame_012.name = "Frame.012"
    frame_013 = moonsurface.nodes.new("NodeFrame")
    frame_013.name = "Frame.013"
    frame_014 = moonsurface.nodes.new("NodeFrame")
    frame_014.name = "Frame.014"
    frame_015 = moonsurface.nodes.new("NodeFrame")
    frame_015.name = "Frame.015"
    math_016 = moonsurface.nodes.new("ShaderNodeMath")
    math_016.name = "Math.016"
    math_016.operation = 'MULTIPLY'
    math_016.use_clamp = False
    math_016.inputs[1].default_value = 1.7999999523162842
    position_006 = moonsurface.nodes.new("GeometryNodeInputPosition")
    position_006.name = "Position.006"
    math_017 = moonsurface.nodes.new("ShaderNodeMath")
    math_017.name = "Math.017"
    math_017.operation = 'MULTIPLY'
    math_017.use_clamp = False
    vector_math_001_1 = moonsurface.nodes.new("ShaderNodeVectorMath")
    vector_math_001_1.name = "Vector Math.001"
    vector_math_001_1.operation = 'DISTANCE'
    math_018 = moonsurface.nodes.new("ShaderNodeMath")
    math_018.name = "Math.018"
    math_018.operation = 'DIVIDE'
    math_018.use_clamp = False
    math_019 = moonsurface.nodes.new("ShaderNodeMath")
    math_019.name = "Math.019"
    math_019.operation = 'SUBTRACT'
    math_019.use_clamp = False
    math_019.inputs[0].default_value = 1.0
    set_position_1 = moonsurface.nodes.new("GeometryNodeSetPosition")
    set_position_1.name = "Set Position"
    set_position_1.inputs[3].hide = True
    set_position_1.inputs[3].default_value = (0.0, 0.0, 0.0)
    math_020 = moonsurface.nodes.new("ShaderNodeMath")
    math_020.name = "Math.020"
    math_020.operation = 'MULTIPLY'
    math_020.use_clamp = False
    math_021 = moonsurface.nodes.new("ShaderNodeMath")
    math_021.name = "Math.021"
    math_021.operation = 'MULTIPLY'
    math_021.use_clamp = False
    compare_003 = moonsurface.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.data_type = 'FLOAT'
    compare_003.mode = 'ELEMENT'
    compare_003.operation = 'LESS_THAN'
    compare_003.inputs[1].default_value = 1.0
    group_008_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_008_1.name = "Group.008"
    group_008_1.node_tree = crater_profile
    math_022 = moonsurface.nodes.new("ShaderNodeMath")
    math_022.name = "Math.022"
    math_022.operation = 'SUBTRACT'
    math_022.use_clamp = False
    group_009_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_009_1.name = "Group.009"
    group_009_1.node_tree = crater_profile
    group_009_1.inputs[0].default_value = 0.0
    distribute_points_on_faces_001 = moonsurface.nodes.new("GeometryNodeDistributePointsOnFaces")
    distribute_points_on_faces_001.name = "Distribute Points on Faces.001"
    distribute_points_on_faces_001.distribute_method = 'POISSON'
    distribute_points_on_faces_001.use_legacy_normal = True
    distribute_points_on_faces_001.inputs[1].default_value = True
    distribute_points_on_faces_001.inputs[3].default_value = 5.0
    random_value_1 = moonsurface.nodes.new("FunctionNodeRandomValue")
    random_value_1.name = "Random Value"
    random_value_1.data_type = 'FLOAT'
    random_value_1.inputs[2].default_value = 0.0
    random_value_1.inputs[3].default_value = 1.0
    random_value_1.inputs[7].default_value = 0
    sample_index_001 = moonsurface.nodes.new("GeometryNodeSampleIndex")
    sample_index_001.name = "Sample Index.001"
    sample_index_001.clamp = False
    sample_index_001.data_type = 'FLOAT_VECTOR'
    sample_index_001.domain = 'POINT'
    sample_nearest = moonsurface.nodes.new("GeometryNodeSampleNearest")
    sample_nearest.name = "Sample Nearest"
    sample_nearest.domain = 'POINT'
    sample_nearest.inputs[1].default_value = (0.0, 0.0, 0.0)
    sample_index_002 = moonsurface.nodes.new("GeometryNodeSampleIndex")
    sample_index_002.name = "Sample Index.002"
    sample_index_002.clamp = False
    sample_index_002.data_type = 'FLOAT'
    sample_index_002.domain = 'POINT'
    sample_nearest_001 = moonsurface.nodes.new("GeometryNodeSampleNearest")
    sample_nearest_001.name = "Sample Nearest.001"
    sample_nearest_001.domain = 'POINT'
    sample_nearest_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    mix_001 = moonsurface.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'MIX'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'VECTOR'
    mix_001.factor_mode = 'UNIFORM'
    mix_001.inputs[4].default_value = (0.0, 0.0, 1.0)
    combine_xyz_003 = moonsurface.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_003.name = "Combine XYZ.003"
    combine_xyz_003.inputs[2].hide = True
    combine_xyz_003.inputs[2].default_value = 0.0
    separate_xyz_004 = moonsurface.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_004.name = "Separate XYZ.004"
    separate_xyz_004.outputs[2].hide = True
    combine_xyz_004 = moonsurface.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_004.name = "Combine XYZ.004"
    combine_xyz_004.inputs[2].hide = True
    combine_xyz_004.inputs[2].default_value = 0.0
    separate_xyz_005 = moonsurface.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_005.name = "Separate XYZ.005"
    separate_xyz_005.outputs[2].hide = True
    math_023 = moonsurface.nodes.new("ShaderNodeMath")
    math_023.name = "Math.023"
    math_023.operation = 'ADD'
    math_023.use_clamp = False
    math_023.inputs[1].default_value = 1.0
    vector_math_003_1 = moonsurface.nodes.new("ShaderNodeVectorMath")
    vector_math_003_1.name = "Vector Math.003"
    vector_math_003_1.operation = 'MULTIPLY'
    sample_index_003 = moonsurface.nodes.new("GeometryNodeSampleIndex")
    sample_index_003.name = "Sample Index.003"
    sample_index_003.clamp = False
    sample_index_003.data_type = 'FLOAT_VECTOR'
    sample_index_003.domain = 'POINT'
    string = moonsurface.nodes.new("FunctionNodeInputString")
    string.name = "String"
    string.string = "crater_normal"
    reroute_017_1 = moonsurface.nodes.new("NodeReroute")
    reroute_017_1.name = "Reroute.017"
    reroute_017_1.socket_idname = "NodeSocketGeometry"
    reroute_020_1 = moonsurface.nodes.new("NodeReroute")
    reroute_020_1.name = "Reroute.020"
    reroute_020_1.socket_idname = "NodeSocketGeometry"
    reroute_021_1 = moonsurface.nodes.new("NodeReroute")
    reroute_021_1.name = "Reroute.021"
    reroute_021_1.socket_idname = "NodeSocketFloat"
    reroute_022_1 = moonsurface.nodes.new("NodeReroute")
    reroute_022_1.name = "Reroute.022"
    reroute_022_1.socket_idname = "NodeSocketVector"
    reroute_023 = moonsurface.nodes.new("NodeReroute")
    reroute_023.name = "Reroute.023"
    reroute_023.socket_idname = "NodeSocketFloat"
    store_named_attribute = moonsurface.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute.name = "Store Named Attribute"
    store_named_attribute.data_type = 'FLOAT_VECTOR'
    store_named_attribute.domain = 'POINT'
    store_named_attribute.inputs[1].default_value = True
    store_named_attribute_001 = moonsurface.nodes.new("GeometryNodeStoreNamedAttribute")
    store_named_attribute_001.name = "Store Named Attribute.001"
    store_named_attribute_001.data_type = 'FLOAT'
    store_named_attribute_001.domain = 'POINT'
    store_named_attribute_001.inputs[1].default_value = True
    named_attribute = moonsurface.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute.name = "Named Attribute"
    named_attribute.data_type = 'FLOAT'
    named_attribute_001 = moonsurface.nodes.new("GeometryNodeInputNamedAttribute")
    named_attribute_001.name = "Named Attribute.001"
    named_attribute_001.data_type = 'FLOAT_VECTOR'
    string_001 = moonsurface.nodes.new("FunctionNodeInputString")
    string_001.name = "String.001"
    string_001.string = "crater_radius"
    float_curve_002 = moonsurface.nodes.new("ShaderNodeFloatCurve")
    float_curve_002.name = "Float Curve.002"
    float_curve_002.mapping.extend = 'EXTRAPOLATED'
    float_curve_002.mapping.tone = 'STANDARD'
    float_curve_002.mapping.black_level = (0.0, 0.0, 0.0)
    float_curve_002.mapping.white_level = (1.0, 1.0, 1.0)
    float_curve_002.mapping.clip_min_x = 0.0
    float_curve_002.mapping.clip_min_y = 0.0
    float_curve_002.mapping.clip_max_x = 1.0
    float_curve_002.mapping.clip_max_y = 1.0
    float_curve_002.mapping.use_clip = True
    float_curve_002_curve_0 = float_curve_002.mapping.curves[0]
    float_curve_002_curve_0_point_0 = float_curve_002_curve_0.points[0]
    float_curve_002_curve_0_point_0.location = (0.0, 0.23125004768371582)
    float_curve_002_curve_0_point_0.handle_type = 'AUTO'
    float_curve_002_curve_0_point_1 = float_curve_002_curve_0.points[1]
    float_curve_002_curve_0_point_1.location = (0.5454543828964233, 0.42750006914138794)
    float_curve_002_curve_0_point_1.handle_type = 'AUTO'
    float_curve_002_curve_0_point_2 = float_curve_002_curve_0.points.new(1.0, 1.0)
    float_curve_002_curve_0_point_2.handle_type = 'AUTO'
    float_curve_002.mapping.update()
    float_curve_002.inputs[0].default_value = 1.0
    reroute_025 = moonsurface.nodes.new("NodeReroute")
    reroute_025.name = "Reroute.025"
    reroute_025.socket_idname = "NodeSocketFloat"
    reroute_026 = moonsurface.nodes.new("NodeReroute")
    reroute_026.name = "Reroute.026"
    reroute_026.socket_idname = "NodeSocketInt"
    position_007 = moonsurface.nodes.new("GeometryNodeInputPosition")
    position_007.name = "Position.007"
    vector_math_004_1 = moonsurface.nodes.new("ShaderNodeVectorMath")
    vector_math_004_1.name = "Vector Math.004"
    vector_math_004_1.operation = 'ADD'
    reroute_027 = moonsurface.nodes.new("NodeReroute")
    reroute_027.name = "Reroute.027"
    reroute_027.socket_idname = "NodeSocketFloat"
    math_024 = moonsurface.nodes.new("ShaderNodeMath")
    math_024.name = "Math.024"
    math_024.operation = 'MULTIPLY'
    math_024.use_clamp = False
    math_025 = moonsurface.nodes.new("ShaderNodeMath")
    math_025.name = "Math.025"
    math_025.operation = 'SUBTRACT'
    math_025.use_clamp = False
    math_025.inputs[0].default_value = 1.0
    frame_016 = moonsurface.nodes.new("NodeFrame")
    frame_016.name = "Frame.016"
    frame_017 = moonsurface.nodes.new("NodeFrame")
    frame_017.name = "Frame.017"
    reroute_028 = moonsurface.nodes.new("NodeReroute")
    reroute_028.name = "Reroute.028"
    reroute_028.socket_idname = "NodeSocketGeometry"
    reroute_031 = moonsurface.nodes.new("NodeReroute")
    reroute_031.name = "Reroute.031"
    reroute_031.socket_idname = "NodeSocketInt"
    reroute_033 = moonsurface.nodes.new("NodeReroute")
    reroute_033.name = "Reroute.033"
    reroute_033.socket_idname = "NodeSocketGeometry"
    reroute_032 = moonsurface.nodes.new("NodeReroute")
    reroute_032.name = "Reroute.032"
    reroute_032.socket_idname = "NodeSocketVectorXYZ"
    reroute_029 = moonsurface.nodes.new("NodeReroute")
    reroute_029.name = "Reroute.029"
    reroute_029.socket_idname = "NodeSocketInt"
    reroute_030 = moonsurface.nodes.new("NodeReroute")
    reroute_030.name = "Reroute.030"
    reroute_030.socket_idname = "NodeSocketInt"
    frame_009 = moonsurface.nodes.new("NodeFrame")
    frame_009.name = "Frame.009"
    frame_009.use_custom_color = True
    frame_009.color = (0.6079999804496765, 0.0, 0.014633849263191223)
    frame_018 = moonsurface.nodes.new("NodeFrame")
    frame_018.name = "Frame.018"
    frame_018.use_custom_color = True
    frame_018.color = (0.6079999804496765, 0.0, 0.043328672647476196)
    reroute_024 = moonsurface.nodes.new("NodeReroute")
    reroute_024.name = "Reroute.024"
    reroute_024.socket_idname = "NodeSocketFloat"
    frame_019 = moonsurface.nodes.new("NodeFrame")
    frame_019.name = "Frame.019"
    reroute_035 = moonsurface.nodes.new("NodeReroute")
    reroute_035.name = "Reroute.035"
    reroute_035.socket_idname = "NodeSocketFloat"
    boolean_math_001 = moonsurface.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.operation = 'OR'
    combine_xyz_005 = moonsurface.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_005.name = "Combine XYZ.005"
    combine_xyz_005.inputs[2].hide = True
    combine_xyz_005.inputs[2].default_value = 0.0
    vector_math_005 = moonsurface.nodes.new("ShaderNodeVectorMath")
    vector_math_005.name = "Vector Math.005"
    vector_math_005.operation = 'LENGTH'
    compare_004 = moonsurface.nodes.new("FunctionNodeCompare")
    compare_004.name = "Compare.004"
    compare_004.data_type = 'FLOAT'
    compare_004.mode = 'ELEMENT'
    compare_004.operation = 'LESS_THAN'
    reroute_034 = moonsurface.nodes.new("NodeReroute")
    reroute_034.name = "Reroute.034"
    reroute_034.socket_idname = "NodeSocketFloat"
    mix_002 = moonsurface.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = 'MIX'
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = 'FLOAT'
    mix_002.factor_mode = 'UNIFORM'
    mix_002.inputs[0].default_value = 0.5
    math_026 = moonsurface.nodes.new("ShaderNodeMath")
    math_026.name = "Math.026"
    math_026.operation = 'MULTIPLY'
    math_026.use_clamp = False
    group_010_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_010_1.name = "Group.010"
    group_010_1.node_tree = random__normal_
    group_010_1.inputs[0].default_value = True
    group_010_1.inputs[1].default_value = 0.05000000074505806
    group_010_1.inputs[2].default_value = 0.02500000037252903
    group_010_1.inputs[3].default_value = 0
    group_010_1.inputs[4].default_value = 87702
    math_027 = moonsurface.nodes.new("ShaderNodeMath")
    math_027.name = "Math.027"
    math_027.operation = 'MINIMUM'
    math_027.use_clamp = False
    frame_020 = moonsurface.nodes.new("NodeFrame")
    frame_020.name = "Frame.020"
    math_028 = moonsurface.nodes.new("ShaderNodeMath")
    math_028.name = "Math.028"
    math_028.operation = 'MULTIPLY'
    math_028.use_clamp = False
    math_028.inputs[1].default_value = 0.125
    group_011_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_011_1.name = "Group.011"
    group_011_1.node_tree = random__normal_
    group_011_1.inputs[0].default_value = True
    group_011_1.inputs[1].default_value = 0.75
    group_011_1.inputs[2].default_value = 0.125
    group_011_1.inputs[4].default_value = 6543
    reroute_036 = moonsurface.nodes.new("NodeReroute")
    reroute_036.name = "Reroute.036"
    reroute_036.socket_idname = "NodeSocketInt"
    math_029 = moonsurface.nodes.new("ShaderNodeMath")
    math_029.name = "Math.029"
    math_029.operation = 'MULTIPLY'
    math_029.use_clamp = False
    attribute_statistic_1 = moonsurface.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic_1.name = "Attribute Statistic"
    attribute_statistic_1.data_type = 'FLOAT_VECTOR'
    attribute_statistic_1.domain = 'POINT'
    attribute_statistic_1.inputs[1].hide = True
    attribute_statistic_1.outputs[0].hide = True
    attribute_statistic_1.outputs[1].hide = True
    attribute_statistic_1.outputs[2].hide = True
    attribute_statistic_1.outputs[3].hide = True
    attribute_statistic_1.outputs[4].hide = True
    attribute_statistic_1.outputs[6].hide = True
    attribute_statistic_1.outputs[7].hide = True
    attribute_statistic_1.inputs[1].default_value = True
    position_008 = moonsurface.nodes.new("GeometryNodeInputPosition")
    position_008.name = "Position.008"
    separate_xyz_006 = moonsurface.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_006.name = "Separate XYZ.006"
    separate_xyz_006.outputs[0].hide = True
    separate_xyz_006.outputs[1].hide = True
    combine_xyz_006 = moonsurface.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_006.name = "Combine XYZ.006"
    combine_xyz_006.inputs[0].hide = True
    combine_xyz_006.inputs[1].hide = True
    combine_xyz_006.inputs[0].default_value = 0.0
    combine_xyz_006.inputs[1].default_value = 0.0
    transform_geometry_004 = moonsurface.nodes.new("GeometryNodeTransform")
    transform_geometry_004.name = "Transform Geometry.004"
    transform_geometry_004.mode = 'COMPONENTS'
    transform_geometry_004.inputs[1].hide = True
    transform_geometry_004.inputs[2].hide = True
    transform_geometry_004.inputs[4].hide = True
    transform_geometry_004.inputs[1].default_value = (0.0, 0.0, 0.0)
    transform_geometry_004.inputs[2].default_value = (0.0, 0.0, 0.0)
    vector_math_006 = moonsurface.nodes.new("ShaderNodeVectorMath")
    vector_math_006.name = "Vector Math.006"
    vector_math_006.operation = 'SCALE'
    group_012_1 = moonsurface.nodes.new("GeometryNodeGroup")
    group_012_1.name = "Group.012"
    group_012_1.node_tree = random__uniform_
    group_012_1.inputs[0].default_value = 0.07500000298023224
    group_012_1.inputs[1].default_value = 0.25
    group_012_1.inputs[3].default_value = 214126
    math_015 = moonsurface.nodes.new("ShaderNodeMath")
    math_015.name = "Math.015"
    math_015.operation = 'DIVIDE'
    math_015.use_clamp = False
    reroute_040 = moonsurface.nodes.new("NodeReroute")
    reroute_040.name = "Reroute.040"
    reroute_040.socket_idname = "NodeSocketFloat"
    reroute_038 = moonsurface.nodes.new("NodeReroute")
    reroute_038.name = "Reroute.038"
    reroute_038.socket_idname = "NodeSocketFloat"
    math_030 = moonsurface.nodes.new("ShaderNodeMath")
    math_030.name = "Math.030"
    math_030.operation = 'POWER'
    math_030.use_clamp = False
    math_030.inputs[1].default_value = 0.5
    float_to_integer_001 = moonsurface.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_001.name = "Float to Integer.001"
    float_to_integer_001.rounding_mode = 'CEILING'
    mesh_boolean_1 = moonsurface.nodes.new("GeometryNodeMeshBoolean")
    mesh_boolean_1.name = "Mesh Boolean"
    mesh_boolean_1.operation = 'UNION'
    mesh_boolean_1.solver = 'EXACT'
    mesh_boolean_1.inputs[2].default_value = False
    mesh_boolean_1.inputs[3].default_value = False
    switch_2 = moonsurface.nodes.new("GeometryNodeSwitch")
    switch_2.name = "Switch"
    switch_2.input_type = 'GEOMETRY'
    reroute_037 = moonsurface.nodes.new("NodeReroute")
    reroute_037.name = "Reroute.037"
    reroute_037.socket_idname = "NodeSocketGeometry"
    reroute_039 = moonsurface.nodes.new("NodeReroute")
    reroute_039.name = "Reroute.039"
    reroute_039.socket_idname = "NodeSocketBool"
    reroute_041 = moonsurface.nodes.new("NodeReroute")
    reroute_041.name = "Reroute.041"
    reroute_041.socket_idname = "NodeSocketBool"
    value = moonsurface.nodes.new("ShaderNodeValue")
    value.name = "Value"
    value.outputs[0].default_value = 15.0
    reroute_042 = moonsurface.nodes.new("NodeReroute")
    reroute_042.name = "Reroute.042"
    reroute_042.socket_idname = "NodeSocketMaterial"
    reroute_043 = moonsurface.nodes.new("NodeReroute")
    reroute_043.name = "Reroute.043"
    reroute_043.socket_idname = "NodeSocketMaterial"
    viewer = moonsurface.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.data_type = 'FLOAT'
    viewer.domain = 'AUTO'
    viewer.inputs[1].default_value = 0.0
    math_031 = moonsurface.nodes.new("ShaderNodeMath")
    math_031.name = "Math.031"
    math_031.operation = 'ADD'
    math_031.use_clamp = False
    math_031.inputs[1].default_value = 1.0
    repeat_input.pair_with_output(repeat_output)
    repeat_input.inputs[2].default_value = 0
    grid.parent = frame_001_2
    vector_math_012.parent = frame_002_1
    raycast.parent = frame_002_1
    frame_002_1.parent = frame_017
    vector_math_017.parent = frame_2
    gradient_texture_001.parent = frame_2
    position_002_1.parent = frame_2
    vector_math_019.parent = frame_2
    set_position_001_1.parent = frame_2
    position_003.parent = frame_2
    combine_xyz_1.parent = frame_2
    math_3.parent = frame_2
    reroute_001_1.parent = frame_002_1
    vector_math_002_1.parent = frame_001_2
    vector_math_021.parent = frame_001_2
    separate_xyz_1.parent = frame_001_2
    vector_math_023.parent = frame_001_2
    frame_001_2.parent = frame_017
    reroute_003_2.parent = frame_2
    compare_1.parent = frame_2
    transform_geometry_001_1.parent = frame_003_2
    attribute_statistic_001.parent = frame_003_2
    position_004_1.parent = frame_003_2
    reroute_007.parent = frame_003_2
    vector_math_028.parent = frame_003_2
    frame_003_2.parent = frame_017
    noise_texture_009.parent = frame_004_1
    group_013_1.parent = frame_004_1
    reroute_009.parent = frame_004_1
    group_2.parent = frame_004_1
    group_014_1.parent = frame_004_1
    group_015.parent = frame_004_1
    group_016.parent = frame_004_1
    frame_004_1.parent = frame_007
    noise_texture_010.parent = frame_005_1
    group_017.parent = frame_005_1
    reroute_010_1.parent = frame_005_1
    group_018.parent = frame_005_1
    group_020.parent = frame_005_1
    group_021.parent = frame_005_1
    frame_005_1.parent = frame_007
    noise_texture_011_1.parent = frame_006
    group_019_1.parent = frame_006
    reroute_011.parent = frame_006
    group_022_1.parent = frame_006
    group_023_1.parent = frame_006
    group_024_1.parent = frame_006
    frame_006.parent = frame_007
    group_026.parent = frame_005_1
    set_position_005.parent = frame_007
    math_002_2.parent = frame_004_1
    math_003_2.parent = frame_005_1
    combine_xyz_002.parent = frame_007
    vector.parent = frame_002_1
    transform_geometry_1.parent = frame_002_1
    float_curve_1.parent = frame_2
    reroute_1.parent = frame_003_2
    frame_007.parent = frame_017
    reroute_012_1.parent = frame_007
    transform_geometry_002_1.parent = frame_008
    attribute_statistic_002.parent = frame_008
    position_005.parent = frame_008
    reroute_013_1.parent = frame_008
    vector_math_030.parent = frame_008
    frame_008.parent = frame_017
    separate_xyz_001_1.parent = frame_019
    math_006_1.parent = frame_019
    math_009.parent = frame_001_2
    math_010_1.parent = frame_001_2
    math_011.parent = frame_001_2
    mix.parent = frame_019
    math_007_1.parent = frame_014
    reroute_002_2.parent = frame_016
    reroute_015_1.parent = frame_006
    group_002_1.parent = frame_015
    group_003_1.parent = frame_019
    group_004_1.parent = frame_014
    group_005_1.parent = frame_014
    reroute_016.parent = frame_016
    group_001_1.parent = frame_011
    distribute_points_on_faces.parent = frame_010
    repeat_input.parent = frame_011
    repeat_output.parent = frame_011
    math_004_2.parent = frame_011
    domain_size.parent = frame_010
    join_geometry_001.parent = frame_011
    join_geometry.parent = frame_011
    sample_index.parent = frame_011
    position_1.parent = frame_011
    transform_geometry_003_1.parent = frame_011
    group_006_1.parent = frame_011
    float_to_integer_002.parent = frame_011
    math_005_2.parent = frame_011
    reroute_018_1.parent = frame_011
    reroute_019_1.parent = frame_011
    group_007_1.parent = frame_011
    float_curve_001.parent = frame_018
    delete_geometry_1.parent = frame_010
    position_001_1.parent = frame_010
    compare_001_1.parent = frame_010
    separate_xyz_002_1.parent = frame_010
    compare_002.parent = frame_010
    math_008_1.parent = frame_010
    math_012.parent = frame_010
    boolean_math_1.parent = frame_010
    separate_xyz_003_1.parent = frame_010
    math_013.parent = frame_010
    math_014.parent = frame_010
    vector_math_1.parent = frame_011
    frame_010.parent = frame_011
    frame_012.parent = frame_016
    frame_013.parent = frame_016
    frame_014.parent = frame_016
    frame_015.parent = frame_016
    math_016.parent = frame_015
    position_006.parent = frame_012
    math_017.parent = frame_012
    vector_math_001_1.parent = frame_012
    math_018.parent = frame_012
    math_019.parent = frame_012
    set_position_1.parent = frame_014
    math_020.parent = frame_014
    math_021.parent = frame_014
    compare_003.parent = frame_014
    group_008_1.parent = frame_013
    math_022.parent = frame_013
    group_009_1.parent = frame_013
    distribute_points_on_faces_001.parent = frame_015
    random_value_1.parent = frame_015
    sample_index_001.parent = frame_012
    sample_nearest.parent = frame_012
    sample_index_002.parent = frame_015
    sample_nearest_001.parent = frame_015
    mix_001.parent = frame_014
    combine_xyz_003.parent = frame_012
    separate_xyz_004.parent = frame_012
    combine_xyz_004.parent = frame_012
    separate_xyz_005.parent = frame_012
    math_023.parent = frame_015
    vector_math_003_1.parent = frame_014
    sample_index_003.parent = frame_015
    string.parent = frame_015
    reroute_017_1.parent = frame_012
    reroute_020_1.parent = frame_012
    reroute_021_1.parent = frame_016
    reroute_022_1.parent = frame_014
    reroute_023.parent = frame_016
    store_named_attribute.parent = frame_015
    store_named_attribute_001.parent = frame_015
    named_attribute.parent = frame_015
    named_attribute_001.parent = frame_015
    string_001.parent = frame_015
    float_curve_002.parent = frame_009
    reroute_025.parent = frame_013
    reroute_026.parent = frame_013
    position_007.parent = frame_014
    vector_math_004_1.parent = frame_014
    reroute_027.parent = frame_013
    math_024.parent = frame_014
    math_025.parent = frame_014
    reroute_028.parent = frame_016
    reroute_033.parent = frame_010
    reroute_032.parent = frame_010
    reroute_029.parent = frame_016
    reroute_030.parent = frame_016
    frame_009.parent = frame_015
    frame_018.parent = frame_011
    reroute_024.parent = frame_016
    frame_019.parent = frame_016
    reroute_035.parent = frame_014
    boolean_math_001.parent = frame_010
    combine_xyz_005.parent = frame_010
    vector_math_005.parent = frame_010
    compare_004.parent = frame_010
    mix_002.parent = frame_020
    math_026.parent = frame_020
    group_010_1.parent = frame_020
    math_027.parent = frame_020
    frame_020.parent = frame_010
    math_028.parent = frame_010
    group_011_1.parent = frame_010
    reroute_036.parent = frame_020
    math_029.parent = frame_011
    attribute_statistic_1.parent = frame_011
    position_008.parent = frame_011
    separate_xyz_006.parent = frame_011
    combine_xyz_006.parent = frame_011
    transform_geometry_004.parent = frame_011
    vector_math_006.parent = frame_011
    group_012_1.parent = frame_011
    math_015.parent = frame_011
    math_030.parent = frame_011
    float_to_integer_001.parent = frame_011
    mesh_boolean_1.parent = frame_011
    switch_2.parent = frame_011
    reroute_037.parent = frame_011
    value.parent = frame_020
    math_031.parent = frame_011
    moonsurface.links.new(set_material_1.outputs[0], group_output_4.inputs[0])
    moonsurface.links.new(set_shade_smooth_1.outputs[0], set_material_1.inputs[0])
    moonsurface.links.new(reroute_001_1.outputs[0], raycast.inputs[0])
    moonsurface.links.new(raycast.outputs[1], vector_math_012.inputs[0])
    moonsurface.links.new(vector_math_019.outputs[0], gradient_texture_001.inputs[0])
    moonsurface.links.new(position_002_1.outputs[0], vector_math_019.inputs[0])
    moonsurface.links.new(combine_xyz_1.outputs[0], vector_math_017.inputs[1])
    moonsurface.links.new(position_003.outputs[0], vector_math_017.inputs[0])
    moonsurface.links.new(float_curve_1.outputs[0], combine_xyz_1.inputs[2])
    moonsurface.links.new(group_input_4.outputs[1], vector_math_002_1.inputs[0])
    moonsurface.links.new(group_input_4.outputs[2], vector_math_002_1.inputs[1])
    moonsurface.links.new(vector_math_002_1.outputs[0], vector_math_021.inputs[0])
    moonsurface.links.new(separate_xyz_1.outputs[0], grid.inputs[2])
    moonsurface.links.new(separate_xyz_1.outputs[1], grid.inputs[3])
    moonsurface.links.new(vector_math_021.outputs[0], vector_math_023.inputs[0])
    moonsurface.links.new(vector_math_023.outputs[0], separate_xyz_1.inputs[0])
    moonsurface.links.new(reroute_003_2.outputs[0], math_3.inputs[0])
    moonsurface.links.new(reroute_006_1.outputs[0], reroute_003_2.inputs[0])
    moonsurface.links.new(reroute_003_2.outputs[0], compare_1.inputs[0])
    moonsurface.links.new(compare_1.outputs[0], set_position_001_1.inputs[1])
    moonsurface.links.new(integer_012.outputs[0], math_001_3.inputs[1])
    moonsurface.links.new(group_input_4.outputs[0], math_001_3.inputs[0])
    moonsurface.links.new(group_input_4.outputs[1], reroute_005_1.inputs[0])
    moonsurface.links.new(math_001_3.outputs[0], float_to_integer_1.inputs[0])
    moonsurface.links.new(position_004_1.outputs[0], attribute_statistic_001.inputs[2])
    moonsurface.links.new(reroute_007.outputs[0], attribute_statistic_001.inputs[0])
    moonsurface.links.new(vector_math_028.outputs[0], transform_geometry_001_1.inputs[3])
    moonsurface.links.new(attribute_statistic_001.outputs[5], vector_math_028.inputs[1])
    moonsurface.links.new(reroute_1.outputs[0], vector_math_028.inputs[0])
    moonsurface.links.new(reroute_005_1.outputs[0], reroute_008.inputs[0])
    moonsurface.links.new(reroute_034.outputs[0], reroute_006_1.inputs[0])
    moonsurface.links.new(group_input_4.outputs[3], reroute_004_1.inputs[0])
    moonsurface.links.new(group_013_1.outputs[0], noise_texture_009.inputs[1])
    moonsurface.links.new(reroute_012_1.outputs[0], reroute_009.inputs[0])
    moonsurface.links.new(reroute_009.outputs[0], group_013_1.inputs[2])
    moonsurface.links.new(reroute_009.outputs[0], group_2.inputs[3])
    moonsurface.links.new(group_2.outputs[0], noise_texture_009.inputs[2])
    moonsurface.links.new(reroute_009.outputs[0], group_014_1.inputs[3])
    moonsurface.links.new(group_014_1.outputs[0], noise_texture_009.inputs[3])
    moonsurface.links.new(reroute_009.outputs[0], group_015.inputs[3])
    moonsurface.links.new(group_015.outputs[0], noise_texture_009.inputs[4])
    moonsurface.links.new(reroute_009.outputs[0], group_016.inputs[3])
    moonsurface.links.new(group_016.outputs[0], noise_texture_009.inputs[5])
    moonsurface.links.new(group_017.outputs[0], noise_texture_010.inputs[1])
    moonsurface.links.new(reroute_010_1.outputs[0], group_017.inputs[2])
    moonsurface.links.new(reroute_010_1.outputs[0], group_018.inputs[3])
    moonsurface.links.new(group_018.outputs[0], noise_texture_010.inputs[2])
    moonsurface.links.new(reroute_010_1.outputs[0], group_020.inputs[3])
    moonsurface.links.new(group_020.outputs[0], noise_texture_010.inputs[4])
    moonsurface.links.new(reroute_010_1.outputs[0], group_021.inputs[3])
    moonsurface.links.new(group_021.outputs[0], noise_texture_010.inputs[5])
    moonsurface.links.new(reroute_012_1.outputs[0], reroute_010_1.inputs[0])
    moonsurface.links.new(group_019_1.outputs[0], noise_texture_011_1.inputs[1])
    moonsurface.links.new(reroute_011.outputs[0], group_019_1.inputs[2])
    moonsurface.links.new(reroute_011.outputs[0], group_022_1.inputs[3])
    moonsurface.links.new(group_022_1.outputs[0], noise_texture_011_1.inputs[2])
    moonsurface.links.new(reroute_011.outputs[0], group_023_1.inputs[3])
    moonsurface.links.new(group_023_1.outputs[0], noise_texture_011_1.inputs[4])
    moonsurface.links.new(reroute_011.outputs[0], group_024_1.inputs[3])
    moonsurface.links.new(group_024_1.outputs[0], noise_texture_011_1.inputs[5])
    moonsurface.links.new(reroute_012_1.outputs[0], reroute_011.inputs[0])
    moonsurface.links.new(reroute_010_1.outputs[0], group_026.inputs[3])
    moonsurface.links.new(group_026.outputs[0], noise_texture_010.inputs[6])
    moonsurface.links.new(grid.outputs[0], set_position_005.inputs[0])
    moonsurface.links.new(noise_texture_009.outputs[0], math_002_2.inputs[0])
    moonsurface.links.new(noise_texture_010.outputs[0], math_003_2.inputs[0])
    moonsurface.links.new(reroute_015_1.outputs[0], math_003_2.inputs[1])
    moonsurface.links.new(math_003_2.outputs[0], math_002_2.inputs[1])
    moonsurface.links.new(math_002_2.outputs[0], combine_xyz_002.inputs[2])
    moonsurface.links.new(combine_xyz_002.outputs[0], set_position_005.inputs[3])
    moonsurface.links.new(vector.outputs[0], raycast.inputs[2])
    moonsurface.links.new(reroute_007.outputs[0], transform_geometry_001_1.inputs[0])
    moonsurface.links.new(vector_math_012.outputs[0], transform_geometry_1.inputs[1])
    moonsurface.links.new(reroute_001_1.outputs[0], transform_geometry_1.inputs[0])
    moonsurface.links.new(vector_math_017.outputs[0], set_position_001_1.inputs[2])
    moonsurface.links.new(gradient_texture_001.outputs[1], float_curve_1.inputs[1])
    moonsurface.links.new(math_3.outputs[0], vector_math_019.inputs[1])
    moonsurface.links.new(reroute_008.outputs[0], reroute_1.inputs[0])
    moonsurface.links.new(float_to_integer_1.outputs[0], reroute_012_1.inputs[0])
    moonsurface.links.new(position_005.outputs[0], attribute_statistic_002.inputs[2])
    moonsurface.links.new(reroute_013_1.outputs[0], attribute_statistic_002.inputs[0])
    moonsurface.links.new(vector_math_030.outputs[0], transform_geometry_002_1.inputs[3])
    moonsurface.links.new(attribute_statistic_002.outputs[5], vector_math_030.inputs[1])
    moonsurface.links.new(reroute_013_1.outputs[0], transform_geometry_002_1.inputs[0])
    moonsurface.links.new(set_position_005.outputs[0], reroute_013_1.inputs[0])
    moonsurface.links.new(transform_geometry_002_1.outputs[0], reroute_001_1.inputs[0])
    moonsurface.links.new(transform_geometry_1.outputs[0], reroute_007.inputs[0])
    moonsurface.links.new(reroute_008.outputs[0], separate_xyz_001_1.inputs[0])
    moonsurface.links.new(separate_xyz_1.outputs[0], math_009.inputs[0])
    moonsurface.links.new(separate_xyz_1.outputs[1], math_009.inputs[1])
    moonsurface.links.new(separate_xyz_1.outputs[0], math_010_1.inputs[0])
    moonsurface.links.new(math_009.outputs[0], math_010_1.inputs[1])
    moonsurface.links.new(math_009.outputs[0], math_011.inputs[1])
    moonsurface.links.new(separate_xyz_1.outputs[1], math_011.inputs[0])
    moonsurface.links.new(math_010_1.outputs[0], grid.inputs[0])
    moonsurface.links.new(math_011.outputs[0], grid.inputs[1])
    moonsurface.links.new(separate_xyz_001_1.outputs[0], mix.inputs[2])
    moonsurface.links.new(separate_xyz_001_1.outputs[1], mix.inputs[3])
    moonsurface.links.new(mix.outputs[0], math_006_1.inputs[0])
    moonsurface.links.new(reroute_035.outputs[0], math_007_1.inputs[0])
    moonsurface.links.new(reroute_014.outputs[0], reroute_002_2.inputs[0])
    moonsurface.links.new(float_to_integer_1.outputs[0], reroute_014.inputs[0])
    moonsurface.links.new(noise_texture_011_1.outputs[0], reroute_015_1.inputs[0])
    moonsurface.links.new(reroute_002_2.outputs[0], group_002_1.inputs[3])
    moonsurface.links.new(reroute_002_2.outputs[0], group_003_1.inputs[3])
    moonsurface.links.new(group_003_1.outputs[0], math_006_1.inputs[1])
    moonsurface.links.new(reroute_002_2.outputs[0], group_004_1.inputs[3])
    moonsurface.links.new(group_004_1.outputs[0], math_007_1.inputs[1])
    moonsurface.links.new(reroute_002_2.outputs[0], group_005_1.inputs[3])
    moonsurface.links.new(set_position_001_1.outputs[0], set_shade_smooth_1.inputs[0])
    moonsurface.links.new(compare_001_1.outputs[0], boolean_math_1.inputs[0])
    moonsurface.links.new(compare_002.outputs[0], boolean_math_1.inputs[1])
    moonsurface.links.new(group_006_1.outputs[0], float_to_integer_002.inputs[0])
    moonsurface.links.new(math_013.outputs[0], compare_001_1.inputs[1])
    moonsurface.links.new(float_to_integer_002.outputs[0], math_005_2.inputs[1])
    moonsurface.links.new(repeat_output.outputs[0], join_geometry.inputs[0])
    moonsurface.links.new(separate_xyz_003_1.outputs[0], math_013.inputs[0])
    moonsurface.links.new(delete_geometry_1.outputs[0], sample_index.inputs[0])
    moonsurface.links.new(separate_xyz_003_1.outputs[1], math_014.inputs[0])
    moonsurface.links.new(math_004_2.outputs[0], reroute_018_1.inputs[0])
    moonsurface.links.new(math_014.outputs[0], compare_002.inputs[1])
    moonsurface.links.new(math_005_2.outputs[0], reroute_019_1.inputs[0])
    moonsurface.links.new(math_008_1.outputs[0], compare_002.inputs[0])
    moonsurface.links.new(math_004_2.outputs[0], math_005_2.inputs[0])
    moonsurface.links.new(repeat_input.outputs[2], math_004_2.inputs[0])
    moonsurface.links.new(reroute_019_1.outputs[0], group_007_1.inputs[2])
    moonsurface.links.new(reroute_019_1.outputs[0], group_001_1.inputs[0])
    moonsurface.links.new(delete_geometry_1.outputs[0], domain_size.inputs[0])
    moonsurface.links.new(group_007_1.outputs[0], float_curve_001.inputs[1])
    moonsurface.links.new(distribute_points_on_faces.outputs[0], delete_geometry_1.inputs[0])
    moonsurface.links.new(join_geometry_001.outputs[0], repeat_output.inputs[0])
    moonsurface.links.new(domain_size.outputs[0], repeat_input.inputs[0])
    moonsurface.links.new(position_001_1.outputs[0], separate_xyz_002_1.inputs[0])
    moonsurface.links.new(reroute_018_1.outputs[0], repeat_output.inputs[1])
    moonsurface.links.new(math_012.outputs[0], compare_001_1.inputs[0])
    moonsurface.links.new(reroute_018_1.outputs[0], sample_index.inputs[2])
    moonsurface.links.new(position_1.outputs[0], sample_index.inputs[1])
    moonsurface.links.new(separate_xyz_002_1.outputs[0], math_012.inputs[0])
    moonsurface.links.new(separate_xyz_002_1.outputs[1], math_008_1.inputs[0])
    moonsurface.links.new(repeat_input.outputs[1], join_geometry_001.inputs[0])
    moonsurface.links.new(reroute_036.outputs[0], distribute_points_on_faces.inputs[6])
    moonsurface.links.new(reroute_031.outputs[0], group_006_1.inputs[2])
    moonsurface.links.new(reroute_032.outputs[0], separate_xyz_003_1.inputs[0])
    moonsurface.links.new(switch_2.outputs[0], set_position_001_1.inputs[0])
    moonsurface.links.new(math_018.outputs[0], compare_003.inputs[0])
    moonsurface.links.new(math_018.outputs[0], math_019.inputs[1])
    moonsurface.links.new(math_019.outputs[0], group_008_1.inputs[0])
    moonsurface.links.new(position_006.outputs[0], sample_index_001.inputs[1])
    moonsurface.links.new(math_017.outputs[0], math_018.inputs[1])
    moonsurface.links.new(math_022.outputs[0], math_020.inputs[0])
    moonsurface.links.new(reroute_023.outputs[0], math_020.inputs[1])
    moonsurface.links.new(vector_math_001_1.outputs[1], math_018.inputs[0])
    moonsurface.links.new(reroute_021_1.outputs[0], math_017.inputs[0])
    moonsurface.links.new(math_020.outputs[0], math_021.inputs[0])
    moonsurface.links.new(math_016.outputs[0], distribute_points_on_faces_001.inputs[2])
    moonsurface.links.new(group_009_1.outputs[0], math_022.inputs[1])
    moonsurface.links.new(reroute_020_1.outputs[0], sample_index_001.inputs[0])
    moonsurface.links.new(reroute_017_1.outputs[0], sample_nearest.inputs[0])
    moonsurface.links.new(sample_nearest.outputs[0], sample_index_001.inputs[2])
    moonsurface.links.new(sample_nearest_001.outputs[0], sample_index_002.inputs[2])
    moonsurface.links.new(compare_003.outputs[0], set_position_1.inputs[1])
    moonsurface.links.new(group_008_1.outputs[0], math_022.inputs[0])
    moonsurface.links.new(separate_xyz_004.outputs[0], combine_xyz_003.inputs[0])
    moonsurface.links.new(separate_xyz_004.outputs[1], combine_xyz_003.inputs[1])
    moonsurface.links.new(combine_xyz_003.outputs[0], vector_math_001_1.inputs[0])
    moonsurface.links.new(separate_xyz_005.outputs[0], combine_xyz_004.inputs[0])
    moonsurface.links.new(separate_xyz_005.outputs[1], combine_xyz_004.inputs[1])
    moonsurface.links.new(sample_index_001.outputs[0], separate_xyz_005.inputs[0])
    moonsurface.links.new(combine_xyz_004.outputs[0], vector_math_001_1.inputs[1])
    moonsurface.links.new(position_006.outputs[0], separate_xyz_004.inputs[0])
    moonsurface.links.new(math_023.outputs[0], random_value_1.inputs[8])
    moonsurface.links.new(sample_nearest_001.outputs[0], sample_index_003.inputs[2])
    moonsurface.links.new(math_021.outputs[0], vector_math_003_1.inputs[0])
    moonsurface.links.new(mix_001.outputs[1], vector_math_003_1.inputs[1])
    moonsurface.links.new(reroute_017_1.outputs[0], reroute_020_1.inputs[0])
    moonsurface.links.new(sample_index_002.outputs[0], reroute_021_1.inputs[0])
    moonsurface.links.new(sample_index_003.outputs[0], reroute_022_1.inputs[0])
    moonsurface.links.new(reroute_021_1.outputs[0], reroute_023.inputs[0])
    moonsurface.links.new(distribute_points_on_faces_001.outputs[0], reroute_017_1.inputs[0])
    moonsurface.links.new(distribute_points_on_faces_001.outputs[0], sample_nearest_001.inputs[0])
    moonsurface.links.new(store_named_attribute_001.outputs[0], sample_index_002.inputs[0])
    moonsurface.links.new(store_named_attribute.outputs[0], sample_index_003.inputs[0])
    moonsurface.links.new(distribute_points_on_faces_001.outputs[0], store_named_attribute_001.inputs[0])
    moonsurface.links.new(distribute_points_on_faces_001.outputs[0], store_named_attribute.inputs[0])
    moonsurface.links.new(string_001.outputs[0], store_named_attribute_001.inputs[2])
    moonsurface.links.new(string_001.outputs[0], named_attribute.inputs[0])
    moonsurface.links.new(named_attribute.outputs[0], sample_index_002.inputs[1])
    moonsurface.links.new(string.outputs[0], store_named_attribute.inputs[2])
    moonsurface.links.new(string.outputs[0], named_attribute_001.inputs[0])
    moonsurface.links.new(named_attribute_001.outputs[0], sample_index_003.inputs[1])
    moonsurface.links.new(distribute_points_on_faces_001.outputs[1], store_named_attribute.inputs[3])
    moonsurface.links.new(random_value_1.outputs[1], float_curve_002.inputs[1])
    moonsurface.links.new(float_curve_002.outputs[0], store_named_attribute_001.inputs[3])
    moonsurface.links.new(reroute_025.outputs[0], group_008_1.inputs[1])
    moonsurface.links.new(reroute_025.outputs[0], group_009_1.inputs[1])
    moonsurface.links.new(reroute_021_1.outputs[0], reroute_025.inputs[0])
    moonsurface.links.new(reroute_022_1.outputs[0], mix_001.inputs[5])
    moonsurface.links.new(reroute_026.outputs[0], group_009_1.inputs[3])
    moonsurface.links.new(reroute_026.outputs[0], group_008_1.inputs[3])
    moonsurface.links.new(position_007.outputs[0], vector_math_004_1.inputs[0])
    moonsurface.links.new(vector_math_003_1.outputs[0], vector_math_004_1.inputs[1])
    moonsurface.links.new(vector_math_004_1.outputs[0], set_position_1.inputs[2])
    moonsurface.links.new(reroute_027.outputs[0], group_008_1.inputs[2])
    moonsurface.links.new(reroute_027.outputs[0], group_009_1.inputs[2])
    moonsurface.links.new(math_024.outputs[0], mix_001.inputs[0])
    moonsurface.links.new(math_025.outputs[0], math_024.inputs[1])
    moonsurface.links.new(reroute_023.outputs[0], math_025.inputs[1])
    moonsurface.links.new(math_006_1.outputs[0], math_016.inputs[0])
    moonsurface.links.new(math_007_1.outputs[0], math_021.inputs[1])
    moonsurface.links.new(reroute_028.outputs[0], distribute_points_on_faces_001.inputs[0])
    moonsurface.links.new(reroute_024.outputs[0], math_017.inputs[1])
    moonsurface.links.new(reroute_028.outputs[0], set_position_1.inputs[0])
    moonsurface.links.new(reroute_024.outputs[0], reroute_027.inputs[0])
    moonsurface.links.new(group_005_1.outputs[0], math_024.inputs[0])
    moonsurface.links.new(reroute_033.outputs[0], distribute_points_on_faces.inputs[0])
    moonsurface.links.new(transform_geometry_001_1.outputs[0], reroute_028.inputs[0])
    moonsurface.links.new(reroute_030.outputs[0], reroute_016.inputs[0])
    moonsurface.links.new(reroute_016.outputs[0], reroute_031.inputs[0])
    moonsurface.links.new(set_position_1.outputs[0], reroute_033.inputs[0])
    moonsurface.links.new(reroute_008.outputs[0], reroute_032.inputs[0])
    moonsurface.links.new(group_002_1.outputs[0], distribute_points_on_faces_001.inputs[5])
    moonsurface.links.new(reroute_002_2.outputs[0], reroute_029.inputs[0])
    moonsurface.links.new(reroute_029.outputs[0], distribute_points_on_faces_001.inputs[6])
    moonsurface.links.new(reroute_029.outputs[0], math_023.inputs[0])
    moonsurface.links.new(reroute_030.outputs[0], reroute_026.inputs[0])
    moonsurface.links.new(reroute_029.outputs[0], reroute_030.inputs[0])
    moonsurface.links.new(math_006_1.outputs[0], reroute_024.inputs[0])
    moonsurface.links.new(reroute_024.outputs[0], reroute_035.inputs[0])
    moonsurface.links.new(separate_xyz_002_1.outputs[0], combine_xyz_005.inputs[0])
    moonsurface.links.new(separate_xyz_002_1.outputs[1], combine_xyz_005.inputs[1])
    moonsurface.links.new(combine_xyz_005.outputs[0], vector_math_005.inputs[0])
    moonsurface.links.new(vector_math_005.outputs[1], compare_004.inputs[0])
    moonsurface.links.new(compare_004.outputs[0], boolean_math_001.inputs[0])
    moonsurface.links.new(boolean_math_1.outputs[0], boolean_math_001.inputs[1])
    moonsurface.links.new(boolean_math_001.outputs[0], delete_geometry_1.inputs[1])
    moonsurface.links.new(reroute_004_1.outputs[0], reroute_034.inputs[0])
    moonsurface.links.new(reroute_034.outputs[0], compare_004.inputs[1])
    moonsurface.links.new(separate_xyz_003_1.outputs[0], mix_002.inputs[2])
    moonsurface.links.new(separate_xyz_003_1.outputs[1], mix_002.inputs[3])
    moonsurface.links.new(group_010_1.outputs[0], math_026.inputs[1])
    moonsurface.links.new(mix_002.outputs[0], math_026.inputs[0])
    moonsurface.links.new(math_026.outputs[0], math_027.inputs[0])
    moonsurface.links.new(math_027.outputs[0], math_028.inputs[0])
    moonsurface.links.new(math_028.outputs[0], distribute_points_on_faces.inputs[2])
    moonsurface.links.new(group_011_1.outputs[0], distribute_points_on_faces.inputs[5])
    moonsurface.links.new(reroute_031.outputs[0], reroute_036.inputs[0])
    moonsurface.links.new(reroute_036.outputs[0], group_011_1.inputs[3])
    moonsurface.links.new(float_curve_001.outputs[0], math_029.inputs[0])
    moonsurface.links.new(math_027.outputs[0], math_029.inputs[1])
    moonsurface.links.new(position_008.outputs[0], attribute_statistic_1.inputs[2])
    moonsurface.links.new(attribute_statistic_1.outputs[5], separate_xyz_006.inputs[0])
    moonsurface.links.new(separate_xyz_006.outputs[2], combine_xyz_006.inputs[2])
    moonsurface.links.new(vector_math_1.outputs[0], transform_geometry_003_1.inputs[1])
    moonsurface.links.new(sample_index.outputs[0], vector_math_1.inputs[0])
    moonsurface.links.new(math_029.outputs[0], transform_geometry_004.inputs[3])
    moonsurface.links.new(transform_geometry_004.outputs[0], transform_geometry_003_1.inputs[0])
    moonsurface.links.new(group_001_1.outputs[0], transform_geometry_004.inputs[0])
    moonsurface.links.new(transform_geometry_004.outputs[0], attribute_statistic_1.inputs[0])
    moonsurface.links.new(vector_math_006.outputs[0], vector_math_1.inputs[1])
    moonsurface.links.new(combine_xyz_006.outputs[0], vector_math_006.inputs[0])
    moonsurface.links.new(reroute_019_1.outputs[0], group_012_1.inputs[2])
    moonsurface.links.new(group_012_1.outputs[0], vector_math_006.inputs[3])
    moonsurface.links.new(group_input_4.outputs[2], reroute_040.inputs[0])
    moonsurface.links.new(reroute_038.outputs[0], math_015.inputs[1])
    moonsurface.links.new(reroute_040.outputs[0], reroute_038.inputs[0])
    moonsurface.links.new(math_029.outputs[0], math_015.inputs[0])
    moonsurface.links.new(math_015.outputs[0], math_030.inputs[0])
    moonsurface.links.new(math_031.outputs[0], float_to_integer_001.inputs[0])
    moonsurface.links.new(float_to_integer_001.outputs[0], group_001_1.inputs[1])
    moonsurface.links.new(join_geometry.outputs[0], switch_2.inputs[1])
    moonsurface.links.new(reroute_033.outputs[0], reroute_037.inputs[0])
    moonsurface.links.new(repeat_output.outputs[0], mesh_boolean_1.inputs[1])
    moonsurface.links.new(mesh_boolean_1.outputs[0], switch_2.inputs[2])
    moonsurface.links.new(reroute_041.outputs[0], switch_2.inputs[0])
    moonsurface.links.new(group_input_4.outputs[4], reroute_039.inputs[0])
    moonsurface.links.new(reroute_039.outputs[0], reroute_041.inputs[0])
    moonsurface.links.new(value.outputs[0], math_027.inputs[1])
    moonsurface.links.new(reroute_042.outputs[0], set_material_1.inputs[2])
    moonsurface.links.new(reroute_043.outputs[0], reroute_042.inputs[0])
    moonsurface.links.new(group_input_4.outputs[5], reroute_043.inputs[0])
    moonsurface.links.new(join_geometry.outputs[0], viewer.inputs[0])
    moonsurface.links.new(math_030.outputs[0], math_031.inputs[0])
    moonsurface.links.new(transform_geometry_003_1.outputs[0], join_geometry_001.inputs[0])
    moonsurface.links.new(reroute_037.outputs[0], join_geometry.inputs[0])
    moonsurface.links.new(reroute_037.outputs[0], mesh_boolean_1.inputs[1])
    return moonsurface

moonsurface = moonsurface_node_group()


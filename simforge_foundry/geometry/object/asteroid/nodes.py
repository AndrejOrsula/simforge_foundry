import bpy

def random__normal__node_group():
    random__normal_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Random (Normal)")
    random__normal_.color_tag = 'NONE'
    random__normal_.default_group_node_width = 140
    value_socket = random__normal_.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket.default_value = 0.0
    value_socket.min_value = -3.4028234663852886e+38
    value_socket.max_value = 3.4028234663852886e+38
    value_socket.subtype = 'NONE'
    value_socket.attribute_domain = 'POINT'
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
    seed_socket = random__normal_.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket.default_value = 0
    seed_socket.min_value = 0
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.hide_value = True
    offset_socket = random__normal_.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
    offset_socket.default_value = 0
    offset_socket.min_value = 0
    offset_socket.max_value = 2147483647
    offset_socket.subtype = 'NONE'
    offset_socket.attribute_domain = 'POINT'
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
    group_output = random__normal_.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    group_input = random__normal_.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    switch = random__normal_.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'FLOAT'
    math_006 = random__normal_.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'MAXIMUM'
    math_006.use_clamp = False
    math_006.inputs[1].default_value = 0.0
    frame.width, frame.height = 150.0, 100.0
    frame_003.width, frame_003.height = 150.0, 100.0
    frame_001.width, frame_001.height = 150.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    random_value_001.width, random_value_001.height = 140.0, 100.0
    math_010.width, math_010.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    random_value_002.width, random_value_002.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    random__normal_.links.new(random_value_002.outputs[1], math.inputs[0])
    random__normal_.links.new(math.outputs[0], math_001.inputs[0])
    random__normal_.links.new(random_value_001.outputs[1], math_002.inputs[0])
    random__normal_.links.new(math_002.outputs[0], math_004.inputs[0])
    random__normal_.links.new(math_003.outputs[0], math_005.inputs[0])
    random__normal_.links.new(group_input.outputs[3], random_value_002.inputs[8])
    random__normal_.links.new(group_input.outputs[3], math_010.inputs[0])
    random__normal_.links.new(math_010.outputs[0], random_value_001.inputs[8])
    random__normal_.links.new(group_input.outputs[2], math_008.inputs[0])
    random__normal_.links.new(group_input.outputs[1], math_007.inputs[0])
    random__normal_.links.new(math_008.outputs[0], math_007.inputs[1])
    random__normal_.links.new(math_005.outputs[0], math_008.inputs[1])
    random__normal_.links.new(math_004.outputs[0], math_005.inputs[1])
    random__normal_.links.new(math_001.outputs[0], math_003.inputs[0])
    random__normal_.links.new(group_input.outputs[4], random_value_001.inputs[7])
    random__normal_.links.new(group_input.outputs[4], random_value_002.inputs[7])
    random__normal_.links.new(group_input.outputs[0], switch.inputs[0])
    random__normal_.links.new(math_007.outputs[0], math_006.inputs[0])
    random__normal_.links.new(switch.outputs[0], group_output.inputs[0])
    random__normal_.links.new(math_007.outputs[0], switch.inputs[1])
    random__normal_.links.new(math_006.outputs[0], switch.inputs[2])
    return random__normal_

random__normal_ = random__normal__node_group()

def random__uniform__node_group():
    random__uniform_ = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Random (Uniform)")
    random__uniform_.color_tag = 'NONE'
    random__uniform_.default_group_node_width = 140
    value_socket_1 = random__uniform_.interface.new_socket(name = "Value", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    value_socket_1.default_value = 0.0
    value_socket_1.min_value = -3.4028234663852886e+38
    value_socket_1.max_value = 3.4028234663852886e+38
    value_socket_1.subtype = 'NONE'
    value_socket_1.attribute_domain = 'POINT'
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
    seed_socket_1 = random__uniform_.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket_1.default_value = 0
    seed_socket_1.min_value = -2147483648
    seed_socket_1.max_value = 2147483647
    seed_socket_1.subtype = 'NONE'
    seed_socket_1.attribute_domain = 'POINT'
    seed_socket_1.hide_value = True
    offset_socket_1 = random__uniform_.interface.new_socket(name = "Offset", in_out='INPUT', socket_type = 'NodeSocketInt')
    offset_socket_1.default_value = 0
    offset_socket_1.min_value = 0
    offset_socket_1.max_value = 2147483647
    offset_socket_1.subtype = 'NONE'
    offset_socket_1.attribute_domain = 'POINT'
    group_output_1 = random__uniform_.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True
    group_input_1 = random__uniform_.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"
    random_value_011 = random__uniform_.nodes.new("FunctionNodeRandomValue")
    random_value_011.name = "Random Value.011"
    random_value_011.data_type = 'FLOAT'
    group_output_1.width, group_output_1.height = 140.0, 100.0
    group_input_1.width, group_input_1.height = 140.0, 100.0
    random_value_011.width, random_value_011.height = 140.0, 100.0
    random__uniform_.links.new(random_value_011.outputs[1], group_output_1.inputs[0])
    random__uniform_.links.new(group_input_1.outputs[0], random_value_011.inputs[2])
    random__uniform_.links.new(group_input_1.outputs[1], random_value_011.inputs[3])
    random__uniform_.links.new(group_input_1.outputs[3], random_value_011.inputs[7])
    random__uniform_.links.new(group_input_1.outputs[2], random_value_011.inputs[8])
    return random__uniform_

random__uniform_ = random__uniform__node_group()

def asteroid_node_group():
    asteroid = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Asteroid")
    asteroid.color_tag = 'GEOMETRY'
    asteroid.default_group_node_width = 140
    asteroid.is_modifier = True
    geometry_socket = asteroid.interface.new_socket(name = "geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    seed_socket_2 = asteroid.interface.new_socket(name = "seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket_2.default_value = 0
    seed_socket_2.min_value = 0
    seed_socket_2.max_value = 2147483647
    seed_socket_2.subtype = 'NONE'
    seed_socket_2.attribute_domain = 'POINT'
    seed_socket_2.force_non_field = True
    detail_socket = asteroid.interface.new_socket(name = "detail", in_out='INPUT', socket_type = 'NodeSocketInt')
    detail_socket.default_value = 4
    detail_socket.min_value = 0
    detail_socket.max_value = 10
    detail_socket.subtype = 'NONE'
    detail_socket.attribute_domain = 'POINT'
    detail_socket.force_non_field = True
    scale_socket = asteroid.interface.new_socket(name = "scale", in_out='INPUT', socket_type = 'NodeSocketVector')
    scale_socket.default_value = (1.0, 1.0, 1.0)
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'XYZ'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.force_non_field = True
    scale_std_socket = asteroid.interface.new_socket(name = "scale_std", in_out='INPUT', socket_type = 'NodeSocketVector')
    scale_std_socket.default_value = (0.0, 0.0, 0.0)
    scale_std_socket.min_value = 0.0
    scale_std_socket.max_value = 3.4028234663852886e+38
    scale_std_socket.subtype = 'XYZ'
    scale_std_socket.attribute_domain = 'POINT'
    scale_std_socket.force_non_field = True
    mat_socket = asteroid.interface.new_socket(name = "mat", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    mat_socket.attribute_domain = 'POINT'
    group_input_2 = asteroid.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"
    group_output_2 = asteroid.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True
    set_material = asteroid.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.inputs[1].default_value = True
    cube = asteroid.nodes.new("GeometryNodeMeshCube")
    cube.name = "Cube"
    cube.inputs[1].default_value = 2
    cube.inputs[2].default_value = 2
    cube.inputs[3].default_value = 2
    subdivision_surface = asteroid.nodes.new("GeometryNodeSubdivisionSurface")
    subdivision_surface.name = "Subdivision Surface"
    subdivision_surface.boundary_smooth = 'ALL'
    subdivision_surface.uv_smooth = 'PRESERVE_BOUNDARIES'
    set_position = asteroid.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    set_position.inputs[1].hide = True
    set_position.inputs[3].hide = True
    set_position.inputs[1].default_value = True
    set_position.inputs[3].default_value = (0.0, 0.0, 0.0)
    voronoi_texture = asteroid.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = 'EUCLIDEAN'
    voronoi_texture.feature = 'SMOOTH_F1'
    voronoi_texture.normalize = False
    voronoi_texture.voronoi_dimensions = '4D'
    voronoi_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    voronoi_texture.inputs[6].default_value = 0.0
    voronoi_texture.inputs[8].default_value = 1.0
    vector_math = asteroid.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'MULTIPLY'
    position = asteroid.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    map_range = asteroid.nodes.new("ShaderNodeMapRange")
    map_range.name = "Map Range"
    map_range.clamp = False
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    map_range.inputs[1].default_value = 0.0
    map_range.inputs[2].default_value = 1.0
    map_range.inputs[3].default_value = 0.6666666269302368
    map_range.inputs[4].default_value = 1.0
    set_position_001 = asteroid.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.inputs[1].hide = True
    set_position_001.inputs[3].hide = True
    set_position_001.inputs[1].default_value = True
    set_position_001.inputs[3].default_value = (0.0, 0.0, 0.0)
    vector_math_001 = asteroid.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'MULTIPLY'
    position_001 = asteroid.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    noise_texture = asteroid.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '4D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    noise_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    noise_texture.inputs[3].default_value = 15.0
    set_shade_smooth = asteroid.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    set_shade_smooth.inputs[1].default_value = True
    set_shade_smooth.inputs[2].default_value = True
    frame_1 = asteroid.nodes.new("NodeFrame")
    frame_1.name = "Frame"
    frame_001_1 = asteroid.nodes.new("NodeFrame")
    frame_001_1.name = "Frame.001"
    frame_001_1.hide = True
    frame_002 = asteroid.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    reroute_001 = asteroid.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketFloat"
    transform_geometry = asteroid.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = 'COMPONENTS'
    transform_geometry.inputs[2].hide = True
    transform_geometry.inputs[4].hide = True
    transform_geometry.inputs[2].default_value = (0.0, 0.0, 0.0)
    reroute_002 = asteroid.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.socket_idname = "NodeSocketInt"
    attribute_statistic = asteroid.nodes.new("GeometryNodeAttributeStatistic")
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
    position_002 = asteroid.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"
    reroute_003 = asteroid.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.socket_idname = "NodeSocketGeometry"
    vector_math_002 = asteroid.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'DIVIDE'
    vector_math_002.inputs[0].default_value = (1.0, 1.0, 1.0)
    vector_math_003 = asteroid.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.operation = 'ADD'
    vector_math_004 = asteroid.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.operation = 'SCALE'
    vector_math_004.inputs[3].default_value = -0.5
    group = asteroid.nodes.new("GeometryNodeGroup")
    group.name = "Group"
    group.node_tree = random__normal_
    group.inputs[0].default_value = True
    group.inputs[1].default_value = 0.5
    group.inputs[2].default_value = 0.3333333432674408
    group.inputs[4].default_value = 11783
    group_001 = asteroid.nodes.new("GeometryNodeGroup")
    group_001.name = "Group.001"
    group_001.node_tree = random__uniform_
    group_001.inputs[0].default_value = -100000000.0
    group_001.inputs[1].default_value = 1000000000.0
    group_001.inputs[3].default_value = 10346
    group_002 = asteroid.nodes.new("GeometryNodeGroup")
    group_002.name = "Group.002"
    group_002.node_tree = random__normal_
    group_002.inputs[0].default_value = True
    group_002.inputs[1].default_value = 0.0
    group_002.inputs[2].default_value = 0.5
    group_002.inputs[4].default_value = 8000
    group_004 = asteroid.nodes.new("GeometryNodeGroup")
    group_004.name = "Group.004"
    group_004.node_tree = random__normal_
    group_004.inputs[0].default_value = True
    group_004.inputs[1].default_value = 3.0
    group_004.inputs[2].default_value = 0.5
    group_004.inputs[4].default_value = 1034
    float_curve = asteroid.nodes.new("ShaderNodeFloatCurve")
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
    float_curve_curve_0_point_1.location = (0.42878779768943787, 0.19999995827674866)
    float_curve_curve_0_point_1.handle_type = 'AUTO_CLAMPED'
    float_curve_curve_0_point_2 = float_curve_curve_0.points.new(0.6500000953674316, 0.8874998092651367)
    float_curve_curve_0_point_2.handle_type = 'AUTO'
    float_curve_curve_0_point_3 = float_curve_curve_0.points.new(1.0, 1.0)
    float_curve_curve_0_point_3.handle_type = 'AUTO'
    float_curve.mapping.update()
    float_curve.inputs[0].default_value = 1.0
    group_005 = asteroid.nodes.new("GeometryNodeGroup")
    group_005.name = "Group.005"
    group_005.node_tree = random__normal_
    group_005.inputs[0].default_value = True
    group_005.inputs[1].default_value = 0.25
    group_005.inputs[2].default_value = 0.10000000149011612
    group_005.inputs[4].default_value = 3258
    reroute_005 = asteroid.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.socket_idname = "NodeSocketFloat"
    group_003 = asteroid.nodes.new("GeometryNodeGroup")
    group_003.name = "Group.003"
    group_003.node_tree = random__normal_
    group_003.inputs[0].default_value = True
    group_003.inputs[1].default_value = 0.0
    group_003.inputs[2].default_value = 0.05000000074505806
    group_003.inputs[4].default_value = 21973
    group_006 = asteroid.nodes.new("GeometryNodeGroup")
    group_006.name = "Group.006"
    group_006.node_tree = random__normal_
    group_006.inputs[0].default_value = True
    group_006.inputs[1].default_value = 0.0
    group_006.inputs[2].default_value = 0.10000000149011612
    group_006.inputs[4].default_value = 14855
    reroute_006 = asteroid.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.socket_idname = "NodeSocketFloat"
    reroute = asteroid.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketVectorXYZ"
    group_007 = asteroid.nodes.new("GeometryNodeGroup")
    group_007.name = "Group.007"
    group_007.node_tree = random__uniform_
    group_007.inputs[0].default_value = -100000000.0
    group_007.inputs[1].default_value = 1000000000.0
    group_007.inputs[3].default_value = 10781
    group_008 = asteroid.nodes.new("GeometryNodeGroup")
    group_008.name = "Group.008"
    group_008.node_tree = random__normal_
    group_008.inputs[0].default_value = True
    group_008.inputs[1].default_value = 0.07500000298023224
    group_008.inputs[2].default_value = 0.02500000037252903
    group_008.inputs[4].default_value = 3267
    group_010 = asteroid.nodes.new("GeometryNodeGroup")
    group_010.name = "Group.010"
    group_010.node_tree = random__normal_
    group_010.inputs[0].default_value = True
    group_010.inputs[1].default_value = 0.5600000023841858
    group_010.inputs[2].default_value = 0.019999999552965164
    group_010.inputs[4].default_value = 5038
    group_011 = asteroid.nodes.new("GeometryNodeGroup")
    group_011.name = "Group.011"
    group_011.node_tree = random__normal_
    group_011.inputs[0].default_value = True
    group_011.inputs[1].default_value = 2.4000000953674316
    group_011.inputs[2].default_value = 0.20000000298023224
    group_011.inputs[4].default_value = 3147
    group_012 = asteroid.nodes.new("GeometryNodeGroup")
    group_012.name = "Group.012"
    group_012.node_tree = random__normal_
    group_012.inputs[0].default_value = True
    group_012.inputs[1].default_value = 0.05000000074505806
    group_012.inputs[2].default_value = 0.009999999776482582
    group_012.inputs[4].default_value = 3622
    frame_003_1 = asteroid.nodes.new("NodeFrame")
    frame_003_1.name = "Frame.003"
    transform_geometry_001 = asteroid.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    transform_geometry_001.inputs[1].hide = True
    transform_geometry_001.inputs[3].hide = True
    transform_geometry_001.inputs[4].hide = True
    transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    transform_geometry_001.inputs[3].default_value = (1.0, 1.0, 1.0)
    random_value = asteroid.nodes.new("FunctionNodeRandomValue")
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
    integer = asteroid.nodes.new("FunctionNodeInputInt")
    integer.name = "Integer"
    integer.integer = 424242
    transform_geometry_003 = asteroid.nodes.new("GeometryNodeTransform")
    transform_geometry_003.name = "Transform Geometry.003"
    transform_geometry_003.mode = 'COMPONENTS'
    transform_geometry_003.inputs[1].hide = True
    transform_geometry_003.inputs[2].hide = True
    transform_geometry_003.inputs[4].hide = True
    transform_geometry_003.inputs[1].default_value = (0.0, 0.0, 0.0)
    transform_geometry_003.inputs[2].default_value = (0.0, 0.0, 0.0)
    combine_xyz_001 = asteroid.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"
    group_009 = asteroid.nodes.new("GeometryNodeGroup")
    group_009.name = "Group.009"
    group_009.node_tree = random__normal_
    group_009.inputs[0].default_value = True
    group_009.inputs[4].default_value = 31680
    group_013 = asteroid.nodes.new("GeometryNodeGroup")
    group_013.name = "Group.013"
    group_013.node_tree = random__normal_
    group_013.inputs[0].default_value = True
    group_013.inputs[4].default_value = 32260
    group_014 = asteroid.nodes.new("GeometryNodeGroup")
    group_014.name = "Group.014"
    group_014.node_tree = random__normal_
    group_014.inputs[0].default_value = True
    group_014.inputs[4].default_value = 40590
    reroute_015 = asteroid.nodes.new("NodeReroute")
    reroute_015.name = "Reroute.015"
    reroute_015.socket_idname = "NodeSocketFloat"
    separate_xyz = asteroid.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz_003 = asteroid.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_003.name = "Separate XYZ.003"
    reroute_017 = asteroid.nodes.new("NodeReroute")
    reroute_017.name = "Reroute.017"
    reroute_017.socket_idname = "NodeSocketVectorXYZ"
    reroute_018 = asteroid.nodes.new("NodeReroute")
    reroute_018.name = "Reroute.018"
    reroute_018.socket_idname = "NodeSocketVectorXYZ"
    reroute_019 = asteroid.nodes.new("NodeReroute")
    reroute_019.name = "Reroute.019"
    reroute_019.socket_idname = "NodeSocketVectorXYZ"
    reroute_020 = asteroid.nodes.new("NodeReroute")
    reroute_020.name = "Reroute.020"
    reroute_020.socket_idname = "NodeSocketFloat"
    frame_005 = asteroid.nodes.new("NodeFrame")
    frame_005.name = "Frame.005"
    math_001_1 = asteroid.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = 'ADD'
    math_001_1.use_clamp = False
    integer_001 = asteroid.nodes.new("FunctionNodeInputInt")
    integer_001.name = "Integer.001"
    integer_001.integer = 0
    group_015 = asteroid.nodes.new("GeometryNodeGroup")
    group_015.name = "Group.015"
    group_015.node_tree = random__normal_
    group_015.inputs[0].default_value = True
    group_015.inputs[1].default_value = 1.0
    group_015.inputs[2].default_value = 0.20000000298023224
    group_015.inputs[4].default_value = 25714
    group_016 = asteroid.nodes.new("GeometryNodeGroup")
    group_016.name = "Group.016"
    group_016.node_tree = random__normal_
    group_016.inputs[0].default_value = True
    group_016.inputs[1].default_value = 1.0
    group_016.inputs[2].default_value = 0.20000000298023224
    group_016.inputs[4].default_value = 16351
    group_017 = asteroid.nodes.new("GeometryNodeGroup")
    group_017.name = "Group.017"
    group_017.node_tree = random__normal_
    group_017.inputs[0].default_value = True
    group_017.inputs[1].default_value = 1.0
    group_017.inputs[2].default_value = 0.20000000298023224
    group_017.inputs[4].default_value = 28906
    combine_xyz = asteroid.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    set_position_002 = asteroid.nodes.new("GeometryNodeSetPosition")
    set_position_002.name = "Set Position.002"
    set_position_002.inputs[1].hide = True
    set_position_002.inputs[3].hide = True
    set_position_002.inputs[1].default_value = True
    set_position_002.inputs[3].default_value = (0.0, 0.0, 0.0)
    voronoi_texture_001 = asteroid.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture_001.name = "Voronoi Texture.001"
    voronoi_texture_001.distance = 'EUCLIDEAN'
    voronoi_texture_001.feature = 'SMOOTH_F1'
    voronoi_texture_001.normalize = True
    voronoi_texture_001.voronoi_dimensions = '4D'
    voronoi_texture_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    voronoi_texture_001.inputs[3].default_value = 0.0
    voronoi_texture_001.inputs[4].default_value = 0.5
    voronoi_texture_001.inputs[5].default_value = 2.0
    voronoi_texture_001.inputs[6].default_value = 1.0
    voronoi_texture_001.inputs[8].default_value = 1.0
    vector_math_005 = asteroid.nodes.new("ShaderNodeVectorMath")
    vector_math_005.name = "Vector Math.005"
    vector_math_005.operation = 'MULTIPLY'
    position_003 = asteroid.nodes.new("GeometryNodeInputPosition")
    position_003.name = "Position.003"
    map_range_001 = asteroid.nodes.new("ShaderNodeMapRange")
    map_range_001.name = "Map Range.001"
    map_range_001.clamp = False
    map_range_001.data_type = 'FLOAT'
    map_range_001.interpolation_type = 'LINEAR'
    map_range_001.inputs[1].default_value = 0.0
    map_range_001.inputs[2].default_value = 1.0
    map_range_001.inputs[3].default_value = 0.550000011920929
    map_range_001.inputs[4].default_value = 1.0
    frame_004 = asteroid.nodes.new("NodeFrame")
    frame_004.name = "Frame.004"
    group_018 = asteroid.nodes.new("GeometryNodeGroup")
    group_018.name = "Group.018"
    group_018.node_tree = random__normal_
    group_018.inputs[0].default_value = True
    group_018.inputs[1].default_value = 3.0
    group_018.inputs[2].default_value = 0.5
    group_018.inputs[4].default_value = 9809
    group_019 = asteroid.nodes.new("GeometryNodeGroup")
    group_019.name = "Group.019"
    group_019.node_tree = random__uniform_
    group_019.inputs[0].default_value = -100000000.0
    group_019.inputs[1].default_value = 1000000000.0
    group_019.inputs[3].default_value = 14168
    float_curve_001 = asteroid.nodes.new("ShaderNodeFloatCurve")
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
    float_curve_001_curve_0_point_0.handle_type = 'AUTO'
    float_curve_001_curve_0_point_1 = float_curve_001_curve_0.points[1]
    float_curve_001_curve_0_point_1.location = (0.5, 1.0)
    float_curve_001_curve_0_point_1.handle_type = 'AUTO'
    float_curve_001_curve_0_point_2 = float_curve_001_curve_0.points.new(1.0, 0.0)
    float_curve_001_curve_0_point_2.handle_type = 'AUTO'
    float_curve_001.mapping.update()
    float_curve_001.inputs[0].default_value = 1.0
    reroute_007 = asteroid.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.socket_idname = "NodeSocketFloat"
    reroute_004 = asteroid.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.socket_idname = "NodeSocketMaterial"
    reroute_008 = asteroid.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.socket_idname = "NodeSocketMaterial"
    group_input_2.width, group_input_2.height = 140.0, 100.0
    group_output_2.width, group_output_2.height = 140.0, 100.0
    set_material.width, set_material.height = 140.0, 100.0
    cube.width, cube.height = 140.0, 100.0
    subdivision_surface.width, subdivision_surface.height = 150.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    voronoi_texture.width, voronoi_texture.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    position.width, position.height = 140.0, 100.0
    map_range.width, map_range.height = 140.0, 100.0
    set_position_001.width, set_position_001.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    position_001.width, position_001.height = 140.0, 100.0
    noise_texture.width, noise_texture.height = 140.0, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    frame_1.width, frame_1.height = 150.0, 100.0
    frame_001_1.width, frame_001_1.height = 150.0, 100.0
    frame_002.width, frame_002.height = 150.0, 100.0
    reroute_001.width, reroute_001.height = 16.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    reroute_002.width, reroute_002.height = 16.0, 100.0
    attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
    position_002.width, position_002.height = 140.0, 100.0
    reroute_003.width, reroute_003.height = 16.0, 100.0
    vector_math_002.width, vector_math_002.height = 140.0, 100.0
    vector_math_003.width, vector_math_003.height = 140.0, 100.0
    vector_math_004.width, vector_math_004.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0
    group_001.width, group_001.height = 140.0, 100.0
    group_002.width, group_002.height = 140.0, 100.0
    group_004.width, group_004.height = 140.0, 100.0
    float_curve.width, float_curve.height = 240.0, 100.0
    group_005.width, group_005.height = 140.0, 100.0
    reroute_005.width, reroute_005.height = 16.0, 100.0
    group_003.width, group_003.height = 140.0, 100.0
    group_006.width, group_006.height = 140.0, 100.0
    reroute_006.width, reroute_006.height = 16.0, 100.0
    reroute.width, reroute.height = 16.0, 100.0
    group_007.width, group_007.height = 140.0, 100.0
    group_008.width, group_008.height = 140.0, 100.0
    group_010.width, group_010.height = 140.0, 100.0
    group_011.width, group_011.height = 140.0, 100.0
    group_012.width, group_012.height = 140.0, 100.0
    frame_003_1.width, frame_003_1.height = 150.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    random_value.width, random_value.height = 140.0, 100.0
    integer.width, integer.height = 140.0, 100.0
    transform_geometry_003.width, transform_geometry_003.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    group_009.width, group_009.height = 140.0, 100.0
    group_013.width, group_013.height = 140.0, 100.0
    group_014.width, group_014.height = 140.0, 100.0
    reroute_015.width, reroute_015.height = 16.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    separate_xyz_003.width, separate_xyz_003.height = 140.0, 100.0
    reroute_017.width, reroute_017.height = 16.0, 100.0
    reroute_018.width, reroute_018.height = 16.0, 100.0
    reroute_019.width, reroute_019.height = 16.0, 100.0
    reroute_020.width, reroute_020.height = 16.0, 100.0
    frame_005.width, frame_005.height = 150.0, 100.0
    math_001_1.width, math_001_1.height = 140.0, 100.0
    integer_001.width, integer_001.height = 140.0, 100.0
    group_015.width, group_015.height = 140.0, 100.0
    group_016.width, group_016.height = 140.0, 100.0
    group_017.width, group_017.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    set_position_002.width, set_position_002.height = 140.0, 100.0
    voronoi_texture_001.width, voronoi_texture_001.height = 140.0, 100.0
    vector_math_005.width, vector_math_005.height = 140.0, 100.0
    position_003.width, position_003.height = 140.0, 100.0
    map_range_001.width, map_range_001.height = 140.0, 100.0
    frame_004.width, frame_004.height = 150.0, 100.0
    group_018.width, group_018.height = 140.0, 100.0
    group_019.width, group_019.height = 140.0, 100.0
    float_curve_001.width, float_curve_001.height = 240.0, 100.0
    reroute_007.width, reroute_007.height = 16.0, 100.0
    reroute_004.width, reroute_004.height = 16.0, 100.0
    reroute_008.width, reroute_008.height = 16.0, 100.0
    asteroid.links.new(set_material.outputs[0], group_output_2.inputs[0])
    asteroid.links.new(set_shade_smooth.outputs[0], set_material.inputs[0])
    asteroid.links.new(reroute_002.outputs[0], subdivision_surface.inputs[1])
    asteroid.links.new(position.outputs[0], vector_math.inputs[0])
    asteroid.links.new(map_range.outputs[0], vector_math.inputs[1])
    asteroid.links.new(vector_math.outputs[0], set_position.inputs[2])
    asteroid.links.new(position_001.outputs[0], vector_math_001.inputs[0])
    asteroid.links.new(noise_texture.outputs[0], vector_math_001.inputs[1])
    asteroid.links.new(reroute_003.outputs[0], transform_geometry.inputs[0])
    asteroid.links.new(math_001_1.outputs[0], reroute_001.inputs[0])
    asteroid.links.new(position_002.outputs[0], attribute_statistic.inputs[2])
    asteroid.links.new(set_position_001.outputs[0], reroute_003.inputs[0])
    asteroid.links.new(reroute_003.outputs[0], attribute_statistic.inputs[0])
    asteroid.links.new(vector_math_002.outputs[0], transform_geometry.inputs[3])
    asteroid.links.new(attribute_statistic.outputs[5], vector_math_002.inputs[1])
    asteroid.links.new(vector_math_004.outputs[0], transform_geometry.inputs[1])
    asteroid.links.new(vector_math_003.outputs[0], vector_math_004.inputs[0])
    asteroid.links.new(attribute_statistic.outputs[3], vector_math_003.inputs[0])
    asteroid.links.new(attribute_statistic.outputs[4], vector_math_003.inputs[1])
    asteroid.links.new(group_001.outputs[0], voronoi_texture.inputs[1])
    asteroid.links.new(reroute_005.outputs[0], group_001.inputs[2])
    asteroid.links.new(group.outputs[0], voronoi_texture.inputs[2])
    asteroid.links.new(group_002.outputs[0], voronoi_texture.inputs[3])
    asteroid.links.new(group_004.outputs[0], voronoi_texture.inputs[5])
    asteroid.links.new(reroute_005.outputs[0], group.inputs[3])
    asteroid.links.new(reroute_005.outputs[0], group_002.inputs[3])
    asteroid.links.new(reroute_005.outputs[0], group_004.inputs[3])
    asteroid.links.new(subdivision_surface.outputs[0], set_position.inputs[0])
    asteroid.links.new(float_curve.outputs[0], map_range.inputs[0])
    asteroid.links.new(voronoi_texture.outputs[0], float_curve.inputs[1])
    asteroid.links.new(reroute_005.outputs[0], group_005.inputs[3])
    asteroid.links.new(group_005.outputs[0], voronoi_texture.inputs[4])
    asteroid.links.new(math_001_1.outputs[0], reroute_005.inputs[0])
    asteroid.links.new(reroute_006.outputs[0], group_003.inputs[3])
    asteroid.links.new(reroute_006.outputs[0], group_006.inputs[3])
    asteroid.links.new(math_001_1.outputs[0], reroute_006.inputs[0])
    asteroid.links.new(group_input_2.outputs[2], reroute.inputs[0])
    asteroid.links.new(group_input_2.outputs[1], reroute_002.inputs[0])
    asteroid.links.new(vector_math_001.outputs[0], set_position_001.inputs[2])
    asteroid.links.new(reroute_001.outputs[0], group_007.inputs[2])
    asteroid.links.new(group_007.outputs[0], noise_texture.inputs[1])
    asteroid.links.new(reroute_001.outputs[0], group_008.inputs[3])
    asteroid.links.new(reroute_001.outputs[0], group_010.inputs[3])
    asteroid.links.new(reroute_001.outputs[0], group_011.inputs[3])
    asteroid.links.new(reroute_001.outputs[0], group_012.inputs[3])
    asteroid.links.new(group_012.outputs[0], noise_texture.inputs[8])
    asteroid.links.new(group_010.outputs[0], noise_texture.inputs[4])
    asteroid.links.new(group_011.outputs[0], noise_texture.inputs[5])
    asteroid.links.new(group_008.outputs[0], noise_texture.inputs[2])
    asteroid.links.new(integer.outputs[0], random_value.inputs[7])
    asteroid.links.new(random_value.outputs[0], transform_geometry_001.inputs[2])
    asteroid.links.new(transform_geometry_001.outputs[0], subdivision_surface.inputs[0])
    asteroid.links.new(cube.outputs[0], transform_geometry_001.inputs[0])
    asteroid.links.new(math_001_1.outputs[0], random_value.inputs[8])
    asteroid.links.new(transform_geometry_003.outputs[0], set_shade_smooth.inputs[0])
    asteroid.links.new(transform_geometry.outputs[0], transform_geometry_003.inputs[0])
    asteroid.links.new(group_009.outputs[0], combine_xyz_001.inputs[0])
    asteroid.links.new(group_013.outputs[0], combine_xyz_001.inputs[1])
    asteroid.links.new(group_014.outputs[0], combine_xyz_001.inputs[2])
    asteroid.links.new(combine_xyz_001.outputs[0], transform_geometry_003.inputs[3])
    asteroid.links.new(math_001_1.outputs[0], reroute_015.inputs[0])
    asteroid.links.new(reroute_020.outputs[0], group_013.inputs[3])
    asteroid.links.new(reroute_020.outputs[0], group_009.inputs[3])
    asteroid.links.new(reroute_020.outputs[0], group_014.inputs[3])
    asteroid.links.new(reroute_019.outputs[0], separate_xyz_003.inputs[0])
    asteroid.links.new(separate_xyz_003.outputs[0], group_009.inputs[2])
    asteroid.links.new(separate_xyz_003.outputs[1], group_013.inputs[2])
    asteroid.links.new(separate_xyz_003.outputs[2], group_014.inputs[2])
    asteroid.links.new(separate_xyz.outputs[0], group_009.inputs[1])
    asteroid.links.new(separate_xyz.outputs[1], group_013.inputs[1])
    asteroid.links.new(separate_xyz.outputs[2], group_014.inputs[1])
    asteroid.links.new(reroute_018.outputs[0], separate_xyz.inputs[0])
    asteroid.links.new(group_input_2.outputs[3], reroute_017.inputs[0])
    asteroid.links.new(reroute.outputs[0], reroute_018.inputs[0])
    asteroid.links.new(reroute_017.outputs[0], reroute_019.inputs[0])
    asteroid.links.new(reroute_015.outputs[0], reroute_020.inputs[0])
    asteroid.links.new(group_input_2.outputs[0], math_001_1.inputs[0])
    asteroid.links.new(integer_001.outputs[0], math_001_1.inputs[1])
    asteroid.links.new(group_006.outputs[0], subdivision_surface.inputs[2])
    asteroid.links.new(group_003.outputs[0], subdivision_surface.inputs[3])
    asteroid.links.new(combine_xyz.outputs[0], cube.inputs[0])
    asteroid.links.new(group_017.outputs[0], combine_xyz.inputs[2])
    asteroid.links.new(group_016.outputs[0], combine_xyz.inputs[1])
    asteroid.links.new(group_015.outputs[0], combine_xyz.inputs[0])
    asteroid.links.new(math_001_1.outputs[0], group_017.inputs[3])
    asteroid.links.new(math_001_1.outputs[0], group_016.inputs[3])
    asteroid.links.new(math_001_1.outputs[0], group_015.inputs[3])
    asteroid.links.new(position_003.outputs[0], vector_math_005.inputs[0])
    asteroid.links.new(map_range_001.outputs[0], vector_math_005.inputs[1])
    asteroid.links.new(group_019.outputs[0], voronoi_texture_001.inputs[1])
    asteroid.links.new(reroute_007.outputs[0], group_019.inputs[2])
    asteroid.links.new(group_018.outputs[0], voronoi_texture_001.inputs[2])
    asteroid.links.new(reroute_007.outputs[0], group_018.inputs[3])
    asteroid.links.new(float_curve_001.outputs[0], map_range_001.inputs[0])
    asteroid.links.new(voronoi_texture_001.outputs[0], float_curve_001.inputs[1])
    asteroid.links.new(set_position.outputs[0], set_position_002.inputs[0])
    asteroid.links.new(set_position_002.outputs[0], set_position_001.inputs[0])
    asteroid.links.new(math_001_1.outputs[0], reroute_007.inputs[0])
    asteroid.links.new(vector_math_005.outputs[0], set_position_002.inputs[2])
    asteroid.links.new(reroute_004.outputs[0], set_material.inputs[2])
    asteroid.links.new(reroute_008.outputs[0], reroute_004.inputs[0])
    asteroid.links.new(group_input_2.outputs[4], reroute_008.inputs[0])
    return asteroid

asteroid = asteroid_node_group()


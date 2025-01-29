import bpy

def peg_node_group():
    peg = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Peg")
    peg.color_tag = 'NONE'
    peg.default_group_node_width = 140
    peg.is_modifier = True
    geometry_socket = peg.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
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
    frame = peg.nodes.new("NodeFrame")
    frame.name = "Frame"
    frame_001 = peg.nodes.new("NodeFrame")
    frame_001.name = "Frame.001"
    frame_002 = peg.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    frame_003 = peg.nodes.new("NodeFrame")
    frame_003.name = "Frame.003"
    frame_004 = peg.nodes.new("NodeFrame")
    frame_004.name = "Frame.004"
    frame_005 = peg.nodes.new("NodeFrame")
    frame_005.name = "Frame.005"
    frame_006 = peg.nodes.new("NodeFrame")
    frame_006.name = "Frame.006"
    switch = peg.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'INT'
    group_input = peg.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_input.outputs[1].hide = True
    group_input.outputs[2].hide = True
    group_input.outputs[3].hide = True
    group_input.outputs[4].hide = True
    group_input.outputs[5].hide = True
    group_input.outputs[6].hide = True
    group_input.outputs[7].hide = True
    group_input.outputs[8].hide = True
    group_input.outputs[9].hide = True
    group_input.outputs[10].hide = True
    group_input.outputs[11].hide = True
    group_input.outputs[12].hide = True
    group_input.outputs[13].hide = True
    group_input.outputs[14].hide = True
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
    reroute = peg.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketBool"
    math = peg.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'MULTIPLY'
    math.use_clamp = False
    math.inputs[0].hide = True
    math.inputs[2].hide = True
    math.inputs[0].default_value = -0.5
    combine_xyz = peg.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    combine_xyz.inputs[0].hide = True
    combine_xyz.inputs[1].hide = True
    combine_xyz.inputs[0].default_value = 0.0
    combine_xyz.inputs[1].default_value = 0.0
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
    group_output = peg.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    group_output.inputs[1].hide = True
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
    math_001 = peg.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'SUBTRACT'
    math_001.use_clamp = False
    math_001.inputs[0].default_value = 1.0
    math_002 = peg.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'MULTIPLY'
    math_002.use_clamp = False
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
    reroute_001 = peg.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketFloat"
    reroute_002 = peg.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.socket_idname = "NodeSocketInt"
    reroute_003 = peg.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.socket_idname = "NodeSocketInt"
    reroute_004 = peg.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.socket_idname = "NodeSocketFloat"
    reroute_005 = peg.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.socket_idname = "NodeSocketFloat"
    reroute_006 = peg.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.socket_idname = "NodeSocketFloat"
    math_003 = peg.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'DIVIDE'
    math_003.use_clamp = False
    math_004 = peg.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'DIVIDE'
    math_004.use_clamp = False
    math_005 = peg.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'CEIL'
    math_005.use_clamp = False
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
    reroute_007 = peg.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.socket_idname = "NodeSocketFloat"
    reroute_008 = peg.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.socket_idname = "NodeSocketFloat"
    set_material = peg.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    set_material.inputs[1].default_value = True
    frame.width, frame.height = 150.0, 100.0
    frame_001.width, frame_001.height = 150.0, 100.0
    frame_002.width, frame_002.height = 150.0, 100.0
    frame_003.width, frame_003.height = 150.0, 100.0
    frame_004.width, frame_004.height = 150.0, 100.0
    frame_005.width, frame_005.height = 150.0, 100.0
    frame_006.width, frame_006.height = 150.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    integer.width, integer.height = 140.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    random_value.width, random_value.height = 140.0, 100.0
    group_input_002.width, group_input_002.height = 140.0, 100.0
    random_value_001.width, random_value_001.height = 140.0, 100.0
    group_input_003.width, group_input_003.height = 140.0, 100.0
    integer_001.width, integer_001.height = 140.0, 100.0
    group_input_004.width, group_input_004.height = 140.0, 100.0
    reroute.width, reroute.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    scale_elements.width, scale_elements.height = 140.0, 100.0
    integer_002.width, integer_002.height = 140.0, 100.0
    group_input_005.width, group_input_005.height = 140.0, 100.0
    random_value_002.width, random_value_002.height = 140.0, 100.0
    group_input_006.width, group_input_006.height = 140.0, 100.0
    random_value_003.width, random_value_003.height = 140.0, 100.0
    group_input_007.width, group_input_007.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
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
    math_001.width, math_001.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    group_input_012.width, group_input_012.height = 140.0, 100.0
    integer_006.width, integer_006.height = 140.0, 100.0
    group_input_013.width, group_input_013.height = 140.0, 100.0
    random_value_006.width, random_value_006.height = 140.0, 100.0
    reroute_001.width, reroute_001.height = 140.0, 100.0
    reroute_002.width, reroute_002.height = 140.0, 100.0
    reroute_003.width, reroute_003.height = 140.0, 100.0
    reroute_004.width, reroute_004.height = 140.0, 100.0
    reroute_005.width, reroute_005.height = 140.0, 100.0
    reroute_006.width, reroute_006.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    switch_001.width, switch_001.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    group_input_014.width, group_input_014.height = 140.0, 100.0
    switch_002.width, switch_002.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    reroute_007.width, reroute_007.height = 140.0, 100.0
    reroute_008.width, reroute_008.height = 140.0, 100.0
    set_material.width, set_material.height = 140.0, 100.0
    peg.links.new(group_input_003.outputs[0], random_value_001.inputs[8])
    peg.links.new(integer_001.outputs[0], random_value_001.inputs[7])
    peg.links.new(group_input.outputs[0], random_value.inputs[8])
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
    peg.links.new(random_value.outputs[3], reroute.inputs[0])
    peg.links.new(reroute.outputs[0], set_shade_smooth.inputs[2])
    peg.links.new(transform_geometry.outputs[0], set_shade_smooth.inputs[0])
    peg.links.new(math_001.outputs[0], math_002.inputs[1])
    peg.links.new(math_002.outputs[0], cone.inputs[4])
    peg.links.new(cone.outputs[3], set_shade_smooth.inputs[1])
    peg.links.new(cone.outputs[0], transform_geometry.inputs[0])
    peg.links.new(combine_xyz.outputs[0], transform_geometry.inputs[1])
    peg.links.new(math.outputs[0], combine_xyz.inputs[2])
    peg.links.new(random_value_004.outputs[1], reroute_004.inputs[0])
    peg.links.new(reroute_005.outputs[0], math.inputs[1])
    peg.links.new(reroute_005.outputs[0], cone.inputs[5])
    peg.links.new(reroute_006.outputs[0], cone.inputs[3])
    peg.links.new(random_value_006.outputs[1], reroute_001.inputs[0])
    peg.links.new(switch.outputs[0], reroute_003.inputs[0])
    peg.links.new(reroute_002.outputs[0], cone.inputs[0])
    peg.links.new(reroute_006.outputs[0], math_002.inputs[0])
    peg.links.new(set_material.outputs[0], group_output.inputs[0])
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
    peg.links.new(random_value_005.outputs[1], math_001.inputs[1])
    peg.links.new(reroute_001.outputs[0], reroute_006.inputs[0])
    peg.links.new(reroute_007.outputs[0], math_008.inputs[0])
    peg.links.new(reroute_003.outputs[0], math_008.inputs[1])
    peg.links.new(reroute_005.outputs[0], math_003.inputs[0])
    peg.links.new(reroute_008.outputs[0], math_003.inputs[1])
    peg.links.new(math_003.outputs[0], math_005.inputs[0])
    peg.links.new(switch_001.outputs[0], cone.inputs[1])
    peg.links.new(reroute_008.outputs[0], math_004.inputs[1])
    peg.links.new(math_004.outputs[0], math_006.inputs[0])
    peg.links.new(math_005.outputs[0], switch_001.inputs[2])
    peg.links.new(math_006.outputs[0], switch_002.inputs[2])
    peg.links.new(switch_002.outputs[0], cone.inputs[2])
    peg.links.new(group_input_014.outputs[13], switch_001.inputs[0])
    peg.links.new(group_input_014.outputs[13], switch_002.inputs[0])
    peg.links.new(reroute_003.outputs[0], reroute_002.inputs[0])
    peg.links.new(math_007.outputs[0], reroute_007.inputs[0])
    peg.links.new(reroute_006.outputs[0], math_007.inputs[0])
    peg.links.new(reroute_006.outputs[0], math_004.inputs[0])
    peg.links.new(reroute_004.outputs[0], reroute_005.inputs[0])
    peg.links.new(math_008.outputs[0], reroute_008.inputs[0])
    peg.links.new(scale_elements.outputs[0], set_material.inputs[0])
    return peg

peg = peg_node_group()


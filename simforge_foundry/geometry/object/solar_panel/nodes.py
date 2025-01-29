import bpy

def solarpanel_node_group():
    solarpanel = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "SolarPanel")
    solarpanel.color_tag = 'GEOMETRY'
    solarpanel.default_group_node_width = 140
    solarpanel.is_modifier = True
    geometry_socket = solarpanel.interface.new_socket(name = "geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    seed_socket = solarpanel.interface.new_socket(name = "seed", in_out='INPUT', socket_type = 'NodeSocketInt')
    seed_socket.default_value = 0
    seed_socket.min_value = 0
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.hide_value = True
    seed_socket.hide_in_modifier = True
    seed_socket.force_non_field = True
    scale_socket = solarpanel.interface.new_socket(name = "scale", in_out='INPUT', socket_type = 'NodeSocketVector')
    scale_socket.default_value = (1.0, 1.0, 0.05000000074505806)
    scale_socket.min_value = 0.0
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'TRANSLATION'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.force_non_field = True
    border_size_socket = solarpanel.interface.new_socket(name = "border_size", in_out='INPUT', socket_type = 'NodeSocketFloat')
    border_size_socket.default_value = 0.009999999776482582
    border_size_socket.min_value = 0.0
    border_size_socket.max_value = 3.4028234663852886e+38
    border_size_socket.subtype = 'DISTANCE'
    border_size_socket.attribute_domain = 'POINT'
    border_size_socket.force_non_field = True
    panel_depth_socket = solarpanel.interface.new_socket(name = "panel_depth", in_out='INPUT', socket_type = 'NodeSocketFloat')
    panel_depth_socket.default_value = 0.0020000000949949026
    panel_depth_socket.min_value = 0.0
    panel_depth_socket.max_value = 3.4028234663852886e+38
    panel_depth_socket.subtype = 'DISTANCE'
    panel_depth_socket.attribute_domain = 'POINT'
    panel_depth_socket.force_non_field = True
    with_back_panel_socket = solarpanel.interface.new_socket(name = "with_back_panel", in_out='INPUT', socket_type = 'NodeSocketBool')
    with_back_panel_socket.default_value = False
    with_back_panel_socket.attribute_domain = 'POINT'
    frame_mat_socket = solarpanel.interface.new_socket(name = "frame_mat", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    frame_mat_socket.attribute_domain = 'POINT'
    cells_mat_socket = solarpanel.interface.new_socket(name = "cells_mat", in_out='INPUT', socket_type = 'NodeSocketMaterial')
    cells_mat_socket.attribute_domain = 'POINT'
    group_input = solarpanel.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    group_output = solarpanel.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    set_material = solarpanel.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    integer_001 = solarpanel.nodes.new("FunctionNodeInputInt")
    integer_001.name = "Integer.001"
    integer_001.mute = True
    integer_001.integer = 0
    grid = solarpanel.nodes.new("GeometryNodeMeshGrid")
    grid.name = "Grid"
    grid.inputs[2].default_value = 2
    grid.inputs[3].default_value = 2
    extrude_mesh = solarpanel.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh.name = "Extrude Mesh"
    extrude_mesh.mode = 'FACES'
    extrude_mesh.inputs[1].default_value = True
    extrude_mesh.inputs[2].default_value = (0.0, 0.0, 0.0)
    extrude_mesh.inputs[4].default_value = False
    extrude_mesh_001 = solarpanel.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_001.name = "Extrude Mesh.001"
    extrude_mesh_001.mode = 'FACES'
    extrude_mesh_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    extrude_mesh_001.inputs[4].default_value = False
    extrude_mesh_002 = solarpanel.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_002.name = "Extrude Mesh.002"
    extrude_mesh_002.mode = 'FACES'
    extrude_mesh_002.inputs[4].default_value = False
    vector = solarpanel.nodes.new("FunctionNodeInputVector")
    vector.name = "Vector"
    vector.vector = (0.0, 0.0, -1.0)
    set_material_002 = solarpanel.nodes.new("GeometryNodeSetMaterial")
    set_material_002.name = "Set Material.002"
    set_material_002.inputs[1].default_value = True
    capture_attribute = solarpanel.nodes.new("GeometryNodeCaptureAttribute")
    capture_attribute.name = "Capture Attribute"
    capture_attribute.active_index = 0
    capture_attribute.capture_items.clear()
    capture_attribute.capture_items.new('FLOAT', "Index")
    capture_attribute.capture_items["Index"].data_type = 'INT'
    capture_attribute.domain = 'POINT'
    index = solarpanel.nodes.new("GeometryNodeInputIndex")
    index.name = "Index"
    delete_geometry = solarpanel.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry.name = "Delete Geometry"
    delete_geometry.domain = 'POINT'
    delete_geometry.mode = 'ALL'
    compare = solarpanel.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.data_type = 'INT'
    compare.mode = 'ELEMENT'
    compare.operation = 'EQUAL'
    mesh_to_curve = solarpanel.nodes.new("GeometryNodeMeshToCurve")
    mesh_to_curve.name = "Mesh to Curve"
    position = solarpanel.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"
    separate_xyz = solarpanel.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"
    separate_xyz.outputs[0].hide = True
    separate_xyz.outputs[1].hide = True
    compare_001 = solarpanel.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = 'FLOAT'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'
    compare_001.inputs[1].default_value = 0.0
    compare_001.inputs[12].default_value = 0.0
    fill_curve = solarpanel.nodes.new("GeometryNodeFillCurve")
    fill_curve.name = "Fill Curve"
    fill_curve.mode = 'NGONS'
    fill_curve.inputs[1].default_value = 0
    join_geometry = solarpanel.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"
    merge_by_distance = solarpanel.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = 'ALL'
    merge_by_distance.inputs[1].default_value = True
    merge_by_distance.inputs[2].default_value = 9.999999747378752e-05
    frame = solarpanel.nodes.new("NodeFrame")
    frame.name = "Frame"
    frame_001 = solarpanel.nodes.new("NodeFrame")
    frame_001.name = "Frame.001"
    frame_002 = solarpanel.nodes.new("NodeFrame")
    frame_002.name = "Frame.002"
    reroute = solarpanel.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketBool"
    reroute_001 = solarpanel.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketBool"
    reroute_002 = solarpanel.nodes.new("NodeReroute")
    reroute_002.name = "Reroute.002"
    reroute_002.socket_idname = "NodeSocketInt"
    reroute_003 = solarpanel.nodes.new("NodeReroute")
    reroute_003.name = "Reroute.003"
    reroute_003.socket_idname = "NodeSocketGeometry"
    reroute_004 = solarpanel.nodes.new("NodeReroute")
    reroute_004.name = "Reroute.004"
    reroute_004.socket_idname = "NodeSocketGeometry"
    reroute_005 = solarpanel.nodes.new("NodeReroute")
    reroute_005.name = "Reroute.005"
    reroute_005.socket_idname = "NodeSocketGeometry"
    switch = solarpanel.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.input_type = 'GEOMETRY'
    integer_math = solarpanel.nodes.new("FunctionNodeIntegerMath")
    integer_math.name = "Integer Math"
    integer_math.mute = True
    integer_math.operation = 'ADD'
    reroute_006 = solarpanel.nodes.new("NodeReroute")
    reroute_006.name = "Reroute.006"
    reroute_006.mute = True
    reroute_006.socket_idname = "NodeSocketInt"
    separate_xyz_001 = solarpanel.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"
    reroute_007 = solarpanel.nodes.new("NodeReroute")
    reroute_007.name = "Reroute.007"
    reroute_007.socket_idname = "NodeSocketFloatDistance"
    reroute_008 = solarpanel.nodes.new("NodeReroute")
    reroute_008.name = "Reroute.008"
    reroute_008.socket_idname = "NodeSocketFloatDistance"
    reroute_009 = solarpanel.nodes.new("NodeReroute")
    reroute_009.name = "Reroute.009"
    reroute_009.socket_idname = "NodeSocketBool"
    merge_by_distance_001 = solarpanel.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_001.name = "Merge by Distance.001"
    merge_by_distance_001.mode = 'ALL'
    merge_by_distance_001.inputs[1].default_value = True
    merge_by_distance_001.inputs[2].default_value = 9.999999747378752e-05
    switch_001 = solarpanel.nodes.new("GeometryNodeSwitch")
    switch_001.name = "Switch.001"
    switch_001.input_type = 'GEOMETRY'
    compare_002 = solarpanel.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = 'FLOAT'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'EQUAL'
    compare_002.inputs[1].default_value = 0.0
    compare_002.inputs[12].default_value = 0.0
    reroute_010 = solarpanel.nodes.new("NodeReroute")
    reroute_010.name = "Reroute.010"
    reroute_010.socket_idname = "NodeSocketGeometry"
    group_input.width, group_input.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    set_material.width, set_material.height = 140.0, 100.0
    integer_001.width, integer_001.height = 140.0, 100.0
    grid.width, grid.height = 140.0, 100.0
    extrude_mesh.width, extrude_mesh.height = 140.0, 100.0
    extrude_mesh_001.width, extrude_mesh_001.height = 140.0, 100.0
    extrude_mesh_002.width, extrude_mesh_002.height = 140.0, 100.0
    vector.width, vector.height = 140.0, 100.0
    set_material_002.width, set_material_002.height = 140.0, 100.0
    capture_attribute.width, capture_attribute.height = 140.0, 100.0
    index.width, index.height = 140.0, 100.0
    delete_geometry.width, delete_geometry.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    mesh_to_curve.width, mesh_to_curve.height = 140.0, 100.0
    position.width, position.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    fill_curve.width, fill_curve.height = 140.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
    frame.width, frame.height = 150.0, 100.0
    frame_001.width, frame_001.height = 150.0, 100.0
    frame_002.width, frame_002.height = 150.0, 100.0
    reroute.width, reroute.height = 140.0, 100.0
    reroute_001.width, reroute_001.height = 140.0, 100.0
    reroute_002.width, reroute_002.height = 140.0, 100.0
    reroute_003.width, reroute_003.height = 140.0, 100.0
    reroute_004.width, reroute_004.height = 140.0, 100.0
    reroute_005.width, reroute_005.height = 140.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    integer_math.width, integer_math.height = 140.0, 100.0
    reroute_006.width, reroute_006.height = 140.0, 100.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    reroute_007.width, reroute_007.height = 140.0, 100.0
    reroute_008.width, reroute_008.height = 140.0, 100.0
    reroute_009.width, reroute_009.height = 140.0, 100.0
    merge_by_distance_001.width, merge_by_distance_001.height = 140.0, 100.0
    switch_001.width, switch_001.height = 140.0, 100.0
    compare_002.width, compare_002.height = 140.0, 100.0
    reroute_010.width, reroute_010.height = 140.0, 100.0
    solarpanel.links.new(set_material.outputs[0], group_output.inputs[0])
    solarpanel.links.new(capture_attribute.outputs[0], extrude_mesh.inputs[0])
    solarpanel.links.new(extrude_mesh.outputs[2], extrude_mesh_001.inputs[1])
    solarpanel.links.new(reroute.outputs[0], extrude_mesh_002.inputs[1])
    solarpanel.links.new(vector.outputs[0], extrude_mesh_002.inputs[2])
    solarpanel.links.new(set_material_002.outputs[0], set_material.inputs[0])
    solarpanel.links.new(extrude_mesh_002.outputs[1], set_material.inputs[1])
    solarpanel.links.new(grid.outputs[0], capture_attribute.inputs[0])
    solarpanel.links.new(index.outputs[0], capture_attribute.inputs[1])
    solarpanel.links.new(reroute_002.outputs[0], compare.inputs[2])
    solarpanel.links.new(index.outputs[0], compare.inputs[3])
    solarpanel.links.new(compare.outputs[0], delete_geometry.inputs[1])
    solarpanel.links.new(extrude_mesh.outputs[0], extrude_mesh_001.inputs[0])
    solarpanel.links.new(extrude_mesh_001.outputs[0], delete_geometry.inputs[0])
    solarpanel.links.new(position.outputs[0], separate_xyz.inputs[0])
    solarpanel.links.new(separate_xyz.outputs[2], compare_001.inputs[0])
    solarpanel.links.new(compare_001.outputs[0], mesh_to_curve.inputs[1])
    solarpanel.links.new(mesh_to_curve.outputs[0], fill_curve.inputs[0])
    solarpanel.links.new(join_geometry.outputs[0], merge_by_distance.inputs[0])
    solarpanel.links.new(reroute_004.outputs[0], mesh_to_curve.inputs[0])
    solarpanel.links.new(reroute_001.outputs[0], reroute.inputs[0])
    solarpanel.links.new(extrude_mesh.outputs[1], reroute_001.inputs[0])
    solarpanel.links.new(capture_attribute.outputs[1], reroute_002.inputs[0])
    solarpanel.links.new(reroute_003.outputs[0], reroute_004.inputs[0])
    solarpanel.links.new(reroute_004.outputs[0], reroute_005.inputs[0])
    solarpanel.links.new(merge_by_distance.outputs[0], switch.inputs[2])
    solarpanel.links.new(switch.outputs[0], extrude_mesh_002.inputs[0])
    solarpanel.links.new(reroute_005.outputs[0], switch.inputs[1])
    solarpanel.links.new(fill_curve.outputs[0], join_geometry.inputs[0])
    solarpanel.links.new(integer_001.outputs[0], integer_math.inputs[0])
    solarpanel.links.new(group_input.outputs[0], integer_math.inputs[1])
    solarpanel.links.new(integer_math.outputs[0], reroute_006.inputs[0])
    solarpanel.links.new(group_input.outputs[1], separate_xyz_001.inputs[0])
    solarpanel.links.new(separate_xyz_001.outputs[0], grid.inputs[0])
    solarpanel.links.new(separate_xyz_001.outputs[1], grid.inputs[1])
    solarpanel.links.new(separate_xyz_001.outputs[2], extrude_mesh.inputs[3])
    solarpanel.links.new(reroute_007.outputs[0], extrude_mesh_001.inputs[3])
    solarpanel.links.new(group_input.outputs[2], reroute_007.inputs[0])
    solarpanel.links.new(group_input.outputs[3], reroute_008.inputs[0])
    solarpanel.links.new(reroute_008.outputs[0], extrude_mesh_002.inputs[3])
    solarpanel.links.new(group_input.outputs[4], reroute_009.inputs[0])
    solarpanel.links.new(reroute_008.outputs[0], compare_002.inputs[0])
    solarpanel.links.new(merge_by_distance_001.outputs[0], switch_001.inputs[2])
    solarpanel.links.new(reroute_010.outputs[0], merge_by_distance_001.inputs[0])
    solarpanel.links.new(reroute_010.outputs[0], switch_001.inputs[1])
    solarpanel.links.new(switch_001.outputs[0], set_material_002.inputs[0])
    solarpanel.links.new(reroute_009.outputs[0], switch.inputs[0])
    solarpanel.links.new(compare_002.outputs[0], switch_001.inputs[0])
    solarpanel.links.new(extrude_mesh_002.outputs[0], reroute_010.inputs[0])
    solarpanel.links.new(group_input.outputs[5], set_material_002.inputs[2])
    solarpanel.links.new(group_input.outputs[6], set_material.inputs[2])
    solarpanel.links.new(delete_geometry.outputs[0], reroute_003.inputs[0])
    solarpanel.links.new(reroute_005.outputs[0], join_geometry.inputs[0])
    return solarpanel

solarpanel = solarpanel_node_group()


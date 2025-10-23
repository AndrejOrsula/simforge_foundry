import bpy
import mathutils


def bag_node_group():
    """Initialize bag node group"""
    bag = bpy.data.node_groups.new(type='GeometryNodeTree', name="Bag")

    bag.color_tag = 'NONE'
    bag.description = ""
    bag.default_group_node_width = 140
    bag.is_modifier = True

    # bag interface

    # Socket Geometry
    geometry_socket = bag.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket.attribute_domain = 'POINT'
    geometry_socket.default_input = 'VALUE'
    geometry_socket.structure_type = 'AUTO'

    # Socket scale
    scale_socket = bag.interface.new_socket(name="scale", in_out='INPUT', socket_type='NodeSocketVector')
    scale_socket.default_value = (0.75, 0.3333333432674408, 0.25)
    scale_socket.min_value = -10000.0
    scale_socket.max_value = 10000.0
    scale_socket.subtype = 'XYZ'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.force_non_field = True
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'SINGLE'

    # Socket base_geometry
    base_geometry_socket = bag.interface.new_socket(name="base_geometry", in_out='INPUT', socket_type='NodeSocketVector')
    base_geometry_socket.dimensions = 2
    # Get the socket again, as its default value could have been updated
    base_geometry_socket = bag.interface.items_tree[base_geometry_socket.index]
    base_geometry_socket.default_value = (2.0, 2.0)
    base_geometry_socket.min_value = 2.0
    base_geometry_socket.max_value = 12.0
    base_geometry_socket.subtype = 'NONE'
    base_geometry_socket.attribute_domain = 'POINT'
    base_geometry_socket.force_non_field = True
    base_geometry_socket.default_input = 'VALUE'
    base_geometry_socket.structure_type = 'SINGLE'

    # Socket detail
    detail_socket = bag.interface.new_socket(name="detail", in_out='INPUT', socket_type='NodeSocketInt')
    detail_socket.default_value = 2
    detail_socket.min_value = 0
    detail_socket.max_value = 6
    detail_socket.subtype = 'NONE'
    detail_socket.attribute_domain = 'POINT'
    detail_socket.force_non_field = True
    detail_socket.default_input = 'VALUE'
    detail_socket.structure_type = 'SINGLE'

    # Socket seam_thickness
    seam_thickness_socket = bag.interface.new_socket(name="seam_thickness", in_out='INPUT', socket_type='NodeSocketFloat')
    seam_thickness_socket.default_value = 0.0
    seam_thickness_socket.min_value = 0.0
    seam_thickness_socket.max_value = 3.4028234663852886e+38
    seam_thickness_socket.subtype = 'DISTANCE'
    seam_thickness_socket.attribute_domain = 'POINT'
    seam_thickness_socket.force_non_field = True
    seam_thickness_socket.default_input = 'VALUE'
    seam_thickness_socket.structure_type = 'SINGLE'

    # Socket bag_taper
    bag_taper_socket = bag.interface.new_socket(name="bag_taper", in_out='INPUT', socket_type='NodeSocketVector')
    bag_taper_socket.default_value = (0.05000000074505806, 0.07500000298023224, 0.4000000059604645)
    bag_taper_socket.min_value = 0.0010000000474974513
    bag_taper_socket.max_value = 1.0
    bag_taper_socket.subtype = 'FACTOR'
    bag_taper_socket.attribute_domain = 'POINT'
    bag_taper_socket.force_non_field = True
    bag_taper_socket.default_input = 'VALUE'
    bag_taper_socket.structure_type = 'SINGLE'

    # Socket neck_taper
    neck_taper_socket = bag.interface.new_socket(name="neck_taper", in_out='INPUT', socket_type='NodeSocketVector')
    neck_taper_socket.default_value = (0.20000000298023224, 0.25, 0.15000000596046448)
    neck_taper_socket.min_value = 0.0010000000474974513
    neck_taper_socket.max_value = 1.0
    neck_taper_socket.subtype = 'FACTOR'
    neck_taper_socket.attribute_domain = 'POINT'
    neck_taper_socket.force_non_field = True
    neck_taper_socket.default_input = 'VALUE'
    neck_taper_socket.structure_type = 'SINGLE'

    # Socket neck_thickness
    neck_thickness_socket = bag.interface.new_socket(name="neck_thickness", in_out='INPUT', socket_type='NodeSocketFloat')
    neck_thickness_socket.default_value = 0.004999999888241291
    neck_thickness_socket.min_value = 9.999999747378752e-05
    neck_thickness_socket.max_value = 3.4028234663852886e+38
    neck_thickness_socket.subtype = 'DISTANCE'
    neck_thickness_socket.attribute_domain = 'POINT'
    neck_thickness_socket.force_non_field = True
    neck_thickness_socket.default_input = 'VALUE'
    neck_thickness_socket.structure_type = 'SINGLE'

    # Socket edge_crease
    edge_crease_socket = bag.interface.new_socket(name="edge_crease", in_out='INPUT', socket_type='NodeSocketFloat')
    edge_crease_socket.default_value = 0.20000000298023224
    edge_crease_socket.min_value = 0.0
    edge_crease_socket.max_value = 1.0
    edge_crease_socket.subtype = 'FACTOR'
    edge_crease_socket.attribute_domain = 'POINT'
    edge_crease_socket.force_non_field = True
    edge_crease_socket.default_input = 'VALUE'
    edge_crease_socket.structure_type = 'SINGLE'

    # Socket vertex_crease
    vertex_crease_socket = bag.interface.new_socket(name="vertex_crease", in_out='INPUT', socket_type='NodeSocketFloat')
    vertex_crease_socket.default_value = 0.3333333432674408
    vertex_crease_socket.min_value = 0.0
    vertex_crease_socket.max_value = 1.0
    vertex_crease_socket.subtype = 'FACTOR'
    vertex_crease_socket.attribute_domain = 'POINT'
    vertex_crease_socket.force_non_field = True
    vertex_crease_socket.default_input = 'VALUE'
    vertex_crease_socket.structure_type = 'SINGLE'

    # Socket mat
    mat_socket = bag.interface.new_socket(name="mat", in_out='INPUT', socket_type='NodeSocketMaterial')
    mat_socket.attribute_domain = 'POINT'
    mat_socket.default_input = 'VALUE'
    mat_socket.structure_type = 'AUTO'

    # Initialize bag nodes

    # Node Group Output
    group_output = bag.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Grid
    grid = bag.nodes.new("GeometryNodeMeshGrid")
    grid.name = "Grid"

    # Node Extrude Mesh
    extrude_mesh = bag.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh.name = "Extrude Mesh"
    extrude_mesh.mode = 'FACES'
    # Offset
    extrude_mesh.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Individual
    extrude_mesh.inputs[4].default_value = False

    # Node Math
    math = bag.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'DIVIDE'
    math.use_clamp = False
    # Value_001
    math.inputs[1].default_value = 2.0

    # Node Transform Geometry
    transform_geometry = bag.nodes.new("GeometryNodeTransform")
    transform_geometry.name = "Transform Geometry"
    transform_geometry.mode = 'COMPONENTS'
    # Rotation
    transform_geometry.inputs[2].default_value = (0.0, 1.5707963705062866, 1.5707963705062866)
    # Scale
    transform_geometry.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Join Geometry
    join_geometry = bag.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # Node Merge by Distance
    merge_by_distance = bag.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance.name = "Merge by Distance"
    merge_by_distance.mode = 'ALL'
    # Selection
    merge_by_distance.inputs[1].default_value = True
    # Distance
    merge_by_distance.inputs[2].default_value = 0.0010000000474974513

    # Node Transform Geometry.001
    transform_geometry_001 = bag.nodes.new("GeometryNodeTransform")
    transform_geometry_001.name = "Transform Geometry.001"
    transform_geometry_001.mode = 'COMPONENTS'
    # Translation
    transform_geometry_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    transform_geometry_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    transform_geometry_001.inputs[3].default_value = (1.0, -1.0, 1.0)

    # Node Reroute
    reroute = bag.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketGeometry"
    # Node Set Shade Smooth
    set_shade_smooth = bag.nodes.new("GeometryNodeSetShadeSmooth")
    set_shade_smooth.name = "Set Shade Smooth"
    set_shade_smooth.domain = 'FACE'
    # Selection
    set_shade_smooth.inputs[1].default_value = True
    # Shade Smooth
    set_shade_smooth.inputs[2].default_value = True

    # Node Normal
    normal = bag.nodes.new("GeometryNodeInputNormal")
    normal.name = "Normal"
    normal.legacy_corner_normals = False

    # Node Extrude Mesh.001
    extrude_mesh_001 = bag.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_001.name = "Extrude Mesh.001"
    extrude_mesh_001.mode = 'FACES'
    # Individual
    extrude_mesh_001.inputs[4].default_value = False

    # Node Compare.001
    compare_001 = bag.nodes.new("FunctionNodeCompare")
    compare_001.name = "Compare.001"
    compare_001.data_type = 'VECTOR'
    compare_001.mode = 'ELEMENT'
    compare_001.operation = 'EQUAL'
    # B_VEC3
    compare_001.inputs[5].default_value = (0.0, 0.0, 1.0)
    # Epsilon
    compare_001.inputs[12].default_value = 0.0010000000474974513

    # Node Vector
    vector = bag.nodes.new("FunctionNodeInputVector")
    vector.name = "Vector"
    vector.vector = (0.0, 0.0, 1.0)

    # Node Flip Faces
    flip_faces = bag.nodes.new("GeometryNodeFlipFaces")
    flip_faces.name = "Flip Faces"
    # Selection
    flip_faces.inputs[1].default_value = True

    # Node Scale Elements
    scale_elements = bag.nodes.new("GeometryNodeScaleElements")
    scale_elements.name = "Scale Elements"
    scale_elements.domain = 'FACE'
    scale_elements.scale_mode = 'SINGLE_AXIS'
    # Axis
    scale_elements.inputs[4].default_value = (1.0, 0.0, 0.0)

    # Node Compare.002
    compare_002 = bag.nodes.new("FunctionNodeCompare")
    compare_002.name = "Compare.002"
    compare_002.data_type = 'VECTOR'
    compare_002.mode = 'ELEMENT'
    compare_002.operation = 'EQUAL'
    # B_VEC3
    compare_002.inputs[5].default_value = (0.0, 1.0, 0.0)
    # Epsilon
    compare_002.inputs[12].default_value = 0.0010000000474974513

    # Node Vector.001
    vector_001 = bag.nodes.new("FunctionNodeInputVector")
    vector_001.name = "Vector.001"
    vector_001.vector = (0.0, 0.0, 0.0)

    # Node Scale Elements.001
    scale_elements_001 = bag.nodes.new("GeometryNodeScaleElements")
    scale_elements_001.name = "Scale Elements.001"
    scale_elements_001.domain = 'FACE'
    scale_elements_001.scale_mode = 'SINGLE_AXIS'
    # Axis
    scale_elements_001.inputs[4].default_value = (0.0, 1.0, 0.0)

    # Node Extrude Mesh.002
    extrude_mesh_002 = bag.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_002.name = "Extrude Mesh.002"
    extrude_mesh_002.mode = 'FACES'
    # Individual
    extrude_mesh_002.inputs[4].default_value = False

    # Node Scale Elements.002
    scale_elements_002 = bag.nodes.new("GeometryNodeScaleElements")
    scale_elements_002.name = "Scale Elements.002"
    scale_elements_002.domain = 'FACE'
    scale_elements_002.scale_mode = 'SINGLE_AXIS'
    # Axis
    scale_elements_002.inputs[4].default_value = (1.0, 0.0, 0.0)

    # Node Scale Elements.003
    scale_elements_003 = bag.nodes.new("GeometryNodeScaleElements")
    scale_elements_003.name = "Scale Elements.003"
    scale_elements_003.domain = 'FACE'
    scale_elements_003.scale_mode = 'SINGLE_AXIS'
    # Axis
    scale_elements_003.inputs[4].default_value = (0.0, 1.0, 0.0)

    # Node Delete Geometry.001
    delete_geometry_001 = bag.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_001.name = "Delete Geometry.001"
    delete_geometry_001.domain = 'FACE'
    delete_geometry_001.mode = 'ALL'

    # Node Subdivision Surface
    subdivision_surface = bag.nodes.new("GeometryNodeSubdivisionSurface")
    subdivision_surface.name = "Subdivision Surface"
    subdivision_surface.boundary_smooth = 'ALL'
    subdivision_surface.uv_smooth = 'PRESERVE_BOUNDARIES'
    # Limit Surface
    subdivision_surface.inputs[4].default_value = True

    # Node Delete Geometry.002
    delete_geometry_002 = bag.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_002.name = "Delete Geometry.002"
    delete_geometry_002.domain = 'FACE'
    delete_geometry_002.mode = 'ALL'

    # Node Switch
    switch = bag.nodes.new("GeometryNodeSwitch")
    switch.name = "Switch"
    switch.mute = True
    switch.input_type = 'GEOMETRY'

    # Node Boolean
    boolean = bag.nodes.new("FunctionNodeInputBool")
    boolean.label = "hollow bag"
    boolean.name = "Boolean"
    boolean.boolean = False

    # Node Extrude Mesh.003
    extrude_mesh_003 = bag.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_003.name = "Extrude Mesh.003"
    extrude_mesh_003.mode = 'FACES'
    # Offset Scale
    extrude_mesh_003.inputs[3].default_value = 9.999999747378752e-05
    # Individual
    extrude_mesh_003.inputs[4].default_value = False

    # Node Scale Elements.004
    scale_elements_004 = bag.nodes.new("GeometryNodeScaleElements")
    scale_elements_004.name = "Scale Elements.004"
    scale_elements_004.domain = 'FACE'
    scale_elements_004.scale_mode = 'SINGLE_AXIS'
    # Axis
    scale_elements_004.inputs[4].default_value = (1.0, 0.0, 0.0)

    # Node Scale Elements.005
    scale_elements_005 = bag.nodes.new("GeometryNodeScaleElements")
    scale_elements_005.name = "Scale Elements.005"
    scale_elements_005.domain = 'FACE'
    scale_elements_005.scale_mode = 'SINGLE_AXIS'
    # Axis
    scale_elements_005.inputs[4].default_value = (0.0, 1.0, 0.0)

    # Node Extrude Mesh.004
    extrude_mesh_004 = bag.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_004.name = "Extrude Mesh.004"
    extrude_mesh_004.mode = 'FACES'
    # Individual
    extrude_mesh_004.inputs[4].default_value = False

    # Node Scale Elements.006
    scale_elements_006 = bag.nodes.new("GeometryNodeScaleElements")
    scale_elements_006.name = "Scale Elements.006"
    scale_elements_006.domain = 'FACE'
    scale_elements_006.scale_mode = 'SINGLE_AXIS'
    # Axis
    scale_elements_006.inputs[4].default_value = (1.0, 0.0, 0.0)

    # Node Scale Elements.007
    scale_elements_007 = bag.nodes.new("GeometryNodeScaleElements")
    scale_elements_007.name = "Scale Elements.007"
    scale_elements_007.domain = 'FACE'
    scale_elements_007.scale_mode = 'SINGLE_AXIS'
    # Axis
    scale_elements_007.inputs[4].default_value = (0.0, 1.0, 0.0)

    # Node Delete Geometry.003
    delete_geometry_003 = bag.nodes.new("GeometryNodeDeleteGeometry")
    delete_geometry_003.name = "Delete Geometry.003"
    delete_geometry_003.domain = 'FACE'
    delete_geometry_003.mode = 'ALL'

    # Node Vector Math
    vector_math = bag.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'ABSOLUTE'

    # Node Position
    position = bag.nodes.new("GeometryNodeInputPosition")
    position.name = "Position"

    # Node Boolean Math
    boolean_math = bag.nodes.new("FunctionNodeBooleanMath")
    boolean_math.name = "Boolean Math"
    boolean_math.operation = 'AND'

    # Node Compare.003
    compare_003 = bag.nodes.new("FunctionNodeCompare")
    compare_003.name = "Compare.003"
    compare_003.data_type = 'FLOAT'
    compare_003.mode = 'ELEMENT'
    compare_003.operation = 'EQUAL'
    # B
    compare_003.inputs[1].default_value = 0.0
    # Epsilon
    compare_003.inputs[12].default_value = 0.0010000000474974513

    # Node Separate XYZ
    separate_xyz = bag.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz.name = "Separate XYZ"

    # Node Vector Math.001
    vector_math_001 = bag.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'SCALE'
    # Scale
    vector_math_001.inputs[3].default_value = -1.0

    # Node Extrude Mesh.005
    extrude_mesh_005 = bag.nodes.new("GeometryNodeExtrudeMesh")
    extrude_mesh_005.name = "Extrude Mesh.005"
    extrude_mesh_005.mode = 'FACES'
    # Offset
    extrude_mesh_005.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Individual
    extrude_mesh_005.inputs[4].default_value = False

    # Node Normal.001
    normal_001 = bag.nodes.new("GeometryNodeInputNormal")
    normal_001.name = "Normal.001"
    normal_001.legacy_corner_normals = False

    # Node Compare.004
    compare_004 = bag.nodes.new("FunctionNodeCompare")
    compare_004.name = "Compare.004"
    compare_004.data_type = 'VECTOR'
    compare_004.mode = 'ELEMENT'
    compare_004.operation = 'EQUAL'
    # B_VEC3
    compare_004.inputs[5].default_value = (0.0, 1.0, 0.0)
    # Epsilon
    compare_004.inputs[12].default_value = 0.0010000000474974513

    # Node Vector Math.002
    vector_math_002 = bag.nodes.new("ShaderNodeVectorMath")
    vector_math_002.name = "Vector Math.002"
    vector_math_002.operation = 'ABSOLUTE'

    # Node Position.002
    position_002 = bag.nodes.new("GeometryNodeInputPosition")
    position_002.name = "Position.002"

    # Node Compare.005
    compare_005 = bag.nodes.new("FunctionNodeCompare")
    compare_005.name = "Compare.005"
    compare_005.data_type = 'FLOAT'
    compare_005.mode = 'ELEMENT'
    compare_005.operation = 'LESS_EQUAL'

    # Node Separate XYZ.001
    separate_xyz_001 = bag.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_001.name = "Separate XYZ.001"

    # Node Boolean Math.001
    boolean_math_001 = bag.nodes.new("FunctionNodeBooleanMath")
    boolean_math_001.name = "Boolean Math.001"
    boolean_math_001.operation = 'AND'

    # Node Compare.006
    compare_006 = bag.nodes.new("FunctionNodeCompare")
    compare_006.name = "Compare.006"
    compare_006.data_type = 'VECTOR'
    compare_006.mode = 'ELEMENT'
    compare_006.operation = 'EQUAL'
    # B_VEC3
    compare_006.inputs[5].default_value = (1.0, 0.0, 0.0)
    # Epsilon
    compare_006.inputs[12].default_value = 0.0010000000474974513

    # Node Math.001
    math_001 = bag.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'SUBTRACT'
    math_001.use_clamp = False

    # Node Clamp
    clamp = bag.nodes.new("ShaderNodeClamp")
    clamp.name = "Clamp"
    clamp.clamp_type = 'MINMAX'
    # Min
    clamp.inputs[1].default_value = 0.0

    # Node Math.002
    math_002 = bag.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'DIVIDE'
    math_002.use_clamp = False
    # Value_001
    math_002.inputs[1].default_value = 4.0

    # Node Scale Elements.008
    scale_elements_008 = bag.nodes.new("GeometryNodeScaleElements")
    scale_elements_008.name = "Scale Elements.008"
    scale_elements_008.domain = 'FACE'
    scale_elements_008.scale_mode = 'SINGLE_AXIS'
    # Axis
    scale_elements_008.inputs[4].default_value = (0.0, 1.0, 0.0)

    # Node Boolean Math.002
    boolean_math_002 = bag.nodes.new("FunctionNodeBooleanMath")
    boolean_math_002.name = "Boolean Math.002"
    boolean_math_002.operation = 'AND'

    # Node Compare.007
    compare_007 = bag.nodes.new("FunctionNodeCompare")
    compare_007.name = "Compare.007"
    compare_007.data_type = 'FLOAT'
    compare_007.mode = 'ELEMENT'
    compare_007.operation = 'LESS_EQUAL'

    # Node Merge by Distance.001
    merge_by_distance_001 = bag.nodes.new("GeometryNodeMergeByDistance")
    merge_by_distance_001.name = "Merge by Distance.001"
    merge_by_distance_001.mode = 'ALL'
    # Selection
    merge_by_distance_001.inputs[1].default_value = True
    # Distance
    merge_by_distance_001.inputs[2].default_value = 0.0010000000474974513

    # Node Math.003
    math_003 = bag.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'DIVIDE'
    math_003.use_clamp = False

    # Node Math.004
    math_004 = bag.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'ADD'
    math_004.use_clamp = False
    # Value_001
    math_004.inputs[1].default_value = 1.0

    # Node Compare
    compare = bag.nodes.new("FunctionNodeCompare")
    compare.name = "Compare"
    compare.mute = True
    compare.data_type = 'FLOAT'
    compare.mode = 'ELEMENT'
    compare.operation = 'GREATER_EQUAL'

    # Node Position.001
    position_001 = bag.nodes.new("GeometryNodeInputPosition")
    position_001.name = "Position.001"
    position_001.mute = True

    # Node Separate XYZ.002
    separate_xyz_002 = bag.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_002.name = "Separate XYZ.002"
    separate_xyz_002.mute = True

    # Node Math.005
    math_005 = bag.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.mute = True
    math_005.operation = 'DIVIDE'
    math_005.use_clamp = False
    # Value_001
    math_005.inputs[1].default_value = 2.25

    # Node Set Position
    set_position = bag.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    # Position
    set_position.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Wave Texture
    wave_texture = bag.nodes.new("ShaderNodeTexWave")
    wave_texture.name = "Wave Texture"
    wave_texture.mute = True
    wave_texture.bands_direction = 'X'
    wave_texture.rings_direction = 'Z'
    wave_texture.wave_profile = 'SIN'
    wave_texture.wave_type = 'BANDS'
    # Vector
    wave_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Scale
    wave_texture.inputs[1].default_value = 2.0
    # Distortion
    wave_texture.inputs[2].default_value = 0.0
    # Detail
    wave_texture.inputs[3].default_value = 2.0
    # Detail Scale
    wave_texture.inputs[4].default_value = 1.0
    # Detail Roughness
    wave_texture.inputs[5].default_value = 0.0
    # Phase Offset
    wave_texture.inputs[6].default_value = 0.0

    # Node Normal.002
    normal_002 = bag.nodes.new("GeometryNodeInputNormal")
    normal_002.name = "Normal.002"
    normal_002.mute = True
    normal_002.legacy_corner_normals = False

    # Node Vector Math.003
    vector_math_003 = bag.nodes.new("ShaderNodeVectorMath")
    vector_math_003.name = "Vector Math.003"
    vector_math_003.mute = True
    vector_math_003.operation = 'SCALE'

    # Node Math.006
    math_006 = bag.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.mute = True
    math_006.operation = 'MULTIPLY'
    math_006.use_clamp = False
    # Value_001
    math_006.inputs[1].default_value = 0.0010000000474974513

    # Node Math.007
    math_007 = bag.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.mute = True
    math_007.operation = 'ADD'
    math_007.use_clamp = False

    # Node Math.008
    math_008 = bag.nodes.new("ShaderNodeMath")
    math_008.name = "Math.008"
    math_008.mute = True
    math_008.operation = 'MULTIPLY'
    math_008.use_clamp = False

    # Node Math.009
    math_009 = bag.nodes.new("ShaderNodeMath")
    math_009.name = "Math.009"
    math_009.mute = True
    math_009.operation = 'SUBTRACT'
    math_009.use_clamp = False

    # Node Math.010
    math_010 = bag.nodes.new("ShaderNodeMath")
    math_010.name = "Math.010"
    math_010.mute = True
    math_010.operation = 'DIVIDE'
    math_010.use_clamp = False

    # Node Math.011
    math_011 = bag.nodes.new("ShaderNodeMath")
    math_011.name = "Math.011"
    math_011.mute = True
    math_011.operation = 'POWER'
    math_011.use_clamp = False
    # Value
    math_011.inputs[0].default_value = 0.5
    # Value_001
    math_011.inputs[1].default_value = 0.5

    # Node Attribute Statistic
    attribute_statistic = bag.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic.name = "Attribute Statistic"
    attribute_statistic.mute = True
    attribute_statistic.data_type = 'FLOAT_VECTOR'
    attribute_statistic.domain = 'POINT'
    # Selection
    attribute_statistic.inputs[1].default_value = True

    # Node Position.003
    position_003 = bag.nodes.new("GeometryNodeInputPosition")
    position_003.name = "Position.003"
    position_003.mute = True

    # Node Separate XYZ.003
    separate_xyz_003 = bag.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_003.name = "Separate XYZ.003"
    separate_xyz_003.mute = True

    # Node Math.012
    math_012 = bag.nodes.new("ShaderNodeMath")
    math_012.name = "Math.012"
    math_012.mute = True
    math_012.operation = 'SUBTRACT'
    math_012.use_clamp = False

    # Node Wave Texture.001
    wave_texture_001 = bag.nodes.new("ShaderNodeTexWave")
    wave_texture_001.name = "Wave Texture.001"
    wave_texture_001.mute = True
    wave_texture_001.bands_direction = 'Y'
    wave_texture_001.rings_direction = 'Z'
    wave_texture_001.wave_profile = 'SIN'
    wave_texture_001.wave_type = 'BANDS'
    # Vector
    wave_texture_001.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Scale
    wave_texture_001.inputs[1].default_value = 2.0
    # Distortion
    wave_texture_001.inputs[2].default_value = 0.0
    # Detail
    wave_texture_001.inputs[3].default_value = 2.0
    # Detail Scale
    wave_texture_001.inputs[4].default_value = 1.0
    # Detail Roughness
    wave_texture_001.inputs[5].default_value = 0.0
    # Phase Offset
    wave_texture_001.inputs[6].default_value = 2.3999998569488525

    # Node Math.013
    math_013 = bag.nodes.new("ShaderNodeMath")
    math_013.name = "Math.013"
    math_013.mute = True
    math_013.operation = 'DIVIDE'
    math_013.use_clamp = False
    # Value_001
    math_013.inputs[1].default_value = 2.0

    # Node Noise Texture
    noise_texture = bag.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.mute = True
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    # Vector
    noise_texture.inputs[0].default_value = (0.0, 0.0, 0.0)
    # Scale
    noise_texture.inputs[2].default_value = 4.0
    # Detail
    noise_texture.inputs[3].default_value = 4.199999809265137
    # Roughness
    noise_texture.inputs[4].default_value = 1.0
    # Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    # Distortion
    noise_texture.inputs[8].default_value = 1.0

    # Node Set Position.001
    set_position_001 = bag.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    set_position_001.mute = True
    # Selection
    set_position_001.inputs[1].default_value = True
    # Position
    set_position_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Vector Math.004
    vector_math_004 = bag.nodes.new("ShaderNodeVectorMath")
    vector_math_004.name = "Vector Math.004"
    vector_math_004.mute = True
    vector_math_004.operation = 'MULTIPLY'

    # Node Vector Math.005
    vector_math_005 = bag.nodes.new("ShaderNodeVectorMath")
    vector_math_005.name = "Vector Math.005"
    vector_math_005.mute = True
    vector_math_005.operation = 'SCALE'
    # Scale
    vector_math_005.inputs[3].default_value = 0.01249999925494194

    # Node Set Material
    set_material = bag.nodes.new("GeometryNodeSetMaterial")
    set_material.name = "Set Material"
    # Selection
    set_material.inputs[1].default_value = True

    # Node Separate XYZ.004
    separate_xyz_004 = bag.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_004.name = "Separate XYZ.004"
    separate_xyz_004.hide = True

    # Node Separate XYZ.005
    separate_xyz_005 = bag.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_005.name = "Separate XYZ.005"

    # Node Math.014
    math_014 = bag.nodes.new("ShaderNodeMath")
    math_014.name = "Math.014"
    math_014.operation = 'MULTIPLY'
    math_014.use_clamp = False

    # Node Math.015
    math_015 = bag.nodes.new("ShaderNodeMath")
    math_015.name = "Math.015"
    math_015.operation = 'SUBTRACT'
    math_015.use_clamp = False

    # Node Combine XYZ
    combine_xyz = bag.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz.name = "Combine XYZ"
    # X
    combine_xyz.inputs[0].default_value = 0.0
    # Y
    combine_xyz.inputs[1].default_value = 0.0

    # Node Math.016
    math_016 = bag.nodes.new("ShaderNodeMath")
    math_016.name = "Math.016"
    math_016.operation = 'MULTIPLY'
    math_016.use_clamp = False
    # Value_001
    math_016.inputs[1].default_value = -0.5

    # Node Separate XYZ.006
    separate_xyz_006 = bag.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_006.name = "Separate XYZ.006"

    # Node Math.017
    math_017 = bag.nodes.new("ShaderNodeMath")
    math_017.name = "Math.017"
    math_017.operation = 'DIVIDE'
    math_017.use_clamp = False

    # Node Math.018
    math_018 = bag.nodes.new("ShaderNodeMath")
    math_018.name = "Math.018"
    math_018.operation = 'DIVIDE'
    math_018.use_clamp = False

    # Node Math.019
    math_019 = bag.nodes.new("ShaderNodeMath")
    math_019.name = "Math.019"
    math_019.operation = 'MULTIPLY'
    math_019.use_clamp = False

    # Node Math.020
    math_020 = bag.nodes.new("ShaderNodeMath")
    math_020.name = "Math.020"
    math_020.operation = 'DIVIDE'
    math_020.use_clamp = False
    # Value
    math_020.inputs[0].default_value = 1.0

    # Node Math.021
    math_021 = bag.nodes.new("ShaderNodeMath")
    math_021.name = "Math.021"
    math_021.operation = 'DIVIDE'
    math_021.use_clamp = False
    # Value
    math_021.inputs[0].default_value = 1.0

    # Node Attribute Statistic.001
    attribute_statistic_001 = bag.nodes.new("GeometryNodeAttributeStatistic")
    attribute_statistic_001.name = "Attribute Statistic.001"
    attribute_statistic_001.data_type = 'FLOAT_VECTOR'
    attribute_statistic_001.domain = 'POINT'

    # Node Position.004
    position_004 = bag.nodes.new("GeometryNodeInputPosition")
    position_004.name = "Position.004"

    # Node Separate XYZ.007
    separate_xyz_007 = bag.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_007.name = "Separate XYZ.007"

    # Node Math.022
    math_022 = bag.nodes.new("ShaderNodeMath")
    math_022.name = "Math.022"
    math_022.operation = 'DIVIDE'
    math_022.use_clamp = False

    # Node Math.023
    math_023 = bag.nodes.new("ShaderNodeMath")
    math_023.name = "Math.023"
    math_023.operation = 'DIVIDE'
    math_023.use_clamp = False

    # Node Math.024
    math_024 = bag.nodes.new("ShaderNodeMath")
    math_024.name = "Math.024"
    math_024.operation = 'SUBTRACT'
    math_024.use_clamp = False

    # Node Math.025
    math_025 = bag.nodes.new("ShaderNodeMath")
    math_025.name = "Math.025"
    math_025.operation = 'SUBTRACT'
    math_025.use_clamp = False

    # Node Math.026
    math_026 = bag.nodes.new("ShaderNodeMath")
    math_026.name = "Math.026"
    math_026.operation = 'DIVIDE'
    math_026.use_clamp = False
    # Value_001
    math_026.inputs[1].default_value = 2.0

    # Node Group Input
    group_input = bag.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Separate XYZ.008
    separate_xyz_008 = bag.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_008.name = "Separate XYZ.008"

    # Node Float to Integer
    float_to_integer = bag.nodes.new("FunctionNodeFloatToInt")
    float_to_integer.name = "Float to Integer"
    float_to_integer.rounding_mode = 'FLOOR'

    # Node Float to Integer.001
    float_to_integer_001 = bag.nodes.new("FunctionNodeFloatToInt")
    float_to_integer_001.name = "Float to Integer.001"
    float_to_integer_001.rounding_mode = 'FLOOR'

    # Node Viewer
    viewer = bag.nodes.new("GeometryNodeViewer")
    viewer.name = "Viewer"
    viewer.data_type = 'FLOAT'
    viewer.domain = 'AUTO'
    viewer.ui_shortcut = 0
    # Value
    viewer.inputs[1].default_value = 0.0

    # Set locations
    group_output.location = (373.3685607910156, 0.0)
    grid.location = (-13308.64453125, 156.97427368164062)
    extrude_mesh.location = (-12091.931640625, 254.1893310546875)
    math.location = (-13241.328125, -61.47602081298828)
    transform_geometry.location = (-12913.4775390625, 351.66485595703125)
    join_geometry.location = (-3405.93310546875, 244.39549255371094)
    merge_by_distance.location = (-3212.031494140625, 216.07830810546875)
    transform_geometry_001.location = (-3825.913330078125, 583.853271484375)
    reroute.location = (-3950.472900390625, 213.77099609375)
    set_shade_smooth.location = (-466.6205139160156, 45.7214469909668)
    normal.location = (-10995.8818359375, 597.0608520507812)
    extrude_mesh_001.location = (-10132.5517578125, 360.5871276855469)
    compare_001.location = (-10780.5048828125, 680.11083984375)
    vector.location = (-10422.611328125, 176.23036193847656)
    flip_faces.location = (-3636.693359375, 373.5006408691406)
    scale_elements.location = (-9008.275390625, 695.5243530273438)
    compare_002.location = (-10204.93359375, 809.6356811523438)
    vector_001.location = (-9750.30859375, 724.8070068359375)
    scale_elements_001.location = (-8749.0771484375, 582.69140625)
    extrude_mesh_002.location = (-7966.4111328125, 562.4959106445312)
    scale_elements_002.location = (-7391.10546875, 444.8206481933594)
    scale_elements_003.location = (-7160.986328125, 474.8790588378906)
    delete_geometry_001.location = (-6923.3310546875, 277.3625183105469)
    subdivision_surface.location = (-3000.1572265625, 181.3656768798828)
    delete_geometry_002.location = (-6367.4287109375, -0.4063495695590973)
    switch.location = (-4270.65576171875, 303.36883544921875)
    boolean.location = (-4476.7646484375, 374.816162109375)
    extrude_mesh_003.location = (-6444.00732421875, 510.074951171875)
    scale_elements_004.location = (-6169.19921875, 497.8723449707031)
    scale_elements_005.location = (-6009.15966796875, 644.396240234375)
    extrude_mesh_004.location = (-5484.68310546875, 501.37164306640625)
    scale_elements_006.location = (-5214.1181640625, 436.015625)
    scale_elements_007.location = (-4983.9990234375, 466.0740661621094)
    delete_geometry_003.location = (-4724.50830078125, 367.4457092285156)
    vector_math.location = (-10447.65625, 678.4166870117188)
    position.location = (-10629.5048828125, 939.4542846679688)
    boolean_math.location = (-9958.5869140625, 840.685546875)
    compare_003.location = (-10230.08984375, 1018.79296875)
    separate_xyz.location = (-10439.5810546875, 1004.0413208007812)
    vector_math_001.location = (-6006.14794921875, 237.17684936523438)
    extrude_mesh_005.location = (-12636.7197265625, 320.2312316894531)
    normal_001.location = (-13487.8056640625, 644.9012451171875)
    compare_004.location = (-13101.8759765625, 744.260009765625)
    vector_math_002.location = (-13289.4580078125, 686.2073974609375)
    position_002.location = (-12632.9794921875, 727.2635498046875)
    compare_005.location = (-12233.5634765625, 806.6022338867188)
    separate_xyz_001.location = (-12443.0546875, 791.8505859375)
    boolean_math_001.location = (-11974.8544921875, 552.5919799804688)
    compare_006.location = (-12286.9931640625, 587.049072265625)
    math_001.location = (-12918.2685546875, -26.172758102416992)
    clamp.location = (-13128.6044921875, 453.8985290527344)
    math_002.location = (-13357.0244140625, 321.8339538574219)
    scale_elements_008.location = (-9516.888671875, 586.9972534179688)
    boolean_math_002.location = (-9909.751953125, 547.9618530273438)
    compare_007.location = (-10274.3857421875, 512.5938110351562)
    merge_by_distance_001.location = (-6699.626953125, 268.5569763183594)
    math_003.location = (-11479.6962890625, -89.35203552246094)
    math_004.location = (-11239.6376953125, -80.09564971923828)
    compare.location = (-1576.5694580078125, -355.9333190917969)
    position_001.location = (-2103.3798828125, -362.8302001953125)
    separate_xyz_002.location = (-1820.84375, -355.9465026855469)
    math_005.location = (-2437.0849609375, -624.8721923828125)
    set_position.location = (-1062.6903076171875, -546.6168823242188)
    wave_texture.location = (-2288.22265625, -985.907958984375)
    normal_002.location = (-1657.2696533203125, -639.6073608398438)
    vector_math_003.location = (-1304.065673828125, -667.641357421875)
    math_006.location = (-1478.8914794921875, -793.545654296875)
    math_007.location = (-2057.295166015625, -1089.9520263671875)
    math_008.location = (-1652.4825439453125, -834.0706176757812)
    math_009.location = (-2140.944580078125, -628.4778442382812)
    math_010.location = (-1896.052734375, -794.8171997070312)
    math_011.location = (-1860.588134765625, -636.7539672851562)
    attribute_statistic.location = (-2729.67724609375, -861.9201049804688)
    position_003.location = (-2937.98828125, -1039.662109375)
    separate_xyz_003.location = (-2451.119873046875, -851.5394897460938)
    math_012.location = (-2237.982177734375, -791.8509521484375)
    wave_texture_001.location = (-2299.693115234375, -1291.8978271484375)
    math_013.location = (-1893.315185546875, -1031.879638671875)
    noise_texture.location = (-1308.6295166015625, -893.1959838867188)
    set_position_001.location = (-651.9876708984375, -597.2646484375)
    vector_math_004.location = (-1110.7645263671875, -754.8290405273438)
    vector_math_005.location = (-903.6542358398438, -719.9539794921875)
    set_material.location = (52.707069396972656, 17.56627082824707)
    separate_xyz_004.location = (-14211.3076171875, 60.62366485595703)
    separate_xyz_005.location = (-8364.9521484375, 1002.6939086914062)
    math_014.location = (-13825.619140625, 278.233154296875)
    math_015.location = (-13616.798828125, 217.35562133789062)
    combine_xyz.location = (-13783.7119140625, -106.47314453125)
    math_016.location = (-14030.23046875, -87.46503448486328)
    separate_xyz_006.location = (-8271.11328125, 836.9984741210938)
    math_017.location = (-7967.5771484375, 968.6863403320312)
    math_018.location = (-7976.83154296875, 770.1826171875)
    math_019.location = (-13410.05859375, 559.7562255859375)
    math_020.location = (-5835.45751953125, 884.9111938476562)
    math_021.location = (-5837.89697265625, 716.1056518554688)
    attribute_statistic_001.location = (-7005.9384765625, 1573.5625)
    position_004.location = (-7280.3046875, 1447.0364990234375)
    separate_xyz_007.location = (-6821.49609375, 1375.314453125)
    math_022.location = (-6180.728515625, 1159.15478515625)
    math_023.location = (-6367.2431640625, 934.0392456054688)
    math_024.location = (-6583.13330078125, 1047.364990234375)
    math_025.location = (-6347.892578125, 1295.829833984375)
    math_026.location = (-6562.9228515625, 1215.219970703125)
    group_input.location = (-14676.5458984375, 450.3015441894531)
    separate_xyz_008.location = (-14470.4716796875, 79.37898254394531)
    float_to_integer.location = (-14209.4658203125, 17.14548683166504)
    float_to_integer_001.location = (-14240.865234375, -105.53564453125)
    viewer.location = (-2812.421142578125, 286.1052551269531)

    # Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    grid.width, grid.height = 140.0, 100.0
    extrude_mesh.width, extrude_mesh.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    transform_geometry.width, transform_geometry.height = 140.0, 100.0
    join_geometry.width, join_geometry.height = 140.0, 100.0
    merge_by_distance.width, merge_by_distance.height = 140.0, 100.0
    transform_geometry_001.width, transform_geometry_001.height = 140.0, 100.0
    reroute.width, reroute.height = 10.5, 100.0
    set_shade_smooth.width, set_shade_smooth.height = 140.0, 100.0
    normal.width, normal.height = 140.0, 100.0
    extrude_mesh_001.width, extrude_mesh_001.height = 140.0, 100.0
    compare_001.width, compare_001.height = 140.0, 100.0
    vector.width, vector.height = 140.0, 100.0
    flip_faces.width, flip_faces.height = 140.0, 100.0
    scale_elements.width, scale_elements.height = 140.0, 100.0
    compare_002.width, compare_002.height = 140.0, 100.0
    vector_001.width, vector_001.height = 140.0, 100.0
    scale_elements_001.width, scale_elements_001.height = 140.0, 100.0
    extrude_mesh_002.width, extrude_mesh_002.height = 140.0, 100.0
    scale_elements_002.width, scale_elements_002.height = 140.0, 100.0
    scale_elements_003.width, scale_elements_003.height = 140.0, 100.0
    delete_geometry_001.width, delete_geometry_001.height = 140.0, 100.0
    subdivision_surface.width, subdivision_surface.height = 150.0, 100.0
    delete_geometry_002.width, delete_geometry_002.height = 140.0, 100.0
    switch.width, switch.height = 140.0, 100.0
    boolean.width, boolean.height = 140.0, 100.0
    extrude_mesh_003.width, extrude_mesh_003.height = 140.0, 100.0
    scale_elements_004.width, scale_elements_004.height = 140.0, 100.0
    scale_elements_005.width, scale_elements_005.height = 140.0, 100.0
    extrude_mesh_004.width, extrude_mesh_004.height = 140.0, 100.0
    scale_elements_006.width, scale_elements_006.height = 140.0, 100.0
    scale_elements_007.width, scale_elements_007.height = 140.0, 100.0
    delete_geometry_003.width, delete_geometry_003.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    position.width, position.height = 140.0, 100.0
    boolean_math.width, boolean_math.height = 140.0, 100.0
    compare_003.width, compare_003.height = 140.0, 100.0
    separate_xyz.width, separate_xyz.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    extrude_mesh_005.width, extrude_mesh_005.height = 140.0, 100.0
    normal_001.width, normal_001.height = 140.0, 100.0
    compare_004.width, compare_004.height = 140.0, 100.0
    vector_math_002.width, vector_math_002.height = 140.0, 100.0
    position_002.width, position_002.height = 140.0, 100.0
    compare_005.width, compare_005.height = 140.0, 100.0
    separate_xyz_001.width, separate_xyz_001.height = 140.0, 100.0
    boolean_math_001.width, boolean_math_001.height = 140.0, 100.0
    compare_006.width, compare_006.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    clamp.width, clamp.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    scale_elements_008.width, scale_elements_008.height = 140.0, 100.0
    boolean_math_002.width, boolean_math_002.height = 140.0, 100.0
    compare_007.width, compare_007.height = 140.0, 100.0
    merge_by_distance_001.width, merge_by_distance_001.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    compare.width, compare.height = 140.0, 100.0
    position_001.width, position_001.height = 140.0, 100.0
    separate_xyz_002.width, separate_xyz_002.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    set_position.width, set_position.height = 140.0, 100.0
    wave_texture.width, wave_texture.height = 150.0, 100.0
    normal_002.width, normal_002.height = 140.0, 100.0
    vector_math_003.width, vector_math_003.height = 140.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    math_008.width, math_008.height = 140.0, 100.0
    math_009.width, math_009.height = 140.0, 100.0
    math_010.width, math_010.height = 140.0, 100.0
    math_011.width, math_011.height = 140.0, 100.0
    attribute_statistic.width, attribute_statistic.height = 140.0, 100.0
    position_003.width, position_003.height = 140.0, 100.0
    separate_xyz_003.width, separate_xyz_003.height = 140.0, 100.0
    math_012.width, math_012.height = 140.0, 100.0
    wave_texture_001.width, wave_texture_001.height = 150.0, 100.0
    math_013.width, math_013.height = 140.0, 100.0
    noise_texture.width, noise_texture.height = 140.0, 100.0
    set_position_001.width, set_position_001.height = 140.0, 100.0
    vector_math_004.width, vector_math_004.height = 140.0, 100.0
    vector_math_005.width, vector_math_005.height = 140.0, 100.0
    set_material.width, set_material.height = 140.0, 100.0
    separate_xyz_004.width, separate_xyz_004.height = 140.0, 100.0
    separate_xyz_005.width, separate_xyz_005.height = 140.0, 100.0
    math_014.width, math_014.height = 140.0, 100.0
    math_015.width, math_015.height = 140.0, 100.0
    combine_xyz.width, combine_xyz.height = 140.0, 100.0
    math_016.width, math_016.height = 140.0, 100.0
    separate_xyz_006.width, separate_xyz_006.height = 140.0, 100.0
    math_017.width, math_017.height = 140.0, 100.0
    math_018.width, math_018.height = 140.0, 100.0
    math_019.width, math_019.height = 140.0, 100.0
    math_020.width, math_020.height = 140.0, 100.0
    math_021.width, math_021.height = 140.0, 100.0
    attribute_statistic_001.width, attribute_statistic_001.height = 140.0, 100.0
    position_004.width, position_004.height = 140.0, 100.0
    separate_xyz_007.width, separate_xyz_007.height = 140.0, 100.0
    math_022.width, math_022.height = 140.0, 100.0
    math_023.width, math_023.height = 140.0, 100.0
    math_024.width, math_024.height = 140.0, 100.0
    math_025.width, math_025.height = 140.0, 100.0
    math_026.width, math_026.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    separate_xyz_008.width, separate_xyz_008.height = 140.0, 100.0
    float_to_integer.width, float_to_integer.height = 140.0, 100.0
    float_to_integer_001.width, float_to_integer_001.height = 140.0, 100.0
    viewer.width, viewer.height = 140.0, 100.0

    # Initialize bag links

    # grid.Mesh -> transform_geometry.Geometry
    bag.links.new(grid.outputs[0], transform_geometry.inputs[0])
    # join_geometry.Geometry -> merge_by_distance.Geometry
    bag.links.new(join_geometry.outputs[0], merge_by_distance.inputs[0])
    # set_material.Geometry -> group_output.Geometry
    bag.links.new(set_material.outputs[0], group_output.inputs[0])
    # reroute.Output -> join_geometry.Geometry
    bag.links.new(reroute.outputs[0], join_geometry.inputs[0])
    # reroute.Output -> transform_geometry_001.Geometry
    bag.links.new(reroute.outputs[0], transform_geometry_001.inputs[0])
    # extrude_mesh.Mesh -> extrude_mesh_001.Mesh
    bag.links.new(extrude_mesh.outputs[0], extrude_mesh_001.inputs[0])
    # compare_001.Result -> extrude_mesh_001.Selection
    bag.links.new(compare_001.outputs[0], extrude_mesh_001.inputs[1])
    # normal.Normal -> compare_001.A
    bag.links.new(normal.outputs[0], compare_001.inputs[4])
    # vector.Vector -> extrude_mesh_001.Offset
    bag.links.new(vector.outputs[0], extrude_mesh_001.inputs[2])
    # transform_geometry_001.Geometry -> flip_faces.Mesh
    bag.links.new(transform_geometry_001.outputs[0], flip_faces.inputs[0])
    # extrude_mesh_001.Top -> scale_elements.Selection
    bag.links.new(extrude_mesh_001.outputs[1], scale_elements.inputs[1])
    # vector_math.Vector -> compare_002.A
    bag.links.new(vector_math.outputs[0], compare_002.inputs[4])
    # vector_001.Vector -> scale_elements.Center
    bag.links.new(vector_001.outputs[0], scale_elements.inputs[3])
    # extrude_mesh_001.Top -> scale_elements_001.Selection
    bag.links.new(extrude_mesh_001.outputs[1], scale_elements_001.inputs[1])
    # vector_001.Vector -> scale_elements_001.Center
    bag.links.new(vector_001.outputs[0], scale_elements_001.inputs[3])
    # scale_elements.Geometry -> scale_elements_001.Geometry
    bag.links.new(scale_elements.outputs[0], scale_elements_001.inputs[0])
    # compare_001.Result -> extrude_mesh_002.Selection
    bag.links.new(compare_001.outputs[0], extrude_mesh_002.inputs[1])
    # vector.Vector -> extrude_mesh_002.Offset
    bag.links.new(vector.outputs[0], extrude_mesh_002.inputs[2])
    # vector_001.Vector -> scale_elements_002.Center
    bag.links.new(vector_001.outputs[0], scale_elements_002.inputs[3])
    # vector_001.Vector -> scale_elements_003.Center
    bag.links.new(vector_001.outputs[0], scale_elements_003.inputs[3])
    # scale_elements_002.Geometry -> scale_elements_003.Geometry
    bag.links.new(scale_elements_002.outputs[0], scale_elements_003.inputs[0])
    # extrude_mesh_002.Mesh -> scale_elements_002.Geometry
    bag.links.new(extrude_mesh_002.outputs[0], scale_elements_002.inputs[0])
    # extrude_mesh_002.Top -> scale_elements_002.Selection
    bag.links.new(extrude_mesh_002.outputs[1], scale_elements_002.inputs[1])
    # extrude_mesh_002.Top -> scale_elements_003.Selection
    bag.links.new(extrude_mesh_002.outputs[1], scale_elements_003.inputs[1])
    # boolean_math.Boolean -> delete_geometry_001.Selection
    bag.links.new(boolean_math.outputs[0], delete_geometry_001.inputs[1])
    # scale_elements_003.Geometry -> delete_geometry_001.Geometry
    bag.links.new(scale_elements_003.outputs[0], delete_geometry_001.inputs[0])
    # merge_by_distance.Geometry -> subdivision_surface.Mesh
    bag.links.new(merge_by_distance.outputs[0], subdivision_surface.inputs[0])
    # extrude_mesh_002.Top -> delete_geometry_002.Selection
    bag.links.new(extrude_mesh_002.outputs[1], delete_geometry_002.inputs[1])
    # switch.Output -> reroute.Input
    bag.links.new(switch.outputs[0], reroute.inputs[0])
    # delete_geometry_002.Geometry -> switch.True
    bag.links.new(delete_geometry_002.outputs[0], switch.inputs[2])
    # boolean.Boolean -> switch.Switch
    bag.links.new(boolean.outputs[0], switch.inputs[0])
    # merge_by_distance_001.Geometry -> extrude_mesh_003.Mesh
    bag.links.new(merge_by_distance_001.outputs[0], extrude_mesh_003.inputs[0])
    # extrude_mesh_002.Top -> extrude_mesh_003.Selection
    bag.links.new(extrude_mesh_002.outputs[1], extrude_mesh_003.inputs[1])
    # scale_elements_004.Geometry -> scale_elements_005.Geometry
    bag.links.new(scale_elements_004.outputs[0], scale_elements_005.inputs[0])
    # extrude_mesh_003.Mesh -> scale_elements_004.Geometry
    bag.links.new(extrude_mesh_003.outputs[0], scale_elements_004.inputs[0])
    # vector_001.Vector -> scale_elements_004.Center
    bag.links.new(vector_001.outputs[0], scale_elements_004.inputs[3])
    # vector_001.Vector -> scale_elements_005.Center
    bag.links.new(vector_001.outputs[0], scale_elements_005.inputs[3])
    # extrude_mesh_003.Top -> scale_elements_004.Selection
    bag.links.new(extrude_mesh_003.outputs[1], scale_elements_004.inputs[1])
    # extrude_mesh_003.Top -> scale_elements_005.Selection
    bag.links.new(extrude_mesh_003.outputs[1], scale_elements_005.inputs[1])
    # scale_elements_006.Geometry -> scale_elements_007.Geometry
    bag.links.new(scale_elements_006.outputs[0], scale_elements_007.inputs[0])
    # extrude_mesh_004.Mesh -> scale_elements_006.Geometry
    bag.links.new(extrude_mesh_004.outputs[0], scale_elements_006.inputs[0])
    # vector_001.Vector -> scale_elements_006.Center
    bag.links.new(vector_001.outputs[0], scale_elements_006.inputs[3])
    # vector_001.Vector -> scale_elements_007.Center
    bag.links.new(vector_001.outputs[0], scale_elements_007.inputs[3])
    # extrude_mesh_004.Top -> scale_elements_006.Selection
    bag.links.new(extrude_mesh_004.outputs[1], scale_elements_006.inputs[1])
    # extrude_mesh_004.Top -> scale_elements_007.Selection
    bag.links.new(extrude_mesh_004.outputs[1], scale_elements_007.inputs[1])
    # scale_elements_005.Geometry -> extrude_mesh_004.Mesh
    bag.links.new(scale_elements_005.outputs[0], extrude_mesh_004.inputs[0])
    # extrude_mesh_003.Top -> extrude_mesh_004.Selection
    bag.links.new(extrude_mesh_003.outputs[1], extrude_mesh_004.inputs[1])
    # boolean_math.Boolean -> delete_geometry_003.Selection
    bag.links.new(boolean_math.outputs[0], delete_geometry_003.inputs[1])
    # scale_elements_007.Geometry -> delete_geometry_003.Geometry
    bag.links.new(scale_elements_007.outputs[0], delete_geometry_003.inputs[0])
    # delete_geometry_003.Geometry -> switch.False
    bag.links.new(delete_geometry_003.outputs[0], switch.inputs[1])
    # normal.Normal -> vector_math.Vector
    bag.links.new(normal.outputs[0], vector_math.inputs[0])
    # separate_xyz.Y -> compare_003.A
    bag.links.new(separate_xyz.outputs[1], compare_003.inputs[0])
    # position.Position -> separate_xyz.Vector
    bag.links.new(position.outputs[0], separate_xyz.inputs[0])
    # compare_003.Result -> boolean_math.Boolean
    bag.links.new(compare_003.outputs[0], boolean_math.inputs[0])
    # compare_002.Result -> boolean_math.Boolean
    bag.links.new(compare_002.outputs[0], boolean_math.inputs[1])
    # vector.Vector -> extrude_mesh_003.Offset
    bag.links.new(vector.outputs[0], extrude_mesh_003.inputs[2])
    # vector_math_001.Vector -> extrude_mesh_004.Offset
    bag.links.new(vector_math_001.outputs[0], extrude_mesh_004.inputs[2])
    # vector.Vector -> vector_math_001.Vector
    bag.links.new(vector.outputs[0], vector_math_001.inputs[0])
    # transform_geometry.Geometry -> extrude_mesh_005.Mesh
    bag.links.new(transform_geometry.outputs[0], extrude_mesh_005.inputs[0])
    # clamp.Result -> extrude_mesh_005.Offset Scale
    bag.links.new(clamp.outputs[0], extrude_mesh_005.inputs[3])
    # vector_math_002.Vector -> compare_004.A
    bag.links.new(vector_math_002.outputs[0], compare_004.inputs[4])
    # compare_004.Result -> extrude_mesh_005.Selection
    bag.links.new(compare_004.outputs[0], extrude_mesh_005.inputs[1])
    # compare_004.Result -> extrude_mesh.Selection
    bag.links.new(compare_004.outputs[0], extrude_mesh.inputs[1])
    # normal_001.Normal -> vector_math_002.Vector
    bag.links.new(normal_001.outputs[0], vector_math_002.inputs[0])
    # extrude_mesh_005.Mesh -> extrude_mesh.Mesh
    bag.links.new(extrude_mesh_005.outputs[0], extrude_mesh.inputs[0])
    # position_002.Position -> separate_xyz_001.Vector
    bag.links.new(position_002.outputs[0], separate_xyz_001.inputs[0])
    # separate_xyz_001.Y -> compare_005.A
    bag.links.new(separate_xyz_001.outputs[1], compare_005.inputs[0])
    # clamp.Result -> compare_005.B
    bag.links.new(clamp.outputs[0], compare_005.inputs[1])
    # compare_005.Result -> boolean_math_001.Boolean
    bag.links.new(compare_005.outputs[0], boolean_math_001.inputs[0])
    # normal_001.Normal -> compare_006.A
    bag.links.new(normal_001.outputs[0], compare_006.inputs[4])
    # compare_006.Result -> boolean_math_001.Boolean
    bag.links.new(compare_006.outputs[0], boolean_math_001.inputs[1])
    # separate_xyz_004.Y -> grid.Size Y
    bag.links.new(separate_xyz_004.outputs[1], grid.inputs[1])
    # separate_xyz_004.Z -> math.Value
    bag.links.new(separate_xyz_004.outputs[2], math.inputs[0])
    # math_001.Value -> extrude_mesh.Offset Scale
    bag.links.new(math_001.outputs[0], extrude_mesh.inputs[3])
    # clamp.Result -> math_001.Value
    bag.links.new(clamp.outputs[0], math_001.inputs[1])
    # math.Value -> math_001.Value
    bag.links.new(math.outputs[0], math_001.inputs[0])
    # separate_xyz_004.Z -> math_002.Value
    bag.links.new(separate_xyz_004.outputs[2], math_002.inputs[0])
    # math_002.Value -> clamp.Max
    bag.links.new(math_002.outputs[0], clamp.inputs[2])
    # vector_001.Vector -> scale_elements_008.Center
    bag.links.new(vector_001.outputs[0], scale_elements_008.inputs[3])
    # extrude_mesh_001.Mesh -> scale_elements_008.Geometry
    bag.links.new(extrude_mesh_001.outputs[0], scale_elements_008.inputs[0])
    # scale_elements_008.Geometry -> scale_elements.Geometry
    bag.links.new(scale_elements_008.outputs[0], scale_elements.inputs[0])
    # compare_001.Result -> boolean_math_002.Boolean
    bag.links.new(compare_001.outputs[0], boolean_math_002.inputs[0])
    # separate_xyz.Y -> compare_007.A
    bag.links.new(separate_xyz.outputs[1], compare_007.inputs[0])
    # compare_007.Result -> boolean_math_002.Boolean
    bag.links.new(compare_007.outputs[0], boolean_math_002.inputs[1])
    # clamp.Result -> compare_007.B
    bag.links.new(clamp.outputs[0], compare_007.inputs[1])
    # delete_geometry_001.Geometry -> merge_by_distance_001.Geometry
    bag.links.new(delete_geometry_001.outputs[0], merge_by_distance_001.inputs[0])
    # merge_by_distance_001.Geometry -> delete_geometry_002.Geometry
    bag.links.new(merge_by_distance_001.outputs[0], delete_geometry_002.inputs[0])
    # boolean_math_002.Boolean -> scale_elements_008.Selection
    bag.links.new(boolean_math_002.outputs[0], scale_elements_008.inputs[1])
    # math_001.Value -> math_003.Value
    bag.links.new(math_001.outputs[0], math_003.inputs[0])
    # clamp.Result -> math_003.Value
    bag.links.new(clamp.outputs[0], math_003.inputs[1])
    # math_004.Value -> scale_elements_008.Scale
    bag.links.new(math_004.outputs[0], scale_elements_008.inputs[2])
    # math_003.Value -> math_004.Value
    bag.links.new(math_003.outputs[0], math_004.inputs[0])
    # position_001.Position -> separate_xyz_002.Vector
    bag.links.new(position_001.outputs[0], separate_xyz_002.inputs[0])
    # separate_xyz_002.Z -> compare.A
    bag.links.new(separate_xyz_002.outputs[2], compare.inputs[0])
    # separate_xyz_004.X -> math_005.Value
    bag.links.new(separate_xyz_004.outputs[0], math_005.inputs[0])
    # math_005.Value -> compare.B
    bag.links.new(math_005.outputs[0], compare.inputs[1])
    # subdivision_surface.Mesh -> set_position.Geometry
    bag.links.new(subdivision_surface.outputs[0], set_position.inputs[0])
    # compare.Result -> set_position.Selection
    bag.links.new(compare.outputs[0], set_position.inputs[1])
    # vector_math_003.Vector -> set_position.Offset
    bag.links.new(vector_math_003.outputs[0], set_position.inputs[3])
    # normal_002.Normal -> vector_math_003.Vector
    bag.links.new(normal_002.outputs[0], vector_math_003.inputs[0])
    # math_006.Value -> vector_math_003.Scale
    bag.links.new(math_006.outputs[0], vector_math_003.inputs[3])
    # wave_texture.Fac -> math_007.Value
    bag.links.new(wave_texture.outputs[1], math_007.inputs[0])
    # math_008.Value -> math_006.Value
    bag.links.new(math_008.outputs[0], math_006.inputs[0])
    # separate_xyz_002.Z -> math_009.Value
    bag.links.new(separate_xyz_002.outputs[2], math_009.inputs[0])
    # math_005.Value -> math_009.Value
    bag.links.new(math_005.outputs[0], math_009.inputs[1])
    # math_009.Value -> math_010.Value
    bag.links.new(math_009.outputs[0], math_010.inputs[0])
    # math_010.Value -> math_008.Value
    bag.links.new(math_010.outputs[0], math_008.inputs[1])
    # subdivision_surface.Mesh -> attribute_statistic.Geometry
    bag.links.new(subdivision_surface.outputs[0], attribute_statistic.inputs[0])
    # position_003.Position -> attribute_statistic.Attribute
    bag.links.new(position_003.outputs[0], attribute_statistic.inputs[2])
    # attribute_statistic.Max -> separate_xyz_003.Vector
    bag.links.new(attribute_statistic.outputs[4], separate_xyz_003.inputs[0])
    # separate_xyz_003.Z -> math_012.Value
    bag.links.new(separate_xyz_003.outputs[2], math_012.inputs[0])
    # math_005.Value -> math_012.Value
    bag.links.new(math_005.outputs[0], math_012.inputs[1])
    # math_012.Value -> math_010.Value
    bag.links.new(math_012.outputs[0], math_010.inputs[1])
    # wave_texture_001.Fac -> math_007.Value
    bag.links.new(wave_texture_001.outputs[1], math_007.inputs[1])
    # math_007.Value -> math_013.Value
    bag.links.new(math_007.outputs[0], math_013.inputs[0])
    # math_013.Value -> math_008.Value
    bag.links.new(math_013.outputs[0], math_008.inputs[0])
    # set_position.Geometry -> set_position_001.Geometry
    bag.links.new(set_position.outputs[0], set_position_001.inputs[0])
    # set_position_001.Geometry -> set_shade_smooth.Geometry
    bag.links.new(set_position_001.outputs[0], set_shade_smooth.inputs[0])
    # math_006.Value -> vector_math_004.Scale
    bag.links.new(math_006.outputs[0], vector_math_004.inputs[3])
    # vector_math_004.Vector -> vector_math_005.Vector
    bag.links.new(vector_math_004.outputs[0], vector_math_005.inputs[0])
    # vector_math_005.Vector -> set_position_001.Offset
    bag.links.new(vector_math_005.outputs[0], set_position_001.inputs[3])
    # set_shade_smooth.Geometry -> set_material.Geometry
    bag.links.new(set_shade_smooth.outputs[0], set_material.inputs[0])
    # separate_xyz_005.X -> scale_elements.Scale
    bag.links.new(separate_xyz_005.outputs[0], scale_elements.inputs[2])
    # separate_xyz_005.Y -> scale_elements_001.Scale
    bag.links.new(separate_xyz_005.outputs[1], scale_elements_001.inputs[2])
    # math_014.Value -> extrude_mesh_001.Offset Scale
    bag.links.new(math_014.outputs[0], extrude_mesh_001.inputs[3])
    # separate_xyz_004.Z -> math_014.Value
    bag.links.new(separate_xyz_004.outputs[2], math_014.inputs[0])
    # separate_xyz_004.X -> math_015.Value
    bag.links.new(separate_xyz_004.outputs[0], math_015.inputs[0])
    # math_015.Value -> grid.Size X
    bag.links.new(math_015.outputs[0], grid.inputs[0])
    # math_014.Value -> math_015.Value
    bag.links.new(math_014.outputs[0], math_015.inputs[1])
    # math_016.Value -> combine_xyz.Z
    bag.links.new(math_016.outputs[0], combine_xyz.inputs[2])
    # combine_xyz.Vector -> transform_geometry.Translation
    bag.links.new(combine_xyz.outputs[0], transform_geometry.inputs[1])
    # math_014.Value -> math_016.Value
    bag.links.new(math_014.outputs[0], math_016.inputs[0])
    # separate_xyz_005.Z -> math_014.Value
    bag.links.new(separate_xyz_005.outputs[2], math_014.inputs[1])
    # math_019.Value -> extrude_mesh_002.Offset Scale
    bag.links.new(math_019.outputs[0], extrude_mesh_002.inputs[3])
    # math_017.Value -> scale_elements_002.Scale
    bag.links.new(math_017.outputs[0], scale_elements_002.inputs[2])
    # math_018.Value -> scale_elements_003.Scale
    bag.links.new(math_018.outputs[0], scale_elements_003.inputs[2])
    # separate_xyz_006.Y -> math_018.Value
    bag.links.new(separate_xyz_006.outputs[1], math_018.inputs[0])
    # separate_xyz_006.X -> math_017.Value
    bag.links.new(separate_xyz_006.outputs[0], math_017.inputs[0])
    # separate_xyz_005.Y -> math_018.Value
    bag.links.new(separate_xyz_005.outputs[1], math_018.inputs[1])
    # separate_xyz_006.Z -> math_019.Value
    bag.links.new(separate_xyz_006.outputs[2], math_019.inputs[0])
    # math_019.Value -> extrude_mesh_004.Offset Scale
    bag.links.new(math_019.outputs[0], extrude_mesh_004.inputs[3])
    # separate_xyz_005.X -> math_017.Value
    bag.links.new(separate_xyz_005.outputs[0], math_017.inputs[1])
    # math_017.Value -> math_020.Value
    bag.links.new(math_017.outputs[0], math_020.inputs[1])
    # math_020.Value -> scale_elements_006.Scale
    bag.links.new(math_020.outputs[0], scale_elements_006.inputs[2])
    # math_018.Value -> math_021.Value
    bag.links.new(math_018.outputs[0], math_021.inputs[1])
    # math_021.Value -> scale_elements_007.Scale
    bag.links.new(math_021.outputs[0], scale_elements_007.inputs[2])
    # math_022.Value -> scale_elements_005.Scale
    bag.links.new(math_022.outputs[0], scale_elements_005.inputs[2])
    # extrude_mesh_003.Mesh -> attribute_statistic_001.Geometry
    bag.links.new(extrude_mesh_003.outputs[0], attribute_statistic_001.inputs[0])
    # extrude_mesh_003.Top -> attribute_statistic_001.Selection
    bag.links.new(extrude_mesh_003.outputs[1], attribute_statistic_001.inputs[1])
    # position_004.Position -> attribute_statistic_001.Attribute
    bag.links.new(position_004.outputs[0], attribute_statistic_001.inputs[2])
    # attribute_statistic_001.Range -> separate_xyz_007.Vector
    bag.links.new(attribute_statistic_001.outputs[5], separate_xyz_007.inputs[0])
    # math_024.Value -> math_023.Value
    bag.links.new(math_024.outputs[0], math_023.inputs[0])
    # math_023.Value -> scale_elements_004.Scale
    bag.links.new(math_023.outputs[0], scale_elements_004.inputs[2])
    # math_025.Value -> math_022.Value
    bag.links.new(math_025.outputs[0], math_022.inputs[0])
    # separate_xyz_007.Y -> math_025.Value
    bag.links.new(separate_xyz_007.outputs[1], math_025.inputs[0])
    # math_026.Value -> math_025.Value
    bag.links.new(math_026.outputs[0], math_025.inputs[1])
    # separate_xyz_007.Y -> math_022.Value
    bag.links.new(separate_xyz_007.outputs[1], math_022.inputs[1])
    # separate_xyz_007.X -> math_024.Value
    bag.links.new(separate_xyz_007.outputs[0], math_024.inputs[0])
    # separate_xyz_007.X -> math_023.Value
    bag.links.new(separate_xyz_007.outputs[0], math_023.inputs[1])
    # separate_xyz_004.Z -> math_019.Value
    bag.links.new(separate_xyz_004.outputs[2], math_019.inputs[1])
    # group_input.scale -> separate_xyz_004.Vector
    bag.links.new(group_input.outputs[0], separate_xyz_004.inputs[0])
    # group_input.seam_thickness -> clamp.Value
    bag.links.new(group_input.outputs[3], clamp.inputs[0])
    # group_input.bag_taper -> separate_xyz_005.Vector
    bag.links.new(group_input.outputs[4], separate_xyz_005.inputs[0])
    # group_input.neck_taper -> separate_xyz_006.Vector
    bag.links.new(group_input.outputs[5], separate_xyz_006.inputs[0])
    # group_input.neck_thickness -> math_024.Value
    bag.links.new(group_input.outputs[6], math_024.inputs[1])
    # group_input.neck_thickness -> math_026.Value
    bag.links.new(group_input.outputs[6], math_026.inputs[0])
    # group_input.detail -> subdivision_surface.Level
    bag.links.new(group_input.outputs[2], subdivision_surface.inputs[1])
    # group_input.edge_crease -> subdivision_surface.Edge Crease
    bag.links.new(group_input.outputs[7], subdivision_surface.inputs[2])
    # group_input.vertex_crease -> subdivision_surface.Vertex Crease
    bag.links.new(group_input.outputs[8], subdivision_surface.inputs[3])
    # normal_002.Normal -> vector_math_004.Vector
    bag.links.new(normal_002.outputs[0], vector_math_004.inputs[0])
    # scale_elements_001.Geometry -> extrude_mesh_002.Mesh
    bag.links.new(scale_elements_001.outputs[0], extrude_mesh_002.inputs[0])
    # noise_texture.Color -> vector_math_004.Vector
    bag.links.new(noise_texture.outputs[1], vector_math_004.inputs[1])
    # group_input.mat -> set_material.Material
    bag.links.new(group_input.outputs[9], set_material.inputs[2])
    # group_input.base_geometry -> separate_xyz_008.Vector
    bag.links.new(group_input.outputs[1], separate_xyz_008.inputs[0])
    # separate_xyz_008.X -> float_to_integer.Float
    bag.links.new(separate_xyz_008.outputs[0], float_to_integer.inputs[0])
    # separate_xyz_008.Y -> float_to_integer_001.Float
    bag.links.new(separate_xyz_008.outputs[1], float_to_integer_001.inputs[0])
    # float_to_integer.Integer -> grid.Vertices X
    bag.links.new(float_to_integer.outputs[0], grid.inputs[2])
    # float_to_integer_001.Integer -> grid.Vertices Y
    bag.links.new(float_to_integer_001.outputs[0], grid.inputs[3])
    # subdivision_surface.Mesh -> viewer.Geometry
    bag.links.new(subdivision_surface.outputs[0], viewer.inputs[0])
    # flip_faces.Mesh -> join_geometry.Geometry
    bag.links.new(flip_faces.outputs[0], join_geometry.inputs[0])

    return bag


bag = bag_node_group()

def random__normal__node_group():
    """Initialize random__normal_ node group"""
    random__normal_ = bpy.data.node_groups.new(type='GeometryNodeTree', name="Random (Normal)")

    random__normal_.color_tag = 'NONE'
    random__normal_.description = ""
    random__normal_.default_group_node_width = 140

    # random__normal_ interface

    # Socket Value
    value_socket = random__normal_.interface.new_socket(name="Value", in_out='OUTPUT', socket_type='NodeSocketFloat')
    value_socket.default_value = 0.0
    value_socket.min_value = -3.4028234663852886e+38
    value_socket.max_value = 3.4028234663852886e+38
    value_socket.subtype = 'NONE'
    value_socket.attribute_domain = 'POINT'
    value_socket.default_input = 'VALUE'
    value_socket.structure_type = 'AUTO'

    # Socket Non-Negative
    non_negative_socket = random__normal_.interface.new_socket(name="Non-Negative", in_out='INPUT', socket_type='NodeSocketBool')
    non_negative_socket.default_value = True
    non_negative_socket.attribute_domain = 'POINT'
    non_negative_socket.default_input = 'VALUE'
    non_negative_socket.structure_type = 'AUTO'

    # Socket Mean
    mean_socket = random__normal_.interface.new_socket(name="Mean", in_out='INPUT', socket_type='NodeSocketFloat')
    mean_socket.default_value = 0.0
    mean_socket.min_value = -3.4028234663852886e+38
    mean_socket.max_value = 3.4028234663852886e+38
    mean_socket.subtype = 'NONE'
    mean_socket.attribute_domain = 'POINT'
    mean_socket.default_input = 'VALUE'
    mean_socket.structure_type = 'AUTO'

    # Socket Std. Dev.
    std__dev__socket = random__normal_.interface.new_socket(name="Std. Dev.", in_out='INPUT', socket_type='NodeSocketFloat')
    std__dev__socket.default_value = 1.0
    std__dev__socket.min_value = 0.0
    std__dev__socket.max_value = 3.4028234663852886e+38
    std__dev__socket.subtype = 'NONE'
    std__dev__socket.attribute_domain = 'POINT'
    std__dev__socket.default_input = 'VALUE'
    std__dev__socket.structure_type = 'AUTO'

    # Socket Seed
    seed_socket = random__normal_.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt')
    seed_socket.default_value = 0
    seed_socket.min_value = 0
    seed_socket.max_value = 2147483647
    seed_socket.subtype = 'NONE'
    seed_socket.attribute_domain = 'POINT'
    seed_socket.hide_value = True
    seed_socket.default_input = 'VALUE'
    seed_socket.structure_type = 'AUTO'

    # Socket Offset
    offset_socket = random__normal_.interface.new_socket(name="Offset", in_out='INPUT', socket_type='NodeSocketInt')
    offset_socket.default_value = 0
    offset_socket.min_value = 0
    offset_socket.max_value = 2147483647
    offset_socket.subtype = 'NONE'
    offset_socket.attribute_domain = 'POINT'
    offset_socket.default_input = 'VALUE'
    offset_socket.structure_type = 'AUTO'

    # Initialize random__normal_ nodes

    # Node Frame
    frame = random__normal_.nodes.new("NodeFrame")
    frame.label = "2 * pi * U_2"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    # Node Frame.003
    frame_003 = random__normal_.nodes.new("NodeFrame")
    frame_003.label = "X_1"
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    # Node Frame.001
    frame_001 = random__normal_.nodes.new("NodeFrame")
    frame_001.label = "sqrt(-2 * ln(U_1))"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Math.002
    math_002_1 = random__normal_.nodes.new("ShaderNodeMath")
    math_002_1.name = "Math.002"
    math_002_1.operation = 'MULTIPLY'
    math_002_1.use_clamp = False
    # Value_001
    math_002_1.inputs[1].default_value = 6.2831854820251465

    # Node Random Value.001
    random_value_001 = random__normal_.nodes.new("FunctionNodeRandomValue")
    random_value_001.label = "U_2"
    random_value_001.name = "Random Value.001"
    random_value_001.data_type = 'FLOAT'
    # Min_001
    random_value_001.inputs[2].default_value = 0.0
    # Max_001
    random_value_001.inputs[3].default_value = 1.0

    # Node Math.010
    math_010_1 = random__normal_.nodes.new("ShaderNodeMath")
    math_010_1.name = "Math.010"
    math_010_1.operation = 'ADD'
    math_010_1.use_clamp = False
    math_010_1.inputs[1].hide = True
    math_010_1.inputs[2].hide = True
    # Value_001
    math_010_1.inputs[1].default_value = 1.0

    # Node Math.005
    math_005_1 = random__normal_.nodes.new("ShaderNodeMath")
    math_005_1.name = "Math.005"
    math_005_1.operation = 'MULTIPLY'
    math_005_1.use_clamp = False

    # Node Math.004
    math_004_1 = random__normal_.nodes.new("ShaderNodeMath")
    math_004_1.name = "Math.004"
    math_004_1.operation = 'COSINE'
    math_004_1.use_clamp = False

    # Node Math.008
    math_008_1 = random__normal_.nodes.new("ShaderNodeMath")
    math_008_1.name = "Math.008"
    math_008_1.operation = 'MULTIPLY'
    math_008_1.use_clamp = False

    # Node Math.007
    math_007_1 = random__normal_.nodes.new("ShaderNodeMath")
    math_007_1.name = "Math.007"
    math_007_1.operation = 'ADD'
    math_007_1.use_clamp = False

    # Node Math
    math_1 = random__normal_.nodes.new("ShaderNodeMath")
    math_1.name = "Math"
    math_1.operation = 'LOGARITHM'
    math_1.use_clamp = False
    # Value_001
    math_1.inputs[1].default_value = 2.7182817459106445

    # Node Random Value.002
    random_value_002 = random__normal_.nodes.new("FunctionNodeRandomValue")
    random_value_002.label = "U_1"
    random_value_002.name = "Random Value.002"
    random_value_002.data_type = 'FLOAT'
    # Min_001
    random_value_002.inputs[2].default_value = 0.0
    # Max_001
    random_value_002.inputs[3].default_value = 1.0

    # Node Math.001
    math_001_1 = random__normal_.nodes.new("ShaderNodeMath")
    math_001_1.name = "Math.001"
    math_001_1.operation = 'MULTIPLY'
    math_001_1.use_clamp = False
    # Value_001
    math_001_1.inputs[1].default_value = -2.0

    # Node Math.003
    math_003_1 = random__normal_.nodes.new("ShaderNodeMath")
    math_003_1.name = "Math.003"
    math_003_1.operation = 'SQRT'
    math_003_1.use_clamp = False

    # Node Group Output
    group_output_1 = random__normal_.nodes.new("NodeGroupOutput")
    group_output_1.name = "Group Output"
    group_output_1.is_active_output = True

    # Node Group Input
    group_input_1 = random__normal_.nodes.new("NodeGroupInput")
    group_input_1.name = "Group Input"

    # Node Switch
    switch_1 = random__normal_.nodes.new("GeometryNodeSwitch")
    switch_1.name = "Switch"
    switch_1.input_type = 'FLOAT'

    # Node Math.006
    math_006_1 = random__normal_.nodes.new("ShaderNodeMath")
    math_006_1.name = "Math.006"
    math_006_1.operation = 'MAXIMUM'
    math_006_1.use_clamp = False
    # Value_001
    math_006_1.inputs[1].default_value = 0.0

    # Set parents
    math_002_1.parent = frame
    random_value_001.parent = frame
    math_010_1.parent = frame
    math_005_1.parent = frame_003
    math_004_1.parent = frame_003
    math_1.parent = frame_001
    random_value_002.parent = frame_001
    math_001_1.parent = frame_001
    math_003_1.parent = frame_001

    # Set locations
    frame.location = (-1061.0, -451.0)
    frame_003.location = (-211.0, -297.0)
    frame_001.location = (-1063.0, -200.0)
    math_002_1.location = (409.9722900390625, -45.65386962890625)
    random_value_001.location = (219.9722900390625, -36.15386962890625)
    math_010_1.location = (29.9722900390625, -153.2261962890625)
    math_005_1.location = (219.63975524902344, -36.41009521484375)
    math_004_1.location = (29.639755249023438, -126.29949951171875)
    math_008_1.location = (210.5360565185547, -105.03559112548828)
    math_007_1.location = (400.53607177734375, 29.03577995300293)
    math_1.location = (219.6490478515625, -45.28599548339844)
    random_value_002.location = (29.6490478515625, -35.78599548339844)
    math_001_1.location = (409.6490478515625, -45.28599548339844)
    math_003_1.location = (599.6490478515625, -56.2860107421875)
    group_output_1.location = (970.5360717773438, -8.96422004699707)
    group_input_1.location = (-1399.3758544921875, -91.58724975585938)
    switch_1.location = (780.5360717773438, 26.53577995300293)
    math_006_1.location = (590.5360717773438, -88.39610290527344)

    # Set dimensions
    frame.width, frame.height = 580.0, 309.0
    frame_003.width, frame_003.height = 390.0, 282.0
    frame_001.width, frame_001.height = 770.0, 233.0
    math_002_1.width, math_002_1.height = 140.0, 100.0
    random_value_001.width, random_value_001.height = 140.0, 100.0
    math_010_1.width, math_010_1.height = 140.0, 100.0
    math_005_1.width, math_005_1.height = 140.0, 100.0
    math_004_1.width, math_004_1.height = 140.0, 100.0
    math_008_1.width, math_008_1.height = 140.0, 100.0
    math_007_1.width, math_007_1.height = 140.0, 100.0
    math_1.width, math_1.height = 140.0, 100.0
    random_value_002.width, random_value_002.height = 140.0, 100.0
    math_001_1.width, math_001_1.height = 140.0, 100.0
    math_003_1.width, math_003_1.height = 140.0, 100.0
    group_output_1.width, group_output_1.height = 140.0, 100.0
    group_input_1.width, group_input_1.height = 140.0, 100.0
    switch_1.width, switch_1.height = 140.0, 100.0
    math_006_1.width, math_006_1.height = 140.0, 100.0

    # Initialize random__normal_ links

    # random_value_002.Value -> math_1.Value
    random__normal_.links.new(random_value_002.outputs[1], math_1.inputs[0])
    # math_1.Value -> math_001_1.Value
    random__normal_.links.new(math_1.outputs[0], math_001_1.inputs[0])
    # random_value_001.Value -> math_002_1.Value
    random__normal_.links.new(random_value_001.outputs[1], math_002_1.inputs[0])
    # math_002_1.Value -> math_004_1.Value
    random__normal_.links.new(math_002_1.outputs[0], math_004_1.inputs[0])
    # math_003_1.Value -> math_005_1.Value
    random__normal_.links.new(math_003_1.outputs[0], math_005_1.inputs[0])
    # group_input_1.Seed -> random_value_002.Seed
    random__normal_.links.new(group_input_1.outputs[3], random_value_002.inputs[8])
    # group_input_1.Seed -> math_010_1.Value
    random__normal_.links.new(group_input_1.outputs[3], math_010_1.inputs[0])
    # math_010_1.Value -> random_value_001.Seed
    random__normal_.links.new(math_010_1.outputs[0], random_value_001.inputs[8])
    # group_input_1.Std. Dev. -> math_008_1.Value
    random__normal_.links.new(group_input_1.outputs[2], math_008_1.inputs[0])
    # group_input_1.Mean -> math_007_1.Value
    random__normal_.links.new(group_input_1.outputs[1], math_007_1.inputs[0])
    # math_008_1.Value -> math_007_1.Value
    random__normal_.links.new(math_008_1.outputs[0], math_007_1.inputs[1])
    # math_005_1.Value -> math_008_1.Value
    random__normal_.links.new(math_005_1.outputs[0], math_008_1.inputs[1])
    # math_004_1.Value -> math_005_1.Value
    random__normal_.links.new(math_004_1.outputs[0], math_005_1.inputs[1])
    # math_001_1.Value -> math_003_1.Value
    random__normal_.links.new(math_001_1.outputs[0], math_003_1.inputs[0])
    # group_input_1.Offset -> random_value_001.ID
    random__normal_.links.new(group_input_1.outputs[4], random_value_001.inputs[7])
    # group_input_1.Offset -> random_value_002.ID
    random__normal_.links.new(group_input_1.outputs[4], random_value_002.inputs[7])
    # group_input_1.Non-Negative -> switch_1.Switch
    random__normal_.links.new(group_input_1.outputs[0], switch_1.inputs[0])
    # math_007_1.Value -> math_006_1.Value
    random__normal_.links.new(math_007_1.outputs[0], math_006_1.inputs[0])
    # switch_1.Output -> group_output_1.Value
    random__normal_.links.new(switch_1.outputs[0], group_output_1.inputs[0])
    # math_007_1.Value -> switch_1.False
    random__normal_.links.new(math_007_1.outputs[0], switch_1.inputs[1])
    # math_006_1.Value -> switch_1.True
    random__normal_.links.new(math_006_1.outputs[0], switch_1.inputs[2])

    return random__normal_


random__normal_ = random__normal__node_group()

def random__uniform__node_group():
    """Initialize random__uniform_ node group"""
    random__uniform_ = bpy.data.node_groups.new(type='GeometryNodeTree', name="Random (Uniform)")

    random__uniform_.color_tag = 'NONE'
    random__uniform_.description = ""
    random__uniform_.default_group_node_width = 140

    # random__uniform_ interface

    # Socket Value
    value_socket_1 = random__uniform_.interface.new_socket(name="Value", in_out='OUTPUT', socket_type='NodeSocketFloat')
    value_socket_1.default_value = 0.0
    value_socket_1.min_value = -3.4028234663852886e+38
    value_socket_1.max_value = 3.4028234663852886e+38
    value_socket_1.subtype = 'NONE'
    value_socket_1.attribute_domain = 'POINT'
    value_socket_1.default_input = 'VALUE'
    value_socket_1.structure_type = 'AUTO'

    # Socket Min
    min_socket = random__uniform_.interface.new_socket(name="Min", in_out='INPUT', socket_type='NodeSocketFloat')
    min_socket.default_value = 0.0
    min_socket.min_value = -3.4028234663852886e+38
    min_socket.max_value = 3.4028234663852886e+38
    min_socket.subtype = 'NONE'
    min_socket.attribute_domain = 'POINT'
    min_socket.default_input = 'VALUE'
    min_socket.structure_type = 'AUTO'

    # Socket Max
    max_socket = random__uniform_.interface.new_socket(name="Max", in_out='INPUT', socket_type='NodeSocketFloat')
    max_socket.default_value = 1.0
    max_socket.min_value = -3.4028234663852886e+38
    max_socket.max_value = 3.4028234663852886e+38
    max_socket.subtype = 'NONE'
    max_socket.attribute_domain = 'POINT'
    max_socket.default_input = 'VALUE'
    max_socket.structure_type = 'AUTO'

    # Socket Seed
    seed_socket_1 = random__uniform_.interface.new_socket(name="Seed", in_out='INPUT', socket_type='NodeSocketInt')
    seed_socket_1.default_value = 0
    seed_socket_1.min_value = -2147483648
    seed_socket_1.max_value = 2147483647
    seed_socket_1.subtype = 'NONE'
    seed_socket_1.attribute_domain = 'POINT'
    seed_socket_1.hide_value = True
    seed_socket_1.default_input = 'VALUE'
    seed_socket_1.structure_type = 'AUTO'

    # Socket Offset
    offset_socket_1 = random__uniform_.interface.new_socket(name="Offset", in_out='INPUT', socket_type='NodeSocketInt')
    offset_socket_1.default_value = 0
    offset_socket_1.min_value = 0
    offset_socket_1.max_value = 2147483647
    offset_socket_1.subtype = 'NONE'
    offset_socket_1.attribute_domain = 'POINT'
    offset_socket_1.default_input = 'VALUE'
    offset_socket_1.structure_type = 'AUTO'

    # Initialize random__uniform_ nodes

    # Node Group Output
    group_output_2 = random__uniform_.nodes.new("NodeGroupOutput")
    group_output_2.name = "Group Output"
    group_output_2.is_active_output = True

    # Node Group Input
    group_input_2 = random__uniform_.nodes.new("NodeGroupInput")
    group_input_2.name = "Group Input"

    # Node Random Value.011
    random_value_011 = random__uniform_.nodes.new("FunctionNodeRandomValue")
    random_value_011.name = "Random Value.011"
    random_value_011.data_type = 'FLOAT'

    # Set locations
    group_output_2.location = (190.0, 0.0)
    group_input_2.location = (-200.0, 0.0)
    random_value_011.location = (0.0, 0.0)

    # Set dimensions
    group_output_2.width, group_output_2.height = 140.0, 100.0
    group_input_2.width, group_input_2.height = 140.0, 100.0
    random_value_011.width, random_value_011.height = 140.0, 100.0

    # Initialize random__uniform_ links

    # random_value_011.Value -> group_output_2.Value
    random__uniform_.links.new(random_value_011.outputs[1], group_output_2.inputs[0])
    # group_input_2.Min -> random_value_011.Min
    random__uniform_.links.new(group_input_2.outputs[0], random_value_011.inputs[2])
    # group_input_2.Max -> random_value_011.Max
    random__uniform_.links.new(group_input_2.outputs[1], random_value_011.inputs[3])
    # group_input_2.Offset -> random_value_011.ID
    random__uniform_.links.new(group_input_2.outputs[3], random_value_011.inputs[7])
    # group_input_2.Seed -> random_value_011.Seed
    random__uniform_.links.new(group_input_2.outputs[2], random_value_011.inputs[8])

    return random__uniform_


random__uniform_ = random__uniform__node_group()

def random_bag_node_group():
    """Initialize random_bag node group"""
    random_bag = bpy.data.node_groups.new(type='GeometryNodeTree', name="random_bag")

    random_bag.color_tag = 'NONE'
    random_bag.description = ""
    random_bag.default_group_node_width = 140
    random_bag.is_modifier = True

    # random_bag interface

    # Socket Geometry
    geometry_socket_1 = random_bag.interface.new_socket(name="Geometry", in_out='OUTPUT', socket_type='NodeSocketGeometry')
    geometry_socket_1.attribute_domain = 'POINT'
    geometry_socket_1.default_input = 'VALUE'
    geometry_socket_1.structure_type = 'AUTO'

    # Socket seed
    seed_socket_2 = random_bag.interface.new_socket(name="seed", in_out='INPUT', socket_type='NodeSocketInt')
    seed_socket_2.default_value = 0
    seed_socket_2.min_value = 0
    seed_socket_2.max_value = 2147483647
    seed_socket_2.subtype = 'NONE'
    seed_socket_2.attribute_domain = 'POINT'
    seed_socket_2.hide_value = True
    seed_socket_2.default_input = 'VALUE'
    seed_socket_2.structure_type = 'AUTO'

    # Socket detail
    detail_socket_1 = random_bag.interface.new_socket(name="detail", in_out='INPUT', socket_type='NodeSocketInt')
    detail_socket_1.default_value = 2
    detail_socket_1.min_value = 0
    detail_socket_1.max_value = 6
    detail_socket_1.subtype = 'NONE'
    detail_socket_1.attribute_domain = 'POINT'
    detail_socket_1.force_non_field = True
    detail_socket_1.default_input = 'VALUE'
    detail_socket_1.structure_type = 'SINGLE'

    # Socket scale
    scale_socket_1 = random_bag.interface.new_socket(name="scale", in_out='INPUT', socket_type='NodeSocketVector')
    scale_socket_1.default_value = (0.699999988079071, 0.3333333432674408, 0.25)
    scale_socket_1.min_value = 0.0010000000474974513
    scale_socket_1.max_value = 10000.0
    scale_socket_1.subtype = 'XYZ'
    scale_socket_1.attribute_domain = 'POINT'
    scale_socket_1.force_non_field = True
    scale_socket_1.default_input = 'VALUE'
    scale_socket_1.structure_type = 'SINGLE'

    # Socket mat
    mat_socket_1 = random_bag.interface.new_socket(name="mat", in_out='INPUT', socket_type='NodeSocketMaterial')
    mat_socket_1.attribute_domain = 'POINT'
    mat_socket_1.default_input = 'VALUE'
    mat_socket_1.structure_type = 'AUTO'

    # Initialize random_bag nodes

    # Node Group Input
    group_input_3 = random_bag.nodes.new("NodeGroupInput")
    group_input_3.name = "Group Input"

    # Node Group Output
    group_output_3 = random_bag.nodes.new("NodeGroupOutput")
    group_output_3.name = "Group Output"
    group_output_3.is_active_output = True

    # Node Bag
    bag_1 = random_bag.nodes.new("GeometryNodeGroup")
    bag_1.name = "Bag"
    bag_1.node_tree = bag
    # Socket_11
    bag_1.inputs[1].default_value = (3.0, 2.0)
    # Socket_3
    bag_1.inputs[3].default_value = 0.0

    # Node Random (Normal)
    random__normal__1 = random_bag.nodes.new("GeometryNodeGroup")
    random__normal__1.name = "Random (Normal)"
    random__normal__1.node_tree = random__normal_
    # Socket_1
    random__normal__1.inputs[0].default_value = True
    # Socket_5
    random__normal__1.inputs[4].default_value = 0

    # Node Random (Uniform)
    random__uniform__1 = random_bag.nodes.new("GeometryNodeGroup")
    random__uniform__1.name = "Random (Uniform)"
    random__uniform__1.node_tree = random__uniform_
    # Socket_1
    random__uniform__1.inputs[0].default_value = 0.003333000000566244
    # Socket_2
    random__uniform__1.inputs[1].default_value = 0.006666999775916338
    # Socket_4
    random__uniform__1.inputs[3].default_value = 9

    # Node Combine XYZ
    combine_xyz_1 = random_bag.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_1.name = "Combine XYZ"

    # Node Random (Normal).001
    random__normal__001 = random_bag.nodes.new("GeometryNodeGroup")
    random__normal__001.name = "Random (Normal).001"
    random__normal__001.node_tree = random__normal_
    # Socket_1
    random__normal__001.inputs[0].default_value = True
    # Socket_5
    random__normal__001.inputs[4].default_value = 1

    # Node Random (Normal).002
    random__normal__002 = random_bag.nodes.new("GeometryNodeGroup")
    random__normal__002.name = "Random (Normal).002"
    random__normal__002.node_tree = random__normal_
    # Socket_1
    random__normal__002.inputs[0].default_value = True
    # Socket_5
    random__normal__002.inputs[4].default_value = 2

    # Node Random (Normal).003
    random__normal__003 = random_bag.nodes.new("GeometryNodeGroup")
    random__normal__003.name = "Random (Normal).003"
    random__normal__003.node_tree = random__normal_
    # Socket_1
    random__normal__003.inputs[0].default_value = True
    # Socket_2
    random__normal__003.inputs[1].default_value = 0.05000000074505806
    # Socket_3
    random__normal__003.inputs[2].default_value = 0.004999999888241291
    # Socket_5
    random__normal__003.inputs[4].default_value = 3

    # Node Combine XYZ.001
    combine_xyz_001 = random_bag.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_001.name = "Combine XYZ.001"

    # Node Random (Normal).004
    random__normal__004 = random_bag.nodes.new("GeometryNodeGroup")
    random__normal__004.name = "Random (Normal).004"
    random__normal__004.node_tree = random__normal_
    # Socket_1
    random__normal__004.inputs[0].default_value = True
    # Socket_2
    random__normal__004.inputs[1].default_value = 0.05000000074505806
    # Socket_3
    random__normal__004.inputs[2].default_value = 0.004999999888241291
    # Socket_5
    random__normal__004.inputs[4].default_value = 4

    # Node Random (Normal).005
    random__normal__005 = random_bag.nodes.new("GeometryNodeGroup")
    random__normal__005.name = "Random (Normal).005"
    random__normal__005.node_tree = random__normal_
    # Socket_1
    random__normal__005.inputs[0].default_value = True
    # Socket_2
    random__normal__005.inputs[1].default_value = 0.4000000059604645
    # Socket_3
    random__normal__005.inputs[2].default_value = 0.05000000074505806
    # Socket_5
    random__normal__005.inputs[4].default_value = 5

    # Node Random (Normal).006
    random__normal__006 = random_bag.nodes.new("GeometryNodeGroup")
    random__normal__006.name = "Random (Normal).006"
    random__normal__006.node_tree = random__normal_
    # Socket_1
    random__normal__006.inputs[0].default_value = True
    # Socket_2
    random__normal__006.inputs[1].default_value = 0.15000000596046448
    # Socket_3
    random__normal__006.inputs[2].default_value = 0.014999999664723873
    # Socket_5
    random__normal__006.inputs[4].default_value = 6

    # Node Combine XYZ.002
    combine_xyz_002 = random_bag.nodes.new("ShaderNodeCombineXYZ")
    combine_xyz_002.name = "Combine XYZ.002"

    # Node Random (Normal).007
    random__normal__007 = random_bag.nodes.new("GeometryNodeGroup")
    random__normal__007.name = "Random (Normal).007"
    random__normal__007.node_tree = random__normal_
    # Socket_1
    random__normal__007.inputs[0].default_value = True
    # Socket_2
    random__normal__007.inputs[1].default_value = 0.20000000298023224
    # Socket_3
    random__normal__007.inputs[2].default_value = 0.019999999552965164
    # Socket_5
    random__normal__007.inputs[4].default_value = 7

    # Node Random (Normal).008
    random__normal__008 = random_bag.nodes.new("GeometryNodeGroup")
    random__normal__008.name = "Random (Normal).008"
    random__normal__008.node_tree = random__normal_
    # Socket_1
    random__normal__008.inputs[0].default_value = True
    # Socket_2
    random__normal__008.inputs[1].default_value = 0.10000000149011612
    # Socket_3
    random__normal__008.inputs[2].default_value = 0.009999999776482582
    # Socket_5
    random__normal__008.inputs[4].default_value = 8

    # Node Random (Normal).010
    random__normal__010 = random_bag.nodes.new("GeometryNodeGroup")
    random__normal__010.name = "Random (Normal).010"
    random__normal__010.node_tree = random__normal_
    # Socket_1
    random__normal__010.inputs[0].default_value = True
    # Socket_2
    random__normal__010.inputs[1].default_value = 0.20000000298023224
    # Socket_3
    random__normal__010.inputs[2].default_value = 0.05000000074505806
    # Socket_5
    random__normal__010.inputs[4].default_value = 10

    # Node Random (Normal).011
    random__normal__011 = random_bag.nodes.new("GeometryNodeGroup")
    random__normal__011.name = "Random (Normal).011"
    random__normal__011.node_tree = random__normal_
    # Socket_1
    random__normal__011.inputs[0].default_value = True
    # Socket_2
    random__normal__011.inputs[1].default_value = 0.33333298563957214
    # Socket_3
    random__normal__011.inputs[2].default_value = 0.08333300054073334
    # Socket_5
    random__normal__011.inputs[4].default_value = 11

    # Node Separate XYZ
    separate_xyz_1 = random_bag.nodes.new("ShaderNodeSeparateXYZ")
    separate_xyz_1.name = "Separate XYZ"

    # Node Math
    math_2 = random_bag.nodes.new("ShaderNodeMath")
    math_2.name = "Math"
    math_2.operation = 'DIVIDE'
    math_2.use_clamp = False
    # Value_001
    math_2.inputs[1].default_value = 10.0

    # Node Math.001
    math_001_2 = random_bag.nodes.new("ShaderNodeMath")
    math_001_2.name = "Math.001"
    math_001_2.operation = 'DIVIDE'
    math_001_2.use_clamp = False
    # Value_001
    math_001_2.inputs[1].default_value = 10.0

    # Node Math.002
    math_002_2 = random_bag.nodes.new("ShaderNodeMath")
    math_002_2.name = "Math.002"
    math_002_2.operation = 'DIVIDE'
    math_002_2.use_clamp = False
    # Value_001
    math_002_2.inputs[1].default_value = 10.0

    # Set locations
    group_input_3.location = (-2435.666748046875, 710.7201538085938)
    group_output_3.location = (200.0, 0.0)
    bag_1.location = (-58.193790435791016, 116.8686752319336)
    random__normal__1.location = (-1422.8194580078125, 1481.9234619140625)
    random__uniform__1.location = (-781.79541015625, -46.84378433227539)
    combine_xyz_1.location = (-1067.6883544921875, 1198.1478271484375)
    random__normal__001.location = (-1431.0369873046875, 1268.802001953125)
    random__normal__002.location = (-1425.2325439453125, 1068.87841796875)
    random__normal__003.location = (-1420.8665771484375, 846.693359375)
    combine_xyz_001.location = (-1030.9127197265625, 609.7442016601562)
    random__normal__004.location = (-1429.084228515625, 633.572021484375)
    random__normal__005.location = (-1423.2796630859375, 433.6484375)
    random__normal__006.location = (-1450.5362548828125, 213.9247589111328)
    combine_xyz_002.location = (-1030.4591064453125, 40.450740814208984)
    random__normal__007.location = (-1458.7537841796875, 0.8033896684646606)
    random__normal__008.location = (-1452.94921875, -199.12025451660156)
    random__normal__010.location = (-777.125, -252.07028198242188)
    random__normal__011.location = (-782.9793090820312, -448.9336853027344)
    separate_xyz_1.location = (-2251.806884765625, 994.312255859375)
    math_2.location = (-1938.161376953125, 969.6211547851562)
    math_001_2.location = (-1929.1092529296875, 1147.4912109375)
    math_002_2.location = (-1905.3477783203125, 1310.63330078125)

    # Set dimensions
    group_input_3.width, group_input_3.height = 140.0, 100.0
    group_output_3.width, group_output_3.height = 140.0, 100.0
    bag_1.width, bag_1.height = 140.0, 100.0
    random__normal__1.width, random__normal__1.height = 140.0, 100.0
    random__uniform__1.width, random__uniform__1.height = 140.0, 100.0
    combine_xyz_1.width, combine_xyz_1.height = 140.0, 100.0
    random__normal__001.width, random__normal__001.height = 140.0, 100.0
    random__normal__002.width, random__normal__002.height = 140.0, 100.0
    random__normal__003.width, random__normal__003.height = 140.0, 100.0
    combine_xyz_001.width, combine_xyz_001.height = 140.0, 100.0
    random__normal__004.width, random__normal__004.height = 140.0, 100.0
    random__normal__005.width, random__normal__005.height = 140.0, 100.0
    random__normal__006.width, random__normal__006.height = 140.0, 100.0
    combine_xyz_002.width, combine_xyz_002.height = 140.0, 100.0
    random__normal__007.width, random__normal__007.height = 140.0, 100.0
    random__normal__008.width, random__normal__008.height = 140.0, 100.0
    random__normal__010.width, random__normal__010.height = 140.0, 100.0
    random__normal__011.width, random__normal__011.height = 140.0, 100.0
    separate_xyz_1.width, separate_xyz_1.height = 140.0, 100.0
    math_2.width, math_2.height = 140.0, 100.0
    math_001_2.width, math_001_2.height = 140.0, 100.0
    math_002_2.width, math_002_2.height = 140.0, 100.0

    # Initialize random_bag links

    # bag_1.Geometry -> group_output_3.Geometry
    random_bag.links.new(bag_1.outputs[0], group_output_3.inputs[0])
    # group_input_3.seed -> random__normal__1.Seed
    random_bag.links.new(group_input_3.outputs[0], random__normal__1.inputs[3])
    # group_input_3.seed -> random__uniform__1.Seed
    random_bag.links.new(group_input_3.outputs[0], random__uniform__1.inputs[2])
    # group_input_3.seed -> random__normal__001.Seed
    random_bag.links.new(group_input_3.outputs[0], random__normal__001.inputs[3])
    # group_input_3.seed -> random__normal__002.Seed
    random_bag.links.new(group_input_3.outputs[0], random__normal__002.inputs[3])
    # random__normal__002.Value -> combine_xyz_1.Z
    random_bag.links.new(random__normal__002.outputs[0], combine_xyz_1.inputs[2])
    # random__normal__001.Value -> combine_xyz_1.Y
    random_bag.links.new(random__normal__001.outputs[0], combine_xyz_1.inputs[1])
    # random__normal__1.Value -> combine_xyz_1.X
    random_bag.links.new(random__normal__1.outputs[0], combine_xyz_1.inputs[0])
    # combine_xyz_1.Vector -> bag_1.scale
    random_bag.links.new(combine_xyz_1.outputs[0], bag_1.inputs[0])
    # group_input_3.detail -> bag_1.detail
    random_bag.links.new(group_input_3.outputs[1], bag_1.inputs[2])
    # group_input_3.seed -> random__normal__003.Seed
    random_bag.links.new(group_input_3.outputs[0], random__normal__003.inputs[3])
    # group_input_3.seed -> random__normal__004.Seed
    random_bag.links.new(group_input_3.outputs[0], random__normal__004.inputs[3])
    # group_input_3.seed -> random__normal__005.Seed
    random_bag.links.new(group_input_3.outputs[0], random__normal__005.inputs[3])
    # random__normal__005.Value -> combine_xyz_001.Z
    random_bag.links.new(random__normal__005.outputs[0], combine_xyz_001.inputs[2])
    # random__normal__004.Value -> combine_xyz_001.Y
    random_bag.links.new(random__normal__004.outputs[0], combine_xyz_001.inputs[1])
    # random__normal__003.Value -> combine_xyz_001.X
    random_bag.links.new(random__normal__003.outputs[0], combine_xyz_001.inputs[0])
    # group_input_3.seed -> random__normal__006.Seed
    random_bag.links.new(group_input_3.outputs[0], random__normal__006.inputs[3])
    # group_input_3.seed -> random__normal__007.Seed
    random_bag.links.new(group_input_3.outputs[0], random__normal__007.inputs[3])
    # group_input_3.seed -> random__normal__008.Seed
    random_bag.links.new(group_input_3.outputs[0], random__normal__008.inputs[3])
    # random__normal__008.Value -> combine_xyz_002.Z
    random_bag.links.new(random__normal__008.outputs[0], combine_xyz_002.inputs[2])
    # random__normal__007.Value -> combine_xyz_002.Y
    random_bag.links.new(random__normal__007.outputs[0], combine_xyz_002.inputs[1])
    # random__normal__006.Value -> combine_xyz_002.X
    random_bag.links.new(random__normal__006.outputs[0], combine_xyz_002.inputs[0])
    # group_input_3.seed -> random__normal__010.Seed
    random_bag.links.new(group_input_3.outputs[0], random__normal__010.inputs[3])
    # group_input_3.seed -> random__normal__011.Seed
    random_bag.links.new(group_input_3.outputs[0], random__normal__011.inputs[3])
    # random__uniform__1.Value -> bag_1.neck_thickness
    random_bag.links.new(random__uniform__1.outputs[0], bag_1.inputs[6])
    # random__normal__010.Value -> bag_1.edge_crease
    random_bag.links.new(random__normal__010.outputs[0], bag_1.inputs[7])
    # random__normal__011.Value -> bag_1.vertex_crease
    random_bag.links.new(random__normal__011.outputs[0], bag_1.inputs[8])
    # group_input_3.mat -> bag_1.mat
    random_bag.links.new(group_input_3.outputs[3], bag_1.inputs[9])
    # group_input_3.scale -> separate_xyz_1.Vector
    random_bag.links.new(group_input_3.outputs[2], separate_xyz_1.inputs[0])
    # separate_xyz_1.Z -> math_2.Value
    random_bag.links.new(separate_xyz_1.outputs[2], math_2.inputs[0])
    # separate_xyz_1.Y -> math_001_2.Value
    random_bag.links.new(separate_xyz_1.outputs[1], math_001_2.inputs[0])
    # separate_xyz_1.X -> math_002_2.Value
    random_bag.links.new(separate_xyz_1.outputs[0], math_002_2.inputs[0])
    # separate_xyz_1.X -> random__normal__1.Mean
    random_bag.links.new(separate_xyz_1.outputs[0], random__normal__1.inputs[1])
    # separate_xyz_1.Y -> random__normal__001.Mean
    random_bag.links.new(separate_xyz_1.outputs[1], random__normal__001.inputs[1])
    # separate_xyz_1.Z -> random__normal__002.Mean
    random_bag.links.new(separate_xyz_1.outputs[2], random__normal__002.inputs[1])
    # math_2.Value -> random__normal__002.Std. Dev.
    random_bag.links.new(math_2.outputs[0], random__normal__002.inputs[2])
    # math_001_2.Value -> random__normal__001.Std. Dev.
    random_bag.links.new(math_001_2.outputs[0], random__normal__001.inputs[2])
    # math_002_2.Value -> random__normal__1.Std. Dev.
    random_bag.links.new(math_002_2.outputs[0], random__normal__1.inputs[2])
    # combine_xyz_001.Vector -> bag_1.bag_taper
    random_bag.links.new(combine_xyz_001.outputs[0], bag_1.inputs[4])
    # combine_xyz_002.Vector -> bag_1.neck_taper
    random_bag.links.new(combine_xyz_002.outputs[0], bag_1.inputs[5])

    return random_bag


random_bag = random_bag_node_group()


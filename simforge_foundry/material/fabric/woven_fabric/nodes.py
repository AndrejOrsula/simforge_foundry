import bpy
import mathutils


mat = bpy.data.materials.new(name = "Woven Fabric")
mat.use_nodes = True


def wovenfabricshader_node_group():
    """Initialize WovenFabricShader node group"""
    wovenfabricshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "WovenFabricShader")

    wovenfabricshader.color_tag = 'NONE'
    wovenfabricshader.description = ""
    wovenfabricshader.default_group_node_width = 140
    # wovenfabricshader interface

    # Socket Shader
    shader_socket = wovenfabricshader.interface.new_socket(name="Shader", in_out='OUTPUT', socket_type='NodeSocketShader')
    shader_socket.attribute_domain = 'POINT'
    shader_socket.default_input = 'VALUE'
    shader_socket.structure_type = 'AUTO'

    # Socket Vector
    vector_socket = wovenfabricshader.interface.new_socket(name="Vector", in_out='INPUT', socket_type='NodeSocketVector')
    vector_socket.default_value = (0.0, 0.0, 0.0)
    vector_socket.min_value = -3.4028234663852886e+38
    vector_socket.max_value = 3.4028234663852886e+38
    vector_socket.subtype = 'NONE'
    vector_socket.attribute_domain = 'POINT'
    vector_socket.default_input = 'VALUE'
    vector_socket.structure_type = 'AUTO'

    # Socket Scale
    scale_socket = wovenfabricshader.interface.new_socket(name="Scale", in_out='INPUT', socket_type='NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    # Socket Weave Color 1
    weave_color_1_socket = wovenfabricshader.interface.new_socket(name="Weave Color 1", in_out='INPUT', socket_type='NodeSocketColor')
    weave_color_1_socket.default_value = (1.0, 1.0, 1.0, 1.0)
    weave_color_1_socket.attribute_domain = 'POINT'
    weave_color_1_socket.default_input = 'VALUE'
    weave_color_1_socket.structure_type = 'AUTO'

    # Socket Weave Color 2
    weave_color_2_socket = wovenfabricshader.interface.new_socket(name="Weave Color 2", in_out='INPUT', socket_type='NodeSocketColor')
    weave_color_2_socket.default_value = (0.02144564688205719, 0.04039090499281883, 0.07594017684459686, 1.0)
    weave_color_2_socket.attribute_domain = 'POINT'
    weave_color_2_socket.default_input = 'VALUE'
    weave_color_2_socket.structure_type = 'AUTO'

    # Socket Roughness
    roughness_socket = wovenfabricshader.interface.new_socket(name="Roughness", in_out='INPUT', socket_type='NodeSocketFloat')
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 1.0
    roughness_socket.subtype = 'FACTOR'
    roughness_socket.attribute_domain = 'POINT'
    roughness_socket.default_input = 'VALUE'
    roughness_socket.structure_type = 'AUTO'

    # Socket Sheen Weight
    sheen_weight_socket = wovenfabricshader.interface.new_socket(name="Sheen Weight", in_out='INPUT', socket_type='NodeSocketFloat')
    sheen_weight_socket.default_value = 1.0
    sheen_weight_socket.min_value = 0.0
    sheen_weight_socket.max_value = 1.0
    sheen_weight_socket.subtype = 'FACTOR'
    sheen_weight_socket.attribute_domain = 'POINT'
    sheen_weight_socket.default_input = 'VALUE'
    sheen_weight_socket.structure_type = 'AUTO'

    # Socket Sheen Roughness
    sheen_roughness_socket = wovenfabricshader.interface.new_socket(name="Sheen Roughness", in_out='INPUT', socket_type='NodeSocketFloat')
    sheen_roughness_socket.default_value = 0.30000001192092896
    sheen_roughness_socket.min_value = 0.0
    sheen_roughness_socket.max_value = 1.0
    sheen_roughness_socket.subtype = 'FACTOR'
    sheen_roughness_socket.attribute_domain = 'POINT'
    sheen_roughness_socket.default_input = 'VALUE'
    sheen_roughness_socket.structure_type = 'AUTO'

    # Socket Sheen Tint
    sheen_tint_socket = wovenfabricshader.interface.new_socket(name="Sheen Tint", in_out='INPUT', socket_type='NodeSocketColor')
    sheen_tint_socket.default_value = (0.3532320261001587, 0.14208389818668365, 0.11482997238636017, 1.0)
    sheen_tint_socket.attribute_domain = 'POINT'
    sheen_tint_socket.default_input = 'VALUE'
    sheen_tint_socket.structure_type = 'AUTO'

    # Socket Weave Bump Strength
    weave_bump_strength_socket = wovenfabricshader.interface.new_socket(name="Weave Bump Strength", in_out='INPUT', socket_type='NodeSocketFloat')
    weave_bump_strength_socket.default_value = 0.4000000059604645
    weave_bump_strength_socket.min_value = 0.0
    weave_bump_strength_socket.max_value = 1.0
    weave_bump_strength_socket.subtype = 'FACTOR'
    weave_bump_strength_socket.attribute_domain = 'POINT'
    weave_bump_strength_socket.default_input = 'VALUE'
    weave_bump_strength_socket.structure_type = 'AUTO'

    # Socket Noise Bump Strength
    noise_bump_strength_socket = wovenfabricshader.interface.new_socket(name="Noise Bump Strength", in_out='INPUT', socket_type='NodeSocketFloat')
    noise_bump_strength_socket.default_value = 0.4000000059604645
    noise_bump_strength_socket.min_value = 0.0
    noise_bump_strength_socket.max_value = 1.0
    noise_bump_strength_socket.subtype = 'FACTOR'
    noise_bump_strength_socket.attribute_domain = 'POINT'
    noise_bump_strength_socket.default_input = 'VALUE'
    noise_bump_strength_socket.structure_type = 'AUTO'

    # Initialize wovenfabricshader nodes

    # Node Group Output
    group_output = wovenfabricshader.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # Node Group Input
    group_input = wovenfabricshader.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # Node Principled BSDF
    principled_bsdf = wovenfabricshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    # Metallic
    principled_bsdf.inputs[1].default_value = 0.0
    # IOR
    principled_bsdf.inputs[3].default_value = 1.5
    # Alpha
    principled_bsdf.inputs[4].default_value = 1.0
    # Diffuse Roughness
    principled_bsdf.inputs[7].default_value = 0.0
    # Subsurface Weight
    principled_bsdf.inputs[8].default_value = 0.0
    # Subsurface Radius
    principled_bsdf.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    # Subsurface Scale
    principled_bsdf.inputs[10].default_value = 0.05000000074505806
    # Subsurface Anisotropy
    principled_bsdf.inputs[12].default_value = 0.0
    # Specular IOR Level
    principled_bsdf.inputs[13].default_value = 0.5
    # Specular Tint
    principled_bsdf.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    # Anisotropic
    principled_bsdf.inputs[15].default_value = 0.0
    # Anisotropic Rotation
    principled_bsdf.inputs[16].default_value = 0.0
    # Tangent
    principled_bsdf.inputs[17].default_value = (0.0, 0.0, 0.0)
    # Transmission Weight
    principled_bsdf.inputs[18].default_value = 0.0
    # Coat Weight
    principled_bsdf.inputs[19].default_value = 0.0
    # Coat Roughness
    principled_bsdf.inputs[20].default_value = 0.029999999329447746
    # Coat IOR
    principled_bsdf.inputs[21].default_value = 1.5
    # Coat Tint
    principled_bsdf.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    # Coat Normal
    principled_bsdf.inputs[23].default_value = (0.0, 0.0, 0.0)
    # Emission Color
    principled_bsdf.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    # Emission Strength
    principled_bsdf.inputs[28].default_value = 0.0
    # Thin Film Thickness
    principled_bsdf.inputs[29].default_value = 0.0
    # Thin Film IOR
    principled_bsdf.inputs[30].default_value = 1.3300000429153442

    # Node Wave Texture
    wave_texture = wovenfabricshader.nodes.new("ShaderNodeTexWave")
    wave_texture.name = "Wave Texture"
    wave_texture.bands_direction = 'Y'
    wave_texture.rings_direction = 'X'
    wave_texture.wave_profile = 'SIN'
    wave_texture.wave_type = 'BANDS'
    # Scale
    wave_texture.inputs[1].default_value = 60.0
    # Distortion
    wave_texture.inputs[2].default_value = 0.0
    # Detail
    wave_texture.inputs[3].default_value = 2.0
    # Detail Scale
    wave_texture.inputs[4].default_value = 1.0
    # Detail Roughness
    wave_texture.inputs[5].default_value = 0.5
    # Phase Offset
    wave_texture.inputs[6].default_value = 0.0

    # Node Mapping
    mapping = wovenfabricshader.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = 'POINT'
    # Location
    mapping.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    mapping.inputs[2].default_value = (0.0, 0.0, 0.0)

    # Node Mapping.001
    mapping_001 = wovenfabricshader.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = 'POINT'
    # Location
    mapping_001.inputs[1].default_value = (0.054999999701976776, 0.0, 0.0)
    # Rotation
    mapping_001.inputs[2].default_value = (0.0, 0.0, 1.5707963705062866)
    # Scale
    mapping_001.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Wave Texture.001
    wave_texture_001 = wovenfabricshader.nodes.new("ShaderNodeTexWave")
    wave_texture_001.name = "Wave Texture.001"
    wave_texture_001.bands_direction = 'X'
    wave_texture_001.rings_direction = 'X'
    wave_texture_001.wave_profile = 'SIN'
    wave_texture_001.wave_type = 'BANDS'
    # Scale
    wave_texture_001.inputs[1].default_value = 60.0
    # Distortion
    wave_texture_001.inputs[2].default_value = 0.0
    # Detail
    wave_texture_001.inputs[3].default_value = 2.0
    # Detail Scale
    wave_texture_001.inputs[4].default_value = 1.0
    # Detail Roughness
    wave_texture_001.inputs[5].default_value = 0.5
    # Phase Offset
    wave_texture_001.inputs[6].default_value = 0.0

    # Node Math
    math = wovenfabricshader.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'MULTIPLY'
    math.use_clamp = False

    # Node Math.001
    math_001 = wovenfabricshader.nodes.new("ShaderNodeMath")
    math_001.name = "Math.001"
    math_001.operation = 'ADD'
    math_001.use_clamp = False
    # Value
    math_001.inputs[0].default_value = -0.6499999761581421

    # Node Frame
    frame = wovenfabricshader.nodes.new("NodeFrame")
    frame.label = "Weaves 1"
    frame.name = "Frame"
    frame.label_size = 20
    frame.shrink = True

    # Node Wave Texture.002
    wave_texture_002 = wovenfabricshader.nodes.new("ShaderNodeTexWave")
    wave_texture_002.name = "Wave Texture.002"
    wave_texture_002.bands_direction = 'Y'
    wave_texture_002.rings_direction = 'X'
    wave_texture_002.wave_profile = 'SIN'
    wave_texture_002.wave_type = 'BANDS'
    # Scale
    wave_texture_002.inputs[1].default_value = 60.0
    # Distortion
    wave_texture_002.inputs[2].default_value = 0.0
    # Detail
    wave_texture_002.inputs[3].default_value = 2.0
    # Detail Scale
    wave_texture_002.inputs[4].default_value = 1.0
    # Detail Roughness
    wave_texture_002.inputs[5].default_value = 0.5
    # Phase Offset
    wave_texture_002.inputs[6].default_value = 0.0

    # Node Mapping.002
    mapping_002 = wovenfabricshader.nodes.new("ShaderNodeMapping")
    mapping_002.name = "Mapping.002"
    mapping_002.vector_type = 'POINT'
    # Location
    mapping_002.inputs[1].default_value = (0.0, 0.0, 0.0)
    # Rotation
    mapping_002.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    mapping_002.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Wave Texture.003
    wave_texture_003 = wovenfabricshader.nodes.new("ShaderNodeTexWave")
    wave_texture_003.name = "Wave Texture.003"
    wave_texture_003.bands_direction = 'X'
    wave_texture_003.rings_direction = 'X'
    wave_texture_003.wave_profile = 'SIN'
    wave_texture_003.wave_type = 'BANDS'
    # Scale
    wave_texture_003.inputs[1].default_value = 60.0
    # Distortion
    wave_texture_003.inputs[2].default_value = 0.0
    # Detail
    wave_texture_003.inputs[3].default_value = 2.0
    # Detail Scale
    wave_texture_003.inputs[4].default_value = 1.0
    # Detail Roughness
    wave_texture_003.inputs[5].default_value = 0.5
    # Phase Offset
    wave_texture_003.inputs[6].default_value = 0.0

    # Node Math.002
    math_002 = wovenfabricshader.nodes.new("ShaderNodeMath")
    math_002.name = "Math.002"
    math_002.operation = 'MULTIPLY'
    math_002.use_clamp = False

    # Node Math.003
    math_003 = wovenfabricshader.nodes.new("ShaderNodeMath")
    math_003.name = "Math.003"
    math_003.operation = 'ADD'
    math_003.use_clamp = False
    # Value
    math_003.inputs[0].default_value = -0.6499999761581421

    # Node Frame.001
    frame_001 = wovenfabricshader.nodes.new("NodeFrame")
    frame_001.label = "Weaves 2"
    frame_001.name = "Frame.001"
    frame_001.label_size = 20
    frame_001.shrink = True

    # Node Mix
    mix = wovenfabricshader.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'LIGHTEN'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'
    # Factor_Float
    mix.inputs[0].default_value = 1.0

    # Node Wave Texture.004
    wave_texture_004 = wovenfabricshader.nodes.new("ShaderNodeTexWave")
    wave_texture_004.name = "Wave Texture.004"
    wave_texture_004.bands_direction = 'Y'
    wave_texture_004.rings_direction = 'X'
    wave_texture_004.wave_profile = 'SIN'
    wave_texture_004.wave_type = 'BANDS'
    # Scale
    wave_texture_004.inputs[1].default_value = 60.0
    # Distortion
    wave_texture_004.inputs[2].default_value = 0.0
    # Detail
    wave_texture_004.inputs[3].default_value = 2.0
    # Detail Scale
    wave_texture_004.inputs[4].default_value = 1.0
    # Detail Roughness
    wave_texture_004.inputs[5].default_value = 0.5
    # Phase Offset
    wave_texture_004.inputs[6].default_value = 0.0

    # Node Mapping.003
    mapping_003 = wovenfabricshader.nodes.new("ShaderNodeMapping")
    mapping_003.name = "Mapping.003"
    mapping_003.vector_type = 'POINT'
    # Location
    mapping_003.inputs[1].default_value = (0.0, 0.054999999701976776, 0.0)
    # Rotation
    mapping_003.inputs[2].default_value = (0.0, 0.0, 1.5707963705062866)
    # Scale
    mapping_003.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Wave Texture.005
    wave_texture_005 = wovenfabricshader.nodes.new("ShaderNodeTexWave")
    wave_texture_005.name = "Wave Texture.005"
    wave_texture_005.bands_direction = 'X'
    wave_texture_005.rings_direction = 'X'
    wave_texture_005.wave_profile = 'SIN'
    wave_texture_005.wave_type = 'BANDS'
    # Scale
    wave_texture_005.inputs[1].default_value = 60.0
    # Distortion
    wave_texture_005.inputs[2].default_value = 0.0
    # Detail
    wave_texture_005.inputs[3].default_value = 2.0
    # Detail Scale
    wave_texture_005.inputs[4].default_value = 1.0
    # Detail Roughness
    wave_texture_005.inputs[5].default_value = 0.5
    # Phase Offset
    wave_texture_005.inputs[6].default_value = 0.0

    # Node Math.004
    math_004 = wovenfabricshader.nodes.new("ShaderNodeMath")
    math_004.name = "Math.004"
    math_004.operation = 'MULTIPLY'
    math_004.use_clamp = False

    # Node Math.005
    math_005 = wovenfabricshader.nodes.new("ShaderNodeMath")
    math_005.name = "Math.005"
    math_005.operation = 'ADD'
    math_005.use_clamp = False
    # Value
    math_005.inputs[0].default_value = -0.6499999761581421

    # Node Frame.002
    frame_002 = wovenfabricshader.nodes.new("NodeFrame")
    frame_002.label = "Weaves 3"
    frame_002.name = "Frame.002"
    frame_002.label_size = 20
    frame_002.shrink = True

    # Node Wave Texture.006
    wave_texture_006 = wovenfabricshader.nodes.new("ShaderNodeTexWave")
    wave_texture_006.name = "Wave Texture.006"
    wave_texture_006.bands_direction = 'Y'
    wave_texture_006.rings_direction = 'X'
    wave_texture_006.wave_profile = 'SIN'
    wave_texture_006.wave_type = 'BANDS'
    # Scale
    wave_texture_006.inputs[1].default_value = 60.0
    # Distortion
    wave_texture_006.inputs[2].default_value = 0.0
    # Detail
    wave_texture_006.inputs[3].default_value = 2.0
    # Detail Scale
    wave_texture_006.inputs[4].default_value = 1.0
    # Detail Roughness
    wave_texture_006.inputs[5].default_value = 0.5
    # Phase Offset
    wave_texture_006.inputs[6].default_value = 0.0

    # Node Mapping.004
    mapping_004 = wovenfabricshader.nodes.new("ShaderNodeMapping")
    mapping_004.name = "Mapping.004"
    mapping_004.vector_type = 'POINT'
    # Location
    mapping_004.inputs[1].default_value = (0.054999999701976776, 0.054999999701976776, 0.0)
    # Rotation
    mapping_004.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Scale
    mapping_004.inputs[3].default_value = (1.0, 1.0, 1.0)

    # Node Wave Texture.007
    wave_texture_007 = wovenfabricshader.nodes.new("ShaderNodeTexWave")
    wave_texture_007.name = "Wave Texture.007"
    wave_texture_007.bands_direction = 'X'
    wave_texture_007.rings_direction = 'X'
    wave_texture_007.wave_profile = 'SIN'
    wave_texture_007.wave_type = 'BANDS'
    # Scale
    wave_texture_007.inputs[1].default_value = 60.0
    # Distortion
    wave_texture_007.inputs[2].default_value = 0.0
    # Detail
    wave_texture_007.inputs[3].default_value = 2.0
    # Detail Scale
    wave_texture_007.inputs[4].default_value = 1.0
    # Detail Roughness
    wave_texture_007.inputs[5].default_value = 0.5
    # Phase Offset
    wave_texture_007.inputs[6].default_value = 0.0

    # Node Math.006
    math_006 = wovenfabricshader.nodes.new("ShaderNodeMath")
    math_006.name = "Math.006"
    math_006.operation = 'MULTIPLY'
    math_006.use_clamp = False

    # Node Math.007
    math_007 = wovenfabricshader.nodes.new("ShaderNodeMath")
    math_007.name = "Math.007"
    math_007.operation = 'ADD'
    math_007.use_clamp = False
    # Value
    math_007.inputs[0].default_value = -0.6499999761581421

    # Node Frame.003
    frame_003 = wovenfabricshader.nodes.new("NodeFrame")
    frame_003.label = "Weaves 4"
    frame_003.name = "Frame.003"
    frame_003.label_size = 20
    frame_003.shrink = True

    # Node Mix.001
    mix_001 = wovenfabricshader.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'LIGHTEN'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'RGBA'
    mix_001.factor_mode = 'UNIFORM'
    # Factor_Float
    mix_001.inputs[0].default_value = 1.0

    # Node Mix.002
    mix_002 = wovenfabricshader.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = 'LIGHTEN'
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = 'RGBA'
    mix_002.factor_mode = 'UNIFORM'
    # Factor_Float
    mix_002.inputs[0].default_value = 1.0

    # Node Bump
    bump = wovenfabricshader.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    # Distance
    bump.inputs[1].default_value = 1.0
    # Filter Width
    bump.inputs[2].default_value = 1.0
    # Normal
    bump.inputs[4].default_value = (0.0, 0.0, 0.0)

    # Node Noise Texture
    noise_texture = wovenfabricshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    # Scale
    noise_texture.inputs[2].default_value = 150.0
    # Detail
    noise_texture.inputs[3].default_value = 15.0
    # Roughness
    noise_texture.inputs[4].default_value = 0.699999988079071
    # Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    # Distortion
    noise_texture.inputs[8].default_value = 0.0

    # Node Bump.001
    bump_001 = wovenfabricshader.nodes.new("ShaderNodeBump")
    bump_001.name = "Bump.001"
    bump_001.invert = False
    # Distance
    bump_001.inputs[1].default_value = 1.0
    # Filter Width
    bump_001.inputs[2].default_value = 1.0

    # Node Frame.004
    frame_004 = wovenfabricshader.nodes.new("NodeFrame")
    frame_004.label = "Bump"
    frame_004.name = "Frame.004"
    frame_004.label_size = 20
    frame_004.shrink = True

    # Node Reroute
    reroute = wovenfabricshader.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketColor"
    # Node Noise Texture.001
    noise_texture_001 = wovenfabricshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = '3D'
    noise_texture_001.noise_type = 'FBM'
    noise_texture_001.normalize = True
    # Scale
    noise_texture_001.inputs[2].default_value = 120.0
    # Detail
    noise_texture_001.inputs[3].default_value = 15.0
    # Roughness
    noise_texture_001.inputs[4].default_value = 0.5
    # Lacunarity
    noise_texture_001.inputs[5].default_value = 2.0
    # Distortion
    noise_texture_001.inputs[8].default_value = 0.0

    # Node Mix.003
    mix_003 = wovenfabricshader.nodes.new("ShaderNodeMix")
    mix_003.name = "Mix.003"
    mix_003.blend_type = 'LINEAR_LIGHT'
    mix_003.clamp_factor = True
    mix_003.clamp_result = False
    mix_003.data_type = 'RGBA'
    mix_003.factor_mode = 'UNIFORM'
    # Factor_Float
    mix_003.inputs[0].default_value = 0.0020000000949949026

    # Node Frame.005
    frame_005 = wovenfabricshader.nodes.new("NodeFrame")
    frame_005.label = "Mapping"
    frame_005.name = "Frame.005"
    frame_005.label_size = 20
    frame_005.shrink = True

    # Node Mix.004
    mix_004 = wovenfabricshader.nodes.new("ShaderNodeMix")
    mix_004.name = "Mix.004"
    mix_004.blend_type = 'LIGHTEN'
    mix_004.clamp_factor = True
    mix_004.clamp_result = False
    mix_004.data_type = 'RGBA'
    mix_004.factor_mode = 'UNIFORM'
    # Factor_Float
    mix_004.inputs[0].default_value = 1.0

    # Node Mix.005
    mix_005 = wovenfabricshader.nodes.new("ShaderNodeMix")
    mix_005.name = "Mix.005"
    mix_005.blend_type = 'LIGHTEN'
    mix_005.clamp_factor = True
    mix_005.clamp_result = False
    mix_005.data_type = 'RGBA'
    mix_005.factor_mode = 'UNIFORM'
    # Factor_Float
    mix_005.inputs[0].default_value = 1.0

    # Node Mix.006
    mix_006 = wovenfabricshader.nodes.new("ShaderNodeMix")
    mix_006.name = "Mix.006"
    mix_006.blend_type = 'MIX'
    mix_006.clamp_factor = True
    mix_006.clamp_result = False
    mix_006.data_type = 'RGBA'
    mix_006.factor_mode = 'UNIFORM'
    # A_Color
    mix_006.inputs[6].default_value = (0.0, 0.0, 0.0, 1.0)

    # Node Mix.007
    mix_007 = wovenfabricshader.nodes.new("ShaderNodeMix")
    mix_007.name = "Mix.007"
    mix_007.blend_type = 'MIX'
    mix_007.clamp_factor = True
    mix_007.clamp_result = False
    mix_007.data_type = 'RGBA'
    mix_007.factor_mode = 'UNIFORM'
    # A_Color
    mix_007.inputs[6].default_value = (0.0, 0.0, 0.0, 1.0)

    # Node Mix.008
    mix_008 = wovenfabricshader.nodes.new("ShaderNodeMix")
    mix_008.name = "Mix.008"
    mix_008.blend_type = 'LIGHTEN'
    mix_008.clamp_factor = True
    mix_008.clamp_result = False
    mix_008.data_type = 'RGBA'
    mix_008.factor_mode = 'UNIFORM'
    # Factor_Float
    mix_008.inputs[0].default_value = 1.0

    # Node Frame.006
    frame_006 = wovenfabricshader.nodes.new("NodeFrame")
    frame_006.label = "Base Color"
    frame_006.name = "Frame.006"
    frame_006.label_size = 20
    frame_006.shrink = True

    # Set parents
    wave_texture.parent = frame
    mapping.parent = frame_005
    mapping_001.parent = frame
    wave_texture_001.parent = frame
    math.parent = frame
    math_001.parent = frame
    wave_texture_002.parent = frame_001
    mapping_002.parent = frame_001
    wave_texture_003.parent = frame_001
    math_002.parent = frame_001
    math_003.parent = frame_001
    wave_texture_004.parent = frame_002
    mapping_003.parent = frame_002
    wave_texture_005.parent = frame_002
    math_004.parent = frame_002
    math_005.parent = frame_002
    wave_texture_006.parent = frame_003
    mapping_004.parent = frame_003
    wave_texture_007.parent = frame_003
    math_006.parent = frame_003
    math_007.parent = frame_003
    mix_002.parent = frame_004
    bump.parent = frame_004
    noise_texture.parent = frame_004
    bump_001.parent = frame_004
    noise_texture_001.parent = frame_005
    mix_003.parent = frame_005
    mix_004.parent = frame_006
    mix_005.parent = frame_006
    mix_006.parent = frame_006
    mix_007.parent = frame_006
    mix_008.parent = frame_006

    # Set locations
    group_output.location = (1689.2373046875, 0.0)
    group_input.location = (-1626.675048828125, 19.472103118896484)
    principled_bsdf.location = (1399.2373046875, 468.5235595703125)
    wave_texture.location = (235.19915771484375, -35.859619140625)
    mapping.location = (30.2110595703125, -97.59844970703125)
    mapping_001.location = (29.9571533203125, -202.9261474609375)
    wave_texture_001.location = (235.9046630859375, -337.4451904296875)
    math.location = (575.734375, -118.29296875)
    math_001.location = (425.7751770019531, -252.321044921875)
    frame.location = (-525.3157958984375, 1233.442138671875)
    wave_texture_002.location = (235.25177001953125, -36.01593017578125)
    mapping_002.location = (30.009765625, -203.08242797851562)
    wave_texture_003.location = (235.957275390625, -337.6014709472656)
    math_002.location = (575.7869873046875, -118.44921875)
    math_003.location = (425.8277893066406, -252.477294921875)
    frame_001.location = (-524.368408203125, 521.9684448242188)
    mix.location = (337.12738037109375, 842.5789184570312)
    wave_texture_004.location = (234.84130859375, -36.01606750488281)
    mapping_003.location = (29.59930419921875, -203.0825653076172)
    wave_texture_005.location = (235.54681396484375, -337.60162353515625)
    math_004.location = (575.3765258789062, -118.44935607910156)
    math_005.location = (425.4173278808594, -252.47743225097656)
    frame_002.location = (-540.4736938476562, -187.6105194091797)
    wave_texture_006.location = (234.946533203125, -36.17254638671875)
    mapping_004.location = (29.70452880859375, -203.23907470703125)
    wave_texture_007.location = (235.65203857421875, -337.75811767578125)
    math_006.location = (575.4817504882812, -118.6058349609375)
    math_007.location = (425.5225524902344, -252.63385009765625)
    frame_003.location = (-538.5789184570312, -899.0841674804688)
    mix_001.location = (332.970703125, -558.1807861328125)
    mix_002.location = (29.79510498046875, -35.96809387207031)
    bump.location = (205.28668212890625, -53.68116760253906)
    noise_texture.location = (198.297607421875, -226.3501434326172)
    bump_001.location = (385.1280517578125, -50.61622619628906)
    frame_004.location = (526.2631225585938, 218.81053161621094)
    reroute.location = (-720.6094360351562, -95.37091064453125)
    noise_texture_001.location = (210.3486328125, -217.09072875976562)
    mix_003.location = (379.701416015625, -36.333526611328125)
    frame_005.location = (-1397.842041015625, 30.284210205078125)
    mix_004.location = (29.8133544921875, -35.93121337890625)
    mix_005.location = (29.82452392578125, -273.5518798828125)
    mix_006.location = (203.14202880859375, -43.1109619140625)
    mix_007.location = (206.40509033203125, -276.77764892578125)
    mix_008.location = (373.27203369140625, -91.94366455078125)
    frame_006.location = (670.2631225585938, 926.4947509765625)

    # Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    principled_bsdf.width, principled_bsdf.height = 240.0, 100.0
    wave_texture.width, wave_texture.height = 150.0, 100.0
    mapping.width, mapping.height = 140.0, 100.0
    mapping_001.width, mapping_001.height = 140.0, 100.0
    wave_texture_001.width, wave_texture_001.height = 150.0, 100.0
    math.width, math.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    frame.width, frame.height = 745.368408203125, 673.07373046875
    wave_texture_002.width, wave_texture_002.height = 150.0, 100.0
    mapping_002.width, mapping_002.height = 140.0, 100.0
    wave_texture_003.width, wave_texture_003.height = 150.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    frame_001.width, frame_001.height = 745.368408203125, 668.3368530273438
    mix.width, mix.height = 140.0, 100.0
    wave_texture_004.width, wave_texture_004.height = 150.0, 100.0
    mapping_003.width, mapping_003.height = 140.0, 100.0
    wave_texture_005.width, wave_texture_005.height = 150.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    frame_002.width, frame_002.height = 745.368408203125, 666.4420776367188
    wave_texture_006.width, wave_texture_006.height = 150.0, 100.0
    mapping_004.width, mapping_004.height = 140.0, 100.0
    wave_texture_007.width, wave_texture_007.height = 150.0, 100.0
    math_006.width, math_006.height = 140.0, 100.0
    math_007.width, math_007.height = 140.0, 100.0
    frame_003.width, frame_003.height = 745.368408203125, 667.3894653320312
    mix_001.width, mix_001.height = 140.0, 100.0
    mix_002.width, mix_002.height = 140.0, 100.0
    bump.width, bump.height = 140.0, 100.0
    noise_texture.width, noise_texture.height = 140.0, 100.0
    bump_001.width, bump_001.height = 140.0, 100.0
    frame_004.width, frame_004.height = 554.9474487304688, 533.810546875
    reroute.width, reroute.height = 10.5, 100.0
    noise_texture_001.width, noise_texture_001.height = 140.0, 100.0
    mix_003.width, mix_003.height = 140.0, 100.0
    frame_005.width, frame_005.height = 549.2631225585938, 524.3367919921875
    mix_004.width, mix_004.height = 140.0, 100.0
    mix_005.width, mix_005.height = 140.0, 100.0
    mix_006.width, mix_006.height = 140.0, 100.0
    mix_007.width, mix_007.height = 140.0, 100.0
    mix_008.width, mix_008.height = 140.0, 100.0
    frame_006.width, frame_006.height = 543.5790405273438, 529.07373046875

    # Initialize wovenfabricshader links

    # mapping_002.Vector -> wave_texture_003.Vector
    wovenfabricshader.links.new(mapping_002.outputs[0], wave_texture_003.inputs[0])
    # bump_001.Normal -> principled_bsdf.Normal
    wovenfabricshader.links.new(bump_001.outputs[0], principled_bsdf.inputs[5])
    # wave_texture_002.Color -> math_002.Value
    wovenfabricshader.links.new(wave_texture_002.outputs[0], math_002.inputs[0])
    # mix_006.Result -> mix_008.A
    wovenfabricshader.links.new(mix_006.outputs[2], mix_008.inputs[6])
    # mix_002.Result -> bump.Height
    wovenfabricshader.links.new(mix_002.outputs[2], bump.inputs[3])
    # math_003.Value -> math_002.Value
    wovenfabricshader.links.new(math_003.outputs[0], math_002.inputs[1])
    # reroute.Output -> noise_texture.Vector
    wovenfabricshader.links.new(reroute.outputs[0], noise_texture.inputs[0])
    # wave_texture_003.Color -> math_003.Value
    wovenfabricshader.links.new(wave_texture_003.outputs[0], math_003.inputs[1])
    # bump.Normal -> bump_001.Normal
    wovenfabricshader.links.new(bump.outputs[0], bump_001.inputs[4])
    # math.Value -> mix.A
    wovenfabricshader.links.new(math.outputs[0], mix.inputs[6])
    # math_007.Value -> math_006.Value
    wovenfabricshader.links.new(math_007.outputs[0], math_006.inputs[1])
    # math_002.Value -> mix.B
    wovenfabricshader.links.new(math_002.outputs[0], mix.inputs[7])
    # mix_008.Result -> principled_bsdf.Base Color
    wovenfabricshader.links.new(mix_008.outputs[2], principled_bsdf.inputs[0])
    # mapping_003.Vector -> wave_texture_004.Vector
    wovenfabricshader.links.new(mapping_003.outputs[0], wave_texture_004.inputs[0])
    # mix_003.Result -> reroute.Input
    wovenfabricshader.links.new(mix_003.outputs[2], reroute.inputs[0])
    # reroute.Output -> mapping_003.Vector
    wovenfabricshader.links.new(reroute.outputs[0], mapping_003.inputs[0])
    # math_002.Value -> mix_005.A
    wovenfabricshader.links.new(math_002.outputs[0], mix_005.inputs[6])
    # mapping_003.Vector -> wave_texture_005.Vector
    wovenfabricshader.links.new(mapping_003.outputs[0], wave_texture_005.inputs[0])
    # wave_texture_004.Color -> math_004.Value
    wovenfabricshader.links.new(wave_texture_004.outputs[0], math_004.inputs[0])
    # noise_texture_001.Color -> mix_003.B
    wovenfabricshader.links.new(noise_texture_001.outputs[1], mix_003.inputs[7])
    # math_005.Value -> math_004.Value
    wovenfabricshader.links.new(math_005.outputs[0], math_004.inputs[1])
    # mix_007.Result -> mix_008.B
    wovenfabricshader.links.new(mix_007.outputs[2], mix_008.inputs[7])
    # wave_texture_005.Color -> math_005.Value
    wovenfabricshader.links.new(wave_texture_005.outputs[0], math_005.inputs[1])
    # mapping_004.Vector -> wave_texture_006.Vector
    wovenfabricshader.links.new(mapping_004.outputs[0], wave_texture_006.inputs[0])
    # noise_texture.Fac -> bump_001.Height
    wovenfabricshader.links.new(noise_texture.outputs[0], bump_001.inputs[3])
    # mapping_001.Vector -> wave_texture.Vector
    wovenfabricshader.links.new(mapping_001.outputs[0], wave_texture.inputs[0])
    # mix_005.Result -> mix_007.Factor
    wovenfabricshader.links.new(mix_005.outputs[2], mix_007.inputs[0])
    # reroute.Output -> mapping_004.Vector
    wovenfabricshader.links.new(reroute.outputs[0], mapping_004.inputs[0])
    # math_006.Value -> mix_005.B
    wovenfabricshader.links.new(math_006.outputs[0], mix_005.inputs[7])
    # mapping.Vector -> noise_texture_001.Vector
    wovenfabricshader.links.new(mapping.outputs[0], noise_texture_001.inputs[0])
    # reroute.Output -> mapping_001.Vector
    wovenfabricshader.links.new(reroute.outputs[0], mapping_001.inputs[0])
    # wave_texture_006.Color -> math_006.Value
    wovenfabricshader.links.new(wave_texture_006.outputs[0], math_006.inputs[0])
    # mapping_001.Vector -> wave_texture_001.Vector
    wovenfabricshader.links.new(mapping_001.outputs[0], wave_texture_001.inputs[0])
    # math_004.Value -> mix_004.B
    wovenfabricshader.links.new(math_004.outputs[0], mix_004.inputs[7])
    # mapping_004.Vector -> wave_texture_007.Vector
    wovenfabricshader.links.new(mapping_004.outputs[0], wave_texture_007.inputs[0])
    # mapping.Vector -> mix_003.A
    wovenfabricshader.links.new(mapping.outputs[0], mix_003.inputs[6])
    # wave_texture.Color -> math.Value
    wovenfabricshader.links.new(wave_texture.outputs[0], math.inputs[0])
    # math.Value -> mix_004.A
    wovenfabricshader.links.new(math.outputs[0], mix_004.inputs[6])
    # wave_texture_007.Color -> math_007.Value
    wovenfabricshader.links.new(wave_texture_007.outputs[0], math_007.inputs[1])
    # mix_004.Result -> mix_006.Factor
    wovenfabricshader.links.new(mix_004.outputs[2], mix_006.inputs[0])
    # math_001.Value -> math.Value
    wovenfabricshader.links.new(math_001.outputs[0], math.inputs[1])
    # math_004.Value -> mix_001.A
    wovenfabricshader.links.new(math_004.outputs[0], mix_001.inputs[6])
    # wave_texture_001.Color -> math_001.Value
    wovenfabricshader.links.new(wave_texture_001.outputs[0], math_001.inputs[1])
    # math_006.Value -> mix_001.B
    wovenfabricshader.links.new(math_006.outputs[0], mix_001.inputs[7])
    # mapping_002.Vector -> wave_texture_002.Vector
    wovenfabricshader.links.new(mapping_002.outputs[0], wave_texture_002.inputs[0])
    # mix.Result -> mix_002.A
    wovenfabricshader.links.new(mix.outputs[2], mix_002.inputs[6])
    # reroute.Output -> mapping_002.Vector
    wovenfabricshader.links.new(reroute.outputs[0], mapping_002.inputs[0])
    # mix_001.Result -> mix_002.B
    wovenfabricshader.links.new(mix_001.outputs[2], mix_002.inputs[7])
    # group_input.Vector -> mapping.Vector
    wovenfabricshader.links.new(group_input.outputs[0], mapping.inputs[0])
    # principled_bsdf.BSDF -> group_output.Shader
    wovenfabricshader.links.new(principled_bsdf.outputs[0], group_output.inputs[0])
    # group_input.Scale -> mapping.Scale
    wovenfabricshader.links.new(group_input.outputs[1], mapping.inputs[3])
    # group_input.Weave Color 1 -> mix_006.B
    wovenfabricshader.links.new(group_input.outputs[2], mix_006.inputs[7])
    # group_input.Weave Color 2 -> mix_007.B
    wovenfabricshader.links.new(group_input.outputs[3], mix_007.inputs[7])
    # group_input.Roughness -> principled_bsdf.Roughness
    wovenfabricshader.links.new(group_input.outputs[4], principled_bsdf.inputs[2])
    # group_input.Sheen Weight -> principled_bsdf.Sheen Weight
    wovenfabricshader.links.new(group_input.outputs[5], principled_bsdf.inputs[24])
    # group_input.Sheen Roughness -> principled_bsdf.Sheen Roughness
    wovenfabricshader.links.new(group_input.outputs[6], principled_bsdf.inputs[25])
    # group_input.Sheen Tint -> principled_bsdf.Sheen Tint
    wovenfabricshader.links.new(group_input.outputs[7], principled_bsdf.inputs[26])
    # group_input.Weave Bump Strength -> bump.Strength
    wovenfabricshader.links.new(group_input.outputs[8], bump.inputs[0])
    # group_input.Noise Bump Strength -> bump_001.Strength
    wovenfabricshader.links.new(group_input.outputs[9], bump_001.inputs[0])

    return wovenfabricshader


wovenfabricshader = wovenfabricshader_node_group()

def woven_fabric_node_group():
    """Initialize Woven Fabric node group"""
    woven_fabric = mat.node_tree

    # Start with a clean node tree
    for node in woven_fabric.nodes:
        woven_fabric.nodes.remove(node)
    woven_fabric.color_tag = 'NONE'
    woven_fabric.description = ""
    woven_fabric.default_group_node_width = 140
    # woven_fabric interface

    # Initialize woven_fabric nodes

    # Node Material Output
    material_output = woven_fabric.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    # Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    # Thickness
    material_output.inputs[3].default_value = 0.0

    # Node Texture Coordinate
    texture_coordinate = woven_fabric.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False

    # Node Group
    group = woven_fabric.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = wovenfabricshader
    # Socket_2
    group.inputs[1].default_value = 1.5
    # Socket_3
    group.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
    # Socket_4
    group.inputs[3].default_value = (0.02144564688205719, 0.04039090499281883, 0.07594017684459686, 1.0)
    # Socket_5
    group.inputs[4].default_value = 1.0
    # Socket_6
    group.inputs[5].default_value = 1.0
    # Socket_7
    group.inputs[6].default_value = 0.3076336085796356
    # Socket_8
    group.inputs[7].default_value = (0.3532320261001587, 0.14208389818668365, 0.11482997238636017, 1.0)
    # Socket_9
    group.inputs[8].default_value = 0.4000000059604645
    # Socket_10
    group.inputs[9].default_value = 0.4000000059604645

    # Set locations
    material_output.location = (1478.1221923828125, -119.21959686279297)
    texture_coordinate.location = (971.8945922851562, -138.34617614746094)
    group.location = (1194.81884765625, -118.82130432128906)

    # Set dimensions
    material_output.width, material_output.height = 140.0, 100.0
    texture_coordinate.width, texture_coordinate.height = 140.0, 100.0
    group.width, group.height = 268.5595703125, 100.0

    # Initialize woven_fabric links

    # group.Shader -> material_output.Surface
    woven_fabric.links.new(group.outputs[0], material_output.inputs[0])
    # texture_coordinate.UV -> group.Vector
    woven_fabric.links.new(texture_coordinate.outputs[2], group.inputs[0])

    return woven_fabric


woven_fabric = woven_fabric_node_group()


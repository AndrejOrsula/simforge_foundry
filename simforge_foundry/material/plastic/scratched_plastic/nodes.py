import bpy, mathutils

mat = bpy.data.materials.new(name = "Plastic with Scratches")
mat.use_nodes = True
#initialize ScratchedPlasticShader node group
def scratchedplasticshader_node_group():

    scratchedplasticshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "ScratchedPlasticShader")

    scratchedplasticshader.color_tag = 'NONE'
    scratchedplasticshader.description = ""
    scratchedplasticshader.default_group_node_width = 140
    

    #scratchedplasticshader interface
    #Socket Shader
    shader_socket = scratchedplasticshader.interface.new_socket(name = "Shader", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    shader_socket.attribute_domain = 'POINT'
    shader_socket.default_input = 'VALUE'
    shader_socket.structure_type = 'AUTO'

    #Socket Scale
    scale_socket = scratchedplasticshader.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    #Socket Plastic Color
    plastic_color_socket = scratchedplasticshader.interface.new_socket(name = "Plastic Color", in_out='INPUT', socket_type = 'NodeSocketColor')
    plastic_color_socket.default_value = (0.029051000252366066, 0.07352200150489807, 0.26980099081993103, 1.0)
    plastic_color_socket.attribute_domain = 'POINT'
    plastic_color_socket.default_input = 'VALUE'
    plastic_color_socket.structure_type = 'AUTO'

    #Socket Subsurface
    subsurface_socket = scratchedplasticshader.interface.new_socket(name = "Subsurface", in_out='INPUT', socket_type = 'NodeSocketFloat')
    subsurface_socket.default_value = 0.20000000298023224
    subsurface_socket.min_value = 0.0
    subsurface_socket.max_value = 1.0
    subsurface_socket.subtype = 'FACTOR'
    subsurface_socket.attribute_domain = 'POINT'
    subsurface_socket.default_input = 'VALUE'
    subsurface_socket.structure_type = 'AUTO'

    #Socket Roughness
    roughness_socket = scratchedplasticshader.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = 'NONE'
    roughness_socket.attribute_domain = 'POINT'
    roughness_socket.default_input = 'VALUE'
    roughness_socket.structure_type = 'AUTO'

    #Socket Noise Roughness Scale
    noise_roughness_scale_socket = scratchedplasticshader.interface.new_socket(name = "Noise Roughness Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_roughness_scale_socket.default_value = 16.0
    noise_roughness_scale_socket.min_value = -1000.0
    noise_roughness_scale_socket.max_value = 1000.0
    noise_roughness_scale_socket.subtype = 'NONE'
    noise_roughness_scale_socket.attribute_domain = 'POINT'
    noise_roughness_scale_socket.default_input = 'VALUE'
    noise_roughness_scale_socket.structure_type = 'AUTO'

    #Socket Noise Roughness Detail
    noise_roughness_detail_socket = scratchedplasticshader.interface.new_socket(name = "Noise Roughness Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_roughness_detail_socket.default_value = 7.0
    noise_roughness_detail_socket.min_value = 0.0
    noise_roughness_detail_socket.max_value = 15.0
    noise_roughness_detail_socket.subtype = 'NONE'
    noise_roughness_detail_socket.attribute_domain = 'POINT'
    noise_roughness_detail_socket.default_input = 'VALUE'
    noise_roughness_detail_socket.structure_type = 'AUTO'

    #Socket Scratches Color
    scratches_color_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Color", in_out='INPUT', socket_type = 'NodeSocketColor')
    scratches_color_socket.default_value = (0.05230899900197983, 0.13902300596237183, 0.5322009921073914, 1.0)
    scratches_color_socket.attribute_domain = 'POINT'
    scratches_color_socket.default_input = 'VALUE'
    scratches_color_socket.structure_type = 'AUTO'

    #Socket Scratches Detail
    scratches_detail_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_detail_socket.default_value = 10.0
    scratches_detail_socket.min_value = 0.0
    scratches_detail_socket.max_value = 15.0
    scratches_detail_socket.subtype = 'NONE'
    scratches_detail_socket.attribute_domain = 'POINT'
    scratches_detail_socket.default_input = 'VALUE'
    scratches_detail_socket.structure_type = 'AUTO'

    #Socket Scratches Distortion
    scratches_distortion_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Distortion", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_distortion_socket.default_value = 0.12999999523162842
    scratches_distortion_socket.min_value = 0.0
    scratches_distortion_socket.max_value = 1.0
    scratches_distortion_socket.subtype = 'FACTOR'
    scratches_distortion_socket.attribute_domain = 'POINT'
    scratches_distortion_socket.default_input = 'VALUE'
    scratches_distortion_socket.structure_type = 'AUTO'

    #Socket Scratches Scale 1
    scratches_scale_1_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Scale 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_scale_1_socket.default_value = 3.0
    scratches_scale_1_socket.min_value = -1000.0
    scratches_scale_1_socket.max_value = 1000.0
    scratches_scale_1_socket.subtype = 'NONE'
    scratches_scale_1_socket.attribute_domain = 'POINT'
    scratches_scale_1_socket.default_input = 'VALUE'
    scratches_scale_1_socket.structure_type = 'AUTO'

    #Socket Scratches Thickness 1
    scratches_thickness_1_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Thickness 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_thickness_1_socket.default_value = 1.0
    scratches_thickness_1_socket.min_value = 0.0
    scratches_thickness_1_socket.max_value = 2.0
    scratches_thickness_1_socket.subtype = 'NONE'
    scratches_thickness_1_socket.attribute_domain = 'POINT'
    scratches_thickness_1_socket.default_input = 'VALUE'
    scratches_thickness_1_socket.structure_type = 'AUTO'

    #Socket Scratches Scale 2
    scratches_scale_2_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Scale 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_scale_2_socket.default_value = 5.0
    scratches_scale_2_socket.min_value = -1000.0
    scratches_scale_2_socket.max_value = 1000.0
    scratches_scale_2_socket.subtype = 'NONE'
    scratches_scale_2_socket.attribute_domain = 'POINT'
    scratches_scale_2_socket.default_input = 'VALUE'
    scratches_scale_2_socket.structure_type = 'AUTO'

    #Socket Scratches Thickness 2
    scratches_thickness_2_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Thickness 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_thickness_2_socket.default_value = 1.0
    scratches_thickness_2_socket.min_value = 0.0
    scratches_thickness_2_socket.max_value = 2.0
    scratches_thickness_2_socket.subtype = 'NONE'
    scratches_thickness_2_socket.attribute_domain = 'POINT'
    scratches_thickness_2_socket.default_input = 'VALUE'
    scratches_thickness_2_socket.structure_type = 'AUTO'

    #Socket Scratches Bump Strength
    scratches_bump_strength_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_bump_strength_socket.default_value = 0.20000000298023224
    scratches_bump_strength_socket.min_value = 0.0
    scratches_bump_strength_socket.max_value = 1.0
    scratches_bump_strength_socket.subtype = 'FACTOR'
    scratches_bump_strength_socket.attribute_domain = 'POINT'
    scratches_bump_strength_socket.default_input = 'VALUE'
    scratches_bump_strength_socket.structure_type = 'AUTO'

    #Socket Noise Bump Strength
    noise_bump_strength_socket = scratchedplasticshader.interface.new_socket(name = "Noise Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_strength_socket.default_value = 0.009999999776482582
    noise_bump_strength_socket.min_value = 0.0
    noise_bump_strength_socket.max_value = 1.0
    noise_bump_strength_socket.subtype = 'FACTOR'
    noise_bump_strength_socket.attribute_domain = 'POINT'
    noise_bump_strength_socket.default_input = 'VALUE'
    noise_bump_strength_socket.structure_type = 'AUTO'


    #initialize scratchedplasticshader nodes
    #node Group Output
    group_output = scratchedplasticshader.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = scratchedplasticshader.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Principled BSDF.001
    principled_bsdf_001 = scratchedplasticshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_001.name = "Principled BSDF.001"
    principled_bsdf_001.distribution = 'MULTI_GGX'
    principled_bsdf_001.subsurface_method = 'RANDOM_WALK'
    #Metallic
    principled_bsdf_001.inputs[1].default_value = 0.0
    #IOR
    principled_bsdf_001.inputs[3].default_value = 1.5
    #Alpha
    principled_bsdf_001.inputs[4].default_value = 1.0
    #Diffuse Roughness
    principled_bsdf_001.inputs[7].default_value = 0.0
    #Subsurface Radius
    principled_bsdf_001.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    #Subsurface Scale
    principled_bsdf_001.inputs[10].default_value = 0.05000000074505806
    #Subsurface Anisotropy
    principled_bsdf_001.inputs[12].default_value = 0.0
    #Specular IOR Level
    principled_bsdf_001.inputs[13].default_value = 0.5
    #Specular Tint
    principled_bsdf_001.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    #Anisotropic
    principled_bsdf_001.inputs[15].default_value = 0.0
    #Anisotropic Rotation
    principled_bsdf_001.inputs[16].default_value = 0.0
    #Tangent
    principled_bsdf_001.inputs[17].default_value = (0.0, 0.0, 0.0)
    #Transmission Weight
    principled_bsdf_001.inputs[18].default_value = 0.0
    #Coat Weight
    principled_bsdf_001.inputs[19].default_value = 0.0
    #Coat Roughness
    principled_bsdf_001.inputs[20].default_value = 0.029999999329447746
    #Coat IOR
    principled_bsdf_001.inputs[21].default_value = 1.5
    #Coat Tint
    principled_bsdf_001.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    #Coat Normal
    principled_bsdf_001.inputs[23].default_value = (0.0, 0.0, 0.0)
    #Sheen Weight
    principled_bsdf_001.inputs[24].default_value = 0.0
    #Sheen Roughness
    principled_bsdf_001.inputs[25].default_value = 0.5
    #Sheen Tint
    principled_bsdf_001.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    #Emission Color
    principled_bsdf_001.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    #Emission Strength
    principled_bsdf_001.inputs[28].default_value = 0.0
    #Thin Film Thickness
    principled_bsdf_001.inputs[29].default_value = 0.0
    #Thin Film IOR
    principled_bsdf_001.inputs[30].default_value = 1.3300000429153442

    #node Magic Texture.002
    magic_texture_002 = scratchedplasticshader.nodes.new("ShaderNodeTexMagic")
    magic_texture_002.name = "Magic Texture.002"
    magic_texture_002.turbulence_depth = 5
    #Distortion
    magic_texture_002.inputs[2].default_value = 3.0

    #node Mapping.001
    mapping_001 = scratchedplasticshader.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = 'POINT'
    #Location
    mapping_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Texture Coordinate.001
    texture_coordinate_001 = scratchedplasticshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_001.name = "Texture Coordinate.001"
    texture_coordinate_001.from_instancer = False

    #node Color Ramp.003
    color_ramp_003 = scratchedplasticshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_003.name = "Color Ramp.003"
    color_ramp_003.color_ramp.color_mode = 'RGB'
    color_ramp_003.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_003.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    color_ramp_003.color_ramp.elements.remove(color_ramp_003.color_ramp.elements[0])
    color_ramp_003_cre_0 = color_ramp_003.color_ramp.elements[0]
    color_ramp_003_cre_0.position = 0.012562813237309456
    color_ramp_003_cre_0.alpha = 1.0
    color_ramp_003_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_003_cre_1 = color_ramp_003.color_ramp.elements.new(0.04271365702152252)
    color_ramp_003_cre_1.alpha = 1.0
    color_ramp_003_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Mix.003
    mix_003 = scratchedplasticshader.nodes.new("ShaderNodeMix")
    mix_003.name = "Mix.003"
    mix_003.blend_type = 'LINEAR_LIGHT'
    mix_003.clamp_factor = True
    mix_003.clamp_result = False
    mix_003.data_type = 'RGBA'
    mix_003.factor_mode = 'UNIFORM'

    #node Noise Texture.002
    noise_texture_002 = scratchedplasticshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_002.name = "Noise Texture.002"
    noise_texture_002.noise_dimensions = '3D'
    noise_texture_002.noise_type = 'FBM'
    noise_texture_002.normalize = True
    #Scale
    noise_texture_002.inputs[2].default_value = 2.0
    #Roughness
    noise_texture_002.inputs[4].default_value = 0.5
    #Lacunarity
    noise_texture_002.inputs[5].default_value = 2.0
    #Distortion
    noise_texture_002.inputs[8].default_value = 0.0

    #node Frame.005
    frame_005 = scratchedplasticshader.nodes.new("NodeFrame")
    frame_005.name = "Frame.005"
    frame_005.label_size = 20
    frame_005.shrink = True

    #node Frame.006
    frame_006 = scratchedplasticshader.nodes.new("NodeFrame")
    frame_006.name = "Frame.006"
    frame_006.label_size = 20
    frame_006.shrink = True

    #node Frame.007
    frame_007 = scratchedplasticshader.nodes.new("NodeFrame")
    frame_007.name = "Frame.007"
    frame_007.label_size = 20
    frame_007.shrink = True

    #node Magic Texture.003
    magic_texture_003 = scratchedplasticshader.nodes.new("ShaderNodeTexMagic")
    magic_texture_003.name = "Magic Texture.003"
    magic_texture_003.turbulence_depth = 5
    #Distortion
    magic_texture_003.inputs[2].default_value = 3.0

    #node Color Ramp.004
    color_ramp_004 = scratchedplasticshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_004.name = "Color Ramp.004"
    color_ramp_004.color_ramp.color_mode = 'RGB'
    color_ramp_004.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_004.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    color_ramp_004.color_ramp.elements.remove(color_ramp_004.color_ramp.elements[0])
    color_ramp_004_cre_0 = color_ramp_004.color_ramp.elements[0]
    color_ramp_004_cre_0.position = 0.012562813237309456
    color_ramp_004_cre_0.alpha = 1.0
    color_ramp_004_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_004_cre_1 = color_ramp_004.color_ramp.elements.new(0.04271365702152252)
    color_ramp_004_cre_1.alpha = 1.0
    color_ramp_004_cre_1.color = (1.0, 1.0, 1.0, 1.0)


    #node Mix.004
    mix_004 = scratchedplasticshader.nodes.new("ShaderNodeMix")
    mix_004.name = "Mix.004"
    mix_004.blend_type = 'DARKEN'
    mix_004.clamp_factor = True
    mix_004.clamp_result = False
    mix_004.data_type = 'RGBA'
    mix_004.factor_mode = 'UNIFORM'
    #Factor_Float
    mix_004.inputs[0].default_value = 1.0

    #node Hue/Saturation/Value.003
    hue_saturation_value_003 = scratchedplasticshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_003.name = "Hue/Saturation/Value.003"
    #Hue
    hue_saturation_value_003.inputs[0].default_value = 0.5
    #Saturation
    hue_saturation_value_003.inputs[1].default_value = 1.0
    #Fac
    hue_saturation_value_003.inputs[3].default_value = 1.0

    #node Hue/Saturation/Value.004
    hue_saturation_value_004 = scratchedplasticshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_004.name = "Hue/Saturation/Value.004"
    #Hue
    hue_saturation_value_004.inputs[0].default_value = 0.5
    #Saturation
    hue_saturation_value_004.inputs[1].default_value = 1.0
    #Fac
    hue_saturation_value_004.inputs[3].default_value = 1.0

    #node Bump.002
    bump_002 = scratchedplasticshader.nodes.new("ShaderNodeBump")
    bump_002.name = "Bump.002"
    bump_002.invert = False
    #Distance
    bump_002.inputs[1].default_value = 1.0
    #Filter Width
    bump_002.inputs[2].default_value = 0.10000000149011612
    #Normal
    bump_002.inputs[4].default_value = (0.0, 0.0, 0.0)

    #node Mix.005
    mix_005 = scratchedplasticshader.nodes.new("ShaderNodeMix")
    mix_005.name = "Mix.005"
    mix_005.blend_type = 'MIX'
    mix_005.clamp_factor = True
    mix_005.clamp_result = False
    mix_005.data_type = 'RGBA'
    mix_005.factor_mode = 'UNIFORM'

    #node Hue/Saturation/Value.005
    hue_saturation_value_005 = scratchedplasticshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_005.name = "Hue/Saturation/Value.005"
    #Hue
    hue_saturation_value_005.inputs[0].default_value = 0.5
    #Saturation
    hue_saturation_value_005.inputs[1].default_value = 1.0
    #Fac
    hue_saturation_value_005.inputs[3].default_value = 1.0

    #node Noise Texture.003
    noise_texture_003 = scratchedplasticshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_003.name = "Noise Texture.003"
    noise_texture_003.noise_dimensions = '3D'
    noise_texture_003.noise_type = 'FBM'
    noise_texture_003.normalize = True
    #Roughness
    noise_texture_003.inputs[4].default_value = 0.5
    #Lacunarity
    noise_texture_003.inputs[5].default_value = 2.0
    #Distortion
    noise_texture_003.inputs[8].default_value = 0.0

    #node Reroute.001
    reroute_001 = scratchedplasticshader.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketVector"
    #node Color Ramp.005
    color_ramp_005 = scratchedplasticshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_005.name = "Color Ramp.005"
    color_ramp_005.color_ramp.color_mode = 'RGB'
    color_ramp_005.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_005.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    color_ramp_005.color_ramp.elements.remove(color_ramp_005.color_ramp.elements[0])
    color_ramp_005_cre_0 = color_ramp_005.color_ramp.elements[0]
    color_ramp_005_cre_0.position = 0.14572863280773163
    color_ramp_005_cre_0.alpha = 1.0
    color_ramp_005_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_005_cre_1 = color_ramp_005.color_ramp.elements.new(0.6909546852111816)
    color_ramp_005_cre_1.alpha = 1.0
    color_ramp_005_cre_1.color = (0.39339300990104675, 0.39339300990104675, 0.39339300990104675, 1.0)


    #node Frame.008
    frame_008 = scratchedplasticshader.nodes.new("NodeFrame")
    frame_008.name = "Frame.008"
    frame_008.label_size = 20
    frame_008.shrink = True

    #node Bump.003
    bump_003 = scratchedplasticshader.nodes.new("ShaderNodeBump")
    bump_003.name = "Bump.003"
    bump_003.invert = False
    #Distance
    bump_003.inputs[1].default_value = 1.0
    #Filter Width
    bump_003.inputs[2].default_value = 0.10000000149011612

    #node Frame.009
    frame_009 = scratchedplasticshader.nodes.new("NodeFrame")
    frame_009.name = "Frame.009"
    frame_009.label_size = 20
    frame_009.shrink = True


    #Set locations
    group_output.location = (0.0, 0.0)
    group_input.location = (0.0, 0.0)
    principled_bsdf_001.location = (0.0, 0.0)
    magic_texture_002.location = (0.0, 0.0)
    mapping_001.location = (0.0, 0.0)
    texture_coordinate_001.location = (0.0, 0.0)
    color_ramp_003.location = (0.0, 0.0)
    mix_003.location = (0.0, 0.0)
    noise_texture_002.location = (0.0, 0.0)
    frame_005.location = (0.0, 0.0)
    frame_006.location = (0.0, 0.0)
    frame_007.location = (0.0, 0.0)
    magic_texture_003.location = (0.0, 0.0)
    color_ramp_004.location = (0.0, 0.0)
    mix_004.location = (0.0, 0.0)
    hue_saturation_value_003.location = (0.0, 0.0)
    hue_saturation_value_004.location = (0.0, 0.0)
    bump_002.location = (0.0, 0.0)
    mix_005.location = (0.0, 0.0)
    hue_saturation_value_005.location = (0.0, 0.0)
    noise_texture_003.location = (0.0, 0.0)
    reroute_001.location = (0.0, 0.0)
    color_ramp_005.location = (0.0, 0.0)
    frame_008.location = (0.0, 0.0)
    bump_003.location = (0.0, 0.0)
    frame_009.location = (0.0, 0.0)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    principled_bsdf_001.width, principled_bsdf_001.height = 240.0, 100.0
    magic_texture_002.width, magic_texture_002.height = 140.0, 100.0
    mapping_001.width, mapping_001.height = 140.0, 100.0
    texture_coordinate_001.width, texture_coordinate_001.height = 140.0, 100.0
    color_ramp_003.width, color_ramp_003.height = 240.0, 100.0
    mix_003.width, mix_003.height = 140.0, 100.0
    noise_texture_002.width, noise_texture_002.height = 140.0, 100.0
    frame_005.width, frame_005.height = 150.0, 100.0
    frame_006.width, frame_006.height = 150.0, 100.0
    frame_007.width, frame_007.height = 150.0, 100.0
    magic_texture_003.width, magic_texture_003.height = 140.0, 100.0
    color_ramp_004.width, color_ramp_004.height = 240.0, 100.0
    mix_004.width, mix_004.height = 140.0, 100.0
    hue_saturation_value_003.width, hue_saturation_value_003.height = 150.0, 100.0
    hue_saturation_value_004.width, hue_saturation_value_004.height = 150.0, 100.0
    bump_002.width, bump_002.height = 140.0, 100.0
    mix_005.width, mix_005.height = 140.0, 100.0
    hue_saturation_value_005.width, hue_saturation_value_005.height = 150.0, 100.0
    noise_texture_003.width, noise_texture_003.height = 140.0, 100.0
    reroute_001.width, reroute_001.height = 140.0, 100.0
    color_ramp_005.width, color_ramp_005.height = 240.0, 100.0
    frame_008.width, frame_008.height = 150.0, 100.0
    bump_003.width, bump_003.height = 140.0, 100.0
    frame_009.width, frame_009.height = 150.0, 100.0

    #initialize scratchedplasticshader links
    #mapping_001.Vector -> mix_003.A
    scratchedplasticshader.links.new(mapping_001.outputs[0], mix_003.inputs[6])
    #mapping_001.Vector -> noise_texture_002.Vector
    scratchedplasticshader.links.new(mapping_001.outputs[0], noise_texture_002.inputs[0])
    #bump_002.Normal -> bump_003.Normal
    scratchedplasticshader.links.new(bump_002.outputs[0], bump_003.inputs[4])
    #mix_004.Result -> mix_005.Factor
    scratchedplasticshader.links.new(mix_004.outputs[2], mix_005.inputs[0])
    #noise_texture_003.Fac -> bump_003.Height
    scratchedplasticshader.links.new(noise_texture_003.outputs[0], bump_003.inputs[3])
    #noise_texture_002.Fac -> mix_003.B
    scratchedplasticshader.links.new(noise_texture_002.outputs[0], mix_003.inputs[7])
    #magic_texture_003.Color -> hue_saturation_value_004.Color
    scratchedplasticshader.links.new(magic_texture_003.outputs[0], hue_saturation_value_004.inputs[4])
    #bump_003.Normal -> principled_bsdf_001.Normal
    scratchedplasticshader.links.new(bump_003.outputs[0], principled_bsdf_001.inputs[5])
    #color_ramp_005.Color -> hue_saturation_value_005.Color
    scratchedplasticshader.links.new(color_ramp_005.outputs[0], hue_saturation_value_005.inputs[4])
    #mix_003.Result -> magic_texture_003.Vector
    scratchedplasticshader.links.new(mix_003.outputs[2], magic_texture_003.inputs[0])
    #hue_saturation_value_004.Color -> color_ramp_004.Fac
    scratchedplasticshader.links.new(hue_saturation_value_004.outputs[0], color_ramp_004.inputs[0])
    #mix_004.Result -> bump_002.Height
    scratchedplasticshader.links.new(mix_004.outputs[2], bump_002.inputs[3])
    #hue_saturation_value_005.Color -> principled_bsdf_001.Roughness
    scratchedplasticshader.links.new(hue_saturation_value_005.outputs[0], principled_bsdf_001.inputs[2])
    #color_ramp_003.Color -> mix_004.A
    scratchedplasticshader.links.new(color_ramp_003.outputs[0], mix_004.inputs[6])
    #mix_005.Result -> principled_bsdf_001.Base Color
    scratchedplasticshader.links.new(mix_005.outputs[2], principled_bsdf_001.inputs[0])
    #color_ramp_004.Color -> mix_004.B
    scratchedplasticshader.links.new(color_ramp_004.outputs[0], mix_004.inputs[7])
    #mix_003.Result -> magic_texture_002.Vector
    scratchedplasticshader.links.new(mix_003.outputs[2], magic_texture_002.inputs[0])
    #magic_texture_002.Color -> hue_saturation_value_003.Color
    scratchedplasticshader.links.new(magic_texture_002.outputs[0], hue_saturation_value_003.inputs[4])
    #noise_texture_003.Fac -> color_ramp_005.Fac
    scratchedplasticshader.links.new(noise_texture_003.outputs[0], color_ramp_005.inputs[0])
    #texture_coordinate_001.Object -> mapping_001.Vector
    scratchedplasticshader.links.new(texture_coordinate_001.outputs[3], mapping_001.inputs[0])
    #reroute_001.Output -> noise_texture_003.Vector
    scratchedplasticshader.links.new(reroute_001.outputs[0], noise_texture_003.inputs[0])
    #mapping_001.Vector -> reroute_001.Input
    scratchedplasticshader.links.new(mapping_001.outputs[0], reroute_001.inputs[0])
    #hue_saturation_value_003.Color -> color_ramp_003.Fac
    scratchedplasticshader.links.new(hue_saturation_value_003.outputs[0], color_ramp_003.inputs[0])
    #principled_bsdf_001.BSDF -> group_output.Shader
    scratchedplasticshader.links.new(principled_bsdf_001.outputs[0], group_output.inputs[0])
    #group_input.Scale -> mapping_001.Scale
    scratchedplasticshader.links.new(group_input.outputs[0], mapping_001.inputs[3])
    #group_input.Plastic Color -> mix_005.B
    scratchedplasticshader.links.new(group_input.outputs[1], mix_005.inputs[7])
    #group_input.Subsurface -> principled_bsdf_001.Subsurface Weight
    scratchedplasticshader.links.new(group_input.outputs[2], principled_bsdf_001.inputs[8])
    #group_input.Roughness -> hue_saturation_value_005.Value
    scratchedplasticshader.links.new(group_input.outputs[3], hue_saturation_value_005.inputs[2])
    #group_input.Noise Roughness Scale -> noise_texture_003.Scale
    scratchedplasticshader.links.new(group_input.outputs[4], noise_texture_003.inputs[2])
    #group_input.Noise Roughness Detail -> noise_texture_003.Detail
    scratchedplasticshader.links.new(group_input.outputs[5], noise_texture_003.inputs[3])
    #group_input.Scratches Color -> mix_005.A
    scratchedplasticshader.links.new(group_input.outputs[6], mix_005.inputs[6])
    #group_input.Scratches Detail -> noise_texture_002.Detail
    scratchedplasticshader.links.new(group_input.outputs[7], noise_texture_002.inputs[3])
    #group_input.Scratches Distortion -> mix_003.Factor
    scratchedplasticshader.links.new(group_input.outputs[8], mix_003.inputs[0])
    #group_input.Scratches Scale 1 -> magic_texture_002.Scale
    scratchedplasticshader.links.new(group_input.outputs[9], magic_texture_002.inputs[1])
    #group_input.Scratches Thickness 1 -> hue_saturation_value_003.Value
    scratchedplasticshader.links.new(group_input.outputs[10], hue_saturation_value_003.inputs[2])
    #group_input.Scratches Scale 2 -> magic_texture_003.Scale
    scratchedplasticshader.links.new(group_input.outputs[11], magic_texture_003.inputs[1])
    #group_input.Scratches Thickness 2 -> hue_saturation_value_004.Value
    scratchedplasticshader.links.new(group_input.outputs[12], hue_saturation_value_004.inputs[2])
    #group_input.Scratches Bump Strength -> bump_002.Strength
    scratchedplasticshader.links.new(group_input.outputs[13], bump_002.inputs[0])
    #group_input.Noise Bump Strength -> bump_003.Strength
    scratchedplasticshader.links.new(group_input.outputs[14], bump_003.inputs[0])
    return scratchedplasticshader

scratchedplasticshader = scratchedplasticshader_node_group()

#initialize Plastic with Scratches node group
def plastic_with_scratches_node_group():

    plastic_with_scratches = mat.node_tree
    #start with a clean node tree
    for node in plastic_with_scratches.nodes:
        plastic_with_scratches.nodes.remove(node)
    plastic_with_scratches.color_tag = 'NONE'
    plastic_with_scratches.description = ""
    plastic_with_scratches.default_group_node_width = 140
    

    #plastic_with_scratches interface

    #initialize plastic_with_scratches nodes
    #node Material Output.001
    material_output_001 = plastic_with_scratches.nodes.new("ShaderNodeOutputMaterial")
    material_output_001.name = "Material Output.001"
    material_output_001.is_active_output = True
    material_output_001.target = 'ALL'
    #Displacement
    material_output_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Thickness
    material_output_001.inputs[3].default_value = 0.0

    #node Group
    group = plastic_with_scratches.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = scratchedplasticshader
    #Socket_1
    group.inputs[0].default_value = 1.0
    #Socket_2
    group.inputs[1].default_value = (0.029051000252366066, 0.07352200150489807, 0.26980099081993103, 1.0)
    #Socket_3
    group.inputs[2].default_value = 0.20000000298023224
    #Socket_4
    group.inputs[3].default_value = 1.0
    #Socket_5
    group.inputs[4].default_value = 16.0
    #Socket_6
    group.inputs[5].default_value = 7.0
    #Socket_7
    group.inputs[6].default_value = (0.05230899900197983, 0.13902300596237183, 0.5322009921073914, 1.0)
    #Socket_8
    group.inputs[7].default_value = 10.0
    #Socket_9
    group.inputs[8].default_value = 0.12999999523162842
    #Socket_10
    group.inputs[9].default_value = 3.0
    #Socket_11
    group.inputs[10].default_value = 1.0
    #Socket_12
    group.inputs[11].default_value = 5.0
    #Socket_13
    group.inputs[12].default_value = 1.0
    #Socket_14
    group.inputs[13].default_value = 0.20000000298023224
    #Socket_15
    group.inputs[14].default_value = 0.009999999776482582


    #Set locations
    material_output_001.location = (0.0, 0.0)
    group.location = (0.0, 0.0)

    #Set dimensions
    material_output_001.width, material_output_001.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0

    #initialize plastic_with_scratches links
    #group.Shader -> material_output_001.Surface
    plastic_with_scratches.links.new(group.outputs[0], material_output_001.inputs[0])
    return plastic_with_scratches

plastic_with_scratches = plastic_with_scratches_node_group()


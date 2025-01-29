import bpy

mat = bpy.data.materials.new(name = "Plastic with Scratches")
mat.use_nodes = True

def scratchedplasticshader_node_group():
    scratchedplasticshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "ScratchedPlasticShader")
    scratchedplasticshader.color_tag = 'NONE'
    scratchedplasticshader.default_group_node_width = 140
    shader_socket = scratchedplasticshader.interface.new_socket(name = "Shader", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    shader_socket.attribute_domain = 'POINT'
    scale_socket = scratchedplasticshader.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    plastic_color_socket = scratchedplasticshader.interface.new_socket(name = "Plastic Color", in_out='INPUT', socket_type = 'NodeSocketColor')
    plastic_color_socket.default_value = (0.029051000252366066, 0.07352200150489807, 0.26980099081993103, 1.0)
    plastic_color_socket.attribute_domain = 'POINT'
    subsurface_socket = scratchedplasticshader.interface.new_socket(name = "Subsurface", in_out='INPUT', socket_type = 'NodeSocketFloat')
    subsurface_socket.default_value = 0.20000000298023224
    subsurface_socket.min_value = 0.0
    subsurface_socket.max_value = 1.0
    subsurface_socket.subtype = 'FACTOR'
    subsurface_socket.attribute_domain = 'POINT'
    roughness_socket = scratchedplasticshader.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = 'NONE'
    roughness_socket.attribute_domain = 'POINT'
    noise_roughness_scale_socket = scratchedplasticshader.interface.new_socket(name = "Noise Roughness Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_roughness_scale_socket.default_value = 16.0
    noise_roughness_scale_socket.min_value = -1000.0
    noise_roughness_scale_socket.max_value = 1000.0
    noise_roughness_scale_socket.subtype = 'NONE'
    noise_roughness_scale_socket.attribute_domain = 'POINT'
    noise_roughness_detail_socket = scratchedplasticshader.interface.new_socket(name = "Noise Roughness Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_roughness_detail_socket.default_value = 7.0
    noise_roughness_detail_socket.min_value = 0.0
    noise_roughness_detail_socket.max_value = 15.0
    noise_roughness_detail_socket.subtype = 'NONE'
    noise_roughness_detail_socket.attribute_domain = 'POINT'
    scratches_color_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Color", in_out='INPUT', socket_type = 'NodeSocketColor')
    scratches_color_socket.default_value = (0.05230899900197983, 0.13902300596237183, 0.5322009921073914, 1.0)
    scratches_color_socket.attribute_domain = 'POINT'
    scratches_detail_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_detail_socket.default_value = 10.0
    scratches_detail_socket.min_value = 0.0
    scratches_detail_socket.max_value = 15.0
    scratches_detail_socket.subtype = 'NONE'
    scratches_detail_socket.attribute_domain = 'POINT'
    scratches_distortion_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Distortion", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_distortion_socket.default_value = 0.12999999523162842
    scratches_distortion_socket.min_value = 0.0
    scratches_distortion_socket.max_value = 1.0
    scratches_distortion_socket.subtype = 'FACTOR'
    scratches_distortion_socket.attribute_domain = 'POINT'
    scratches_scale_1_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Scale 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_scale_1_socket.default_value = 3.0
    scratches_scale_1_socket.min_value = -1000.0
    scratches_scale_1_socket.max_value = 1000.0
    scratches_scale_1_socket.subtype = 'NONE'
    scratches_scale_1_socket.attribute_domain = 'POINT'
    scratches_thickness_1_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Thickness 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_thickness_1_socket.default_value = 1.0
    scratches_thickness_1_socket.min_value = 0.0
    scratches_thickness_1_socket.max_value = 2.0
    scratches_thickness_1_socket.subtype = 'NONE'
    scratches_thickness_1_socket.attribute_domain = 'POINT'
    scratches_scale_2_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Scale 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_scale_2_socket.default_value = 5.0
    scratches_scale_2_socket.min_value = -1000.0
    scratches_scale_2_socket.max_value = 1000.0
    scratches_scale_2_socket.subtype = 'NONE'
    scratches_scale_2_socket.attribute_domain = 'POINT'
    scratches_thickness_2_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Thickness 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_thickness_2_socket.default_value = 1.0
    scratches_thickness_2_socket.min_value = 0.0
    scratches_thickness_2_socket.max_value = 2.0
    scratches_thickness_2_socket.subtype = 'NONE'
    scratches_thickness_2_socket.attribute_domain = 'POINT'
    scratches_bump_strength_socket = scratchedplasticshader.interface.new_socket(name = "Scratches Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scratches_bump_strength_socket.default_value = 0.20000000298023224
    scratches_bump_strength_socket.min_value = 0.0
    scratches_bump_strength_socket.max_value = 1.0
    scratches_bump_strength_socket.subtype = 'FACTOR'
    scratches_bump_strength_socket.attribute_domain = 'POINT'
    noise_bump_strength_socket = scratchedplasticshader.interface.new_socket(name = "Noise Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    noise_bump_strength_socket.default_value = 0.009999999776482582
    noise_bump_strength_socket.min_value = 0.0
    noise_bump_strength_socket.max_value = 1.0
    noise_bump_strength_socket.subtype = 'FACTOR'
    noise_bump_strength_socket.attribute_domain = 'POINT'
    group_output = scratchedplasticshader.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    group_input = scratchedplasticshader.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    principled_bsdf_001 = scratchedplasticshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf_001.name = "Principled BSDF.001"
    principled_bsdf_001.distribution = 'MULTI_GGX'
    principled_bsdf_001.subsurface_method = 'RANDOM_WALK'
    principled_bsdf_001.inputs[1].default_value = 0.0
    principled_bsdf_001.inputs[3].default_value = 1.5
    principled_bsdf_001.inputs[4].default_value = 1.0
    principled_bsdf_001.inputs[7].default_value = 0.0
    principled_bsdf_001.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    principled_bsdf_001.inputs[10].default_value = 0.05000000074505806
    principled_bsdf_001.inputs[12].default_value = 0.0
    principled_bsdf_001.inputs[13].default_value = 0.5
    principled_bsdf_001.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_001.inputs[15].default_value = 0.0
    principled_bsdf_001.inputs[16].default_value = 0.0
    principled_bsdf_001.inputs[17].default_value = (0.0, 0.0, 0.0)
    principled_bsdf_001.inputs[18].default_value = 0.0
    principled_bsdf_001.inputs[19].default_value = 0.0
    principled_bsdf_001.inputs[20].default_value = 0.029999999329447746
    principled_bsdf_001.inputs[21].default_value = 1.5
    principled_bsdf_001.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_001.inputs[23].default_value = (0.0, 0.0, 0.0)
    principled_bsdf_001.inputs[24].default_value = 0.0
    principled_bsdf_001.inputs[25].default_value = 0.5
    principled_bsdf_001.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_001.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf_001.inputs[28].default_value = 0.0
    principled_bsdf_001.inputs[29].default_value = 0.0
    principled_bsdf_001.inputs[30].default_value = 1.3300000429153442
    magic_texture_002 = scratchedplasticshader.nodes.new("ShaderNodeTexMagic")
    magic_texture_002.name = "Magic Texture.002"
    magic_texture_002.turbulence_depth = 5
    magic_texture_002.inputs[2].default_value = 3.0
    mapping_001 = scratchedplasticshader.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = 'POINT'
    mapping_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    texture_coordinate_001 = scratchedplasticshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate_001.name = "Texture Coordinate.001"
    texture_coordinate_001.from_instancer = False
    color_ramp_003 = scratchedplasticshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_003.name = "Color Ramp.003"
    color_ramp_003.color_ramp.color_mode = 'RGB'
    color_ramp_003.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_003.color_ramp.interpolation = 'LINEAR'
    color_ramp_003.color_ramp.elements.remove(color_ramp_003.color_ramp.elements[0])
    color_ramp_003_cre_0 = color_ramp_003.color_ramp.elements[0]
    color_ramp_003_cre_0.position = 0.012562813237309456
    color_ramp_003_cre_0.alpha = 1.0
    color_ramp_003_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_003_cre_1 = color_ramp_003.color_ramp.elements.new(0.04271365702152252)
    color_ramp_003_cre_1.alpha = 1.0
    color_ramp_003_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    mix_003 = scratchedplasticshader.nodes.new("ShaderNodeMix")
    mix_003.name = "Mix.003"
    mix_003.blend_type = 'LINEAR_LIGHT'
    mix_003.clamp_factor = True
    mix_003.clamp_result = False
    mix_003.data_type = 'RGBA'
    mix_003.factor_mode = 'UNIFORM'
    noise_texture_002 = scratchedplasticshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_002.name = "Noise Texture.002"
    noise_texture_002.noise_dimensions = '3D'
    noise_texture_002.noise_type = 'FBM'
    noise_texture_002.normalize = True
    noise_texture_002.inputs[2].default_value = 2.0
    noise_texture_002.inputs[4].default_value = 0.5
    noise_texture_002.inputs[5].default_value = 2.0
    noise_texture_002.inputs[8].default_value = 0.0
    frame_005 = scratchedplasticshader.nodes.new("NodeFrame")
    frame_005.name = "Frame.005"
    frame_006 = scratchedplasticshader.nodes.new("NodeFrame")
    frame_006.name = "Frame.006"
    frame_007 = scratchedplasticshader.nodes.new("NodeFrame")
    frame_007.name = "Frame.007"
    magic_texture_003 = scratchedplasticshader.nodes.new("ShaderNodeTexMagic")
    magic_texture_003.name = "Magic Texture.003"
    magic_texture_003.turbulence_depth = 5
    magic_texture_003.inputs[2].default_value = 3.0
    color_ramp_004 = scratchedplasticshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_004.name = "Color Ramp.004"
    color_ramp_004.color_ramp.color_mode = 'RGB'
    color_ramp_004.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_004.color_ramp.interpolation = 'LINEAR'
    color_ramp_004.color_ramp.elements.remove(color_ramp_004.color_ramp.elements[0])
    color_ramp_004_cre_0 = color_ramp_004.color_ramp.elements[0]
    color_ramp_004_cre_0.position = 0.012562813237309456
    color_ramp_004_cre_0.alpha = 1.0
    color_ramp_004_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_004_cre_1 = color_ramp_004.color_ramp.elements.new(0.04271365702152252)
    color_ramp_004_cre_1.alpha = 1.0
    color_ramp_004_cre_1.color = (1.0, 1.0, 1.0, 1.0)
    mix_004 = scratchedplasticshader.nodes.new("ShaderNodeMix")
    mix_004.name = "Mix.004"
    mix_004.blend_type = 'DARKEN'
    mix_004.clamp_factor = True
    mix_004.clamp_result = False
    mix_004.data_type = 'RGBA'
    mix_004.factor_mode = 'UNIFORM'
    mix_004.inputs[0].default_value = 1.0
    hue_saturation_value_003 = scratchedplasticshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_003.name = "Hue/Saturation/Value.003"
    hue_saturation_value_003.inputs[0].default_value = 0.5
    hue_saturation_value_003.inputs[1].default_value = 1.0
    hue_saturation_value_003.inputs[3].default_value = 1.0
    hue_saturation_value_004 = scratchedplasticshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_004.name = "Hue/Saturation/Value.004"
    hue_saturation_value_004.inputs[0].default_value = 0.5
    hue_saturation_value_004.inputs[1].default_value = 1.0
    hue_saturation_value_004.inputs[3].default_value = 1.0
    bump_002 = scratchedplasticshader.nodes.new("ShaderNodeBump")
    bump_002.name = "Bump.002"
    bump_002.invert = False
    bump_002.inputs[1].default_value = 1.0
    bump_002.inputs[3].default_value = (0.0, 0.0, 0.0)
    mix_005 = scratchedplasticshader.nodes.new("ShaderNodeMix")
    mix_005.name = "Mix.005"
    mix_005.blend_type = 'MIX'
    mix_005.clamp_factor = True
    mix_005.clamp_result = False
    mix_005.data_type = 'RGBA'
    mix_005.factor_mode = 'UNIFORM'
    hue_saturation_value_005 = scratchedplasticshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value_005.name = "Hue/Saturation/Value.005"
    hue_saturation_value_005.inputs[0].default_value = 0.5
    hue_saturation_value_005.inputs[1].default_value = 1.0
    hue_saturation_value_005.inputs[3].default_value = 1.0
    noise_texture_003 = scratchedplasticshader.nodes.new("ShaderNodeTexNoise")
    noise_texture_003.name = "Noise Texture.003"
    noise_texture_003.noise_dimensions = '3D'
    noise_texture_003.noise_type = 'FBM'
    noise_texture_003.normalize = True
    noise_texture_003.inputs[4].default_value = 0.5
    noise_texture_003.inputs[5].default_value = 2.0
    noise_texture_003.inputs[8].default_value = 0.0
    reroute_001 = scratchedplasticshader.nodes.new("NodeReroute")
    reroute_001.name = "Reroute.001"
    reroute_001.socket_idname = "NodeSocketVector"
    color_ramp_005 = scratchedplasticshader.nodes.new("ShaderNodeValToRGB")
    color_ramp_005.name = "Color Ramp.005"
    color_ramp_005.color_ramp.color_mode = 'RGB'
    color_ramp_005.color_ramp.hue_interpolation = 'NEAR'
    color_ramp_005.color_ramp.interpolation = 'LINEAR'
    color_ramp_005.color_ramp.elements.remove(color_ramp_005.color_ramp.elements[0])
    color_ramp_005_cre_0 = color_ramp_005.color_ramp.elements[0]
    color_ramp_005_cre_0.position = 0.14572863280773163
    color_ramp_005_cre_0.alpha = 1.0
    color_ramp_005_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    color_ramp_005_cre_1 = color_ramp_005.color_ramp.elements.new(0.6909546852111816)
    color_ramp_005_cre_1.alpha = 1.0
    color_ramp_005_cre_1.color = (0.39339300990104675, 0.39339300990104675, 0.39339300990104675, 1.0)
    frame_008 = scratchedplasticshader.nodes.new("NodeFrame")
    frame_008.name = "Frame.008"
    bump_003 = scratchedplasticshader.nodes.new("ShaderNodeBump")
    bump_003.name = "Bump.003"
    bump_003.invert = False
    bump_003.inputs[1].default_value = 1.0
    frame_009 = scratchedplasticshader.nodes.new("NodeFrame")
    frame_009.name = "Frame.009"
    scratchedplasticshader.links.new(mapping_001.outputs[0], mix_003.inputs[6])
    scratchedplasticshader.links.new(mapping_001.outputs[0], noise_texture_002.inputs[0])
    scratchedplasticshader.links.new(bump_002.outputs[0], bump_003.inputs[3])
    scratchedplasticshader.links.new(mix_004.outputs[2], mix_005.inputs[0])
    scratchedplasticshader.links.new(noise_texture_003.outputs[0], bump_003.inputs[2])
    scratchedplasticshader.links.new(noise_texture_002.outputs[0], mix_003.inputs[7])
    scratchedplasticshader.links.new(magic_texture_003.outputs[0], hue_saturation_value_004.inputs[4])
    scratchedplasticshader.links.new(bump_003.outputs[0], principled_bsdf_001.inputs[5])
    scratchedplasticshader.links.new(color_ramp_005.outputs[0], hue_saturation_value_005.inputs[4])
    scratchedplasticshader.links.new(mix_003.outputs[2], magic_texture_003.inputs[0])
    scratchedplasticshader.links.new(hue_saturation_value_004.outputs[0], color_ramp_004.inputs[0])
    scratchedplasticshader.links.new(mix_004.outputs[2], bump_002.inputs[2])
    scratchedplasticshader.links.new(hue_saturation_value_005.outputs[0], principled_bsdf_001.inputs[2])
    scratchedplasticshader.links.new(color_ramp_003.outputs[0], mix_004.inputs[6])
    scratchedplasticshader.links.new(mix_005.outputs[2], principled_bsdf_001.inputs[0])
    scratchedplasticshader.links.new(color_ramp_004.outputs[0], mix_004.inputs[7])
    scratchedplasticshader.links.new(mix_003.outputs[2], magic_texture_002.inputs[0])
    scratchedplasticshader.links.new(magic_texture_002.outputs[0], hue_saturation_value_003.inputs[4])
    scratchedplasticshader.links.new(noise_texture_003.outputs[0], color_ramp_005.inputs[0])
    scratchedplasticshader.links.new(texture_coordinate_001.outputs[3], mapping_001.inputs[0])
    scratchedplasticshader.links.new(reroute_001.outputs[0], noise_texture_003.inputs[0])
    scratchedplasticshader.links.new(mapping_001.outputs[0], reroute_001.inputs[0])
    scratchedplasticshader.links.new(hue_saturation_value_003.outputs[0], color_ramp_003.inputs[0])
    scratchedplasticshader.links.new(principled_bsdf_001.outputs[0], group_output.inputs[0])
    scratchedplasticshader.links.new(group_input.outputs[0], mapping_001.inputs[3])
    scratchedplasticshader.links.new(group_input.outputs[1], mix_005.inputs[7])
    scratchedplasticshader.links.new(group_input.outputs[2], principled_bsdf_001.inputs[8])
    scratchedplasticshader.links.new(group_input.outputs[3], hue_saturation_value_005.inputs[2])
    scratchedplasticshader.links.new(group_input.outputs[4], noise_texture_003.inputs[2])
    scratchedplasticshader.links.new(group_input.outputs[5], noise_texture_003.inputs[3])
    scratchedplasticshader.links.new(group_input.outputs[6], mix_005.inputs[6])
    scratchedplasticshader.links.new(group_input.outputs[7], noise_texture_002.inputs[3])
    scratchedplasticshader.links.new(group_input.outputs[8], mix_003.inputs[0])
    scratchedplasticshader.links.new(group_input.outputs[9], magic_texture_002.inputs[1])
    scratchedplasticshader.links.new(group_input.outputs[10], hue_saturation_value_003.inputs[2])
    scratchedplasticshader.links.new(group_input.outputs[11], magic_texture_003.inputs[1])
    scratchedplasticshader.links.new(group_input.outputs[12], hue_saturation_value_004.inputs[2])
    scratchedplasticshader.links.new(group_input.outputs[13], bump_002.inputs[0])
    scratchedplasticshader.links.new(group_input.outputs[14], bump_003.inputs[0])
    return scratchedplasticshader

scratchedplasticshader = scratchedplasticshader_node_group()

def plastic_with_scratches_node_group():
    plastic_with_scratches = mat.node_tree
    for node in plastic_with_scratches.nodes:
        plastic_with_scratches.nodes.remove(node)
    plastic_with_scratches.color_tag = 'NONE'
    plastic_with_scratches.default_group_node_width = 140
    material_output_001 = plastic_with_scratches.nodes.new("ShaderNodeOutputMaterial")
    material_output_001.name = "Material Output.001"
    material_output_001.is_active_output = True
    material_output_001.target = 'ALL'
    material_output_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    material_output_001.inputs[3].default_value = 0.0
    group = plastic_with_scratches.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = scratchedplasticshader
    group.inputs[0].default_value = 1.0
    group.inputs[1].default_value = (0.029051000252366066, 0.07352200150489807, 0.26980099081993103, 1.0)
    group.inputs[2].default_value = 0.20000000298023224
    group.inputs[3].default_value = 1.0
    group.inputs[4].default_value = 16.0
    group.inputs[5].default_value = 7.0
    group.inputs[6].default_value = (0.05230899900197983, 0.13902300596237183, 0.5322009921073914, 1.0)
    group.inputs[7].default_value = 10.0
    group.inputs[8].default_value = 0.12999999523162842
    group.inputs[9].default_value = 3.0
    group.inputs[10].default_value = 1.0
    group.inputs[11].default_value = 5.0
    group.inputs[12].default_value = 1.0
    group.inputs[13].default_value = 0.20000000298023224
    group.inputs[14].default_value = 0.009999999776482582
    plastic_with_scratches.links.new(group.outputs[0], material_output_001.inputs[0])
    return plastic_with_scratches

plastic_with_scratches = plastic_with_scratches_node_group()


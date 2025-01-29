import bpy

mat = bpy.data.materials.new(name = "Brushed Chrome")
mat.use_nodes = True

def brushedchrome_node_group():
    brushedchrome = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "BrushedChrome")
    brushedchrome.color_tag = 'NONE'
    brushedchrome.default_group_node_width = 140
    shader_socket = brushedchrome.interface.new_socket(name = "Shader", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    shader_socket.attribute_domain = 'POINT'
    scale_socket = brushedchrome.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    base_color_socket = brushedchrome.interface.new_socket(name = "Base Color", in_out='INPUT', socket_type = 'NodeSocketColor')
    base_color_socket.default_value = (0.2199402153491974, 0.2199402153491974, 0.2199402153491974, 1.0)
    base_color_socket.attribute_domain = 'POINT'
    metallic_socket = brushedchrome.interface.new_socket(name = "Metallic", in_out='INPUT', socket_type = 'NodeSocketFloat')
    metallic_socket.default_value = 1.0
    metallic_socket.min_value = 0.0
    metallic_socket.max_value = 1.0
    metallic_socket.subtype = 'FACTOR'
    metallic_socket.attribute_domain = 'POINT'
    detail_1_socket = brushedchrome.interface.new_socket(name = "Detail 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detail_1_socket.default_value = 15.0
    detail_1_socket.min_value = 0.0
    detail_1_socket.max_value = 15.0
    detail_1_socket.subtype = 'NONE'
    detail_1_socket.attribute_domain = 'POINT'
    detail_2_socket = brushedchrome.interface.new_socket(name = "Detail 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detail_2_socket.default_value = 0.5
    detail_2_socket.min_value = 0.0
    detail_2_socket.max_value = 1.0
    detail_2_socket.subtype = 'FACTOR'
    detail_2_socket.attribute_domain = 'POINT'
    roughness_socket = brushedchrome.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = 'NONE'
    roughness_socket.attribute_domain = 'POINT'
    bump_strength_socket = brushedchrome.interface.new_socket(name = "Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    bump_strength_socket.default_value = 0.009999999776482582
    bump_strength_socket.min_value = 0.0
    bump_strength_socket.max_value = 1.0
    bump_strength_socket.subtype = 'FACTOR'
    bump_strength_socket.attribute_domain = 'POINT'
    rotation_socket = brushedchrome.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketVector')
    rotation_socket.default_value = (0.0, 0.0, 0.0)
    rotation_socket.min_value = -3.4028234663852886e+38
    rotation_socket.max_value = 3.4028234663852886e+38
    rotation_socket.subtype = 'EULER'
    rotation_socket.attribute_domain = 'POINT'
    clear_coat_weight_socket = brushedchrome.interface.new_socket(name = "Clear Coat Weight", in_out='INPUT', socket_type = 'NodeSocketFloat')
    clear_coat_weight_socket.default_value = 1.0
    clear_coat_weight_socket.min_value = 0.0
    clear_coat_weight_socket.max_value = 1.0
    clear_coat_weight_socket.subtype = 'FACTOR'
    clear_coat_weight_socket.attribute_domain = 'POINT'
    clear_coat_roughness_socket = brushedchrome.interface.new_socket(name = "Clear Coat Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    clear_coat_roughness_socket.default_value = 0.10000000149011612
    clear_coat_roughness_socket.min_value = 0.0
    clear_coat_roughness_socket.max_value = 1.0
    clear_coat_roughness_socket.subtype = 'FACTOR'
    clear_coat_roughness_socket.attribute_domain = 'POINT'
    clear_coat_tint_socket = brushedchrome.interface.new_socket(name = "Clear Coat Tint", in_out='INPUT', socket_type = 'NodeSocketColor')
    clear_coat_tint_socket.default_value = (1.0, 1.0, 1.0, 1.0)
    clear_coat_tint_socket.attribute_domain = 'POINT'
    group_output = brushedchrome.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    group_input = brushedchrome.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    noise_texture = brushedchrome.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    noise_texture.inputs[2].default_value = 15.0
    noise_texture.inputs[5].default_value = 2.0
    noise_texture.inputs[8].default_value = 0.0
    mapping = brushedchrome.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = 'POINT'
    mapping.inputs[1].default_value = (0.0, 0.0, 0.0)
    colorramp = brushedchrome.nodes.new("ShaderNodeValToRGB")
    colorramp.name = "ColorRamp"
    colorramp.color_ramp.color_mode = 'RGB'
    colorramp.color_ramp.hue_interpolation = 'NEAR'
    colorramp.color_ramp.interpolation = 'LINEAR'
    colorramp.color_ramp.elements.remove(colorramp.color_ramp.elements[0])
    colorramp_cre_0 = colorramp.color_ramp.elements[0]
    colorramp_cre_0.position = 0.16183581948280334
    colorramp_cre_0.alpha = 1.0
    colorramp_cre_0.color = (0.12864121794700623, 0.12864121794700623, 0.12864121794700623, 1.0)
    colorramp_cre_1 = colorramp.color_ramp.elements.new(0.7681161761283875)
    colorramp_cre_1.alpha = 1.0
    colorramp_cre_1.color = (0.40373504161834717, 0.40373504161834717, 0.40373504161834717, 1.0)
    texture_coordinate = brushedchrome.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False
    principled_bsdf = brushedchrome.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK_SKIN'
    principled_bsdf.inputs[3].default_value = 1.4500000476837158
    principled_bsdf.inputs[4].default_value = 1.0
    principled_bsdf.inputs[5].default_value = (0.0, 0.0, 0.0)
    principled_bsdf.inputs[7].default_value = 0.0
    principled_bsdf.inputs[8].default_value = 0.0
    principled_bsdf.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    principled_bsdf.inputs[10].default_value = 0.05000000074505806
    principled_bsdf.inputs[11].default_value = 1.399999976158142
    principled_bsdf.inputs[12].default_value = 0.0
    principled_bsdf.inputs[13].default_value = 0.5
    principled_bsdf.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf.inputs[15].default_value = 0.0
    principled_bsdf.inputs[16].default_value = 0.0
    principled_bsdf.inputs[17].default_value = (0.0, 0.0, 0.0)
    principled_bsdf.inputs[18].default_value = 0.0
    principled_bsdf.inputs[21].default_value = 1.5
    principled_bsdf.inputs[24].default_value = 0.0
    principled_bsdf.inputs[25].default_value = 0.5
    principled_bsdf.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf.inputs[27].default_value = (0.0, 0.0, 0.0, 1.0)
    principled_bsdf.inputs[28].default_value = 1.0
    principled_bsdf.inputs[29].default_value = 0.0
    principled_bsdf.inputs[30].default_value = 1.3300000429153442
    mapping_001 = brushedchrome.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = 'POINT'
    mapping_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    mapping_001.inputs[3].default_value = (80.0, 1.0, 1.0)
    hue_saturation_value = brushedchrome.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    hue_saturation_value.inputs[0].default_value = 0.5
    hue_saturation_value.inputs[1].default_value = 1.0
    hue_saturation_value.inputs[3].default_value = 1.0
    bump = brushedchrome.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    bump.inputs[1].default_value = 1.0
    bump.inputs[3].default_value = (0.0, 0.0, 0.0)
    brushedchrome.links.new(mapping_001.outputs[0], noise_texture.inputs[0])
    brushedchrome.links.new(bump.outputs[0], principled_bsdf.inputs[23])
    brushedchrome.links.new(noise_texture.outputs[1], bump.inputs[2])
    brushedchrome.links.new(mapping.outputs[0], mapping_001.inputs[0])
    brushedchrome.links.new(noise_texture.outputs[0], colorramp.inputs[0])
    brushedchrome.links.new(hue_saturation_value.outputs[0], principled_bsdf.inputs[2])
    brushedchrome.links.new(colorramp.outputs[0], hue_saturation_value.inputs[4])
    brushedchrome.links.new(principled_bsdf.outputs[0], group_output.inputs[0])
    brushedchrome.links.new(group_input.outputs[0], mapping.inputs[3])
    brushedchrome.links.new(group_input.outputs[7], mapping.inputs[2])
    brushedchrome.links.new(group_input.outputs[5], hue_saturation_value.inputs[2])
    brushedchrome.links.new(group_input.outputs[1], principled_bsdf.inputs[0])
    brushedchrome.links.new(group_input.outputs[2], principled_bsdf.inputs[1])
    brushedchrome.links.new(group_input.outputs[6], bump.inputs[0])
    brushedchrome.links.new(group_input.outputs[8], principled_bsdf.inputs[19])
    brushedchrome.links.new(group_input.outputs[9], principled_bsdf.inputs[20])
    brushedchrome.links.new(group_input.outputs[10], principled_bsdf.inputs[22])
    brushedchrome.links.new(group_input.outputs[3], noise_texture.inputs[3])
    brushedchrome.links.new(group_input.outputs[4], noise_texture.inputs[4])
    brushedchrome.links.new(texture_coordinate.outputs[3], mapping.inputs[0])
    return brushedchrome

brushedchrome = brushedchrome_node_group()

def brushed_chrome_node_group():
    brushed_chrome = mat.node_tree
    for node in brushed_chrome.nodes:
        brushed_chrome.nodes.remove(node)
    brushed_chrome.color_tag = 'NONE'
    brushed_chrome.default_group_node_width = 140
    material_output = brushed_chrome.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    material_output.inputs[3].default_value = 0.0
    group = brushed_chrome.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = brushedchrome
    group.inputs[0].default_value = 1.0
    group.inputs[1].default_value = (0.2199402153491974, 0.2199402153491974, 0.2199402153491974, 1.0)
    group.inputs[2].default_value = 1.0
    group.inputs[3].default_value = 15.0
    group.inputs[4].default_value = 0.5
    group.inputs[5].default_value = 1.0
    group.inputs[6].default_value = 0.009999999776482582
    group.inputs[7].default_value = (0.0, 0.0, 0.0)
    group.inputs[8].default_value = 1.0
    group.inputs[9].default_value = 0.10000000149011612
    group.inputs[10].default_value = (1.0, 1.0, 1.0, 1.0)
    brushed_chrome.links.new(group.outputs[0], material_output.inputs[0])
    return brushed_chrome

brushed_chrome = brushed_chrome_node_group()


import bpy, mathutils

mat = bpy.data.materials.new(name = "Brushed Chrome")
mat.use_nodes = True
#initialize BrushedChrome node group
def brushedchrome_node_group():

    brushedchrome = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "BrushedChrome")

    brushedchrome.color_tag = 'NONE'
    brushedchrome.description = ""
    brushedchrome.default_group_node_width = 140
    

    #brushedchrome interface
    #Socket Shader
    shader_socket = brushedchrome.interface.new_socket(name = "Shader", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    shader_socket.attribute_domain = 'POINT'
    shader_socket.default_input = 'VALUE'
    shader_socket.structure_type = 'AUTO'

    #Socket Scale
    scale_socket = brushedchrome.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    #Socket Base Color
    base_color_socket = brushedchrome.interface.new_socket(name = "Base Color", in_out='INPUT', socket_type = 'NodeSocketColor')
    base_color_socket.default_value = (0.2199402153491974, 0.2199402153491974, 0.2199402153491974, 1.0)
    base_color_socket.attribute_domain = 'POINT'
    base_color_socket.default_input = 'VALUE'
    base_color_socket.structure_type = 'AUTO'

    #Socket Metallic
    metallic_socket = brushedchrome.interface.new_socket(name = "Metallic", in_out='INPUT', socket_type = 'NodeSocketFloat')
    metallic_socket.default_value = 1.0
    metallic_socket.min_value = 0.0
    metallic_socket.max_value = 1.0
    metallic_socket.subtype = 'FACTOR'
    metallic_socket.attribute_domain = 'POINT'
    metallic_socket.default_input = 'VALUE'
    metallic_socket.structure_type = 'AUTO'

    #Socket Detail 1
    detail_1_socket = brushedchrome.interface.new_socket(name = "Detail 1", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detail_1_socket.default_value = 15.0
    detail_1_socket.min_value = 0.0
    detail_1_socket.max_value = 15.0
    detail_1_socket.subtype = 'NONE'
    detail_1_socket.attribute_domain = 'POINT'
    detail_1_socket.default_input = 'VALUE'
    detail_1_socket.structure_type = 'AUTO'

    #Socket Detail 2
    detail_2_socket = brushedchrome.interface.new_socket(name = "Detail 2", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detail_2_socket.default_value = 0.5
    detail_2_socket.min_value = 0.0
    detail_2_socket.max_value = 1.0
    detail_2_socket.subtype = 'FACTOR'
    detail_2_socket.attribute_domain = 'POINT'
    detail_2_socket.default_input = 'VALUE'
    detail_2_socket.structure_type = 'AUTO'

    #Socket Roughness
    roughness_socket = brushedchrome.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = 'NONE'
    roughness_socket.attribute_domain = 'POINT'
    roughness_socket.default_input = 'VALUE'
    roughness_socket.structure_type = 'AUTO'

    #Socket Bump Strength
    bump_strength_socket = brushedchrome.interface.new_socket(name = "Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    bump_strength_socket.default_value = 0.009999999776482582
    bump_strength_socket.min_value = 0.0
    bump_strength_socket.max_value = 1.0
    bump_strength_socket.subtype = 'FACTOR'
    bump_strength_socket.attribute_domain = 'POINT'
    bump_strength_socket.default_input = 'VALUE'
    bump_strength_socket.structure_type = 'AUTO'

    #Socket Rotation
    rotation_socket = brushedchrome.interface.new_socket(name = "Rotation", in_out='INPUT', socket_type = 'NodeSocketVector')
    rotation_socket.default_value = (0.0, 0.0, 0.0)
    rotation_socket.min_value = -3.4028234663852886e+38
    rotation_socket.max_value = 3.4028234663852886e+38
    rotation_socket.subtype = 'EULER'
    rotation_socket.attribute_domain = 'POINT'
    rotation_socket.default_input = 'VALUE'
    rotation_socket.structure_type = 'AUTO'

    #Socket Clear Coat Weight
    clear_coat_weight_socket = brushedchrome.interface.new_socket(name = "Clear Coat Weight", in_out='INPUT', socket_type = 'NodeSocketFloat')
    clear_coat_weight_socket.default_value = 1.0
    clear_coat_weight_socket.min_value = 0.0
    clear_coat_weight_socket.max_value = 1.0
    clear_coat_weight_socket.subtype = 'FACTOR'
    clear_coat_weight_socket.attribute_domain = 'POINT'
    clear_coat_weight_socket.default_input = 'VALUE'
    clear_coat_weight_socket.structure_type = 'AUTO'

    #Socket Clear Coat Roughness
    clear_coat_roughness_socket = brushedchrome.interface.new_socket(name = "Clear Coat Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    clear_coat_roughness_socket.default_value = 0.10000000149011612
    clear_coat_roughness_socket.min_value = 0.0
    clear_coat_roughness_socket.max_value = 1.0
    clear_coat_roughness_socket.subtype = 'FACTOR'
    clear_coat_roughness_socket.attribute_domain = 'POINT'
    clear_coat_roughness_socket.default_input = 'VALUE'
    clear_coat_roughness_socket.structure_type = 'AUTO'

    #Socket Clear Coat Tint
    clear_coat_tint_socket = brushedchrome.interface.new_socket(name = "Clear Coat Tint", in_out='INPUT', socket_type = 'NodeSocketColor')
    clear_coat_tint_socket.default_value = (1.0, 1.0, 1.0, 1.0)
    clear_coat_tint_socket.attribute_domain = 'POINT'
    clear_coat_tint_socket.default_input = 'VALUE'
    clear_coat_tint_socket.structure_type = 'AUTO'


    #initialize brushedchrome nodes
    #node Group Output
    group_output = brushedchrome.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = brushedchrome.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Noise Texture
    noise_texture = brushedchrome.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    #Scale
    noise_texture.inputs[2].default_value = 15.0
    #Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    #Distortion
    noise_texture.inputs[8].default_value = 0.0

    #node Mapping
    mapping = brushedchrome.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = 'POINT'
    #Location
    mapping.inputs[1].default_value = (0.0, 0.0, 0.0)

    #node ColorRamp
    colorramp = brushedchrome.nodes.new("ShaderNodeValToRGB")
    colorramp.name = "ColorRamp"
    colorramp.color_ramp.color_mode = 'RGB'
    colorramp.color_ramp.hue_interpolation = 'NEAR'
    colorramp.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    colorramp.color_ramp.elements.remove(colorramp.color_ramp.elements[0])
    colorramp_cre_0 = colorramp.color_ramp.elements[0]
    colorramp_cre_0.position = 0.16183581948280334
    colorramp_cre_0.alpha = 1.0
    colorramp_cre_0.color = (0.12864121794700623, 0.12864121794700623, 0.12864121794700623, 1.0)

    colorramp_cre_1 = colorramp.color_ramp.elements.new(0.7681161761283875)
    colorramp_cre_1.alpha = 1.0
    colorramp_cre_1.color = (0.40373504161834717, 0.40373504161834717, 0.40373504161834717, 1.0)


    #node Texture Coordinate
    texture_coordinate = brushedchrome.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False

    #node Principled BSDF
    principled_bsdf = brushedchrome.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK_SKIN'
    #IOR
    principled_bsdf.inputs[3].default_value = 1.4500000476837158
    #Alpha
    principled_bsdf.inputs[4].default_value = 1.0
    #Normal
    principled_bsdf.inputs[5].default_value = (0.0, 0.0, 0.0)
    #Diffuse Roughness
    principled_bsdf.inputs[7].default_value = 0.0
    #Subsurface Weight
    principled_bsdf.inputs[8].default_value = 0.0
    #Subsurface Radius
    principled_bsdf.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    #Subsurface Scale
    principled_bsdf.inputs[10].default_value = 0.05000000074505806
    #Subsurface IOR
    principled_bsdf.inputs[11].default_value = 1.399999976158142
    #Subsurface Anisotropy
    principled_bsdf.inputs[12].default_value = 0.0
    #Specular IOR Level
    principled_bsdf.inputs[13].default_value = 0.5
    #Specular Tint
    principled_bsdf.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    #Anisotropic
    principled_bsdf.inputs[15].default_value = 0.0
    #Anisotropic Rotation
    principled_bsdf.inputs[16].default_value = 0.0
    #Tangent
    principled_bsdf.inputs[17].default_value = (0.0, 0.0, 0.0)
    #Transmission Weight
    principled_bsdf.inputs[18].default_value = 0.0
    #Coat IOR
    principled_bsdf.inputs[21].default_value = 1.5
    #Sheen Weight
    principled_bsdf.inputs[24].default_value = 0.0
    #Sheen Roughness
    principled_bsdf.inputs[25].default_value = 0.5
    #Sheen Tint
    principled_bsdf.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    #Emission Color
    principled_bsdf.inputs[27].default_value = (0.0, 0.0, 0.0, 1.0)
    #Emission Strength
    principled_bsdf.inputs[28].default_value = 1.0
    #Thin Film Thickness
    principled_bsdf.inputs[29].default_value = 0.0
    #Thin Film IOR
    principled_bsdf.inputs[30].default_value = 1.3300000429153442

    #node Mapping.001
    mapping_001 = brushedchrome.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = 'POINT'
    #Location
    mapping_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    mapping_001.inputs[3].default_value = (80.0, 1.0, 1.0)

    #node Hue/Saturation/Value
    hue_saturation_value = brushedchrome.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    #Hue
    hue_saturation_value.inputs[0].default_value = 0.5
    #Saturation
    hue_saturation_value.inputs[1].default_value = 1.0
    #Fac
    hue_saturation_value.inputs[3].default_value = 1.0

    #node Bump
    bump = brushedchrome.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    #Distance
    bump.inputs[1].default_value = 1.0
    #Filter Width
    bump.inputs[2].default_value = 0.10000000149011612
    #Normal
    bump.inputs[4].default_value = (0.0, 0.0, 0.0)


    #Set locations
    group_output.location = (0.0, 0.0)
    group_input.location = (0.0, 0.0)
    noise_texture.location = (0.0, 0.0)
    mapping.location = (0.0, 0.0)
    colorramp.location = (0.0, 0.0)
    texture_coordinate.location = (0.0, 0.0)
    principled_bsdf.location = (0.0, 0.0)
    mapping_001.location = (0.0, 0.0)
    hue_saturation_value.location = (0.0, 0.0)
    bump.location = (0.0, 0.0)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    noise_texture.width, noise_texture.height = 140.0, 100.0
    mapping.width, mapping.height = 140.0, 100.0
    colorramp.width, colorramp.height = 240.0, 100.0
    texture_coordinate.width, texture_coordinate.height = 140.0, 100.0
    principled_bsdf.width, principled_bsdf.height = 240.0, 100.0
    mapping_001.width, mapping_001.height = 140.0, 100.0
    hue_saturation_value.width, hue_saturation_value.height = 150.0, 100.0
    bump.width, bump.height = 140.0, 100.0

    #initialize brushedchrome links
    #mapping_001.Vector -> noise_texture.Vector
    brushedchrome.links.new(mapping_001.outputs[0], noise_texture.inputs[0])
    #bump.Normal -> principled_bsdf.Coat Normal
    brushedchrome.links.new(bump.outputs[0], principled_bsdf.inputs[23])
    #noise_texture.Color -> bump.Height
    brushedchrome.links.new(noise_texture.outputs[1], bump.inputs[3])
    #mapping.Vector -> mapping_001.Vector
    brushedchrome.links.new(mapping.outputs[0], mapping_001.inputs[0])
    #noise_texture.Fac -> colorramp.Fac
    brushedchrome.links.new(noise_texture.outputs[0], colorramp.inputs[0])
    #hue_saturation_value.Color -> principled_bsdf.Roughness
    brushedchrome.links.new(hue_saturation_value.outputs[0], principled_bsdf.inputs[2])
    #colorramp.Color -> hue_saturation_value.Color
    brushedchrome.links.new(colorramp.outputs[0], hue_saturation_value.inputs[4])
    #principled_bsdf.BSDF -> group_output.Shader
    brushedchrome.links.new(principled_bsdf.outputs[0], group_output.inputs[0])
    #group_input.Scale -> mapping.Scale
    brushedchrome.links.new(group_input.outputs[0], mapping.inputs[3])
    #group_input.Rotation -> mapping.Rotation
    brushedchrome.links.new(group_input.outputs[7], mapping.inputs[2])
    #group_input.Roughness -> hue_saturation_value.Value
    brushedchrome.links.new(group_input.outputs[5], hue_saturation_value.inputs[2])
    #group_input.Base Color -> principled_bsdf.Base Color
    brushedchrome.links.new(group_input.outputs[1], principled_bsdf.inputs[0])
    #group_input.Metallic -> principled_bsdf.Metallic
    brushedchrome.links.new(group_input.outputs[2], principled_bsdf.inputs[1])
    #group_input.Bump Strength -> bump.Strength
    brushedchrome.links.new(group_input.outputs[6], bump.inputs[0])
    #group_input.Clear Coat Weight -> principled_bsdf.Coat Weight
    brushedchrome.links.new(group_input.outputs[8], principled_bsdf.inputs[19])
    #group_input.Clear Coat Roughness -> principled_bsdf.Coat Roughness
    brushedchrome.links.new(group_input.outputs[9], principled_bsdf.inputs[20])
    #group_input.Clear Coat Tint -> principled_bsdf.Coat Tint
    brushedchrome.links.new(group_input.outputs[10], principled_bsdf.inputs[22])
    #group_input.Detail 1 -> noise_texture.Detail
    brushedchrome.links.new(group_input.outputs[3], noise_texture.inputs[3])
    #group_input.Detail 2 -> noise_texture.Roughness
    brushedchrome.links.new(group_input.outputs[4], noise_texture.inputs[4])
    #texture_coordinate.Object -> mapping.Vector
    brushedchrome.links.new(texture_coordinate.outputs[3], mapping.inputs[0])
    return brushedchrome

brushedchrome = brushedchrome_node_group()

#initialize Brushed Chrome node group
def brushed_chrome_node_group():

    brushed_chrome = mat.node_tree
    #start with a clean node tree
    for node in brushed_chrome.nodes:
        brushed_chrome.nodes.remove(node)
    brushed_chrome.color_tag = 'NONE'
    brushed_chrome.description = ""
    brushed_chrome.default_group_node_width = 140
    

    #brushed_chrome interface

    #initialize brushed_chrome nodes
    #node Material Output
    material_output = brushed_chrome.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    #Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Thickness
    material_output.inputs[3].default_value = 0.0

    #node Group
    group = brushed_chrome.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = brushedchrome
    #Socket_1
    group.inputs[0].default_value = 1.0
    #Socket_2
    group.inputs[1].default_value = (0.2199402153491974, 0.2199402153491974, 0.2199402153491974, 1.0)
    #Socket_3
    group.inputs[2].default_value = 1.0
    #Socket_4
    group.inputs[3].default_value = 15.0
    #Socket_5
    group.inputs[4].default_value = 0.5
    #Socket_6
    group.inputs[5].default_value = 1.0
    #Socket_7
    group.inputs[6].default_value = 0.009999999776482582
    #Socket_8
    group.inputs[7].default_value = (0.0, 0.0, 0.0)
    #Socket_9
    group.inputs[8].default_value = 1.0
    #Socket_10
    group.inputs[9].default_value = 0.10000000149011612
    #Socket_11
    group.inputs[10].default_value = (1.0, 1.0, 1.0, 1.0)


    #Set locations
    material_output.location = (0.0, 0.0)
    group.location = (0.0, 0.0)

    #Set dimensions
    material_output.width, material_output.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0

    #initialize brushed_chrome links
    #group.Shader -> material_output.Surface
    brushed_chrome.links.new(group.outputs[0], material_output.inputs[0])
    return brushed_chrome

brushed_chrome = brushed_chrome_node_group()


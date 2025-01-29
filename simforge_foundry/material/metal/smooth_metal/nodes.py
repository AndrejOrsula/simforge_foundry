import bpy

mat = bpy.data.materials.new(name = "Smooth Metal")
mat.use_nodes = True

def smooth_metal_node_group():
    smooth_metal = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "Smooth Metal")
    smooth_metal.color_tag = 'NONE'
    smooth_metal.default_group_node_width = 140
    shader_socket = smooth_metal.interface.new_socket(name = "Shader", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    shader_socket.attribute_domain = 'POINT'
    scale_socket = smooth_metal.interface.new_socket(name = "Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    base_color_socket = smooth_metal.interface.new_socket(name = "Base Color", in_out='INPUT', socket_type = 'NodeSocketColor')
    base_color_socket.default_value = (0.457051545381546, 0.457051545381546, 0.457051545381546, 1.0)
    base_color_socket.attribute_domain = 'POINT'
    metallic_socket = smooth_metal.interface.new_socket(name = "Metallic", in_out='INPUT', socket_type = 'NodeSocketFloat')
    metallic_socket.default_value = 1.0
    metallic_socket.min_value = 0.0
    metallic_socket.max_value = 1.0
    metallic_socket.subtype = 'FACTOR'
    metallic_socket.attribute_domain = 'POINT'
    detail_socket = smooth_metal.interface.new_socket(name = "Detail", in_out='INPUT', socket_type = 'NodeSocketFloat')
    detail_socket.default_value = 10.0
    detail_socket.min_value = 0.0
    detail_socket.max_value = 15.0
    detail_socket.subtype = 'NONE'
    detail_socket.attribute_domain = 'POINT'
    roughness_socket = smooth_metal.interface.new_socket(name = "Roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = 'NONE'
    roughness_socket.attribute_domain = 'POINT'
    bump_strength_socket = smooth_metal.interface.new_socket(name = "Bump Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    bump_strength_socket.default_value = 0.009999999776482582
    bump_strength_socket.min_value = 0.0
    bump_strength_socket.max_value = 1.0
    bump_strength_socket.subtype = 'FACTOR'
    bump_strength_socket.attribute_domain = 'POINT'
    group_output = smooth_metal.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    group_input = smooth_metal.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    principled_bsdf = smooth_metal.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    principled_bsdf.inputs[3].default_value = 1.5
    principled_bsdf.inputs[4].default_value = 1.0
    principled_bsdf.inputs[7].default_value = 0.0
    principled_bsdf.inputs[8].default_value = 0.0
    principled_bsdf.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    principled_bsdf.inputs[10].default_value = 0.05000000074505806
    principled_bsdf.inputs[12].default_value = 0.0
    principled_bsdf.inputs[13].default_value = 0.5
    principled_bsdf.inputs[14].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf.inputs[15].default_value = 0.0
    principled_bsdf.inputs[16].default_value = 0.0
    principled_bsdf.inputs[17].default_value = (0.0, 0.0, 0.0)
    principled_bsdf.inputs[18].default_value = 0.0
    principled_bsdf.inputs[19].default_value = 0.0
    principled_bsdf.inputs[20].default_value = 0.029999999329447746
    principled_bsdf.inputs[21].default_value = 1.5
    principled_bsdf.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf.inputs[23].default_value = (0.0, 0.0, 0.0)
    principled_bsdf.inputs[24].default_value = 0.0
    principled_bsdf.inputs[25].default_value = 0.5
    principled_bsdf.inputs[26].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    principled_bsdf.inputs[28].default_value = 0.0
    principled_bsdf.inputs[29].default_value = 0.0
    principled_bsdf.inputs[30].default_value = 1.3300000429153442
    voronoi_texture = smooth_metal.nodes.new("ShaderNodeTexVoronoi")
    voronoi_texture.name = "Voronoi Texture"
    voronoi_texture.distance = 'EUCLIDEAN'
    voronoi_texture.feature = 'F1'
    voronoi_texture.normalize = False
    voronoi_texture.voronoi_dimensions = '3D'
    voronoi_texture.inputs[2].default_value = 20.0
    voronoi_texture.inputs[4].default_value = 0.5
    voronoi_texture.inputs[5].default_value = 2.0
    voronoi_texture.inputs[8].default_value = 1.0
    mapping = smooth_metal.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = 'POINT'
    mapping.inputs[1].default_value = (0.0, 0.0, 0.0)
    mapping.inputs[2].default_value = (0.0, 0.0, 0.0)
    texture_coordinate = smooth_metal.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False
    noise_texture = smooth_metal.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    noise_texture.inputs[2].default_value = 3.0
    noise_texture.inputs[4].default_value = 0.44999998807907104
    noise_texture.inputs[5].default_value = 2.0
    noise_texture.inputs[8].default_value = 0.0
    mix = smooth_metal.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'LINEAR_LIGHT'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'
    mix.inputs[0].default_value = 0.30000001192092896
    colorramp = smooth_metal.nodes.new("ShaderNodeValToRGB")
    colorramp.name = "ColorRamp"
    colorramp.color_ramp.color_mode = 'RGB'
    colorramp.color_ramp.hue_interpolation = 'NEAR'
    colorramp.color_ramp.interpolation = 'LINEAR'
    colorramp.color_ramp.elements.remove(colorramp.color_ramp.elements[0])
    colorramp_cre_0 = colorramp.color_ramp.elements[0]
    colorramp_cre_0.position = 0.3550724983215332
    colorramp_cre_0.alpha = 1.0
    colorramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)
    colorramp_cre_1 = colorramp.color_ramp.elements.new(0.5942029356956482)
    colorramp_cre_1.alpha = 1.0
    colorramp_cre_1.color = (0.40373504161834717, 0.40373504161834717, 0.40373504161834717, 1.0)
    hue_saturation_value = smooth_metal.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    hue_saturation_value.inputs[0].default_value = 0.5
    hue_saturation_value.inputs[1].default_value = 1.0
    hue_saturation_value.inputs[3].default_value = 1.0
    noise_texture_001 = smooth_metal.nodes.new("ShaderNodeTexNoise")
    noise_texture_001.name = "Noise Texture.001"
    noise_texture_001.noise_dimensions = '3D'
    noise_texture_001.noise_type = 'FBM'
    noise_texture_001.normalize = True
    noise_texture_001.inputs[2].default_value = 2.0
    noise_texture_001.inputs[4].default_value = 1.0
    noise_texture_001.inputs[5].default_value = 2.0
    noise_texture_001.inputs[8].default_value = 0.0
    mix_001 = smooth_metal.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'LINEAR_LIGHT'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'RGBA'
    mix_001.factor_mode = 'UNIFORM'
    mix_001.inputs[0].default_value = 0.029999999329447746
    bump = smooth_metal.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    bump.inputs[1].default_value = 1.0
    bump.inputs[3].default_value = (0.0, 0.0, 0.0)
    smooth_metal.links.new(mapping.outputs[0], mix.inputs[6])
    smooth_metal.links.new(texture_coordinate.outputs[3], mapping.inputs[0])
    smooth_metal.links.new(noise_texture_001.outputs[1], bump.inputs[2])
    smooth_metal.links.new(voronoi_texture.outputs[0], mix.inputs[7])
    smooth_metal.links.new(mix.outputs[2], noise_texture.inputs[0])
    smooth_metal.links.new(mix_001.outputs[2], noise_texture_001.inputs[0])
    smooth_metal.links.new(hue_saturation_value.outputs[0], principled_bsdf.inputs[2])
    smooth_metal.links.new(mapping.outputs[0], mix_001.inputs[6])
    smooth_metal.links.new(noise_texture_001.outputs[1], colorramp.inputs[0])
    smooth_metal.links.new(noise_texture.outputs[1], mix_001.inputs[7])
    smooth_metal.links.new(colorramp.outputs[0], hue_saturation_value.inputs[4])
    smooth_metal.links.new(mapping.outputs[0], voronoi_texture.inputs[0])
    smooth_metal.links.new(bump.outputs[0], principled_bsdf.inputs[5])
    smooth_metal.links.new(principled_bsdf.outputs[0], group_output.inputs[0])
    smooth_metal.links.new(group_input.outputs[0], mapping.inputs[3])
    smooth_metal.links.new(group_input.outputs[3], voronoi_texture.inputs[3])
    smooth_metal.links.new(group_input.outputs[3], noise_texture.inputs[3])
    smooth_metal.links.new(group_input.outputs[3], noise_texture_001.inputs[3])
    smooth_metal.links.new(group_input.outputs[4], hue_saturation_value.inputs[2])
    smooth_metal.links.new(group_input.outputs[5], bump.inputs[0])
    smooth_metal.links.new(group_input.outputs[1], principled_bsdf.inputs[0])
    smooth_metal.links.new(group_input.outputs[2], principled_bsdf.inputs[1])
    return smooth_metal

smooth_metal = smooth_metal_node_group()

def smooth_metal_1_node_group():
    smooth_metal_1 = mat.node_tree
    for node in smooth_metal_1.nodes:
        smooth_metal_1.nodes.remove(node)
    smooth_metal_1.color_tag = 'NONE'
    smooth_metal_1.default_group_node_width = 140
    material_output = smooth_metal_1.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    material_output.inputs[3].default_value = 0.0
    group = smooth_metal_1.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = smooth_metal
    group.inputs[0].default_value = 1.0
    group.inputs[1].default_value = (0.457051545381546, 0.457051545381546, 0.457051545381546, 1.0)
    group.inputs[2].default_value = 1.0
    group.inputs[3].default_value = 10.0
    group.inputs[4].default_value = 1.0
    group.inputs[5].default_value = 0.009999999776482582
    smooth_metal_1.links.new(group.outputs[0], material_output.inputs[0])
    return smooth_metal_1

smooth_metal_1 = smooth_metal_1_node_group()


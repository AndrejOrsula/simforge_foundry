import bpy

mat = bpy.data.materials.new(name = "Gold Smooth")
mat.use_nodes = True

def goldsmoothshader_node_group():
    goldsmoothshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "GoldSmoothShader")
    goldsmoothshader.color_tag = 'NONE'
    goldsmoothshader.default_group_node_width = 140
    bsdf_socket = goldsmoothshader.interface.new_socket(name = "BSDF", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    bsdf_socket.attribute_domain = 'POINT'
    group_output = goldsmoothshader.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    group_input = goldsmoothshader.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    principled_bsdf = goldsmoothshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'GGX'
    principled_bsdf.subsurface_method = 'BURLEY'
    principled_bsdf.inputs[1].default_value = 1.0
    principled_bsdf.inputs[2].default_value = 0.27000001072883606
    principled_bsdf.inputs[3].default_value = 1.4500000476837158
    principled_bsdf.inputs[4].default_value = 1.0
    principled_bsdf.inputs[7].default_value = 0.0
    principled_bsdf.inputs[8].default_value = 0.0
    principled_bsdf.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    principled_bsdf.inputs[10].default_value = 0.05000000074505806
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
    principled_bsdf.inputs[27].default_value = (0.0, 0.0, 0.0, 1.0)
    principled_bsdf.inputs[28].default_value = 1.0
    principled_bsdf.inputs[29].default_value = 0.0
    principled_bsdf.inputs[30].default_value = 1.3300000429153442
    texture_coordinate = goldsmoothshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False
    mapping = goldsmoothshader.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = 'POINT'
    mapping.inputs[1].default_value = (0.0, 0.0, 0.0)
    mapping.inputs[2].default_value = (0.0, 0.0, 0.0)
    mapping.inputs[3].default_value = (1.0, 1.0, 1.0)
    musgrave_texture = goldsmoothshader.nodes.new("ShaderNodeTexNoise")
    musgrave_texture.name = "Musgrave Texture"
    musgrave_texture.noise_dimensions = '3D'
    musgrave_texture.noise_type = 'FBM'
    musgrave_texture.normalize = False
    musgrave_texture.inputs[2].default_value = 400.0
    musgrave_texture.inputs[3].default_value = 14.0
    musgrave_texture.inputs[4].default_value = 0.999993085861206
    musgrave_texture.inputs[5].default_value = 2.0
    musgrave_texture.inputs[8].default_value = 0.0
    colorramp = goldsmoothshader.nodes.new("ShaderNodeValToRGB")
    colorramp.name = "ColorRamp"
    colorramp.color_ramp.color_mode = 'RGB'
    colorramp.color_ramp.hue_interpolation = 'NEAR'
    colorramp.color_ramp.interpolation = 'LINEAR'
    colorramp.color_ramp.elements.remove(colorramp.color_ramp.elements[0])
    colorramp_cre_0 = colorramp.color_ramp.elements[0]
    colorramp_cre_0.position = 0.0
    colorramp_cre_0.alpha = 1.0
    colorramp_cre_0.color = (0.6080294847488403, 0.33629006147384644, 0.08473001420497894, 1.0)
    colorramp_cre_1 = colorramp.color_ramp.elements.new(1.0)
    colorramp_cre_1.alpha = 1.0
    colorramp_cre_1.color = (0.2788943350315094, 0.09758733958005905, 0.025186873972415924, 1.0)
    noise_texture = goldsmoothshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    noise_texture.inputs[2].default_value = 12.09999942779541
    noise_texture.inputs[3].default_value = 16.0
    noise_texture.inputs[4].default_value = 0.5
    noise_texture.inputs[5].default_value = 2.0
    noise_texture.inputs[8].default_value = 0.0
    bump = goldsmoothshader.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    bump.inputs[0].default_value = 0.00800000037997961
    bump.inputs[1].default_value = 1.0
    bump.inputs[3].default_value = (0.0, 0.0, 0.0)
    goldsmoothshader.links.new(mapping.outputs[0], musgrave_texture.inputs[0])
    goldsmoothshader.links.new(mapping.outputs[0], noise_texture.inputs[0])
    goldsmoothshader.links.new(musgrave_texture.outputs[0], colorramp.inputs[0])
    goldsmoothshader.links.new(bump.outputs[0], principled_bsdf.inputs[5])
    goldsmoothshader.links.new(texture_coordinate.outputs[3], mapping.inputs[0])
    goldsmoothshader.links.new(colorramp.outputs[0], principled_bsdf.inputs[0])
    goldsmoothshader.links.new(noise_texture.outputs[0], bump.inputs[2])
    goldsmoothshader.links.new(principled_bsdf.outputs[0], group_output.inputs[0])
    return goldsmoothshader

goldsmoothshader = goldsmoothshader_node_group()

def gold_smooth_node_group():
    gold_smooth = mat.node_tree
    for node in gold_smooth.nodes:
        gold_smooth.nodes.remove(node)
    gold_smooth.color_tag = 'NONE'
    gold_smooth.default_group_node_width = 140
    material_output = gold_smooth.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    material_output.inputs[3].default_value = 0.0
    group = gold_smooth.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = goldsmoothshader
    gold_smooth.links.new(group.outputs[0], material_output.inputs[0])
    return gold_smooth

gold_smooth = gold_smooth_node_group()


import bpy, mathutils

mat = bpy.data.materials.new(name = "Gold Smooth")
mat.use_nodes = True
#initialize GoldSmoothShader node group
def goldsmoothshader_node_group():

    goldsmoothshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "GoldSmoothShader")

    goldsmoothshader.color_tag = 'NONE'
    goldsmoothshader.description = ""
    goldsmoothshader.default_group_node_width = 140
    

    #goldsmoothshader interface
    #Socket BSDF
    bsdf_socket = goldsmoothshader.interface.new_socket(name = "BSDF", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    bsdf_socket.attribute_domain = 'POINT'
    bsdf_socket.default_input = 'VALUE'
    bsdf_socket.structure_type = 'AUTO'


    #initialize goldsmoothshader nodes
    #node Group Output
    group_output = goldsmoothshader.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = goldsmoothshader.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Principled BSDF
    principled_bsdf = goldsmoothshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'GGX'
    principled_bsdf.subsurface_method = 'BURLEY'
    #Metallic
    principled_bsdf.inputs[1].default_value = 1.0
    #Roughness
    principled_bsdf.inputs[2].default_value = 0.27000001072883606
    #IOR
    principled_bsdf.inputs[3].default_value = 1.4500000476837158
    #Alpha
    principled_bsdf.inputs[4].default_value = 1.0
    #Diffuse Roughness
    principled_bsdf.inputs[7].default_value = 0.0
    #Subsurface Weight
    principled_bsdf.inputs[8].default_value = 0.0
    #Subsurface Radius
    principled_bsdf.inputs[9].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    #Subsurface Scale
    principled_bsdf.inputs[10].default_value = 0.05000000074505806
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
    #Coat Weight
    principled_bsdf.inputs[19].default_value = 0.0
    #Coat Roughness
    principled_bsdf.inputs[20].default_value = 0.029999999329447746
    #Coat IOR
    principled_bsdf.inputs[21].default_value = 1.5
    #Coat Tint
    principled_bsdf.inputs[22].default_value = (1.0, 1.0, 1.0, 1.0)
    #Coat Normal
    principled_bsdf.inputs[23].default_value = (0.0, 0.0, 0.0)
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

    #node Texture Coordinate
    texture_coordinate = goldsmoothshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False

    #node Mapping
    mapping = goldsmoothshader.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = 'POINT'
    #Location
    mapping.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    mapping.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    mapping.inputs[3].default_value = (1.0, 1.0, 1.0)

    #node Musgrave Texture
    musgrave_texture = goldsmoothshader.nodes.new("ShaderNodeTexNoise")
    musgrave_texture.name = "Musgrave Texture"
    musgrave_texture.noise_dimensions = '3D'
    musgrave_texture.noise_type = 'FBM'
    musgrave_texture.normalize = False
    #Scale
    musgrave_texture.inputs[2].default_value = 400.0
    #Detail
    musgrave_texture.inputs[3].default_value = 14.0
    #Roughness
    musgrave_texture.inputs[4].default_value = 0.999993085861206
    #Lacunarity
    musgrave_texture.inputs[5].default_value = 2.0
    #Distortion
    musgrave_texture.inputs[8].default_value = 0.0

    #node ColorRamp
    colorramp = goldsmoothshader.nodes.new("ShaderNodeValToRGB")
    colorramp.name = "ColorRamp"
    colorramp.color_ramp.color_mode = 'RGB'
    colorramp.color_ramp.hue_interpolation = 'NEAR'
    colorramp.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    colorramp.color_ramp.elements.remove(colorramp.color_ramp.elements[0])
    colorramp_cre_0 = colorramp.color_ramp.elements[0]
    colorramp_cre_0.position = 0.0
    colorramp_cre_0.alpha = 1.0
    colorramp_cre_0.color = (0.6080294847488403, 0.33629006147384644, 0.08473001420497894, 1.0)

    colorramp_cre_1 = colorramp.color_ramp.elements.new(1.0)
    colorramp_cre_1.alpha = 1.0
    colorramp_cre_1.color = (0.2788943350315094, 0.09758733958005905, 0.025186873972415924, 1.0)


    #node Noise Texture
    noise_texture = goldsmoothshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    #Scale
    noise_texture.inputs[2].default_value = 12.09999942779541
    #Detail
    noise_texture.inputs[3].default_value = 16.0
    #Roughness
    noise_texture.inputs[4].default_value = 0.5
    #Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    #Distortion
    noise_texture.inputs[8].default_value = 0.0

    #node Bump
    bump = goldsmoothshader.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    #Strength
    bump.inputs[0].default_value = 0.00800000037997961
    #Distance
    bump.inputs[1].default_value = 1.0
    #Filter Width
    bump.inputs[2].default_value = 0.10000000149011612
    #Normal
    bump.inputs[4].default_value = (0.0, 0.0, 0.0)


    #Set locations
    group_output.location = (0.0, 0.0)
    group_input.location = (0.0, 0.0)
    principled_bsdf.location = (0.0, 0.0)
    texture_coordinate.location = (0.0, 0.0)
    mapping.location = (0.0, 0.0)
    musgrave_texture.location = (0.0, 0.0)
    colorramp.location = (0.0, 0.0)
    noise_texture.location = (0.0, 0.0)
    bump.location = (0.0, 0.0)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    principled_bsdf.width, principled_bsdf.height = 240.0, 100.0
    texture_coordinate.width, texture_coordinate.height = 140.0, 100.0
    mapping.width, mapping.height = 140.0, 100.0
    musgrave_texture.width, musgrave_texture.height = 140.0, 100.0
    colorramp.width, colorramp.height = 240.0, 100.0
    noise_texture.width, noise_texture.height = 140.0, 100.0
    bump.width, bump.height = 140.0, 100.0

    #initialize goldsmoothshader links
    #mapping.Vector -> musgrave_texture.Vector
    goldsmoothshader.links.new(mapping.outputs[0], musgrave_texture.inputs[0])
    #mapping.Vector -> noise_texture.Vector
    goldsmoothshader.links.new(mapping.outputs[0], noise_texture.inputs[0])
    #musgrave_texture.Fac -> colorramp.Fac
    goldsmoothshader.links.new(musgrave_texture.outputs[0], colorramp.inputs[0])
    #bump.Normal -> principled_bsdf.Normal
    goldsmoothshader.links.new(bump.outputs[0], principled_bsdf.inputs[5])
    #texture_coordinate.Object -> mapping.Vector
    goldsmoothshader.links.new(texture_coordinate.outputs[3], mapping.inputs[0])
    #colorramp.Color -> principled_bsdf.Base Color
    goldsmoothshader.links.new(colorramp.outputs[0], principled_bsdf.inputs[0])
    #noise_texture.Fac -> bump.Height
    goldsmoothshader.links.new(noise_texture.outputs[0], bump.inputs[3])
    #principled_bsdf.BSDF -> group_output.BSDF
    goldsmoothshader.links.new(principled_bsdf.outputs[0], group_output.inputs[0])
    return goldsmoothshader

goldsmoothshader = goldsmoothshader_node_group()

#initialize Gold Smooth node group
def gold_smooth_node_group():

    gold_smooth = mat.node_tree
    #start with a clean node tree
    for node in gold_smooth.nodes:
        gold_smooth.nodes.remove(node)
    gold_smooth.color_tag = 'NONE'
    gold_smooth.description = ""
    gold_smooth.default_group_node_width = 140
    

    #gold_smooth interface

    #initialize gold_smooth nodes
    #node Material Output
    material_output = gold_smooth.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    #Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Thickness
    material_output.inputs[3].default_value = 0.0

    #node Group
    group = gold_smooth.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = goldsmoothshader


    #Set locations
    material_output.location = (0.0, 0.0)
    group.location = (0.0, 0.0)

    #Set dimensions
    material_output.width, material_output.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0

    #initialize gold_smooth links
    #group.BSDF -> material_output.Surface
    gold_smooth.links.new(group.outputs[0], material_output.inputs[0])
    return gold_smooth

gold_smooth = gold_smooth_node_group()


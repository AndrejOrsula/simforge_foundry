import bpy, mathutils

mat = bpy.data.materials.new(name = "SolarCellMat")
mat.use_nodes = True
#initialize SolarCellShader node group
def solarcellshader_node_group():

    solarcellshader = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "SolarCellShader")

    solarcellshader.color_tag = 'NONE'
    solarcellshader.description = ""
    solarcellshader.default_group_node_width = 140
    

    #solarcellshader interface
    #Socket Shader
    shader_socket = solarcellshader.interface.new_socket(name = "Shader", in_out='OUTPUT', socket_type = 'NodeSocketShader')
    shader_socket.attribute_domain = 'POINT'
    shader_socket.default_input = 'VALUE'
    shader_socket.structure_type = 'AUTO'

    #Socket scale
    scale_socket = solarcellshader.interface.new_socket(name = "scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
    scale_socket.default_value = 1.0
    scale_socket.min_value = -3.4028234663852886e+38
    scale_socket.max_value = 3.4028234663852886e+38
    scale_socket.subtype = 'NONE'
    scale_socket.attribute_domain = 'POINT'
    scale_socket.default_input = 'VALUE'
    scale_socket.structure_type = 'AUTO'

    #Socket color1
    color1_socket = solarcellshader.interface.new_socket(name = "color1", in_out='INPUT', socket_type = 'NodeSocketColor')
    color1_socket.default_value = (1.0, 0.3528609871864319, 0.06422899663448334, 1.0)
    color1_socket.attribute_domain = 'POINT'
    color1_socket.default_input = 'VALUE'
    color1_socket.structure_type = 'AUTO'

    #Socket color2
    color2_socket = solarcellshader.interface.new_socket(name = "color2", in_out='INPUT', socket_type = 'NodeSocketColor')
    color2_socket.default_value = (0.01960499957203865, 0.01960499957203865, 0.01960499957203865, 1.0)
    color2_socket.attribute_domain = 'POINT'
    color2_socket.default_input = 'VALUE'
    color2_socket.structure_type = 'AUTO'

    #Socket grid_visibility
    grid_visibility_socket = solarcellshader.interface.new_socket(name = "grid_visibility", in_out='INPUT', socket_type = 'NodeSocketFloat')
    grid_visibility_socket.default_value = 0.30000001192092896
    grid_visibility_socket.min_value = 0.0
    grid_visibility_socket.max_value = 1.0
    grid_visibility_socket.subtype = 'FACTOR'
    grid_visibility_socket.attribute_domain = 'POINT'
    grid_visibility_socket.default_input = 'VALUE'
    grid_visibility_socket.structure_type = 'AUTO'

    #Socket roughness
    roughness_socket = solarcellshader.interface.new_socket(name = "roughness", in_out='INPUT', socket_type = 'NodeSocketFloat')
    roughness_socket.default_value = 1.0
    roughness_socket.min_value = 0.0
    roughness_socket.max_value = 2.0
    roughness_socket.subtype = 'NONE'
    roughness_socket.attribute_domain = 'POINT'
    roughness_socket.default_input = 'VALUE'
    roughness_socket.structure_type = 'AUTO'

    #Socket bump_strength
    bump_strength_socket = solarcellshader.interface.new_socket(name = "bump_strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
    bump_strength_socket.default_value = 0.20000000298023224
    bump_strength_socket.min_value = 0.0
    bump_strength_socket.max_value = 1.0
    bump_strength_socket.subtype = 'FACTOR'
    bump_strength_socket.attribute_domain = 'POINT'
    bump_strength_socket.default_input = 'VALUE'
    bump_strength_socket.structure_type = 'AUTO'


    #initialize solarcellshader nodes
    #node Group Output
    group_output = solarcellshader.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    #node Group Input
    group_input = solarcellshader.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    #node Principled BSDF
    principled_bsdf = solarcellshader.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.name = "Principled BSDF"
    principled_bsdf.distribution = 'MULTI_GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    #Metallic
    principled_bsdf.inputs[1].default_value = 1.0
    #IOR
    principled_bsdf.inputs[3].default_value = 1.5
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
    principled_bsdf.inputs[27].default_value = (1.0, 1.0, 1.0, 1.0)
    #Emission Strength
    principled_bsdf.inputs[28].default_value = 0.0
    #Thin Film Thickness
    principled_bsdf.inputs[29].default_value = 0.0
    #Thin Film IOR
    principled_bsdf.inputs[30].default_value = 1.3300000429153442

    #node Brick Texture
    brick_texture = solarcellshader.nodes.new("ShaderNodeTexBrick")
    brick_texture.name = "Brick Texture"
    brick_texture.offset = 1.0
    brick_texture.offset_frequency = 2
    brick_texture.squash = 1.0
    brick_texture.squash_frequency = 2
    #Color1
    brick_texture.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
    #Color2
    brick_texture.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
    #Mortar
    brick_texture.inputs[3].default_value = (0.0, 0.0, 0.0, 1.0)
    #Scale
    brick_texture.inputs[4].default_value = 5.0
    #Mortar Size
    brick_texture.inputs[5].default_value = 0.019999999552965164
    #Mortar Smooth
    brick_texture.inputs[6].default_value = 0.10000000149011612
    #Bias
    brick_texture.inputs[7].default_value = 0.0
    #Brick Width
    brick_texture.inputs[8].default_value = 0.5
    #Row Height
    brick_texture.inputs[9].default_value = 0.25

    #node Mapping
    mapping = solarcellshader.nodes.new("ShaderNodeMapping")
    mapping.name = "Mapping"
    mapping.vector_type = 'POINT'
    #Location
    mapping.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    mapping.inputs[2].default_value = (0.0, 0.0, 0.0)

    #node Texture Coordinate
    texture_coordinate = solarcellshader.nodes.new("ShaderNodeTexCoord")
    texture_coordinate.name = "Texture Coordinate"
    texture_coordinate.from_instancer = False

    #node Brick Texture.001
    brick_texture_001 = solarcellshader.nodes.new("ShaderNodeTexBrick")
    brick_texture_001.name = "Brick Texture.001"
    brick_texture_001.offset = 1.0
    brick_texture_001.offset_frequency = 2
    brick_texture_001.squash = 1.0
    brick_texture_001.squash_frequency = 2
    #Color1
    brick_texture_001.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
    #Color2
    brick_texture_001.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
    #Mortar
    brick_texture_001.inputs[3].default_value = (0.0, 0.0, 0.0, 1.0)
    #Scale
    brick_texture_001.inputs[4].default_value = 20.0
    #Mortar Size
    brick_texture_001.inputs[5].default_value = 0.019999999552965164
    #Mortar Smooth
    brick_texture_001.inputs[6].default_value = 0.4000000059604645
    #Bias
    brick_texture_001.inputs[7].default_value = 0.0
    #Brick Width
    brick_texture_001.inputs[8].default_value = 0.5
    #Row Height
    brick_texture_001.inputs[9].default_value = 0.25

    #node Brick Texture.002
    brick_texture_002 = solarcellshader.nodes.new("ShaderNodeTexBrick")
    brick_texture_002.name = "Brick Texture.002"
    brick_texture_002.offset = 1.0
    brick_texture_002.offset_frequency = 2
    brick_texture_002.squash = 1.0
    brick_texture_002.squash_frequency = 2
    #Color1
    brick_texture_002.inputs[1].default_value = (1.0, 1.0, 1.0, 1.0)
    #Color2
    brick_texture_002.inputs[2].default_value = (1.0, 1.0, 1.0, 1.0)
    #Mortar
    brick_texture_002.inputs[3].default_value = (0.0, 0.0, 0.0, 1.0)
    #Scale
    brick_texture_002.inputs[4].default_value = 120.0
    #Mortar Size
    brick_texture_002.inputs[5].default_value = 0.17000000178813934
    #Mortar Smooth
    brick_texture_002.inputs[6].default_value = 0.0
    #Bias
    brick_texture_002.inputs[7].default_value = 0.0
    #Brick Width
    brick_texture_002.inputs[8].default_value = 0.5
    #Row Height
    brick_texture_002.inputs[9].default_value = 0.5

    #node Mix
    mix = solarcellshader.nodes.new("ShaderNodeMix")
    mix.name = "Mix"
    mix.blend_type = 'DARKEN'
    mix.clamp_factor = True
    mix.clamp_result = False
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'

    #node Mix.001
    mix_001 = solarcellshader.nodes.new("ShaderNodeMix")
    mix_001.name = "Mix.001"
    mix_001.blend_type = 'DARKEN'
    mix_001.clamp_factor = True
    mix_001.clamp_result = False
    mix_001.data_type = 'RGBA'
    mix_001.factor_mode = 'UNIFORM'
    #B_Color
    mix_001.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)

    #node Mix.002
    mix_002 = solarcellshader.nodes.new("ShaderNodeMix")
    mix_002.name = "Mix.002"
    mix_002.blend_type = 'MIX'
    mix_002.clamp_factor = True
    mix_002.clamp_result = False
    mix_002.data_type = 'RGBA'
    mix_002.factor_mode = 'UNIFORM'

    #node Bump
    bump = solarcellshader.nodes.new("ShaderNodeBump")
    bump.name = "Bump"
    bump.invert = False
    #Distance
    bump.inputs[1].default_value = 1.0
    #Filter Width
    bump.inputs[2].default_value = 0.10000000149011612
    #Normal
    bump.inputs[4].default_value = (0.0, 0.0, 0.0)

    #node Noise Texture
    noise_texture = solarcellshader.nodes.new("ShaderNodeTexNoise")
    noise_texture.name = "Noise Texture"
    noise_texture.noise_dimensions = '3D'
    noise_texture.noise_type = 'FBM'
    noise_texture.normalize = True
    #Scale
    noise_texture.inputs[2].default_value = 50.0
    #Detail
    noise_texture.inputs[3].default_value = 15.0
    #Roughness
    noise_texture.inputs[4].default_value = 0.6000000238418579
    #Lacunarity
    noise_texture.inputs[5].default_value = 2.0
    #Distortion
    noise_texture.inputs[8].default_value = 0.0

    #node Color Ramp
    color_ramp = solarcellshader.nodes.new("ShaderNodeValToRGB")
    color_ramp.name = "Color Ramp"
    color_ramp.color_ramp.color_mode = 'RGB'
    color_ramp.color_ramp.hue_interpolation = 'NEAR'
    color_ramp.color_ramp.interpolation = 'LINEAR'

    #initialize color ramp elements
    color_ramp.color_ramp.elements.remove(color_ramp.color_ramp.elements[0])
    color_ramp_cre_0 = color_ramp.color_ramp.elements[0]
    color_ramp_cre_0.position = 0.26633164286613464
    color_ramp_cre_0.alpha = 1.0
    color_ramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    color_ramp_cre_1 = color_ramp.color_ramp.elements.new(1.0)
    color_ramp_cre_1.alpha = 1.0
    color_ramp_cre_1.color = (0.47251400351524353, 0.47251400351524353, 0.47251400351524353, 1.0)


    #node Hue/Saturation/Value
    hue_saturation_value = solarcellshader.nodes.new("ShaderNodeHueSaturation")
    hue_saturation_value.name = "Hue/Saturation/Value"
    #Hue
    hue_saturation_value.inputs[0].default_value = 0.5
    #Saturation
    hue_saturation_value.inputs[1].default_value = 1.0
    #Fac
    hue_saturation_value.inputs[3].default_value = 1.0

    #node Reroute
    reroute = solarcellshader.nodes.new("NodeReroute")
    reroute.name = "Reroute"
    reroute.socket_idname = "NodeSocketVector"
    #node Mapping.001
    mapping_001 = solarcellshader.nodes.new("ShaderNodeMapping")
    mapping_001.name = "Mapping.001"
    mapping_001.vector_type = 'POINT'
    #Location
    mapping_001.inputs[1].default_value = (0.0, 0.0, 0.0)
    #Rotation
    mapping_001.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Scale
    mapping_001.inputs[3].default_value = (0.5, 0.5, 0.5)


    #Set locations
    group_output.location = (0.0, 0.0)
    group_input.location = (0.0, 0.0)
    principled_bsdf.location = (0.0, 0.0)
    brick_texture.location = (0.0, 0.0)
    mapping.location = (0.0, 0.0)
    texture_coordinate.location = (0.0, 0.0)
    brick_texture_001.location = (0.0, 0.0)
    brick_texture_002.location = (0.0, 0.0)
    mix.location = (0.0, 0.0)
    mix_001.location = (0.0, 0.0)
    mix_002.location = (0.0, 0.0)
    bump.location = (0.0, 0.0)
    noise_texture.location = (0.0, 0.0)
    color_ramp.location = (0.0, 0.0)
    hue_saturation_value.location = (0.0, 0.0)
    reroute.location = (0.0, 0.0)
    mapping_001.location = (0.0, 0.0)

    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    principled_bsdf.width, principled_bsdf.height = 240.0, 100.0
    brick_texture.width, brick_texture.height = 150.0, 100.0
    mapping.width, mapping.height = 140.0, 100.0
    texture_coordinate.width, texture_coordinate.height = 140.0, 100.0
    brick_texture_001.width, brick_texture_001.height = 150.0, 100.0
    brick_texture_002.width, brick_texture_002.height = 150.0, 100.0
    mix.width, mix.height = 140.0, 100.0
    mix_001.width, mix_001.height = 140.0, 100.0
    mix_002.width, mix_002.height = 140.0, 100.0
    bump.width, bump.height = 140.0, 100.0
    noise_texture.width, noise_texture.height = 140.0, 100.0
    color_ramp.width, color_ramp.height = 240.0, 100.0
    hue_saturation_value.width, hue_saturation_value.height = 150.0, 100.0
    reroute.width, reroute.height = 140.0, 100.0
    mapping_001.width, mapping_001.height = 140.0, 100.0

    #initialize solarcellshader links
    #reroute.Output -> brick_texture_002.Vector
    solarcellshader.links.new(reroute.outputs[0], brick_texture_002.inputs[0])
    #brick_texture_001.Color -> mix.A
    solarcellshader.links.new(brick_texture_001.outputs[0], mix.inputs[6])
    #mix_001.Result -> mix_002.Factor
    solarcellshader.links.new(mix_001.outputs[2], mix_002.inputs[0])
    #brick_texture.Color -> mix.B
    solarcellshader.links.new(brick_texture.outputs[0], mix.inputs[7])
    #bump.Normal -> principled_bsdf.Normal
    solarcellshader.links.new(bump.outputs[0], principled_bsdf.inputs[5])
    #mix.Result -> mix_001.A
    solarcellshader.links.new(mix.outputs[2], mix_001.inputs[6])
    #reroute.Output -> noise_texture.Vector
    solarcellshader.links.new(reroute.outputs[0], noise_texture.inputs[0])
    #brick_texture_002.Color -> mix_001.Factor
    solarcellshader.links.new(brick_texture_002.outputs[0], mix_001.inputs[0])
    #mix_001.Result -> bump.Height
    solarcellshader.links.new(mix_001.outputs[2], bump.inputs[3])
    #mix_002.Result -> principled_bsdf.Base Color
    solarcellshader.links.new(mix_002.outputs[2], principled_bsdf.inputs[0])
    #color_ramp.Color -> hue_saturation_value.Color
    solarcellshader.links.new(color_ramp.outputs[0], hue_saturation_value.inputs[4])
    #reroute.Output -> brick_texture.Vector
    solarcellshader.links.new(reroute.outputs[0], brick_texture.inputs[0])
    #hue_saturation_value.Color -> principled_bsdf.Roughness
    solarcellshader.links.new(hue_saturation_value.outputs[0], principled_bsdf.inputs[2])
    #noise_texture.Fac -> color_ramp.Fac
    solarcellshader.links.new(noise_texture.outputs[0], color_ramp.inputs[0])
    #reroute.Output -> brick_texture_001.Vector
    solarcellshader.links.new(reroute.outputs[0], brick_texture_001.inputs[0])
    #principled_bsdf.BSDF -> group_output.Shader
    solarcellshader.links.new(principled_bsdf.outputs[0], group_output.inputs[0])
    #group_input.scale -> mapping.Scale
    solarcellshader.links.new(group_input.outputs[0], mapping.inputs[3])
    #group_input.color1 -> mix_002.A
    solarcellshader.links.new(group_input.outputs[1], mix_002.inputs[6])
    #group_input.color2 -> mix_002.B
    solarcellshader.links.new(group_input.outputs[2], mix_002.inputs[7])
    #group_input.grid_visibility -> mix.Factor
    solarcellshader.links.new(group_input.outputs[3], mix.inputs[0])
    #group_input.roughness -> hue_saturation_value.Value
    solarcellshader.links.new(group_input.outputs[4], hue_saturation_value.inputs[2])
    #group_input.bump_strength -> bump.Strength
    solarcellshader.links.new(group_input.outputs[5], bump.inputs[0])
    #mapping_001.Vector -> reroute.Input
    solarcellshader.links.new(mapping_001.outputs[0], reroute.inputs[0])
    #mapping.Vector -> mapping_001.Vector
    solarcellshader.links.new(mapping.outputs[0], mapping_001.inputs[0])
    #texture_coordinate.UV -> mapping.Vector
    solarcellshader.links.new(texture_coordinate.outputs[2], mapping.inputs[0])
    return solarcellshader

solarcellshader = solarcellshader_node_group()

#initialize SolarCellMat node group
def solarcellmat_node_group():

    solarcellmat = mat.node_tree
    #start with a clean node tree
    for node in solarcellmat.nodes:
        solarcellmat.nodes.remove(node)
    solarcellmat.color_tag = 'NONE'
    solarcellmat.description = ""
    solarcellmat.default_group_node_width = 140
    

    #solarcellmat interface

    #initialize solarcellmat nodes
    #node Material Output
    material_output = solarcellmat.nodes.new("ShaderNodeOutputMaterial")
    material_output.name = "Material Output"
    material_output.is_active_output = True
    material_output.target = 'ALL'
    #Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Thickness
    material_output.inputs[3].default_value = 0.0

    #node Group
    group = solarcellmat.nodes.new("ShaderNodeGroup")
    group.name = "Group"
    group.node_tree = solarcellshader
    #Socket_1
    group.inputs[0].default_value = 1.0
    #Socket_2
    group.inputs[1].default_value = (1.0, 0.3528609871864319, 0.06422899663448334, 1.0)
    #Socket_3
    group.inputs[2].default_value = (0.01960499957203865, 0.01960499957203865, 0.01960499957203865, 1.0)
    #Socket_4
    group.inputs[3].default_value = 0.30000001192092896
    #Socket_5
    group.inputs[4].default_value = 1.0
    #Socket_6
    group.inputs[5].default_value = 0.20000000298023224


    #Set locations
    material_output.location = (0.0, 0.0)
    group.location = (0.0, 0.0)

    #Set dimensions
    material_output.width, material_output.height = 140.0, 100.0
    group.width, group.height = 140.0, 100.0

    #initialize solarcellmat links
    #group.Shader -> material_output.Surface
    solarcellmat.links.new(group.outputs[0], material_output.inputs[0])
    return solarcellmat

solarcellmat = solarcellmat_node_group()


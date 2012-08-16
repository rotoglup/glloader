# List of GL enumerants for glext.h header
#
# This is NOT the master GL enumerant registry (enum.spec).
#
# This is NOT official, it only comes as a support to the official enumext
#   that does not contain some 'real world' extensions, such as 
#   GL_EXT_texture_rectangle or GL_EXT_texture_edge_clamp
#
###############################################################################

# Extension #?
EXT_texture_rectangle enum:
	TEXTURE_RECTANGLE_EXT				= 0x84F5
	TEXTURE_BINDING_RECTANGLE_EXT		= 0x84F6
	PROXY_TEXTURE_RECTANGLE_EXT			= 0x84F7
	MAX_RECTANGLE_TEXTURE_SIZE_EXT		= 0x84F8

###############################################################################

# Extension #?
EXT_texture_edge_clamp enum:
	CLAMP_TO_EDGE_EXT					= 0x812F

###############################################################################

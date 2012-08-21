import ctypes

path = r"M:\bin\vc8\release\rtguGL.dll"
_rtgugl = ctypes.WinDLL(path)

GLchar = ctypes.c_char
GLcharARB = ctypes.c_char
char = ctypes.c_char
GLenum = ctypes.c_uint
GLboolean = ctypes.c_ubyte
GLbyte = ctypes.c_byte
GLshort = ctypes.c_short
GLint = ctypes.c_int
GLubyte = ctypes.c_ubyte
GLushort = ctypes.c_ushort
GLbitfield = ctypes.c_uint
GLuint = ctypes.c_uint
GLsizei = ctypes.c_size_t
GLfloat = ctypes.c_float
GLclampf = ctypes.c_float
GLdouble = ctypes.c_double
GLclampd = ctypes.c_double

GLintptr = ctypes.POINTER(ctypes.c_int)

class _cl_context(ctypes.Structure):
  pass

class _cl_event(ctypes.Structure):
  pass

GLsync = ctypes.c_void_p

GLint64 = ctypes.c_int64
GLint64EXT = ctypes.c_int64
GLuint64 = ctypes.c_uint64
GLuint64EXT = ctypes.c_uint64

GLhalfNV = ctypes.c_uint16
GLhalfARB = ctypes.c_uint16

GLsizeiptrARB = GLsizeiptr = GLsizei
GLintptrARB = GLintptr = GLint
size_t = ctypes.c_ulong

GLhandleARB = ctypes.c_uint

GLvdpauSurfaceNV = GLintptr

GLDEBUGPROCARB = ctypes.WINFUNCTYPE(None, GLenum,GLenum,GLuint,GLenum,GLsizei,ctypes.POINTER(GLchar),ctypes.c_void_p)
GLDEBUGPROCAMD = ctypes.WINFUNCTYPE(None, GLuint,GLenum,GLenum,GLsizei,ctypes.POINTER(GLchar),ctypes.c_void_p)
GLDEBUGPROC = ctypes.WINFUNCTYPE(None, GLenum,GLenum,GLuint,GLenum,GLsizei,ctypes.POINTER(GLchar),ctypes.c_void_p)

def GL_EXT(name):
  name = "SUPPORTS_" + name
  def supports_fn():
    return ctypes.c_int.in_dll(_rtgugl, name)
  globals()[name] = supports_fn

def GL_PROC(catname, resType, name, args):
  fn_type = ctypes.WINFUNCTYPE(resType, *args)
  fn = fn_type.in_dll(_rtgugl, name)
  globals()[name] = fn
  
# GENERATED CODE

GL_EXT('GL_3DFX_multisample')
GL_EXT('GL_3DFX_tbuffer')
GL_EXT('GL_3DFX_texture_compression_FXT1')
GL_EXT('GL_AMD_blend_minmax_factor')
GL_EXT('GL_AMD_conservative_depth')
GL_EXT('GL_AMD_debug_output')
GL_EXT('GL_AMD_depth_clamp_separate')
GL_EXT('GL_AMD_draw_buffers_blend')
GL_EXT('GL_AMD_multi_draw_indirect')
GL_EXT('GL_AMD_name_gen_delete')
GL_EXT('GL_AMD_performance_monitor')
GL_EXT('GL_AMD_pinned_memory')
GL_EXT('GL_AMD_query_buffer_object')
GL_EXT('GL_AMD_sample_positions')
GL_EXT('GL_AMD_seamless_cubemap_per_texture')
GL_EXT('GL_AMD_shader_stencil_export')
GL_EXT('GL_AMD_stencil_operation_extended')
GL_EXT('GL_AMD_texture_texture4')
GL_EXT('GL_AMD_transform_feedback3_lines_triangles')
GL_EXT('GL_AMD_vertex_shader_layer')
GL_EXT('GL_AMD_vertex_shader_tessellator')
GL_EXT('GL_AMD_vertex_shader_viewport_index')
GL_EXT('GL_APPLE_aux_depth_stencil')
GL_EXT('GL_APPLE_client_storage')
GL_EXT('GL_APPLE_element_array')
GL_EXT('GL_APPLE_fence')
GL_EXT('GL_APPLE_float_pixels')
GL_EXT('GL_APPLE_flush_buffer_range')
GL_EXT('GL_APPLE_object_purgeable')
GL_EXT('GL_APPLE_rgb_422')
GL_EXT('GL_APPLE_row_bytes')
GL_EXT('GL_APPLE_specular_vector')
GL_EXT('GL_APPLE_texture_range')
GL_EXT('GL_APPLE_transform_hint')
GL_EXT('GL_APPLE_vertex_array_object')
GL_EXT('GL_APPLE_vertex_array_range')
GL_EXT('GL_APPLE_vertex_program_evaluators')
GL_EXT('GL_APPLE_ycbcr_422')
GL_EXT('GL_ARB_ES2_compatibility')
GL_EXT('GL_ARB_ES3_compatibility')
GL_EXT('GL_ARB_arrays_of_arrays')
GL_EXT('GL_ARB_base_instance')
GL_EXT('GL_ARB_blend_func_extended')
GL_EXT('GL_ARB_cl_event')
GL_EXT('GL_ARB_clear_buffer_object')
GL_EXT('GL_ARB_color_buffer_float')
GL_EXT('GL_ARB_compatibility')
GL_EXT('GL_ARB_compressed_texture_pixel_storage')
GL_EXT('GL_ARB_compute_shader')
GL_EXT('GL_ARB_conservative_depth')
GL_EXT('GL_ARB_copy_buffer')
GL_EXT('GL_ARB_copy_image')
GL_EXT('GL_ARB_debug_output')
GL_EXT('GL_ARB_depth_buffer_float')
GL_EXT('GL_ARB_depth_clamp')
GL_EXT('GL_ARB_depth_texture')
GL_EXT('GL_ARB_draw_buffers')
GL_EXT('GL_ARB_draw_buffers_blend')
GL_EXT('GL_ARB_draw_elements_base_vertex')
GL_EXT('GL_ARB_draw_indirect')
GL_EXT('GL_ARB_draw_instanced')
GL_EXT('GL_ARB_explicit_attrib_location')
GL_EXT('GL_ARB_explicit_uniform_location')
GL_EXT('GL_ARB_fragment_coord_conventions')
GL_EXT('GL_ARB_fragment_layer_viewport')
GL_EXT('GL_ARB_fragment_program')
GL_EXT('GL_ARB_fragment_program_shadow')
GL_EXT('GL_ARB_fragment_shader')
GL_EXT('GL_ARB_framebuffer_no_attachments')
GL_EXT('GL_ARB_framebuffer_object')
GL_EXT('GL_ARB_framebuffer_object_DEPRECATED')
GL_EXT('GL_ARB_framebuffer_sRGB')
GL_EXT('GL_ARB_geometry_shader4')
GL_EXT('GL_ARB_get_program_binary')
GL_EXT('GL_ARB_gpu_shader5')
GL_EXT('GL_ARB_gpu_shader_fp64')
GL_EXT('GL_ARB_half_float_pixel')
GL_EXT('GL_ARB_half_float_vertex')
GL_EXT('GL_ARB_imaging')
GL_EXT('GL_ARB_imaging_DEPRECATED')
GL_EXT('GL_ARB_instanced_arrays')
GL_EXT('GL_ARB_internalformat_query')
GL_EXT('GL_ARB_internalformat_query2')
GL_EXT('GL_ARB_invalidate_subdata')
GL_EXT('GL_ARB_map_buffer_alignment')
GL_EXT('GL_ARB_map_buffer_range')
GL_EXT('GL_ARB_matrix_palette')
GL_EXT('GL_ARB_multi_draw_indirect')
GL_EXT('GL_ARB_multisample')
GL_EXT('GL_ARB_multitexture')
GL_EXT('GL_ARB_occlusion_query')
GL_EXT('GL_ARB_occlusion_query2')
GL_EXT('GL_ARB_pixel_buffer_object')
GL_EXT('GL_ARB_point_parameters')
GL_EXT('GL_ARB_point_sprite')
GL_EXT('GL_ARB_program_interface_query')
GL_EXT('GL_ARB_provoking_vertex')
GL_EXT('GL_ARB_robust_buffer_access_behavior')
GL_EXT('GL_ARB_robustness')
GL_EXT('GL_ARB_robustness_isolation')
GL_EXT('GL_ARB_sample_shading')
GL_EXT('GL_ARB_sampler_objects')
GL_EXT('GL_ARB_seamless_cube_map')
GL_EXT('GL_ARB_separate_shader_objects')
GL_EXT('GL_ARB_shader_atomic_counters')
GL_EXT('GL_ARB_shader_bit_encoding')
GL_EXT('GL_ARB_shader_image_load_store')
GL_EXT('GL_ARB_shader_image_size')
GL_EXT('GL_ARB_shader_objects')
GL_EXT('GL_ARB_shader_precision')
GL_EXT('GL_ARB_shader_stencil_export')
GL_EXT('GL_ARB_shader_storage_buffer_object')
GL_EXT('GL_ARB_shader_subroutine')
GL_EXT('GL_ARB_shader_texture_lod')
GL_EXT('GL_ARB_shading_language_100')
GL_EXT('GL_ARB_shading_language_420pack')
GL_EXT('GL_ARB_shading_language_include')
GL_EXT('GL_ARB_shading_language_packing')
GL_EXT('GL_ARB_shadow')
GL_EXT('GL_ARB_shadow_ambient')
GL_EXT('GL_ARB_stencil_texturing')
GL_EXT('GL_ARB_sync')
GL_EXT('GL_ARB_tessellation_shader')
GL_EXT('GL_ARB_texture_border_clamp')
GL_EXT('GL_ARB_texture_buffer_object')
GL_EXT('GL_ARB_texture_buffer_object_rgb32')
GL_EXT('GL_ARB_texture_buffer_range')
GL_EXT('GL_ARB_texture_compression')
GL_EXT('GL_ARB_texture_compression_bptc')
GL_EXT('GL_ARB_texture_compression_rgtc')
GL_EXT('GL_ARB_texture_cube_map')
GL_EXT('GL_ARB_texture_cube_map_array')
GL_EXT('GL_ARB_texture_env_add')
GL_EXT('GL_ARB_texture_env_combine')
GL_EXT('GL_ARB_texture_env_crossbar')
GL_EXT('GL_ARB_texture_env_dot3')
GL_EXT('GL_ARB_texture_float')
GL_EXT('GL_ARB_texture_gather')
GL_EXT('GL_ARB_texture_mirrored_repeat')
GL_EXT('GL_ARB_texture_multisample')
GL_EXT('GL_ARB_texture_non_power_of_two')
GL_EXT('GL_ARB_texture_query_levels')
GL_EXT('GL_ARB_texture_query_lod')
GL_EXT('GL_ARB_texture_rectangle')
GL_EXT('GL_ARB_texture_rg')
GL_EXT('GL_ARB_texture_rgb10_a2ui')
GL_EXT('GL_ARB_texture_storage')
GL_EXT('GL_ARB_texture_storage_multisample')
GL_EXT('GL_ARB_texture_swizzle')
GL_EXT('GL_ARB_texture_view')
GL_EXT('GL_ARB_timer_query')
GL_EXT('GL_ARB_transform_feedback2')
GL_EXT('GL_ARB_transform_feedback3')
GL_EXT('GL_ARB_transform_feedback_instanced')
GL_EXT('GL_ARB_transpose_matrix')
GL_EXT('GL_ARB_uniform_buffer_object')
GL_EXT('GL_ARB_vertex_array_bgra')
GL_EXT('GL_ARB_vertex_array_object')
GL_EXT('GL_ARB_vertex_attrib_64bit')
GL_EXT('GL_ARB_vertex_attrib_binding')
GL_EXT('GL_ARB_vertex_blend')
GL_EXT('GL_ARB_vertex_buffer_object')
GL_EXT('GL_ARB_vertex_program')
GL_EXT('GL_ARB_vertex_shader')
GL_EXT('GL_ARB_vertex_type_2_10_10_10_rev')
GL_EXT('GL_ARB_viewport_array')
GL_EXT('GL_ARB_window_pos')
GL_EXT('GL_ATI_draw_buffers')
GL_EXT('GL_ATI_element_array')
GL_EXT('GL_ATI_envmap_bumpmap')
GL_EXT('GL_ATI_fragment_shader')
GL_EXT('GL_ATI_map_object_buffer')
GL_EXT('GL_ATI_meminfo')
GL_EXT('GL_ATI_pixel_format_float')
GL_EXT('GL_ATI_pn_triangles')
GL_EXT('GL_ATI_separate_stencil')
GL_EXT('GL_ATI_text_fragment_shader')
GL_EXT('GL_ATI_texture_env_combine3')
GL_EXT('GL_ATI_texture_float')
GL_EXT('GL_ATI_texture_mirror_once')
GL_EXT('GL_ATI_vertex_array_object')
GL_EXT('GL_ATI_vertex_attrib_array_object')
GL_EXT('GL_ATI_vertex_streams')
GL_EXT('GL_EXT_422_pixels')
GL_EXT('GL_EXT_abgr')
GL_EXT('GL_EXT_bgra')
GL_EXT('GL_EXT_bindable_uniform')
GL_EXT('GL_EXT_blend_color')
GL_EXT('GL_EXT_blend_equation_separate')
GL_EXT('GL_EXT_blend_func_separate')
GL_EXT('GL_EXT_blend_logic_op')
GL_EXT('GL_EXT_blend_minmax')
GL_EXT('GL_EXT_blend_subtract')
GL_EXT('GL_EXT_clip_volume_hint')
GL_EXT('GL_EXT_cmyka')
GL_EXT('GL_EXT_color_subtable')
GL_EXT('GL_EXT_compiled_vertex_array')
GL_EXT('GL_EXT_convolution')
GL_EXT('GL_EXT_coordinate_frame')
GL_EXT('GL_EXT_copy_texture')
GL_EXT('GL_EXT_cull_vertex')
GL_EXT('GL_EXT_depth_bounds_test')
GL_EXT('GL_EXT_direct_state_access')
GL_EXT('GL_EXT_draw_buffers2')
GL_EXT('GL_EXT_draw_instanced')
GL_EXT('GL_EXT_draw_range_elements')
GL_EXT('GL_EXT_fog_coord')
GL_EXT('GL_EXT_framebuffer_blit')
GL_EXT('GL_EXT_framebuffer_multisample')
GL_EXT('GL_EXT_framebuffer_multisample_blit_scaled')
GL_EXT('GL_EXT_framebuffer_object')
GL_EXT('GL_EXT_framebuffer_sRGB')
GL_EXT('GL_EXT_geometry_shader4')
GL_EXT('GL_EXT_gpu_program_parameters')
GL_EXT('GL_EXT_gpu_shader4')
GL_EXT('GL_EXT_histogram')
GL_EXT('GL_EXT_index_array_formats')
GL_EXT('GL_EXT_index_func')
GL_EXT('GL_EXT_index_material')
GL_EXT('GL_EXT_index_texture')
GL_EXT('GL_EXT_light_texture')
GL_EXT('GL_EXT_misc_attribute')
GL_EXT('GL_EXT_multi_draw_arrays')
GL_EXT('GL_EXT_multisample')
GL_EXT('GL_EXT_packed_depth_stencil')
GL_EXT('GL_EXT_packed_float')
GL_EXT('GL_EXT_packed_pixels')
GL_EXT('GL_EXT_paletted_texture')
GL_EXT('GL_EXT_pixel_buffer_object')
GL_EXT('GL_EXT_pixel_transform')
GL_EXT('GL_EXT_pixel_transform_color_table')
GL_EXT('GL_EXT_point_parameters')
GL_EXT('GL_EXT_polygon_offset')
GL_EXT('GL_EXT_provoking_vertex')
GL_EXT('GL_EXT_rescale_normal')
GL_EXT('GL_EXT_secondary_color')
GL_EXT('GL_EXT_separate_shader_objects')
GL_EXT('GL_EXT_separate_specular_color')
GL_EXT('GL_EXT_shader_image_load_store')
GL_EXT('GL_EXT_shadow_funcs')
GL_EXT('GL_EXT_shared_texture_palette')
GL_EXT('GL_EXT_stencil_clear_tag')
GL_EXT('GL_EXT_stencil_two_side')
GL_EXT('GL_EXT_stencil_wrap')
GL_EXT('GL_EXT_subtexture')
GL_EXT('GL_EXT_texture')
GL_EXT('GL_EXT_texture3D')
GL_EXT('GL_EXT_texture_array')
GL_EXT('GL_EXT_texture_buffer_object')
GL_EXT('GL_EXT_texture_compression_latc')
GL_EXT('GL_EXT_texture_compression_rgtc')
GL_EXT('GL_EXT_texture_compression_s3tc')
GL_EXT('GL_EXT_texture_cube_map')
GL_EXT('GL_EXT_texture_edge_clamp')
GL_EXT('GL_EXT_texture_env_add')
GL_EXT('GL_EXT_texture_env_combine')
GL_EXT('GL_EXT_texture_env_dot3')
GL_EXT('GL_EXT_texture_filter_anisotropic')
GL_EXT('GL_EXT_texture_integer')
GL_EXT('GL_EXT_texture_lod_bias')
GL_EXT('GL_EXT_texture_mirror_clamp')
GL_EXT('GL_EXT_texture_object')
GL_EXT('GL_EXT_texture_perturb_normal')
GL_EXT('GL_EXT_texture_rectangle')
GL_EXT('GL_EXT_texture_sRGB')
GL_EXT('GL_EXT_texture_sRGB_decode')
GL_EXT('GL_EXT_texture_shared_exponent')
GL_EXT('GL_EXT_texture_snorm')
GL_EXT('GL_EXT_texture_swizzle')
GL_EXT('GL_EXT_timer_query')
GL_EXT('GL_EXT_transform_feedback')
GL_EXT('GL_EXT_vertex_array')
GL_EXT('GL_EXT_vertex_array_bgra')
GL_EXT('GL_EXT_vertex_attrib_64bit')
GL_EXT('GL_EXT_vertex_shader')
GL_EXT('GL_EXT_vertex_weighting')
GL_EXT('GL_EXT_x11_sync_object')
GL_EXT('GL_FfdMaskSGIX')
GL_EXT('GL_GREMEDY_frame_terminator')
GL_EXT('GL_GREMEDY_string_marker')
GL_EXT('GL_HP_convolution_border_modes')
GL_EXT('GL_HP_image_transform')
GL_EXT('GL_HP_occlusion_test')
GL_EXT('GL_HP_texture_lighting')
GL_EXT('GL_IBM_cull_vertex')
GL_EXT('GL_IBM_multimode_draw_arrays')
GL_EXT('GL_IBM_rasterpos_clip')
GL_EXT('GL_IBM_texture_mirrored_repeat')
GL_EXT('GL_IBM_vertex_array_lists')
GL_EXT('GL_INGR_color_clamp')
GL_EXT('GL_INGR_interlace_read')
GL_EXT('GL_INGR_palette_buffer')
GL_EXT('GL_INTEL_parallel_arrays')
GL_EXT('GL_INTEL_texture_scissor')
GL_EXT('GL_KHR_debug')
GL_EXT('GL_KHR_texture_compression_astc_ldr')
GL_EXT('GL_MESAX_texture_stack')
GL_EXT('GL_MESA_pack_invert')
GL_EXT('GL_MESA_resize_buffers')
GL_EXT('GL_MESA_window_pos')
GL_EXT('GL_MESA_ycbcr_texture')
GL_EXT('GL_NV_bindless_texture')
GL_EXT('GL_NV_blend_square')
GL_EXT('GL_NV_conditional_render')
GL_EXT('GL_NV_copy_depth_to_color')
GL_EXT('GL_NV_copy_image')
GL_EXT('GL_NV_depth_buffer_float')
GL_EXT('GL_NV_depth_clamp')
GL_EXT('GL_NV_evaluators')
GL_EXT('GL_NV_explicit_multisample')
GL_EXT('GL_NV_fence')
GL_EXT('GL_NV_float_buffer')
GL_EXT('GL_NV_fog_distance')
GL_EXT('GL_NV_fragment_program')
GL_EXT('GL_NV_fragment_program2')
GL_EXT('GL_NV_fragment_program4')
GL_EXT('GL_NV_fragment_program_option')
GL_EXT('GL_NV_framebuffer_multisample_coverage')
GL_EXT('GL_NV_geometry_program4')
GL_EXT('GL_NV_geometry_shader4')
GL_EXT('GL_NV_gpu_program4')
GL_EXT('GL_NV_gpu_program5')
GL_EXT('GL_NV_gpu_shader5')
GL_EXT('GL_NV_half_float')
GL_EXT('GL_NV_light_max_exponent')
GL_EXT('GL_NV_multisample_coverage')
GL_EXT('GL_NV_multisample_filter_hint')
GL_EXT('GL_NV_occlusion_query')
GL_EXT('GL_NV_packed_depth_stencil')
GL_EXT('GL_NV_parameter_buffer_object')
GL_EXT('GL_NV_parameter_buffer_object2')
GL_EXT('GL_NV_path_rendering')
GL_EXT('GL_NV_pixel_data_range')
GL_EXT('GL_NV_point_sprite')
GL_EXT('GL_NV_present_video')
GL_EXT('GL_NV_primitive_restart')
GL_EXT('GL_NV_register_combiners')
GL_EXT('GL_NV_register_combiners2')
GL_EXT('GL_NV_shader_atomic_float')
GL_EXT('GL_NV_shader_buffer_load')
GL_EXT('GL_NV_shader_buffer_store')
GL_EXT('GL_NV_tessellation_program5')
GL_EXT('GL_NV_texgen_emboss')
GL_EXT('GL_NV_texgen_reflection')
GL_EXT('GL_NV_texture_barrier')
GL_EXT('GL_NV_texture_compression_vtc')
GL_EXT('GL_NV_texture_env_combine4')
GL_EXT('GL_NV_texture_expand_normal')
GL_EXT('GL_NV_texture_multisample')
GL_EXT('GL_NV_texture_rectangle')
GL_EXT('GL_NV_texture_shader')
GL_EXT('GL_NV_texture_shader2')
GL_EXT('GL_NV_texture_shader3')
GL_EXT('GL_NV_transform_feedback')
GL_EXT('GL_NV_transform_feedback2')
GL_EXT('GL_NV_vdpau_interop')
GL_EXT('GL_NV_vertex_array_range')
GL_EXT('GL_NV_vertex_array_range2')
GL_EXT('GL_NV_vertex_attrib_integer_64bit')
GL_EXT('GL_NV_vertex_buffer_unified_memory')
GL_EXT('GL_NV_vertex_program')
GL_EXT('GL_NV_vertex_program1_1')
GL_EXT('GL_NV_vertex_program2')
GL_EXT('GL_NV_vertex_program2_option')
GL_EXT('GL_NV_vertex_program3')
GL_EXT('GL_NV_vertex_program4')
GL_EXT('GL_NV_video_capture')
GL_EXT('GL_OES_read_format')
GL_EXT('GL_OML_interlace')
GL_EXT('GL_OML_resample')
GL_EXT('GL_OML_subsample')
GL_EXT('GL_PGI_misc_hints')
GL_EXT('GL_PGI_vertex_hints')
GL_EXT('GL_REND_screen_coordinates')
GL_EXT('GL_S3_s3tc')
GL_EXT('GL_SGIS_detail_texture')
GL_EXT('GL_SGIS_fog_function')
GL_EXT('GL_SGIS_generate_mipmap')
GL_EXT('GL_SGIS_multisample')
GL_EXT('GL_SGIS_pixel_texture')
GL_EXT('GL_SGIS_point_line_texgen')
GL_EXT('GL_SGIS_point_parameters')
GL_EXT('GL_SGIS_sharpen_texture')
GL_EXT('GL_SGIS_texture4D')
GL_EXT('GL_SGIS_texture_border_clamp')
GL_EXT('GL_SGIS_texture_color_mask')
GL_EXT('GL_SGIS_texture_edge_clamp')
GL_EXT('GL_SGIS_texture_filter4')
GL_EXT('GL_SGIS_texture_lod')
GL_EXT('GL_SGIS_texture_select')
GL_EXT('GL_SGIX_async')
GL_EXT('GL_SGIX_async_histogram')
GL_EXT('GL_SGIX_async_pixel')
GL_EXT('GL_SGIX_blend_alpha_minmax')
GL_EXT('GL_SGIX_calligraphic_fragment')
GL_EXT('GL_SGIX_clipmap')
GL_EXT('GL_SGIX_convolution_accuracy')
GL_EXT('GL_SGIX_depth_texture')
GL_EXT('GL_SGIX_flush_raster')
GL_EXT('GL_SGIX_fog_offset')
GL_EXT('GL_SGIX_fog_scale')
GL_EXT('GL_SGIX_fragment_lighting')
GL_EXT('GL_SGIX_framezoom')
GL_EXT('GL_SGIX_impact_pixel_texture')
GL_EXT('GL_SGIX_instruments')
GL_EXT('GL_SGIX_interlace')
GL_EXT('GL_SGIX_ir_instrument1')
GL_EXT('GL_SGIX_list_priority')
GL_EXT('GL_SGIX_pixel_texture')
GL_EXT('GL_SGIX_pixel_tiles')
GL_EXT('GL_SGIX_polynomial_ffd')
GL_EXT('GL_SGIX_reference_plane')
GL_EXT('GL_SGIX_resample')
GL_EXT('GL_SGIX_scalebias_hint')
GL_EXT('GL_SGIX_shadow')
GL_EXT('GL_SGIX_shadow_ambient')
GL_EXT('GL_SGIX_sprite')
GL_EXT('GL_SGIX_subsample')
GL_EXT('GL_SGIX_tag_sample_buffer')
GL_EXT('GL_SGIX_texture_add_env')
GL_EXT('GL_SGIX_texture_coordinate_clamp')
GL_EXT('GL_SGIX_texture_lod_bias')
GL_EXT('GL_SGIX_texture_multi_buffer')
GL_EXT('GL_SGIX_texture_scale_bias')
GL_EXT('GL_SGIX_vertex_preclip')
GL_EXT('GL_SGIX_ycrcb')
GL_EXT('GL_SGIX_ycrcb_subsample')
GL_EXT('GL_SGIX_ycrcba')
GL_EXT('GL_SGI_color_matrix')
GL_EXT('GL_SGI_color_table')
GL_EXT('GL_SGI_depth_pass_instrument')
GL_EXT('GL_SGI_texture_color_table')
GL_EXT('GL_SUNX_constant_data')
GL_EXT('GL_SUN_convolution_border_modes')
GL_EXT('GL_SUN_global_alpha')
GL_EXT('GL_SUN_mesh_array')
GL_EXT('GL_SUN_slice_accum')
GL_EXT('GL_SUN_triangle_list')
GL_EXT('GL_SUN_vertex')
GL_EXT('GL_VERSION_1_1')
GL_EXT('GL_VERSION_1_1_DEPRECATED')
GL_EXT('GL_VERSION_1_2')
GL_EXT('GL_VERSION_1_2_DEPRECATED')
GL_EXT('GL_VERSION_1_3')
GL_EXT('GL_VERSION_1_3_DEPRECATED')
GL_EXT('GL_VERSION_1_4')
GL_EXT('GL_VERSION_1_4_DEPRECATED')
GL_EXT('GL_VERSION_1_5')
GL_EXT('GL_VERSION_1_5_DEPRECATED')
GL_EXT('GL_VERSION_2_0')
GL_EXT('GL_VERSION_2_0_DEPRECATED')
GL_EXT('GL_VERSION_2_1')
GL_EXT('GL_VERSION_2_1_DEPRECATED')
GL_EXT('GL_VERSION_3_0')
GL_EXT('GL_VERSION_3_0_DEPRECATED')
GL_EXT('GL_VERSION_3_1')
GL_EXT('GL_VERSION_3_2')
GL_EXT('GL_VERSION_3_3')
GL_EXT('GL_VERSION_4_0')
GL_EXT('GL_VERSION_4_1')
GL_EXT('GL_VERSION_4_2')
GL_EXT('GL_VERSION_4_3')
GL_EXT('GL_WIN_phong_shading')
GL_EXT('GL_WIN_specular_fog')

"""
GL_EXT('WGL_3DL_stereo_control')
GL_EXT('WGL_AMD_gpu_association')
GL_EXT('WGL_ARB_buffer_region')
GL_EXT('WGL_ARB_create_context')
GL_EXT('WGL_ARB_create_context_profile')
GL_EXT('WGL_ARB_create_context_robustness')
GL_EXT('WGL_ARB_extensions_string')
GL_EXT('WGL_ARB_make_current_read')
GL_EXT('WGL_ARB_pbuffer')
GL_EXT('WGL_ARB_pixel_format')
GL_EXT('WGL_ARB_pixel_format_float')
GL_EXT('WGL_ARB_render_texture')
GL_EXT('WGL_EXT_create_context_es2_profile')
GL_EXT('WGL_EXT_depth_float')
GL_EXT('WGL_EXT_display_color_table')
GL_EXT('WGL_EXT_extensions_string')
GL_EXT('WGL_EXT_make_current_read')
GL_EXT('WGL_EXT_pbuffer')
GL_EXT('WGL_EXT_pixel_format')
GL_EXT('WGL_EXT_pixel_format_packed_float')
GL_EXT('WGL_EXT_swap_control')
GL_EXT('WGL_EXT_swap_control_tear')
GL_EXT('WGL_I3D_digital_video_control')
GL_EXT('WGL_I3D_gamma')
GL_EXT('WGL_I3D_genlock')
GL_EXT('WGL_I3D_image_buffer')
GL_EXT('WGL_I3D_swap_frame_lock')
GL_EXT('WGL_I3D_swap_frame_usage')
GL_EXT('WGL_NV_DX_interop')
GL_EXT('WGL_NV_DX_interop2')
GL_EXT('WGL_NV_gpu_affinity')
GL_EXT('WGL_NV_render_depth_texture')
GL_EXT('WGL_NV_render_texture_rectangle')
GL_EXT('WGL_NV_swap_group')
GL_EXT('WGL_NV_video_output')
GL_EXT('WGL_OML_sync_control')
"""

# 3DFX_multisample
GL_MULTISAMPLE_3DFX = 0x86B2
GL_SAMPLE_BUFFERS_3DFX = 0x86B3
GL_SAMPLES_3DFX = 0x86B4
GL_MULTISAMPLE_BIT_3DFX = 0x20000000
WGL_SAMPLE_BUFFERS_3DFX = 0x2060
WGL_SAMPLES_3DFX = 0x2061
# 3DFX_tbuffer
# 3DFX_texture_compression_FXT1
GL_COMPRESSED_RGB_FXT1_3DFX = 0x86B0
GL_COMPRESSED_RGBA_FXT1_3DFX = 0x86B1
# AMD_blend_minmax_factor
GL_FACTOR_MIN_AMD = 0x901C
GL_FACTOR_MAX_AMD = 0x901D
# AMD_conservative_depth
# AMD_debug_output
GL_MAX_DEBUG_LOGGED_MESSAGES_AMD = 0x9144
GL_MAX_DEBUG_MESSAGE_LENGTH_AMD = 0x9143
GL_DEBUG_LOGGED_MESSAGES_AMD = 0x9145
GL_DEBUG_SEVERITY_HIGH_AMD = 0x9146
GL_DEBUG_SEVERITY_MEDIUM_AMD = 0x9147
GL_DEBUG_SEVERITY_LOW_AMD = 0x9148
GL_DEBUG_CATEGORY_API_ERROR_AMD = 0x9149
GL_DEBUG_CATEGORY_WINDOW_SYSTEM_AMD = 0x914A
GL_DEBUG_CATEGORY_DEPRECATION_AMD = 0x914B
GL_DEBUG_CATEGORY_UNDEFINED_BEHAVIOR_AMD = 0x914C
GL_DEBUG_CATEGORY_PERFORMANCE_AMD = 0x914D
GL_DEBUG_CATEGORY_SHADER_COMPILER_AMD = 0x914E
GL_DEBUG_CATEGORY_APPLICATION_AMD = 0x914F
GL_DEBUG_CATEGORY_OTHER_AMD = 0x9150
# AMD_depth_clamp_separate
GL_DEPTH_CLAMP_NEAR_AMD = 0x901E
GL_DEPTH_CLAMP_FAR_AMD = 0x901F
# AMD_draw_buffers_blend
# AMD_multi_draw_indirect
# AMD_name_gen_delete
GL_DATA_BUFFER_AMD = 0x9151
GL_PERFORMANCE_MONITOR_AMD = 0x9152
GL_QUERY_OBJECT_AMD = 0x9153
GL_VERTEX_ARRAY_OBJECT_AMD = 0x9154
GL_SAMPLER_OBJECT_AMD = 0x9155
# AMD_performance_monitor
GL_COUNTER_TYPE_AMD = 0x8BC0
GL_COUNTER_RANGE_AMD = 0x8BC1
GL_UNSIGNED_INT64_AMD = 0x8BC2
GL_PERCENTAGE_AMD = 0x8BC3
GL_PERFMON_RESULT_AVAILABLE_AMD = 0x8BC4
GL_PERFMON_RESULT_SIZE_AMD = 0x8BC5
GL_PERFMON_RESULT_AMD = 0x8BC6
# AMD_pinned_memory
GL_EXTERNAL_VIRTUAL_MEMORY_BUFFER_AMD = 0x9160
# AMD_query_buffer_object
GL_QUERY_BUFFER_AMD = 0x9192
GL_QUERY_BUFFER_BINDING_AMD = 0x9193
GL_QUERY_RESULT_NO_WAIT_AMD = 0x9194
# AMD_sample_positions
GL_SUBSAMPLE_DISTANCE_AMD = 0x883F
# AMD_seamless_cubemap_per_texture
# AMD_shader_stencil_export
# AMD_stencil_operation_extended
GL_SET_AMD = 0x874A
GL_REPLACE_VALUE_AMD = 0x874B
GL_STENCIL_OP_VALUE_AMD = 0x874C
GL_STENCIL_BACK_OP_VALUE_AMD = 0x874D
# AMD_texture_texture4
# AMD_transform_feedback3_lines_triangles
# AMD_vertex_shader_layer
# AMD_vertex_shader_tessellator
GL_SAMPLER_BUFFER_AMD = 0x9001
GL_INT_SAMPLER_BUFFER_AMD = 0x9002
GL_UNSIGNED_INT_SAMPLER_BUFFER_AMD = 0x9003
GL_TESSELLATION_MODE_AMD = 0x9004
GL_TESSELLATION_FACTOR_AMD = 0x9005
GL_DISCRETE_AMD = 0x9006
GL_CONTINUOUS_AMD = 0x9007
# AMD_vertex_shader_viewport_index
# APPLE_aux_depth_stencil
GL_AUX_DEPTH_STENCIL_APPLE = 0x8A14
# APPLE_client_storage
GL_UNPACK_CLIENT_STORAGE_APPLE = 0x85B2
# APPLE_element_array
GL_ELEMENT_ARRAY_APPLE = 0x8A0C
GL_ELEMENT_ARRAY_TYPE_APPLE = 0x8A0D
GL_ELEMENT_ARRAY_POINTER_APPLE = 0x8A0E
# APPLE_fence
GL_DRAW_PIXELS_APPLE = 0x8A0A
GL_FENCE_APPLE = 0x8A0B
# APPLE_float_pixels
GL_HALF_APPLE = 0x140B
GL_RGBA_FLOAT32_APPLE = 0x8814
GL_RGB_FLOAT32_APPLE = 0x8815
GL_ALPHA_FLOAT32_APPLE = 0x8816
GL_INTENSITY_FLOAT32_APPLE = 0x8817
GL_LUMINANCE_FLOAT32_APPLE = 0x8818
GL_LUMINANCE_ALPHA_FLOAT32_APPLE = 0x8819
GL_RGBA_FLOAT16_APPLE = 0x881A
GL_RGB_FLOAT16_APPLE = 0x881B
GL_ALPHA_FLOAT16_APPLE = 0x881C
GL_INTENSITY_FLOAT16_APPLE = 0x881D
GL_LUMINANCE_FLOAT16_APPLE = 0x881E
GL_LUMINANCE_ALPHA_FLOAT16_APPLE = 0x881F
GL_COLOR_FLOAT_APPLE = 0x8A0F
# APPLE_flush_buffer_range
GL_BUFFER_SERIALIZED_MODIFY_APPLE = 0x8A12
GL_BUFFER_FLUSHING_UNMAP_APPLE = 0x8A13
# APPLE_object_purgeable
GL_BUFFER_OBJECT_APPLE = 0x85B3
GL_RELEASED_APPLE = 0x8A19
GL_VOLATILE_APPLE = 0x8A1A
GL_RETAINED_APPLE = 0x8A1B
GL_UNDEFINED_APPLE = 0x8A1C
GL_PURGEABLE_APPLE = 0x8A1D
# APPLE_rgb_422
GL_RGB_422_APPLE = 0x8A1F
# APPLE_row_bytes
GL_PACK_ROW_BYTES_APPLE = 0x8A15
GL_UNPACK_ROW_BYTES_APPLE = 0x8A16
# APPLE_specular_vector
GL_LIGHT_MODEL_SPECULAR_VECTOR_APPLE = 0x85B0
# APPLE_texture_range
GL_TEXTURE_RANGE_LENGTH_APPLE = 0x85B7
GL_TEXTURE_RANGE_POINTER_APPLE = 0x85B8
GL_TEXTURE_STORAGE_HINT_APPLE = 0x85BC
GL_STORAGE_PRIVATE_APPLE = 0x85BD
# APPLE_transform_hint
GL_TRANSFORM_HINT_APPLE = 0x85B1
# APPLE_vertex_array_object
GL_VERTEX_ARRAY_BINDING_APPLE = 0x85B5
# APPLE_vertex_array_range
GL_VERTEX_ARRAY_RANGE_APPLE = 0x851D
GL_VERTEX_ARRAY_RANGE_LENGTH_APPLE = 0x851E
GL_VERTEX_ARRAY_STORAGE_HINT_APPLE = 0x851F
GL_VERTEX_ARRAY_RANGE_POINTER_APPLE = 0x8521
GL_STORAGE_CLIENT_APPLE = 0x85B4
GL_STORAGE_CACHED_APPLE = 0x85BE
GL_STORAGE_SHARED_APPLE = 0x85BF
# APPLE_vertex_program_evaluators
GL_VERTEX_ATTRIB_MAP1_APPLE = 0x8A00
GL_VERTEX_ATTRIB_MAP2_APPLE = 0x8A01
GL_VERTEX_ATTRIB_MAP1_SIZE_APPLE = 0x8A02
GL_VERTEX_ATTRIB_MAP1_COEFF_APPLE = 0x8A03
GL_VERTEX_ATTRIB_MAP1_ORDER_APPLE = 0x8A04
GL_VERTEX_ATTRIB_MAP1_DOMAIN_APPLE = 0x8A05
GL_VERTEX_ATTRIB_MAP2_SIZE_APPLE = 0x8A06
GL_VERTEX_ATTRIB_MAP2_COEFF_APPLE = 0x8A07
GL_VERTEX_ATTRIB_MAP2_ORDER_APPLE = 0x8A08
GL_VERTEX_ATTRIB_MAP2_DOMAIN_APPLE = 0x8A09
# APPLE_ycbcr_422
GL_YCBCR_422_APPLE = 0x85B9
GL_UNSIGNED_SHORT_8_8_APPLE = 0x85BA
GL_UNSIGNED_SHORT_8_8_REV_APPLE = 0x85BB
# ARB_ES2_compatibility
GL_FIXED = 0x140C
GL_IMPLEMENTATION_COLOR_READ_TYPE = 0x8B9A
GL_IMPLEMENTATION_COLOR_READ_FORMAT = 0x8B9B
GL_LOW_FLOAT = 0x8DF0
GL_MEDIUM_FLOAT = 0x8DF1
GL_HIGH_FLOAT = 0x8DF2
GL_LOW_INT = 0x8DF3
GL_MEDIUM_INT = 0x8DF4
GL_HIGH_INT = 0x8DF5
GL_SHADER_COMPILER = 0x8DFA
GL_SHADER_BINARY_FORMATS = 0x8DF8
GL_NUM_SHADER_BINARY_FORMATS = 0x8DF9
GL_MAX_VERTEX_UNIFORM_VECTORS = 0x8DFB
GL_MAX_VARYING_VECTORS = 0x8DFC
GL_MAX_FRAGMENT_UNIFORM_VECTORS = 0x8DFD
GL_RGB565 = 0x8D62
# ARB_ES3_compatibility
GL_COMPRESSED_RGB8_ETC2 = 0x9274
GL_COMPRESSED_SRGB8_ETC2 = 0x9275
GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9276
GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9277
GL_COMPRESSED_RGBA8_ETC2_EAC = 0x9278
GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC = 0x9279
GL_COMPRESSED_R11_EAC = 0x9270
GL_COMPRESSED_SIGNED_R11_EAC = 0x9271
GL_COMPRESSED_RG11_EAC = 0x9272
GL_COMPRESSED_SIGNED_RG11_EAC = 0x9273
GL_PRIMITIVE_RESTART_FIXED_INDEX = 0x8D69
GL_ANY_SAMPLES_PASSED_CONSERVATIVE = 0x8D6A
GL_MAX_ELEMENT_INDEX = 0x8D6B
# ARB_arrays_of_arrays
# ARB_base_instance
# ARB_blend_func_extended
GL_SRC1_COLOR = 0x88F9
GL_ONE_MINUS_SRC1_COLOR = 0x88FA
GL_ONE_MINUS_SRC1_ALPHA = 0x88FB
GL_MAX_DUAL_SOURCE_DRAW_BUFFERS = 0x88FC
# ARB_cl_event
GL_SYNC_CL_EVENT_ARB = 0x8240
GL_SYNC_CL_EVENT_COMPLETE_ARB = 0x8241
# ARB_clear_buffer_object
# ARB_color_buffer_float
GL_RGBA_FLOAT_MODE_ARB = 0x8820
GL_CLAMP_VERTEX_COLOR_ARB = 0x891A
GL_CLAMP_FRAGMENT_COLOR_ARB = 0x891B
GL_CLAMP_READ_COLOR_ARB = 0x891C
GL_FIXED_ONLY_ARB = 0x891D
# ARB_compatibility
# ARB_compressed_texture_pixel_storage
GL_UNPACK_COMPRESSED_BLOCK_WIDTH = 0x9127
GL_UNPACK_COMPRESSED_BLOCK_HEIGHT = 0x9128
GL_UNPACK_COMPRESSED_BLOCK_DEPTH = 0x9129
GL_UNPACK_COMPRESSED_BLOCK_SIZE = 0x912A
GL_PACK_COMPRESSED_BLOCK_WIDTH = 0x912B
GL_PACK_COMPRESSED_BLOCK_HEIGHT = 0x912C
GL_PACK_COMPRESSED_BLOCK_DEPTH = 0x912D
GL_PACK_COMPRESSED_BLOCK_SIZE = 0x912E
# ARB_compute_shader
GL_COMPUTE_SHADER = 0x91B9
GL_MAX_COMPUTE_UNIFORM_BLOCKS = 0x91BB
GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS = 0x91BC
GL_MAX_COMPUTE_IMAGE_UNIFORMS = 0x91BD
GL_MAX_COMPUTE_SHARED_MEMORY_SIZE = 0x8262
GL_MAX_COMPUTE_UNIFORM_COMPONENTS = 0x8263
GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS = 0x8264
GL_MAX_COMPUTE_ATOMIC_COUNTERS = 0x8265
GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS = 0x8266
GL_MAX_COMPUTE_LOCAL_INVOCATIONS = 0x90EB
GL_MAX_COMPUTE_WORK_GROUP_COUNT = 0x91BE
GL_MAX_COMPUTE_WORK_GROUP_SIZE = 0x91BF
GL_COMPUTE_LOCAL_WORK_SIZE = 0x8267
GL_UNIFORM_BLOCK_REFERENCED_BY_COMPUTE_SHADER = 0x90EC
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_COMPUTE_SHADER = 0x90ED
GL_DISPATCH_INDIRECT_BUFFER = 0x90EE
GL_DISPATCH_INDIRECT_BUFFER_BINDING = 0x90EF
GL_COMPUTE_SHADER_BIT = 0x00000020
# ARB_conservative_depth
# ARB_copy_buffer
GL_COPY_READ_BUFFER_BINDING = 0x8F36
GL_COPY_READ_BUFFER = 0x8F36 # GL_COPY_READ_BUFFER_BINDING
GL_COPY_WRITE_BUFFER_BINDING = 0x8F37
GL_COPY_WRITE_BUFFER = 0x8F37 # GL_COPY_WRITE_BUFFER_BINDING
# ARB_copy_image
# ARB_debug_output
GL_DEBUG_OUTPUT_SYNCHRONOUS_ARB = 0x8242
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH_ARB = 0x8243
GL_DEBUG_CALLBACK_FUNCTION_ARB = 0x8244
GL_DEBUG_CALLBACK_USER_PARAM_ARB = 0x8245
GL_DEBUG_SOURCE_API_ARB = 0x8246
GL_DEBUG_SOURCE_WINDOW_SYSTEM_ARB = 0x8247
GL_DEBUG_SOURCE_SHADER_COMPILER_ARB = 0x8248
GL_DEBUG_SOURCE_THIRD_PARTY_ARB = 0x8249
GL_DEBUG_SOURCE_APPLICATION_ARB = 0x824A
GL_DEBUG_SOURCE_OTHER_ARB = 0x824B
GL_DEBUG_TYPE_ERROR_ARB = 0x824C
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR_ARB = 0x824D
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR_ARB = 0x824E
GL_DEBUG_TYPE_PORTABILITY_ARB = 0x824F
GL_DEBUG_TYPE_PERFORMANCE_ARB = 0x8250
GL_DEBUG_TYPE_OTHER_ARB = 0x8251
GL_MAX_DEBUG_MESSAGE_LENGTH_ARB = 0x9143
GL_MAX_DEBUG_LOGGED_MESSAGES_ARB = 0x9144
GL_DEBUG_LOGGED_MESSAGES_ARB = 0x9145
GL_DEBUG_SEVERITY_HIGH_ARB = 0x9146
GL_DEBUG_SEVERITY_MEDIUM_ARB = 0x9147
GL_DEBUG_SEVERITY_LOW_ARB = 0x9148
# ARB_depth_buffer_float
GL_DEPTH_COMPONENT32F = 0x8CAC
GL_DEPTH32F_STENCIL8 = 0x8CAD
GL_FLOAT_32_UNSIGNED_INT_24_8_REV = 0x8DAD
# ARB_depth_clamp
GL_DEPTH_CLAMP = 0x864F
# ARB_depth_texture
GL_DEPTH_COMPONENT16_ARB = 0x81A5
GL_DEPTH_COMPONENT24_ARB = 0x81A6
GL_DEPTH_COMPONENT32_ARB = 0x81A7
GL_TEXTURE_DEPTH_SIZE_ARB = 0x884A
GL_DEPTH_TEXTURE_MODE_ARB = 0x884B
# ARB_draw_buffers
GL_MAX_DRAW_BUFFERS_ARB = 0x8824
GL_DRAW_BUFFER0_ARB = 0x8825
GL_DRAW_BUFFER1_ARB = 0x8826
GL_DRAW_BUFFER2_ARB = 0x8827
GL_DRAW_BUFFER3_ARB = 0x8828
GL_DRAW_BUFFER4_ARB = 0x8829
GL_DRAW_BUFFER5_ARB = 0x882A
GL_DRAW_BUFFER6_ARB = 0x882B
GL_DRAW_BUFFER7_ARB = 0x882C
GL_DRAW_BUFFER8_ARB = 0x882D
GL_DRAW_BUFFER9_ARB = 0x882E
GL_DRAW_BUFFER10_ARB = 0x882F
GL_DRAW_BUFFER11_ARB = 0x8830
GL_DRAW_BUFFER12_ARB = 0x8831
GL_DRAW_BUFFER13_ARB = 0x8832
GL_DRAW_BUFFER14_ARB = 0x8833
GL_DRAW_BUFFER15_ARB = 0x8834
# ARB_draw_buffers_blend
# ARB_draw_elements_base_vertex
# ARB_draw_indirect
GL_DRAW_INDIRECT_BUFFER = 0x8F3F
GL_DRAW_INDIRECT_BUFFER_BINDING = 0x8F43
# ARB_draw_instanced
# ARB_explicit_attrib_location
# ARB_explicit_uniform_location
GL_MAX_UNIFORM_LOCATIONS = 0x826E
# ARB_fragment_coord_conventions
# ARB_fragment_layer_viewport
# ARB_fragment_program
GL_FRAGMENT_PROGRAM_ARB = 0x8804
GL_PROGRAM_ALU_INSTRUCTIONS_ARB = 0x8805
GL_PROGRAM_TEX_INSTRUCTIONS_ARB = 0x8806
GL_PROGRAM_TEX_INDIRECTIONS_ARB = 0x8807
GL_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB = 0x8808
GL_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB = 0x8809
GL_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB = 0x880A
GL_MAX_PROGRAM_ALU_INSTRUCTIONS_ARB = 0x880B
GL_MAX_PROGRAM_TEX_INSTRUCTIONS_ARB = 0x880C
GL_MAX_PROGRAM_TEX_INDIRECTIONS_ARB = 0x880D
GL_MAX_PROGRAM_NATIVE_ALU_INSTRUCTIONS_ARB = 0x880E
GL_MAX_PROGRAM_NATIVE_TEX_INSTRUCTIONS_ARB = 0x880F
GL_MAX_PROGRAM_NATIVE_TEX_INDIRECTIONS_ARB = 0x8810
GL_MAX_TEXTURE_COORDS_ARB = 0x8871
GL_MAX_TEXTURE_IMAGE_UNITS_ARB = 0x8872
# ARB_fragment_program_shadow
# ARB_fragment_shader
GL_FRAGMENT_SHADER_ARB = 0x8B30
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS_ARB = 0x8B49
GL_FRAGMENT_SHADER_DERIVATIVE_HINT_ARB = 0x8B8B
# ARB_framebuffer_no_attachments
GL_FRAMEBUFFER_DEFAULT_WIDTH = 0x9310
GL_FRAMEBUFFER_DEFAULT_HEIGHT = 0x9311
GL_FRAMEBUFFER_DEFAULT_LAYERS = 0x9312
GL_FRAMEBUFFER_DEFAULT_SAMPLES = 0x9313
GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS = 0x9314
GL_MAX_FRAMEBUFFER_WIDTH = 0x9315
GL_MAX_FRAMEBUFFER_HEIGHT = 0x9316
GL_MAX_FRAMEBUFFER_LAYERS = 0x9317
GL_MAX_FRAMEBUFFER_SAMPLES = 0x9318
# ARB_framebuffer_object
GL_INVALID_FRAMEBUFFER_OPERATION = 0x0506
GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING = 0x8210
GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE = 0x8211
GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE = 0x8212
GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE = 0x8213
GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE = 0x8214
GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE = 0x8215
GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE = 0x8216
GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE = 0x8217
GL_FRAMEBUFFER_DEFAULT = 0x8218
GL_FRAMEBUFFER_UNDEFINED = 0x8219
GL_DEPTH_STENCIL_ATTACHMENT = 0x821A
GL_MAX_RENDERBUFFER_SIZE = 0x84E8
GL_DEPTH_STENCIL = 0x84F9
GL_UNSIGNED_INT_24_8 = 0x84FA
GL_DEPTH24_STENCIL8 = 0x88F0
GL_TEXTURE_STENCIL_SIZE = 0x88F1
GL_TEXTURE_RED_TYPE = 0x8C10
GL_TEXTURE_GREEN_TYPE = 0x8C11
GL_TEXTURE_BLUE_TYPE = 0x8C12
GL_TEXTURE_ALPHA_TYPE = 0x8C13
GL_TEXTURE_DEPTH_TYPE = 0x8C16
GL_UNSIGNED_NORMALIZED = 0x8C17
GL_FRAMEBUFFER_BINDING = 0x8CA6
GL_DRAW_FRAMEBUFFER_BINDING = 0x8CA6 # GL_FRAMEBUFFER_BINDING
GL_RENDERBUFFER_BINDING = 0x8CA7
GL_READ_FRAMEBUFFER = 0x8CA8
GL_DRAW_FRAMEBUFFER = 0x8CA9
GL_READ_FRAMEBUFFER_BINDING = 0x8CAA
GL_RENDERBUFFER_SAMPLES = 0x8CAB
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 0x8CD0
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 0x8CD1
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 0x8CD2
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 0x8CD3
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER = 0x8CD4
GL_FRAMEBUFFER_COMPLETE = 0x8CD5
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 0x8CD6
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 0x8CD7
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER = 0x8CDB
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER = 0x8CDC
GL_FRAMEBUFFER_UNSUPPORTED = 0x8CDD
GL_MAX_COLOR_ATTACHMENTS = 0x8CDF
GL_COLOR_ATTACHMENT0 = 0x8CE0
GL_COLOR_ATTACHMENT1 = 0x8CE1
GL_COLOR_ATTACHMENT2 = 0x8CE2
GL_COLOR_ATTACHMENT3 = 0x8CE3
GL_COLOR_ATTACHMENT4 = 0x8CE4
GL_COLOR_ATTACHMENT5 = 0x8CE5
GL_COLOR_ATTACHMENT6 = 0x8CE6
GL_COLOR_ATTACHMENT7 = 0x8CE7
GL_COLOR_ATTACHMENT8 = 0x8CE8
GL_COLOR_ATTACHMENT9 = 0x8CE9
GL_COLOR_ATTACHMENT10 = 0x8CEA
GL_COLOR_ATTACHMENT11 = 0x8CEB
GL_COLOR_ATTACHMENT12 = 0x8CEC
GL_COLOR_ATTACHMENT13 = 0x8CED
GL_COLOR_ATTACHMENT14 = 0x8CEE
GL_COLOR_ATTACHMENT15 = 0x8CEF
GL_DEPTH_ATTACHMENT = 0x8D00
GL_STENCIL_ATTACHMENT = 0x8D20
GL_FRAMEBUFFER = 0x8D40
GL_RENDERBUFFER = 0x8D41
GL_RENDERBUFFER_WIDTH = 0x8D42
GL_RENDERBUFFER_HEIGHT = 0x8D43
GL_RENDERBUFFER_INTERNAL_FORMAT = 0x8D44
GL_STENCIL_INDEX1 = 0x8D46
GL_STENCIL_INDEX4 = 0x8D47
GL_STENCIL_INDEX8 = 0x8D48
GL_STENCIL_INDEX16 = 0x8D49
GL_RENDERBUFFER_RED_SIZE = 0x8D50
GL_RENDERBUFFER_GREEN_SIZE = 0x8D51
GL_RENDERBUFFER_BLUE_SIZE = 0x8D52
GL_RENDERBUFFER_ALPHA_SIZE = 0x8D53
GL_RENDERBUFFER_DEPTH_SIZE = 0x8D54
GL_RENDERBUFFER_STENCIL_SIZE = 0x8D55
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE = 0x8D56
GL_MAX_SAMPLES = 0x8D57
# ARB_framebuffer_object_DEPRECATED
GL_INDEX = 0x8222
GL_TEXTURE_LUMINANCE_TYPE = 0x8C14
GL_TEXTURE_INTENSITY_TYPE = 0x8C15
# ARB_framebuffer_sRGB
GL_FRAMEBUFFER_SRGB = 0x8DB9
WGL_FRAMEBUFFER_SRGB_CAPABLE_ARB = 0x20A9
# ARB_geometry_shader4
GL_LINES_ADJACENCY_ARB = 0x000A
GL_LINE_STRIP_ADJACENCY_ARB = 0x000B
GL_TRIANGLES_ADJACENCY_ARB = 0x000C
GL_TRIANGLE_STRIP_ADJACENCY_ARB = 0x000D
GL_PROGRAM_POINT_SIZE_ARB = 0x8642
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_ARB = 0x8C29
GL_FRAMEBUFFER_ATTACHMENT_LAYERED_ARB = 0x8DA7
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_ARB = 0x8DA8
GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_ARB = 0x8DA9
GL_GEOMETRY_SHADER_ARB = 0x8DD9
GL_GEOMETRY_VERTICES_OUT_ARB = 0x8DDA
GL_GEOMETRY_INPUT_TYPE_ARB = 0x8DDB
GL_GEOMETRY_OUTPUT_TYPE_ARB = 0x8DDC
GL_MAX_GEOMETRY_VARYING_COMPONENTS_ARB = 0x8DDD
GL_MAX_VERTEX_VARYING_COMPONENTS_ARB = 0x8DDE
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_ARB = 0x8DDF
GL_MAX_GEOMETRY_OUTPUT_VERTICES_ARB = 0x8DE0
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_ARB = 0x8DE1
# ARB_get_program_binary
GL_PROGRAM_BINARY_RETRIEVABLE_HINT = 0x8257
GL_PROGRAM_BINARY_LENGTH = 0x8741
GL_NUM_PROGRAM_BINARY_FORMATS = 0x87FE
GL_PROGRAM_BINARY_FORMATS = 0x87FF
# ARB_gpu_shader5
GL_GEOMETRY_SHADER_INVOCATIONS = 0x887F
GL_MAX_GEOMETRY_SHADER_INVOCATIONS = 0x8E5A
GL_MIN_FRAGMENT_INTERPOLATION_OFFSET = 0x8E5B
GL_MAX_FRAGMENT_INTERPOLATION_OFFSET = 0x8E5C
GL_FRAGMENT_INTERPOLATION_OFFSET_BITS = 0x8E5D
# ARB_gpu_shader_fp64
GL_DOUBLE_VEC2 = 0x8FFC
GL_DOUBLE_VEC3 = 0x8FFD
GL_DOUBLE_VEC4 = 0x8FFE
GL_DOUBLE_MAT2 = 0x8F46
GL_DOUBLE_MAT3 = 0x8F47
GL_DOUBLE_MAT4 = 0x8F48
GL_DOUBLE_MAT2x3 = 0x8F49
GL_DOUBLE_MAT2x4 = 0x8F4A
GL_DOUBLE_MAT3x2 = 0x8F4B
GL_DOUBLE_MAT3x4 = 0x8F4C
GL_DOUBLE_MAT4x2 = 0x8F4D
GL_DOUBLE_MAT4x3 = 0x8F4E
# ARB_half_float_pixel
GL_HALF_FLOAT_ARB = 0x140B
# ARB_half_float_vertex
GL_HALF_FLOAT = 0x140B
# ARB_imaging
GL_CONSTANT_COLOR = 0x8001
GL_ONE_MINUS_CONSTANT_COLOR = 0x8002
GL_CONSTANT_ALPHA = 0x8003
GL_ONE_MINUS_CONSTANT_ALPHA = 0x8004
GL_BLEND_COLOR = 0x8005
GL_FUNC_ADD = 0x8006
GL_MIN = 0x8007
GL_MAX = 0x8008
GL_BLEND_EQUATION = 0x8009
GL_FUNC_SUBTRACT = 0x800A
GL_FUNC_REVERSE_SUBTRACT = 0x800B
# ARB_imaging_DEPRECATED
GL_CONVOLUTION_1D = 0x8010
GL_CONVOLUTION_2D = 0x8011
GL_SEPARABLE_2D = 0x8012
GL_CONVOLUTION_BORDER_MODE = 0x8013
GL_CONVOLUTION_FILTER_SCALE = 0x8014
GL_CONVOLUTION_FILTER_BIAS = 0x8015
GL_REDUCE = 0x8016
GL_CONVOLUTION_FORMAT = 0x8017
GL_CONVOLUTION_WIDTH = 0x8018
GL_CONVOLUTION_HEIGHT = 0x8019
GL_MAX_CONVOLUTION_WIDTH = 0x801A
GL_MAX_CONVOLUTION_HEIGHT = 0x801B
GL_POST_CONVOLUTION_RED_SCALE = 0x801C
GL_POST_CONVOLUTION_GREEN_SCALE = 0x801D
GL_POST_CONVOLUTION_BLUE_SCALE = 0x801E
GL_POST_CONVOLUTION_ALPHA_SCALE = 0x801F
GL_POST_CONVOLUTION_RED_BIAS = 0x8020
GL_POST_CONVOLUTION_GREEN_BIAS = 0x8021
GL_POST_CONVOLUTION_BLUE_BIAS = 0x8022
GL_POST_CONVOLUTION_ALPHA_BIAS = 0x8023
GL_HISTOGRAM = 0x8024
GL_PROXY_HISTOGRAM = 0x8025
GL_HISTOGRAM_WIDTH = 0x8026
GL_HISTOGRAM_FORMAT = 0x8027
GL_HISTOGRAM_RED_SIZE = 0x8028
GL_HISTOGRAM_GREEN_SIZE = 0x8029
GL_HISTOGRAM_BLUE_SIZE = 0x802A
GL_HISTOGRAM_ALPHA_SIZE = 0x802B
GL_HISTOGRAM_LUMINANCE_SIZE = 0x802C
GL_HISTOGRAM_SINK = 0x802D
GL_MINMAX = 0x802E
GL_MINMAX_FORMAT = 0x802F
GL_MINMAX_SINK = 0x8030
GL_TABLE_TOO_LARGE = 0x8031
GL_COLOR_MATRIX = 0x80B1
GL_COLOR_MATRIX_STACK_DEPTH = 0x80B2
GL_MAX_COLOR_MATRIX_STACK_DEPTH = 0x80B3
GL_POST_COLOR_MATRIX_RED_SCALE = 0x80B4
GL_POST_COLOR_MATRIX_GREEN_SCALE = 0x80B5
GL_POST_COLOR_MATRIX_BLUE_SCALE = 0x80B6
GL_POST_COLOR_MATRIX_ALPHA_SCALE = 0x80B7
GL_POST_COLOR_MATRIX_RED_BIAS = 0x80B8
GL_POST_COLOR_MATRIX_GREEN_BIAS = 0x80B9
GL_POST_COLOR_MATRIX_BLUE_BIAS = 0x80BA
GL_POST_COLOR_MATRIX_ALPHA_BIAS = 0x80BB
GL_COLOR_TABLE = 0x80D0
GL_POST_CONVOLUTION_COLOR_TABLE = 0x80D1
GL_POST_COLOR_MATRIX_COLOR_TABLE = 0x80D2
GL_PROXY_COLOR_TABLE = 0x80D3
GL_PROXY_POST_CONVOLUTION_COLOR_TABLE = 0x80D4
GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE = 0x80D5
GL_COLOR_TABLE_SCALE = 0x80D6
GL_COLOR_TABLE_BIAS = 0x80D7
GL_COLOR_TABLE_FORMAT = 0x80D8
GL_COLOR_TABLE_WIDTH = 0x80D9
GL_COLOR_TABLE_RED_SIZE = 0x80DA
GL_COLOR_TABLE_GREEN_SIZE = 0x80DB
GL_COLOR_TABLE_BLUE_SIZE = 0x80DC
GL_COLOR_TABLE_ALPHA_SIZE = 0x80DD
GL_COLOR_TABLE_LUMINANCE_SIZE = 0x80DE
GL_COLOR_TABLE_INTENSITY_SIZE = 0x80DF
GL_CONSTANT_BORDER = 0x8151
GL_REPLICATE_BORDER = 0x8153
GL_CONVOLUTION_BORDER_COLOR = 0x8154
# ARB_instanced_arrays
GL_VERTEX_ATTRIB_ARRAY_DIVISOR_ARB = 0x88FE
# ARB_internalformat_query
GL_NUM_SAMPLE_COUNTS = 0x9380
# ARB_internalformat_query2
GL_INTERNALFORMAT_SUPPORTED = 0x826F
GL_INTERNALFORMAT_PREFERRED = 0x8270
GL_INTERNALFORMAT_RED_SIZE = 0x8271
GL_INTERNALFORMAT_GREEN_SIZE = 0x8272
GL_INTERNALFORMAT_BLUE_SIZE = 0x8273
GL_INTERNALFORMAT_ALPHA_SIZE = 0x8274
GL_INTERNALFORMAT_DEPTH_SIZE = 0x8275
GL_INTERNALFORMAT_STENCIL_SIZE = 0x8276
GL_INTERNALFORMAT_SHARED_SIZE = 0x8277
GL_INTERNALFORMAT_RED_TYPE = 0x8278
GL_INTERNALFORMAT_GREEN_TYPE = 0x8279
GL_INTERNALFORMAT_BLUE_TYPE = 0x827A
GL_INTERNALFORMAT_ALPHA_TYPE = 0x827B
GL_INTERNALFORMAT_DEPTH_TYPE = 0x827C
GL_INTERNALFORMAT_STENCIL_TYPE = 0x827D
GL_MAX_WIDTH = 0x827E
GL_MAX_HEIGHT = 0x827F
GL_MAX_DEPTH = 0x8280
GL_MAX_LAYERS = 0x8281
GL_MAX_COMBINED_DIMENSIONS = 0x8282
GL_COLOR_COMPONENTS = 0x8283
GL_DEPTH_COMPONENTS = 0x8284
GL_STENCIL_COMPONENTS = 0x8285
GL_COLOR_RENDERABLE = 0x8286
GL_DEPTH_RENDERABLE = 0x8287
GL_STENCIL_RENDERABLE = 0x8288
GL_FRAMEBUFFER_RENDERABLE = 0x8289
GL_FRAMEBUFFER_RENDERABLE_LAYERED = 0x828A
GL_FRAMEBUFFER_BLEND = 0x828B
GL_READ_PIXELS = 0x828C
GL_READ_PIXELS_FORMAT = 0x828D
GL_READ_PIXELS_TYPE = 0x828E
GL_TEXTURE_IMAGE_FORMAT = 0x828F
GL_TEXTURE_IMAGE_TYPE = 0x8290
GL_GET_TEXTURE_IMAGE_FORMAT = 0x8291
GL_GET_TEXTURE_IMAGE_TYPE = 0x8292
GL_MIPMAP = 0x8293
GL_MANUAL_GENERATE_MIPMAP = 0x8294
GL_AUTO_GENERATE_MIPMAP = 0x8295
GL_COLOR_ENCODING = 0x8296
GL_SRGB_READ = 0x8297
GL_SRGB_WRITE = 0x8298
GL_SRGB_DECODE_ARB = 0x8299
GL_FILTER = 0x829A
GL_VERTEX_TEXTURE = 0x829B
GL_TESS_CONTROL_TEXTURE = 0x829C
GL_TESS_EVALUATION_TEXTURE = 0x829D
GL_GEOMETRY_TEXTURE = 0x829E
GL_FRAGMENT_TEXTURE = 0x829F
GL_COMPUTE_TEXTURE = 0x82A0
GL_TEXTURE_SHADOW = 0x82A1
GL_TEXTURE_GATHER = 0x82A2
GL_TEXTURE_GATHER_SHADOW = 0x82A3
GL_SHADER_IMAGE_LOAD = 0x82A4
GL_SHADER_IMAGE_STORE = 0x82A5
GL_SHADER_IMAGE_ATOMIC = 0x82A6
GL_IMAGE_TEXEL_SIZE = 0x82A7
GL_IMAGE_COMPATIBILITY_CLASS = 0x82A8
GL_IMAGE_PIXEL_FORMAT = 0x82A9
GL_IMAGE_PIXEL_TYPE = 0x82AA
GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_TEST = 0x82AC
GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_TEST = 0x82AD
GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_WRITE = 0x82AE
GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_WRITE = 0x82AF
GL_TEXTURE_COMPRESSED_BLOCK_WIDTH = 0x82B1
GL_TEXTURE_COMPRESSED_BLOCK_HEIGHT = 0x82B2
GL_TEXTURE_COMPRESSED_BLOCK_SIZE = 0x82B3
GL_CLEAR_BUFFER = 0x82B4
GL_TEXTURE_VIEW = 0x82B5
GL_VIEW_COMPATIBILITY_CLASS = 0x82B6
GL_FULL_SUPPORT = 0x82B7
GL_CAVEAT_SUPPORT = 0x82B8
GL_IMAGE_CLASS_4_X_32 = 0x82B9
GL_IMAGE_CLASS_2_X_32 = 0x82BA
GL_IMAGE_CLASS_1_X_32 = 0x82BB
GL_IMAGE_CLASS_4_X_16 = 0x82BC
GL_IMAGE_CLASS_2_X_16 = 0x82BD
GL_IMAGE_CLASS_1_X_16 = 0x82BE
GL_IMAGE_CLASS_4_X_8 = 0x82BF
GL_IMAGE_CLASS_2_X_8 = 0x82C0
GL_IMAGE_CLASS_1_X_8 = 0x82C1
GL_IMAGE_CLASS_11_11_10 = 0x82C2
GL_IMAGE_CLASS_10_10_10_2 = 0x82C3
GL_VIEW_CLASS_128_BITS = 0x82C4
GL_VIEW_CLASS_96_BITS = 0x82C5
GL_VIEW_CLASS_64_BITS = 0x82C6
GL_VIEW_CLASS_48_BITS = 0x82C7
GL_VIEW_CLASS_32_BITS = 0x82C8
GL_VIEW_CLASS_24_BITS = 0x82C9
GL_VIEW_CLASS_16_BITS = 0x82CA
GL_VIEW_CLASS_8_BITS = 0x82CB
GL_VIEW_CLASS_S3TC_DXT1_RGB = 0x82CC
GL_VIEW_CLASS_S3TC_DXT1_RGBA = 0x82CD
GL_VIEW_CLASS_S3TC_DXT3_RGBA = 0x82CE
GL_VIEW_CLASS_S3TC_DXT5_RGBA = 0x82CF
GL_VIEW_CLASS_RGTC1_RED = 0x82D0
GL_VIEW_CLASS_RGTC2_RG = 0x82D1
GL_VIEW_CLASS_BPTC_UNORM = 0x82D2
GL_VIEW_CLASS_BPTC_FLOAT = 0x82D3
# ARB_invalidate_subdata
# ARB_map_buffer_alignment
GL_MIN_MAP_BUFFER_ALIGNMENT = 0x90BC
# ARB_map_buffer_range
GL_MAP_READ_BIT = 0x0001
GL_MAP_WRITE_BIT = 0x0002
GL_MAP_INVALIDATE_RANGE_BIT = 0x0004
GL_MAP_INVALIDATE_BUFFER_BIT = 0x0008
GL_MAP_FLUSH_EXPLICIT_BIT = 0x0010
GL_MAP_UNSYNCHRONIZED_BIT = 0x0020
# ARB_matrix_palette
GL_MATRIX_PALETTE_ARB = 0x8840
GL_MAX_MATRIX_PALETTE_STACK_DEPTH_ARB = 0x8841
GL_MAX_PALETTE_MATRICES_ARB = 0x8842
GL_CURRENT_PALETTE_MATRIX_ARB = 0x8843
GL_MATRIX_INDEX_ARRAY_ARB = 0x8844
GL_CURRENT_MATRIX_INDEX_ARB = 0x8845
GL_MATRIX_INDEX_ARRAY_SIZE_ARB = 0x8846
GL_MATRIX_INDEX_ARRAY_TYPE_ARB = 0x8847
GL_MATRIX_INDEX_ARRAY_STRIDE_ARB = 0x8848
GL_MATRIX_INDEX_ARRAY_POINTER_ARB = 0x8849
# ARB_multi_draw_indirect
# ARB_multisample
GL_MULTISAMPLE_ARB = 0x809D
GL_SAMPLE_ALPHA_TO_COVERAGE_ARB = 0x809E
GL_SAMPLE_ALPHA_TO_ONE_ARB = 0x809F
GL_SAMPLE_COVERAGE_ARB = 0x80A0
GL_SAMPLE_BUFFERS_ARB = 0x80A8
GL_SAMPLES_ARB = 0x80A9
GL_SAMPLE_COVERAGE_VALUE_ARB = 0x80AA
GL_SAMPLE_COVERAGE_INVERT_ARB = 0x80AB
GL_MULTISAMPLE_BIT_ARB = 0x20000000
WGL_SAMPLE_BUFFERS_ARB = 0x2041
WGL_SAMPLES_ARB = 0x2042
# ARB_multitexture
GL_TEXTURE0_ARB = 0x84C0
GL_TEXTURE1_ARB = 0x84C1
GL_TEXTURE2_ARB = 0x84C2
GL_TEXTURE3_ARB = 0x84C3
GL_TEXTURE4_ARB = 0x84C4
GL_TEXTURE5_ARB = 0x84C5
GL_TEXTURE6_ARB = 0x84C6
GL_TEXTURE7_ARB = 0x84C7
GL_TEXTURE8_ARB = 0x84C8
GL_TEXTURE9_ARB = 0x84C9
GL_TEXTURE10_ARB = 0x84CA
GL_TEXTURE11_ARB = 0x84CB
GL_TEXTURE12_ARB = 0x84CC
GL_TEXTURE13_ARB = 0x84CD
GL_TEXTURE14_ARB = 0x84CE
GL_TEXTURE15_ARB = 0x84CF
GL_TEXTURE16_ARB = 0x84D0
GL_TEXTURE17_ARB = 0x84D1
GL_TEXTURE18_ARB = 0x84D2
GL_TEXTURE19_ARB = 0x84D3
GL_TEXTURE20_ARB = 0x84D4
GL_TEXTURE21_ARB = 0x84D5
GL_TEXTURE22_ARB = 0x84D6
GL_TEXTURE23_ARB = 0x84D7
GL_TEXTURE24_ARB = 0x84D8
GL_TEXTURE25_ARB = 0x84D9
GL_TEXTURE26_ARB = 0x84DA
GL_TEXTURE27_ARB = 0x84DB
GL_TEXTURE28_ARB = 0x84DC
GL_TEXTURE29_ARB = 0x84DD
GL_TEXTURE30_ARB = 0x84DE
GL_TEXTURE31_ARB = 0x84DF
GL_ACTIVE_TEXTURE_ARB = 0x84E0
GL_CLIENT_ACTIVE_TEXTURE_ARB = 0x84E1
GL_MAX_TEXTURE_UNITS_ARB = 0x84E2
# ARB_occlusion_query
GL_QUERY_COUNTER_BITS_ARB = 0x8864
GL_CURRENT_QUERY_ARB = 0x8865
GL_QUERY_RESULT_ARB = 0x8866
GL_QUERY_RESULT_AVAILABLE_ARB = 0x8867
GL_SAMPLES_PASSED_ARB = 0x8914
# ARB_occlusion_query2
GL_ANY_SAMPLES_PASSED = 0x8C2F
# ARB_pixel_buffer_object
GL_PIXEL_PACK_BUFFER_ARB = 0x88EB
GL_PIXEL_UNPACK_BUFFER_ARB = 0x88EC
GL_PIXEL_PACK_BUFFER_BINDING_ARB = 0x88ED
GL_PIXEL_UNPACK_BUFFER_BINDING_ARB = 0x88EF
# ARB_point_parameters
GL_POINT_SIZE_MIN_ARB = 0x8126
GL_POINT_SIZE_MAX_ARB = 0x8127
GL_POINT_FADE_THRESHOLD_SIZE_ARB = 0x8128
GL_POINT_DISTANCE_ATTENUATION_ARB = 0x8129
# ARB_point_sprite
GL_POINT_SPRITE_ARB = 0x8861
GL_COORD_REPLACE_ARB = 0x8862
# ARB_program_interface_query
GL_UNIFORM = 0x92E1
GL_UNIFORM_BLOCK = 0x92E2
GL_PROGRAM_INPUT = 0x92E3
GL_PROGRAM_OUTPUT = 0x92E4
GL_BUFFER_VARIABLE = 0x92E5
GL_SHADER_STORAGE_BLOCK = 0x92E6
GL_VERTEX_SUBROUTINE = 0x92E8
GL_TESS_CONTROL_SUBROUTINE = 0x92E9
GL_TESS_EVALUATION_SUBROUTINE = 0x92EA
GL_GEOMETRY_SUBROUTINE = 0x92EB
GL_FRAGMENT_SUBROUTINE = 0x92EC
GL_COMPUTE_SUBROUTINE = 0x92ED
GL_VERTEX_SUBROUTINE_UNIFORM = 0x92EE
GL_TESS_CONTROL_SUBROUTINE_UNIFORM = 0x92EF
GL_TESS_EVALUATION_SUBROUTINE_UNIFORM = 0x92F0
GL_GEOMETRY_SUBROUTINE_UNIFORM = 0x92F1
GL_FRAGMENT_SUBROUTINE_UNIFORM = 0x92F2
GL_COMPUTE_SUBROUTINE_UNIFORM = 0x92F3
GL_TRANSFORM_FEEDBACK_VARYING = 0x92F4
GL_ACTIVE_RESOURCES = 0x92F5
GL_MAX_NAME_LENGTH = 0x92F6
GL_MAX_NUM_ACTIVE_VARIABLES = 0x92F7
GL_MAX_NUM_COMPATIBLE_SUBROUTINES = 0x92F8
GL_NAME_LENGTH = 0x92F9
GL_TYPE = 0x92FA
GL_ARRAY_SIZE = 0x92FB
GL_OFFSET = 0x92FC
GL_BLOCK_INDEX = 0x92FD
GL_ARRAY_STRIDE = 0x92FE
GL_MATRIX_STRIDE = 0x92FF
GL_IS_ROW_MAJOR = 0x9300
GL_ATOMIC_COUNTER_BUFFER_INDEX = 0x9301
GL_BUFFER_BINDING = 0x9302
GL_BUFFER_DATA_SIZE = 0x9303
GL_NUM_ACTIVE_VARIABLES = 0x9304
GL_ACTIVE_VARIABLES = 0x9305
GL_REFERENCED_BY_VERTEX_SHADER = 0x9306
GL_REFERENCED_BY_TESS_CONTROL_SHADER = 0x9307
GL_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x9308
GL_REFERENCED_BY_GEOMETRY_SHADER = 0x9309
GL_REFERENCED_BY_FRAGMENT_SHADER = 0x930A
GL_REFERENCED_BY_COMPUTE_SHADER = 0x930B
GL_TOP_LEVEL_ARRAY_SIZE = 0x930C
GL_TOP_LEVEL_ARRAY_STRIDE = 0x930D
GL_LOCATION = 0x930E
GL_LOCATION_INDEX = 0x930F
GL_IS_PER_PATCH = 0x92E7
# ARB_provoking_vertex
GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION = 0x8E4C
GL_FIRST_VERTEX_CONVENTION = 0x8E4D
GL_LAST_VERTEX_CONVENTION = 0x8E4E
GL_PROVOKING_VERTEX = 0x8E4F
# ARB_robust_buffer_access_behavior
# ARB_robustness
GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT_ARB = 0x00000004
GL_LOSE_CONTEXT_ON_RESET_ARB = 0x8252
GL_GUILTY_CONTEXT_RESET_ARB = 0x8253
GL_INNOCENT_CONTEXT_RESET_ARB = 0x8254
GL_UNKNOWN_CONTEXT_RESET_ARB = 0x8255
GL_RESET_NOTIFICATION_STRATEGY_ARB = 0x8256
GL_NO_RESET_NOTIFICATION_ARB = 0x8261
# ARB_robustness_isolation
# ARB_sample_shading
GL_SAMPLE_SHADING_ARB = 0x8C36
GL_MIN_SAMPLE_SHADING_VALUE_ARB = 0x8C37
# ARB_sampler_objects
GL_SAMPLER_BINDING = 0x8919
# ARB_seamless_cube_map
GL_TEXTURE_CUBE_MAP_SEAMLESS = 0x884F
# ARB_separate_shader_objects
GL_VERTEX_SHADER_BIT = 0x00000001
GL_FRAGMENT_SHADER_BIT = 0x00000002
GL_GEOMETRY_SHADER_BIT = 0x00000004
GL_TESS_CONTROL_SHADER_BIT = 0x00000008
GL_TESS_EVALUATION_SHADER_BIT = 0x00000010
GL_ALL_SHADER_BITS = 0xFFFFFFFF
GL_PROGRAM_SEPARABLE = 0x8258
GL_ACTIVE_PROGRAM = 0x8259
GL_PROGRAM_PIPELINE_BINDING = 0x825A
# ARB_shader_atomic_counters
GL_ATOMIC_COUNTER_BUFFER = 0x92C0
GL_ATOMIC_COUNTER_BUFFER_BINDING = 0x92C1
GL_ATOMIC_COUNTER_BUFFER_START = 0x92C2
GL_ATOMIC_COUNTER_BUFFER_SIZE = 0x92C3
GL_ATOMIC_COUNTER_BUFFER_DATA_SIZE = 0x92C4
GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTERS = 0x92C5
GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTER_INDICES = 0x92C6
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_VERTEX_SHADER = 0x92C7
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_CONTROL_SHADER = 0x92C8
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x92C9
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_GEOMETRY_SHADER = 0x92CA
GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_FRAGMENT_SHADER = 0x92CB
GL_MAX_VERTEX_ATOMIC_COUNTER_BUFFERS = 0x92CC
GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS = 0x92CD
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS = 0x92CE
GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS = 0x92CF
GL_MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS = 0x92D0
GL_MAX_COMBINED_ATOMIC_COUNTER_BUFFERS = 0x92D1
GL_MAX_VERTEX_ATOMIC_COUNTERS = 0x92D2
GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS = 0x92D3
GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS = 0x92D4
GL_MAX_GEOMETRY_ATOMIC_COUNTERS = 0x92D5
GL_MAX_FRAGMENT_ATOMIC_COUNTERS = 0x92D6
GL_MAX_COMBINED_ATOMIC_COUNTERS = 0x92D7
GL_MAX_ATOMIC_COUNTER_BUFFER_SIZE = 0x92D8
GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS = 0x92DC
GL_ACTIVE_ATOMIC_COUNTER_BUFFERS = 0x92D9
GL_UNIFORM_ATOMIC_COUNTER_BUFFER_INDEX = 0x92DA
GL_UNSIGNED_INT_ATOMIC_COUNTER = 0x92DB
# ARB_shader_bit_encoding
# ARB_shader_image_load_store
GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT = 0x00000001
GL_ELEMENT_ARRAY_BARRIER_BIT = 0x00000002
GL_UNIFORM_BARRIER_BIT = 0x00000004
GL_TEXTURE_FETCH_BARRIER_BIT = 0x00000008
GL_SHADER_IMAGE_ACCESS_BARRIER_BIT = 0x00000020
GL_COMMAND_BARRIER_BIT = 0x00000040
GL_PIXEL_BUFFER_BARRIER_BIT = 0x00000080
GL_TEXTURE_UPDATE_BARRIER_BIT = 0x00000100
GL_BUFFER_UPDATE_BARRIER_BIT = 0x00000200
GL_FRAMEBUFFER_BARRIER_BIT = 0x00000400
GL_TRANSFORM_FEEDBACK_BARRIER_BIT = 0x00000800
GL_ATOMIC_COUNTER_BARRIER_BIT = 0x00001000
GL_ALL_BARRIER_BITS = 0xFFFFFFFF
GL_MAX_IMAGE_UNITS = 0x8F38
GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS = 0x8F39
GL_IMAGE_BINDING_NAME = 0x8F3A
GL_IMAGE_BINDING_LEVEL = 0x8F3B
GL_IMAGE_BINDING_LAYERED = 0x8F3C
GL_IMAGE_BINDING_LAYER = 0x8F3D
GL_IMAGE_BINDING_ACCESS = 0x8F3E
GL_IMAGE_1D = 0x904C
GL_IMAGE_2D = 0x904D
GL_IMAGE_3D = 0x904E
GL_IMAGE_2D_RECT = 0x904F
GL_IMAGE_CUBE = 0x9050
GL_IMAGE_BUFFER = 0x9051
GL_IMAGE_1D_ARRAY = 0x9052
GL_IMAGE_2D_ARRAY = 0x9053
GL_IMAGE_CUBE_MAP_ARRAY = 0x9054
GL_IMAGE_2D_MULTISAMPLE = 0x9055
GL_IMAGE_2D_MULTISAMPLE_ARRAY = 0x9056
GL_INT_IMAGE_1D = 0x9057
GL_INT_IMAGE_2D = 0x9058
GL_INT_IMAGE_3D = 0x9059
GL_INT_IMAGE_2D_RECT = 0x905A
GL_INT_IMAGE_CUBE = 0x905B
GL_INT_IMAGE_BUFFER = 0x905C
GL_INT_IMAGE_1D_ARRAY = 0x905D
GL_INT_IMAGE_2D_ARRAY = 0x905E
GL_INT_IMAGE_CUBE_MAP_ARRAY = 0x905F
GL_INT_IMAGE_2D_MULTISAMPLE = 0x9060
GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY = 0x9061
GL_UNSIGNED_INT_IMAGE_1D = 0x9062
GL_UNSIGNED_INT_IMAGE_2D = 0x9063
GL_UNSIGNED_INT_IMAGE_3D = 0x9064
GL_UNSIGNED_INT_IMAGE_2D_RECT = 0x9065
GL_UNSIGNED_INT_IMAGE_CUBE = 0x9066
GL_UNSIGNED_INT_IMAGE_BUFFER = 0x9067
GL_UNSIGNED_INT_IMAGE_1D_ARRAY = 0x9068
GL_UNSIGNED_INT_IMAGE_2D_ARRAY = 0x9069
GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY = 0x906A
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE = 0x906B
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY = 0x906C
GL_MAX_IMAGE_SAMPLES = 0x906D
GL_IMAGE_BINDING_FORMAT = 0x906E
GL_IMAGE_FORMAT_COMPATIBILITY_TYPE = 0x90C7
GL_IMAGE_FORMAT_COMPATIBILITY_BY_SIZE = 0x90C8
GL_IMAGE_FORMAT_COMPATIBILITY_BY_CLASS = 0x90C9
GL_MAX_VERTEX_IMAGE_UNIFORMS = 0x90CA
GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS = 0x90CB
GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS = 0x90CC
GL_MAX_GEOMETRY_IMAGE_UNIFORMS = 0x90CD
GL_MAX_FRAGMENT_IMAGE_UNIFORMS = 0x90CE
GL_MAX_COMBINED_IMAGE_UNIFORMS = 0x90CF
# ARB_shader_image_size
# ARB_shader_objects
GL_PROGRAM_OBJECT_ARB = 0x8B40
GL_SHADER_OBJECT_ARB = 0x8B48
GL_OBJECT_TYPE_ARB = 0x8B4E
GL_OBJECT_SUBTYPE_ARB = 0x8B4F
GL_FLOAT_VEC2_ARB = 0x8B50
GL_FLOAT_VEC3_ARB = 0x8B51
GL_FLOAT_VEC4_ARB = 0x8B52
GL_INT_VEC2_ARB = 0x8B53
GL_INT_VEC3_ARB = 0x8B54
GL_INT_VEC4_ARB = 0x8B55
GL_BOOL_ARB = 0x8B56
GL_BOOL_VEC2_ARB = 0x8B57
GL_BOOL_VEC3_ARB = 0x8B58
GL_BOOL_VEC4_ARB = 0x8B59
GL_FLOAT_MAT2_ARB = 0x8B5A
GL_FLOAT_MAT3_ARB = 0x8B5B
GL_FLOAT_MAT4_ARB = 0x8B5C
GL_SAMPLER_1D_ARB = 0x8B5D
GL_SAMPLER_2D_ARB = 0x8B5E
GL_SAMPLER_3D_ARB = 0x8B5F
GL_SAMPLER_CUBE_ARB = 0x8B60
GL_SAMPLER_1D_SHADOW_ARB = 0x8B61
GL_SAMPLER_2D_SHADOW_ARB = 0x8B62
GL_SAMPLER_2D_RECT_ARB = 0x8B63
GL_SAMPLER_2D_RECT_SHADOW_ARB = 0x8B64
GL_OBJECT_DELETE_STATUS_ARB = 0x8B80
GL_OBJECT_COMPILE_STATUS_ARB = 0x8B81
GL_OBJECT_LINK_STATUS_ARB = 0x8B82
GL_OBJECT_VALIDATE_STATUS_ARB = 0x8B83
GL_OBJECT_INFO_LOG_LENGTH_ARB = 0x8B84
GL_OBJECT_ATTACHED_OBJECTS_ARB = 0x8B85
GL_OBJECT_ACTIVE_UNIFORMS_ARB = 0x8B86
GL_OBJECT_ACTIVE_UNIFORM_MAX_LENGTH_ARB = 0x8B87
GL_OBJECT_SHADER_SOURCE_LENGTH_ARB = 0x8B88
# ARB_shader_precision
# ARB_shader_stencil_export
# ARB_shader_storage_buffer_object
GL_SHADER_STORAGE_BUFFER = 0x90D2
GL_SHADER_STORAGE_BUFFER_BINDING = 0x90D3
GL_SHADER_STORAGE_BUFFER_START = 0x90D4
GL_SHADER_STORAGE_BUFFER_SIZE = 0x90D5
GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS = 0x90D6
GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS = 0x90D7
GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS = 0x90D8
GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS = 0x90D9
GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS = 0x90DA
GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS = 0x90DB
GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS = 0x90DC
GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS = 0x90DD
GL_MAX_SHADER_STORAGE_BLOCK_SIZE = 0x90DE
GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT = 0x90DF
GL_SHADER_STORAGE_BARRIER_BIT = 0x2000
GL_MAX_COMBINED_SHADER_OUTPUT_RESOURCES = 0x8F39 # GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS
# ARB_shader_subroutine
GL_ACTIVE_SUBROUTINES = 0x8DE5
GL_ACTIVE_SUBROUTINE_UNIFORMS = 0x8DE6
GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS = 0x8E47
GL_ACTIVE_SUBROUTINE_MAX_LENGTH = 0x8E48
GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH = 0x8E49
GL_MAX_SUBROUTINES = 0x8DE7
GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS = 0x8DE8
GL_NUM_COMPATIBLE_SUBROUTINES = 0x8E4A
GL_COMPATIBLE_SUBROUTINES = 0x8E4B
# ARB_shader_texture_lod
# ARB_shading_language_100
GL_SHADING_LANGUAGE_VERSION_ARB = 0x8B8C
# ARB_shading_language_420pack
# ARB_shading_language_include
GL_SHADER_INCLUDE_ARB = 0x8DAE
GL_NAMED_STRING_LENGTH_ARB = 0x8DE9
GL_NAMED_STRING_TYPE_ARB = 0x8DEA
# ARB_shading_language_packing
# ARB_shadow
GL_TEXTURE_COMPARE_MODE_ARB = 0x884C
GL_TEXTURE_COMPARE_FUNC_ARB = 0x884D
GL_COMPARE_R_TO_TEXTURE_ARB = 0x884E
# ARB_shadow_ambient
GL_TEXTURE_COMPARE_FAIL_VALUE_ARB = 0x80BF
# ARB_stencil_texturing
GL_DEPTH_STENCIL_TEXTURE_MODE = 0x90EA
# ARB_sync
GL_MAX_SERVER_WAIT_TIMEOUT = 0x9111
GL_OBJECT_TYPE = 0x9112
GL_SYNC_CONDITION = 0x9113
GL_SYNC_STATUS = 0x9114
GL_SYNC_FLAGS = 0x9115
GL_SYNC_FENCE = 0x9116
GL_SYNC_GPU_COMMANDS_COMPLETE = 0x9117
GL_UNSIGNALED = 0x9118
GL_SIGNALED = 0x9119
GL_ALREADY_SIGNALED = 0x911A
GL_TIMEOUT_EXPIRED = 0x911B
GL_CONDITION_SATISFIED = 0x911C
GL_WAIT_FAILED = 0x911D
GL_SYNC_FLUSH_COMMANDS_BIT = 0x00000001
GL_TIMEOUT_IGNORED = 0xFFFFFFFFFFFFFFFF
# ARB_tessellation_shader
GL_PATCHES = 0x000E
GL_PATCH_VERTICES = 0x8E72
GL_PATCH_DEFAULT_INNER_LEVEL = 0x8E73
GL_PATCH_DEFAULT_OUTER_LEVEL = 0x8E74
GL_TESS_CONTROL_OUTPUT_VERTICES = 0x8E75
GL_TESS_GEN_MODE = 0x8E76
GL_TESS_GEN_SPACING = 0x8E77
GL_TESS_GEN_VERTEX_ORDER = 0x8E78
GL_TESS_GEN_POINT_MODE = 0x8E79
GL_ISOLINES = 0x8E7A
GL_FRACTIONAL_ODD = 0x8E7B
GL_FRACTIONAL_EVEN = 0x8E7C
GL_MAX_PATCH_VERTICES = 0x8E7D
GL_MAX_TESS_GEN_LEVEL = 0x8E7E
GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS = 0x8E7F
GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS = 0x8E80
GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS = 0x8E81
GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS = 0x8E82
GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS = 0x8E83
GL_MAX_TESS_PATCH_COMPONENTS = 0x8E84
GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS = 0x8E85
GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS = 0x8E86
GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS = 0x8E89
GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS = 0x8E8A
GL_MAX_TESS_CONTROL_INPUT_COMPONENTS = 0x886C
GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS = 0x886D
GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS = 0x8E1E
GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS = 0x8E1F
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER = 0x84F0
GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x84F1
GL_TESS_EVALUATION_SHADER = 0x8E87
GL_TESS_CONTROL_SHADER = 0x8E88
# ARB_texture_border_clamp
GL_CLAMP_TO_BORDER_ARB = 0x812D
# ARB_texture_buffer_object
GL_TEXTURE_BUFFER_ARB = 0x8C2A
GL_MAX_TEXTURE_BUFFER_SIZE_ARB = 0x8C2B
GL_TEXTURE_BINDING_BUFFER_ARB = 0x8C2C
GL_TEXTURE_BUFFER_DATA_STORE_BINDING_ARB = 0x8C2D
GL_TEXTURE_BUFFER_FORMAT_ARB = 0x8C2E
# ARB_texture_buffer_object_rgb32
# ARB_texture_buffer_range
GL_TEXTURE_BUFFER_OFFSET = 0x919D
GL_TEXTURE_BUFFER_SIZE = 0x919E
GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT = 0x919F
# ARB_texture_compression
GL_COMPRESSED_ALPHA_ARB = 0x84E9
GL_COMPRESSED_LUMINANCE_ARB = 0x84EA
GL_COMPRESSED_LUMINANCE_ALPHA_ARB = 0x84EB
GL_COMPRESSED_INTENSITY_ARB = 0x84EC
GL_COMPRESSED_RGB_ARB = 0x84ED
GL_COMPRESSED_RGBA_ARB = 0x84EE
GL_TEXTURE_COMPRESSION_HINT_ARB = 0x84EF
GL_TEXTURE_COMPRESSED_IMAGE_SIZE_ARB = 0x86A0
GL_TEXTURE_COMPRESSED_ARB = 0x86A1
GL_NUM_COMPRESSED_TEXTURE_FORMATS_ARB = 0x86A2
GL_COMPRESSED_TEXTURE_FORMATS_ARB = 0x86A3
# ARB_texture_compression_bptc
GL_COMPRESSED_RGBA_BPTC_UNORM_ARB = 0x8E8C
GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM_ARB = 0x8E8D
GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT_ARB = 0x8E8E
GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_ARB = 0x8E8F
# ARB_texture_compression_rgtc
GL_COMPRESSED_RED_RGTC1 = 0x8DBB
GL_COMPRESSED_SIGNED_RED_RGTC1 = 0x8DBC
GL_COMPRESSED_RG_RGTC2 = 0x8DBD
GL_COMPRESSED_SIGNED_RG_RGTC2 = 0x8DBE
# ARB_texture_cube_map
GL_NORMAL_MAP_ARB = 0x8511
GL_REFLECTION_MAP_ARB = 0x8512
GL_TEXTURE_CUBE_MAP_ARB = 0x8513
GL_TEXTURE_BINDING_CUBE_MAP_ARB = 0x8514
GL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB = 0x8515
GL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB = 0x8516
GL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB = 0x8517
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB = 0x8518
GL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB = 0x8519
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB = 0x851A
GL_PROXY_TEXTURE_CUBE_MAP_ARB = 0x851B
GL_MAX_CUBE_MAP_TEXTURE_SIZE_ARB = 0x851C
# ARB_texture_cube_map_array
GL_TEXTURE_CUBE_MAP_ARRAY_ARB = 0x9009
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY_ARB = 0x900A
GL_PROXY_TEXTURE_CUBE_MAP_ARRAY_ARB = 0x900B
GL_SAMPLER_CUBE_MAP_ARRAY_ARB = 0x900C
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW_ARB = 0x900D
GL_INT_SAMPLER_CUBE_MAP_ARRAY_ARB = 0x900E
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY_ARB = 0x900F
# ARB_texture_env_add
# ARB_texture_env_combine
GL_COMBINE_ARB = 0x8570
GL_COMBINE_RGB_ARB = 0x8571
GL_COMBINE_ALPHA_ARB = 0x8572
GL_SOURCE0_RGB_ARB = 0x8580
GL_SOURCE1_RGB_ARB = 0x8581
GL_SOURCE2_RGB_ARB = 0x8582
GL_SOURCE0_ALPHA_ARB = 0x8588
GL_SOURCE1_ALPHA_ARB = 0x8589
GL_SOURCE2_ALPHA_ARB = 0x858A
GL_OPERAND0_RGB_ARB = 0x8590
GL_OPERAND1_RGB_ARB = 0x8591
GL_OPERAND2_RGB_ARB = 0x8592
GL_OPERAND0_ALPHA_ARB = 0x8598
GL_OPERAND1_ALPHA_ARB = 0x8599
GL_OPERAND2_ALPHA_ARB = 0x859A
GL_RGB_SCALE_ARB = 0x8573
GL_ADD_SIGNED_ARB = 0x8574
GL_INTERPOLATE_ARB = 0x8575
GL_SUBTRACT_ARB = 0x84E7
GL_CONSTANT_ARB = 0x8576
GL_PRIMARY_COLOR_ARB = 0x8577
GL_PREVIOUS_ARB = 0x8578
# ARB_texture_env_crossbar
# ARB_texture_env_dot3
GL_DOT3_RGB_ARB = 0x86AE
GL_DOT3_RGBA_ARB = 0x86AF
# ARB_texture_float
GL_TEXTURE_RED_TYPE_ARB = 0x8C10
GL_TEXTURE_GREEN_TYPE_ARB = 0x8C11
GL_TEXTURE_BLUE_TYPE_ARB = 0x8C12
GL_TEXTURE_ALPHA_TYPE_ARB = 0x8C13
GL_TEXTURE_LUMINANCE_TYPE_ARB = 0x8C14
GL_TEXTURE_INTENSITY_TYPE_ARB = 0x8C15
GL_TEXTURE_DEPTH_TYPE_ARB = 0x8C16
GL_UNSIGNED_NORMALIZED_ARB = 0x8C17
GL_RGBA32F_ARB = 0x8814
GL_RGB32F_ARB = 0x8815
GL_ALPHA32F_ARB = 0x8816
GL_INTENSITY32F_ARB = 0x8817
GL_LUMINANCE32F_ARB = 0x8818
GL_LUMINANCE_ALPHA32F_ARB = 0x8819
GL_RGBA16F_ARB = 0x881A
GL_RGB16F_ARB = 0x881B
GL_ALPHA16F_ARB = 0x881C
GL_INTENSITY16F_ARB = 0x881D
GL_LUMINANCE16F_ARB = 0x881E
GL_LUMINANCE_ALPHA16F_ARB = 0x881F
# ARB_texture_gather
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_ARB = 0x8E5E
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_ARB = 0x8E5F
GL_MAX_PROGRAM_TEXTURE_GATHER_COMPONENTS_ARB = 0x8F9F
# ARB_texture_mirrored_repeat
GL_MIRRORED_REPEAT_ARB = 0x8370
# ARB_texture_multisample
GL_SAMPLE_POSITION = 0x8E50
GL_SAMPLE_MASK = 0x8E51
GL_SAMPLE_MASK_VALUE = 0x8E52
GL_MAX_SAMPLE_MASK_WORDS = 0x8E59
GL_TEXTURE_2D_MULTISAMPLE = 0x9100
GL_PROXY_TEXTURE_2D_MULTISAMPLE = 0x9101
GL_TEXTURE_2D_MULTISAMPLE_ARRAY = 0x9102
GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY = 0x9103
GL_TEXTURE_BINDING_2D_MULTISAMPLE = 0x9104
GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY = 0x9105
GL_TEXTURE_SAMPLES = 0x9106
GL_TEXTURE_FIXED_SAMPLE_LOCATIONS = 0x9107
GL_SAMPLER_2D_MULTISAMPLE = 0x9108
GL_INT_SAMPLER_2D_MULTISAMPLE = 0x9109
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE = 0x910A
GL_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910B
GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910C
GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910D
GL_MAX_COLOR_TEXTURE_SAMPLES = 0x910E
GL_MAX_DEPTH_TEXTURE_SAMPLES = 0x910F
GL_MAX_INTEGER_SAMPLES = 0x9110
# ARB_texture_non_power_of_two
# ARB_texture_query_levels
# ARB_texture_query_lod
# ARB_texture_rectangle
GL_TEXTURE_RECTANGLE_ARB = 0x84F5
GL_TEXTURE_BINDING_RECTANGLE_ARB = 0x84F6
GL_PROXY_TEXTURE_RECTANGLE_ARB = 0x84F7
GL_MAX_RECTANGLE_TEXTURE_SIZE_ARB = 0x84F8
# ARB_texture_rg
GL_RG = 0x8227
GL_RG_INTEGER = 0x8228
GL_R8 = 0x8229
GL_R16 = 0x822A
GL_RG8 = 0x822B
GL_RG16 = 0x822C
GL_R16F = 0x822D
GL_R32F = 0x822E
GL_RG16F = 0x822F
GL_RG32F = 0x8230
GL_R8I = 0x8231
GL_R8UI = 0x8232
GL_R16I = 0x8233
GL_R16UI = 0x8234
GL_R32I = 0x8235
GL_R32UI = 0x8236
GL_RG8I = 0x8237
GL_RG8UI = 0x8238
GL_RG16I = 0x8239
GL_RG16UI = 0x823A
GL_RG32I = 0x823B
GL_RG32UI = 0x823C
# ARB_texture_rgb10_a2ui
GL_RGB10_A2UI = 0x906F
# ARB_texture_storage
GL_TEXTURE_IMMUTABLE_FORMAT = 0x912F
# ARB_texture_storage_multisample
# ARB_texture_swizzle
GL_TEXTURE_SWIZZLE_R = 0x8E42
GL_TEXTURE_SWIZZLE_G = 0x8E43
GL_TEXTURE_SWIZZLE_B = 0x8E44
GL_TEXTURE_SWIZZLE_A = 0x8E45
GL_TEXTURE_SWIZZLE_RGBA = 0x8E46
# ARB_texture_view
GL_TEXTURE_VIEW_MIN_LEVEL = 0x82DB
GL_TEXTURE_VIEW_NUM_LEVELS = 0x82DC
GL_TEXTURE_VIEW_MIN_LAYER = 0x82DD
GL_TEXTURE_VIEW_NUM_LAYERS = 0x82DE
GL_TEXTURE_IMMUTABLE_LEVELS = 0x82DF
# ARB_timer_query
GL_TIME_ELAPSED = 0x88BF
GL_TIMESTAMP = 0x8E28
# ARB_transform_feedback2
GL_TRANSFORM_FEEDBACK = 0x8E22
GL_TRANSFORM_FEEDBACK_PAUSED = 0x8E23
GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED = 0x8E23 # GL_TRANSFORM_FEEDBACK_PAUSED
GL_TRANSFORM_FEEDBACK_ACTIVE = 0x8E24
GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE = 0x8E24 # GL_TRANSFORM_FEEDBACK_ACTIVE
GL_TRANSFORM_FEEDBACK_BINDING = 0x8E25
# ARB_transform_feedback3
GL_MAX_TRANSFORM_FEEDBACK_BUFFERS = 0x8E70
GL_MAX_VERTEX_STREAMS = 0x8E71
# ARB_transform_feedback_instanced
# ARB_transpose_matrix
GL_TRANSPOSE_MODELVIEW_MATRIX_ARB = 0x84E3
GL_TRANSPOSE_PROJECTION_MATRIX_ARB = 0x84E4
GL_TRANSPOSE_TEXTURE_MATRIX_ARB = 0x84E5
GL_TRANSPOSE_COLOR_MATRIX_ARB = 0x84E6
# ARB_uniform_buffer_object
GL_UNIFORM_BUFFER = 0x8A11
GL_UNIFORM_BUFFER_BINDING = 0x8A28
GL_UNIFORM_BUFFER_START = 0x8A29
GL_UNIFORM_BUFFER_SIZE = 0x8A2A
GL_MAX_VERTEX_UNIFORM_BLOCKS = 0x8A2B
GL_MAX_GEOMETRY_UNIFORM_BLOCKS = 0x8A2C
GL_MAX_FRAGMENT_UNIFORM_BLOCKS = 0x8A2D
GL_MAX_COMBINED_UNIFORM_BLOCKS = 0x8A2E
GL_MAX_UNIFORM_BUFFER_BINDINGS = 0x8A2F
GL_MAX_UNIFORM_BLOCK_SIZE = 0x8A30
GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS = 0x8A31
GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS = 0x8A32
GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS = 0x8A33
GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT = 0x8A34
GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH = 0x8A35
GL_ACTIVE_UNIFORM_BLOCKS = 0x8A36
GL_UNIFORM_TYPE = 0x8A37
GL_UNIFORM_SIZE = 0x8A38
GL_UNIFORM_NAME_LENGTH = 0x8A39
GL_UNIFORM_BLOCK_INDEX = 0x8A3A
GL_UNIFORM_OFFSET = 0x8A3B
GL_UNIFORM_ARRAY_STRIDE = 0x8A3C
GL_UNIFORM_MATRIX_STRIDE = 0x8A3D
GL_UNIFORM_IS_ROW_MAJOR = 0x8A3E
GL_UNIFORM_BLOCK_BINDING = 0x8A3F
GL_UNIFORM_BLOCK_DATA_SIZE = 0x8A40
GL_UNIFORM_BLOCK_NAME_LENGTH = 0x8A41
GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS = 0x8A42
GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES = 0x8A43
GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER = 0x8A44
GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER = 0x8A45
GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER = 0x8A46
GL_INVALID_INDEX = 0xFFFFFFFF
# ARB_vertex_array_bgra
# ARB_vertex_array_object
GL_VERTEX_ARRAY_BINDING = 0x85B5
# ARB_vertex_attrib_64bit
# ARB_vertex_attrib_binding
GL_VERTEX_ATTRIB_BINDING = 0x82D4
GL_VERTEX_ATTRIB_RELATIVE_OFFSET = 0x82D5
GL_VERTEX_BINDING_DIVISOR = 0x82D6
GL_VERTEX_BINDING_OFFSET = 0x82D7
GL_VERTEX_BINDING_STRIDE = 0x82D8
GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET = 0x82D9
GL_MAX_VERTEX_ATTRIB_BINDINGS = 0x82DA
# ARB_vertex_blend
GL_MAX_VERTEX_UNITS_ARB = 0x86A4
GL_ACTIVE_VERTEX_UNITS_ARB = 0x86A5
GL_WEIGHT_SUM_UNITY_ARB = 0x86A6
GL_VERTEX_BLEND_ARB = 0x86A7
GL_CURRENT_WEIGHT_ARB = 0x86A8
GL_WEIGHT_ARRAY_TYPE_ARB = 0x86A9
GL_WEIGHT_ARRAY_STRIDE_ARB = 0x86AA
GL_WEIGHT_ARRAY_SIZE_ARB = 0x86AB
GL_WEIGHT_ARRAY_POINTER_ARB = 0x86AC
GL_WEIGHT_ARRAY_ARB = 0x86AD
GL_MODELVIEW0_ARB = 0x1700
GL_MODELVIEW1_ARB = 0x850A
GL_MODELVIEW2_ARB = 0x8722
GL_MODELVIEW3_ARB = 0x8723
GL_MODELVIEW4_ARB = 0x8724
GL_MODELVIEW5_ARB = 0x8725
GL_MODELVIEW6_ARB = 0x8726
GL_MODELVIEW7_ARB = 0x8727
GL_MODELVIEW8_ARB = 0x8728
GL_MODELVIEW9_ARB = 0x8729
GL_MODELVIEW10_ARB = 0x872A
GL_MODELVIEW11_ARB = 0x872B
GL_MODELVIEW12_ARB = 0x872C
GL_MODELVIEW13_ARB = 0x872D
GL_MODELVIEW14_ARB = 0x872E
GL_MODELVIEW15_ARB = 0x872F
GL_MODELVIEW16_ARB = 0x8730
GL_MODELVIEW17_ARB = 0x8731
GL_MODELVIEW18_ARB = 0x8732
GL_MODELVIEW19_ARB = 0x8733
GL_MODELVIEW20_ARB = 0x8734
GL_MODELVIEW21_ARB = 0x8735
GL_MODELVIEW22_ARB = 0x8736
GL_MODELVIEW23_ARB = 0x8737
GL_MODELVIEW24_ARB = 0x8738
GL_MODELVIEW25_ARB = 0x8739
GL_MODELVIEW26_ARB = 0x873A
GL_MODELVIEW27_ARB = 0x873B
GL_MODELVIEW28_ARB = 0x873C
GL_MODELVIEW29_ARB = 0x873D
GL_MODELVIEW30_ARB = 0x873E
GL_MODELVIEW31_ARB = 0x873F
# ARB_vertex_buffer_object
GL_BUFFER_SIZE_ARB = 0x8764
GL_BUFFER_USAGE_ARB = 0x8765
GL_ARRAY_BUFFER_ARB = 0x8892
GL_ELEMENT_ARRAY_BUFFER_ARB = 0x8893
GL_ARRAY_BUFFER_BINDING_ARB = 0x8894
GL_ELEMENT_ARRAY_BUFFER_BINDING_ARB = 0x8895
GL_VERTEX_ARRAY_BUFFER_BINDING_ARB = 0x8896
GL_NORMAL_ARRAY_BUFFER_BINDING_ARB = 0x8897
GL_COLOR_ARRAY_BUFFER_BINDING_ARB = 0x8898
GL_INDEX_ARRAY_BUFFER_BINDING_ARB = 0x8899
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING_ARB = 0x889A
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING_ARB = 0x889B
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING_ARB = 0x889C
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING_ARB = 0x889D
GL_WEIGHT_ARRAY_BUFFER_BINDING_ARB = 0x889E
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING_ARB = 0x889F
GL_READ_ONLY_ARB = 0x88B8
GL_WRITE_ONLY_ARB = 0x88B9
GL_READ_WRITE_ARB = 0x88BA
GL_BUFFER_ACCESS_ARB = 0x88BB
GL_BUFFER_MAPPED_ARB = 0x88BC
GL_BUFFER_MAP_POINTER_ARB = 0x88BD
GL_STREAM_DRAW_ARB = 0x88E0
GL_STREAM_READ_ARB = 0x88E1
GL_STREAM_COPY_ARB = 0x88E2
GL_STATIC_DRAW_ARB = 0x88E4
GL_STATIC_READ_ARB = 0x88E5
GL_STATIC_COPY_ARB = 0x88E6
GL_DYNAMIC_DRAW_ARB = 0x88E8
GL_DYNAMIC_READ_ARB = 0x88E9
GL_DYNAMIC_COPY_ARB = 0x88EA
# ARB_vertex_program
GL_COLOR_SUM_ARB = 0x8458
GL_VERTEX_PROGRAM_ARB = 0x8620
GL_VERTEX_ATTRIB_ARRAY_ENABLED_ARB = 0x8622
GL_VERTEX_ATTRIB_ARRAY_SIZE_ARB = 0x8623
GL_VERTEX_ATTRIB_ARRAY_STRIDE_ARB = 0x8624
GL_VERTEX_ATTRIB_ARRAY_TYPE_ARB = 0x8625
GL_CURRENT_VERTEX_ATTRIB_ARB = 0x8626
GL_PROGRAM_LENGTH_ARB = 0x8627
GL_PROGRAM_STRING_ARB = 0x8628
GL_MAX_PROGRAM_MATRIX_STACK_DEPTH_ARB = 0x862E
GL_MAX_PROGRAM_MATRICES_ARB = 0x862F
GL_CURRENT_MATRIX_STACK_DEPTH_ARB = 0x8640
GL_CURRENT_MATRIX_ARB = 0x8641
GL_VERTEX_PROGRAM_POINT_SIZE_ARB = 0x8642
GL_VERTEX_PROGRAM_TWO_SIDE_ARB = 0x8643
GL_VERTEX_ATTRIB_ARRAY_POINTER_ARB = 0x8645
GL_PROGRAM_ERROR_POSITION_ARB = 0x864B
GL_PROGRAM_BINDING_ARB = 0x8677
GL_MAX_VERTEX_ATTRIBS_ARB = 0x8869
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED_ARB = 0x886A
GL_PROGRAM_ERROR_STRING_ARB = 0x8874
GL_PROGRAM_FORMAT_ASCII_ARB = 0x8875
GL_PROGRAM_FORMAT_ARB = 0x8876
GL_PROGRAM_INSTRUCTIONS_ARB = 0x88A0
GL_MAX_PROGRAM_INSTRUCTIONS_ARB = 0x88A1
GL_PROGRAM_NATIVE_INSTRUCTIONS_ARB = 0x88A2
GL_MAX_PROGRAM_NATIVE_INSTRUCTIONS_ARB = 0x88A3
GL_PROGRAM_TEMPORARIES_ARB = 0x88A4
GL_MAX_PROGRAM_TEMPORARIES_ARB = 0x88A5
GL_PROGRAM_NATIVE_TEMPORARIES_ARB = 0x88A6
GL_MAX_PROGRAM_NATIVE_TEMPORARIES_ARB = 0x88A7
GL_PROGRAM_PARAMETERS_ARB = 0x88A8
GL_MAX_PROGRAM_PARAMETERS_ARB = 0x88A9
GL_PROGRAM_NATIVE_PARAMETERS_ARB = 0x88AA
GL_MAX_PROGRAM_NATIVE_PARAMETERS_ARB = 0x88AB
GL_PROGRAM_ATTRIBS_ARB = 0x88AC
GL_MAX_PROGRAM_ATTRIBS_ARB = 0x88AD
GL_PROGRAM_NATIVE_ATTRIBS_ARB = 0x88AE
GL_MAX_PROGRAM_NATIVE_ATTRIBS_ARB = 0x88AF
GL_PROGRAM_ADDRESS_REGISTERS_ARB = 0x88B0
GL_MAX_PROGRAM_ADDRESS_REGISTERS_ARB = 0x88B1
GL_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB = 0x88B2
GL_MAX_PROGRAM_NATIVE_ADDRESS_REGISTERS_ARB = 0x88B3
GL_MAX_PROGRAM_LOCAL_PARAMETERS_ARB = 0x88B4
GL_MAX_PROGRAM_ENV_PARAMETERS_ARB = 0x88B5
GL_PROGRAM_UNDER_NATIVE_LIMITS_ARB = 0x88B6
GL_TRANSPOSE_CURRENT_MATRIX_ARB = 0x88B7
GL_MATRIX0_ARB = 0x88C0
GL_MATRIX1_ARB = 0x88C1
GL_MATRIX2_ARB = 0x88C2
GL_MATRIX3_ARB = 0x88C3
GL_MATRIX4_ARB = 0x88C4
GL_MATRIX5_ARB = 0x88C5
GL_MATRIX6_ARB = 0x88C6
GL_MATRIX7_ARB = 0x88C7
GL_MATRIX8_ARB = 0x88C8
GL_MATRIX9_ARB = 0x88C9
GL_MATRIX10_ARB = 0x88CA
GL_MATRIX11_ARB = 0x88CB
GL_MATRIX12_ARB = 0x88CC
GL_MATRIX13_ARB = 0x88CD
GL_MATRIX14_ARB = 0x88CE
GL_MATRIX15_ARB = 0x88CF
GL_MATRIX16_ARB = 0x88D0
GL_MATRIX17_ARB = 0x88D1
GL_MATRIX18_ARB = 0x88D2
GL_MATRIX19_ARB = 0x88D3
GL_MATRIX20_ARB = 0x88D4
GL_MATRIX21_ARB = 0x88D5
GL_MATRIX22_ARB = 0x88D6
GL_MATRIX23_ARB = 0x88D7
GL_MATRIX24_ARB = 0x88D8
GL_MATRIX25_ARB = 0x88D9
GL_MATRIX26_ARB = 0x88DA
GL_MATRIX27_ARB = 0x88DB
GL_MATRIX28_ARB = 0x88DC
GL_MATRIX29_ARB = 0x88DD
GL_MATRIX30_ARB = 0x88DE
GL_MATRIX31_ARB = 0x88DF
# ARB_vertex_shader
GL_VERTEX_SHADER_ARB = 0x8B31
GL_MAX_VERTEX_UNIFORM_COMPONENTS_ARB = 0x8B4A
GL_MAX_VARYING_FLOATS_ARB = 0x8B4B
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS_ARB = 0x8B4C
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS_ARB = 0x8B4D
GL_OBJECT_ACTIVE_ATTRIBUTES_ARB = 0x8B89
GL_OBJECT_ACTIVE_ATTRIBUTE_MAX_LENGTH_ARB = 0x8B8A
# ARB_vertex_type_2_10_10_10_rev
GL_INT_2_10_10_10_REV = 0x8D9F
# ARB_viewport_array
GL_MAX_VIEWPORTS = 0x825B
GL_VIEWPORT_SUBPIXEL_BITS = 0x825C
GL_VIEWPORT_BOUNDS_RANGE = 0x825D
GL_LAYER_PROVOKING_VERTEX = 0x825E
GL_VIEWPORT_INDEX_PROVOKING_VERTEX = 0x825F
GL_UNDEFINED_VERTEX = 0x8260
# ARB_window_pos
# ATI_draw_buffers
GL_MAX_DRAW_BUFFERS_ATI = 0x8824
GL_DRAW_BUFFER0_ATI = 0x8825
GL_DRAW_BUFFER1_ATI = 0x8826
GL_DRAW_BUFFER2_ATI = 0x8827
GL_DRAW_BUFFER3_ATI = 0x8828
GL_DRAW_BUFFER4_ATI = 0x8829
GL_DRAW_BUFFER5_ATI = 0x882A
GL_DRAW_BUFFER6_ATI = 0x882B
GL_DRAW_BUFFER7_ATI = 0x882C
GL_DRAW_BUFFER8_ATI = 0x882D
GL_DRAW_BUFFER9_ATI = 0x882E
GL_DRAW_BUFFER10_ATI = 0x882F
GL_DRAW_BUFFER11_ATI = 0x8830
GL_DRAW_BUFFER12_ATI = 0x8831
GL_DRAW_BUFFER13_ATI = 0x8832
GL_DRAW_BUFFER14_ATI = 0x8833
GL_DRAW_BUFFER15_ATI = 0x8834
# ATI_element_array
GL_ELEMENT_ARRAY_ATI = 0x8768
GL_ELEMENT_ARRAY_TYPE_ATI = 0x8769
GL_ELEMENT_ARRAY_POINTER_ATI = 0x876A
# ATI_envmap_bumpmap
GL_BUMP_ROT_MATRIX_ATI = 0x8775
GL_BUMP_ROT_MATRIX_SIZE_ATI = 0x8776
GL_BUMP_NUM_TEX_UNITS_ATI = 0x8777
GL_BUMP_TEX_UNITS_ATI = 0x8778
GL_DUDV_ATI = 0x8779
GL_DU8DV8_ATI = 0x877A
GL_BUMP_ENVMAP_ATI = 0x877B
GL_BUMP_TARGET_ATI = 0x877C
# ATI_fragment_shader
GL_FRAGMENT_SHADER_ATI = 0x8920
GL_REG_0_ATI = 0x8921
GL_REG_1_ATI = 0x8922
GL_REG_2_ATI = 0x8923
GL_REG_3_ATI = 0x8924
GL_REG_4_ATI = 0x8925
GL_REG_5_ATI = 0x8926
GL_REG_6_ATI = 0x8927
GL_REG_7_ATI = 0x8928
GL_REG_8_ATI = 0x8929
GL_REG_9_ATI = 0x892A
GL_REG_10_ATI = 0x892B
GL_REG_11_ATI = 0x892C
GL_REG_12_ATI = 0x892D
GL_REG_13_ATI = 0x892E
GL_REG_14_ATI = 0x892F
GL_REG_15_ATI = 0x8930
GL_REG_16_ATI = 0x8931
GL_REG_17_ATI = 0x8932
GL_REG_18_ATI = 0x8933
GL_REG_19_ATI = 0x8934
GL_REG_20_ATI = 0x8935
GL_REG_21_ATI = 0x8936
GL_REG_22_ATI = 0x8937
GL_REG_23_ATI = 0x8938
GL_REG_24_ATI = 0x8939
GL_REG_25_ATI = 0x893A
GL_REG_26_ATI = 0x893B
GL_REG_27_ATI = 0x893C
GL_REG_28_ATI = 0x893D
GL_REG_29_ATI = 0x893E
GL_REG_30_ATI = 0x893F
GL_REG_31_ATI = 0x8940
GL_CON_0_ATI = 0x8941
GL_CON_1_ATI = 0x8942
GL_CON_2_ATI = 0x8943
GL_CON_3_ATI = 0x8944
GL_CON_4_ATI = 0x8945
GL_CON_5_ATI = 0x8946
GL_CON_6_ATI = 0x8947
GL_CON_7_ATI = 0x8948
GL_CON_8_ATI = 0x8949
GL_CON_9_ATI = 0x894A
GL_CON_10_ATI = 0x894B
GL_CON_11_ATI = 0x894C
GL_CON_12_ATI = 0x894D
GL_CON_13_ATI = 0x894E
GL_CON_14_ATI = 0x894F
GL_CON_15_ATI = 0x8950
GL_CON_16_ATI = 0x8951
GL_CON_17_ATI = 0x8952
GL_CON_18_ATI = 0x8953
GL_CON_19_ATI = 0x8954
GL_CON_20_ATI = 0x8955
GL_CON_21_ATI = 0x8956
GL_CON_22_ATI = 0x8957
GL_CON_23_ATI = 0x8958
GL_CON_24_ATI = 0x8959
GL_CON_25_ATI = 0x895A
GL_CON_26_ATI = 0x895B
GL_CON_27_ATI = 0x895C
GL_CON_28_ATI = 0x895D
GL_CON_29_ATI = 0x895E
GL_CON_30_ATI = 0x895F
GL_CON_31_ATI = 0x8960
GL_MOV_ATI = 0x8961
GL_ADD_ATI = 0x8963
GL_MUL_ATI = 0x8964
GL_SUB_ATI = 0x8965
GL_DOT3_ATI = 0x8966
GL_DOT4_ATI = 0x8967
GL_MAD_ATI = 0x8968
GL_LERP_ATI = 0x8969
GL_CND_ATI = 0x896A
GL_CND0_ATI = 0x896B
GL_DOT2_ADD_ATI = 0x896C
GL_SECONDARY_INTERPOLATOR_ATI = 0x896D
GL_NUM_FRAGMENT_REGISTERS_ATI = 0x896E
GL_NUM_FRAGMENT_CONSTANTS_ATI = 0x896F
GL_NUM_PASSES_ATI = 0x8970
GL_NUM_INSTRUCTIONS_PER_PASS_ATI = 0x8971
GL_NUM_INSTRUCTIONS_TOTAL_ATI = 0x8972
GL_NUM_INPUT_INTERPOLATOR_COMPONENTS_ATI = 0x8973
GL_NUM_LOOPBACK_COMPONENTS_ATI = 0x8974
GL_COLOR_ALPHA_PAIRING_ATI = 0x8975
GL_SWIZZLE_STR_ATI = 0x8976
GL_SWIZZLE_STQ_ATI = 0x8977
GL_SWIZZLE_STR_DR_ATI = 0x8978
GL_SWIZZLE_STQ_DQ_ATI = 0x8979
GL_SWIZZLE_STRQ_ATI = 0x897A
GL_SWIZZLE_STRQ_DQ_ATI = 0x897B
GL_RED_BIT_ATI = 0x00000001
GL_GREEN_BIT_ATI = 0x00000002
GL_BLUE_BIT_ATI = 0x00000004
GL_2X_BIT_ATI = 0x00000001
GL_4X_BIT_ATI = 0x00000002
GL_8X_BIT_ATI = 0x00000004
GL_HALF_BIT_ATI = 0x00000008
GL_QUARTER_BIT_ATI = 0x00000010
GL_EIGHTH_BIT_ATI = 0x00000020
GL_SATURATE_BIT_ATI = 0x00000040
GL_COMP_BIT_ATI = 0x00000002
GL_NEGATE_BIT_ATI = 0x00000004
GL_BIAS_BIT_ATI = 0x00000008
# ATI_map_object_buffer
# ATI_meminfo
GL_VBO_FREE_MEMORY_ATI = 0x87FB
GL_TEXTURE_FREE_MEMORY_ATI = 0x87FC
GL_RENDERBUFFER_FREE_MEMORY_ATI = 0x87FD
# ATI_pixel_format_float
GL_RGBA_FLOAT_MODE_ATI = 0x8820
GL_COLOR_CLEAR_UNCLAMPED_VALUE_ATI = 0x8835
WGL_TYPE_RGBA_FLOAT_ATI = 0x21A0
# ATI_pn_triangles
GL_PN_TRIANGLES_ATI = 0x87F0
GL_MAX_PN_TRIANGLES_TESSELATION_LEVEL_ATI = 0x87F1
GL_PN_TRIANGLES_POINT_MODE_ATI = 0x87F2
GL_PN_TRIANGLES_NORMAL_MODE_ATI = 0x87F3
GL_PN_TRIANGLES_TESSELATION_LEVEL_ATI = 0x87F4
GL_PN_TRIANGLES_POINT_MODE_LINEAR_ATI = 0x87F5
GL_PN_TRIANGLES_POINT_MODE_CUBIC_ATI = 0x87F6
GL_PN_TRIANGLES_NORMAL_MODE_LINEAR_ATI = 0x87F7
GL_PN_TRIANGLES_NORMAL_MODE_QUADRATIC_ATI = 0x87F8
# ATI_separate_stencil
GL_STENCIL_BACK_FUNC_ATI = 0x8800
GL_STENCIL_BACK_FAIL_ATI = 0x8801
GL_STENCIL_BACK_PASS_DEPTH_FAIL_ATI = 0x8802
GL_STENCIL_BACK_PASS_DEPTH_PASS_ATI = 0x8803
# ATI_text_fragment_shader
GL_TEXT_FRAGMENT_SHADER_ATI = 0x8200
# ATI_texture_env_combine3
GL_MODULATE_ADD_ATI = 0x8744
GL_MODULATE_SIGNED_ADD_ATI = 0x8745
GL_MODULATE_SUBTRACT_ATI = 0x8746
# ATI_texture_float
GL_RGBA_FLOAT32_ATI = 0x8814
GL_RGB_FLOAT32_ATI = 0x8815
GL_ALPHA_FLOAT32_ATI = 0x8816
GL_INTENSITY_FLOAT32_ATI = 0x8817
GL_LUMINANCE_FLOAT32_ATI = 0x8818
GL_LUMINANCE_ALPHA_FLOAT32_ATI = 0x8819
GL_RGBA_FLOAT16_ATI = 0x881A
GL_RGB_FLOAT16_ATI = 0x881B
GL_ALPHA_FLOAT16_ATI = 0x881C
GL_INTENSITY_FLOAT16_ATI = 0x881D
GL_LUMINANCE_FLOAT16_ATI = 0x881E
GL_LUMINANCE_ALPHA_FLOAT16_ATI = 0x881F
# ATI_texture_mirror_once
GL_MIRROR_CLAMP_ATI = 0x8742
GL_MIRROR_CLAMP_TO_EDGE_ATI = 0x8743
# ATI_vertex_array_object
GL_STATIC_ATI = 0x8760
GL_DYNAMIC_ATI = 0x8761
GL_PRESERVE_ATI = 0x8762
GL_DISCARD_ATI = 0x8763
GL_OBJECT_BUFFER_SIZE_ATI = 0x8764
GL_OBJECT_BUFFER_USAGE_ATI = 0x8765
GL_ARRAY_OBJECT_BUFFER_ATI = 0x8766
GL_ARRAY_OBJECT_OFFSET_ATI = 0x8767
# ATI_vertex_attrib_array_object
# ATI_vertex_streams
GL_MAX_VERTEX_STREAMS_ATI = 0x876B
GL_VERTEX_STREAM0_ATI = 0x876C
GL_VERTEX_STREAM1_ATI = 0x876D
GL_VERTEX_STREAM2_ATI = 0x876E
GL_VERTEX_STREAM3_ATI = 0x876F
GL_VERTEX_STREAM4_ATI = 0x8770
GL_VERTEX_STREAM5_ATI = 0x8771
GL_VERTEX_STREAM6_ATI = 0x8772
GL_VERTEX_STREAM7_ATI = 0x8773
GL_VERTEX_SOURCE_ATI = 0x8774
# EXT_422_pixels
GL_422_EXT = 0x80CC
GL_422_REV_EXT = 0x80CD
GL_422_AVERAGE_EXT = 0x80CE
GL_422_REV_AVERAGE_EXT = 0x80CF
# EXT_abgr
GL_ABGR_EXT = 0x8000
# EXT_bgra
GL_BGR_EXT = 0x80E0
GL_BGRA_EXT = 0x80E1
# EXT_bindable_uniform
GL_MAX_VERTEX_BINDABLE_UNIFORMS_EXT = 0x8DE2
GL_MAX_FRAGMENT_BINDABLE_UNIFORMS_EXT = 0x8DE3
GL_MAX_GEOMETRY_BINDABLE_UNIFORMS_EXT = 0x8DE4
GL_MAX_BINDABLE_UNIFORM_SIZE_EXT = 0x8DED
GL_UNIFORM_BUFFER_EXT = 0x8DEE
GL_UNIFORM_BUFFER_BINDING_EXT = 0x8DEF
# EXT_blend_color
GL_CONSTANT_COLOR_EXT = 0x8001
GL_ONE_MINUS_CONSTANT_COLOR_EXT = 0x8002
GL_CONSTANT_ALPHA_EXT = 0x8003
GL_ONE_MINUS_CONSTANT_ALPHA_EXT = 0x8004
GL_BLEND_COLOR_EXT = 0x8005
# EXT_blend_equation_separate
GL_BLEND_EQUATION_RGB_EXT = 0x8009
GL_BLEND_EQUATION_ALPHA_EXT = 0x883D
# EXT_blend_func_separate
GL_BLEND_DST_RGB_EXT = 0x80C8
GL_BLEND_SRC_RGB_EXT = 0x80C9
GL_BLEND_DST_ALPHA_EXT = 0x80CA
GL_BLEND_SRC_ALPHA_EXT = 0x80CB
# EXT_blend_logic_op
# EXT_blend_minmax
GL_FUNC_ADD_EXT = 0x8006
GL_MIN_EXT = 0x8007
GL_MAX_EXT = 0x8008
GL_BLEND_EQUATION_EXT = 0x8009
# EXT_blend_subtract
GL_FUNC_SUBTRACT_EXT = 0x800A
GL_FUNC_REVERSE_SUBTRACT_EXT = 0x800B
# EXT_clip_volume_hint
GL_CLIP_VOLUME_CLIPPING_HINT_EXT = 0x80F0
# EXT_cmyka
GL_CMYK_EXT = 0x800C
GL_CMYKA_EXT = 0x800D
GL_PACK_CMYK_HINT_EXT = 0x800E
GL_UNPACK_CMYK_HINT_EXT = 0x800F
# EXT_color_subtable
# EXT_compiled_vertex_array
GL_ARRAY_ELEMENT_LOCK_FIRST_EXT = 0x81A8
GL_ARRAY_ELEMENT_LOCK_COUNT_EXT = 0x81A9
# EXT_convolution
GL_CONVOLUTION_1D_EXT = 0x8010
GL_CONVOLUTION_2D_EXT = 0x8011
GL_SEPARABLE_2D_EXT = 0x8012
GL_CONVOLUTION_BORDER_MODE_EXT = 0x8013
GL_CONVOLUTION_FILTER_SCALE_EXT = 0x8014
GL_CONVOLUTION_FILTER_BIAS_EXT = 0x8015
GL_REDUCE_EXT = 0x8016
GL_CONVOLUTION_FORMAT_EXT = 0x8017
GL_CONVOLUTION_WIDTH_EXT = 0x8018
GL_CONVOLUTION_HEIGHT_EXT = 0x8019
GL_MAX_CONVOLUTION_WIDTH_EXT = 0x801A
GL_MAX_CONVOLUTION_HEIGHT_EXT = 0x801B
GL_POST_CONVOLUTION_RED_SCALE_EXT = 0x801C
GL_POST_CONVOLUTION_GREEN_SCALE_EXT = 0x801D
GL_POST_CONVOLUTION_BLUE_SCALE_EXT = 0x801E
GL_POST_CONVOLUTION_ALPHA_SCALE_EXT = 0x801F
GL_POST_CONVOLUTION_RED_BIAS_EXT = 0x8020
GL_POST_CONVOLUTION_GREEN_BIAS_EXT = 0x8021
GL_POST_CONVOLUTION_BLUE_BIAS_EXT = 0x8022
GL_POST_CONVOLUTION_ALPHA_BIAS_EXT = 0x8023
# EXT_coordinate_frame
GL_TANGENT_ARRAY_EXT = 0x8439
GL_BINORMAL_ARRAY_EXT = 0x843A
GL_CURRENT_TANGENT_EXT = 0x843B
GL_CURRENT_BINORMAL_EXT = 0x843C
GL_TANGENT_ARRAY_TYPE_EXT = 0x843E
GL_TANGENT_ARRAY_STRIDE_EXT = 0x843F
GL_BINORMAL_ARRAY_TYPE_EXT = 0x8440
GL_BINORMAL_ARRAY_STRIDE_EXT = 0x8441
GL_TANGENT_ARRAY_POINTER_EXT = 0x8442
GL_BINORMAL_ARRAY_POINTER_EXT = 0x8443
GL_MAP1_TANGENT_EXT = 0x8444
GL_MAP2_TANGENT_EXT = 0x8445
GL_MAP1_BINORMAL_EXT = 0x8446
GL_MAP2_BINORMAL_EXT = 0x8447
# EXT_copy_texture
# EXT_cull_vertex
GL_CULL_VERTEX_EXT = 0x81AA
GL_CULL_VERTEX_EYE_POSITION_EXT = 0x81AB
GL_CULL_VERTEX_OBJECT_POSITION_EXT = 0x81AC
# EXT_depth_bounds_test
GL_DEPTH_BOUNDS_TEST_EXT = 0x8890
GL_DEPTH_BOUNDS_EXT = 0x8891
# EXT_direct_state_access
GL_PROGRAM_MATRIX_EXT = 0x8E2D
GL_TRANSPOSE_PROGRAM_MATRIX_EXT = 0x8E2E
GL_PROGRAM_MATRIX_STACK_DEPTH_EXT = 0x8E2F
# EXT_draw_buffers2
# EXT_draw_instanced
# EXT_draw_range_elements
GL_MAX_ELEMENTS_VERTICES_EXT = 0x80E8
GL_MAX_ELEMENTS_INDICES_EXT = 0x80E9
# EXT_fog_coord
GL_FOG_COORDINATE_SOURCE_EXT = 0x8450
GL_FOG_COORDINATE_EXT = 0x8451
GL_FRAGMENT_DEPTH_EXT = 0x8452
GL_CURRENT_FOG_COORDINATE_EXT = 0x8453
GL_FOG_COORDINATE_ARRAY_TYPE_EXT = 0x8454
GL_FOG_COORDINATE_ARRAY_STRIDE_EXT = 0x8455
GL_FOG_COORDINATE_ARRAY_POINTER_EXT = 0x8456
GL_FOG_COORDINATE_ARRAY_EXT = 0x8457
# EXT_framebuffer_blit
GL_READ_FRAMEBUFFER_EXT = 0x8CA8
GL_DRAW_FRAMEBUFFER_EXT = 0x8CA9
GL_DRAW_FRAMEBUFFER_BINDING_EXT = 0x8CA6 # GL_FRAMEBUFFER_BINDING_EXT
GL_READ_FRAMEBUFFER_BINDING_EXT = 0x8CAA
# EXT_framebuffer_multisample
GL_RENDERBUFFER_SAMPLES_EXT = 0x8CAB
GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE_EXT = 0x8D56
GL_MAX_SAMPLES_EXT = 0x8D57
# EXT_framebuffer_multisample_blit_scaled
GL_SCALED_RESOLVE_FASTEST_EXT = 0x90BA
GL_SCALED_RESOLVE_NICEST_EXT = 0x90BB
# EXT_framebuffer_object
GL_INVALID_FRAMEBUFFER_OPERATION_EXT = 0x0506
GL_MAX_RENDERBUFFER_SIZE_EXT = 0x84E8
GL_FRAMEBUFFER_BINDING_EXT = 0x8CA6
GL_RENDERBUFFER_BINDING_EXT = 0x8CA7
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE_EXT = 0x8CD0
GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME_EXT = 0x8CD1
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL_EXT = 0x8CD2
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE_EXT = 0x8CD3
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_3D_ZOFFSET_EXT = 0x8CD4
GL_FRAMEBUFFER_COMPLETE_EXT = 0x8CD5
GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT_EXT = 0x8CD6
GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT_EXT = 0x8CD7
GL_FRAMEBUFFER_INCOMPLETE_DIMENSIONS_EXT = 0x8CD9
GL_FRAMEBUFFER_INCOMPLETE_FORMATS_EXT = 0x8CDA
GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER_EXT = 0x8CDB
GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER_EXT = 0x8CDC
GL_FRAMEBUFFER_UNSUPPORTED_EXT = 0x8CDD
GL_MAX_COLOR_ATTACHMENTS_EXT = 0x8CDF
GL_COLOR_ATTACHMENT0_EXT = 0x8CE0
GL_COLOR_ATTACHMENT1_EXT = 0x8CE1
GL_COLOR_ATTACHMENT2_EXT = 0x8CE2
GL_COLOR_ATTACHMENT3_EXT = 0x8CE3
GL_COLOR_ATTACHMENT4_EXT = 0x8CE4
GL_COLOR_ATTACHMENT5_EXT = 0x8CE5
GL_COLOR_ATTACHMENT6_EXT = 0x8CE6
GL_COLOR_ATTACHMENT7_EXT = 0x8CE7
GL_COLOR_ATTACHMENT8_EXT = 0x8CE8
GL_COLOR_ATTACHMENT9_EXT = 0x8CE9
GL_COLOR_ATTACHMENT10_EXT = 0x8CEA
GL_COLOR_ATTACHMENT11_EXT = 0x8CEB
GL_COLOR_ATTACHMENT12_EXT = 0x8CEC
GL_COLOR_ATTACHMENT13_EXT = 0x8CED
GL_COLOR_ATTACHMENT14_EXT = 0x8CEE
GL_COLOR_ATTACHMENT15_EXT = 0x8CEF
GL_DEPTH_ATTACHMENT_EXT = 0x8D00
GL_STENCIL_ATTACHMENT_EXT = 0x8D20
GL_FRAMEBUFFER_EXT = 0x8D40
GL_RENDERBUFFER_EXT = 0x8D41
GL_RENDERBUFFER_WIDTH_EXT = 0x8D42
GL_RENDERBUFFER_HEIGHT_EXT = 0x8D43
GL_RENDERBUFFER_INTERNAL_FORMAT_EXT = 0x8D44
GL_STENCIL_INDEX1_EXT = 0x8D46
GL_STENCIL_INDEX4_EXT = 0x8D47
GL_STENCIL_INDEX8_EXT = 0x8D48
GL_STENCIL_INDEX16_EXT = 0x8D49
GL_RENDERBUFFER_RED_SIZE_EXT = 0x8D50
GL_RENDERBUFFER_GREEN_SIZE_EXT = 0x8D51
GL_RENDERBUFFER_BLUE_SIZE_EXT = 0x8D52
GL_RENDERBUFFER_ALPHA_SIZE_EXT = 0x8D53
GL_RENDERBUFFER_DEPTH_SIZE_EXT = 0x8D54
GL_RENDERBUFFER_STENCIL_SIZE_EXT = 0x8D55
# EXT_framebuffer_sRGB
GL_FRAMEBUFFER_SRGB_EXT = 0x8DB9
GL_FRAMEBUFFER_SRGB_CAPABLE_EXT = 0x8DBA
WGL_FRAMEBUFFER_SRGB_CAPABLE_EXT = 0x20A9
# EXT_geometry_shader4
GL_GEOMETRY_SHADER_EXT = 0x8DD9
GL_MAX_GEOMETRY_VARYING_COMPONENTS_EXT = 0x8DDD
GL_MAX_VERTEX_VARYING_COMPONENTS_EXT = 0x8DDE
GL_MAX_VARYING_COMPONENTS_EXT = 0x8B4B
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS_EXT = 0x8DDF
GL_MAX_GEOMETRY_OUTPUT_VERTICES_EXT = 0x8DE0
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS_EXT = 0x8DE1
# EXT_gpu_program_parameters
# EXT_gpu_shader4
GL_SAMPLER_1D_ARRAY_EXT = 0x8DC0
GL_SAMPLER_2D_ARRAY_EXT = 0x8DC1
GL_SAMPLER_BUFFER_EXT = 0x8DC2
GL_SAMPLER_1D_ARRAY_SHADOW_EXT = 0x8DC3
GL_SAMPLER_2D_ARRAY_SHADOW_EXT = 0x8DC4
GL_SAMPLER_CUBE_SHADOW_EXT = 0x8DC5
GL_UNSIGNED_INT_VEC2_EXT = 0x8DC6
GL_UNSIGNED_INT_VEC3_EXT = 0x8DC7
GL_UNSIGNED_INT_VEC4_EXT = 0x8DC8
GL_INT_SAMPLER_1D_EXT = 0x8DC9
GL_INT_SAMPLER_2D_EXT = 0x8DCA
GL_INT_SAMPLER_3D_EXT = 0x8DCB
GL_INT_SAMPLER_CUBE_EXT = 0x8DCC
GL_INT_SAMPLER_2D_RECT_EXT = 0x8DCD
GL_INT_SAMPLER_1D_ARRAY_EXT = 0x8DCE
GL_INT_SAMPLER_2D_ARRAY_EXT = 0x8DCF
GL_INT_SAMPLER_BUFFER_EXT = 0x8DD0
GL_UNSIGNED_INT_SAMPLER_1D_EXT = 0x8DD1
GL_UNSIGNED_INT_SAMPLER_2D_EXT = 0x8DD2
GL_UNSIGNED_INT_SAMPLER_3D_EXT = 0x8DD3
GL_UNSIGNED_INT_SAMPLER_CUBE_EXT = 0x8DD4
GL_UNSIGNED_INT_SAMPLER_2D_RECT_EXT = 0x8DD5
GL_UNSIGNED_INT_SAMPLER_1D_ARRAY_EXT = 0x8DD6
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY_EXT = 0x8DD7
GL_UNSIGNED_INT_SAMPLER_BUFFER_EXT = 0x8DD8
# EXT_histogram
GL_HISTOGRAM_EXT = 0x8024
GL_PROXY_HISTOGRAM_EXT = 0x8025
GL_HISTOGRAM_WIDTH_EXT = 0x8026
GL_HISTOGRAM_FORMAT_EXT = 0x8027
GL_HISTOGRAM_RED_SIZE_EXT = 0x8028
GL_HISTOGRAM_GREEN_SIZE_EXT = 0x8029
GL_HISTOGRAM_BLUE_SIZE_EXT = 0x802A
GL_HISTOGRAM_ALPHA_SIZE_EXT = 0x802B
GL_HISTOGRAM_LUMINANCE_SIZE_EXT = 0x802C
GL_HISTOGRAM_SINK_EXT = 0x802D
GL_MINMAX_EXT = 0x802E
GL_MINMAX_FORMAT_EXT = 0x802F
GL_MINMAX_SINK_EXT = 0x8030
GL_TABLE_TOO_LARGE_EXT = 0x8031
# EXT_index_array_formats
GL_IUI_V2F_EXT = 0x81AD
GL_IUI_V3F_EXT = 0x81AE
GL_IUI_N3F_V2F_EXT = 0x81AF
GL_IUI_N3F_V3F_EXT = 0x81B0
GL_T2F_IUI_V2F_EXT = 0x81B1
GL_T2F_IUI_V3F_EXT = 0x81B2
GL_T2F_IUI_N3F_V2F_EXT = 0x81B3
GL_T2F_IUI_N3F_V3F_EXT = 0x81B4
# EXT_index_func
GL_INDEX_TEST_EXT = 0x81B5
GL_INDEX_TEST_FUNC_EXT = 0x81B6
GL_INDEX_TEST_REF_EXT = 0x81B7
# EXT_index_material
GL_INDEX_MATERIAL_EXT = 0x81B8
GL_INDEX_MATERIAL_PARAMETER_EXT = 0x81B9
GL_INDEX_MATERIAL_FACE_EXT = 0x81BA
# EXT_index_texture
# EXT_light_texture
GL_FRAGMENT_MATERIAL_EXT = 0x8349
GL_FRAGMENT_NORMAL_EXT = 0x834A
GL_FRAGMENT_COLOR_EXT = 0x834C
GL_ATTENUATION_EXT = 0x834D
GL_SHADOW_ATTENUATION_EXT = 0x834E
GL_TEXTURE_APPLICATION_MODE_EXT = 0x834F
GL_TEXTURE_LIGHT_EXT = 0x8350
GL_TEXTURE_MATERIAL_FACE_EXT = 0x8351
GL_TEXTURE_MATERIAL_PARAMETER_EXT = 0x8352
# EXT_misc_attribute
# EXT_multi_draw_arrays
# EXT_multisample
GL_MULTISAMPLE_EXT = 0x809D
GL_SAMPLE_ALPHA_TO_MASK_EXT = 0x809E
GL_SAMPLE_ALPHA_TO_ONE_EXT = 0x809F
GL_SAMPLE_MASK_EXT = 0x80A0
GL_1PASS_EXT = 0x80A1
GL_2PASS_0_EXT = 0x80A2
GL_2PASS_1_EXT = 0x80A3
GL_4PASS_0_EXT = 0x80A4
GL_4PASS_1_EXT = 0x80A5
GL_4PASS_2_EXT = 0x80A6
GL_4PASS_3_EXT = 0x80A7
GL_SAMPLE_BUFFERS_EXT = 0x80A8
GL_SAMPLES_EXT = 0x80A9
GL_SAMPLE_MASK_VALUE_EXT = 0x80AA
GL_SAMPLE_MASK_INVERT_EXT = 0x80AB
GL_SAMPLE_PATTERN_EXT = 0x80AC
GL_MULTISAMPLE_BIT_EXT = 0x20000000
WGL_SAMPLE_BUFFERS_EXT = 0x2041
WGL_SAMPLES_EXT = 0x2042
# EXT_packed_depth_stencil
GL_DEPTH_STENCIL_EXT = 0x84F9
GL_UNSIGNED_INT_24_8_EXT = 0x84FA
GL_DEPTH24_STENCIL8_EXT = 0x88F0
GL_TEXTURE_STENCIL_SIZE_EXT = 0x88F1
# EXT_packed_float
GL_R11F_G11F_B10F_EXT = 0x8C3A
GL_UNSIGNED_INT_10F_11F_11F_REV_EXT = 0x8C3B
GL_RGBA_SIGNED_COMPONENTS_EXT = 0x8C3C
# EXT_packed_pixels
GL_UNSIGNED_BYTE_3_3_2_EXT = 0x8032
GL_UNSIGNED_SHORT_4_4_4_4_EXT = 0x8033
GL_UNSIGNED_SHORT_5_5_5_1_EXT = 0x8034
GL_UNSIGNED_INT_8_8_8_8_EXT = 0x8035
GL_UNSIGNED_INT_10_10_10_2_EXT = 0x8036
# EXT_paletted_texture
GL_COLOR_INDEX1_EXT = 0x80E2
GL_COLOR_INDEX2_EXT = 0x80E3
GL_COLOR_INDEX4_EXT = 0x80E4
GL_COLOR_INDEX8_EXT = 0x80E5
GL_COLOR_INDEX12_EXT = 0x80E6
GL_COLOR_INDEX16_EXT = 0x80E7
GL_TEXTURE_INDEX_SIZE_EXT = 0x80ED
# EXT_pixel_buffer_object
GL_PIXEL_PACK_BUFFER_EXT = 0x88EB
GL_PIXEL_UNPACK_BUFFER_EXT = 0x88EC
GL_PIXEL_PACK_BUFFER_BINDING_EXT = 0x88ED
GL_PIXEL_UNPACK_BUFFER_BINDING_EXT = 0x88EF
# EXT_pixel_transform
GL_PIXEL_TRANSFORM_2D_EXT = 0x8330
GL_PIXEL_MAG_FILTER_EXT = 0x8331
GL_PIXEL_MIN_FILTER_EXT = 0x8332
GL_PIXEL_CUBIC_WEIGHT_EXT = 0x8333
GL_CUBIC_EXT = 0x8334
GL_AVERAGE_EXT = 0x8335
GL_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT = 0x8336
GL_MAX_PIXEL_TRANSFORM_2D_STACK_DEPTH_EXT = 0x8337
GL_PIXEL_TRANSFORM_2D_MATRIX_EXT = 0x8338
# EXT_pixel_transform_color_table
# EXT_point_parameters
GL_POINT_SIZE_MIN_EXT = 0x8126
GL_POINT_SIZE_MAX_EXT = 0x8127
GL_POINT_FADE_THRESHOLD_SIZE_EXT = 0x8128
GL_DISTANCE_ATTENUATION_EXT = 0x8129
# EXT_polygon_offset
GL_POLYGON_OFFSET_EXT = 0x8037
GL_POLYGON_OFFSET_FACTOR_EXT = 0x8038
GL_POLYGON_OFFSET_BIAS_EXT = 0x8039
# EXT_provoking_vertex
GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION_EXT = 0x8E4C
GL_FIRST_VERTEX_CONVENTION_EXT = 0x8E4D
GL_LAST_VERTEX_CONVENTION_EXT = 0x8E4E
GL_PROVOKING_VERTEX_EXT = 0x8E4F
# EXT_rescale_normal
GL_RESCALE_NORMAL_EXT = 0x803A
# EXT_secondary_color
GL_COLOR_SUM_EXT = 0x8458
GL_CURRENT_SECONDARY_COLOR_EXT = 0x8459
GL_SECONDARY_COLOR_ARRAY_SIZE_EXT = 0x845A
GL_SECONDARY_COLOR_ARRAY_TYPE_EXT = 0x845B
GL_SECONDARY_COLOR_ARRAY_STRIDE_EXT = 0x845C
GL_SECONDARY_COLOR_ARRAY_POINTER_EXT = 0x845D
GL_SECONDARY_COLOR_ARRAY_EXT = 0x845E
# EXT_separate_shader_objects
GL_ACTIVE_PROGRAM_EXT = 0x8B8D
# EXT_separate_specular_color
GL_LIGHT_MODEL_COLOR_CONTROL_EXT = 0x81F8
GL_SINGLE_COLOR_EXT = 0x81F9
GL_SEPARATE_SPECULAR_COLOR_EXT = 0x81FA
# EXT_shader_image_load_store
GL_MAX_IMAGE_UNITS_EXT = 0x8F38
GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS_EXT = 0x8F39
GL_IMAGE_BINDING_NAME_EXT = 0x8F3A
GL_IMAGE_BINDING_LEVEL_EXT = 0x8F3B
GL_IMAGE_BINDING_LAYERED_EXT = 0x8F3C
GL_IMAGE_BINDING_LAYER_EXT = 0x8F3D
GL_IMAGE_BINDING_ACCESS_EXT = 0x8F3E
GL_IMAGE_1D_EXT = 0x904C
GL_IMAGE_2D_EXT = 0x904D
GL_IMAGE_3D_EXT = 0x904E
GL_IMAGE_2D_RECT_EXT = 0x904F
GL_IMAGE_CUBE_EXT = 0x9050
GL_IMAGE_BUFFER_EXT = 0x9051
GL_IMAGE_1D_ARRAY_EXT = 0x9052
GL_IMAGE_2D_ARRAY_EXT = 0x9053
GL_IMAGE_CUBE_MAP_ARRAY_EXT = 0x9054
GL_IMAGE_2D_MULTISAMPLE_EXT = 0x9055
GL_IMAGE_2D_MULTISAMPLE_ARRAY_EXT = 0x9056
GL_INT_IMAGE_1D_EXT = 0x9057
GL_INT_IMAGE_2D_EXT = 0x9058
GL_INT_IMAGE_3D_EXT = 0x9059
GL_INT_IMAGE_2D_RECT_EXT = 0x905A
GL_INT_IMAGE_CUBE_EXT = 0x905B
GL_INT_IMAGE_BUFFER_EXT = 0x905C
GL_INT_IMAGE_1D_ARRAY_EXT = 0x905D
GL_INT_IMAGE_2D_ARRAY_EXT = 0x905E
GL_INT_IMAGE_CUBE_MAP_ARRAY_EXT = 0x905F
GL_INT_IMAGE_2D_MULTISAMPLE_EXT = 0x9060
GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY_EXT = 0x9061
GL_UNSIGNED_INT_IMAGE_1D_EXT = 0x9062
GL_UNSIGNED_INT_IMAGE_2D_EXT = 0x9063
GL_UNSIGNED_INT_IMAGE_3D_EXT = 0x9064
GL_UNSIGNED_INT_IMAGE_2D_RECT_EXT = 0x9065
GL_UNSIGNED_INT_IMAGE_CUBE_EXT = 0x9066
GL_UNSIGNED_INT_IMAGE_BUFFER_EXT = 0x9067
GL_UNSIGNED_INT_IMAGE_1D_ARRAY_EXT = 0x9068
GL_UNSIGNED_INT_IMAGE_2D_ARRAY_EXT = 0x9069
GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY_EXT = 0x906A
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_EXT = 0x906B
GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY_EXT = 0x906C
GL_MAX_IMAGE_SAMPLES_EXT = 0x906D
GL_IMAGE_BINDING_FORMAT_EXT = 0x906E
GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT_EXT = 0x00000001
GL_ELEMENT_ARRAY_BARRIER_BIT_EXT = 0x00000002
GL_UNIFORM_BARRIER_BIT_EXT = 0x00000004
GL_TEXTURE_FETCH_BARRIER_BIT_EXT = 0x00000008
GL_SHADER_IMAGE_ACCESS_BARRIER_BIT_EXT = 0x00000020
GL_COMMAND_BARRIER_BIT_EXT = 0x00000040
GL_PIXEL_BUFFER_BARRIER_BIT_EXT = 0x00000080
GL_TEXTURE_UPDATE_BARRIER_BIT_EXT = 0x00000100
GL_BUFFER_UPDATE_BARRIER_BIT_EXT = 0x00000200
GL_FRAMEBUFFER_BARRIER_BIT_EXT = 0x00000400
GL_TRANSFORM_FEEDBACK_BARRIER_BIT_EXT = 0x00000800
GL_ATOMIC_COUNTER_BARRIER_BIT_EXT = 0x00001000
GL_ALL_BARRIER_BITS_EXT = 0xFFFFFFFF
# EXT_shadow_funcs
# EXT_shared_texture_palette
GL_SHARED_TEXTURE_PALETTE_EXT = 0x81FB
# EXT_stencil_clear_tag
GL_STENCIL_TAG_BITS_EXT = 0x88F2
GL_STENCIL_CLEAR_TAG_VALUE_EXT = 0x88F3
# EXT_stencil_two_side
GL_STENCIL_TEST_TWO_SIDE_EXT = 0x8910
GL_ACTIVE_STENCIL_FACE_EXT = 0x8911
# EXT_stencil_wrap
GL_INCR_WRAP_EXT = 0x8507
GL_DECR_WRAP_EXT = 0x8508
# EXT_subtexture
# EXT_texture
GL_ALPHA4_EXT = 0x803B
GL_ALPHA8_EXT = 0x803C
GL_ALPHA12_EXT = 0x803D
GL_ALPHA16_EXT = 0x803E
GL_LUMINANCE4_EXT = 0x803F
GL_LUMINANCE8_EXT = 0x8040
GL_LUMINANCE12_EXT = 0x8041
GL_LUMINANCE16_EXT = 0x8042
GL_LUMINANCE4_ALPHA4_EXT = 0x8043
GL_LUMINANCE6_ALPHA2_EXT = 0x8044
GL_LUMINANCE8_ALPHA8_EXT = 0x8045
GL_LUMINANCE12_ALPHA4_EXT = 0x8046
GL_LUMINANCE12_ALPHA12_EXT = 0x8047
GL_LUMINANCE16_ALPHA16_EXT = 0x8048
GL_INTENSITY_EXT = 0x8049
GL_INTENSITY4_EXT = 0x804A
GL_INTENSITY8_EXT = 0x804B
GL_INTENSITY12_EXT = 0x804C
GL_INTENSITY16_EXT = 0x804D
GL_RGB2_EXT = 0x804E
GL_RGB4_EXT = 0x804F
GL_RGB5_EXT = 0x8050
GL_RGB8_EXT = 0x8051
GL_RGB10_EXT = 0x8052
GL_RGB12_EXT = 0x8053
GL_RGB16_EXT = 0x8054
GL_RGBA2_EXT = 0x8055
GL_RGBA4_EXT = 0x8056
GL_RGB5_A1_EXT = 0x8057
GL_RGBA8_EXT = 0x8058
GL_RGB10_A2_EXT = 0x8059
GL_RGBA12_EXT = 0x805A
GL_RGBA16_EXT = 0x805B
GL_TEXTURE_RED_SIZE_EXT = 0x805C
GL_TEXTURE_GREEN_SIZE_EXT = 0x805D
GL_TEXTURE_BLUE_SIZE_EXT = 0x805E
GL_TEXTURE_ALPHA_SIZE_EXT = 0x805F
GL_TEXTURE_LUMINANCE_SIZE_EXT = 0x8060
GL_TEXTURE_INTENSITY_SIZE_EXT = 0x8061
GL_REPLACE_EXT = 0x8062
GL_PROXY_TEXTURE_1D_EXT = 0x8063
GL_PROXY_TEXTURE_2D_EXT = 0x8064
GL_TEXTURE_TOO_LARGE_EXT = 0x8065
# EXT_texture3D
GL_PACK_SKIP_IMAGES_EXT = 0x806B
GL_PACK_IMAGE_HEIGHT_EXT = 0x806C
GL_UNPACK_SKIP_IMAGES_EXT = 0x806D
GL_UNPACK_IMAGE_HEIGHT_EXT = 0x806E
GL_TEXTURE_3D_EXT = 0x806F
GL_PROXY_TEXTURE_3D_EXT = 0x8070
GL_TEXTURE_DEPTH_EXT = 0x8071
GL_TEXTURE_WRAP_R_EXT = 0x8072
GL_MAX_3D_TEXTURE_SIZE_EXT = 0x8073
# EXT_texture_array
GL_TEXTURE_1D_ARRAY_EXT = 0x8C18
GL_PROXY_TEXTURE_1D_ARRAY_EXT = 0x8C19
GL_TEXTURE_2D_ARRAY_EXT = 0x8C1A
GL_PROXY_TEXTURE_2D_ARRAY_EXT = 0x8C1B
GL_TEXTURE_BINDING_1D_ARRAY_EXT = 0x8C1C
GL_TEXTURE_BINDING_2D_ARRAY_EXT = 0x8C1D
GL_MAX_ARRAY_TEXTURE_LAYERS_EXT = 0x88FF
GL_COMPARE_REF_DEPTH_TO_TEXTURE_EXT = 0x884E
# EXT_texture_buffer_object
GL_TEXTURE_BUFFER_EXT = 0x8C2A
GL_MAX_TEXTURE_BUFFER_SIZE_EXT = 0x8C2B
GL_TEXTURE_BINDING_BUFFER_EXT = 0x8C2C
GL_TEXTURE_BUFFER_DATA_STORE_BINDING_EXT = 0x8C2D
GL_TEXTURE_BUFFER_FORMAT_EXT = 0x8C2E
# EXT_texture_compression_latc
GL_COMPRESSED_LUMINANCE_LATC1_EXT = 0x8C70
GL_COMPRESSED_SIGNED_LUMINANCE_LATC1_EXT = 0x8C71
GL_COMPRESSED_LUMINANCE_ALPHA_LATC2_EXT = 0x8C72
GL_COMPRESSED_SIGNED_LUMINANCE_ALPHA_LATC2_EXT = 0x8C73
# EXT_texture_compression_rgtc
GL_COMPRESSED_RED_RGTC1_EXT = 0x8DBB
GL_COMPRESSED_SIGNED_RED_RGTC1_EXT = 0x8DBC
GL_COMPRESSED_RED_GREEN_RGTC2_EXT = 0x8DBD
GL_COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT = 0x8DBE
# EXT_texture_compression_s3tc
GL_COMPRESSED_RGB_S3TC_DXT1_EXT = 0x83F0
GL_COMPRESSED_RGBA_S3TC_DXT1_EXT = 0x83F1
GL_COMPRESSED_RGBA_S3TC_DXT3_EXT = 0x83F2
GL_COMPRESSED_RGBA_S3TC_DXT5_EXT = 0x83F3
# EXT_texture_cube_map
GL_NORMAL_MAP_EXT = 0x8511
GL_REFLECTION_MAP_EXT = 0x8512
GL_TEXTURE_CUBE_MAP_EXT = 0x8513
GL_TEXTURE_BINDING_CUBE_MAP_EXT = 0x8514
GL_TEXTURE_CUBE_MAP_POSITIVE_X_EXT = 0x8515
GL_TEXTURE_CUBE_MAP_NEGATIVE_X_EXT = 0x8516
GL_TEXTURE_CUBE_MAP_POSITIVE_Y_EXT = 0x8517
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y_EXT = 0x8518
GL_TEXTURE_CUBE_MAP_POSITIVE_Z_EXT = 0x8519
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z_EXT = 0x851A
GL_PROXY_TEXTURE_CUBE_MAP_EXT = 0x851B
GL_MAX_CUBE_MAP_TEXTURE_SIZE_EXT = 0x851C
# EXT_texture_edge_clamp
GL_CLAMP_TO_EDGE_EXT = 0x812F
# EXT_texture_env_add
# EXT_texture_env_combine
GL_COMBINE_EXT = 0x8570
GL_COMBINE_RGB_EXT = 0x8571
GL_COMBINE_ALPHA_EXT = 0x8572
GL_RGB_SCALE_EXT = 0x8573
GL_ADD_SIGNED_EXT = 0x8574
GL_INTERPOLATE_EXT = 0x8575
GL_CONSTANT_EXT = 0x8576
GL_PRIMARY_COLOR_EXT = 0x8577
GL_PREVIOUS_EXT = 0x8578
GL_SOURCE0_RGB_EXT = 0x8580
GL_SOURCE1_RGB_EXT = 0x8581
GL_SOURCE2_RGB_EXT = 0x8582
GL_SOURCE0_ALPHA_EXT = 0x8588
GL_SOURCE1_ALPHA_EXT = 0x8589
GL_SOURCE2_ALPHA_EXT = 0x858A
GL_OPERAND0_RGB_EXT = 0x8590
GL_OPERAND1_RGB_EXT = 0x8591
GL_OPERAND2_RGB_EXT = 0x8592
GL_OPERAND0_ALPHA_EXT = 0x8598
GL_OPERAND1_ALPHA_EXT = 0x8599
GL_OPERAND2_ALPHA_EXT = 0x859A
# EXT_texture_env_dot3
GL_DOT3_RGB_EXT = 0x8740
GL_DOT3_RGBA_EXT = 0x8741
# EXT_texture_filter_anisotropic
GL_TEXTURE_MAX_ANISOTROPY_EXT = 0x84FE
GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT = 0x84FF
# EXT_texture_integer
GL_RGBA32UI_EXT = 0x8D70
GL_RGB32UI_EXT = 0x8D71
GL_ALPHA32UI_EXT = 0x8D72
GL_INTENSITY32UI_EXT = 0x8D73
GL_LUMINANCE32UI_EXT = 0x8D74
GL_LUMINANCE_ALPHA32UI_EXT = 0x8D75
GL_RGBA16UI_EXT = 0x8D76
GL_RGB16UI_EXT = 0x8D77
GL_ALPHA16UI_EXT = 0x8D78
GL_INTENSITY16UI_EXT = 0x8D79
GL_LUMINANCE16UI_EXT = 0x8D7A
GL_LUMINANCE_ALPHA16UI_EXT = 0x8D7B
GL_RGBA8UI_EXT = 0x8D7C
GL_RGB8UI_EXT = 0x8D7D
GL_ALPHA8UI_EXT = 0x8D7E
GL_INTENSITY8UI_EXT = 0x8D7F
GL_LUMINANCE8UI_EXT = 0x8D80
GL_LUMINANCE_ALPHA8UI_EXT = 0x8D81
GL_RGBA32I_EXT = 0x8D82
GL_RGB32I_EXT = 0x8D83
GL_ALPHA32I_EXT = 0x8D84
GL_INTENSITY32I_EXT = 0x8D85
GL_LUMINANCE32I_EXT = 0x8D86
GL_LUMINANCE_ALPHA32I_EXT = 0x8D87
GL_RGBA16I_EXT = 0x8D88
GL_RGB16I_EXT = 0x8D89
GL_ALPHA16I_EXT = 0x8D8A
GL_INTENSITY16I_EXT = 0x8D8B
GL_LUMINANCE16I_EXT = 0x8D8C
GL_LUMINANCE_ALPHA16I_EXT = 0x8D8D
GL_RGBA8I_EXT = 0x8D8E
GL_RGB8I_EXT = 0x8D8F
GL_ALPHA8I_EXT = 0x8D90
GL_INTENSITY8I_EXT = 0x8D91
GL_LUMINANCE8I_EXT = 0x8D92
GL_LUMINANCE_ALPHA8I_EXT = 0x8D93
GL_RED_INTEGER_EXT = 0x8D94
GL_GREEN_INTEGER_EXT = 0x8D95
GL_BLUE_INTEGER_EXT = 0x8D96
GL_ALPHA_INTEGER_EXT = 0x8D97
GL_RGB_INTEGER_EXT = 0x8D98
GL_RGBA_INTEGER_EXT = 0x8D99
GL_BGR_INTEGER_EXT = 0x8D9A
GL_BGRA_INTEGER_EXT = 0x8D9B
GL_LUMINANCE_INTEGER_EXT = 0x8D9C
GL_LUMINANCE_ALPHA_INTEGER_EXT = 0x8D9D
GL_RGBA_INTEGER_MODE_EXT = 0x8D9E
# EXT_texture_lod_bias
GL_MAX_TEXTURE_LOD_BIAS_EXT = 0x84FD
GL_TEXTURE_FILTER_CONTROL_EXT = 0x8500
GL_TEXTURE_LOD_BIAS_EXT = 0x8501
# EXT_texture_mirror_clamp
GL_MIRROR_CLAMP_EXT = 0x8742
GL_MIRROR_CLAMP_TO_EDGE_EXT = 0x8743
GL_MIRROR_CLAMP_TO_BORDER_EXT = 0x8912
# EXT_texture_object
GL_TEXTURE_PRIORITY_EXT = 0x8066
GL_TEXTURE_RESIDENT_EXT = 0x8067
GL_TEXTURE_1D_BINDING_EXT = 0x8068
GL_TEXTURE_2D_BINDING_EXT = 0x8069
GL_TEXTURE_3D_BINDING_EXT = 0x806A
# EXT_texture_perturb_normal
GL_PERTURB_EXT = 0x85AE
GL_TEXTURE_NORMAL_EXT = 0x85AF
# EXT_texture_rectangle
GL_TEXTURE_RECTANGLE_EXT = 0x84F5
GL_TEXTURE_BINDING_RECTANGLE_EXT = 0x84F6
GL_PROXY_TEXTURE_RECTANGLE_EXT = 0x84F7
GL_MAX_RECTANGLE_TEXTURE_SIZE_EXT = 0x84F8
# EXT_texture_sRGB
GL_SRGB_EXT = 0x8C40
GL_SRGB8_EXT = 0x8C41
GL_SRGB_ALPHA_EXT = 0x8C42
GL_SRGB8_ALPHA8_EXT = 0x8C43
GL_SLUMINANCE_ALPHA_EXT = 0x8C44
GL_SLUMINANCE8_ALPHA8_EXT = 0x8C45
GL_SLUMINANCE_EXT = 0x8C46
GL_SLUMINANCE8_EXT = 0x8C47
GL_COMPRESSED_SRGB_EXT = 0x8C48
GL_COMPRESSED_SRGB_ALPHA_EXT = 0x8C49
GL_COMPRESSED_SLUMINANCE_EXT = 0x8C4A
GL_COMPRESSED_SLUMINANCE_ALPHA_EXT = 0x8C4B
GL_COMPRESSED_SRGB_S3TC_DXT1_EXT = 0x8C4C
GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT = 0x8C4D
GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT = 0x8C4E
GL_COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT = 0x8C4F
# EXT_texture_sRGB_decode
GL_TEXTURE_SRGB_DECODE_EXT = 0x8A48
GL_DECODE_EXT = 0x8A49
GL_SKIP_DECODE_EXT = 0x8A4A
# EXT_texture_shared_exponent
GL_RGB9_E5_EXT = 0x8C3D
GL_UNSIGNED_INT_5_9_9_9_REV_EXT = 0x8C3E
GL_TEXTURE_SHARED_SIZE_EXT = 0x8C3F
# EXT_texture_snorm
GL_ALPHA_SNORM = 0x9010
GL_LUMINANCE_SNORM = 0x9011
GL_LUMINANCE_ALPHA_SNORM = 0x9012
GL_INTENSITY_SNORM = 0x9013
GL_ALPHA8_SNORM = 0x9014
GL_LUMINANCE8_SNORM = 0x9015
GL_LUMINANCE8_ALPHA8_SNORM = 0x9016
GL_INTENSITY8_SNORM = 0x9017
GL_ALPHA16_SNORM = 0x9018
GL_LUMINANCE16_SNORM = 0x9019
GL_LUMINANCE16_ALPHA16_SNORM = 0x901A
GL_INTENSITY16_SNORM = 0x901B
# EXT_texture_swizzle
GL_TEXTURE_SWIZZLE_R_EXT = 0x8E42
GL_TEXTURE_SWIZZLE_G_EXT = 0x8E43
GL_TEXTURE_SWIZZLE_B_EXT = 0x8E44
GL_TEXTURE_SWIZZLE_A_EXT = 0x8E45
GL_TEXTURE_SWIZZLE_RGBA_EXT = 0x8E46
# EXT_timer_query
GL_TIME_ELAPSED_EXT = 0x88BF
# EXT_transform_feedback
GL_TRANSFORM_FEEDBACK_BUFFER_EXT = 0x8C8E
GL_TRANSFORM_FEEDBACK_BUFFER_START_EXT = 0x8C84
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE_EXT = 0x8C85
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING_EXT = 0x8C8F
GL_INTERLEAVED_ATTRIBS_EXT = 0x8C8C
GL_SEPARATE_ATTRIBS_EXT = 0x8C8D
GL_PRIMITIVES_GENERATED_EXT = 0x8C87
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN_EXT = 0x8C88
GL_RASTERIZER_DISCARD_EXT = 0x8C89
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS_EXT = 0x8C8A
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS_EXT = 0x8C8B
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS_EXT = 0x8C80
GL_TRANSFORM_FEEDBACK_VARYINGS_EXT = 0x8C83
GL_TRANSFORM_FEEDBACK_BUFFER_MODE_EXT = 0x8C7F
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH_EXT = 0x8C76
# EXT_vertex_array
GL_VERTEX_ARRAY_EXT = 0x8074
GL_NORMAL_ARRAY_EXT = 0x8075
GL_COLOR_ARRAY_EXT = 0x8076
GL_INDEX_ARRAY_EXT = 0x8077
GL_TEXTURE_COORD_ARRAY_EXT = 0x8078
GL_EDGE_FLAG_ARRAY_EXT = 0x8079
GL_VERTEX_ARRAY_SIZE_EXT = 0x807A
GL_VERTEX_ARRAY_TYPE_EXT = 0x807B
GL_VERTEX_ARRAY_STRIDE_EXT = 0x807C
GL_VERTEX_ARRAY_COUNT_EXT = 0x807D
GL_NORMAL_ARRAY_TYPE_EXT = 0x807E
GL_NORMAL_ARRAY_STRIDE_EXT = 0x807F
GL_NORMAL_ARRAY_COUNT_EXT = 0x8080
GL_COLOR_ARRAY_SIZE_EXT = 0x8081
GL_COLOR_ARRAY_TYPE_EXT = 0x8082
GL_COLOR_ARRAY_STRIDE_EXT = 0x8083
GL_COLOR_ARRAY_COUNT_EXT = 0x8084
GL_INDEX_ARRAY_TYPE_EXT = 0x8085
GL_INDEX_ARRAY_STRIDE_EXT = 0x8086
GL_INDEX_ARRAY_COUNT_EXT = 0x8087
GL_TEXTURE_COORD_ARRAY_SIZE_EXT = 0x8088
GL_TEXTURE_COORD_ARRAY_TYPE_EXT = 0x8089
GL_TEXTURE_COORD_ARRAY_STRIDE_EXT = 0x808A
GL_TEXTURE_COORD_ARRAY_COUNT_EXT = 0x808B
GL_EDGE_FLAG_ARRAY_STRIDE_EXT = 0x808C
GL_EDGE_FLAG_ARRAY_COUNT_EXT = 0x808D
GL_VERTEX_ARRAY_POINTER_EXT = 0x808E
GL_NORMAL_ARRAY_POINTER_EXT = 0x808F
GL_COLOR_ARRAY_POINTER_EXT = 0x8090
GL_INDEX_ARRAY_POINTER_EXT = 0x8091
GL_TEXTURE_COORD_ARRAY_POINTER_EXT = 0x8092
GL_EDGE_FLAG_ARRAY_POINTER_EXT = 0x8093
# EXT_vertex_array_bgra
# EXT_vertex_attrib_64bit
GL_DOUBLE_VEC2_EXT = 0x8FFC
GL_DOUBLE_VEC3_EXT = 0x8FFD
GL_DOUBLE_VEC4_EXT = 0x8FFE
GL_DOUBLE_MAT2_EXT = 0x8F46
GL_DOUBLE_MAT3_EXT = 0x8F47
GL_DOUBLE_MAT4_EXT = 0x8F48
GL_DOUBLE_MAT2x3_EXT = 0x8F49
GL_DOUBLE_MAT2x4_EXT = 0x8F4A
GL_DOUBLE_MAT3x2_EXT = 0x8F4B
GL_DOUBLE_MAT3x4_EXT = 0x8F4C
GL_DOUBLE_MAT4x2_EXT = 0x8F4D
GL_DOUBLE_MAT4x3_EXT = 0x8F4E
# EXT_vertex_shader
GL_VERTEX_SHADER_EXT = 0x8780
GL_VERTEX_SHADER_BINDING_EXT = 0x8781
GL_OP_INDEX_EXT = 0x8782
GL_OP_NEGATE_EXT = 0x8783
GL_OP_DOT3_EXT = 0x8784
GL_OP_DOT4_EXT = 0x8785
GL_OP_MUL_EXT = 0x8786
GL_OP_ADD_EXT = 0x8787
GL_OP_MADD_EXT = 0x8788
GL_OP_FRAC_EXT = 0x8789
GL_OP_MAX_EXT = 0x878A
GL_OP_MIN_EXT = 0x878B
GL_OP_SET_GE_EXT = 0x878C
GL_OP_SET_LT_EXT = 0x878D
GL_OP_CLAMP_EXT = 0x878E
GL_OP_FLOOR_EXT = 0x878F
GL_OP_ROUND_EXT = 0x8790
GL_OP_EXP_BASE_2_EXT = 0x8791
GL_OP_LOG_BASE_2_EXT = 0x8792
GL_OP_POWER_EXT = 0x8793
GL_OP_RECIP_EXT = 0x8794
GL_OP_RECIP_SQRT_EXT = 0x8795
GL_OP_SUB_EXT = 0x8796
GL_OP_CROSS_PRODUCT_EXT = 0x8797
GL_OP_MULTIPLY_MATRIX_EXT = 0x8798
GL_OP_MOV_EXT = 0x8799
GL_OUTPUT_VERTEX_EXT = 0x879A
GL_OUTPUT_COLOR0_EXT = 0x879B
GL_OUTPUT_COLOR1_EXT = 0x879C
GL_OUTPUT_TEXTURE_COORD0_EXT = 0x879D
GL_OUTPUT_TEXTURE_COORD1_EXT = 0x879E
GL_OUTPUT_TEXTURE_COORD2_EXT = 0x879F
GL_OUTPUT_TEXTURE_COORD3_EXT = 0x87A0
GL_OUTPUT_TEXTURE_COORD4_EXT = 0x87A1
GL_OUTPUT_TEXTURE_COORD5_EXT = 0x87A2
GL_OUTPUT_TEXTURE_COORD6_EXT = 0x87A3
GL_OUTPUT_TEXTURE_COORD7_EXT = 0x87A4
GL_OUTPUT_TEXTURE_COORD8_EXT = 0x87A5
GL_OUTPUT_TEXTURE_COORD9_EXT = 0x87A6
GL_OUTPUT_TEXTURE_COORD10_EXT = 0x87A7
GL_OUTPUT_TEXTURE_COORD11_EXT = 0x87A8
GL_OUTPUT_TEXTURE_COORD12_EXT = 0x87A9
GL_OUTPUT_TEXTURE_COORD13_EXT = 0x87AA
GL_OUTPUT_TEXTURE_COORD14_EXT = 0x87AB
GL_OUTPUT_TEXTURE_COORD15_EXT = 0x87AC
GL_OUTPUT_TEXTURE_COORD16_EXT = 0x87AD
GL_OUTPUT_TEXTURE_COORD17_EXT = 0x87AE
GL_OUTPUT_TEXTURE_COORD18_EXT = 0x87AF
GL_OUTPUT_TEXTURE_COORD19_EXT = 0x87B0
GL_OUTPUT_TEXTURE_COORD20_EXT = 0x87B1
GL_OUTPUT_TEXTURE_COORD21_EXT = 0x87B2
GL_OUTPUT_TEXTURE_COORD22_EXT = 0x87B3
GL_OUTPUT_TEXTURE_COORD23_EXT = 0x87B4
GL_OUTPUT_TEXTURE_COORD24_EXT = 0x87B5
GL_OUTPUT_TEXTURE_COORD25_EXT = 0x87B6
GL_OUTPUT_TEXTURE_COORD26_EXT = 0x87B7
GL_OUTPUT_TEXTURE_COORD27_EXT = 0x87B8
GL_OUTPUT_TEXTURE_COORD28_EXT = 0x87B9
GL_OUTPUT_TEXTURE_COORD29_EXT = 0x87BA
GL_OUTPUT_TEXTURE_COORD30_EXT = 0x87BB
GL_OUTPUT_TEXTURE_COORD31_EXT = 0x87BC
GL_OUTPUT_FOG_EXT = 0x87BD
GL_SCALAR_EXT = 0x87BE
GL_VECTOR_EXT = 0x87BF
GL_MATRIX_EXT = 0x87C0
GL_VARIANT_EXT = 0x87C1
GL_INVARIANT_EXT = 0x87C2
GL_LOCAL_CONSTANT_EXT = 0x87C3
GL_LOCAL_EXT = 0x87C4
GL_MAX_VERTEX_SHADER_INSTRUCTIONS_EXT = 0x87C5
GL_MAX_VERTEX_SHADER_VARIANTS_EXT = 0x87C6
GL_MAX_VERTEX_SHADER_INVARIANTS_EXT = 0x87C7
GL_MAX_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 0x87C8
GL_MAX_VERTEX_SHADER_LOCALS_EXT = 0x87C9
GL_MAX_OPTIMIZED_VERTEX_SHADER_INSTRUCTIONS_EXT = 0x87CA
GL_MAX_OPTIMIZED_VERTEX_SHADER_VARIANTS_EXT = 0x87CB
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 0x87CC
GL_MAX_OPTIMIZED_VERTEX_SHADER_INVARIANTS_EXT = 0x87CD
GL_MAX_OPTIMIZED_VERTEX_SHADER_LOCALS_EXT = 0x87CE
GL_VERTEX_SHADER_INSTRUCTIONS_EXT = 0x87CF
GL_VERTEX_SHADER_VARIANTS_EXT = 0x87D0
GL_VERTEX_SHADER_INVARIANTS_EXT = 0x87D1
GL_VERTEX_SHADER_LOCAL_CONSTANTS_EXT = 0x87D2
GL_VERTEX_SHADER_LOCALS_EXT = 0x87D3
GL_VERTEX_SHADER_OPTIMIZED_EXT = 0x87D4
GL_X_EXT = 0x87D5
GL_Y_EXT = 0x87D6
GL_Z_EXT = 0x87D7
GL_W_EXT = 0x87D8
GL_NEGATIVE_X_EXT = 0x87D9
GL_NEGATIVE_Y_EXT = 0x87DA
GL_NEGATIVE_Z_EXT = 0x87DB
GL_NEGATIVE_W_EXT = 0x87DC
GL_ZERO_EXT = 0x87DD
GL_ONE_EXT = 0x87DE
GL_NEGATIVE_ONE_EXT = 0x87DF
GL_NORMALIZED_RANGE_EXT = 0x87E0
GL_FULL_RANGE_EXT = 0x87E1
GL_CURRENT_VERTEX_EXT = 0x87E2
GL_MVP_MATRIX_EXT = 0x87E3
GL_VARIANT_VALUE_EXT = 0x87E4
GL_VARIANT_DATATYPE_EXT = 0x87E5
GL_VARIANT_ARRAY_STRIDE_EXT = 0x87E6
GL_VARIANT_ARRAY_TYPE_EXT = 0x87E7
GL_VARIANT_ARRAY_EXT = 0x87E8
GL_VARIANT_ARRAY_POINTER_EXT = 0x87E9
GL_INVARIANT_VALUE_EXT = 0x87EA
GL_INVARIANT_DATATYPE_EXT = 0x87EB
GL_LOCAL_CONSTANT_VALUE_EXT = 0x87EC
GL_LOCAL_CONSTANT_DATATYPE_EXT = 0x87ED
# EXT_vertex_weighting
GL_MODELVIEW0_STACK_DEPTH_EXT = 0x0BA3 # GL_MODELVIEW_STACK_DEPTH
GL_MODELVIEW1_STACK_DEPTH_EXT = 0x8502
GL_MODELVIEW0_MATRIX_EXT = 0x0BA6 # GL_MODELVIEW_MATRIX
GL_MODELVIEW1_MATRIX_EXT = 0x8506
GL_VERTEX_WEIGHTING_EXT = 0x8509
GL_MODELVIEW0_EXT = 0x1700 # GL_MODELVIEW
GL_MODELVIEW1_EXT = 0x850A
GL_CURRENT_VERTEX_WEIGHT_EXT = 0x850B
GL_VERTEX_WEIGHT_ARRAY_EXT = 0x850C
GL_VERTEX_WEIGHT_ARRAY_SIZE_EXT = 0x850D
GL_VERTEX_WEIGHT_ARRAY_TYPE_EXT = 0x850E
GL_VERTEX_WEIGHT_ARRAY_STRIDE_EXT = 0x850F
GL_VERTEX_WEIGHT_ARRAY_POINTER_EXT = 0x8510
# EXT_x11_sync_object
GL_SYNC_X11_FENCE_EXT = 0x90E1
# FfdMaskSGIX
GL_TEXTURE_DEFORMATION_BIT_SGIX = 0x00000001
GL_GEOMETRY_DEFORMATION_BIT_SGIX = 0x00000002
# GREMEDY_frame_terminator
# GREMEDY_string_marker
# HP_convolution_border_modes
GL_IGNORE_BORDER_HP = 0x8150
GL_CONSTANT_BORDER_HP = 0x8151
GL_REPLICATE_BORDER_HP = 0x8153
GL_CONVOLUTION_BORDER_COLOR_HP = 0x8154
# HP_image_transform
GL_IMAGE_SCALE_X_HP = 0x8155
GL_IMAGE_SCALE_Y_HP = 0x8156
GL_IMAGE_TRANSLATE_X_HP = 0x8157
GL_IMAGE_TRANSLATE_Y_HP = 0x8158
GL_IMAGE_ROTATE_ANGLE_HP = 0x8159
GL_IMAGE_ROTATE_ORIGIN_X_HP = 0x815A
GL_IMAGE_ROTATE_ORIGIN_Y_HP = 0x815B
GL_IMAGE_MAG_FILTER_HP = 0x815C
GL_IMAGE_MIN_FILTER_HP = 0x815D
GL_IMAGE_CUBIC_WEIGHT_HP = 0x815E
GL_CUBIC_HP = 0x815F
GL_AVERAGE_HP = 0x8160
GL_IMAGE_TRANSFORM_2D_HP = 0x8161
GL_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP = 0x8162
GL_PROXY_POST_IMAGE_TRANSFORM_COLOR_TABLE_HP = 0x8163
# HP_occlusion_test
GL_OCCLUSION_TEST_HP = 0x8165
GL_OCCLUSION_TEST_RESULT_HP = 0x8166
# HP_texture_lighting
GL_TEXTURE_LIGHTING_MODE_HP = 0x8167
GL_TEXTURE_POST_SPECULAR_HP = 0x8168
GL_TEXTURE_PRE_SPECULAR_HP = 0x8169
# IBM_cull_vertex
GL_CULL_VERTEX_IBM = 103050
# IBM_multimode_draw_arrays
# IBM_rasterpos_clip
GL_RASTER_POSITION_UNCLIPPED_IBM = 0x19262
# IBM_texture_mirrored_repeat
GL_MIRRORED_REPEAT_IBM = 0x8370
# IBM_vertex_array_lists
GL_VERTEX_ARRAY_LIST_IBM = 103070
GL_NORMAL_ARRAY_LIST_IBM = 103071
GL_COLOR_ARRAY_LIST_IBM = 103072
GL_INDEX_ARRAY_LIST_IBM = 103073
GL_TEXTURE_COORD_ARRAY_LIST_IBM = 103074
GL_EDGE_FLAG_ARRAY_LIST_IBM = 103075
GL_FOG_COORDINATE_ARRAY_LIST_IBM = 103076
GL_SECONDARY_COLOR_ARRAY_LIST_IBM = 103077
GL_VERTEX_ARRAY_LIST_STRIDE_IBM = 103080
GL_NORMAL_ARRAY_LIST_STRIDE_IBM = 103081
GL_COLOR_ARRAY_LIST_STRIDE_IBM = 103082
GL_INDEX_ARRAY_LIST_STRIDE_IBM = 103083
GL_TEXTURE_COORD_ARRAY_LIST_STRIDE_IBM = 103084
GL_EDGE_FLAG_ARRAY_LIST_STRIDE_IBM = 103085
GL_FOG_COORDINATE_ARRAY_LIST_STRIDE_IBM = 103086
GL_SECONDARY_COLOR_ARRAY_LIST_STRIDE_IBM = 103087
# INGR_color_clamp
GL_RED_MIN_CLAMP_INGR = 0x8560
GL_GREEN_MIN_CLAMP_INGR = 0x8561
GL_BLUE_MIN_CLAMP_INGR = 0x8562
GL_ALPHA_MIN_CLAMP_INGR = 0x8563
GL_RED_MAX_CLAMP_INGR = 0x8564
GL_GREEN_MAX_CLAMP_INGR = 0x8565
GL_BLUE_MAX_CLAMP_INGR = 0x8566
GL_ALPHA_MAX_CLAMP_INGR = 0x8567
# INGR_interlace_read
GL_INTERLACE_READ_INGR = 0x8568
# INGR_palette_buffer
# INTEL_parallel_arrays
GL_PARALLEL_ARRAYS_INTEL = 0x83F4
GL_VERTEX_ARRAY_PARALLEL_POINTERS_INTEL = 0x83F5
GL_NORMAL_ARRAY_PARALLEL_POINTERS_INTEL = 0x83F6
GL_COLOR_ARRAY_PARALLEL_POINTERS_INTEL = 0x83F7
GL_TEXTURE_COORD_ARRAY_PARALLEL_POINTERS_INTEL = 0x83F8
# INTEL_texture_scissor
# KHR_debug
GL_DEBUG_OUTPUT_SYNCHRONOUS = 0x8242
GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH = 0x8243
GL_DEBUG_CALLBACK_FUNCTION = 0x8244
GL_DEBUG_CALLBACK_USER_PARAM = 0x8245
GL_DEBUG_SOURCE_API = 0x8246
GL_DEBUG_SOURCE_WINDOW_SYSTEM = 0x8247
GL_DEBUG_SOURCE_SHADER_COMPILER = 0x8248
GL_DEBUG_SOURCE_THIRD_PARTY = 0x8249
GL_DEBUG_SOURCE_APPLICATION = 0x824A
GL_DEBUG_SOURCE_OTHER = 0x824B
GL_DEBUG_TYPE_ERROR = 0x824C
GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR = 0x824D
GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR = 0x824E
GL_DEBUG_TYPE_PORTABILITY = 0x824F
GL_DEBUG_TYPE_PERFORMANCE = 0x8250
GL_DEBUG_TYPE_OTHER = 0x8251
GL_DEBUG_TYPE_MARKER = 0x8268
GL_DEBUG_TYPE_PUSH_GROUP = 0x8269
GL_DEBUG_TYPE_POP_GROUP = 0x826A
GL_DEBUG_SEVERITY_NOTIFICATION = 0x826B
GL_MAX_DEBUG_GROUP_STACK_DEPTH = 0x826C
GL_DEBUG_GROUP_STACK_DEPTH = 0x826D
GL_BUFFER = 0x82E0
GL_SHADER = 0x82E1
GL_PROGRAM = 0x82E2
GL_QUERY = 0x82E3
GL_PROGRAM_PIPELINE = 0x82E4
GL_SAMPLER = 0x82E6
GL_DISPLAY_LIST = 0x82E7
GL_MAX_LABEL_LENGTH = 0x82E8
GL_MAX_DEBUG_MESSAGE_LENGTH = 0x9143
GL_MAX_DEBUG_LOGGED_MESSAGES = 0x9144
GL_DEBUG_LOGGED_MESSAGES = 0x9145
GL_DEBUG_SEVERITY_HIGH = 0x9146
GL_DEBUG_SEVERITY_MEDIUM = 0x9147
GL_DEBUG_SEVERITY_LOW = 0x9148
GL_DEBUG_OUTPUT = 0x92E0
GL_CONTEXT_FLAG_DEBUG_BIT = 0x00000002
# KHR_texture_compression_astc_ldr
GL_COMPRESSED_RGBA_ASTC_4x4_KHR = 0x93B0
GL_COMPRESSED_RGBA_ASTC_5x4_KHR = 0x93B1
GL_COMPRESSED_RGBA_ASTC_5x5_KHR = 0x93B2
GL_COMPRESSED_RGBA_ASTC_6x5_KHR = 0x93B3
GL_COMPRESSED_RGBA_ASTC_6x6_KHR = 0x93B4
GL_COMPRESSED_RGBA_ASTC_8x5_KHR = 0x93B5
GL_COMPRESSED_RGBA_ASTC_8x6_KHR = 0x93B6
GL_COMPRESSED_RGBA_ASTC_8x8_KHR = 0x93B7
GL_COMPRESSED_RGBA_ASTC_10x5_KHR = 0x93B8
GL_COMPRESSED_RGBA_ASTC_10x6_KHR = 0x93B9
GL_COMPRESSED_RGBA_ASTC_10x8_KHR = 0x93BA
GL_COMPRESSED_RGBA_ASTC_10x10_KHR = 0x93BB
GL_COMPRESSED_RGBA_ASTC_12x10_KHR = 0x93BC
GL_COMPRESSED_RGBA_ASTC_12x12_KHR = 0x93BD
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR = 0x93D0
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR = 0x93D1
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR = 0x93D2
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR = 0x93D3
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR = 0x93D4
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR = 0x93D5
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR = 0x93D6
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR = 0x93D7
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR = 0x93D8
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR = 0x93D9
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR = 0x93DA
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR = 0x93DB
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR = 0x93DC
GL_COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR = 0x93DD
# MESAX_texture_stack
GL_TEXTURE_1D_STACK_MESAX = 0x8759
GL_TEXTURE_2D_STACK_MESAX = 0x875A
GL_PROXY_TEXTURE_1D_STACK_MESAX = 0x875B
GL_PROXY_TEXTURE_2D_STACK_MESAX = 0x875C
GL_TEXTURE_1D_STACK_BINDING_MESAX = 0x875D
GL_TEXTURE_2D_STACK_BINDING_MESAX = 0x875E
# MESA_pack_invert
GL_PACK_INVERT_MESA = 0x8758
# MESA_resize_buffers
# MESA_window_pos
# MESA_ycbcr_texture
GL_UNSIGNED_SHORT_8_8_MESA = 0x85BA
GL_UNSIGNED_SHORT_8_8_REV_MESA = 0x85BB
GL_YCBCR_MESA = 0x8757
# NV_bindless_texture
# NV_blend_square
# NV_conditional_render
GL_QUERY_WAIT_NV = 0x8E13
GL_QUERY_NO_WAIT_NV = 0x8E14
GL_QUERY_BY_REGION_WAIT_NV = 0x8E15
GL_QUERY_BY_REGION_NO_WAIT_NV = 0x8E16
# NV_copy_depth_to_color
GL_DEPTH_STENCIL_TO_RGBA_NV = 0x886E
GL_DEPTH_STENCIL_TO_BGRA_NV = 0x886F
# NV_copy_image
# NV_depth_buffer_float
GL_DEPTH_COMPONENT32F_NV = 0x8DAB
GL_DEPTH32F_STENCIL8_NV = 0x8DAC
GL_FLOAT_32_UNSIGNED_INT_24_8_REV_NV = 0x8DAD
GL_DEPTH_BUFFER_FLOAT_MODE_NV = 0x8DAF
# NV_depth_clamp
GL_DEPTH_CLAMP_NV = 0x864F
# NV_evaluators
GL_EVAL_2D_NV = 0x86C0
GL_EVAL_TRIANGULAR_2D_NV = 0x86C1
GL_MAP_TESSELLATION_NV = 0x86C2
GL_MAP_ATTRIB_U_ORDER_NV = 0x86C3
GL_MAP_ATTRIB_V_ORDER_NV = 0x86C4
GL_EVAL_FRACTIONAL_TESSELLATION_NV = 0x86C5
GL_EVAL_VERTEX_ATTRIB0_NV = 0x86C6
GL_EVAL_VERTEX_ATTRIB1_NV = 0x86C7
GL_EVAL_VERTEX_ATTRIB2_NV = 0x86C8
GL_EVAL_VERTEX_ATTRIB3_NV = 0x86C9
GL_EVAL_VERTEX_ATTRIB4_NV = 0x86CA
GL_EVAL_VERTEX_ATTRIB5_NV = 0x86CB
GL_EVAL_VERTEX_ATTRIB6_NV = 0x86CC
GL_EVAL_VERTEX_ATTRIB7_NV = 0x86CD
GL_EVAL_VERTEX_ATTRIB8_NV = 0x86CE
GL_EVAL_VERTEX_ATTRIB9_NV = 0x86CF
GL_EVAL_VERTEX_ATTRIB10_NV = 0x86D0
GL_EVAL_VERTEX_ATTRIB11_NV = 0x86D1
GL_EVAL_VERTEX_ATTRIB12_NV = 0x86D2
GL_EVAL_VERTEX_ATTRIB13_NV = 0x86D3
GL_EVAL_VERTEX_ATTRIB14_NV = 0x86D4
GL_EVAL_VERTEX_ATTRIB15_NV = 0x86D5
GL_MAX_MAP_TESSELLATION_NV = 0x86D6
GL_MAX_RATIONAL_EVAL_ORDER_NV = 0x86D7
# NV_explicit_multisample
GL_SAMPLE_POSITION_NV = 0x8E50
GL_SAMPLE_MASK_NV = 0x8E51
GL_SAMPLE_MASK_VALUE_NV = 0x8E52
GL_TEXTURE_BINDING_RENDERBUFFER_NV = 0x8E53
GL_TEXTURE_RENDERBUFFER_DATA_STORE_BINDING_NV = 0x8E54
GL_TEXTURE_RENDERBUFFER_NV = 0x8E55
GL_SAMPLER_RENDERBUFFER_NV = 0x8E56
GL_INT_SAMPLER_RENDERBUFFER_NV = 0x8E57
GL_UNSIGNED_INT_SAMPLER_RENDERBUFFER_NV = 0x8E58
GL_MAX_SAMPLE_MASK_WORDS_NV = 0x8E59
# NV_fence
GL_ALL_COMPLETED_NV = 0x84F2
GL_FENCE_STATUS_NV = 0x84F3
GL_FENCE_CONDITION_NV = 0x84F4
# NV_float_buffer
GL_FLOAT_R_NV = 0x8880
GL_FLOAT_RG_NV = 0x8881
GL_FLOAT_RGB_NV = 0x8882
GL_FLOAT_RGBA_NV = 0x8883
GL_FLOAT_R16_NV = 0x8884
GL_FLOAT_R32_NV = 0x8885
GL_FLOAT_RG16_NV = 0x8886
GL_FLOAT_RG32_NV = 0x8887
GL_FLOAT_RGB16_NV = 0x8888
GL_FLOAT_RGB32_NV = 0x8889
GL_FLOAT_RGBA16_NV = 0x888A
GL_FLOAT_RGBA32_NV = 0x888B
GL_TEXTURE_FLOAT_COMPONENTS_NV = 0x888C
GL_FLOAT_CLEAR_COLOR_VALUE_NV = 0x888D
GL_FLOAT_RGBA_MODE_NV = 0x888E
WGL_FLOAT_COMPONENTS_NV = 0x20B0
WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_R_NV = 0x20B1
WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RG_NV = 0x20B2
WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGB_NV = 0x20B3
WGL_BIND_TO_TEXTURE_RECTANGLE_FLOAT_RGBA_NV = 0x20B4
WGL_TEXTURE_FLOAT_R_NV = 0x20B5
WGL_TEXTURE_FLOAT_RG_NV = 0x20B6
WGL_TEXTURE_FLOAT_RGB_NV = 0x20B7
WGL_TEXTURE_FLOAT_RGBA_NV = 0x20B8
# NV_fog_distance
GL_FOG_DISTANCE_MODE_NV = 0x855A
GL_EYE_RADIAL_NV = 0x855B
GL_EYE_PLANE_ABSOLUTE_NV = 0x855C
# NV_fragment_program
GL_MAX_FRAGMENT_PROGRAM_LOCAL_PARAMETERS_NV = 0x8868
GL_FRAGMENT_PROGRAM_NV = 0x8870
GL_MAX_TEXTURE_COORDS_NV = 0x8871
GL_MAX_TEXTURE_IMAGE_UNITS_NV = 0x8872
GL_FRAGMENT_PROGRAM_BINDING_NV = 0x8873
GL_PROGRAM_ERROR_STRING_NV = 0x8874
# NV_fragment_program2
GL_MAX_PROGRAM_EXEC_INSTRUCTIONS_NV = 0x88F4
GL_MAX_PROGRAM_CALL_DEPTH_NV = 0x88F5
GL_MAX_PROGRAM_IF_DEPTH_NV = 0x88F6
GL_MAX_PROGRAM_LOOP_DEPTH_NV = 0x88F7
GL_MAX_PROGRAM_LOOP_COUNT_NV = 0x88F8
# NV_fragment_program4
# NV_fragment_program_option
# NV_framebuffer_multisample_coverage
GL_RENDERBUFFER_COVERAGE_SAMPLES_NV = 0x8CAB
GL_RENDERBUFFER_COLOR_SAMPLES_NV = 0x8E10
GL_MAX_MULTISAMPLE_COVERAGE_MODES_NV = 0x8E11
GL_MULTISAMPLE_COVERAGE_MODES_NV = 0x8E12
# NV_geometry_program4
GL_LINES_ADJACENCY_EXT = 0x000A
GL_LINE_STRIP_ADJACENCY_EXT = 0x000B
GL_TRIANGLES_ADJACENCY_EXT = 0x000C
GL_TRIANGLE_STRIP_ADJACENCY_EXT = 0x000D
GL_GEOMETRY_PROGRAM_NV = 0x8C26
GL_MAX_PROGRAM_OUTPUT_VERTICES_NV = 0x8C27
GL_MAX_PROGRAM_TOTAL_OUTPUT_COMPONENTS_NV = 0x8C28
GL_GEOMETRY_VERTICES_OUT_EXT = 0x8DDA
GL_GEOMETRY_INPUT_TYPE_EXT = 0x8DDB
GL_GEOMETRY_OUTPUT_TYPE_EXT = 0x8DDC
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS_EXT = 0x8C29
GL_FRAMEBUFFER_ATTACHMENT_LAYERED_EXT = 0x8DA7
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS_EXT = 0x8DA8
GL_FRAMEBUFFER_INCOMPLETE_LAYER_COUNT_EXT = 0x8DA9
GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER_EXT = 0x8CD4
GL_PROGRAM_POINT_SIZE_EXT = 0x8642
# NV_geometry_shader4
# NV_gpu_program4
GL_MIN_PROGRAM_TEXEL_OFFSET_NV = 0x8904
GL_MAX_PROGRAM_TEXEL_OFFSET_NV = 0x8905
GL_PROGRAM_ATTRIB_COMPONENTS_NV = 0x8906
GL_PROGRAM_RESULT_COMPONENTS_NV = 0x8907
GL_MAX_PROGRAM_ATTRIB_COMPONENTS_NV = 0x8908
GL_MAX_PROGRAM_RESULT_COMPONENTS_NV = 0x8909
GL_MAX_PROGRAM_GENERIC_ATTRIBS_NV = 0x8DA5
GL_MAX_PROGRAM_GENERIC_RESULTS_NV = 0x8DA6
# NV_gpu_program5
GL_MAX_GEOMETRY_PROGRAM_INVOCATIONS_NV = 0x8E5A
GL_MIN_FRAGMENT_INTERPOLATION_OFFSET_NV = 0x8E5B
GL_MAX_FRAGMENT_INTERPOLATION_OFFSET_NV = 0x8E5C
GL_FRAGMENT_PROGRAM_INTERPOLATION_OFFSET_BITS_NV = 0x8E5D
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET_NV = 0x8E5E
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET_NV = 0x8E5F
GL_MAX_PROGRAM_SUBROUTINE_PARAMETERS_NV = 0x8F44
GL_MAX_PROGRAM_SUBROUTINE_NUM_NV = 0x8F45
# NV_gpu_shader5
GL_INT64_NV = 0x140E
GL_UNSIGNED_INT64_NV = 0x140F
GL_INT8_NV = 0x8FE0
GL_INT8_VEC2_NV = 0x8FE1
GL_INT8_VEC3_NV = 0x8FE2
GL_INT8_VEC4_NV = 0x8FE3
GL_INT16_NV = 0x8FE4
GL_INT16_VEC2_NV = 0x8FE5
GL_INT16_VEC3_NV = 0x8FE6
GL_INT16_VEC4_NV = 0x8FE7
GL_INT64_VEC2_NV = 0x8FE9
GL_INT64_VEC3_NV = 0x8FEA
GL_INT64_VEC4_NV = 0x8FEB
GL_UNSIGNED_INT8_NV = 0x8FEC
GL_UNSIGNED_INT8_VEC2_NV = 0x8FED
GL_UNSIGNED_INT8_VEC3_NV = 0x8FEE
GL_UNSIGNED_INT8_VEC4_NV = 0x8FEF
GL_UNSIGNED_INT16_NV = 0x8FF0
GL_UNSIGNED_INT16_VEC2_NV = 0x8FF1
GL_UNSIGNED_INT16_VEC3_NV = 0x8FF2
GL_UNSIGNED_INT16_VEC4_NV = 0x8FF3
GL_UNSIGNED_INT64_VEC2_NV = 0x8FF5
GL_UNSIGNED_INT64_VEC3_NV = 0x8FF6
GL_UNSIGNED_INT64_VEC4_NV = 0x8FF7
GL_FLOAT16_NV = 0x8FF8
GL_FLOAT16_VEC2_NV = 0x8FF9
GL_FLOAT16_VEC3_NV = 0x8FFA
GL_FLOAT16_VEC4_NV = 0x8FFB
# NV_half_float
GL_HALF_FLOAT_NV = 0x140B
# NV_light_max_exponent
GL_MAX_SHININESS_NV = 0x8504
GL_MAX_SPOT_EXPONENT_NV = 0x8505
# NV_multisample_coverage
GL_COVERAGE_SAMPLES_NV = 0x80A9
GL_COLOR_SAMPLES_NV = 0x8E20
WGL_COVERAGE_SAMPLES_NV = 0x2042
WGL_COLOR_SAMPLES_NV = 0x20B9
# NV_multisample_filter_hint
GL_MULTISAMPLE_FILTER_HINT_NV = 0x8534
# NV_occlusion_query
GL_PIXEL_COUNTER_BITS_NV = 0x8864
GL_CURRENT_OCCLUSION_QUERY_ID_NV = 0x8865
GL_PIXEL_COUNT_NV = 0x8866
GL_PIXEL_COUNT_AVAILABLE_NV = 0x8867
# NV_packed_depth_stencil
GL_DEPTH_STENCIL_NV = 0x84F9
GL_UNSIGNED_INT_24_8_NV = 0x84FA
# NV_parameter_buffer_object
GL_MAX_PROGRAM_PARAMETER_BUFFER_BINDINGS_NV = 0x8DA0
GL_MAX_PROGRAM_PARAMETER_BUFFER_SIZE_NV = 0x8DA1
GL_VERTEX_PROGRAM_PARAMETER_BUFFER_NV = 0x8DA2
GL_GEOMETRY_PROGRAM_PARAMETER_BUFFER_NV = 0x8DA3
GL_FRAGMENT_PROGRAM_PARAMETER_BUFFER_NV = 0x8DA4
# NV_parameter_buffer_object2
# NV_path_rendering
GL_PATH_FORMAT_SVG_NV = 0x9070
GL_PATH_FORMAT_PS_NV = 0x9071
GL_STANDARD_FONT_NAME_NV = 0x9072
GL_SYSTEM_FONT_NAME_NV = 0x9073
GL_FILE_NAME_NV = 0x9074
GL_PATH_STROKE_WIDTH_NV = 0x9075
GL_PATH_END_CAPS_NV = 0x9076
GL_PATH_INITIAL_END_CAP_NV = 0x9077
GL_PATH_TERMINAL_END_CAP_NV = 0x9078
GL_PATH_JOIN_STYLE_NV = 0x9079
GL_PATH_MITER_LIMIT_NV = 0x907A
GL_PATH_DASH_CAPS_NV = 0x907B
GL_PATH_INITIAL_DASH_CAP_NV = 0x907C
GL_PATH_TERMINAL_DASH_CAP_NV = 0x907D
GL_PATH_DASH_OFFSET_NV = 0x907E
GL_PATH_CLIENT_LENGTH_NV = 0x907F
GL_PATH_FILL_MODE_NV = 0x9080
GL_PATH_FILL_MASK_NV = 0x9081
GL_PATH_FILL_COVER_MODE_NV = 0x9082
GL_PATH_STROKE_COVER_MODE_NV = 0x9083
GL_PATH_STROKE_MASK_NV = 0x9084
GL_PATH_SAMPLE_QUALITY_NV = 0x9085
GL_PATH_STROKE_BOUND_NV = 0x9086
GL_PATH_STROKE_OVERSAMPLE_COUNT_NV = 0x9087
GL_COUNT_UP_NV = 0x9088
GL_COUNT_DOWN_NV = 0x9089
GL_PATH_OBJECT_BOUNDING_BOX_NV = 0x908A
GL_CONVEX_HULL_NV = 0x908B
GL_MULTI_HULLS_NV = 0x908C
GL_BOUNDING_BOX_NV = 0x908D
GL_TRANSLATE_X_NV = 0x908E
GL_TRANSLATE_Y_NV = 0x908F
GL_TRANSLATE_2D_NV = 0x9090
GL_TRANSLATE_3D_NV = 0x9091
GL_AFFINE_2D_NV = 0x9092
GL_PROJECTIVE_2D_NV = 0x9093
GL_AFFINE_3D_NV = 0x9094
GL_PROJECTIVE_3D_NV = 0x9095
GL_TRANSPOSE_AFFINE_2D_NV = 0x9096
GL_TRANSPOSE_PROJECTIVE_2D_NV = 0x9097
GL_TRANSPOSE_AFFINE_3D_NV = 0x9098
GL_TRANSPOSE_PROJECTIVE_3D_NV = 0x9099
GL_UTF8_NV = 0x909A
GL_UTF16_NV = 0x909B
GL_BOUNDING_BOX_OF_BOUNDING_BOXES_NV = 0x909C
GL_PATH_COMMAND_COUNT_NV = 0x909D
GL_PATH_COORD_COUNT_NV = 0x909E
GL_PATH_DASH_ARRAY_COUNT_NV = 0x909F
GL_PATH_COMPUTED_LENGTH_NV = 0x90A0
GL_PATH_FILL_BOUNDING_BOX_NV = 0x90A1
GL_PATH_STROKE_BOUNDING_BOX_NV = 0x90A2
GL_SQUARE_NV = 0x90A3
GL_ROUND_NV = 0x90A4
GL_TRIANGULAR_NV = 0x90A5
GL_BEVEL_NV = 0x90A6
GL_MITER_REVERT_NV = 0x90A7
GL_MITER_TRUNCATE_NV = 0x90A8
GL_SKIP_MISSING_GLYPH_NV = 0x90A9
GL_USE_MISSING_GLYPH_NV = 0x90AA
GL_PATH_ERROR_POSITION_NV = 0x90AB
GL_PATH_FOG_GEN_MODE_NV = 0x90AC
GL_ACCUM_ADJACENT_PAIRS_NV = 0x90AD
GL_ADJACENT_PAIRS_NV = 0x90AE
GL_FIRST_TO_REST_NV = 0x90AF
GL_PATH_GEN_MODE_NV = 0x90B0
GL_PATH_GEN_COEFF_NV = 0x90B1
GL_PATH_GEN_COLOR_FORMAT_NV = 0x90B2
GL_PATH_GEN_COMPONENTS_NV = 0x90B3
GL_PATH_STENCIL_FUNC_NV = 0x90B7
GL_PATH_STENCIL_REF_NV = 0x90B8
GL_PATH_STENCIL_VALUE_MASK_NV = 0x90B9
GL_PATH_STENCIL_DEPTH_OFFSET_FACTOR_NV = 0x90BD
GL_PATH_STENCIL_DEPTH_OFFSET_UNITS_NV = 0x90BE
GL_PATH_COVER_DEPTH_FUNC_NV = 0x90BF
GL_PATH_DASH_OFFSET_RESET_NV = 0x90B4
GL_MOVE_TO_RESETS_NV = 0x90B5
GL_MOVE_TO_CONTINUES_NV = 0x90B6
GL_CLOSE_PATH_NV = 0x00
GL_MOVE_TO_NV = 0x02
GL_RELATIVE_MOVE_TO_NV = 0x03
GL_LINE_TO_NV = 0x04
GL_RELATIVE_LINE_TO_NV = 0x05
GL_HORIZONTAL_LINE_TO_NV = 0x06
GL_RELATIVE_HORIZONTAL_LINE_TO_NV = 0x07
GL_VERTICAL_LINE_TO_NV = 0x08
GL_RELATIVE_VERTICAL_LINE_TO_NV = 0x09
GL_QUADRATIC_CURVE_TO_NV = 0x0A
GL_RELATIVE_QUADRATIC_CURVE_TO_NV = 0x0B
GL_CUBIC_CURVE_TO_NV = 0x0C
GL_RELATIVE_CUBIC_CURVE_TO_NV = 0x0D
GL_SMOOTH_QUADRATIC_CURVE_TO_NV = 0x0E
GL_RELATIVE_SMOOTH_QUADRATIC_CURVE_TO_NV = 0x0F
GL_SMOOTH_CUBIC_CURVE_TO_NV = 0x10
GL_RELATIVE_SMOOTH_CUBIC_CURVE_TO_NV = 0x11
GL_SMALL_CCW_ARC_TO_NV = 0x12
GL_RELATIVE_SMALL_CCW_ARC_TO_NV = 0x13
GL_SMALL_CW_ARC_TO_NV = 0x14
GL_RELATIVE_SMALL_CW_ARC_TO_NV = 0x15
GL_LARGE_CCW_ARC_TO_NV = 0x16
GL_RELATIVE_LARGE_CCW_ARC_TO_NV = 0x17
GL_LARGE_CW_ARC_TO_NV = 0x18
GL_RELATIVE_LARGE_CW_ARC_TO_NV = 0x19
GL_RESTART_PATH_NV = 0xF0
GL_DUP_FIRST_CUBIC_CURVE_TO_NV = 0xF2
GL_DUP_LAST_CUBIC_CURVE_TO_NV = 0xF4
GL_RECT_NV = 0xF6
GL_CIRCULAR_CCW_ARC_TO_NV = 0xF8
GL_CIRCULAR_CW_ARC_TO_NV = 0xFA
GL_CIRCULAR_TANGENT_ARC_TO_NV = 0xFC
GL_ARC_TO_NV = 0xFE
GL_RELATIVE_ARC_TO_NV = 0xFF
GL_BOLD_BIT_NV = 0x01
GL_ITALIC_BIT_NV = 0x02
GL_GLYPH_WIDTH_BIT_NV = 0x01
GL_GLYPH_HEIGHT_BIT_NV = 0x02
GL_GLYPH_HORIZONTAL_BEARING_X_BIT_NV = 0x04
GL_GLYPH_HORIZONTAL_BEARING_Y_BIT_NV = 0x08
GL_GLYPH_HORIZONTAL_BEARING_ADVANCE_BIT_NV = 0x10
GL_GLYPH_VERTICAL_BEARING_X_BIT_NV = 0x20
GL_GLYPH_VERTICAL_BEARING_Y_BIT_NV = 0x40
GL_GLYPH_VERTICAL_BEARING_ADVANCE_BIT_NV = 0x80
GL_GLYPH_HAS_KERNING_NV = 0x100
GL_FONT_X_MIN_BOUNDS_NV = 0x00010000
GL_FONT_Y_MIN_BOUNDS_NV = 0x00020000
GL_FONT_X_MAX_BOUNDS_NV = 0x00040000
GL_FONT_Y_MAX_BOUNDS_NV = 0x00080000
GL_FONT_UNITS_PER_EM_NV = 0x00100000
GL_FONT_ASCENDER_NV = 0x00200000
GL_FONT_DESCENDER_NV = 0x00400000
GL_FONT_HEIGHT_NV = 0x00800000
GL_FONT_MAX_ADVANCE_WIDTH_NV = 0x01000000
GL_FONT_MAX_ADVANCE_HEIGHT_NV = 0x02000000
GL_FONT_UNDERLINE_POSITION_NV = 0x04000000
GL_FONT_UNDERLINE_THICKNESS_NV = 0x08000000
GL_FONT_HAS_KERNING_NV = 0x10000000
# NV_pixel_data_range
GL_WRITE_PIXEL_DATA_RANGE_NV = 0x8878
GL_READ_PIXEL_DATA_RANGE_NV = 0x8879
GL_WRITE_PIXEL_DATA_RANGE_LENGTH_NV = 0x887A
GL_READ_PIXEL_DATA_RANGE_LENGTH_NV = 0x887B
GL_WRITE_PIXEL_DATA_RANGE_POINTER_NV = 0x887C
GL_READ_PIXEL_DATA_RANGE_POINTER_NV = 0x887D
# NV_point_sprite
GL_POINT_SPRITE_NV = 0x8861
GL_COORD_REPLACE_NV = 0x8862
GL_POINT_SPRITE_R_MODE_NV = 0x8863
# NV_present_video
GL_FRAME_NV = 0x8E26
GL_FIELDS_NV = 0x8E27
GL_CURRENT_TIME_NV = 0x8E28
GL_NUM_FILL_STREAMS_NV = 0x8E29
GL_PRESENT_TIME_NV = 0x8E2A
GL_PRESENT_DURATION_NV = 0x8E2B
WGL_NUM_VIDEO_SLOTS_NV = 0x20F0
# NV_primitive_restart
GL_PRIMITIVE_RESTART_NV = 0x8558
GL_PRIMITIVE_RESTART_INDEX_NV = 0x8559
# NV_register_combiners
GL_REGISTER_COMBINERS_NV = 0x8522
GL_VARIABLE_A_NV = 0x8523
GL_VARIABLE_B_NV = 0x8524
GL_VARIABLE_C_NV = 0x8525
GL_VARIABLE_D_NV = 0x8526
GL_VARIABLE_E_NV = 0x8527
GL_VARIABLE_F_NV = 0x8528
GL_VARIABLE_G_NV = 0x8529
GL_CONSTANT_COLOR0_NV = 0x852A
GL_CONSTANT_COLOR1_NV = 0x852B
GL_PRIMARY_COLOR_NV = 0x852C
GL_SECONDARY_COLOR_NV = 0x852D
GL_SPARE0_NV = 0x852E
GL_SPARE1_NV = 0x852F
GL_DISCARD_NV = 0x8530
GL_E_TIMES_F_NV = 0x8531
GL_SPARE0_PLUS_SECONDARY_COLOR_NV = 0x8532
GL_UNSIGNED_IDENTITY_NV = 0x8536
GL_UNSIGNED_INVERT_NV = 0x8537
GL_EXPAND_NORMAL_NV = 0x8538
GL_EXPAND_NEGATE_NV = 0x8539
GL_HALF_BIAS_NORMAL_NV = 0x853A
GL_HALF_BIAS_NEGATE_NV = 0x853B
GL_SIGNED_IDENTITY_NV = 0x853C
GL_SIGNED_NEGATE_NV = 0x853D
GL_SCALE_BY_TWO_NV = 0x853E
GL_SCALE_BY_FOUR_NV = 0x853F
GL_SCALE_BY_ONE_HALF_NV = 0x8540
GL_BIAS_BY_NEGATIVE_ONE_HALF_NV = 0x8541
GL_COMBINER_INPUT_NV = 0x8542
GL_COMBINER_MAPPING_NV = 0x8543
GL_COMBINER_COMPONENT_USAGE_NV = 0x8544
GL_COMBINER_AB_DOT_PRODUCT_NV = 0x8545
GL_COMBINER_CD_DOT_PRODUCT_NV = 0x8546
GL_COMBINER_MUX_SUM_NV = 0x8547
GL_COMBINER_SCALE_NV = 0x8548
GL_COMBINER_BIAS_NV = 0x8549
GL_COMBINER_AB_OUTPUT_NV = 0x854A
GL_COMBINER_CD_OUTPUT_NV = 0x854B
GL_COMBINER_SUM_OUTPUT_NV = 0x854C
GL_MAX_GENERAL_COMBINERS_NV = 0x854D
GL_NUM_GENERAL_COMBINERS_NV = 0x854E
GL_COLOR_SUM_CLAMP_NV = 0x854F
GL_COMBINER0_NV = 0x8550
GL_COMBINER1_NV = 0x8551
GL_COMBINER2_NV = 0x8552
GL_COMBINER3_NV = 0x8553
GL_COMBINER4_NV = 0x8554
GL_COMBINER5_NV = 0x8555
GL_COMBINER6_NV = 0x8556
GL_COMBINER7_NV = 0x8557
# NV_register_combiners2
GL_PER_STAGE_CONSTANTS_NV = 0x8535
# NV_shader_atomic_float
# NV_shader_buffer_load
GL_BUFFER_GPU_ADDRESS_NV = 0x8F1D
GL_GPU_ADDRESS_NV = 0x8F34
GL_MAX_SHADER_BUFFER_ADDRESS_NV = 0x8F35
# NV_shader_buffer_store
GL_SHADER_GLOBAL_ACCESS_BARRIER_BIT_NV = 0x00000010
# NV_tessellation_program5
GL_MAX_PROGRAM_PATCH_ATTRIBS_NV = 0x86D8
GL_TESS_CONTROL_PROGRAM_NV = 0x891E
GL_TESS_EVALUATION_PROGRAM_NV = 0x891F
GL_TESS_CONTROL_PROGRAM_PARAMETER_BUFFER_NV = 0x8C74
GL_TESS_EVALUATION_PROGRAM_PARAMETER_BUFFER_NV = 0x8C75
# NV_texgen_emboss
GL_EMBOSS_LIGHT_NV = 0x855D
GL_EMBOSS_CONSTANT_NV = 0x855E
GL_EMBOSS_MAP_NV = 0x855F
# NV_texgen_reflection
GL_NORMAL_MAP_NV = 0x8511
GL_REFLECTION_MAP_NV = 0x8512
# NV_texture_barrier
# NV_texture_compression_vtc
# NV_texture_env_combine4
GL_COMBINE4_NV = 0x8503
GL_SOURCE3_RGB_NV = 0x8583
GL_SOURCE3_ALPHA_NV = 0x858B
GL_OPERAND3_RGB_NV = 0x8593
GL_OPERAND3_ALPHA_NV = 0x859B
# NV_texture_expand_normal
GL_TEXTURE_UNSIGNED_REMAP_MODE_NV = 0x888F
# NV_texture_multisample
GL_TEXTURE_COVERAGE_SAMPLES_NV = 0x9045
GL_TEXTURE_COLOR_SAMPLES_NV = 0x9046
# NV_texture_rectangle
GL_TEXTURE_RECTANGLE_NV = 0x84F5
GL_TEXTURE_BINDING_RECTANGLE_NV = 0x84F6
GL_PROXY_TEXTURE_RECTANGLE_NV = 0x84F7
GL_MAX_RECTANGLE_TEXTURE_SIZE_NV = 0x84F8
# NV_texture_shader
GL_OFFSET_TEXTURE_RECTANGLE_NV = 0x864C
GL_OFFSET_TEXTURE_RECTANGLE_SCALE_NV = 0x864D
GL_DOT_PRODUCT_TEXTURE_RECTANGLE_NV = 0x864E
GL_RGBA_UNSIGNED_DOT_PRODUCT_MAPPING_NV = 0x86D9
GL_UNSIGNED_INT_S8_S8_8_8_NV = 0x86DA
GL_UNSIGNED_INT_8_8_S8_S8_REV_NV = 0x86DB
GL_DSDT_MAG_INTENSITY_NV = 0x86DC
GL_SHADER_CONSISTENT_NV = 0x86DD
GL_TEXTURE_SHADER_NV = 0x86DE
GL_SHADER_OPERATION_NV = 0x86DF
GL_CULL_MODES_NV = 0x86E0
GL_OFFSET_TEXTURE_MATRIX_NV = 0x86E1
GL_OFFSET_TEXTURE_SCALE_NV = 0x86E2
GL_OFFSET_TEXTURE_BIAS_NV = 0x86E3
GL_OFFSET_TEXTURE_2D_MATRIX_NV = 0x86E1 # GL_OFFSET_TEXTURE_MATRIX_NV
GL_OFFSET_TEXTURE_2D_SCALE_NV = 0x86E2 # GL_OFFSET_TEXTURE_SCALE_NV
GL_OFFSET_TEXTURE_2D_BIAS_NV = 0x86E3 # GL_OFFSET_TEXTURE_BIAS_NV
GL_PREVIOUS_TEXTURE_INPUT_NV = 0x86E4
GL_CONST_EYE_NV = 0x86E5
GL_PASS_THROUGH_NV = 0x86E6
GL_CULL_FRAGMENT_NV = 0x86E7
GL_OFFSET_TEXTURE_2D_NV = 0x86E8
GL_DEPENDENT_AR_TEXTURE_2D_NV = 0x86E9
GL_DEPENDENT_GB_TEXTURE_2D_NV = 0x86EA
GL_DOT_PRODUCT_NV = 0x86EC
GL_DOT_PRODUCT_DEPTH_REPLACE_NV = 0x86ED
GL_DOT_PRODUCT_TEXTURE_2D_NV = 0x86EE
GL_DOT_PRODUCT_TEXTURE_CUBE_MAP_NV = 0x86F0
GL_DOT_PRODUCT_DIFFUSE_CUBE_MAP_NV = 0x86F1
GL_DOT_PRODUCT_REFLECT_CUBE_MAP_NV = 0x86F2
GL_DOT_PRODUCT_CONST_EYE_REFLECT_CUBE_MAP_NV = 0x86F3
GL_HILO_NV = 0x86F4
GL_DSDT_NV = 0x86F5
GL_DSDT_MAG_NV = 0x86F6
GL_DSDT_MAG_VIB_NV = 0x86F7
GL_HILO16_NV = 0x86F8
GL_SIGNED_HILO_NV = 0x86F9
GL_SIGNED_HILO16_NV = 0x86FA
GL_SIGNED_RGBA_NV = 0x86FB
GL_SIGNED_RGBA8_NV = 0x86FC
GL_SIGNED_RGB_NV = 0x86FE
GL_SIGNED_RGB8_NV = 0x86FF
GL_SIGNED_LUMINANCE_NV = 0x8701
GL_SIGNED_LUMINANCE8_NV = 0x8702
GL_SIGNED_LUMINANCE_ALPHA_NV = 0x8703
GL_SIGNED_LUMINANCE8_ALPHA8_NV = 0x8704
GL_SIGNED_ALPHA_NV = 0x8705
GL_SIGNED_ALPHA8_NV = 0x8706
GL_SIGNED_INTENSITY_NV = 0x8707
GL_SIGNED_INTENSITY8_NV = 0x8708
GL_DSDT8_NV = 0x8709
GL_DSDT8_MAG8_NV = 0x870A
GL_DSDT8_MAG8_INTENSITY8_NV = 0x870B
GL_SIGNED_RGB_UNSIGNED_ALPHA_NV = 0x870C
GL_SIGNED_RGB8_UNSIGNED_ALPHA8_NV = 0x870D
GL_HI_SCALE_NV = 0x870E
GL_LO_SCALE_NV = 0x870F
GL_DS_SCALE_NV = 0x8710
GL_DT_SCALE_NV = 0x8711
GL_MAGNITUDE_SCALE_NV = 0x8712
GL_VIBRANCE_SCALE_NV = 0x8713
GL_HI_BIAS_NV = 0x8714
GL_LO_BIAS_NV = 0x8715
GL_DS_BIAS_NV = 0x8716
GL_DT_BIAS_NV = 0x8717
GL_MAGNITUDE_BIAS_NV = 0x8718
GL_VIBRANCE_BIAS_NV = 0x8719
GL_TEXTURE_BORDER_VALUES_NV = 0x871A
GL_TEXTURE_HI_SIZE_NV = 0x871B
GL_TEXTURE_LO_SIZE_NV = 0x871C
GL_TEXTURE_DS_SIZE_NV = 0x871D
GL_TEXTURE_DT_SIZE_NV = 0x871E
GL_TEXTURE_MAG_SIZE_NV = 0x871F
# NV_texture_shader2
GL_DOT_PRODUCT_TEXTURE_3D_NV = 0x86EF
# NV_texture_shader3
GL_OFFSET_PROJECTIVE_TEXTURE_2D_NV = 0x8850
GL_OFFSET_PROJECTIVE_TEXTURE_2D_SCALE_NV = 0x8851
GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_NV = 0x8852
GL_OFFSET_PROJECTIVE_TEXTURE_RECTANGLE_SCALE_NV = 0x8853
GL_OFFSET_HILO_TEXTURE_2D_NV = 0x8854
GL_OFFSET_HILO_TEXTURE_RECTANGLE_NV = 0x8855
GL_OFFSET_HILO_PROJECTIVE_TEXTURE_2D_NV = 0x8856
GL_OFFSET_HILO_PROJECTIVE_TEXTURE_RECTANGLE_NV = 0x8857
GL_DEPENDENT_HILO_TEXTURE_2D_NV = 0x8858
GL_DEPENDENT_RGB_TEXTURE_3D_NV = 0x8859
GL_DEPENDENT_RGB_TEXTURE_CUBE_MAP_NV = 0x885A
GL_DOT_PRODUCT_PASS_THROUGH_NV = 0x885B
GL_DOT_PRODUCT_TEXTURE_1D_NV = 0x885C
GL_DOT_PRODUCT_AFFINE_DEPTH_REPLACE_NV = 0x885D
GL_HILO8_NV = 0x885E
GL_SIGNED_HILO8_NV = 0x885F
GL_FORCE_BLUE_TO_ONE_NV = 0x8860
# NV_transform_feedback
GL_BACK_PRIMARY_COLOR_NV = 0x8C77
GL_BACK_SECONDARY_COLOR_NV = 0x8C78
GL_TEXTURE_COORD_NV = 0x8C79
GL_CLIP_DISTANCE_NV = 0x8C7A
GL_VERTEX_ID_NV = 0x8C7B
GL_PRIMITIVE_ID_NV = 0x8C7C
GL_GENERIC_ATTRIB_NV = 0x8C7D
GL_TRANSFORM_FEEDBACK_ATTRIBS_NV = 0x8C7E
GL_TRANSFORM_FEEDBACK_BUFFER_MODE_NV = 0x8C7F
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS_NV = 0x8C80
GL_ACTIVE_VARYINGS_NV = 0x8C81
GL_ACTIVE_VARYING_MAX_LENGTH_NV = 0x8C82
GL_TRANSFORM_FEEDBACK_VARYINGS_NV = 0x8C83
GL_TRANSFORM_FEEDBACK_BUFFER_START_NV = 0x8C84
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE_NV = 0x8C85
GL_TRANSFORM_FEEDBACK_RECORD_NV = 0x8C86
GL_PRIMITIVES_GENERATED_NV = 0x8C87
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN_NV = 0x8C88
GL_RASTERIZER_DISCARD_NV = 0x8C89
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS_NV = 0x8C8A
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS_NV = 0x8C8B
GL_INTERLEAVED_ATTRIBS_NV = 0x8C8C
GL_SEPARATE_ATTRIBS_NV = 0x8C8D
GL_TRANSFORM_FEEDBACK_BUFFER_NV = 0x8C8E
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING_NV = 0x8C8F
GL_LAYER_NV = 0x8DAA
GL_NEXT_BUFFER_NV = -2
GL_SKIP_COMPONENTS4_NV = -3
GL_SKIP_COMPONENTS3_NV = -4
GL_SKIP_COMPONENTS2_NV = -5
GL_SKIP_COMPONENTS1_NV = -6
# NV_transform_feedback2
GL_TRANSFORM_FEEDBACK_NV = 0x8E22
GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED_NV = 0x8E23
GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE_NV = 0x8E24
GL_TRANSFORM_FEEDBACK_BINDING_NV = 0x8E25
# NV_vdpau_interop
GL_SURFACE_STATE_NV = 0x86EB
GL_SURFACE_REGISTERED_NV = 0x86FD
GL_SURFACE_MAPPED_NV = 0x8700
GL_WRITE_DISCARD_NV = 0x88BE
# NV_vertex_array_range
GL_VERTEX_ARRAY_RANGE_NV = 0x851D
GL_VERTEX_ARRAY_RANGE_LENGTH_NV = 0x851E
GL_VERTEX_ARRAY_RANGE_VALID_NV = 0x851F
GL_MAX_VERTEX_ARRAY_RANGE_ELEMENT_NV = 0x8520
GL_VERTEX_ARRAY_RANGE_POINTER_NV = 0x8521
# NV_vertex_array_range2
GL_VERTEX_ARRAY_RANGE_WITHOUT_FLUSH_NV = 0x8533
# NV_vertex_attrib_integer_64bit
# NV_vertex_buffer_unified_memory
GL_VERTEX_ATTRIB_ARRAY_UNIFIED_NV = 0x8F1E
GL_ELEMENT_ARRAY_UNIFIED_NV = 0x8F1F
GL_VERTEX_ATTRIB_ARRAY_ADDRESS_NV = 0x8F20
GL_VERTEX_ARRAY_ADDRESS_NV = 0x8F21
GL_NORMAL_ARRAY_ADDRESS_NV = 0x8F22
GL_COLOR_ARRAY_ADDRESS_NV = 0x8F23
GL_INDEX_ARRAY_ADDRESS_NV = 0x8F24
GL_TEXTURE_COORD_ARRAY_ADDRESS_NV = 0x8F25
GL_EDGE_FLAG_ARRAY_ADDRESS_NV = 0x8F26
GL_SECONDARY_COLOR_ARRAY_ADDRESS_NV = 0x8F27
GL_FOG_COORD_ARRAY_ADDRESS_NV = 0x8F28
GL_ELEMENT_ARRAY_ADDRESS_NV = 0x8F29
GL_VERTEX_ATTRIB_ARRAY_LENGTH_NV = 0x8F2A
GL_VERTEX_ARRAY_LENGTH_NV = 0x8F2B
GL_NORMAL_ARRAY_LENGTH_NV = 0x8F2C
GL_COLOR_ARRAY_LENGTH_NV = 0x8F2D
GL_INDEX_ARRAY_LENGTH_NV = 0x8F2E
GL_TEXTURE_COORD_ARRAY_LENGTH_NV = 0x8F2F
GL_EDGE_FLAG_ARRAY_LENGTH_NV = 0x8F30
GL_SECONDARY_COLOR_ARRAY_LENGTH_NV = 0x8F31
GL_FOG_COORD_ARRAY_LENGTH_NV = 0x8F32
GL_ELEMENT_ARRAY_LENGTH_NV = 0x8F33
GL_DRAW_INDIRECT_UNIFIED_NV = 0x8F40
GL_DRAW_INDIRECT_ADDRESS_NV = 0x8F41
GL_DRAW_INDIRECT_LENGTH_NV = 0x8F42
# NV_vertex_program
GL_VERTEX_PROGRAM_NV = 0x8620
GL_VERTEX_STATE_PROGRAM_NV = 0x8621
GL_ATTRIB_ARRAY_SIZE_NV = 0x8623
GL_ATTRIB_ARRAY_STRIDE_NV = 0x8624
GL_ATTRIB_ARRAY_TYPE_NV = 0x8625
GL_CURRENT_ATTRIB_NV = 0x8626
GL_PROGRAM_LENGTH_NV = 0x8627
GL_PROGRAM_STRING_NV = 0x8628
GL_MODELVIEW_PROJECTION_NV = 0x8629
GL_IDENTITY_NV = 0x862A
GL_INVERSE_NV = 0x862B
GL_TRANSPOSE_NV = 0x862C
GL_INVERSE_TRANSPOSE_NV = 0x862D
GL_MAX_TRACK_MATRIX_STACK_DEPTH_NV = 0x862E
GL_MAX_TRACK_MATRICES_NV = 0x862F
GL_MATRIX0_NV = 0x8630
GL_MATRIX1_NV = 0x8631
GL_MATRIX2_NV = 0x8632
GL_MATRIX3_NV = 0x8633
GL_MATRIX4_NV = 0x8634
GL_MATRIX5_NV = 0x8635
GL_MATRIX6_NV = 0x8636
GL_MATRIX7_NV = 0x8637
GL_CURRENT_MATRIX_STACK_DEPTH_NV = 0x8640
GL_CURRENT_MATRIX_NV = 0x8641
GL_VERTEX_PROGRAM_POINT_SIZE_NV = 0x8642
GL_VERTEX_PROGRAM_TWO_SIDE_NV = 0x8643
GL_PROGRAM_PARAMETER_NV = 0x8644
GL_ATTRIB_ARRAY_POINTER_NV = 0x8645
GL_PROGRAM_TARGET_NV = 0x8646
GL_PROGRAM_RESIDENT_NV = 0x8647
GL_TRACK_MATRIX_NV = 0x8648
GL_TRACK_MATRIX_TRANSFORM_NV = 0x8649
GL_VERTEX_PROGRAM_BINDING_NV = 0x864A
GL_PROGRAM_ERROR_POSITION_NV = 0x864B
GL_VERTEX_ATTRIB_ARRAY0_NV = 0x8650
GL_VERTEX_ATTRIB_ARRAY1_NV = 0x8651
GL_VERTEX_ATTRIB_ARRAY2_NV = 0x8652
GL_VERTEX_ATTRIB_ARRAY3_NV = 0x8653
GL_VERTEX_ATTRIB_ARRAY4_NV = 0x8654
GL_VERTEX_ATTRIB_ARRAY5_NV = 0x8655
GL_VERTEX_ATTRIB_ARRAY6_NV = 0x8656
GL_VERTEX_ATTRIB_ARRAY7_NV = 0x8657
GL_VERTEX_ATTRIB_ARRAY8_NV = 0x8658
GL_VERTEX_ATTRIB_ARRAY9_NV = 0x8659
GL_VERTEX_ATTRIB_ARRAY10_NV = 0x865A
GL_VERTEX_ATTRIB_ARRAY11_NV = 0x865B
GL_VERTEX_ATTRIB_ARRAY12_NV = 0x865C
GL_VERTEX_ATTRIB_ARRAY13_NV = 0x865D
GL_VERTEX_ATTRIB_ARRAY14_NV = 0x865E
GL_VERTEX_ATTRIB_ARRAY15_NV = 0x865F
GL_MAP1_VERTEX_ATTRIB0_4_NV = 0x8660
GL_MAP1_VERTEX_ATTRIB1_4_NV = 0x8661
GL_MAP1_VERTEX_ATTRIB2_4_NV = 0x8662
GL_MAP1_VERTEX_ATTRIB3_4_NV = 0x8663
GL_MAP1_VERTEX_ATTRIB4_4_NV = 0x8664
GL_MAP1_VERTEX_ATTRIB5_4_NV = 0x8665
GL_MAP1_VERTEX_ATTRIB6_4_NV = 0x8666
GL_MAP1_VERTEX_ATTRIB7_4_NV = 0x8667
GL_MAP1_VERTEX_ATTRIB8_4_NV = 0x8668
GL_MAP1_VERTEX_ATTRIB9_4_NV = 0x8669
GL_MAP1_VERTEX_ATTRIB10_4_NV = 0x866A
GL_MAP1_VERTEX_ATTRIB11_4_NV = 0x866B
GL_MAP1_VERTEX_ATTRIB12_4_NV = 0x866C
GL_MAP1_VERTEX_ATTRIB13_4_NV = 0x866D
GL_MAP1_VERTEX_ATTRIB14_4_NV = 0x866E
GL_MAP1_VERTEX_ATTRIB15_4_NV = 0x866F
GL_MAP2_VERTEX_ATTRIB0_4_NV = 0x8670
GL_MAP2_VERTEX_ATTRIB1_4_NV = 0x8671
GL_MAP2_VERTEX_ATTRIB2_4_NV = 0x8672
GL_MAP2_VERTEX_ATTRIB3_4_NV = 0x8673
GL_MAP2_VERTEX_ATTRIB4_4_NV = 0x8674
GL_MAP2_VERTEX_ATTRIB5_4_NV = 0x8675
GL_MAP2_VERTEX_ATTRIB6_4_NV = 0x8676
GL_MAP2_VERTEX_ATTRIB7_4_NV = 0x8677
GL_MAP2_VERTEX_ATTRIB8_4_NV = 0x8678
GL_MAP2_VERTEX_ATTRIB9_4_NV = 0x8679
GL_MAP2_VERTEX_ATTRIB10_4_NV = 0x867A
GL_MAP2_VERTEX_ATTRIB11_4_NV = 0x867B
GL_MAP2_VERTEX_ATTRIB12_4_NV = 0x867C
GL_MAP2_VERTEX_ATTRIB13_4_NV = 0x867D
GL_MAP2_VERTEX_ATTRIB14_4_NV = 0x867E
GL_MAP2_VERTEX_ATTRIB15_4_NV = 0x867F
# NV_vertex_program1_1
# NV_vertex_program2
# NV_vertex_program2_option
# NV_vertex_program3
# NV_vertex_program4
GL_VERTEX_ATTRIB_ARRAY_INTEGER_NV = 0x88FD
# NV_video_capture
GL_VIDEO_BUFFER_NV = 0x9020
GL_VIDEO_BUFFER_BINDING_NV = 0x9021
GL_FIELD_UPPER_NV = 0x9022
GL_FIELD_LOWER_NV = 0x9023
GL_NUM_VIDEO_CAPTURE_STREAMS_NV = 0x9024
GL_NEXT_VIDEO_CAPTURE_BUFFER_STATUS_NV = 0x9025
GL_VIDEO_CAPTURE_TO_422_SUPPORTED_NV = 0x9026
GL_LAST_VIDEO_CAPTURE_STATUS_NV = 0x9027
GL_VIDEO_BUFFER_PITCH_NV = 0x9028
GL_VIDEO_COLOR_CONVERSION_MATRIX_NV = 0x9029
GL_VIDEO_COLOR_CONVERSION_MAX_NV = 0x902A
GL_VIDEO_COLOR_CONVERSION_MIN_NV = 0x902B
GL_VIDEO_COLOR_CONVERSION_OFFSET_NV = 0x902C
GL_VIDEO_BUFFER_INTERNAL_FORMAT_NV = 0x902D
GL_PARTIAL_SUCCESS_NV = 0x902E
GL_SUCCESS_NV = 0x902F
GL_FAILURE_NV = 0x9030
GL_YCBYCR8_422_NV = 0x9031
GL_YCBAYCR8A_4224_NV = 0x9032
GL_Z6Y10Z6CB10Z6Y10Z6CR10_422_NV = 0x9033
GL_Z6Y10Z6CB10Z6A10Z6Y10Z6CR10Z6A10_4224_NV = 0x9034
GL_Z4Y12Z4CB12Z4Y12Z4CR12_422_NV = 0x9035
GL_Z4Y12Z4CB12Z4A12Z4Y12Z4CR12Z4A12_4224_NV = 0x9036
GL_Z4Y12Z4CB12Z4CR12_444_NV = 0x9037
GL_VIDEO_CAPTURE_FRAME_WIDTH_NV = 0x9038
GL_VIDEO_CAPTURE_FRAME_HEIGHT_NV = 0x9039
GL_VIDEO_CAPTURE_FIELD_UPPER_HEIGHT_NV = 0x903A
GL_VIDEO_CAPTURE_FIELD_LOWER_HEIGHT_NV = 0x903B
GL_VIDEO_CAPTURE_SURFACE_ORIGIN_NV = 0x903C
WGL_UNIQUE_ID_NV = 0x20CE
WGL_NUM_VIDEO_CAPTURE_SLOTS_NV = 0x20CF
# OES_read_format
GL_IMPLEMENTATION_COLOR_READ_TYPE_OES = 0x8B9A
GL_IMPLEMENTATION_COLOR_READ_FORMAT_OES = 0x8B9B
# OML_interlace
GL_INTERLACE_OML = 0x8980
GL_INTERLACE_READ_OML = 0x8981
# OML_resample
GL_PACK_RESAMPLE_OML = 0x8984
GL_UNPACK_RESAMPLE_OML = 0x8985
GL_RESAMPLE_REPLICATE_OML = 0x8986
GL_RESAMPLE_ZERO_FILL_OML = 0x8987
GL_RESAMPLE_AVERAGE_OML = 0x8988
GL_RESAMPLE_DECIMATE_OML = 0x8989
# OML_subsample
GL_FORMAT_SUBSAMPLE_24_24_OML = 0x8982
GL_FORMAT_SUBSAMPLE_244_244_OML = 0x8983
# PGI_misc_hints
GL_PREFER_DOUBLEBUFFER_HINT_PGI = 0x1A1F8
GL_CONSERVE_MEMORY_HINT_PGI = 0x1A1FD
GL_RECLAIM_MEMORY_HINT_PGI = 0x1A1FE
GL_NATIVE_GRAPHICS_HANDLE_PGI = 0x1A202
GL_NATIVE_GRAPHICS_BEGIN_HINT_PGI = 0x1A203
GL_NATIVE_GRAPHICS_END_HINT_PGI = 0x1A204
GL_ALWAYS_FAST_HINT_PGI = 0x1A20C
GL_ALWAYS_SOFT_HINT_PGI = 0x1A20D
GL_ALLOW_DRAW_OBJ_HINT_PGI = 0x1A20E
GL_ALLOW_DRAW_WIN_HINT_PGI = 0x1A20F
GL_ALLOW_DRAW_FRG_HINT_PGI = 0x1A210
GL_ALLOW_DRAW_MEM_HINT_PGI = 0x1A211
GL_STRICT_DEPTHFUNC_HINT_PGI = 0x1A216
GL_STRICT_LIGHTING_HINT_PGI = 0x1A217
GL_STRICT_SCISSOR_HINT_PGI = 0x1A218
GL_FULL_STIPPLE_HINT_PGI = 0x1A219
GL_CLIP_NEAR_HINT_PGI = 0x1A220
GL_CLIP_FAR_HINT_PGI = 0x1A221
GL_WIDE_LINE_HINT_PGI = 0x1A222
GL_BACK_NORMALS_HINT_PGI = 0x1A223
# PGI_vertex_hints
GL_VERTEX_DATA_HINT_PGI = 0x1A22A
GL_VERTEX_CONSISTENT_HINT_PGI = 0x1A22B
GL_MATERIAL_SIDE_HINT_PGI = 0x1A22C
GL_MAX_VERTEX_HINT_PGI = 0x1A22D
GL_COLOR3_BIT_PGI = 0x00010000
GL_COLOR4_BIT_PGI = 0x00020000
GL_EDGEFLAG_BIT_PGI = 0x00040000
GL_INDEX_BIT_PGI = 0x00080000
GL_MAT_AMBIENT_BIT_PGI = 0x00100000
GL_MAT_AMBIENT_AND_DIFFUSE_BIT_PGI = 0x00200000
GL_MAT_DIFFUSE_BIT_PGI = 0x00400000
GL_MAT_EMISSION_BIT_PGI = 0x00800000
GL_MAT_COLOR_INDEXES_BIT_PGI = 0x01000000
GL_MAT_SHININESS_BIT_PGI = 0x02000000
GL_MAT_SPECULAR_BIT_PGI = 0x04000000
GL_NORMAL_BIT_PGI = 0x08000000
GL_TEXCOORD1_BIT_PGI = 0x10000000
GL_TEXCOORD2_BIT_PGI = 0x20000000
GL_TEXCOORD3_BIT_PGI = 0x40000000
GL_TEXCOORD4_BIT_PGI = 0x80000000
GL_VERTEX23_BIT_PGI = 0x00000004
GL_VERTEX4_BIT_PGI = 0x00000008
# REND_screen_coordinates
GL_SCREEN_COORDINATES_REND = 0x8490
GL_INVERTED_SCREEN_W_REND = 0x8491
# S3_s3tc
GL_RGB_S3TC = 0x83A0
GL_RGB4_S3TC = 0x83A1
GL_RGBA_S3TC = 0x83A2
GL_RGBA4_S3TC = 0x83A3
GL_RGBA_DXT5_S3TC = 0x83A4
GL_RGBA4_DXT5_S3TC = 0x83A5
# SGIS_detail_texture
GL_DETAIL_TEXTURE_2D_SGIS = 0x8095
GL_DETAIL_TEXTURE_2D_BINDING_SGIS = 0x8096
GL_LINEAR_DETAIL_SGIS = 0x8097
GL_LINEAR_DETAIL_ALPHA_SGIS = 0x8098
GL_LINEAR_DETAIL_COLOR_SGIS = 0x8099
GL_DETAIL_TEXTURE_LEVEL_SGIS = 0x809A
GL_DETAIL_TEXTURE_MODE_SGIS = 0x809B
GL_DETAIL_TEXTURE_FUNC_POINTS_SGIS = 0x809C
# SGIS_fog_function
GL_FOG_FUNC_SGIS = 0x812A
GL_FOG_FUNC_POINTS_SGIS = 0x812B
GL_MAX_FOG_FUNC_POINTS_SGIS = 0x812C
# SGIS_generate_mipmap
GL_GENERATE_MIPMAP_SGIS = 0x8191
GL_GENERATE_MIPMAP_HINT_SGIS = 0x8192
# SGIS_multisample
GL_MULTISAMPLE_SGIS = 0x809D
GL_SAMPLE_ALPHA_TO_MASK_SGIS = 0x809E
GL_SAMPLE_ALPHA_TO_ONE_SGIS = 0x809F
GL_SAMPLE_MASK_SGIS = 0x80A0
GL_1PASS_SGIS = 0x80A1
GL_2PASS_0_SGIS = 0x80A2
GL_2PASS_1_SGIS = 0x80A3
GL_4PASS_0_SGIS = 0x80A4
GL_4PASS_1_SGIS = 0x80A5
GL_4PASS_2_SGIS = 0x80A6
GL_4PASS_3_SGIS = 0x80A7
GL_SAMPLE_BUFFERS_SGIS = 0x80A8
GL_SAMPLES_SGIS = 0x80A9
GL_SAMPLE_MASK_VALUE_SGIS = 0x80AA
GL_SAMPLE_MASK_INVERT_SGIS = 0x80AB
GL_SAMPLE_PATTERN_SGIS = 0x80AC
# SGIS_pixel_texture
GL_PIXEL_TEXTURE_SGIS = 0x8353
GL_PIXEL_FRAGMENT_RGB_SOURCE_SGIS = 0x8354
GL_PIXEL_FRAGMENT_ALPHA_SOURCE_SGIS = 0x8355
GL_PIXEL_GROUP_COLOR_SGIS = 0x8356
# SGIS_point_line_texgen
GL_EYE_DISTANCE_TO_POINT_SGIS = 0x81F0
GL_OBJECT_DISTANCE_TO_POINT_SGIS = 0x81F1
GL_EYE_DISTANCE_TO_LINE_SGIS = 0x81F2
GL_OBJECT_DISTANCE_TO_LINE_SGIS = 0x81F3
GL_EYE_POINT_SGIS = 0x81F4
GL_OBJECT_POINT_SGIS = 0x81F5
GL_EYE_LINE_SGIS = 0x81F6
GL_OBJECT_LINE_SGIS = 0x81F7
# SGIS_point_parameters
GL_POINT_SIZE_MIN_SGIS = 0x8126
GL_POINT_SIZE_MAX_SGIS = 0x8127
GL_POINT_FADE_THRESHOLD_SIZE_SGIS = 0x8128
GL_DISTANCE_ATTENUATION_SGIS = 0x8129
# SGIS_sharpen_texture
GL_LINEAR_SHARPEN_SGIS = 0x80AD
GL_LINEAR_SHARPEN_ALPHA_SGIS = 0x80AE
GL_LINEAR_SHARPEN_COLOR_SGIS = 0x80AF
GL_SHARPEN_TEXTURE_FUNC_POINTS_SGIS = 0x80B0
# SGIS_texture4D
GL_PACK_SKIP_VOLUMES_SGIS = 0x8130
GL_PACK_IMAGE_DEPTH_SGIS = 0x8131
GL_UNPACK_SKIP_VOLUMES_SGIS = 0x8132
GL_UNPACK_IMAGE_DEPTH_SGIS = 0x8133
GL_TEXTURE_4D_SGIS = 0x8134
GL_PROXY_TEXTURE_4D_SGIS = 0x8135
GL_TEXTURE_4DSIZE_SGIS = 0x8136
GL_TEXTURE_WRAP_Q_SGIS = 0x8137
GL_MAX_4D_TEXTURE_SIZE_SGIS = 0x8138
GL_TEXTURE_4D_BINDING_SGIS = 0x814F
# SGIS_texture_border_clamp
GL_CLAMP_TO_BORDER_SGIS = 0x812D
# SGIS_texture_color_mask
GL_TEXTURE_COLOR_WRITEMASK_SGIS = 0x81EF
# SGIS_texture_edge_clamp
GL_CLAMP_TO_EDGE_SGIS = 0x812F
# SGIS_texture_filter4
GL_FILTER4_SGIS = 0x8146
GL_TEXTURE_FILTER4_SIZE_SGIS = 0x8147
# SGIS_texture_lod
GL_TEXTURE_MIN_LOD_SGIS = 0x813A
GL_TEXTURE_MAX_LOD_SGIS = 0x813B
GL_TEXTURE_BASE_LEVEL_SGIS = 0x813C
GL_TEXTURE_MAX_LEVEL_SGIS = 0x813D
# SGIS_texture_select
GL_DUAL_ALPHA4_SGIS = 0x8110
GL_DUAL_ALPHA8_SGIS = 0x8111
GL_DUAL_ALPHA12_SGIS = 0x8112
GL_DUAL_ALPHA16_SGIS = 0x8113
GL_DUAL_LUMINANCE4_SGIS = 0x8114
GL_DUAL_LUMINANCE8_SGIS = 0x8115
GL_DUAL_LUMINANCE12_SGIS = 0x8116
GL_DUAL_LUMINANCE16_SGIS = 0x8117
GL_DUAL_INTENSITY4_SGIS = 0x8118
GL_DUAL_INTENSITY8_SGIS = 0x8119
GL_DUAL_INTENSITY12_SGIS = 0x811A
GL_DUAL_INTENSITY16_SGIS = 0x811B
GL_DUAL_LUMINANCE_ALPHA4_SGIS = 0x811C
GL_DUAL_LUMINANCE_ALPHA8_SGIS = 0x811D
GL_QUAD_ALPHA4_SGIS = 0x811E
GL_QUAD_ALPHA8_SGIS = 0x811F
GL_QUAD_LUMINANCE4_SGIS = 0x8120
GL_QUAD_LUMINANCE8_SGIS = 0x8121
GL_QUAD_INTENSITY4_SGIS = 0x8122
GL_QUAD_INTENSITY8_SGIS = 0x8123
GL_DUAL_TEXTURE_SELECT_SGIS = 0x8124
GL_QUAD_TEXTURE_SELECT_SGIS = 0x8125
# SGIX_async
GL_ASYNC_MARKER_SGIX = 0x8329
# SGIX_async_histogram
GL_ASYNC_HISTOGRAM_SGIX = 0x832C
GL_MAX_ASYNC_HISTOGRAM_SGIX = 0x832D
# SGIX_async_pixel
GL_ASYNC_TEX_IMAGE_SGIX = 0x835C
GL_ASYNC_DRAW_PIXELS_SGIX = 0x835D
GL_ASYNC_READ_PIXELS_SGIX = 0x835E
GL_MAX_ASYNC_TEX_IMAGE_SGIX = 0x835F
GL_MAX_ASYNC_DRAW_PIXELS_SGIX = 0x8360
GL_MAX_ASYNC_READ_PIXELS_SGIX = 0x8361
# SGIX_blend_alpha_minmax
GL_ALPHA_MIN_SGIX = 0x8320
GL_ALPHA_MAX_SGIX = 0x8321
# SGIX_calligraphic_fragment
GL_CALLIGRAPHIC_FRAGMENT_SGIX = 0x8183
# SGIX_clipmap
GL_LINEAR_CLIPMAP_LINEAR_SGIX = 0x8170
GL_TEXTURE_CLIPMAP_CENTER_SGIX = 0x8171
GL_TEXTURE_CLIPMAP_FRAME_SGIX = 0x8172
GL_TEXTURE_CLIPMAP_OFFSET_SGIX = 0x8173
GL_TEXTURE_CLIPMAP_VIRTUAL_DEPTH_SGIX = 0x8174
GL_TEXTURE_CLIPMAP_LOD_OFFSET_SGIX = 0x8175
GL_TEXTURE_CLIPMAP_DEPTH_SGIX = 0x8176
GL_MAX_CLIPMAP_DEPTH_SGIX = 0x8177
GL_MAX_CLIPMAP_VIRTUAL_DEPTH_SGIX = 0x8178
GL_NEAREST_CLIPMAP_NEAREST_SGIX = 0x844D
GL_NEAREST_CLIPMAP_LINEAR_SGIX = 0x844E
GL_LINEAR_CLIPMAP_NEAREST_SGIX = 0x844F
# SGIX_convolution_accuracy
GL_CONVOLUTION_HINT_SGIX = 0x8316
# SGIX_depth_texture
GL_DEPTH_COMPONENT16_SGIX = 0x81A5
GL_DEPTH_COMPONENT24_SGIX = 0x81A6
GL_DEPTH_COMPONENT32_SGIX = 0x81A7
# SGIX_flush_raster
# SGIX_fog_offset
GL_FOG_OFFSET_SGIX = 0x8198
GL_FOG_OFFSET_VALUE_SGIX = 0x8199
# SGIX_fog_scale
GL_FOG_SCALE_SGIX = 0x81FC
GL_FOG_SCALE_VALUE_SGIX = 0x81FD
# SGIX_fragment_lighting
GL_FRAGMENT_LIGHTING_SGIX = 0x8400
GL_FRAGMENT_COLOR_MATERIAL_SGIX = 0x8401
GL_FRAGMENT_COLOR_MATERIAL_FACE_SGIX = 0x8402
GL_FRAGMENT_COLOR_MATERIAL_PARAMETER_SGIX = 0x8403
GL_MAX_FRAGMENT_LIGHTS_SGIX = 0x8404
GL_MAX_ACTIVE_LIGHTS_SGIX = 0x8405
GL_CURRENT_RASTER_NORMAL_SGIX = 0x8406
GL_LIGHT_ENV_MODE_SGIX = 0x8407
GL_FRAGMENT_LIGHT_MODEL_LOCAL_VIEWER_SGIX = 0x8408
GL_FRAGMENT_LIGHT_MODEL_TWO_SIDE_SGIX = 0x8409
GL_FRAGMENT_LIGHT_MODEL_AMBIENT_SGIX = 0x840A
GL_FRAGMENT_LIGHT_MODEL_NORMAL_INTERPOLATION_SGIX = 0x840B
GL_FRAGMENT_LIGHT0_SGIX = 0x840C
GL_FRAGMENT_LIGHT1_SGIX = 0x840D
GL_FRAGMENT_LIGHT2_SGIX = 0x840E
GL_FRAGMENT_LIGHT3_SGIX = 0x840F
GL_FRAGMENT_LIGHT4_SGIX = 0x8410
GL_FRAGMENT_LIGHT5_SGIX = 0x8411
GL_FRAGMENT_LIGHT6_SGIX = 0x8412
GL_FRAGMENT_LIGHT7_SGIX = 0x8413
# SGIX_framezoom
GL_FRAMEZOOM_SGIX = 0x818B
GL_FRAMEZOOM_FACTOR_SGIX = 0x818C
GL_MAX_FRAMEZOOM_FACTOR_SGIX = 0x818D
# SGIX_impact_pixel_texture
GL_PIXEL_TEX_GEN_Q_CEILING_SGIX = 0x8184
GL_PIXEL_TEX_GEN_Q_ROUND_SGIX = 0x8185
GL_PIXEL_TEX_GEN_Q_FLOOR_SGIX = 0x8186
GL_PIXEL_TEX_GEN_ALPHA_REPLACE_SGIX = 0x8187
GL_PIXEL_TEX_GEN_ALPHA_NO_REPLACE_SGIX = 0x8188
GL_PIXEL_TEX_GEN_ALPHA_LS_SGIX = 0x8189
GL_PIXEL_TEX_GEN_ALPHA_MS_SGIX = 0x818A
# SGIX_instruments
GL_INSTRUMENT_BUFFER_POINTER_SGIX = 0x8180
GL_INSTRUMENT_MEASUREMENTS_SGIX = 0x8181
# SGIX_interlace
GL_INTERLACE_SGIX = 0x8094
# SGIX_ir_instrument1
GL_IR_INSTRUMENT1_SGIX = 0x817F
# SGIX_list_priority
GL_LIST_PRIORITY_SGIX = 0x8182
# SGIX_pixel_texture
GL_PIXEL_TEX_GEN_SGIX = 0x8139
GL_PIXEL_TEX_GEN_MODE_SGIX = 0x832B
# SGIX_pixel_tiles
GL_PIXEL_TILE_BEST_ALIGNMENT_SGIX = 0x813E
GL_PIXEL_TILE_CACHE_INCREMENT_SGIX = 0x813F
GL_PIXEL_TILE_WIDTH_SGIX = 0x8140
GL_PIXEL_TILE_HEIGHT_SGIX = 0x8141
GL_PIXEL_TILE_GRID_WIDTH_SGIX = 0x8142
GL_PIXEL_TILE_GRID_HEIGHT_SGIX = 0x8143
GL_PIXEL_TILE_GRID_DEPTH_SGIX = 0x8144
GL_PIXEL_TILE_CACHE_SIZE_SGIX = 0x8145
# SGIX_polynomial_ffd
GL_GEOMETRY_DEFORMATION_SGIX = 0x8194
GL_TEXTURE_DEFORMATION_SGIX = 0x8195
GL_DEFORMATIONS_MASK_SGIX = 0x8196
GL_MAX_DEFORMATION_ORDER_SGIX = 0x8197
# SGIX_reference_plane
GL_REFERENCE_PLANE_SGIX = 0x817D
GL_REFERENCE_PLANE_EQUATION_SGIX = 0x817E
# SGIX_resample
GL_PACK_RESAMPLE_SGIX = 0x842C
GL_UNPACK_RESAMPLE_SGIX = 0x842D
GL_RESAMPLE_REPLICATE_SGIX = 0x842E
GL_RESAMPLE_ZERO_FILL_SGIX = 0x842F
GL_RESAMPLE_DECIMATE_SGIX = 0x8430
# SGIX_scalebias_hint
GL_SCALEBIAS_HINT_SGIX = 0x8322
# SGIX_shadow
GL_TEXTURE_COMPARE_SGIX = 0x819A
GL_TEXTURE_COMPARE_OPERATOR_SGIX = 0x819B
GL_TEXTURE_LEQUAL_R_SGIX = 0x819C
GL_TEXTURE_GEQUAL_R_SGIX = 0x819D
# SGIX_shadow_ambient
GL_SHADOW_AMBIENT_SGIX = 0x80BF
# SGIX_sprite
GL_SPRITE_SGIX = 0x8148
GL_SPRITE_MODE_SGIX = 0x8149
GL_SPRITE_AXIS_SGIX = 0x814A
GL_SPRITE_TRANSLATION_SGIX = 0x814B
GL_SPRITE_AXIAL_SGIX = 0x814C
GL_SPRITE_OBJECT_ALIGNED_SGIX = 0x814D
GL_SPRITE_EYE_ALIGNED_SGIX = 0x814E
# SGIX_subsample
GL_PACK_SUBSAMPLE_RATE_SGIX = 0x85A0
GL_UNPACK_SUBSAMPLE_RATE_SGIX = 0x85A1
GL_PIXEL_SUBSAMPLE_4444_SGIX = 0x85A2
GL_PIXEL_SUBSAMPLE_2424_SGIX = 0x85A3
GL_PIXEL_SUBSAMPLE_4242_SGIX = 0x85A4
# SGIX_tag_sample_buffer
# SGIX_texture_add_env
GL_TEXTURE_ENV_BIAS_SGIX = 0x80BE
# SGIX_texture_coordinate_clamp
GL_TEXTURE_MAX_CLAMP_S_SGIX = 0x8369
GL_TEXTURE_MAX_CLAMP_T_SGIX = 0x836A
GL_TEXTURE_MAX_CLAMP_R_SGIX = 0x836B
# SGIX_texture_lod_bias
GL_TEXTURE_LOD_BIAS_S_SGIX = 0x818E
GL_TEXTURE_LOD_BIAS_T_SGIX = 0x818F
GL_TEXTURE_LOD_BIAS_R_SGIX = 0x8190
# SGIX_texture_multi_buffer
GL_TEXTURE_MULTI_BUFFER_HINT_SGIX = 0x812E
# SGIX_texture_scale_bias
GL_POST_TEXTURE_FILTER_BIAS_SGIX = 0x8179
GL_POST_TEXTURE_FILTER_SCALE_SGIX = 0x817A
GL_POST_TEXTURE_FILTER_BIAS_RANGE_SGIX = 0x817B
GL_POST_TEXTURE_FILTER_SCALE_RANGE_SGIX = 0x817C
# SGIX_vertex_preclip
GL_VERTEX_PRECLIP_SGIX = 0x83EE
GL_VERTEX_PRECLIP_HINT_SGIX = 0x83EF
# SGIX_ycrcb
GL_YCRCB_422_SGIX = 0x81BB
GL_YCRCB_444_SGIX = 0x81BC
# SGIX_ycrcb_subsample
# SGIX_ycrcba
GL_YCRCB_SGIX = 0x8318
GL_YCRCBA_SGIX = 0x8319
# SGI_color_matrix
GL_COLOR_MATRIX_SGI = 0x80B1
GL_COLOR_MATRIX_STACK_DEPTH_SGI = 0x80B2
GL_MAX_COLOR_MATRIX_STACK_DEPTH_SGI = 0x80B3
GL_POST_COLOR_MATRIX_RED_SCALE_SGI = 0x80B4
GL_POST_COLOR_MATRIX_GREEN_SCALE_SGI = 0x80B5
GL_POST_COLOR_MATRIX_BLUE_SCALE_SGI = 0x80B6
GL_POST_COLOR_MATRIX_ALPHA_SCALE_SGI = 0x80B7
GL_POST_COLOR_MATRIX_RED_BIAS_SGI = 0x80B8
GL_POST_COLOR_MATRIX_GREEN_BIAS_SGI = 0x80B9
GL_POST_COLOR_MATRIX_BLUE_BIAS_SGI = 0x80BA
GL_POST_COLOR_MATRIX_ALPHA_BIAS_SGI = 0x80BB
# SGI_color_table
GL_COLOR_TABLE_SGI = 0x80D0
GL_POST_CONVOLUTION_COLOR_TABLE_SGI = 0x80D1
GL_POST_COLOR_MATRIX_COLOR_TABLE_SGI = 0x80D2
GL_PROXY_COLOR_TABLE_SGI = 0x80D3
GL_PROXY_POST_CONVOLUTION_COLOR_TABLE_SGI = 0x80D4
GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE_SGI = 0x80D5
GL_COLOR_TABLE_SCALE_SGI = 0x80D6
GL_COLOR_TABLE_BIAS_SGI = 0x80D7
GL_COLOR_TABLE_FORMAT_SGI = 0x80D8
GL_COLOR_TABLE_WIDTH_SGI = 0x80D9
GL_COLOR_TABLE_RED_SIZE_SGI = 0x80DA
GL_COLOR_TABLE_GREEN_SIZE_SGI = 0x80DB
GL_COLOR_TABLE_BLUE_SIZE_SGI = 0x80DC
GL_COLOR_TABLE_ALPHA_SIZE_SGI = 0x80DD
GL_COLOR_TABLE_LUMINANCE_SIZE_SGI = 0x80DE
GL_COLOR_TABLE_INTENSITY_SIZE_SGI = 0x80DF
# SGI_depth_pass_instrument
GL_DEPTH_PASS_INSTRUMENT_SGIX = 0x8310
GL_DEPTH_PASS_INSTRUMENT_COUNTERS_SGIX = 0x8311
GL_DEPTH_PASS_INSTRUMENT_MAX_SGIX = 0x8312
# SGI_texture_color_table
GL_TEXTURE_COLOR_TABLE_SGI = 0x80BC
GL_PROXY_TEXTURE_COLOR_TABLE_SGI = 0x80BD
# SUNX_constant_data
GL_UNPACK_CONSTANT_DATA_SUNX = 0x81D5
GL_TEXTURE_CONSTANT_DATA_SUNX = 0x81D6
# SUN_convolution_border_modes
GL_WRAP_BORDER_SUN = 0x81D4
# SUN_global_alpha
GL_GLOBAL_ALPHA_SUN = 0x81D9
GL_GLOBAL_ALPHA_FACTOR_SUN = 0x81DA
# SUN_mesh_array
GL_QUAD_MESH_SUN = 0x8614
GL_TRIANGLE_MESH_SUN = 0x8615
# SUN_slice_accum
GL_SLICE_ACCUM_SUN = 0x85CC
# SUN_triangle_list
GL_RESTART_SUN = 0x0001
GL_REPLACE_MIDDLE_SUN = 0x0002
GL_REPLACE_OLDEST_SUN = 0x0003
GL_TRIANGLE_LIST_SUN = 0x81D7
GL_REPLACEMENT_CODE_SUN = 0x81D8
GL_REPLACEMENT_CODE_ARRAY_SUN = 0x85C0
GL_REPLACEMENT_CODE_ARRAY_TYPE_SUN = 0x85C1
GL_REPLACEMENT_CODE_ARRAY_STRIDE_SUN = 0x85C2
GL_REPLACEMENT_CODE_ARRAY_POINTER_SUN = 0x85C3
GL_R1UI_V3F_SUN = 0x85C4
GL_R1UI_C4UB_V3F_SUN = 0x85C5
GL_R1UI_C3F_V3F_SUN = 0x85C6
GL_R1UI_N3F_V3F_SUN = 0x85C7
GL_R1UI_C4F_N3F_V3F_SUN = 0x85C8
GL_R1UI_T2F_V3F_SUN = 0x85C9
GL_R1UI_T2F_N3F_V3F_SUN = 0x85CA
GL_R1UI_T2F_C4F_N3F_V3F_SUN = 0x85CB
# SUN_vertex
# VERSION_1_1
GL_DEPTH_BUFFER_BIT = 0x00000100
GL_STENCIL_BUFFER_BIT = 0x00000400
GL_COLOR_BUFFER_BIT = 0x00004000
GL_FALSE = 0
GL_TRUE = 1
GL_POINTS = 0x0000
GL_LINES = 0x0001
GL_LINE_LOOP = 0x0002
GL_LINE_STRIP = 0x0003
GL_TRIANGLES = 0x0004
GL_TRIANGLE_STRIP = 0x0005
GL_TRIANGLE_FAN = 0x0006
GL_NEVER = 0x0200
GL_LESS = 0x0201
GL_EQUAL = 0x0202
GL_LEQUAL = 0x0203
GL_GREATER = 0x0204
GL_NOTEQUAL = 0x0205
GL_GEQUAL = 0x0206
GL_ALWAYS = 0x0207
GL_ZERO = 0
GL_ONE = 1
GL_SRC_COLOR = 0x0300
GL_ONE_MINUS_SRC_COLOR = 0x0301
GL_SRC_ALPHA = 0x0302
GL_ONE_MINUS_SRC_ALPHA = 0x0303
GL_DST_ALPHA = 0x0304
GL_ONE_MINUS_DST_ALPHA = 0x0305
GL_DST_COLOR = 0x0306
GL_ONE_MINUS_DST_COLOR = 0x0307
GL_SRC_ALPHA_SATURATE = 0x0308
GL_NONE = 0
GL_FRONT_LEFT = 0x0400
GL_FRONT_RIGHT = 0x0401
GL_BACK_LEFT = 0x0402
GL_BACK_RIGHT = 0x0403
GL_FRONT = 0x0404
GL_BACK = 0x0405
GL_LEFT = 0x0406
GL_RIGHT = 0x0407
GL_FRONT_AND_BACK = 0x0408
GL_NO_ERROR = 0
GL_INVALID_ENUM = 0x0500
GL_INVALID_VALUE = 0x0501
GL_INVALID_OPERATION = 0x0502
GL_OUT_OF_MEMORY = 0x0505
GL_CW = 0x0900
GL_CCW = 0x0901
GL_POINT_SIZE = 0x0B11
GL_POINT_SIZE_RANGE = 0x0B12
GL_POINT_SIZE_GRANULARITY = 0x0B13
GL_LINE_SMOOTH = 0x0B20
GL_LINE_WIDTH = 0x0B21
GL_LINE_WIDTH_RANGE = 0x0B22
GL_LINE_WIDTH_GRANULARITY = 0x0B23
GL_POLYGON_SMOOTH = 0x0B41
GL_CULL_FACE = 0x0B44
GL_CULL_FACE_MODE = 0x0B45
GL_FRONT_FACE = 0x0B46
GL_DEPTH_RANGE = 0x0B70
GL_DEPTH_TEST = 0x0B71
GL_DEPTH_WRITEMASK = 0x0B72
GL_DEPTH_CLEAR_VALUE = 0x0B73
GL_DEPTH_FUNC = 0x0B74
GL_STENCIL_TEST = 0x0B90
GL_STENCIL_CLEAR_VALUE = 0x0B91
GL_STENCIL_FUNC = 0x0B92
GL_STENCIL_VALUE_MASK = 0x0B93
GL_STENCIL_FAIL = 0x0B94
GL_STENCIL_PASS_DEPTH_FAIL = 0x0B95
GL_STENCIL_PASS_DEPTH_PASS = 0x0B96
GL_STENCIL_REF = 0x0B97
GL_STENCIL_WRITEMASK = 0x0B98
GL_VIEWPORT = 0x0BA2
GL_DITHER = 0x0BD0
GL_BLEND_DST = 0x0BE0
GL_BLEND_SRC = 0x0BE1
GL_BLEND = 0x0BE2
GL_LOGIC_OP_MODE = 0x0BF0
GL_COLOR_LOGIC_OP = 0x0BF2
GL_DRAW_BUFFER = 0x0C01
GL_READ_BUFFER = 0x0C02
GL_SCISSOR_BOX = 0x0C10
GL_SCISSOR_TEST = 0x0C11
GL_COLOR_CLEAR_VALUE = 0x0C22
GL_COLOR_WRITEMASK = 0x0C23
GL_DOUBLEBUFFER = 0x0C32
GL_STEREO = 0x0C33
GL_LINE_SMOOTH_HINT = 0x0C52
GL_POLYGON_SMOOTH_HINT = 0x0C53
GL_UNPACK_SWAP_BYTES = 0x0CF0
GL_UNPACK_LSB_FIRST = 0x0CF1
GL_UNPACK_ROW_LENGTH = 0x0CF2
GL_UNPACK_SKIP_ROWS = 0x0CF3
GL_UNPACK_SKIP_PIXELS = 0x0CF4
GL_UNPACK_ALIGNMENT = 0x0CF5
GL_PACK_SWAP_BYTES = 0x0D00
GL_PACK_LSB_FIRST = 0x0D01
GL_PACK_ROW_LENGTH = 0x0D02
GL_PACK_SKIP_ROWS = 0x0D03
GL_PACK_SKIP_PIXELS = 0x0D04
GL_PACK_ALIGNMENT = 0x0D05
GL_MAX_TEXTURE_SIZE = 0x0D33
GL_MAX_VIEWPORT_DIMS = 0x0D3A
GL_SUBPIXEL_BITS = 0x0D50
GL_TEXTURE_1D = 0x0DE0
GL_TEXTURE_2D = 0x0DE1
GL_POLYGON_OFFSET_UNITS = 0x2A00
GL_POLYGON_OFFSET_POINT = 0x2A01
GL_POLYGON_OFFSET_LINE = 0x2A02
GL_POLYGON_OFFSET_FILL = 0x8037
GL_POLYGON_OFFSET_FACTOR = 0x8038
GL_TEXTURE_BINDING_1D = 0x8068
GL_TEXTURE_BINDING_2D = 0x8069
GL_TEXTURE_WIDTH = 0x1000
GL_TEXTURE_HEIGHT = 0x1001
GL_TEXTURE_INTERNAL_FORMAT = 0x1003
GL_TEXTURE_BORDER_COLOR = 0x1004
GL_TEXTURE_RED_SIZE = 0x805C
GL_TEXTURE_GREEN_SIZE = 0x805D
GL_TEXTURE_BLUE_SIZE = 0x805E
GL_TEXTURE_ALPHA_SIZE = 0x805F
GL_DONT_CARE = 0x1100
GL_FASTEST = 0x1101
GL_NICEST = 0x1102
GL_BYTE = 0x1400
GL_UNSIGNED_BYTE = 0x1401
GL_SHORT = 0x1402
GL_UNSIGNED_SHORT = 0x1403
GL_INT = 0x1404
GL_UNSIGNED_INT = 0x1405
GL_FLOAT = 0x1406
GL_DOUBLE = 0x140A
GL_STACK_OVERFLOW = 0x0503
GL_STACK_UNDERFLOW = 0x0504
GL_CLEAR = 0x1500
GL_AND = 0x1501
GL_AND_REVERSE = 0x1502
GL_COPY = 0x1503
GL_AND_INVERTED = 0x1504
GL_NOOP = 0x1505
GL_XOR = 0x1506
GL_OR = 0x1507
GL_NOR = 0x1508
GL_EQUIV = 0x1509
GL_INVERT = 0x150A
GL_OR_REVERSE = 0x150B
GL_COPY_INVERTED = 0x150C
GL_OR_INVERTED = 0x150D
GL_NAND = 0x150E
GL_SET = 0x150F
GL_TEXTURE = 0x1702
GL_COLOR = 0x1800
GL_DEPTH = 0x1801
GL_STENCIL = 0x1802
GL_STENCIL_INDEX = 0x1901
GL_DEPTH_COMPONENT = 0x1902
GL_RED = 0x1903
GL_GREEN = 0x1904
GL_BLUE = 0x1905
GL_ALPHA = 0x1906
GL_RGB = 0x1907
GL_RGBA = 0x1908
GL_POINT = 0x1B00
GL_LINE = 0x1B01
GL_FILL = 0x1B02
GL_KEEP = 0x1E00
GL_REPLACE = 0x1E01
GL_INCR = 0x1E02
GL_DECR = 0x1E03
GL_VENDOR = 0x1F00
GL_RENDERER = 0x1F01
GL_VERSION = 0x1F02
GL_EXTENSIONS = 0x1F03
GL_NEAREST = 0x2600
GL_LINEAR = 0x2601
GL_NEAREST_MIPMAP_NEAREST = 0x2700
GL_LINEAR_MIPMAP_NEAREST = 0x2701
GL_NEAREST_MIPMAP_LINEAR = 0x2702
GL_LINEAR_MIPMAP_LINEAR = 0x2703
GL_TEXTURE_MAG_FILTER = 0x2800
GL_TEXTURE_MIN_FILTER = 0x2801
GL_TEXTURE_WRAP_S = 0x2802
GL_TEXTURE_WRAP_T = 0x2803
GL_PROXY_TEXTURE_1D = 0x8063
GL_PROXY_TEXTURE_2D = 0x8064
GL_REPEAT = 0x2901
GL_R3_G3_B2 = 0x2A10
GL_RGB4 = 0x804F
GL_RGB5 = 0x8050
GL_RGB8 = 0x8051
GL_RGB10 = 0x8052
GL_RGB12 = 0x8053
GL_RGB16 = 0x8054
GL_RGBA2 = 0x8055
GL_RGBA4 = 0x8056
GL_RGB5_A1 = 0x8057
GL_RGBA8 = 0x8058
GL_RGB10_A2 = 0x8059
GL_RGBA12 = 0x805A
GL_RGBA16 = 0x805B
# VERSION_1_1_DEPRECATED
GL_CURRENT_BIT = 0x00000001
GL_POINT_BIT = 0x00000002
GL_LINE_BIT = 0x00000004
GL_POLYGON_BIT = 0x00000008
GL_POLYGON_STIPPLE_BIT = 0x00000010
GL_PIXEL_MODE_BIT = 0x00000020
GL_LIGHTING_BIT = 0x00000040
GL_FOG_BIT = 0x00000080
GL_ACCUM_BUFFER_BIT = 0x00000200
GL_VIEWPORT_BIT = 0x00000800
GL_TRANSFORM_BIT = 0x00001000
GL_ENABLE_BIT = 0x00002000
GL_HINT_BIT = 0x00008000
GL_EVAL_BIT = 0x00010000
GL_LIST_BIT = 0x00020000
GL_TEXTURE_BIT = 0x00040000
GL_SCISSOR_BIT = 0x00080000
GL_ALL_ATTRIB_BITS = 0xFFFFFFFF
GL_CLIENT_PIXEL_STORE_BIT = 0x00000001
GL_CLIENT_VERTEX_ARRAY_BIT = 0x00000002
GL_CLIENT_ALL_ATTRIB_BITS = 0xFFFFFFFF
GL_QUADS = 0x0007
GL_QUAD_STRIP = 0x0008
GL_POLYGON = 0x0009
GL_ACCUM = 0x0100
GL_LOAD = 0x0101
GL_RETURN = 0x0102
GL_MULT = 0x0103
GL_ADD = 0x0104
GL_AUX0 = 0x0409
GL_AUX1 = 0x040A
GL_AUX2 = 0x040B
GL_AUX3 = 0x040C
GL_2D = 0x0600
GL_3D = 0x0601
GL_3D_COLOR = 0x0602
GL_3D_COLOR_TEXTURE = 0x0603
GL_4D_COLOR_TEXTURE = 0x0604
GL_PASS_THROUGH_TOKEN = 0x0700
GL_POINT_TOKEN = 0x0701
GL_LINE_TOKEN = 0x0702
GL_POLYGON_TOKEN = 0x0703
GL_BITMAP_TOKEN = 0x0704
GL_DRAW_PIXEL_TOKEN = 0x0705
GL_COPY_PIXEL_TOKEN = 0x0706
GL_LINE_RESET_TOKEN = 0x0707
GL_EXP = 0x0800
GL_EXP2 = 0x0801
GL_COEFF = 0x0A00
GL_ORDER = 0x0A01
GL_DOMAIN = 0x0A02
GL_PIXEL_MAP_I_TO_I = 0x0C70
GL_PIXEL_MAP_S_TO_S = 0x0C71
GL_PIXEL_MAP_I_TO_R = 0x0C72
GL_PIXEL_MAP_I_TO_G = 0x0C73
GL_PIXEL_MAP_I_TO_B = 0x0C74
GL_PIXEL_MAP_I_TO_A = 0x0C75
GL_PIXEL_MAP_R_TO_R = 0x0C76
GL_PIXEL_MAP_G_TO_G = 0x0C77
GL_PIXEL_MAP_B_TO_B = 0x0C78
GL_PIXEL_MAP_A_TO_A = 0x0C79
GL_VERTEX_ARRAY_POINTER = 0x808E
GL_NORMAL_ARRAY_POINTER = 0x808F
GL_COLOR_ARRAY_POINTER = 0x8090
GL_INDEX_ARRAY_POINTER = 0x8091
GL_TEXTURE_COORD_ARRAY_POINTER = 0x8092
GL_EDGE_FLAG_ARRAY_POINTER = 0x8093
GL_FEEDBACK_BUFFER_POINTER = 0x0DF0
GL_SELECTION_BUFFER_POINTER = 0x0DF3
GL_CURRENT_COLOR = 0x0B00
GL_CURRENT_INDEX = 0x0B01
GL_CURRENT_NORMAL = 0x0B02
GL_CURRENT_TEXTURE_COORDS = 0x0B03
GL_CURRENT_RASTER_COLOR = 0x0B04
GL_CURRENT_RASTER_INDEX = 0x0B05
GL_CURRENT_RASTER_TEXTURE_COORDS = 0x0B06
GL_CURRENT_RASTER_POSITION = 0x0B07
GL_CURRENT_RASTER_POSITION_VALID = 0x0B08
GL_CURRENT_RASTER_DISTANCE = 0x0B09
GL_POINT_SMOOTH = 0x0B10
GL_LINE_STIPPLE = 0x0B24
GL_LINE_STIPPLE_PATTERN = 0x0B25
GL_LINE_STIPPLE_REPEAT = 0x0B26
GL_LIST_MODE = 0x0B30
GL_MAX_LIST_NESTING = 0x0B31
GL_LIST_BASE = 0x0B32
GL_LIST_INDEX = 0x0B33
GL_POLYGON_MODE = 0x0B40
GL_POLYGON_STIPPLE = 0x0B42
GL_EDGE_FLAG = 0x0B43
GL_LIGHTING = 0x0B50
GL_LIGHT_MODEL_LOCAL_VIEWER = 0x0B51
GL_LIGHT_MODEL_TWO_SIDE = 0x0B52
GL_LIGHT_MODEL_AMBIENT = 0x0B53
GL_SHADE_MODEL = 0x0B54
GL_COLOR_MATERIAL_FACE = 0x0B55
GL_COLOR_MATERIAL_PARAMETER = 0x0B56
GL_COLOR_MATERIAL = 0x0B57
GL_FOG = 0x0B60
GL_FOG_INDEX = 0x0B61
GL_FOG_DENSITY = 0x0B62
GL_FOG_START = 0x0B63
GL_FOG_END = 0x0B64
GL_FOG_MODE = 0x0B65
GL_FOG_COLOR = 0x0B66
GL_ACCUM_CLEAR_VALUE = 0x0B80
GL_MATRIX_MODE = 0x0BA0
GL_NORMALIZE = 0x0BA1
GL_MODELVIEW_STACK_DEPTH = 0x0BA3
GL_PROJECTION_STACK_DEPTH = 0x0BA4
GL_TEXTURE_STACK_DEPTH = 0x0BA5
GL_MODELVIEW_MATRIX = 0x0BA6
GL_PROJECTION_MATRIX = 0x0BA7
GL_TEXTURE_MATRIX = 0x0BA8
GL_ATTRIB_STACK_DEPTH = 0x0BB0
GL_CLIENT_ATTRIB_STACK_DEPTH = 0x0BB1
GL_ALPHA_TEST = 0x0BC0
GL_ALPHA_TEST_FUNC = 0x0BC1
GL_ALPHA_TEST_REF = 0x0BC2
GL_INDEX_LOGIC_OP = 0x0BF1
GL_LOGIC_OP = 0x0BF1
GL_AUX_BUFFERS = 0x0C00
GL_INDEX_CLEAR_VALUE = 0x0C20
GL_INDEX_WRITEMASK = 0x0C21
GL_INDEX_MODE = 0x0C30
GL_RGBA_MODE = 0x0C31
GL_RENDER_MODE = 0x0C40
GL_PERSPECTIVE_CORRECTION_HINT = 0x0C50
GL_POINT_SMOOTH_HINT = 0x0C51
GL_FOG_HINT = 0x0C54
GL_TEXTURE_GEN_S = 0x0C60
GL_TEXTURE_GEN_T = 0x0C61
GL_TEXTURE_GEN_R = 0x0C62
GL_TEXTURE_GEN_Q = 0x0C63
GL_PIXEL_MAP_I_TO_I_SIZE = 0x0CB0
GL_PIXEL_MAP_S_TO_S_SIZE = 0x0CB1
GL_PIXEL_MAP_I_TO_R_SIZE = 0x0CB2
GL_PIXEL_MAP_I_TO_G_SIZE = 0x0CB3
GL_PIXEL_MAP_I_TO_B_SIZE = 0x0CB4
GL_PIXEL_MAP_I_TO_A_SIZE = 0x0CB5
GL_PIXEL_MAP_R_TO_R_SIZE = 0x0CB6
GL_PIXEL_MAP_G_TO_G_SIZE = 0x0CB7
GL_PIXEL_MAP_B_TO_B_SIZE = 0x0CB8
GL_PIXEL_MAP_A_TO_A_SIZE = 0x0CB9
GL_MAP_COLOR = 0x0D10
GL_MAP_STENCIL = 0x0D11
GL_INDEX_SHIFT = 0x0D12
GL_INDEX_OFFSET = 0x0D13
GL_RED_SCALE = 0x0D14
GL_RED_BIAS = 0x0D15
GL_ZOOM_X = 0x0D16
GL_ZOOM_Y = 0x0D17
GL_GREEN_SCALE = 0x0D18
GL_GREEN_BIAS = 0x0D19
GL_BLUE_SCALE = 0x0D1A
GL_BLUE_BIAS = 0x0D1B
GL_ALPHA_SCALE = 0x0D1C
GL_ALPHA_BIAS = 0x0D1D
GL_DEPTH_SCALE = 0x0D1E
GL_DEPTH_BIAS = 0x0D1F
GL_MAX_EVAL_ORDER = 0x0D30
GL_MAX_LIGHTS = 0x0D31
GL_MAX_CLIP_PLANES = 0x0D32
GL_MAX_PIXEL_MAP_TABLE = 0x0D34
GL_MAX_ATTRIB_STACK_DEPTH = 0x0D35
GL_MAX_MODELVIEW_STACK_DEPTH = 0x0D36
GL_MAX_NAME_STACK_DEPTH = 0x0D37
GL_MAX_PROJECTION_STACK_DEPTH = 0x0D38
GL_MAX_TEXTURE_STACK_DEPTH = 0x0D39
GL_MAX_CLIENT_ATTRIB_STACK_DEPTH = 0x0D3B
GL_INDEX_BITS = 0x0D51
GL_RED_BITS = 0x0D52
GL_GREEN_BITS = 0x0D53
GL_BLUE_BITS = 0x0D54
GL_ALPHA_BITS = 0x0D55
GL_DEPTH_BITS = 0x0D56
GL_STENCIL_BITS = 0x0D57
GL_ACCUM_RED_BITS = 0x0D58
GL_ACCUM_GREEN_BITS = 0x0D59
GL_ACCUM_BLUE_BITS = 0x0D5A
GL_ACCUM_ALPHA_BITS = 0x0D5B
GL_NAME_STACK_DEPTH = 0x0D70
GL_AUTO_NORMAL = 0x0D80
GL_MAP1_COLOR_4 = 0x0D90
GL_MAP1_INDEX = 0x0D91
GL_MAP1_NORMAL = 0x0D92
GL_MAP1_TEXTURE_COORD_1 = 0x0D93
GL_MAP1_TEXTURE_COORD_2 = 0x0D94
GL_MAP1_TEXTURE_COORD_3 = 0x0D95
GL_MAP1_TEXTURE_COORD_4 = 0x0D96
GL_MAP1_VERTEX_3 = 0x0D97
GL_MAP1_VERTEX_4 = 0x0D98
GL_MAP2_COLOR_4 = 0x0DB0
GL_MAP2_INDEX = 0x0DB1
GL_MAP2_NORMAL = 0x0DB2
GL_MAP2_TEXTURE_COORD_1 = 0x0DB3
GL_MAP2_TEXTURE_COORD_2 = 0x0DB4
GL_MAP2_TEXTURE_COORD_3 = 0x0DB5
GL_MAP2_TEXTURE_COORD_4 = 0x0DB6
GL_MAP2_VERTEX_3 = 0x0DB7
GL_MAP2_VERTEX_4 = 0x0DB8
GL_MAP1_GRID_DOMAIN = 0x0DD0
GL_MAP1_GRID_SEGMENTS = 0x0DD1
GL_MAP2_GRID_DOMAIN = 0x0DD2
GL_MAP2_GRID_SEGMENTS = 0x0DD3
GL_FEEDBACK_BUFFER_SIZE = 0x0DF1
GL_FEEDBACK_BUFFER_TYPE = 0x0DF2
GL_SELECTION_BUFFER_SIZE = 0x0DF4
GL_VERTEX_ARRAY = 0x8074
GL_NORMAL_ARRAY = 0x8075
GL_COLOR_ARRAY = 0x8076
GL_INDEX_ARRAY = 0x8077
GL_TEXTURE_COORD_ARRAY = 0x8078
GL_EDGE_FLAG_ARRAY = 0x8079
GL_VERTEX_ARRAY_SIZE = 0x807A
GL_VERTEX_ARRAY_TYPE = 0x807B
GL_VERTEX_ARRAY_STRIDE = 0x807C
GL_NORMAL_ARRAY_TYPE = 0x807E
GL_NORMAL_ARRAY_STRIDE = 0x807F
GL_COLOR_ARRAY_SIZE = 0x8081
GL_COLOR_ARRAY_TYPE = 0x8082
GL_COLOR_ARRAY_STRIDE = 0x8083
GL_INDEX_ARRAY_TYPE = 0x8085
GL_INDEX_ARRAY_STRIDE = 0x8086
GL_TEXTURE_COORD_ARRAY_SIZE = 0x8088
GL_TEXTURE_COORD_ARRAY_TYPE = 0x8089
GL_TEXTURE_COORD_ARRAY_STRIDE = 0x808A
GL_EDGE_FLAG_ARRAY_STRIDE = 0x808C
GL_TEXTURE_COMPONENTS = 0x1003
GL_TEXTURE_BORDER = 0x1005
GL_TEXTURE_LUMINANCE_SIZE = 0x8060
GL_TEXTURE_INTENSITY_SIZE = 0x8061
GL_TEXTURE_PRIORITY = 0x8066
GL_TEXTURE_RESIDENT = 0x8067
GL_AMBIENT = 0x1200
GL_DIFFUSE = 0x1201
GL_SPECULAR = 0x1202
GL_POSITION = 0x1203
GL_SPOT_DIRECTION = 0x1204
GL_SPOT_EXPONENT = 0x1205
GL_SPOT_CUTOFF = 0x1206
GL_CONSTANT_ATTENUATION = 0x1207
GL_LINEAR_ATTENUATION = 0x1208
GL_QUADRATIC_ATTENUATION = 0x1209
GL_COMPILE = 0x1300
GL_COMPILE_AND_EXECUTE = 0x1301
GL_2_BYTES = 0x1407
GL_3_BYTES = 0x1408
GL_4_BYTES = 0x1409
GL_EMISSION = 0x1600
GL_SHININESS = 0x1601
GL_AMBIENT_AND_DIFFUSE = 0x1602
GL_COLOR_INDEXES = 0x1603
GL_MODELVIEW = 0x1700
GL_PROJECTION = 0x1701
GL_COLOR_INDEX = 0x1900
GL_LUMINANCE = 0x1909
GL_LUMINANCE_ALPHA = 0x190A
GL_BITMAP = 0x1A00
GL_RENDER = 0x1C00
GL_FEEDBACK = 0x1C01
GL_SELECT = 0x1C02
GL_FLAT = 0x1D00
GL_SMOOTH = 0x1D01
GL_S = 0x2000
GL_T = 0x2001
GL_R = 0x2002
GL_Q = 0x2003
GL_MODULATE = 0x2100
GL_DECAL = 0x2101
GL_TEXTURE_ENV_MODE = 0x2200
GL_TEXTURE_ENV_COLOR = 0x2201
GL_TEXTURE_ENV = 0x2300
GL_EYE_LINEAR = 0x2400
GL_OBJECT_LINEAR = 0x2401
GL_SPHERE_MAP = 0x2402
GL_TEXTURE_GEN_MODE = 0x2500
GL_OBJECT_PLANE = 0x2501
GL_EYE_PLANE = 0x2502
GL_CLAMP = 0x2900
GL_ALPHA4 = 0x803B
GL_ALPHA8 = 0x803C
GL_ALPHA12 = 0x803D
GL_ALPHA16 = 0x803E
GL_LUMINANCE4 = 0x803F
GL_LUMINANCE8 = 0x8040
GL_LUMINANCE12 = 0x8041
GL_LUMINANCE16 = 0x8042
GL_LUMINANCE4_ALPHA4 = 0x8043
GL_LUMINANCE6_ALPHA2 = 0x8044
GL_LUMINANCE8_ALPHA8 = 0x8045
GL_LUMINANCE12_ALPHA4 = 0x8046
GL_LUMINANCE12_ALPHA12 = 0x8047
GL_LUMINANCE16_ALPHA16 = 0x8048
GL_INTENSITY = 0x8049
GL_INTENSITY4 = 0x804A
GL_INTENSITY8 = 0x804B
GL_INTENSITY12 = 0x804C
GL_INTENSITY16 = 0x804D
GL_V2F = 0x2A20
GL_V3F = 0x2A21
GL_C4UB_V2F = 0x2A22
GL_C4UB_V3F = 0x2A23
GL_C3F_V3F = 0x2A24
GL_N3F_V3F = 0x2A25
GL_C4F_N3F_V3F = 0x2A26
GL_T2F_V3F = 0x2A27
GL_T4F_V4F = 0x2A28
GL_T2F_C4UB_V3F = 0x2A29
GL_T2F_C3F_V3F = 0x2A2A
GL_T2F_N3F_V3F = 0x2A2B
GL_T2F_C4F_N3F_V3F = 0x2A2C
GL_T4F_C4F_N3F_V4F = 0x2A2D
GL_CLIP_PLANE0 = 0x3000
GL_CLIP_PLANE1 = 0x3001
GL_CLIP_PLANE2 = 0x3002
GL_CLIP_PLANE3 = 0x3003
GL_CLIP_PLANE4 = 0x3004
GL_CLIP_PLANE5 = 0x3005
GL_LIGHT0 = 0x4000
GL_LIGHT1 = 0x4001
GL_LIGHT2 = 0x4002
GL_LIGHT3 = 0x4003
GL_LIGHT4 = 0x4004
GL_LIGHT5 = 0x4005
GL_LIGHT6 = 0x4006
GL_LIGHT7 = 0x4007
# VERSION_1_2
GL_UNSIGNED_BYTE_3_3_2 = 0x8032
GL_UNSIGNED_SHORT_4_4_4_4 = 0x8033
GL_UNSIGNED_SHORT_5_5_5_1 = 0x8034
GL_UNSIGNED_INT_8_8_8_8 = 0x8035
GL_UNSIGNED_INT_10_10_10_2 = 0x8036
GL_TEXTURE_BINDING_3D = 0x806A
GL_PACK_SKIP_IMAGES = 0x806B
GL_PACK_IMAGE_HEIGHT = 0x806C
GL_UNPACK_SKIP_IMAGES = 0x806D
GL_UNPACK_IMAGE_HEIGHT = 0x806E
GL_TEXTURE_3D = 0x806F
GL_PROXY_TEXTURE_3D = 0x8070
GL_TEXTURE_DEPTH = 0x8071
GL_TEXTURE_WRAP_R = 0x8072
GL_MAX_3D_TEXTURE_SIZE = 0x8073
GL_UNSIGNED_BYTE_2_3_3_REV = 0x8362
GL_UNSIGNED_SHORT_5_6_5 = 0x8363
GL_UNSIGNED_SHORT_5_6_5_REV = 0x8364
GL_UNSIGNED_SHORT_4_4_4_4_REV = 0x8365
GL_UNSIGNED_SHORT_1_5_5_5_REV = 0x8366
GL_UNSIGNED_INT_8_8_8_8_REV = 0x8367
GL_UNSIGNED_INT_2_10_10_10_REV = 0x8368
GL_BGR = 0x80E0
GL_BGRA = 0x80E1
GL_MAX_ELEMENTS_VERTICES = 0x80E8
GL_MAX_ELEMENTS_INDICES = 0x80E9
GL_CLAMP_TO_EDGE = 0x812F
GL_TEXTURE_MIN_LOD = 0x813A
GL_TEXTURE_MAX_LOD = 0x813B
GL_TEXTURE_BASE_LEVEL = 0x813C
GL_TEXTURE_MAX_LEVEL = 0x813D
GL_SMOOTH_POINT_SIZE_RANGE = 0x0B12
GL_SMOOTH_POINT_SIZE_GRANULARITY = 0x0B13
GL_SMOOTH_LINE_WIDTH_RANGE = 0x0B22
GL_SMOOTH_LINE_WIDTH_GRANULARITY = 0x0B23
GL_ALIASED_LINE_WIDTH_RANGE = 0x846E
# VERSION_1_2_DEPRECATED
GL_RESCALE_NORMAL = 0x803A
GL_LIGHT_MODEL_COLOR_CONTROL = 0x81F8
GL_SINGLE_COLOR = 0x81F9
GL_SEPARATE_SPECULAR_COLOR = 0x81FA
GL_ALIASED_POINT_SIZE_RANGE = 0x846D
# VERSION_1_3
GL_TEXTURE0 = 0x84C0
GL_TEXTURE1 = 0x84C1
GL_TEXTURE2 = 0x84C2
GL_TEXTURE3 = 0x84C3
GL_TEXTURE4 = 0x84C4
GL_TEXTURE5 = 0x84C5
GL_TEXTURE6 = 0x84C6
GL_TEXTURE7 = 0x84C7
GL_TEXTURE8 = 0x84C8
GL_TEXTURE9 = 0x84C9
GL_TEXTURE10 = 0x84CA
GL_TEXTURE11 = 0x84CB
GL_TEXTURE12 = 0x84CC
GL_TEXTURE13 = 0x84CD
GL_TEXTURE14 = 0x84CE
GL_TEXTURE15 = 0x84CF
GL_TEXTURE16 = 0x84D0
GL_TEXTURE17 = 0x84D1
GL_TEXTURE18 = 0x84D2
GL_TEXTURE19 = 0x84D3
GL_TEXTURE20 = 0x84D4
GL_TEXTURE21 = 0x84D5
GL_TEXTURE22 = 0x84D6
GL_TEXTURE23 = 0x84D7
GL_TEXTURE24 = 0x84D8
GL_TEXTURE25 = 0x84D9
GL_TEXTURE26 = 0x84DA
GL_TEXTURE27 = 0x84DB
GL_TEXTURE28 = 0x84DC
GL_TEXTURE29 = 0x84DD
GL_TEXTURE30 = 0x84DE
GL_TEXTURE31 = 0x84DF
GL_ACTIVE_TEXTURE = 0x84E0
GL_MULTISAMPLE = 0x809D
GL_SAMPLE_ALPHA_TO_COVERAGE = 0x809E
GL_SAMPLE_ALPHA_TO_ONE = 0x809F
GL_SAMPLE_COVERAGE = 0x80A0
GL_SAMPLE_BUFFERS = 0x80A8
GL_SAMPLES = 0x80A9
GL_SAMPLE_COVERAGE_VALUE = 0x80AA
GL_SAMPLE_COVERAGE_INVERT = 0x80AB
GL_TEXTURE_CUBE_MAP = 0x8513
GL_TEXTURE_BINDING_CUBE_MAP = 0x8514
GL_TEXTURE_CUBE_MAP_POSITIVE_X = 0x8515
GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 0x8516
GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 0x8517
GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x8518
GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 0x8519
GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x851A
GL_PROXY_TEXTURE_CUBE_MAP = 0x851B
GL_MAX_CUBE_MAP_TEXTURE_SIZE = 0x851C
GL_COMPRESSED_RGB = 0x84ED
GL_COMPRESSED_RGBA = 0x84EE
GL_TEXTURE_COMPRESSION_HINT = 0x84EF
GL_TEXTURE_COMPRESSED_IMAGE_SIZE = 0x86A0
GL_TEXTURE_COMPRESSED = 0x86A1
GL_NUM_COMPRESSED_TEXTURE_FORMATS = 0x86A2
GL_COMPRESSED_TEXTURE_FORMATS = 0x86A3
GL_CLAMP_TO_BORDER = 0x812D
# VERSION_1_3_DEPRECATED
GL_CLIENT_ACTIVE_TEXTURE = 0x84E1
GL_MAX_TEXTURE_UNITS = 0x84E2
GL_TRANSPOSE_MODELVIEW_MATRIX = 0x84E3
GL_TRANSPOSE_PROJECTION_MATRIX = 0x84E4
GL_TRANSPOSE_TEXTURE_MATRIX = 0x84E5
GL_TRANSPOSE_COLOR_MATRIX = 0x84E6
GL_MULTISAMPLE_BIT = 0x20000000
GL_NORMAL_MAP = 0x8511
GL_REFLECTION_MAP = 0x8512
GL_COMPRESSED_ALPHA = 0x84E9
GL_COMPRESSED_LUMINANCE = 0x84EA
GL_COMPRESSED_LUMINANCE_ALPHA = 0x84EB
GL_COMPRESSED_INTENSITY = 0x84EC
GL_COMBINE = 0x8570
GL_COMBINE_RGB = 0x8571
GL_COMBINE_ALPHA = 0x8572
GL_SOURCE0_RGB = 0x8580
GL_SOURCE1_RGB = 0x8581
GL_SOURCE2_RGB = 0x8582
GL_SOURCE0_ALPHA = 0x8588
GL_SOURCE1_ALPHA = 0x8589
GL_SOURCE2_ALPHA = 0x858A
GL_OPERAND0_RGB = 0x8590
GL_OPERAND1_RGB = 0x8591
GL_OPERAND2_RGB = 0x8592
GL_OPERAND0_ALPHA = 0x8598
GL_OPERAND1_ALPHA = 0x8599
GL_OPERAND2_ALPHA = 0x859A
GL_RGB_SCALE = 0x8573
GL_ADD_SIGNED = 0x8574
GL_INTERPOLATE = 0x8575
GL_SUBTRACT = 0x84E7
GL_CONSTANT = 0x8576
GL_PRIMARY_COLOR = 0x8577
GL_PREVIOUS = 0x8578
GL_DOT3_RGB = 0x86AE
GL_DOT3_RGBA = 0x86AF
# VERSION_1_4
GL_BLEND_DST_RGB = 0x80C8
GL_BLEND_SRC_RGB = 0x80C9
GL_BLEND_DST_ALPHA = 0x80CA
GL_BLEND_SRC_ALPHA = 0x80CB
GL_POINT_FADE_THRESHOLD_SIZE = 0x8128
GL_DEPTH_COMPONENT16 = 0x81A5
GL_DEPTH_COMPONENT24 = 0x81A6
GL_DEPTH_COMPONENT32 = 0x81A7
GL_MIRRORED_REPEAT = 0x8370
GL_MAX_TEXTURE_LOD_BIAS = 0x84FD
GL_TEXTURE_LOD_BIAS = 0x8501
GL_INCR_WRAP = 0x8507
GL_DECR_WRAP = 0x8508
GL_TEXTURE_DEPTH_SIZE = 0x884A
GL_TEXTURE_COMPARE_MODE = 0x884C
GL_TEXTURE_COMPARE_FUNC = 0x884D
# VERSION_1_4_DEPRECATED
GL_POINT_SIZE_MIN = 0x8126
GL_POINT_SIZE_MAX = 0x8127
GL_POINT_DISTANCE_ATTENUATION = 0x8129
GL_GENERATE_MIPMAP = 0x8191
GL_GENERATE_MIPMAP_HINT = 0x8192
GL_FOG_COORDINATE_SOURCE = 0x8450
GL_FOG_COORDINATE = 0x8451
GL_FRAGMENT_DEPTH = 0x8452
GL_CURRENT_FOG_COORDINATE = 0x8453
GL_FOG_COORDINATE_ARRAY_TYPE = 0x8454
GL_FOG_COORDINATE_ARRAY_STRIDE = 0x8455
GL_FOG_COORDINATE_ARRAY_POINTER = 0x8456
GL_FOG_COORDINATE_ARRAY = 0x8457
GL_COLOR_SUM = 0x8458
GL_CURRENT_SECONDARY_COLOR = 0x8459
GL_SECONDARY_COLOR_ARRAY_SIZE = 0x845A
GL_SECONDARY_COLOR_ARRAY_TYPE = 0x845B
GL_SECONDARY_COLOR_ARRAY_STRIDE = 0x845C
GL_SECONDARY_COLOR_ARRAY_POINTER = 0x845D
GL_SECONDARY_COLOR_ARRAY = 0x845E
GL_TEXTURE_FILTER_CONTROL = 0x8500
GL_DEPTH_TEXTURE_MODE = 0x884B
GL_COMPARE_R_TO_TEXTURE = 0x884E
# VERSION_1_5
GL_BUFFER_SIZE = 0x8764
GL_BUFFER_USAGE = 0x8765
GL_QUERY_COUNTER_BITS = 0x8864
GL_CURRENT_QUERY = 0x8865
GL_QUERY_RESULT = 0x8866
GL_QUERY_RESULT_AVAILABLE = 0x8867
GL_ARRAY_BUFFER = 0x8892
GL_ELEMENT_ARRAY_BUFFER = 0x8893
GL_ARRAY_BUFFER_BINDING = 0x8894
GL_ELEMENT_ARRAY_BUFFER_BINDING = 0x8895
GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x889F
GL_READ_ONLY = 0x88B8
GL_WRITE_ONLY = 0x88B9
GL_READ_WRITE = 0x88BA
GL_BUFFER_ACCESS = 0x88BB
GL_BUFFER_MAPPED = 0x88BC
GL_BUFFER_MAP_POINTER = 0x88BD
GL_STREAM_DRAW = 0x88E0
GL_STREAM_READ = 0x88E1
GL_STREAM_COPY = 0x88E2
GL_STATIC_DRAW = 0x88E4
GL_STATIC_READ = 0x88E5
GL_STATIC_COPY = 0x88E6
GL_DYNAMIC_DRAW = 0x88E8
GL_DYNAMIC_READ = 0x88E9
GL_DYNAMIC_COPY = 0x88EA
GL_SAMPLES_PASSED = 0x8914
# VERSION_1_5_DEPRECATED
GL_VERTEX_ARRAY_BUFFER_BINDING = 0x8896
GL_NORMAL_ARRAY_BUFFER_BINDING = 0x8897
GL_COLOR_ARRAY_BUFFER_BINDING = 0x8898
GL_INDEX_ARRAY_BUFFER_BINDING = 0x8899
GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING = 0x889A
GL_EDGE_FLAG_ARRAY_BUFFER_BINDING = 0x889B
GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING = 0x889C
GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING = 0x889D
GL_WEIGHT_ARRAY_BUFFER_BINDING = 0x889E
GL_FOG_COORD_SRC = 0x8450
GL_FOG_COORD = 0x8451
GL_CURRENT_FOG_COORD = 0x8453
GL_FOG_COORD_ARRAY_TYPE = 0x8454
GL_FOG_COORD_ARRAY_STRIDE = 0x8455
GL_FOG_COORD_ARRAY_POINTER = 0x8456
GL_FOG_COORD_ARRAY = 0x8457
GL_FOG_COORD_ARRAY_BUFFER_BINDING = 0x889D
GL_SRC0_RGB = 0x8580
GL_SRC1_RGB = 0x8581
GL_SRC2_RGB = 0x8582
GL_SRC0_ALPHA = 0x8588
GL_SRC1_ALPHA = 0x8589
GL_SRC2_ALPHA = 0x858A
# VERSION_2_0
GL_BLEND_EQUATION_RGB = 0x8009
GL_VERTEX_ATTRIB_ARRAY_ENABLED = 0x8622
GL_VERTEX_ATTRIB_ARRAY_SIZE = 0x8623
GL_VERTEX_ATTRIB_ARRAY_STRIDE = 0x8624
GL_VERTEX_ATTRIB_ARRAY_TYPE = 0x8625
GL_CURRENT_VERTEX_ATTRIB = 0x8626
GL_VERTEX_PROGRAM_POINT_SIZE = 0x8642
GL_VERTEX_ATTRIB_ARRAY_POINTER = 0x8645
GL_STENCIL_BACK_FUNC = 0x8800
GL_STENCIL_BACK_FAIL = 0x8801
GL_STENCIL_BACK_PASS_DEPTH_FAIL = 0x8802
GL_STENCIL_BACK_PASS_DEPTH_PASS = 0x8803
GL_MAX_DRAW_BUFFERS = 0x8824
GL_DRAW_BUFFER0 = 0x8825
GL_DRAW_BUFFER1 = 0x8826
GL_DRAW_BUFFER2 = 0x8827
GL_DRAW_BUFFER3 = 0x8828
GL_DRAW_BUFFER4 = 0x8829
GL_DRAW_BUFFER5 = 0x882A
GL_DRAW_BUFFER6 = 0x882B
GL_DRAW_BUFFER7 = 0x882C
GL_DRAW_BUFFER8 = 0x882D
GL_DRAW_BUFFER9 = 0x882E
GL_DRAW_BUFFER10 = 0x882F
GL_DRAW_BUFFER11 = 0x8830
GL_DRAW_BUFFER12 = 0x8831
GL_DRAW_BUFFER13 = 0x8832
GL_DRAW_BUFFER14 = 0x8833
GL_DRAW_BUFFER15 = 0x8834
GL_BLEND_EQUATION_ALPHA = 0x883D
GL_MAX_VERTEX_ATTRIBS = 0x8869
GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 0x886A
GL_MAX_TEXTURE_IMAGE_UNITS = 0x8872
GL_FRAGMENT_SHADER = 0x8B30
GL_VERTEX_SHADER = 0x8B31
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS = 0x8B49
GL_MAX_VERTEX_UNIFORM_COMPONENTS = 0x8B4A
GL_MAX_VARYING_FLOATS = 0x8B4B
GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 0x8B4C
GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 0x8B4D
GL_SHADER_TYPE = 0x8B4F
GL_FLOAT_VEC2 = 0x8B50
GL_FLOAT_VEC3 = 0x8B51
GL_FLOAT_VEC4 = 0x8B52
GL_INT_VEC2 = 0x8B53
GL_INT_VEC3 = 0x8B54
GL_INT_VEC4 = 0x8B55
GL_BOOL = 0x8B56
GL_BOOL_VEC2 = 0x8B57
GL_BOOL_VEC3 = 0x8B58
GL_BOOL_VEC4 = 0x8B59
GL_FLOAT_MAT2 = 0x8B5A
GL_FLOAT_MAT3 = 0x8B5B
GL_FLOAT_MAT4 = 0x8B5C
GL_SAMPLER_1D = 0x8B5D
GL_SAMPLER_2D = 0x8B5E
GL_SAMPLER_3D = 0x8B5F
GL_SAMPLER_CUBE = 0x8B60
GL_SAMPLER_1D_SHADOW = 0x8B61
GL_SAMPLER_2D_SHADOW = 0x8B62
GL_DELETE_STATUS = 0x8B80
GL_COMPILE_STATUS = 0x8B81
GL_LINK_STATUS = 0x8B82
GL_VALIDATE_STATUS = 0x8B83
GL_INFO_LOG_LENGTH = 0x8B84
GL_ATTACHED_SHADERS = 0x8B85
GL_ACTIVE_UNIFORMS = 0x8B86
GL_ACTIVE_UNIFORM_MAX_LENGTH = 0x8B87
GL_SHADER_SOURCE_LENGTH = 0x8B88
GL_ACTIVE_ATTRIBUTES = 0x8B89
GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 0x8B8A
GL_FRAGMENT_SHADER_DERIVATIVE_HINT = 0x8B8B
GL_SHADING_LANGUAGE_VERSION = 0x8B8C
GL_CURRENT_PROGRAM = 0x8B8D
GL_POINT_SPRITE_COORD_ORIGIN = 0x8CA0
GL_LOWER_LEFT = 0x8CA1
GL_UPPER_LEFT = 0x8CA2
GL_STENCIL_BACK_REF = 0x8CA3
GL_STENCIL_BACK_VALUE_MASK = 0x8CA4
GL_STENCIL_BACK_WRITEMASK = 0x8CA5
# VERSION_2_0_DEPRECATED
GL_VERTEX_PROGRAM_TWO_SIDE = 0x8643
GL_POINT_SPRITE = 0x8861
GL_COORD_REPLACE = 0x8862
GL_MAX_TEXTURE_COORDS = 0x8871
# VERSION_2_1
GL_PIXEL_PACK_BUFFER = 0x88EB
GL_PIXEL_UNPACK_BUFFER = 0x88EC
GL_PIXEL_PACK_BUFFER_BINDING = 0x88ED
GL_PIXEL_UNPACK_BUFFER_BINDING = 0x88EF
GL_FLOAT_MAT2x3 = 0x8B65
GL_FLOAT_MAT2x4 = 0x8B66
GL_FLOAT_MAT3x2 = 0x8B67
GL_FLOAT_MAT3x4 = 0x8B68
GL_FLOAT_MAT4x2 = 0x8B69
GL_FLOAT_MAT4x3 = 0x8B6A
GL_SRGB = 0x8C40
GL_SRGB8 = 0x8C41
GL_SRGB_ALPHA = 0x8C42
GL_SRGB8_ALPHA8 = 0x8C43
GL_COMPRESSED_SRGB = 0x8C48
GL_COMPRESSED_SRGB_ALPHA = 0x8C49
# VERSION_2_1_DEPRECATED
GL_CURRENT_RASTER_SECONDARY_COLOR = 0x845F
GL_SLUMINANCE_ALPHA = 0x8C44
GL_SLUMINANCE8_ALPHA8 = 0x8C45
GL_SLUMINANCE = 0x8C46
GL_SLUMINANCE8 = 0x8C47
GL_COMPRESSED_SLUMINANCE = 0x8C4A
GL_COMPRESSED_SLUMINANCE_ALPHA = 0x8C4B
# VERSION_3_0
GL_COMPARE_REF_TO_TEXTURE = 0x884E
GL_CLIP_DISTANCE0 = 0x3000
GL_CLIP_DISTANCE1 = 0x3001
GL_CLIP_DISTANCE2 = 0x3002
GL_CLIP_DISTANCE3 = 0x3003
GL_CLIP_DISTANCE4 = 0x3004
GL_CLIP_DISTANCE5 = 0x3005
GL_CLIP_DISTANCE6 = 0x3006
GL_CLIP_DISTANCE7 = 0x3007
GL_MAX_CLIP_DISTANCES = 0x0D32
GL_MAJOR_VERSION = 0x821B
GL_MINOR_VERSION = 0x821C
GL_NUM_EXTENSIONS = 0x821D
GL_CONTEXT_FLAGS = 0x821E
GL_COMPRESSED_RED = 0x8225
GL_COMPRESSED_RG = 0x8226
GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT = 0x0001
GL_RGBA32F = 0x8814
GL_RGB32F = 0x8815
GL_RGBA16F = 0x881A
GL_RGB16F = 0x881B
GL_VERTEX_ATTRIB_ARRAY_INTEGER = 0x88FD
GL_MAX_ARRAY_TEXTURE_LAYERS = 0x88FF
GL_MIN_PROGRAM_TEXEL_OFFSET = 0x8904
GL_MAX_PROGRAM_TEXEL_OFFSET = 0x8905
GL_CLAMP_READ_COLOR = 0x891C
GL_FIXED_ONLY = 0x891D
GL_MAX_VARYING_COMPONENTS = 0x8B4B
GL_TEXTURE_1D_ARRAY = 0x8C18
GL_PROXY_TEXTURE_1D_ARRAY = 0x8C19
GL_TEXTURE_2D_ARRAY = 0x8C1A
GL_PROXY_TEXTURE_2D_ARRAY = 0x8C1B
GL_TEXTURE_BINDING_1D_ARRAY = 0x8C1C
GL_TEXTURE_BINDING_2D_ARRAY = 0x8C1D
GL_R11F_G11F_B10F = 0x8C3A
GL_UNSIGNED_INT_10F_11F_11F_REV = 0x8C3B
GL_RGB9_E5 = 0x8C3D
GL_UNSIGNED_INT_5_9_9_9_REV = 0x8C3E
GL_TEXTURE_SHARED_SIZE = 0x8C3F
GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH = 0x8C76
GL_TRANSFORM_FEEDBACK_BUFFER_MODE = 0x8C7F
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS = 0x8C80
GL_TRANSFORM_FEEDBACK_VARYINGS = 0x8C83
GL_TRANSFORM_FEEDBACK_BUFFER_START = 0x8C84
GL_TRANSFORM_FEEDBACK_BUFFER_SIZE = 0x8C85
GL_PRIMITIVES_GENERATED = 0x8C87
GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = 0x8C88
GL_RASTERIZER_DISCARD = 0x8C89
GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS = 0x8C8A
GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS = 0x8C8B
GL_INTERLEAVED_ATTRIBS = 0x8C8C
GL_SEPARATE_ATTRIBS = 0x8C8D
GL_TRANSFORM_FEEDBACK_BUFFER = 0x8C8E
GL_TRANSFORM_FEEDBACK_BUFFER_BINDING = 0x8C8F
GL_RGBA32UI = 0x8D70
GL_RGB32UI = 0x8D71
GL_RGBA16UI = 0x8D76
GL_RGB16UI = 0x8D77
GL_RGBA8UI = 0x8D7C
GL_RGB8UI = 0x8D7D
GL_RGBA32I = 0x8D82
GL_RGB32I = 0x8D83
GL_RGBA16I = 0x8D88
GL_RGB16I = 0x8D89
GL_RGBA8I = 0x8D8E
GL_RGB8I = 0x8D8F
GL_RED_INTEGER = 0x8D94
GL_GREEN_INTEGER = 0x8D95
GL_BLUE_INTEGER = 0x8D96
GL_RGB_INTEGER = 0x8D98
GL_RGBA_INTEGER = 0x8D99
GL_BGR_INTEGER = 0x8D9A
GL_BGRA_INTEGER = 0x8D9B
GL_SAMPLER_1D_ARRAY = 0x8DC0
GL_SAMPLER_2D_ARRAY = 0x8DC1
GL_SAMPLER_1D_ARRAY_SHADOW = 0x8DC3
GL_SAMPLER_2D_ARRAY_SHADOW = 0x8DC4
GL_SAMPLER_CUBE_SHADOW = 0x8DC5
GL_UNSIGNED_INT_VEC2 = 0x8DC6
GL_UNSIGNED_INT_VEC3 = 0x8DC7
GL_UNSIGNED_INT_VEC4 = 0x8DC8
GL_INT_SAMPLER_1D = 0x8DC9
GL_INT_SAMPLER_2D = 0x8DCA
GL_INT_SAMPLER_3D = 0x8DCB
GL_INT_SAMPLER_CUBE = 0x8DCC
GL_INT_SAMPLER_1D_ARRAY = 0x8DCE
GL_INT_SAMPLER_2D_ARRAY = 0x8DCF
GL_UNSIGNED_INT_SAMPLER_1D = 0x8DD1
GL_UNSIGNED_INT_SAMPLER_2D = 0x8DD2
GL_UNSIGNED_INT_SAMPLER_3D = 0x8DD3
GL_UNSIGNED_INT_SAMPLER_CUBE = 0x8DD4
GL_UNSIGNED_INT_SAMPLER_1D_ARRAY = 0x8DD6
GL_UNSIGNED_INT_SAMPLER_2D_ARRAY = 0x8DD7
GL_QUERY_WAIT = 0x8E13
GL_QUERY_NO_WAIT = 0x8E14
GL_QUERY_BY_REGION_WAIT = 0x8E15
GL_QUERY_BY_REGION_NO_WAIT = 0x8E16
GL_BUFFER_ACCESS_FLAGS = 0x911F
GL_BUFFER_MAP_LENGTH = 0x9120
GL_BUFFER_MAP_OFFSET = 0x9121
# VERSION_3_0_DEPRECATED
GL_CLAMP_VERTEX_COLOR = 0x891A
GL_CLAMP_FRAGMENT_COLOR = 0x891B
GL_ALPHA_INTEGER = 0x8D97
# VERSION_3_1
GL_SAMPLER_2D_RECT = 0x8B63
GL_SAMPLER_2D_RECT_SHADOW = 0x8B64
GL_SAMPLER_BUFFER = 0x8DC2
GL_INT_SAMPLER_2D_RECT = 0x8DCD
GL_INT_SAMPLER_BUFFER = 0x8DD0
GL_UNSIGNED_INT_SAMPLER_2D_RECT = 0x8DD5
GL_UNSIGNED_INT_SAMPLER_BUFFER = 0x8DD8
GL_TEXTURE_BUFFER = 0x8C2A
GL_MAX_TEXTURE_BUFFER_SIZE = 0x8C2B
GL_TEXTURE_BINDING_BUFFER = 0x8C2C
GL_TEXTURE_BUFFER_DATA_STORE_BINDING = 0x8C2D
GL_TEXTURE_BUFFER_FORMAT = 0x8C2E
GL_TEXTURE_RECTANGLE = 0x84F5
GL_TEXTURE_BINDING_RECTANGLE = 0x84F6
GL_PROXY_TEXTURE_RECTANGLE = 0x84F7
GL_MAX_RECTANGLE_TEXTURE_SIZE = 0x84F8
GL_RED_SNORM = 0x8F90
GL_RG_SNORM = 0x8F91
GL_RGB_SNORM = 0x8F92
GL_RGBA_SNORM = 0x8F93
GL_R8_SNORM = 0x8F94
GL_RG8_SNORM = 0x8F95
GL_RGB8_SNORM = 0x8F96
GL_RGBA8_SNORM = 0x8F97
GL_R16_SNORM = 0x8F98
GL_RG16_SNORM = 0x8F99
GL_RGB16_SNORM = 0x8F9A
GL_RGBA16_SNORM = 0x8F9B
GL_SIGNED_NORMALIZED = 0x8F9C
GL_PRIMITIVE_RESTART = 0x8F9D
GL_PRIMITIVE_RESTART_INDEX = 0x8F9E
# VERSION_3_2
GL_CONTEXT_CORE_PROFILE_BIT = 0x00000001
GL_CONTEXT_COMPATIBILITY_PROFILE_BIT = 0x00000002
GL_LINES_ADJACENCY = 0x000A
GL_LINE_STRIP_ADJACENCY = 0x000B
GL_TRIANGLES_ADJACENCY = 0x000C
GL_TRIANGLE_STRIP_ADJACENCY = 0x000D
GL_PROGRAM_POINT_SIZE = 0x8642
GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS = 0x8C29
GL_FRAMEBUFFER_ATTACHMENT_LAYERED = 0x8DA7
GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS = 0x8DA8
GL_GEOMETRY_SHADER = 0x8DD9
GL_GEOMETRY_VERTICES_OUT = 0x8916
GL_GEOMETRY_INPUT_TYPE = 0x8917
GL_GEOMETRY_OUTPUT_TYPE = 0x8918
GL_MAX_GEOMETRY_UNIFORM_COMPONENTS = 0x8DDF
GL_MAX_GEOMETRY_OUTPUT_VERTICES = 0x8DE0
GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS = 0x8DE1
GL_MAX_VERTEX_OUTPUT_COMPONENTS = 0x9122
GL_MAX_GEOMETRY_INPUT_COMPONENTS = 0x9123
GL_MAX_GEOMETRY_OUTPUT_COMPONENTS = 0x9124
GL_MAX_FRAGMENT_INPUT_COMPONENTS = 0x9125
GL_CONTEXT_PROFILE_MASK = 0x9126
# VERSION_3_3
GL_VERTEX_ATTRIB_ARRAY_DIVISOR = 0x88FE
# VERSION_4_0
GL_SAMPLE_SHADING = 0x8C36
GL_MIN_SAMPLE_SHADING_VALUE = 0x8C37
GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET = 0x8E5E
GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET = 0x8E5F
GL_MAX_PROGRAM_TEXTURE_GATHER_COMPONENTS = 0x8F9F
GL_TEXTURE_CUBE_MAP_ARRAY = 0x9009
GL_TEXTURE_BINDING_CUBE_MAP_ARRAY = 0x900A
GL_PROXY_TEXTURE_CUBE_MAP_ARRAY = 0x900B
GL_SAMPLER_CUBE_MAP_ARRAY = 0x900C
GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW = 0x900D
GL_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900E
GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900F
# VERSION_4_1
# VERSION_4_2
# VERSION_4_3
GL_NUM_SHADING_LANGUAGE_VERSIONS = 0x82E9
GL_VERTEX_ATTRIB_ARRAY_LONG = 0x874E
# WIN_phong_shading
GL_PHONG_WIN = 0x80EA
GL_PHONG_HINT_WIN = 0x80EB
# WIN_specular_fog
GL_FOG_SPECULAR_TEXTURE_WIN = 0x80EC

"""
# 3DL_stereo_control
WGL_STEREO_EMITTER_ENABLE_3DL = 0x2055
WGL_STEREO_EMITTER_DISABLE_3DL = 0x2056
WGL_STEREO_POLARITY_NORMAL_3DL = 0x2057
WGL_STEREO_POLARITY_INVERT_3DL = 0x2058
# AMD_gpu_association
WGL_GPU_VENDOR_AMD = 0x1F00
WGL_GPU_RENDERER_STRING_AMD = 0x1F01
WGL_GPU_OPENGL_VERSION_STRING_AMD = 0x1F02
WGL_GPU_FASTEST_TARGET_GPUS_AMD = 0x21A2
WGL_GPU_RAM_AMD = 0x21A3
WGL_GPU_CLOCK_AMD = 0x21A4
WGL_GPU_NUM_PIPES_AMD = 0x21A5
WGL_GPU_NUM_SIMD_AMD = 0x21A6
WGL_GPU_NUM_RB_AMD = 0x21A7
WGL_GPU_NUM_SPI_AMD = 0x21A8
# ARB_buffer_region
WGL_FRONT_COLOR_BUFFER_BIT_ARB = 0x00000001
WGL_BACK_COLOR_BUFFER_BIT_ARB = 0x00000002
WGL_DEPTH_BUFFER_BIT_ARB = 0x00000004
WGL_STENCIL_BUFFER_BIT_ARB = 0x00000008
# ARB_create_context
WGL_CONTEXT_DEBUG_BIT_ARB = 0x00000001
WGL_CONTEXT_FORWARD_COMPATIBLE_BIT_ARB = 0x00000002
WGL_CONTEXT_MAJOR_VERSION_ARB = 0x2091
WGL_CONTEXT_MINOR_VERSION_ARB = 0x2092
WGL_CONTEXT_LAYER_PLANE_ARB = 0x2093
WGL_CONTEXT_FLAGS_ARB = 0x2094
WGL_ERROR_INVALID_VERSION_ARB = 0x2095
# ARB_create_context_profile
WGL_CONTEXT_PROFILE_MASK_ARB = 0x9126
WGL_CONTEXT_CORE_PROFILE_BIT_ARB = 0x00000001
WGL_CONTEXT_COMPATIBILITY_PROFILE_BIT_ARB = 0x00000002
WGL_ERROR_INVALID_PROFILE_ARB = 0x2096
# ARB_create_context_robustness
WGL_CONTEXT_ROBUST_ACCESS_BIT_ARB = 0x00000004
WGL_LOSE_CONTEXT_ON_RESET_ARB = 0x8252
WGL_CONTEXT_RESET_NOTIFICATION_STRATEGY_ARB = 0x8256
WGL_NO_RESET_NOTIFICATION_ARB = 0x8261
# ARB_extensions_string
# ARB_make_current_read
WGL_ERROR_INVALID_PIXEL_TYPE_ARB = 0x2043
WGL_ERROR_INCOMPATIBLE_DEVICE_CONTEXTS_ARB = 0x2054
# ARB_pbuffer
WGL_DRAW_TO_PBUFFER_ARB = 0x202D
WGL_MAX_PBUFFER_PIXELS_ARB = 0x202E
WGL_MAX_PBUFFER_WIDTH_ARB = 0x202F
WGL_MAX_PBUFFER_HEIGHT_ARB = 0x2030
WGL_PBUFFER_LARGEST_ARB = 0x2033
WGL_PBUFFER_WIDTH_ARB = 0x2034
WGL_PBUFFER_HEIGHT_ARB = 0x2035
WGL_PBUFFER_LOST_ARB = 0x2036
# ARB_pixel_format
WGL_NUMBER_PIXEL_FORMATS_ARB = 0x2000
WGL_DRAW_TO_WINDOW_ARB = 0x2001
WGL_DRAW_TO_BITMAP_ARB = 0x2002
WGL_ACCELERATION_ARB = 0x2003
WGL_NEED_PALETTE_ARB = 0x2004
WGL_NEED_SYSTEM_PALETTE_ARB = 0x2005
WGL_SWAP_LAYER_BUFFERS_ARB = 0x2006
WGL_SWAP_METHOD_ARB = 0x2007
WGL_NUMBER_OVERLAYS_ARB = 0x2008
WGL_NUMBER_UNDERLAYS_ARB = 0x2009
WGL_TRANSPARENT_ARB = 0x200A
WGL_TRANSPARENT_RED_VALUE_ARB = 0x2037
WGL_TRANSPARENT_GREEN_VALUE_ARB = 0x2038
WGL_TRANSPARENT_BLUE_VALUE_ARB = 0x2039
WGL_TRANSPARENT_ALPHA_VALUE_ARB = 0x203A
WGL_TRANSPARENT_INDEX_VALUE_ARB = 0x203B
WGL_SHARE_DEPTH_ARB = 0x200C
WGL_SHARE_STENCIL_ARB = 0x200D
WGL_SHARE_ACCUM_ARB = 0x200E
WGL_SUPPORT_GDI_ARB = 0x200F
WGL_SUPPORT_OPENGL_ARB = 0x2010
WGL_DOUBLE_BUFFER_ARB = 0x2011
WGL_STEREO_ARB = 0x2012
WGL_PIXEL_TYPE_ARB = 0x2013
WGL_COLOR_BITS_ARB = 0x2014
WGL_RED_BITS_ARB = 0x2015
WGL_RED_SHIFT_ARB = 0x2016
WGL_GREEN_BITS_ARB = 0x2017
WGL_GREEN_SHIFT_ARB = 0x2018
WGL_BLUE_BITS_ARB = 0x2019
WGL_BLUE_SHIFT_ARB = 0x201A
WGL_ALPHA_BITS_ARB = 0x201B
WGL_ALPHA_SHIFT_ARB = 0x201C
WGL_ACCUM_BITS_ARB = 0x201D
WGL_ACCUM_RED_BITS_ARB = 0x201E
WGL_ACCUM_GREEN_BITS_ARB = 0x201F
WGL_ACCUM_BLUE_BITS_ARB = 0x2020
WGL_ACCUM_ALPHA_BITS_ARB = 0x2021
WGL_DEPTH_BITS_ARB = 0x2022
WGL_STENCIL_BITS_ARB = 0x2023
WGL_AUX_BUFFERS_ARB = 0x2024
WGL_NO_ACCELERATION_ARB = 0x2025
WGL_GENERIC_ACCELERATION_ARB = 0x2026
WGL_FULL_ACCELERATION_ARB = 0x2027
WGL_SWAP_EXCHANGE_ARB = 0x2028
WGL_SWAP_COPY_ARB = 0x2029
WGL_SWAP_UNDEFINED_ARB = 0x202A
WGL_TYPE_RGBA_ARB = 0x202B
WGL_TYPE_COLORINDEX_ARB = 0x202C
# ARB_pixel_format_float
WGL_TYPE_RGBA_FLOAT_ARB = 0x21A0
# ARB_render_texture
WGL_BIND_TO_TEXTURE_RGB_ARB = 0x2070
WGL_BIND_TO_TEXTURE_RGBA_ARB = 0x2071
WGL_TEXTURE_FORMAT_ARB = 0x2072
WGL_TEXTURE_TARGET_ARB = 0x2073
WGL_MIPMAP_TEXTURE_ARB = 0x2074
WGL_TEXTURE_RGB_ARB = 0x2075
WGL_TEXTURE_RGBA_ARB = 0x2076
WGL_NO_TEXTURE_ARB = 0x2077
WGL_TEXTURE_CUBE_MAP_ARB = 0x2078
WGL_TEXTURE_1D_ARB = 0x2079
WGL_TEXTURE_2D_ARB = 0x207A
WGL_MIPMAP_LEVEL_ARB = 0x207B
WGL_CUBE_MAP_FACE_ARB = 0x207C
WGL_TEXTURE_CUBE_MAP_POSITIVE_X_ARB = 0x207D
WGL_TEXTURE_CUBE_MAP_NEGATIVE_X_ARB = 0x207E
WGL_TEXTURE_CUBE_MAP_POSITIVE_Y_ARB = 0x207F
WGL_TEXTURE_CUBE_MAP_NEGATIVE_Y_ARB = 0x2080
WGL_TEXTURE_CUBE_MAP_POSITIVE_Z_ARB = 0x2081
WGL_TEXTURE_CUBE_MAP_NEGATIVE_Z_ARB = 0x2082
WGL_FRONT_LEFT_ARB = 0x2083
WGL_FRONT_RIGHT_ARB = 0x2084
WGL_BACK_LEFT_ARB = 0x2085
WGL_BACK_RIGHT_ARB = 0x2086
WGL_AUX0_ARB = 0x2087
WGL_AUX1_ARB = 0x2088
WGL_AUX2_ARB = 0x2089
WGL_AUX3_ARB = 0x208A
WGL_AUX4_ARB = 0x208B
WGL_AUX5_ARB = 0x208C
WGL_AUX6_ARB = 0x208D
WGL_AUX7_ARB = 0x208E
WGL_AUX8_ARB = 0x208F
WGL_AUX9_ARB = 0x2090
# EXT_create_context_es2_profile
WGL_CONTEXT_ES2_PROFILE_BIT_EXT = 0x00000004
# EXT_depth_float
WGL_DEPTH_FLOAT_EXT = 0x2040
# EXT_display_color_table
# EXT_extensions_string
# EXT_make_current_read
WGL_ERROR_INVALID_PIXEL_TYPE_EXT = 0x2043
# EXT_pbuffer
WGL_DRAW_TO_PBUFFER_EXT = 0x202D
WGL_MAX_PBUFFER_PIXELS_EXT = 0x202E
WGL_MAX_PBUFFER_WIDTH_EXT = 0x202F
WGL_MAX_PBUFFER_HEIGHT_EXT = 0x2030
WGL_OPTIMAL_PBUFFER_WIDTH_EXT = 0x2031
WGL_OPTIMAL_PBUFFER_HEIGHT_EXT = 0x2032
WGL_PBUFFER_LARGEST_EXT = 0x2033
WGL_PBUFFER_WIDTH_EXT = 0x2034
WGL_PBUFFER_HEIGHT_EXT = 0x2035
# EXT_pixel_format
WGL_NUMBER_PIXEL_FORMATS_EXT = 0x2000
WGL_DRAW_TO_WINDOW_EXT = 0x2001
WGL_DRAW_TO_BITMAP_EXT = 0x2002
WGL_ACCELERATION_EXT = 0x2003
WGL_NEED_PALETTE_EXT = 0x2004
WGL_NEED_SYSTEM_PALETTE_EXT = 0x2005
WGL_SWAP_LAYER_BUFFERS_EXT = 0x2006
WGL_SWAP_METHOD_EXT = 0x2007
WGL_NUMBER_OVERLAYS_EXT = 0x2008
WGL_NUMBER_UNDERLAYS_EXT = 0x2009
WGL_TRANSPARENT_EXT = 0x200A
WGL_TRANSPARENT_VALUE_EXT = 0x200B
WGL_SHARE_DEPTH_EXT = 0x200C
WGL_SHARE_STENCIL_EXT = 0x200D
WGL_SHARE_ACCUM_EXT = 0x200E
WGL_SUPPORT_GDI_EXT = 0x200F
WGL_SUPPORT_OPENGL_EXT = 0x2010
WGL_DOUBLE_BUFFER_EXT = 0x2011
WGL_STEREO_EXT = 0x2012
WGL_PIXEL_TYPE_EXT = 0x2013
WGL_COLOR_BITS_EXT = 0x2014
WGL_RED_BITS_EXT = 0x2015
WGL_RED_SHIFT_EXT = 0x2016
WGL_GREEN_BITS_EXT = 0x2017
WGL_GREEN_SHIFT_EXT = 0x2018
WGL_BLUE_BITS_EXT = 0x2019
WGL_BLUE_SHIFT_EXT = 0x201A
WGL_ALPHA_BITS_EXT = 0x201B
WGL_ALPHA_SHIFT_EXT = 0x201C
WGL_ACCUM_BITS_EXT = 0x201D
WGL_ACCUM_RED_BITS_EXT = 0x201E
WGL_ACCUM_GREEN_BITS_EXT = 0x201F
WGL_ACCUM_BLUE_BITS_EXT = 0x2020
WGL_ACCUM_ALPHA_BITS_EXT = 0x2021
WGL_DEPTH_BITS_EXT = 0x2022
WGL_STENCIL_BITS_EXT = 0x2023
WGL_AUX_BUFFERS_EXT = 0x2024
WGL_NO_ACCELERATION_EXT = 0x2025
WGL_GENERIC_ACCELERATION_EXT = 0x2026
WGL_FULL_ACCELERATION_EXT = 0x2027
WGL_SWAP_EXCHANGE_EXT = 0x2028
WGL_SWAP_COPY_EXT = 0x2029
WGL_SWAP_UNDEFINED_EXT = 0x202A
WGL_TYPE_RGBA_EXT = 0x202B
WGL_TYPE_COLORINDEX_EXT = 0x202C
# EXT_pixel_format_packed_float
WGL_TYPE_RGBA_UNSIGNED_FLOAT_EXT = 0x20A8
# EXT_swap_control
# EXT_swap_control_tear
# I3D_digital_video_control
WGL_DIGITAL_VIDEO_CURSOR_ALPHA_FRAMEBUFFER_I3D = 0x2050
WGL_DIGITAL_VIDEO_CURSOR_ALPHA_VALUE_I3D = 0x2051
WGL_DIGITAL_VIDEO_CURSOR_INCLUDED_I3D = 0x2052
WGL_DIGITAL_VIDEO_GAMMA_CORRECTED_I3D = 0x2053
# I3D_gamma
WGL_GAMMA_TABLE_SIZE_I3D = 0x204E
WGL_GAMMA_EXCLUDE_DESKTOP_I3D = 0x204F
# I3D_genlock
WGL_GENLOCK_SOURCE_MULTIVIEW_I3D = 0x2044
WGL_GENLOCK_SOURCE_EXTERNAL_SYNC_I3D = 0x2045
WGL_GENLOCK_SOURCE_EXTERNAL_FIELD_I3D = 0x2046
WGL_GENLOCK_SOURCE_EXTERNAL_TTL_I3D = 0x2047
WGL_GENLOCK_SOURCE_DIGITAL_SYNC_I3D = 0x2048
WGL_GENLOCK_SOURCE_DIGITAL_FIELD_I3D = 0x2049
WGL_GENLOCK_SOURCE_EDGE_FALLING_I3D = 0x204A
WGL_GENLOCK_SOURCE_EDGE_RISING_I3D = 0x204B
WGL_GENLOCK_SOURCE_EDGE_BOTH_I3D = 0x204C
# I3D_image_buffer
WGL_IMAGE_BUFFER_MIN_ACCESS_I3D = 0x00000001
WGL_IMAGE_BUFFER_LOCK_I3D = 0x00000002
# I3D_swap_frame_lock
# I3D_swap_frame_usage
# NV_DX_interop
WGL_ACCESS_READ_ONLY_NV = 0x00000000
WGL_ACCESS_READ_WRITE_NV = 0x00000001
WGL_ACCESS_WRITE_DISCARD_NV = 0x00000002
# NV_DX_interop2
# NV_gpu_affinity
WGL_ERROR_INCOMPATIBLE_AFFINITY_MASKS_NV = 0x20D0
WGL_ERROR_MISSING_AFFINITY_MASK_NV = 0x20D1
# NV_render_depth_texture
WGL_BIND_TO_TEXTURE_DEPTH_NV = 0x20A3
WGL_BIND_TO_TEXTURE_RECTANGLE_DEPTH_NV = 0x20A4
WGL_DEPTH_TEXTURE_FORMAT_NV = 0x20A5
WGL_TEXTURE_DEPTH_COMPONENT_NV = 0x20A6
WGL_DEPTH_COMPONENT_NV = 0x20A7
# NV_render_texture_rectangle
WGL_BIND_TO_TEXTURE_RECTANGLE_RGB_NV = 0x20A0
WGL_BIND_TO_TEXTURE_RECTANGLE_RGBA_NV = 0x20A1
WGL_TEXTURE_RECTANGLE_NV = 0x20A2
# NV_swap_group
# NV_video_output
WGL_BIND_TO_VIDEO_RGB_NV = 0x20C0
WGL_BIND_TO_VIDEO_RGBA_NV = 0x20C1
WGL_BIND_TO_VIDEO_RGB_AND_DEPTH_NV = 0x20C2
WGL_VIDEO_OUT_COLOR_NV = 0x20C3
WGL_VIDEO_OUT_ALPHA_NV = 0x20C4
WGL_VIDEO_OUT_DEPTH_NV = 0x20C5
WGL_VIDEO_OUT_COLOR_AND_ALPHA_NV = 0x20C6
WGL_VIDEO_OUT_COLOR_AND_DEPTH_NV = 0x20C7
WGL_VIDEO_OUT_FRAME = 0x20C8
WGL_VIDEO_OUT_FIELD_1 = 0x20C9
WGL_VIDEO_OUT_FIELD_2 = 0x20CA
WGL_VIDEO_OUT_STACKED_FIELDS_1_2 = 0x20CB
WGL_VIDEO_OUT_STACKED_FIELDS_2_1 = 0x20CC
# OML_sync_control
"""

GL_PROC('GL_3DFX_tbuffer', None, 'glTbufferMask3DFX', (GLuint, ))
GL_PROC('GL_AMD_debug_output', None, 'glDebugMessageEnableAMD', (GLenum, GLenum, GLsizei, ctypes.POINTER(GLuint), GLboolean, ))
GL_PROC('GL_AMD_debug_output', None, 'glDebugMessageInsertAMD', (GLenum, GLenum, GLuint, GLsizei, ctypes.POINTER(GLchar), ))
GL_PROC('GL_AMD_debug_output', None, 'glDebugMessageCallbackAMD', (GLDEBUGPROCAMD, ctypes.c_void_p, ))
GL_PROC('GL_AMD_debug_output', GLuint, 'glGetDebugMessageLogAMD', (GLuint, GLsizei, ctypes.POINTER(GLenum), ctypes.POINTER(GLuint), ctypes.POINTER(GLuint), ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_AMD_draw_buffers_blend', None, 'glBlendFuncIndexedAMD', (GLuint, GLenum, GLenum, ))
GL_PROC('GL_AMD_draw_buffers_blend', None, 'glBlendFuncSeparateIndexedAMD', (GLuint, GLenum, GLenum, GLenum, GLenum, ))
GL_PROC('GL_AMD_draw_buffers_blend', None, 'glBlendEquationIndexedAMD', (GLuint, GLenum, ))
GL_PROC('GL_AMD_draw_buffers_blend', None, 'glBlendEquationSeparateIndexedAMD', (GLuint, GLenum, GLenum, ))
GL_PROC('GL_AMD_multi_draw_indirect', None, 'glMultiDrawArraysIndirectAMD', (GLenum, ctypes.c_void_p, GLsizei, GLsizei, ))
GL_PROC('GL_AMD_multi_draw_indirect', None, 'glMultiDrawElementsIndirectAMD', (GLenum, GLenum, ctypes.c_void_p, GLsizei, GLsizei, ))
GL_PROC('GL_AMD_name_gen_delete', None, 'glGenNamesAMD', (GLenum, GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_AMD_name_gen_delete', None, 'glDeleteNamesAMD', (GLenum, GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_AMD_name_gen_delete', GLboolean, 'glIsNameAMD', (GLenum, GLuint, ))
GL_PROC('GL_AMD_performance_monitor', None, 'glGetPerfMonitorGroupsAMD', (ctypes.POINTER(GLint), GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_AMD_performance_monitor', None, 'glGetPerfMonitorCountersAMD', (GLuint, ctypes.POINTER(GLint), ctypes.POINTER(GLint), GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_AMD_performance_monitor', None, 'glGetPerfMonitorGroupStringAMD', (GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_AMD_performance_monitor', None, 'glGetPerfMonitorCounterStringAMD', (GLuint, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_AMD_performance_monitor', None, 'glGetPerfMonitorCounterInfoAMD', (GLuint, GLuint, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_AMD_performance_monitor', None, 'glGenPerfMonitorsAMD', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_AMD_performance_monitor', None, 'glDeletePerfMonitorsAMD', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_AMD_performance_monitor', None, 'glSelectPerfMonitorCountersAMD', (GLuint, GLboolean, GLuint, GLint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_AMD_performance_monitor', None, 'glBeginPerfMonitorAMD', (GLuint, ))
GL_PROC('GL_AMD_performance_monitor', None, 'glEndPerfMonitorAMD', (GLuint, ))
GL_PROC('GL_AMD_performance_monitor', None, 'glGetPerfMonitorCounterDataAMD', (GLuint, GLenum, GLsizei, ctypes.POINTER(GLuint), ctypes.POINTER(GLint), ))
GL_PROC('GL_AMD_sample_positions', None, 'glSetMultisamplefvAMD', (GLenum, GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_AMD_stencil_operation_extended', None, 'glStencilOpValueAMD', (GLenum, GLuint, ))
GL_PROC('GL_AMD_vertex_shader_tessellator', None, 'glTessellationFactorAMD', (GLfloat, ))
GL_PROC('GL_AMD_vertex_shader_tessellator', None, 'glTessellationModeAMD', (GLenum, ))
GL_PROC('GL_APPLE_element_array', None, 'glElementPointerAPPLE', (GLenum, ctypes.c_void_p, ))
GL_PROC('GL_APPLE_element_array', None, 'glDrawElementArrayAPPLE', (GLenum, GLint, GLsizei, ))
GL_PROC('GL_APPLE_element_array', None, 'glDrawRangeElementArrayAPPLE', (GLenum, GLuint, GLuint, GLint, GLsizei, ))
GL_PROC('GL_APPLE_element_array', None, 'glMultiDrawElementArrayAPPLE', (GLenum, ctypes.POINTER(GLint), ctypes.POINTER(GLsizei), GLsizei, ))
GL_PROC('GL_APPLE_element_array', None, 'glMultiDrawRangeElementArrayAPPLE', (GLenum, GLuint, GLuint, ctypes.POINTER(GLint), ctypes.POINTER(GLsizei), GLsizei, ))
GL_PROC('GL_APPLE_fence', None, 'glGenFencesAPPLE', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_APPLE_fence', None, 'glDeleteFencesAPPLE', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_APPLE_fence', None, 'glSetFenceAPPLE', (GLuint, ))
GL_PROC('GL_APPLE_fence', GLboolean, 'glIsFenceAPPLE', (GLuint, ))
GL_PROC('GL_APPLE_fence', GLboolean, 'glTestFenceAPPLE', (GLuint, ))
GL_PROC('GL_APPLE_fence', None, 'glFinishFenceAPPLE', (GLuint, ))
GL_PROC('GL_APPLE_fence', GLboolean, 'glTestObjectAPPLE', (GLenum, GLuint, ))
GL_PROC('GL_APPLE_fence', None, 'glFinishObjectAPPLE', (GLenum, GLint, ))
GL_PROC('GL_APPLE_flush_buffer_range', None, 'glBufferParameteriAPPLE', (GLenum, GLenum, GLint, ))
GL_PROC('GL_APPLE_flush_buffer_range', None, 'glFlushMappedBufferRangeAPPLE', (GLenum, GLintptr, GLsizeiptr, ))
GL_PROC('GL_APPLE_object_purgeable', GLenum, 'glObjectPurgeableAPPLE', (GLenum, GLuint, GLenum, ))
GL_PROC('GL_APPLE_object_purgeable', GLenum, 'glObjectUnpurgeableAPPLE', (GLenum, GLuint, GLenum, ))
GL_PROC('GL_APPLE_object_purgeable', None, 'glGetObjectParameterivAPPLE', (GLenum, GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_APPLE_texture_range', None, 'glTextureRangeAPPLE', (GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_APPLE_texture_range', None, 'glGetTexParameterPointervAPPLE', (GLenum, GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_APPLE_vertex_array_object', None, 'glBindVertexArrayAPPLE', (GLuint, ))
GL_PROC('GL_APPLE_vertex_array_object', None, 'glDeleteVertexArraysAPPLE', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_APPLE_vertex_array_object', None, 'glGenVertexArraysAPPLE', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_APPLE_vertex_array_object', GLboolean, 'glIsVertexArrayAPPLE', (GLuint, ))
GL_PROC('GL_APPLE_vertex_array_range', None, 'glVertexArrayRangeAPPLE', (GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_APPLE_vertex_array_range', None, 'glFlushVertexArrayRangeAPPLE', (GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_APPLE_vertex_array_range', None, 'glVertexArrayParameteriAPPLE', (GLenum, GLint, ))
GL_PROC('GL_APPLE_vertex_program_evaluators', None, 'glEnableVertexAttribAPPLE', (GLuint, GLenum, ))
GL_PROC('GL_APPLE_vertex_program_evaluators', None, 'glDisableVertexAttribAPPLE', (GLuint, GLenum, ))
GL_PROC('GL_APPLE_vertex_program_evaluators', GLboolean, 'glIsVertexAttribEnabledAPPLE', (GLuint, GLenum, ))
GL_PROC('GL_APPLE_vertex_program_evaluators', None, 'glMapVertexAttrib1dAPPLE', (GLuint, GLuint, GLdouble, GLdouble, GLint, GLint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_APPLE_vertex_program_evaluators', None, 'glMapVertexAttrib1fAPPLE', (GLuint, GLuint, GLfloat, GLfloat, GLint, GLint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_APPLE_vertex_program_evaluators', None, 'glMapVertexAttrib2dAPPLE', (GLuint, GLuint, GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble, GLint, GLint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_APPLE_vertex_program_evaluators', None, 'glMapVertexAttrib2fAPPLE', (GLuint, GLuint, GLfloat, GLfloat, GLint, GLint, GLfloat, GLfloat, GLint, GLint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_ES2_compatibility', None, 'glReleaseShaderCompiler', ())
GL_PROC('GL_ARB_ES2_compatibility', None, 'glShaderBinary', (GLsizei, ctypes.POINTER(GLuint), GLenum, ctypes.c_void_p, GLsizei, ))
GL_PROC('GL_ARB_ES2_compatibility', None, 'glGetShaderPrecisionFormat', (GLenum, GLenum, ctypes.POINTER(GLint), ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_ES2_compatibility', None, 'glDepthRangef', (GLfloat, GLfloat, ))
GL_PROC('GL_ARB_ES2_compatibility', None, 'glClearDepthf', (GLfloat, ))
GL_PROC('GL_ARB_base_instance', None, 'glDrawArraysInstancedBaseInstance', (GLenum, GLint, GLsizei, GLsizei, GLuint, ))
GL_PROC('GL_ARB_base_instance', None, 'glDrawElementsInstancedBaseInstance', (GLenum, GLsizei, GLenum, ctypes.c_void_p, GLsizei, GLuint, ))
GL_PROC('GL_ARB_base_instance', None, 'glDrawElementsInstancedBaseVertexBaseInstance', (GLenum, GLsizei, GLenum, ctypes.c_void_p, GLsizei, GLint, GLuint, ))
GL_PROC('GL_ARB_blend_func_extended', None, 'glBindFragDataLocationIndexed', (GLuint, GLuint, GLuint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_blend_func_extended', GLint, 'glGetFragDataIndex', (GLuint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_cl_event', GLsync, 'glCreateSyncFromCLeventARB', (ctypes.POINTER(_cl_context), ctypes.POINTER(_cl_event), GLbitfield, ))
GL_PROC('GL_ARB_clear_buffer_object', None, 'glClearBufferData', (GLenum, GLenum, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_ARB_clear_buffer_object', None, 'glClearBufferSubData', (GLenum, GLenum, GLintptr, GLsizeiptr, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_ARB_clear_buffer_object', None, 'glClearNamedBufferDataEXT', (GLuint, GLenum, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_ARB_clear_buffer_object', None, 'glClearNamedBufferSubDataEXT', (GLuint, GLenum, GLsizeiptr, GLsizeiptr, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_ARB_color_buffer_float', None, 'glClampColorARB', (GLenum, GLenum, ))
GL_PROC('GL_ARB_compute_shader', None, 'glDispatchCompute', (GLuint, GLuint, GLuint, ))
GL_PROC('GL_ARB_compute_shader', None, 'glDispatchComputeIndirect', (GLintptr, ))
GL_PROC('GL_ARB_copy_buffer', None, 'glCopyBufferSubData', (GLenum, GLenum, GLintptr, GLintptr, GLsizeiptr, ))
GL_PROC('GL_ARB_copy_image', None, 'glCopyImageSubData', (GLuint, GLenum, GLint, GLint, GLint, GLint, GLuint, GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, ))
GL_PROC('GL_ARB_debug_output', None, 'glDebugMessageControlARB', (GLenum, GLenum, GLenum, GLsizei, ctypes.POINTER(GLuint), GLboolean, ))
GL_PROC('GL_ARB_debug_output', None, 'glDebugMessageInsertARB', (GLenum, GLenum, GLuint, GLenum, GLsizei, ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_debug_output', None, 'glDebugMessageCallbackARB', (GLDEBUGPROCARB, ctypes.c_void_p, ))
GL_PROC('GL_ARB_debug_output', GLuint, 'glGetDebugMessageLogARB', (GLuint, GLsizei, ctypes.POINTER(GLenum), ctypes.POINTER(GLenum), ctypes.POINTER(GLuint), ctypes.POINTER(GLenum), ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_draw_buffers', None, 'glDrawBuffersARB', (GLsizei, ctypes.POINTER(GLenum), ))
GL_PROC('GL_ARB_draw_buffers_blend', None, 'glBlendEquationiARB', (GLuint, GLenum, ))
GL_PROC('GL_ARB_draw_buffers_blend', None, 'glBlendEquationSeparateiARB', (GLuint, GLenum, GLenum, ))
GL_PROC('GL_ARB_draw_buffers_blend', None, 'glBlendFunciARB', (GLuint, GLenum, GLenum, ))
GL_PROC('GL_ARB_draw_buffers_blend', None, 'glBlendFuncSeparateiARB', (GLuint, GLenum, GLenum, GLenum, GLenum, ))
GL_PROC('GL_ARB_draw_elements_base_vertex', None, 'glDrawElementsBaseVertex', (GLenum, GLsizei, GLenum, ctypes.c_void_p, GLint, ))
GL_PROC('GL_ARB_draw_elements_base_vertex', None, 'glDrawRangeElementsBaseVertex', (GLenum, GLuint, GLuint, GLsizei, GLenum, ctypes.c_void_p, GLint, ))
GL_PROC('GL_ARB_draw_elements_base_vertex', None, 'glDrawElementsInstancedBaseVertex', (GLenum, GLsizei, GLenum, ctypes.c_void_p, GLsizei, GLint, ))
GL_PROC('GL_ARB_draw_elements_base_vertex', None, 'glMultiDrawElementsBaseVertex', (GLenum, ctypes.POINTER(GLsizei), GLenum, ctypes.POINTER(ctypes.c_void_p), GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_draw_indirect', None, 'glDrawArraysIndirect', (GLenum, ctypes.c_void_p, ))
GL_PROC('GL_ARB_draw_indirect', None, 'glDrawElementsIndirect', (GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_ARB_draw_instanced', None, 'glDrawArraysInstancedARB', (GLenum, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_ARB_draw_instanced', None, 'glDrawElementsInstancedARB', (GLenum, GLsizei, GLenum, ctypes.c_void_p, GLsizei, ))
GL_PROC('GL_ARB_framebuffer_no_attachments', None, 'glFramebufferParameteri', (GLenum, GLenum, GLint, ))
GL_PROC('GL_ARB_framebuffer_no_attachments', None, 'glGetFramebufferParameteriv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_framebuffer_no_attachments', None, 'glNamedFramebufferParameteriEXT', (GLuint, GLenum, GLint, ))
GL_PROC('GL_ARB_framebuffer_no_attachments', None, 'glGetNamedFramebufferParameterivEXT', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_framebuffer_object', GLboolean, 'glIsRenderbuffer', (GLuint, ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glBindRenderbuffer', (GLenum, GLuint, ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glDeleteRenderbuffers', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glGenRenderbuffers', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glRenderbufferStorage', (GLenum, GLenum, GLsizei, GLsizei, ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glGetRenderbufferParameteriv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_framebuffer_object', GLboolean, 'glIsFramebuffer', (GLuint, ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glBindFramebuffer', (GLenum, GLuint, ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glDeleteFramebuffers', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glGenFramebuffers', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_framebuffer_object', GLenum, 'glCheckFramebufferStatus', (GLenum, ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glFramebufferTexture1D', (GLenum, GLenum, GLenum, GLuint, GLint, ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glFramebufferTexture2D', (GLenum, GLenum, GLenum, GLuint, GLint, ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glFramebufferTexture3D', (GLenum, GLenum, GLenum, GLuint, GLint, GLint, ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glFramebufferRenderbuffer', (GLenum, GLenum, GLenum, GLuint, ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glGetFramebufferAttachmentParameteriv', (GLenum, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glGenerateMipmap', (GLenum, ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glBlitFramebuffer', (GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLbitfield, GLenum, ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glRenderbufferStorageMultisample', (GLenum, GLsizei, GLenum, GLsizei, GLsizei, ))
GL_PROC('GL_ARB_framebuffer_object', None, 'glFramebufferTextureLayer', (GLenum, GLenum, GLuint, GLint, GLint, ))
GL_PROC('GL_ARB_geometry_shader4', None, 'glProgramParameteriARB', (GLuint, GLenum, GLint, ))
GL_PROC('GL_ARB_geometry_shader4', None, 'glFramebufferTextureARB', (GLenum, GLenum, GLuint, GLint, ))
GL_PROC('GL_ARB_geometry_shader4', None, 'glFramebufferTextureLayerARB', (GLenum, GLenum, GLuint, GLint, GLint, ))
GL_PROC('GL_ARB_geometry_shader4', None, 'glFramebufferTextureFaceARB', (GLenum, GLenum, GLuint, GLint, GLenum, ))
GL_PROC('GL_ARB_get_program_binary', None, 'glGetProgramBinary', (GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLenum), ctypes.c_void_p, ))
GL_PROC('GL_ARB_get_program_binary', None, 'glProgramBinary', (GLuint, GLenum, ctypes.c_void_p, GLsizei, ))
GL_PROC('GL_ARB_get_program_binary', None, 'glProgramParameteri', (GLuint, GLenum, GLint, ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniform1d', (GLint, GLdouble, ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniform2d', (GLint, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniform3d', (GLint, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniform4d', (GLint, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniform1dv', (GLint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniform2dv', (GLint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniform3dv', (GLint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniform4dv', (GLint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniformMatrix2dv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniformMatrix3dv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniformMatrix4dv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniformMatrix2x3dv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniformMatrix2x4dv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniformMatrix3x2dv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniformMatrix3x4dv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniformMatrix4x2dv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glUniformMatrix4x3dv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_gpu_shader_fp64', None, 'glGetUniformdv', (GLuint, GLint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_instanced_arrays', None, 'glVertexAttribDivisorARB', (GLuint, GLuint, ))
GL_PROC('GL_ARB_internalformat_query', None, 'glGetInternalformativ', (GLenum, GLenum, GLenum, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_internalformat_query2', None, 'glGetInternalformati64v', (GLenum, GLenum, GLenum, GLsizei, ctypes.POINTER(GLint64), ))
GL_PROC('GL_ARB_invalidate_subdata', None, 'glInvalidateTexSubImage', (GLuint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, ))
GL_PROC('GL_ARB_invalidate_subdata', None, 'glInvalidateTexImage', (GLuint, GLint, ))
GL_PROC('GL_ARB_invalidate_subdata', None, 'glInvalidateBufferSubData', (GLuint, GLintptr, GLsizeiptr, ))
GL_PROC('GL_ARB_invalidate_subdata', None, 'glInvalidateBufferData', (GLuint, ))
GL_PROC('GL_ARB_invalidate_subdata', None, 'glInvalidateFramebuffer', (GLenum, GLsizei, ctypes.POINTER(GLenum), ))
GL_PROC('GL_ARB_invalidate_subdata', None, 'glInvalidateSubFramebuffer', (GLenum, GLsizei, ctypes.POINTER(GLenum), GLint, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_ARB_map_buffer_range', ctypes.c_void_p, 'glMapBufferRange', (GLenum, GLintptr, GLsizeiptr, GLbitfield, ))
GL_PROC('GL_ARB_map_buffer_range', None, 'glFlushMappedBufferRange', (GLenum, GLintptr, GLsizeiptr, ))
GL_PROC('GL_ARB_matrix_palette', None, 'glCurrentPaletteMatrixARB', (GLint, ))
GL_PROC('GL_ARB_matrix_palette', None, 'glMatrixIndexubvARB', (GLint, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_ARB_matrix_palette', None, 'glMatrixIndexusvARB', (GLint, ctypes.POINTER(GLushort), ))
GL_PROC('GL_ARB_matrix_palette', None, 'glMatrixIndexuivARB', (GLint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_matrix_palette', None, 'glMatrixIndexPointerARB', (GLint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_multi_draw_indirect', None, 'glMultiDrawArraysIndirect', (GLenum, ctypes.c_void_p, GLsizei, GLsizei, ))
GL_PROC('GL_ARB_multi_draw_indirect', None, 'glMultiDrawElementsIndirect', (GLenum, GLenum, ctypes.c_void_p, GLsizei, GLsizei, ))
GL_PROC('GL_ARB_multisample', None, 'glSampleCoverageARB', (GLfloat, GLboolean, ))
GL_PROC('GL_ARB_multitexture', None, 'glActiveTextureARB', (GLenum, ))
GL_PROC('GL_ARB_multitexture', None, 'glClientActiveTextureARB', (GLenum, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord1dARB', (GLenum, GLdouble, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord1dvARB', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord1fARB', (GLenum, GLfloat, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord1fvARB', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord1iARB', (GLenum, GLint, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord1ivARB', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord1sARB', (GLenum, GLshort, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord1svARB', (GLenum, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord2dARB', (GLenum, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord2dvARB', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord2fARB', (GLenum, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord2fvARB', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord2iARB', (GLenum, GLint, GLint, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord2ivARB', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord2sARB', (GLenum, GLshort, GLshort, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord2svARB', (GLenum, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord3dARB', (GLenum, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord3dvARB', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord3fARB', (GLenum, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord3fvARB', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord3iARB', (GLenum, GLint, GLint, GLint, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord3ivARB', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord3sARB', (GLenum, GLshort, GLshort, GLshort, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord3svARB', (GLenum, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord4dARB', (GLenum, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord4dvARB', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord4fARB', (GLenum, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord4fvARB', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord4iARB', (GLenum, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord4ivARB', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord4sARB', (GLenum, GLshort, GLshort, GLshort, GLshort, ))
GL_PROC('GL_ARB_multitexture', None, 'glMultiTexCoord4svARB', (GLenum, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ARB_occlusion_query', None, 'glGenQueriesARB', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_occlusion_query', None, 'glDeleteQueriesARB', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_occlusion_query', GLboolean, 'glIsQueryARB', (GLuint, ))
GL_PROC('GL_ARB_occlusion_query', None, 'glBeginQueryARB', (GLenum, GLuint, ))
GL_PROC('GL_ARB_occlusion_query', None, 'glEndQueryARB', (GLenum, ))
GL_PROC('GL_ARB_occlusion_query', None, 'glGetQueryivARB', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_occlusion_query', None, 'glGetQueryObjectivARB', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_occlusion_query', None, 'glGetQueryObjectuivARB', (GLuint, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_point_parameters', None, 'glPointParameterfARB', (GLenum, GLfloat, ))
GL_PROC('GL_ARB_point_parameters', None, 'glPointParameterfvARB', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_program_interface_query', None, 'glGetProgramInterfaceiv', (GLuint, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_program_interface_query', GLuint, 'glGetProgramResourceIndex', (GLuint, GLenum, ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_program_interface_query', None, 'glGetProgramResourceName', (GLuint, GLenum, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_program_interface_query', None, 'glGetProgramResourceiv', (GLuint, GLenum, GLuint, GLsizei, ctypes.POINTER(GLenum), GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_program_interface_query', GLint, 'glGetProgramResourceLocation', (GLuint, GLenum, ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_program_interface_query', GLint, 'glGetProgramResourceLocationIndex', (GLuint, GLenum, ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_provoking_vertex', None, 'glProvokingVertex', (GLenum, ))
GL_PROC('GL_ARB_robustness', GLenum, 'glGetGraphicsResetStatusARB', ())
GL_PROC('GL_ARB_robustness', None, 'glGetnMapdvARB', (GLenum, GLenum, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_robustness', None, 'glGetnMapfvARB', (GLenum, GLenum, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_robustness', None, 'glGetnMapivARB', (GLenum, GLenum, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_robustness', None, 'glGetnPixelMapfvARB', (GLenum, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_robustness', None, 'glGetnPixelMapuivARB', (GLenum, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_robustness', None, 'glGetnPixelMapusvARB', (GLenum, GLsizei, ctypes.POINTER(GLushort), ))
GL_PROC('GL_ARB_robustness', None, 'glGetnPolygonStippleARB', (GLsizei, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_ARB_robustness', None, 'glGetnColorTableARB', (GLenum, GLenum, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_robustness', None, 'glGetnConvolutionFilterARB', (GLenum, GLenum, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_robustness', None, 'glGetnSeparableFilterARB', (GLenum, GLenum, GLenum, GLsizei, ctypes.c_void_p, GLsizei, ctypes.c_void_p, ctypes.c_void_p, ))
GL_PROC('GL_ARB_robustness', None, 'glGetnHistogramARB', (GLenum, GLboolean, GLenum, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_robustness', None, 'glGetnMinmaxARB', (GLenum, GLboolean, GLenum, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_robustness', None, 'glGetnTexImageARB', (GLenum, GLint, GLenum, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_robustness', None, 'glReadnPixelsARB', (GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_robustness', None, 'glGetnCompressedTexImageARB', (GLenum, GLint, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_robustness', None, 'glGetnUniformfvARB', (GLuint, GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_robustness', None, 'glGetnUniformivARB', (GLuint, GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_robustness', None, 'glGetnUniformuivARB', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_robustness', None, 'glGetnUniformdvARB', (GLuint, GLint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_sample_shading', None, 'glMinSampleShadingARB', (GLfloat, ))
GL_PROC('GL_ARB_sampler_objects', None, 'glGenSamplers', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_sampler_objects', None, 'glDeleteSamplers', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_sampler_objects', GLboolean, 'glIsSampler', (GLuint, ))
GL_PROC('GL_ARB_sampler_objects', None, 'glBindSampler', (GLuint, GLuint, ))
GL_PROC('GL_ARB_sampler_objects', None, 'glSamplerParameteri', (GLuint, GLenum, GLint, ))
GL_PROC('GL_ARB_sampler_objects', None, 'glSamplerParameteriv', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_sampler_objects', None, 'glSamplerParameterf', (GLuint, GLenum, GLfloat, ))
GL_PROC('GL_ARB_sampler_objects', None, 'glSamplerParameterfv', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_sampler_objects', None, 'glSamplerParameterIiv', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_sampler_objects', None, 'glSamplerParameterIuiv', (GLuint, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_sampler_objects', None, 'glGetSamplerParameteriv', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_sampler_objects', None, 'glGetSamplerParameterIiv', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_sampler_objects', None, 'glGetSamplerParameterfv', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_sampler_objects', None, 'glGetSamplerParameterIuiv', (GLuint, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glUseProgramStages', (GLuint, GLbitfield, GLuint, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glActiveShaderProgram', (GLuint, GLuint, ))
GL_PROC('GL_ARB_separate_shader_objects', GLuint, 'glCreateShaderProgramv', (GLenum, GLsizei, ctypes.POINTER(ctypes.POINTER(GLchar)), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glBindProgramPipeline', (GLuint, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glDeleteProgramPipelines', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glGenProgramPipelines', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_separate_shader_objects', GLboolean, 'glIsProgramPipeline', (GLuint, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glGetProgramPipelineiv', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform1i', (GLuint, GLint, GLint, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform1iv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform1f', (GLuint, GLint, GLfloat, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform1fv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform1d', (GLuint, GLint, GLdouble, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform1dv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform1ui', (GLuint, GLint, GLuint, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform1uiv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform2i', (GLuint, GLint, GLint, GLint, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform2iv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform2f', (GLuint, GLint, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform2fv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform2d', (GLuint, GLint, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform2dv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform2ui', (GLuint, GLint, GLuint, GLuint, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform2uiv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform3i', (GLuint, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform3iv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform3f', (GLuint, GLint, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform3fv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform3d', (GLuint, GLint, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform3dv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform3ui', (GLuint, GLint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform3uiv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform4i', (GLuint, GLint, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform4iv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform4f', (GLuint, GLint, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform4fv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform4d', (GLuint, GLint, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform4dv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform4ui', (GLuint, GLint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniform4uiv', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix2fv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix3fv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix4fv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix2dv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix3dv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix4dv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix2x3fv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix3x2fv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix2x4fv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix4x2fv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix3x4fv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix4x3fv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix2x3dv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix3x2dv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix2x4dv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix4x2dv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix3x4dv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glProgramUniformMatrix4x3dv', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glValidateProgramPipeline', (GLuint, ))
GL_PROC('GL_ARB_separate_shader_objects', None, 'glGetProgramPipelineInfoLog', (GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_shader_atomic_counters', None, 'glGetActiveAtomicCounterBufferiv', (GLuint, GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_shader_image_load_store', None, 'glBindImageTexture', (GLuint, GLuint, GLint, GLboolean, GLint, GLenum, GLenum, ))
GL_PROC('GL_ARB_shader_image_load_store', None, 'glMemoryBarrier', (GLbitfield, ))
GL_PROC('GL_ARB_shader_objects', None, 'glDeleteObjectARB', (GLhandleARB, ))
GL_PROC('GL_ARB_shader_objects', GLhandleARB, 'glGetHandleARB', (GLenum, ))
GL_PROC('GL_ARB_shader_objects', None, 'glDetachObjectARB', (GLhandleARB, GLhandleARB, ))
GL_PROC('GL_ARB_shader_objects', GLhandleARB, 'glCreateShaderObjectARB', (GLenum, ))
GL_PROC('GL_ARB_shader_objects', None, 'glShaderSourceARB', (GLhandleARB, GLsizei, ctypes.POINTER(ctypes.POINTER(GLcharARB)), ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_shader_objects', None, 'glCompileShaderARB', (GLhandleARB, ))
GL_PROC('GL_ARB_shader_objects', GLhandleARB, 'glCreateProgramObjectARB', ())
GL_PROC('GL_ARB_shader_objects', None, 'glAttachObjectARB', (GLhandleARB, GLhandleARB, ))
GL_PROC('GL_ARB_shader_objects', None, 'glLinkProgramARB', (GLhandleARB, ))
GL_PROC('GL_ARB_shader_objects', None, 'glUseProgramObjectARB', (GLhandleARB, ))
GL_PROC('GL_ARB_shader_objects', None, 'glValidateProgramARB', (GLhandleARB, ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform1fARB', (GLint, GLfloat, ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform2fARB', (GLint, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform3fARB', (GLint, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform4fARB', (GLint, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform1iARB', (GLint, GLint, ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform2iARB', (GLint, GLint, GLint, ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform3iARB', (GLint, GLint, GLint, GLint, ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform4iARB', (GLint, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform1fvARB', (GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform2fvARB', (GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform3fvARB', (GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform4fvARB', (GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform1ivARB', (GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform2ivARB', (GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform3ivARB', (GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniform4ivARB', (GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniformMatrix2fvARB', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniformMatrix3fvARB', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_shader_objects', None, 'glUniformMatrix4fvARB', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_shader_objects', None, 'glGetObjectParameterfvARB', (GLhandleARB, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_shader_objects', None, 'glGetObjectParameterivARB', (GLhandleARB, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_shader_objects', None, 'glGetInfoLogARB', (GLhandleARB, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLcharARB), ))
GL_PROC('GL_ARB_shader_objects', None, 'glGetAttachedObjectsARB', (GLhandleARB, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLhandleARB), ))
GL_PROC('GL_ARB_shader_objects', GLint, 'glGetUniformLocationARB', (GLhandleARB, ctypes.POINTER(GLcharARB), ))
GL_PROC('GL_ARB_shader_objects', None, 'glGetActiveUniformARB', (GLhandleARB, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLint), ctypes.POINTER(GLenum), ctypes.POINTER(GLcharARB), ))
GL_PROC('GL_ARB_shader_objects', None, 'glGetUniformfvARB', (GLhandleARB, GLint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_shader_objects', None, 'glGetUniformivARB', (GLhandleARB, GLint, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_shader_objects', None, 'glGetShaderSourceARB', (GLhandleARB, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLcharARB), ))
GL_PROC('GL_ARB_shader_storage_buffer_object', None, 'glShaderStorageBlockBinding', (GLuint, GLuint, GLuint, ))
GL_PROC('GL_ARB_shader_subroutine', GLint, 'glGetSubroutineUniformLocation', (GLuint, GLenum, ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_shader_subroutine', GLuint, 'glGetSubroutineIndex', (GLuint, GLenum, ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_shader_subroutine', None, 'glGetActiveSubroutineUniformiv', (GLuint, GLenum, GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_shader_subroutine', None, 'glGetActiveSubroutineUniformName', (GLuint, GLenum, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_shader_subroutine', None, 'glGetActiveSubroutineName', (GLuint, GLenum, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_shader_subroutine', None, 'glUniformSubroutinesuiv', (GLenum, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_shader_subroutine', None, 'glGetUniformSubroutineuiv', (GLenum, GLint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_shader_subroutine', None, 'glGetProgramStageiv', (GLuint, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_shading_language_include', None, 'glNamedStringARB', (GLenum, GLint, ctypes.POINTER(GLchar), GLint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_shading_language_include', None, 'glDeleteNamedStringARB', (GLint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_shading_language_include', None, 'glCompileShaderIncludeARB', (GLuint, GLsizei, ctypes.POINTER(ctypes.POINTER(GLchar)), ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_shading_language_include', GLboolean, 'glIsNamedStringARB', (GLint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_shading_language_include', None, 'glGetNamedStringARB', (GLint, ctypes.POINTER(GLchar), GLsizei, ctypes.POINTER(GLint), ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_shading_language_include', None, 'glGetNamedStringivARB', (GLint, ctypes.POINTER(GLchar), GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_sync', GLsync, 'glFenceSync', (GLenum, GLbitfield, ))
GL_PROC('GL_ARB_sync', GLboolean, 'glIsSync', (GLsync, ))
GL_PROC('GL_ARB_sync', None, 'glDeleteSync', (GLsync, ))
GL_PROC('GL_ARB_sync', GLenum, 'glClientWaitSync', (GLsync, GLbitfield, GLuint64, ))
GL_PROC('GL_ARB_sync', None, 'glWaitSync', (GLsync, GLbitfield, GLuint64, ))
GL_PROC('GL_ARB_sync', None, 'glGetInteger64v', (GLenum, ctypes.POINTER(GLint64), ))
GL_PROC('GL_ARB_sync', None, 'glGetSynciv', (GLsync, GLenum, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_tessellation_shader', None, 'glPatchParameteri', (GLenum, GLint, ))
GL_PROC('GL_ARB_tessellation_shader', None, 'glPatchParameterfv', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_texture_buffer_object', None, 'glTexBufferARB', (GLenum, GLenum, GLuint, ))
GL_PROC('GL_ARB_texture_buffer_range', None, 'glTexBufferRange', (GLenum, GLenum, GLuint, GLintptr, GLsizeiptr, ))
GL_PROC('GL_ARB_texture_buffer_range', None, 'glTextureBufferRangeEXT', (GLuint, GLenum, GLenum, GLuint, GLintptr, GLsizeiptr, ))
GL_PROC('GL_ARB_texture_compression', None, 'glCompressedTexImage3DARB', (GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_texture_compression', None, 'glCompressedTexImage2DARB', (GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_texture_compression', None, 'glCompressedTexImage1DARB', (GLenum, GLint, GLenum, GLsizei, GLint, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_texture_compression', None, 'glCompressedTexSubImage3DARB', (GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_texture_compression', None, 'glCompressedTexSubImage2DARB', (GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_texture_compression', None, 'glCompressedTexSubImage1DARB', (GLenum, GLint, GLint, GLsizei, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_texture_compression', None, 'glGetCompressedTexImageARB', (GLenum, GLint, ctypes.c_void_p, ))
GL_PROC('GL_ARB_texture_multisample', None, 'glTexImage2DMultisample', (GLenum, GLsizei, GLint, GLsizei, GLsizei, GLboolean, ))
GL_PROC('GL_ARB_texture_multisample', None, 'glTexImage3DMultisample', (GLenum, GLsizei, GLint, GLsizei, GLsizei, GLsizei, GLboolean, ))
GL_PROC('GL_ARB_texture_multisample', None, 'glGetMultisamplefv', (GLenum, GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_texture_multisample', None, 'glSampleMaski', (GLuint, GLbitfield, ))
GL_PROC('GL_ARB_texture_storage', None, 'glTexStorage1D', (GLenum, GLsizei, GLenum, GLsizei, ))
GL_PROC('GL_ARB_texture_storage', None, 'glTexStorage2D', (GLenum, GLsizei, GLenum, GLsizei, GLsizei, ))
GL_PROC('GL_ARB_texture_storage', None, 'glTexStorage3D', (GLenum, GLsizei, GLenum, GLsizei, GLsizei, GLsizei, ))
GL_PROC('GL_ARB_texture_storage', None, 'glTextureStorage1DEXT', (GLuint, GLenum, GLsizei, GLenum, GLsizei, ))
GL_PROC('GL_ARB_texture_storage', None, 'glTextureStorage2DEXT', (GLuint, GLenum, GLsizei, GLenum, GLsizei, GLsizei, ))
GL_PROC('GL_ARB_texture_storage', None, 'glTextureStorage3DEXT', (GLuint, GLenum, GLsizei, GLenum, GLsizei, GLsizei, GLsizei, ))
GL_PROC('GL_ARB_texture_storage_multisample', None, 'glTexStorage2DMultisample', (GLenum, GLsizei, GLenum, GLsizei, GLsizei, GLboolean, ))
GL_PROC('GL_ARB_texture_storage_multisample', None, 'glTexStorage3DMultisample', (GLenum, GLsizei, GLenum, GLsizei, GLsizei, GLsizei, GLboolean, ))
GL_PROC('GL_ARB_texture_storage_multisample', None, 'glTextureStorage2DMultisampleEXT', (GLuint, GLenum, GLsizei, GLenum, GLsizei, GLsizei, GLboolean, ))
GL_PROC('GL_ARB_texture_storage_multisample', None, 'glTextureStorage3DMultisampleEXT', (GLuint, GLenum, GLsizei, GLenum, GLsizei, GLsizei, GLsizei, GLboolean, ))
GL_PROC('GL_ARB_texture_view', None, 'glTextureView', (GLuint, GLenum, GLuint, GLenum, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_ARB_timer_query', None, 'glQueryCounter', (GLuint, GLenum, ))
GL_PROC('GL_ARB_timer_query', None, 'glGetQueryObjecti64v', (GLuint, GLenum, ctypes.POINTER(GLint64), ))
GL_PROC('GL_ARB_timer_query', None, 'glGetQueryObjectui64v', (GLuint, GLenum, ctypes.POINTER(GLuint64), ))
GL_PROC('GL_ARB_transform_feedback2', None, 'glBindTransformFeedback', (GLenum, GLuint, ))
GL_PROC('GL_ARB_transform_feedback2', None, 'glDeleteTransformFeedbacks', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_transform_feedback2', None, 'glGenTransformFeedbacks', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_transform_feedback2', GLboolean, 'glIsTransformFeedback', (GLuint, ))
GL_PROC('GL_ARB_transform_feedback2', None, 'glPauseTransformFeedback', ())
GL_PROC('GL_ARB_transform_feedback2', None, 'glResumeTransformFeedback', ())
GL_PROC('GL_ARB_transform_feedback2', None, 'glDrawTransformFeedback', (GLenum, GLuint, ))
GL_PROC('GL_ARB_transform_feedback3', None, 'glDrawTransformFeedbackStream', (GLenum, GLuint, GLuint, ))
GL_PROC('GL_ARB_transform_feedback3', None, 'glBeginQueryIndexed', (GLenum, GLuint, GLuint, ))
GL_PROC('GL_ARB_transform_feedback3', None, 'glEndQueryIndexed', (GLenum, GLuint, ))
GL_PROC('GL_ARB_transform_feedback3', None, 'glGetQueryIndexediv', (GLenum, GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_transform_feedback_instanced', None, 'glDrawTransformFeedbackInstanced', (GLenum, GLuint, GLsizei, ))
GL_PROC('GL_ARB_transform_feedback_instanced', None, 'glDrawTransformFeedbackStreamInstanced', (GLenum, GLuint, GLuint, GLsizei, ))
GL_PROC('GL_ARB_transpose_matrix', None, 'glLoadTransposeMatrixfARB', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_transpose_matrix', None, 'glLoadTransposeMatrixdARB', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_transpose_matrix', None, 'glMultTransposeMatrixfARB', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_transpose_matrix', None, 'glMultTransposeMatrixdARB', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_uniform_buffer_object', None, 'glGetUniformIndices', (GLuint, GLsizei, ctypes.POINTER(ctypes.POINTER(GLchar)), ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_uniform_buffer_object', None, 'glGetActiveUniformsiv', (GLuint, GLsizei, ctypes.POINTER(GLuint), GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_uniform_buffer_object', None, 'glGetActiveUniformName', (GLuint, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_uniform_buffer_object', GLuint, 'glGetUniformBlockIndex', (GLuint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_uniform_buffer_object', None, 'glGetActiveUniformBlockiv', (GLuint, GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_uniform_buffer_object', None, 'glGetActiveUniformBlockName', (GLuint, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_ARB_uniform_buffer_object', None, 'glUniformBlockBinding', (GLuint, GLuint, GLuint, ))
GL_PROC('GL_ARB_vertex_array_object', None, 'glBindVertexArray', (GLuint, ))
GL_PROC('GL_ARB_vertex_array_object', None, 'glDeleteVertexArrays', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_array_object', None, 'glGenVertexArrays', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_array_object', GLboolean, 'glIsVertexArray', (GLuint, ))
GL_PROC('GL_ARB_vertex_attrib_64bit', None, 'glVertexAttribL1d', (GLuint, GLdouble, ))
GL_PROC('GL_ARB_vertex_attrib_64bit', None, 'glVertexAttribL2d', (GLuint, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_vertex_attrib_64bit', None, 'glVertexAttribL3d', (GLuint, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_vertex_attrib_64bit', None, 'glVertexAttribL4d', (GLuint, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_vertex_attrib_64bit', None, 'glVertexAttribL1dv', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_attrib_64bit', None, 'glVertexAttribL2dv', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_attrib_64bit', None, 'glVertexAttribL3dv', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_attrib_64bit', None, 'glVertexAttribL4dv', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_attrib_64bit', None, 'glVertexAttribLPointer', (GLuint, GLint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_vertex_attrib_64bit', None, 'glGetVertexAttribLdv', (GLuint, GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_attrib_binding', None, 'glBindVertexBuffer', (GLuint, GLuint, GLintptr, GLsizei, ))
GL_PROC('GL_ARB_vertex_attrib_binding', None, 'glVertexAttribFormat', (GLuint, GLint, GLenum, GLboolean, GLuint, ))
GL_PROC('GL_ARB_vertex_attrib_binding', None, 'glVertexAttribIFormat', (GLuint, GLint, GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_attrib_binding', None, 'glVertexAttribLFormat', (GLuint, GLint, GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_attrib_binding', None, 'glVertexAttribBinding', (GLuint, GLuint, ))
GL_PROC('GL_ARB_vertex_attrib_binding', None, 'glVertexBindingDivisor', (GLuint, GLuint, ))
GL_PROC('GL_ARB_vertex_attrib_binding', None, 'glVertexArrayBindVertexBufferEXT', (GLuint, GLuint, GLuint, GLintptr, GLsizei, ))
GL_PROC('GL_ARB_vertex_attrib_binding', None, 'glVertexArrayVertexAttribFormatEXT', (GLuint, GLuint, GLint, GLenum, GLboolean, GLuint, ))
GL_PROC('GL_ARB_vertex_attrib_binding', None, 'glVertexArrayVertexAttribIFormatEXT', (GLuint, GLuint, GLint, GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_attrib_binding', None, 'glVertexArrayVertexAttribLFormatEXT', (GLuint, GLuint, GLint, GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_attrib_binding', None, 'glVertexArrayVertexAttribBindingEXT', (GLuint, GLuint, GLuint, ))
GL_PROC('GL_ARB_vertex_attrib_binding', None, 'glVertexArrayVertexBindingDivisorEXT', (GLuint, GLuint, GLuint, ))
GL_PROC('GL_ARB_vertex_blend', None, 'glWeightbvARB', (GLint, ctypes.POINTER(GLbyte), ))
GL_PROC('GL_ARB_vertex_blend', None, 'glWeightsvARB', (GLint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ARB_vertex_blend', None, 'glWeightivARB', (GLint, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_vertex_blend', None, 'glWeightfvARB', (GLint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_vertex_blend', None, 'glWeightdvARB', (GLint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_blend', None, 'glWeightubvARB', (GLint, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_ARB_vertex_blend', None, 'glWeightusvARB', (GLint, ctypes.POINTER(GLushort), ))
GL_PROC('GL_ARB_vertex_blend', None, 'glWeightuivARB', (GLint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_blend', None, 'glWeightPointerARB', (GLint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_vertex_blend', None, 'glVertexBlendARB', (GLint, ))
GL_PROC('GL_ARB_vertex_buffer_object', None, 'glBindBufferARB', (GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_buffer_object', None, 'glDeleteBuffersARB', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_buffer_object', None, 'glGenBuffersARB', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_buffer_object', GLboolean, 'glIsBufferARB', (GLuint, ))
GL_PROC('GL_ARB_vertex_buffer_object', None, 'glBufferDataARB', (GLenum, GLsizeiptrARB, ctypes.c_void_p, GLenum, ))
GL_PROC('GL_ARB_vertex_buffer_object', None, 'glBufferSubDataARB', (GLenum, GLintptrARB, GLsizeiptrARB, ctypes.c_void_p, ))
GL_PROC('GL_ARB_vertex_buffer_object', None, 'glGetBufferSubDataARB', (GLenum, GLintptrARB, GLsizeiptrARB, ctypes.c_void_p, ))
GL_PROC('GL_ARB_vertex_buffer_object', ctypes.c_void_p, 'glMapBufferARB', (GLenum, GLenum, ))
GL_PROC('GL_ARB_vertex_buffer_object', GLboolean, 'glUnmapBufferARB', (GLenum, ))
GL_PROC('GL_ARB_vertex_buffer_object', None, 'glGetBufferParameterivARB', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_vertex_buffer_object', None, 'glGetBufferPointervARB', (GLenum, GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib1dARB', (GLuint, GLdouble, ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib1dvARB', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib1fARB', (GLuint, GLfloat, ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib1fvARB', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib1sARB', (GLuint, GLshort, ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib1svARB', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib2dARB', (GLuint, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib2dvARB', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib2fARB', (GLuint, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib2fvARB', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib2sARB', (GLuint, GLshort, GLshort, ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib2svARB', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib3dARB', (GLuint, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib3dvARB', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib3fARB', (GLuint, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib3fvARB', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib3sARB', (GLuint, GLshort, GLshort, GLshort, ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib3svARB', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4NbvARB', (GLuint, ctypes.POINTER(GLbyte), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4NivARB', (GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4NsvARB', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4NubARB', (GLuint, GLubyte, GLubyte, GLubyte, GLubyte, ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4NubvARB', (GLuint, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4NuivARB', (GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4NusvARB', (GLuint, ctypes.POINTER(GLushort), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4bvARB', (GLuint, ctypes.POINTER(GLbyte), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4dARB', (GLuint, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4dvARB', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4fARB', (GLuint, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4fvARB', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4ivARB', (GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4sARB', (GLuint, GLshort, GLshort, GLshort, GLshort, ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4svARB', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4ubvARB', (GLuint, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4uivARB', (GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttrib4usvARB', (GLuint, ctypes.POINTER(GLushort), ))
GL_PROC('GL_ARB_vertex_program', None, 'glVertexAttribPointerARB', (GLuint, GLint, GLenum, GLboolean, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_vertex_program', None, 'glEnableVertexAttribArrayARB', (GLuint, ))
GL_PROC('GL_ARB_vertex_program', None, 'glDisableVertexAttribArrayARB', (GLuint, ))
GL_PROC('GL_ARB_vertex_program', None, 'glProgramStringARB', (GLenum, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_ARB_vertex_program', None, 'glBindProgramARB', (GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_program', None, 'glDeleteProgramsARB', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_program', None, 'glGenProgramsARB', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_program', None, 'glProgramEnvParameter4dARB', (GLenum, GLuint, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_vertex_program', None, 'glProgramEnvParameter4dvARB', (GLenum, GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_program', None, 'glProgramEnvParameter4fARB', (GLenum, GLuint, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_vertex_program', None, 'glProgramEnvParameter4fvARB', (GLenum, GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_vertex_program', None, 'glProgramLocalParameter4dARB', (GLenum, GLuint, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_vertex_program', None, 'glProgramLocalParameter4dvARB', (GLenum, GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_program', None, 'glProgramLocalParameter4fARB', (GLenum, GLuint, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_vertex_program', None, 'glProgramLocalParameter4fvARB', (GLenum, GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_vertex_program', None, 'glGetProgramEnvParameterdvARB', (GLenum, GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_program', None, 'glGetProgramEnvParameterfvARB', (GLenum, GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_vertex_program', None, 'glGetProgramLocalParameterdvARB', (GLenum, GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_program', None, 'glGetProgramLocalParameterfvARB', (GLenum, GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_vertex_program', None, 'glGetProgramivARB', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_vertex_program', None, 'glGetProgramStringARB', (GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_ARB_vertex_program', None, 'glGetVertexAttribdvARB', (GLuint, GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_vertex_program', None, 'glGetVertexAttribfvARB', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_vertex_program', None, 'glGetVertexAttribivARB', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_vertex_program', None, 'glGetVertexAttribPointervARB', (GLuint, GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_ARB_vertex_program', GLboolean, 'glIsProgramARB', (GLuint, ))
GL_PROC('GL_ARB_vertex_shader', None, 'glBindAttribLocationARB', (GLhandleARB, GLuint, ctypes.POINTER(GLcharARB), ))
GL_PROC('GL_ARB_vertex_shader', None, 'glGetActiveAttribARB', (GLhandleARB, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLint), ctypes.POINTER(GLenum), ctypes.POINTER(GLcharARB), ))
GL_PROC('GL_ARB_vertex_shader', GLint, 'glGetAttribLocationARB', (GLhandleARB, ctypes.POINTER(GLcharARB), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glVertexP2ui', (GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glVertexP2uiv', (GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glVertexP3ui', (GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glVertexP3uiv', (GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glVertexP4ui', (GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glVertexP4uiv', (GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glTexCoordP1ui', (GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glTexCoordP1uiv', (GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glTexCoordP2ui', (GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glTexCoordP2uiv', (GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glTexCoordP3ui', (GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glTexCoordP3uiv', (GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glTexCoordP4ui', (GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glTexCoordP4uiv', (GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glMultiTexCoordP1ui', (GLenum, GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glMultiTexCoordP1uiv', (GLenum, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glMultiTexCoordP2ui', (GLenum, GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glMultiTexCoordP2uiv', (GLenum, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glMultiTexCoordP3ui', (GLenum, GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glMultiTexCoordP3uiv', (GLenum, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glMultiTexCoordP4ui', (GLenum, GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glMultiTexCoordP4uiv', (GLenum, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glNormalP3ui', (GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glNormalP3uiv', (GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glColorP3ui', (GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glColorP3uiv', (GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glColorP4ui', (GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glColorP4uiv', (GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glSecondaryColorP3ui', (GLenum, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glSecondaryColorP3uiv', (GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glVertexAttribP1ui', (GLuint, GLenum, GLboolean, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glVertexAttribP1uiv', (GLuint, GLenum, GLboolean, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glVertexAttribP2ui', (GLuint, GLenum, GLboolean, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glVertexAttribP2uiv', (GLuint, GLenum, GLboolean, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glVertexAttribP3ui', (GLuint, GLenum, GLboolean, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glVertexAttribP3uiv', (GLuint, GLenum, GLboolean, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glVertexAttribP4ui', (GLuint, GLenum, GLboolean, GLuint, ))
GL_PROC('GL_ARB_vertex_type_2_10_10_10_rev', None, 'glVertexAttribP4uiv', (GLuint, GLenum, GLboolean, ctypes.POINTER(GLuint), ))
GL_PROC('GL_ARB_viewport_array', None, 'glViewportArrayv', (GLuint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_viewport_array', None, 'glViewportIndexedf', (GLuint, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_viewport_array', None, 'glViewportIndexedfv', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_viewport_array', None, 'glScissorArrayv', (GLuint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_viewport_array', None, 'glScissorIndexed', (GLuint, GLint, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_ARB_viewport_array', None, 'glScissorIndexedv', (GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_viewport_array', None, 'glDepthRangeArrayv', (GLuint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_viewport_array', None, 'glDepthRangeIndexed', (GLuint, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_viewport_array', None, 'glGetFloati_v', (GLenum, GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_viewport_array', None, 'glGetDoublei_v', (GLenum, GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos2dARB', (GLdouble, GLdouble, ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos2dvARB', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos2fARB', (GLfloat, GLfloat, ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos2fvARB', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos2iARB', (GLint, GLint, ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos2ivARB', (ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos2sARB', (GLshort, GLshort, ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos2svARB', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos3dARB', (GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos3dvARB', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos3fARB', (GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos3fvARB', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos3iARB', (GLint, GLint, GLint, ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos3ivARB', (ctypes.POINTER(GLint), ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos3sARB', (GLshort, GLshort, GLshort, ))
GL_PROC('GL_ARB_window_pos', None, 'glWindowPos3svARB', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_ATI_draw_buffers', None, 'glDrawBuffersATI', (GLsizei, ctypes.POINTER(GLenum), ))
GL_PROC('GL_ATI_element_array', None, 'glElementPointerATI', (GLenum, ctypes.c_void_p, ))
GL_PROC('GL_ATI_element_array', None, 'glDrawElementArrayATI', (GLenum, GLsizei, ))
GL_PROC('GL_ATI_element_array', None, 'glDrawRangeElementArrayATI', (GLenum, GLuint, GLuint, GLsizei, ))
GL_PROC('GL_ATI_envmap_bumpmap', None, 'glTexBumpParameterivATI', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ATI_envmap_bumpmap', None, 'glTexBumpParameterfvATI', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ATI_envmap_bumpmap', None, 'glGetTexBumpParameterivATI', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ATI_envmap_bumpmap', None, 'glGetTexBumpParameterfvATI', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ATI_fragment_shader', GLuint, 'glGenFragmentShadersATI', (GLuint, ))
GL_PROC('GL_ATI_fragment_shader', None, 'glBindFragmentShaderATI', (GLuint, ))
GL_PROC('GL_ATI_fragment_shader', None, 'glDeleteFragmentShaderATI', (GLuint, ))
GL_PROC('GL_ATI_fragment_shader', None, 'glBeginFragmentShaderATI', ())
GL_PROC('GL_ATI_fragment_shader', None, 'glEndFragmentShaderATI', ())
GL_PROC('GL_ATI_fragment_shader', None, 'glPassTexCoordATI', (GLuint, GLuint, GLenum, ))
GL_PROC('GL_ATI_fragment_shader', None, 'glSampleMapATI', (GLuint, GLuint, GLenum, ))
GL_PROC('GL_ATI_fragment_shader', None, 'glColorFragmentOp1ATI', (GLenum, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_ATI_fragment_shader', None, 'glColorFragmentOp2ATI', (GLenum, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_ATI_fragment_shader', None, 'glColorFragmentOp3ATI', (GLenum, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_ATI_fragment_shader', None, 'glAlphaFragmentOp1ATI', (GLenum, GLuint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_ATI_fragment_shader', None, 'glAlphaFragmentOp2ATI', (GLenum, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_ATI_fragment_shader', None, 'glAlphaFragmentOp3ATI', (GLenum, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_ATI_fragment_shader', None, 'glSetFragmentShaderConstantATI', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ATI_map_object_buffer', ctypes.c_void_p, 'glMapObjectBufferATI', (GLuint, ))
GL_PROC('GL_ATI_map_object_buffer', None, 'glUnmapObjectBufferATI', (GLuint, ))
GL_PROC('GL_ATI_pn_triangles', None, 'glPNTrianglesiATI', (GLenum, GLint, ))
GL_PROC('GL_ATI_pn_triangles', None, 'glPNTrianglesfATI', (GLenum, GLfloat, ))
GL_PROC('GL_ATI_separate_stencil', None, 'glStencilOpSeparateATI', (GLenum, GLenum, GLenum, GLenum, ))
GL_PROC('GL_ATI_separate_stencil', None, 'glStencilFuncSeparateATI', (GLenum, GLenum, GLint, GLuint, ))
GL_PROC('GL_ATI_vertex_array_object', GLuint, 'glNewObjectBufferATI', (GLsizei, ctypes.c_void_p, GLenum, ))
GL_PROC('GL_ATI_vertex_array_object', GLboolean, 'glIsObjectBufferATI', (GLuint, ))
GL_PROC('GL_ATI_vertex_array_object', None, 'glUpdateObjectBufferATI', (GLuint, GLuint, GLsizei, ctypes.c_void_p, GLenum, ))
GL_PROC('GL_ATI_vertex_array_object', None, 'glGetObjectBufferfvATI', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ATI_vertex_array_object', None, 'glGetObjectBufferivATI', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ATI_vertex_array_object', None, 'glFreeObjectBufferATI', (GLuint, ))
GL_PROC('GL_ATI_vertex_array_object', None, 'glArrayObjectATI', (GLenum, GLint, GLenum, GLsizei, GLuint, GLuint, ))
GL_PROC('GL_ATI_vertex_array_object', None, 'glGetArrayObjectfvATI', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ATI_vertex_array_object', None, 'glGetArrayObjectivATI', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ATI_vertex_array_object', None, 'glVariantArrayObjectATI', (GLuint, GLenum, GLsizei, GLuint, GLuint, ))
GL_PROC('GL_ATI_vertex_array_object', None, 'glGetVariantArrayObjectfvATI', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ATI_vertex_array_object', None, 'glGetVariantArrayObjectivATI', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ATI_vertex_attrib_array_object', None, 'glVertexAttribArrayObjectATI', (GLuint, GLint, GLenum, GLboolean, GLsizei, GLuint, GLuint, ))
GL_PROC('GL_ATI_vertex_attrib_array_object', None, 'glGetVertexAttribArrayObjectfvATI', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ATI_vertex_attrib_array_object', None, 'glGetVertexAttribArrayObjectivATI', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream1sATI', (GLenum, GLshort, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream1svATI', (GLenum, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream1iATI', (GLenum, GLint, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream1ivATI', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream1fATI', (GLenum, GLfloat, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream1fvATI', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream1dATI', (GLenum, GLdouble, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream1dvATI', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream2sATI', (GLenum, GLshort, GLshort, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream2svATI', (GLenum, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream2iATI', (GLenum, GLint, GLint, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream2ivATI', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream2fATI', (GLenum, GLfloat, GLfloat, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream2fvATI', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream2dATI', (GLenum, GLdouble, GLdouble, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream2dvATI', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream3sATI', (GLenum, GLshort, GLshort, GLshort, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream3svATI', (GLenum, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream3iATI', (GLenum, GLint, GLint, GLint, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream3ivATI', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream3fATI', (GLenum, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream3fvATI', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream3dATI', (GLenum, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream3dvATI', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream4sATI', (GLenum, GLshort, GLshort, GLshort, GLshort, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream4svATI', (GLenum, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream4iATI', (GLenum, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream4ivATI', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream4fATI', (GLenum, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream4fvATI', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream4dATI', (GLenum, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexStream4dvATI', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glNormalStream3bATI', (GLenum, GLbyte, GLbyte, GLbyte, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glNormalStream3bvATI', (GLenum, ctypes.POINTER(GLbyte), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glNormalStream3sATI', (GLenum, GLshort, GLshort, GLshort, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glNormalStream3svATI', (GLenum, ctypes.POINTER(GLshort), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glNormalStream3iATI', (GLenum, GLint, GLint, GLint, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glNormalStream3ivATI', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glNormalStream3fATI', (GLenum, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glNormalStream3fvATI', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glNormalStream3dATI', (GLenum, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glNormalStream3dvATI', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_ATI_vertex_streams', None, 'glClientActiveVertexStreamATI', (GLenum, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexBlendEnviATI', (GLenum, GLint, ))
GL_PROC('GL_ATI_vertex_streams', None, 'glVertexBlendEnvfATI', (GLenum, GLfloat, ))
GL_PROC('GL_EXT_bindable_uniform', None, 'glUniformBufferEXT', (GLuint, GLint, GLuint, ))
GL_PROC('GL_EXT_bindable_uniform', GLint, 'glGetUniformBufferSizeEXT', (GLuint, GLint, ))
GL_PROC('GL_EXT_bindable_uniform', GLintptr, 'glGetUniformOffsetEXT', (GLuint, GLint, ))
GL_PROC('GL_EXT_blend_color', None, 'glBlendColorEXT', (GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_EXT_blend_equation_separate', None, 'glBlendEquationSeparateEXT', (GLenum, GLenum, ))
GL_PROC('GL_EXT_blend_func_separate', None, 'glBlendFuncSeparateEXT', (GLenum, GLenum, GLenum, GLenum, ))
GL_PROC('GL_EXT_blend_minmax', None, 'glBlendEquationEXT', (GLenum, ))
GL_PROC('GL_EXT_color_subtable', None, 'glColorSubTableEXT', (GLenum, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_color_subtable', None, 'glCopyColorSubTableEXT', (GLenum, GLsizei, GLint, GLint, GLsizei, ))
GL_PROC('GL_EXT_compiled_vertex_array', None, 'glLockArraysEXT', (GLint, GLsizei, ))
GL_PROC('GL_EXT_compiled_vertex_array', None, 'glUnlockArraysEXT', ())
GL_PROC('GL_EXT_convolution', None, 'glConvolutionFilter1DEXT', (GLenum, GLenum, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_convolution', None, 'glConvolutionFilter2DEXT', (GLenum, GLenum, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_convolution', None, 'glConvolutionParameterfEXT', (GLenum, GLenum, GLfloat, ))
GL_PROC('GL_EXT_convolution', None, 'glConvolutionParameterfvEXT', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_convolution', None, 'glConvolutionParameteriEXT', (GLenum, GLenum, GLint, ))
GL_PROC('GL_EXT_convolution', None, 'glConvolutionParameterivEXT', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_convolution', None, 'glCopyConvolutionFilter1DEXT', (GLenum, GLenum, GLint, GLint, GLsizei, ))
GL_PROC('GL_EXT_convolution', None, 'glCopyConvolutionFilter2DEXT', (GLenum, GLenum, GLint, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_EXT_convolution', None, 'glGetConvolutionFilterEXT', (GLenum, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_convolution', None, 'glGetConvolutionParameterfvEXT', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_convolution', None, 'glGetConvolutionParameterivEXT', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_convolution', None, 'glGetSeparableFilterEXT', (GLenum, GLenum, GLenum, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ))
GL_PROC('GL_EXT_convolution', None, 'glSeparableFilter2DEXT', (GLenum, GLenum, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ctypes.c_void_p, ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glTangent3bEXT', (GLbyte, GLbyte, GLbyte, ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glTangent3bvEXT', (ctypes.POINTER(GLbyte), ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glTangent3dEXT', (GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glTangent3dvEXT', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glTangent3fEXT', (GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glTangent3fvEXT', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glTangent3iEXT', (GLint, GLint, GLint, ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glTangent3ivEXT', (ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glTangent3sEXT', (GLshort, GLshort, GLshort, ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glTangent3svEXT', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glBinormal3bEXT', (GLbyte, GLbyte, GLbyte, ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glBinormal3bvEXT', (ctypes.POINTER(GLbyte), ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glBinormal3dEXT', (GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glBinormal3dvEXT', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glBinormal3fEXT', (GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glBinormal3fvEXT', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glBinormal3iEXT', (GLint, GLint, GLint, ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glBinormal3ivEXT', (ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glBinormal3sEXT', (GLshort, GLshort, GLshort, ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glBinormal3svEXT', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glTangentPointerEXT', (GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_coordinate_frame', None, 'glBinormalPointerEXT', (GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_copy_texture', None, 'glCopyTexImage1DEXT', (GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLint, ))
GL_PROC('GL_EXT_copy_texture', None, 'glCopyTexImage2DEXT', (GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLsizei, GLint, ))
GL_PROC('GL_EXT_copy_texture', None, 'glCopyTexSubImage1DEXT', (GLenum, GLint, GLint, GLint, GLint, GLsizei, ))
GL_PROC('GL_EXT_copy_texture', None, 'glCopyTexSubImage2DEXT', (GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_EXT_copy_texture', None, 'glCopyTexSubImage3DEXT', (GLenum, GLint, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_EXT_cull_vertex', None, 'glCullParameterdvEXT', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_cull_vertex', None, 'glCullParameterfvEXT', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_depth_bounds_test', None, 'glDepthBoundsEXT', (GLclampd, GLclampd, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glClientAttribDefaultEXT', (GLbitfield, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glPushClientAttribDefaultEXT', (GLbitfield, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixLoadfEXT', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixLoaddEXT', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixMultfEXT', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixMultdEXT', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixLoadIdentityEXT', (GLenum, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixRotatefEXT', (GLenum, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixRotatedEXT', (GLenum, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixScalefEXT', (GLenum, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixScaledEXT', (GLenum, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixTranslatefEXT', (GLenum, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixTranslatedEXT', (GLenum, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixFrustumEXT', (GLenum, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixOrthoEXT', (GLenum, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixPopEXT', (GLenum, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixPushEXT', (GLenum, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixLoadTransposefEXT', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixLoadTransposedEXT', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixMultTransposefEXT', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMatrixMultTransposedEXT', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glTextureParameterfEXT', (GLuint, GLenum, GLenum, GLfloat, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glTextureParameterfvEXT', (GLuint, GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glTextureParameteriEXT', (GLuint, GLenum, GLenum, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glTextureParameterivEXT', (GLuint, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glTextureImage1DEXT', (GLuint, GLenum, GLint, GLenum, GLsizei, GLint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glTextureImage2DEXT', (GLuint, GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glTextureSubImage1DEXT', (GLuint, GLenum, GLint, GLint, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glTextureSubImage2DEXT', (GLuint, GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCopyTextureImage1DEXT', (GLuint, GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCopyTextureImage2DEXT', (GLuint, GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLsizei, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCopyTextureSubImage1DEXT', (GLuint, GLenum, GLint, GLint, GLint, GLint, GLsizei, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCopyTextureSubImage2DEXT', (GLuint, GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetTextureImageEXT', (GLuint, GLenum, GLint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetTextureParameterfvEXT', (GLuint, GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetTextureParameterivEXT', (GLuint, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetTextureLevelParameterfvEXT', (GLuint, GLenum, GLint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetTextureLevelParameterivEXT', (GLuint, GLenum, GLint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glTextureImage3DEXT', (GLuint, GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glTextureSubImage3DEXT', (GLuint, GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCopyTextureSubImage3DEXT', (GLuint, GLenum, GLint, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexParameterfEXT', (GLenum, GLenum, GLenum, GLfloat, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexParameterfvEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexParameteriEXT', (GLenum, GLenum, GLenum, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexParameterivEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexImage1DEXT', (GLenum, GLenum, GLint, GLenum, GLsizei, GLint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexImage2DEXT', (GLenum, GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexSubImage1DEXT', (GLenum, GLenum, GLint, GLint, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexSubImage2DEXT', (GLenum, GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCopyMultiTexImage1DEXT', (GLenum, GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCopyMultiTexImage2DEXT', (GLenum, GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLsizei, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCopyMultiTexSubImage1DEXT', (GLenum, GLenum, GLint, GLint, GLint, GLint, GLsizei, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCopyMultiTexSubImage2DEXT', (GLenum, GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetMultiTexImageEXT', (GLenum, GLenum, GLint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetMultiTexParameterfvEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetMultiTexParameterivEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetMultiTexLevelParameterfvEXT', (GLenum, GLenum, GLint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetMultiTexLevelParameterivEXT', (GLenum, GLenum, GLint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexImage3DEXT', (GLenum, GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexSubImage3DEXT', (GLenum, GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCopyMultiTexSubImage3DEXT', (GLenum, GLenum, GLint, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glBindMultiTextureEXT', (GLenum, GLenum, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glEnableClientStateIndexedEXT', (GLenum, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glDisableClientStateIndexedEXT', (GLenum, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glEnableClientStateiEXT', (GLenum, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glDisableClientStateiEXT', (GLenum, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexCoordPointerEXT', (GLenum, GLint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexEnvfEXT', (GLenum, GLenum, GLenum, GLfloat, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexEnvfvEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexEnviEXT', (GLenum, GLenum, GLenum, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexEnvivEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexGendEXT', (GLenum, GLenum, GLenum, GLdouble, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexGendvEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexGenfEXT', (GLenum, GLenum, GLenum, GLfloat, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexGenfvEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexGeniEXT', (GLenum, GLenum, GLenum, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexGenivEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetMultiTexEnvfvEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetMultiTexEnvivEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetMultiTexGendvEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetMultiTexGenfvEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetMultiTexGenivEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetFloatIndexedvEXT', (GLenum, GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetDoubleIndexedvEXT', (GLenum, GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetPointerIndexedvEXT', (GLenum, GLuint, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetFloati_vEXT', (GLenum, GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetDoublei_vEXT', (GLenum, GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetPointeri_vEXT', (GLenum, GLuint, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCompressedTextureImage3DEXT', (GLuint, GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCompressedTextureImage2DEXT', (GLuint, GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCompressedTextureImage1DEXT', (GLuint, GLenum, GLint, GLenum, GLsizei, GLint, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCompressedTextureSubImage3DEXT', (GLuint, GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCompressedTextureSubImage2DEXT', (GLuint, GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCompressedTextureSubImage1DEXT', (GLuint, GLenum, GLint, GLint, GLsizei, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetCompressedTextureImageEXT', (GLuint, GLenum, GLint, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCompressedMultiTexImage3DEXT', (GLenum, GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCompressedMultiTexImage2DEXT', (GLenum, GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCompressedMultiTexImage1DEXT', (GLenum, GLenum, GLint, GLenum, GLsizei, GLint, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCompressedMultiTexSubImage3DEXT', (GLenum, GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCompressedMultiTexSubImage2DEXT', (GLenum, GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glCompressedMultiTexSubImage1DEXT', (GLenum, GLenum, GLint, GLint, GLsizei, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetCompressedMultiTexImageEXT', (GLenum, GLenum, GLint, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedProgramStringEXT', (GLuint, GLenum, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedProgramLocalParameter4dEXT', (GLuint, GLenum, GLuint, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedProgramLocalParameter4dvEXT', (GLuint, GLenum, GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedProgramLocalParameter4fEXT', (GLuint, GLenum, GLuint, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedProgramLocalParameter4fvEXT', (GLuint, GLenum, GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetNamedProgramLocalParameterdvEXT', (GLuint, GLenum, GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetNamedProgramLocalParameterfvEXT', (GLuint, GLenum, GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetNamedProgramivEXT', (GLuint, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetNamedProgramStringEXT', (GLuint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedProgramLocalParameters4fvEXT', (GLuint, GLenum, GLuint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedProgramLocalParameterI4iEXT', (GLuint, GLenum, GLuint, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedProgramLocalParameterI4ivEXT', (GLuint, GLenum, GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedProgramLocalParametersI4ivEXT', (GLuint, GLenum, GLuint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedProgramLocalParameterI4uiEXT', (GLuint, GLenum, GLuint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedProgramLocalParameterI4uivEXT', (GLuint, GLenum, GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedProgramLocalParametersI4uivEXT', (GLuint, GLenum, GLuint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetNamedProgramLocalParameterIivEXT', (GLuint, GLenum, GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetNamedProgramLocalParameterIuivEXT', (GLuint, GLenum, GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glTextureParameterIivEXT', (GLuint, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glTextureParameterIuivEXT', (GLuint, GLenum, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetTextureParameterIivEXT', (GLuint, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetTextureParameterIuivEXT', (GLuint, GLenum, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexParameterIivEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexParameterIuivEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetMultiTexParameterIivEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetMultiTexParameterIuivEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform1fEXT', (GLuint, GLint, GLfloat, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform2fEXT', (GLuint, GLint, GLfloat, GLfloat, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform3fEXT', (GLuint, GLint, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform4fEXT', (GLuint, GLint, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform1iEXT', (GLuint, GLint, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform2iEXT', (GLuint, GLint, GLint, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform3iEXT', (GLuint, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform4iEXT', (GLuint, GLint, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform1fvEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform2fvEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform3fvEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform4fvEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform1ivEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform2ivEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform3ivEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform4ivEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix2fvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix3fvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix4fvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix2x3fvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix3x2fvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix2x4fvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix4x2fvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix3x4fvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix4x3fvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform1uiEXT', (GLuint, GLint, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform2uiEXT', (GLuint, GLint, GLuint, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform3uiEXT', (GLuint, GLint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform4uiEXT', (GLuint, GLint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform1uivEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform2uivEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform3uivEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform4uivEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedBufferDataEXT', (GLuint, GLsizeiptr, ctypes.c_void_p, GLenum, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedBufferSubDataEXT', (GLuint, GLintptr, GLsizeiptr, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', ctypes.c_void_p, 'glMapNamedBufferEXT', (GLuint, GLenum, ))
GL_PROC('GL_EXT_direct_state_access', GLboolean, 'glUnmapNamedBufferEXT', (GLuint, ))
GL_PROC('GL_EXT_direct_state_access', ctypes.c_void_p, 'glMapNamedBufferRangeEXT', (GLuint, GLintptr, GLsizeiptr, GLbitfield, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glFlushMappedNamedBufferRangeEXT', (GLuint, GLintptr, GLsizeiptr, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedCopyBufferSubDataEXT', (GLuint, GLuint, GLintptr, GLintptr, GLsizeiptr, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetNamedBufferParameterivEXT', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetNamedBufferPointervEXT', (GLuint, GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetNamedBufferSubDataEXT', (GLuint, GLintptr, GLsizeiptr, ctypes.c_void_p, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glTextureBufferEXT', (GLuint, GLenum, GLenum, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexBufferEXT', (GLenum, GLenum, GLenum, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedRenderbufferStorageEXT', (GLuint, GLenum, GLsizei, GLsizei, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetNamedRenderbufferParameterivEXT', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', GLenum, 'glCheckNamedFramebufferStatusEXT', (GLuint, GLenum, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedFramebufferTexture1DEXT', (GLuint, GLenum, GLenum, GLuint, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedFramebufferTexture2DEXT', (GLuint, GLenum, GLenum, GLuint, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedFramebufferTexture3DEXT', (GLuint, GLenum, GLenum, GLuint, GLint, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedFramebufferRenderbufferEXT', (GLuint, GLenum, GLenum, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetNamedFramebufferAttachmentParameterivEXT', (GLuint, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGenerateTextureMipmapEXT', (GLuint, GLenum, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGenerateMultiTexMipmapEXT', (GLenum, GLenum, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glFramebufferDrawBufferEXT', (GLuint, GLenum, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glFramebufferDrawBuffersEXT', (GLuint, GLsizei, ctypes.POINTER(GLenum), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glFramebufferReadBufferEXT', (GLuint, GLenum, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetFramebufferParameterivEXT', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedRenderbufferStorageMultisampleEXT', (GLuint, GLsizei, GLenum, GLsizei, GLsizei, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedRenderbufferStorageMultisampleCoverageEXT', (GLuint, GLsizei, GLsizei, GLenum, GLsizei, GLsizei, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedFramebufferTextureEXT', (GLuint, GLenum, GLuint, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedFramebufferTextureLayerEXT', (GLuint, GLenum, GLuint, GLint, GLint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glNamedFramebufferTextureFaceEXT', (GLuint, GLenum, GLuint, GLint, GLenum, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glTextureRenderbufferEXT', (GLuint, GLenum, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glMultiTexRenderbufferEXT', (GLenum, GLenum, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform1dEXT', (GLuint, GLint, GLdouble, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform2dEXT', (GLuint, GLint, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform3dEXT', (GLuint, GLint, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform4dEXT', (GLuint, GLint, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform1dvEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform2dvEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform3dvEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniform4dvEXT', (GLuint, GLint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix2dvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix3dvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix4dvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix2x3dvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix2x4dvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix3x2dvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix3x4dvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix4x2dvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glProgramUniformMatrix4x3dvEXT', (GLuint, GLint, GLsizei, GLboolean, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glEnableVertexArrayAttribEXT', (GLuint, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glDisableVertexArrayAttribEXT', (GLuint, GLuint, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glEnableVertexArrayEXT', (GLuint, GLenum, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glDisableVertexArrayEXT', (GLuint, GLenum, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glVertexArrayColorOffsetEXT', (GLuint, GLuint, GLint, GLenum, GLsizei, GLintptr, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glVertexArrayEdgeFlagOffsetEXT', (GLuint, GLuint, GLsizei, GLintptr, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glVertexArrayFogCoordOffsetEXT', (GLuint, GLuint, GLenum, GLsizei, GLintptr, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glVertexArrayIndexOffsetEXT', (GLuint, GLuint, GLenum, GLsizei, GLintptr, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glVertexArrayMultiTexCoordOffsetEXT', (GLuint, GLuint, GLenum, GLint, GLenum, GLsizei, GLintptr, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glVertexArrayNormalOffsetEXT', (GLuint, GLuint, GLenum, GLsizei, GLintptr, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glVertexArraySecondaryColorOffsetEXT', (GLuint, GLuint, GLint, GLenum, GLsizei, GLintptr, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glVertexArrayTexCoordOffsetEXT', (GLuint, GLuint, GLint, GLenum, GLsizei, GLintptr, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glVertexArrayVertexOffsetEXT', (GLuint, GLuint, GLint, GLenum, GLsizei, GLintptr, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glVertexArrayVertexAttribIOffsetEXT', (GLuint, GLuint, GLuint, GLint, GLenum, GLsizei, GLintptr, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glVertexArrayVertexAttribOffsetEXT', (GLuint, GLuint, GLuint, GLint, GLenum, GLboolean, GLsizei, GLintptr, ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetVertexArrayIntegervEXT', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetVertexArrayPointervEXT', (GLuint, GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetVertexArrayIntegeri_vEXT', (GLuint, GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_direct_state_access', None, 'glGetVertexArrayPointeri_vEXT', (GLuint, GLuint, GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_EXT_draw_buffers2', None, 'glColorMaskIndexedEXT', (GLuint, GLboolean, GLboolean, GLboolean, GLboolean, ))
GL_PROC('GL_EXT_draw_buffers2', None, 'glGetBooleanIndexedvEXT', (GLenum, GLuint, ctypes.POINTER(GLboolean), ))
GL_PROC('GL_EXT_draw_buffers2', None, 'glGetIntegerIndexedvEXT', (GLenum, GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_draw_buffers2', None, 'glEnableIndexedEXT', (GLenum, GLuint, ))
GL_PROC('GL_EXT_draw_buffers2', None, 'glDisableIndexedEXT', (GLenum, GLuint, ))
GL_PROC('GL_EXT_draw_buffers2', GLboolean, 'glIsEnabledIndexedEXT', (GLenum, GLuint, ))
GL_PROC('GL_EXT_draw_instanced', None, 'glDrawArraysInstancedEXT', (GLenum, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_EXT_draw_instanced', None, 'glDrawElementsInstancedEXT', (GLenum, GLsizei, GLenum, ctypes.c_void_p, GLsizei, ))
GL_PROC('GL_EXT_draw_range_elements', None, 'glDrawRangeElementsEXT', (GLenum, GLuint, GLuint, GLsizei, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_fog_coord', None, 'glFogCoordfEXT', (GLfloat, ))
GL_PROC('GL_EXT_fog_coord', None, 'glFogCoordfvEXT', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_fog_coord', None, 'glFogCoorddEXT', (GLdouble, ))
GL_PROC('GL_EXT_fog_coord', None, 'glFogCoorddvEXT', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_fog_coord', None, 'glFogCoordPointerEXT', (GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_framebuffer_blit', None, 'glBlitFramebufferEXT', (GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLbitfield, GLenum, ))
GL_PROC('GL_EXT_framebuffer_multisample', None, 'glRenderbufferStorageMultisampleEXT', (GLenum, GLsizei, GLenum, GLsizei, GLsizei, ))
GL_PROC('GL_EXT_framebuffer_object', GLboolean, 'glIsRenderbufferEXT', (GLuint, ))
GL_PROC('GL_EXT_framebuffer_object', None, 'glBindRenderbufferEXT', (GLenum, GLuint, ))
GL_PROC('GL_EXT_framebuffer_object', None, 'glDeleteRenderbuffersEXT', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_framebuffer_object', None, 'glGenRenderbuffersEXT', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_framebuffer_object', None, 'glRenderbufferStorageEXT', (GLenum, GLenum, GLsizei, GLsizei, ))
GL_PROC('GL_EXT_framebuffer_object', None, 'glGetRenderbufferParameterivEXT', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_framebuffer_object', GLboolean, 'glIsFramebufferEXT', (GLuint, ))
GL_PROC('GL_EXT_framebuffer_object', None, 'glBindFramebufferEXT', (GLenum, GLuint, ))
GL_PROC('GL_EXT_framebuffer_object', None, 'glDeleteFramebuffersEXT', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_framebuffer_object', None, 'glGenFramebuffersEXT', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_framebuffer_object', GLenum, 'glCheckFramebufferStatusEXT', (GLenum, ))
GL_PROC('GL_EXT_framebuffer_object', None, 'glFramebufferTexture1DEXT', (GLenum, GLenum, GLenum, GLuint, GLint, ))
GL_PROC('GL_EXT_framebuffer_object', None, 'glFramebufferTexture2DEXT', (GLenum, GLenum, GLenum, GLuint, GLint, ))
GL_PROC('GL_EXT_framebuffer_object', None, 'glFramebufferTexture3DEXT', (GLenum, GLenum, GLenum, GLuint, GLint, GLint, ))
GL_PROC('GL_EXT_framebuffer_object', None, 'glFramebufferRenderbufferEXT', (GLenum, GLenum, GLenum, GLuint, ))
GL_PROC('GL_EXT_framebuffer_object', None, 'glGetFramebufferAttachmentParameterivEXT', (GLenum, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_framebuffer_object', None, 'glGenerateMipmapEXT', (GLenum, ))
GL_PROC('GL_EXT_geometry_shader4', None, 'glProgramParameteriEXT', (GLuint, GLenum, GLint, ))
GL_PROC('GL_EXT_gpu_program_parameters', None, 'glProgramEnvParameters4fvEXT', (GLenum, GLuint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_gpu_program_parameters', None, 'glProgramLocalParameters4fvEXT', (GLenum, GLuint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_gpu_shader4', None, 'glGetUniformuivEXT', (GLuint, GLint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_gpu_shader4', None, 'glBindFragDataLocationEXT', (GLuint, GLuint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_EXT_gpu_shader4', GLint, 'glGetFragDataLocationEXT', (GLuint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_EXT_gpu_shader4', None, 'glUniform1uiEXT', (GLint, GLuint, ))
GL_PROC('GL_EXT_gpu_shader4', None, 'glUniform2uiEXT', (GLint, GLuint, GLuint, ))
GL_PROC('GL_EXT_gpu_shader4', None, 'glUniform3uiEXT', (GLint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_EXT_gpu_shader4', None, 'glUniform4uiEXT', (GLint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_EXT_gpu_shader4', None, 'glUniform1uivEXT', (GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_gpu_shader4', None, 'glUniform2uivEXT', (GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_gpu_shader4', None, 'glUniform3uivEXT', (GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_gpu_shader4', None, 'glUniform4uivEXT', (GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_histogram', None, 'glGetHistogramEXT', (GLenum, GLboolean, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_histogram', None, 'glGetHistogramParameterfvEXT', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_histogram', None, 'glGetHistogramParameterivEXT', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_histogram', None, 'glGetMinmaxEXT', (GLenum, GLboolean, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_histogram', None, 'glGetMinmaxParameterfvEXT', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_histogram', None, 'glGetMinmaxParameterivEXT', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_histogram', None, 'glHistogramEXT', (GLenum, GLsizei, GLenum, GLboolean, ))
GL_PROC('GL_EXT_histogram', None, 'glMinmaxEXT', (GLenum, GLenum, GLboolean, ))
GL_PROC('GL_EXT_histogram', None, 'glResetHistogramEXT', (GLenum, ))
GL_PROC('GL_EXT_histogram', None, 'glResetMinmaxEXT', (GLenum, ))
GL_PROC('GL_EXT_index_func', None, 'glIndexFuncEXT', (GLenum, GLclampf, ))
GL_PROC('GL_EXT_index_material', None, 'glIndexMaterialEXT', (GLenum, GLenum, ))
GL_PROC('GL_EXT_light_texture', None, 'glApplyTextureEXT', (GLenum, ))
GL_PROC('GL_EXT_light_texture', None, 'glTextureLightEXT', (GLenum, ))
GL_PROC('GL_EXT_light_texture', None, 'glTextureMaterialEXT', (GLenum, GLenum, ))
GL_PROC('GL_EXT_multi_draw_arrays', None, 'glMultiDrawArraysEXT', (GLenum, ctypes.POINTER(GLint), ctypes.POINTER(GLsizei), GLsizei, ))
GL_PROC('GL_EXT_multi_draw_arrays', None, 'glMultiDrawElementsEXT', (GLenum, ctypes.POINTER(GLsizei), GLenum, ctypes.POINTER(ctypes.c_void_p), GLsizei, ))
GL_PROC('GL_EXT_multisample', None, 'glSampleMaskEXT', (GLclampf, GLboolean, ))
GL_PROC('GL_EXT_multisample', None, 'glSamplePatternEXT', (GLenum, ))
GL_PROC('GL_EXT_paletted_texture', None, 'glColorTableEXT', (GLenum, GLenum, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_paletted_texture', None, 'glGetColorTableEXT', (GLenum, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_paletted_texture', None, 'glGetColorTableParameterivEXT', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_paletted_texture', None, 'glGetColorTableParameterfvEXT', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_pixel_transform', None, 'glPixelTransformParameteriEXT', (GLenum, GLenum, GLint, ))
GL_PROC('GL_EXT_pixel_transform', None, 'glPixelTransformParameterfEXT', (GLenum, GLenum, GLfloat, ))
GL_PROC('GL_EXT_pixel_transform', None, 'glPixelTransformParameterivEXT', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_pixel_transform', None, 'glPixelTransformParameterfvEXT', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_pixel_transform', None, 'glGetPixelTransformParameterivEXT', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_pixel_transform', None, 'glGetPixelTransformParameterfvEXT', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_point_parameters', None, 'glPointParameterfEXT', (GLenum, GLfloat, ))
GL_PROC('GL_EXT_point_parameters', None, 'glPointParameterfvEXT', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_polygon_offset', None, 'glPolygonOffsetEXT', (GLfloat, GLfloat, ))
GL_PROC('GL_EXT_provoking_vertex', None, 'glProvokingVertexEXT', (GLenum, ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3bEXT', (GLbyte, GLbyte, GLbyte, ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3bvEXT', (ctypes.POINTER(GLbyte), ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3dEXT', (GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3dvEXT', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3fEXT', (GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3fvEXT', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3iEXT', (GLint, GLint, GLint, ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3ivEXT', (ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3sEXT', (GLshort, GLshort, GLshort, ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3svEXT', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3ubEXT', (GLubyte, GLubyte, GLubyte, ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3ubvEXT', (ctypes.POINTER(GLubyte), ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3uiEXT', (GLuint, GLuint, GLuint, ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3uivEXT', (ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3usEXT', (GLushort, GLushort, GLushort, ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColor3usvEXT', (ctypes.POINTER(GLushort), ))
GL_PROC('GL_EXT_secondary_color', None, 'glSecondaryColorPointerEXT', (GLint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_separate_shader_objects', None, 'glUseShaderProgramEXT', (GLenum, GLuint, ))
GL_PROC('GL_EXT_separate_shader_objects', None, 'glActiveProgramEXT', (GLuint, ))
GL_PROC('GL_EXT_separate_shader_objects', GLuint, 'glCreateShaderProgramEXT', (GLenum, ctypes.POINTER(GLchar), ))
GL_PROC('GL_EXT_shader_image_load_store', None, 'glBindImageTextureEXT', (GLuint, GLuint, GLint, GLboolean, GLint, GLenum, GLint, ))
GL_PROC('GL_EXT_shader_image_load_store', None, 'glMemoryBarrierEXT', (GLbitfield, ))
GL_PROC('GL_EXT_stencil_clear_tag', None, 'glStencilClearTagEXT', (GLsizei, GLuint, ))
GL_PROC('GL_EXT_stencil_two_side', None, 'glActiveStencilFaceEXT', (GLenum, ))
GL_PROC('GL_EXT_subtexture', None, 'glTexSubImage1DEXT', (GLenum, GLint, GLint, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_subtexture', None, 'glTexSubImage2DEXT', (GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_texture3D', None, 'glTexImage3DEXT', (GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_texture3D', None, 'glTexSubImage3DEXT', (GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_texture_buffer_object', None, 'glTexBufferEXT', (GLenum, GLenum, GLuint, ))
GL_PROC('GL_EXT_texture_integer', None, 'glTexParameterIivEXT', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_texture_integer', None, 'glTexParameterIuivEXT', (GLenum, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_texture_integer', None, 'glGetTexParameterIivEXT', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_texture_integer', None, 'glGetTexParameterIuivEXT', (GLenum, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_texture_integer', None, 'glClearColorIiEXT', (GLint, GLint, GLint, GLint, ))
GL_PROC('GL_EXT_texture_integer', None, 'glClearColorIuiEXT', (GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_EXT_texture_object', GLboolean, 'glAreTexturesResidentEXT', (GLsizei, ctypes.POINTER(GLuint), ctypes.POINTER(GLboolean), ))
GL_PROC('GL_EXT_texture_object', None, 'glBindTextureEXT', (GLenum, GLuint, ))
GL_PROC('GL_EXT_texture_object', None, 'glDeleteTexturesEXT', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_texture_object', None, 'glGenTexturesEXT', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_texture_object', GLboolean, 'glIsTextureEXT', (GLuint, ))
GL_PROC('GL_EXT_texture_object', None, 'glPrioritizeTexturesEXT', (GLsizei, ctypes.POINTER(GLuint), ctypes.POINTER(GLclampf), ))
GL_PROC('GL_EXT_texture_perturb_normal', None, 'glTextureNormalEXT', (GLenum, ))
GL_PROC('GL_EXT_timer_query', None, 'glGetQueryObjecti64vEXT', (GLuint, GLenum, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_EXT_timer_query', None, 'glGetQueryObjectui64vEXT', (GLuint, GLenum, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_EXT_transform_feedback', None, 'glBeginTransformFeedbackEXT', (GLenum, ))
GL_PROC('GL_EXT_transform_feedback', None, 'glEndTransformFeedbackEXT', ())
GL_PROC('GL_EXT_transform_feedback', None, 'glBindBufferRangeEXT', (GLenum, GLuint, GLuint, GLintptr, GLsizeiptr, ))
GL_PROC('GL_EXT_transform_feedback', None, 'glBindBufferOffsetEXT', (GLenum, GLuint, GLuint, GLintptr, ))
GL_PROC('GL_EXT_transform_feedback', None, 'glBindBufferBaseEXT', (GLenum, GLuint, GLuint, ))
GL_PROC('GL_EXT_transform_feedback', None, 'glTransformFeedbackVaryingsEXT', (GLuint, GLsizei, ctypes.POINTER(ctypes.POINTER(GLchar)), GLenum, ))
GL_PROC('GL_EXT_transform_feedback', None, 'glGetTransformFeedbackVaryingEXT', (GLuint, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLsizei), ctypes.POINTER(GLenum), ctypes.POINTER(GLchar), ))
GL_PROC('GL_EXT_vertex_array', None, 'glArrayElementEXT', (GLint, ))
GL_PROC('GL_EXT_vertex_array', None, 'glColorPointerEXT', (GLint, GLenum, GLsizei, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_vertex_array', None, 'glDrawArraysEXT', (GLenum, GLint, GLsizei, ))
GL_PROC('GL_EXT_vertex_array', None, 'glEdgeFlagPointerEXT', (GLsizei, GLsizei, ctypes.POINTER(GLboolean), ))
GL_PROC('GL_EXT_vertex_array', None, 'glGetPointervEXT', (GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_EXT_vertex_array', None, 'glIndexPointerEXT', (GLenum, GLsizei, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_vertex_array', None, 'glNormalPointerEXT', (GLenum, GLsizei, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_vertex_array', None, 'glTexCoordPointerEXT', (GLint, GLenum, GLsizei, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_vertex_array', None, 'glVertexPointerEXT', (GLint, GLenum, GLsizei, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_vertex_attrib_64bit', None, 'glVertexAttribL1dEXT', (GLuint, GLdouble, ))
GL_PROC('GL_EXT_vertex_attrib_64bit', None, 'glVertexAttribL2dEXT', (GLuint, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_vertex_attrib_64bit', None, 'glVertexAttribL3dEXT', (GLuint, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_vertex_attrib_64bit', None, 'glVertexAttribL4dEXT', (GLuint, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_EXT_vertex_attrib_64bit', None, 'glVertexAttribL1dvEXT', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_vertex_attrib_64bit', None, 'glVertexAttribL2dvEXT', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_vertex_attrib_64bit', None, 'glVertexAttribL3dvEXT', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_vertex_attrib_64bit', None, 'glVertexAttribL4dvEXT', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_vertex_attrib_64bit', None, 'glVertexAttribLPointerEXT', (GLuint, GLint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_vertex_attrib_64bit', None, 'glGetVertexAttribLdvEXT', (GLuint, GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_vertex_attrib_64bit', None, 'glVertexArrayVertexAttribLOffsetEXT', (GLuint, GLuint, GLuint, GLint, GLenum, GLsizei, GLintptr, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glBeginVertexShaderEXT', ())
GL_PROC('GL_EXT_vertex_shader', None, 'glEndVertexShaderEXT', ())
GL_PROC('GL_EXT_vertex_shader', None, 'glBindVertexShaderEXT', (GLuint, ))
GL_PROC('GL_EXT_vertex_shader', GLuint, 'glGenVertexShadersEXT', (GLuint, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glDeleteVertexShaderEXT', (GLuint, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glShaderOp1EXT', (GLenum, GLuint, GLuint, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glShaderOp2EXT', (GLenum, GLuint, GLuint, GLuint, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glShaderOp3EXT', (GLenum, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glSwizzleEXT', (GLuint, GLuint, GLenum, GLenum, GLenum, GLenum, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glWriteMaskEXT', (GLuint, GLuint, GLenum, GLenum, GLenum, GLenum, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glInsertComponentEXT', (GLuint, GLuint, GLuint, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glExtractComponentEXT', (GLuint, GLuint, GLuint, ))
GL_PROC('GL_EXT_vertex_shader', GLuint, 'glGenSymbolsEXT', (GLenum, GLenum, GLenum, GLuint, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glSetInvariantEXT', (GLuint, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glSetLocalConstantEXT', (GLuint, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glVariantbvEXT', (GLuint, ctypes.POINTER(GLbyte), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glVariantsvEXT', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glVariantivEXT', (GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glVariantfvEXT', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glVariantdvEXT', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glVariantubvEXT', (GLuint, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glVariantusvEXT', (GLuint, ctypes.POINTER(GLushort), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glVariantuivEXT', (GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glVariantPointerEXT', (GLuint, GLenum, GLuint, ctypes.c_void_p, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glEnableVariantClientStateEXT', (GLuint, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glDisableVariantClientStateEXT', (GLuint, ))
GL_PROC('GL_EXT_vertex_shader', GLuint, 'glBindLightParameterEXT', (GLenum, GLenum, ))
GL_PROC('GL_EXT_vertex_shader', GLuint, 'glBindMaterialParameterEXT', (GLenum, GLenum, ))
GL_PROC('GL_EXT_vertex_shader', GLuint, 'glBindTexGenParameterEXT', (GLenum, GLenum, GLenum, ))
GL_PROC('GL_EXT_vertex_shader', GLuint, 'glBindTextureUnitParameterEXT', (GLenum, GLenum, ))
GL_PROC('GL_EXT_vertex_shader', GLuint, 'glBindParameterEXT', (GLenum, ))
GL_PROC('GL_EXT_vertex_shader', GLboolean, 'glIsVariantEnabledEXT', (GLuint, GLenum, ))
GL_PROC('GL_EXT_vertex_shader', None, 'glGetVariantBooleanvEXT', (GLuint, GLenum, ctypes.POINTER(GLboolean), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glGetVariantIntegervEXT', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glGetVariantFloatvEXT', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glGetVariantPointervEXT', (GLuint, GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glGetInvariantBooleanvEXT', (GLuint, GLenum, ctypes.POINTER(GLboolean), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glGetInvariantIntegervEXT', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glGetInvariantFloatvEXT', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glGetLocalConstantBooleanvEXT', (GLuint, GLenum, ctypes.POINTER(GLboolean), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glGetLocalConstantIntegervEXT', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_EXT_vertex_shader', None, 'glGetLocalConstantFloatvEXT', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_vertex_weighting', None, 'glVertexWeightfEXT', (GLfloat, ))
GL_PROC('GL_EXT_vertex_weighting', None, 'glVertexWeightfvEXT', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_EXT_vertex_weighting', None, 'glVertexWeightPointerEXT', (GLint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_EXT_x11_sync_object', GLsync, 'glImportSyncEXT', (GLenum, GLintptr, GLbitfield, ))
GL_PROC('GL_GREMEDY_frame_terminator', None, 'glFrameTerminatorGREMEDY', ())
GL_PROC('GL_GREMEDY_string_marker', None, 'glStringMarkerGREMEDY', (GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_HP_image_transform', None, 'glImageTransformParameteriHP', (GLenum, GLenum, GLint, ))
GL_PROC('GL_HP_image_transform', None, 'glImageTransformParameterfHP', (GLenum, GLenum, GLfloat, ))
GL_PROC('GL_HP_image_transform', None, 'glImageTransformParameterivHP', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_HP_image_transform', None, 'glImageTransformParameterfvHP', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_HP_image_transform', None, 'glGetImageTransformParameterivHP', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_HP_image_transform', None, 'glGetImageTransformParameterfvHP', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_IBM_multimode_draw_arrays', None, 'glMultiModeDrawArraysIBM', (ctypes.POINTER(GLenum), ctypes.POINTER(GLint), ctypes.POINTER(GLsizei), GLsizei, GLint, ))
GL_PROC('GL_IBM_multimode_draw_arrays', None, 'glMultiModeDrawElementsIBM', (ctypes.POINTER(GLenum), ctypes.POINTER(GLsizei), GLenum, ctypes.POINTER(ctypes.c_void_p), GLsizei, GLint, ))
GL_PROC('GL_IBM_vertex_array_lists', None, 'glColorPointerListIBM', (GLint, GLenum, GLint, ctypes.POINTER(ctypes.c_void_p), GLint, ))
GL_PROC('GL_IBM_vertex_array_lists', None, 'glSecondaryColorPointerListIBM', (GLint, GLenum, GLint, ctypes.POINTER(ctypes.c_void_p), GLint, ))
GL_PROC('GL_IBM_vertex_array_lists', None, 'glEdgeFlagPointerListIBM', (GLint, ctypes.POINTER(ctypes.POINTER(GLboolean)), GLint, ))
GL_PROC('GL_IBM_vertex_array_lists', None, 'glFogCoordPointerListIBM', (GLenum, GLint, ctypes.POINTER(ctypes.c_void_p), GLint, ))
GL_PROC('GL_IBM_vertex_array_lists', None, 'glIndexPointerListIBM', (GLenum, GLint, ctypes.POINTER(ctypes.c_void_p), GLint, ))
GL_PROC('GL_IBM_vertex_array_lists', None, 'glNormalPointerListIBM', (GLenum, GLint, ctypes.POINTER(ctypes.c_void_p), GLint, ))
GL_PROC('GL_IBM_vertex_array_lists', None, 'glTexCoordPointerListIBM', (GLint, GLenum, GLint, ctypes.POINTER(ctypes.c_void_p), GLint, ))
GL_PROC('GL_IBM_vertex_array_lists', None, 'glVertexPointerListIBM', (GLint, GLenum, GLint, ctypes.POINTER(ctypes.c_void_p), GLint, ))
GL_PROC('GL_INTEL_parallel_arrays', None, 'glVertexPointervINTEL', (GLint, GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_INTEL_parallel_arrays', None, 'glNormalPointervINTEL', (GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_INTEL_parallel_arrays', None, 'glColorPointervINTEL', (GLint, GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_INTEL_parallel_arrays', None, 'glTexCoordPointervINTEL', (GLint, GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_KHR_debug', None, 'glDebugMessageControl', (GLenum, GLenum, GLenum, GLsizei, ctypes.POINTER(GLuint), GLboolean, ))
GL_PROC('GL_KHR_debug', None, 'glDebugMessageInsert', (GLenum, GLenum, GLuint, GLenum, GLsizei, ctypes.POINTER(GLchar), ))
GL_PROC('GL_KHR_debug', None, 'glDebugMessageCallback', (GLDEBUGPROC, ctypes.c_void_p, ))
GL_PROC('GL_KHR_debug', GLuint, 'glGetDebugMessageLog', (GLuint, GLsizei, ctypes.POINTER(GLenum), ctypes.POINTER(GLenum), ctypes.POINTER(GLuint), ctypes.POINTER(GLenum), ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_KHR_debug', None, 'glPushDebugGroup', (GLenum, GLuint, GLsizei, ctypes.POINTER(GLchar), ))
GL_PROC('GL_KHR_debug', None, 'glPopDebugGroup', ())
GL_PROC('GL_KHR_debug', None, 'glObjectLabel', (GLenum, GLuint, GLsizei, ctypes.POINTER(GLchar), ))
GL_PROC('GL_KHR_debug', None, 'glGetObjectLabel', (GLenum, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_KHR_debug', None, 'glObjectPtrLabel', (ctypes.c_void_p, GLsizei, ctypes.POINTER(GLchar), ))
GL_PROC('GL_KHR_debug', None, 'glGetObjectPtrLabel', (ctypes.c_void_p, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_MESA_resize_buffers', None, 'glResizeBuffersMESA', ())
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos2dMESA', (GLdouble, GLdouble, ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos2dvMESA', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos2fMESA', (GLfloat, GLfloat, ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos2fvMESA', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos2iMESA', (GLint, GLint, ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos2ivMESA', (ctypes.POINTER(GLint), ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos2sMESA', (GLshort, GLshort, ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos2svMESA', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos3dMESA', (GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos3dvMESA', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos3fMESA', (GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos3fvMESA', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos3iMESA', (GLint, GLint, GLint, ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos3ivMESA', (ctypes.POINTER(GLint), ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos3sMESA', (GLshort, GLshort, GLshort, ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos3svMESA', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos4dMESA', (GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos4dvMESA', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos4fMESA', (GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos4fvMESA', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos4iMESA', (GLint, GLint, GLint, GLint, ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos4ivMESA', (ctypes.POINTER(GLint), ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos4sMESA', (GLshort, GLshort, GLshort, GLshort, ))
GL_PROC('GL_MESA_window_pos', None, 'glWindowPos4svMESA', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_NV_bindless_texture', GLuint64, 'glGetTextureHandleNV', (GLuint, ))
GL_PROC('GL_NV_bindless_texture', GLuint64, 'glGetTextureSamplerHandleNV', (GLuint, GLuint, ))
GL_PROC('GL_NV_bindless_texture', None, 'glMakeTextureHandleResidentNV', (GLuint64, ))
GL_PROC('GL_NV_bindless_texture', None, 'glMakeTextureHandleNonResidentNV', (GLuint64, ))
GL_PROC('GL_NV_bindless_texture', GLuint64, 'glGetImageHandleNV', (GLuint, GLint, GLboolean, GLint, GLenum, ))
GL_PROC('GL_NV_bindless_texture', None, 'glMakeImageHandleResidentNV', (GLuint64, GLenum, ))
GL_PROC('GL_NV_bindless_texture', None, 'glMakeImageHandleNonResidentNV', (GLuint64, ))
GL_PROC('GL_NV_bindless_texture', None, 'glUniformHandleui64NV', (GLint, GLuint64, ))
GL_PROC('GL_NV_bindless_texture', None, 'glUniformHandleui64vNV', (GLint, GLsizei, ctypes.POINTER(GLuint64), ))
GL_PROC('GL_NV_bindless_texture', None, 'glProgramUniformHandleui64NV', (GLuint, GLint, GLuint64, ))
GL_PROC('GL_NV_bindless_texture', None, 'glProgramUniformHandleui64vNV', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint64), ))
GL_PROC('GL_NV_bindless_texture', GLboolean, 'glIsTextureHandleResidentNV', (GLuint64, ))
GL_PROC('GL_NV_conditional_render', None, 'glBeginConditionalRenderNV', (GLuint, GLenum, ))
GL_PROC('GL_NV_conditional_render', None, 'glEndConditionalRenderNV', ())
GL_PROC('GL_NV_copy_image', None, 'glCopyImageSubDataNV', (GLuint, GLenum, GLint, GLint, GLint, GLint, GLuint, GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, ))
GL_PROC('GL_NV_depth_buffer_float', None, 'glDepthRangedNV', (GLdouble, GLdouble, ))
GL_PROC('GL_NV_depth_buffer_float', None, 'glClearDepthdNV', (GLdouble, ))
GL_PROC('GL_NV_depth_buffer_float', None, 'glDepthBoundsdNV', (GLdouble, GLdouble, ))
GL_PROC('GL_NV_evaluators', None, 'glMapControlPointsNV', (GLenum, GLuint, GLenum, GLsizei, GLsizei, GLint, GLint, GLboolean, ctypes.c_void_p, ))
GL_PROC('GL_NV_evaluators', None, 'glMapParameterivNV', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_evaluators', None, 'glMapParameterfvNV', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_evaluators', None, 'glGetMapControlPointsNV', (GLenum, GLuint, GLenum, GLsizei, GLsizei, GLboolean, ctypes.c_void_p, ))
GL_PROC('GL_NV_evaluators', None, 'glGetMapParameterivNV', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_evaluators', None, 'glGetMapParameterfvNV', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_evaluators', None, 'glGetMapAttribParameterivNV', (GLenum, GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_evaluators', None, 'glGetMapAttribParameterfvNV', (GLenum, GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_evaluators', None, 'glEvalMapsNV', (GLenum, GLenum, ))
GL_PROC('GL_NV_explicit_multisample', None, 'glGetMultisamplefvNV', (GLenum, GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_explicit_multisample', None, 'glSampleMaskIndexedNV', (GLuint, GLbitfield, ))
GL_PROC('GL_NV_explicit_multisample', None, 'glTexRenderbufferNV', (GLenum, GLuint, ))
GL_PROC('GL_NV_fence', None, 'glDeleteFencesNV', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_fence', None, 'glGenFencesNV', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_fence', GLboolean, 'glIsFenceNV', (GLuint, ))
GL_PROC('GL_NV_fence', GLboolean, 'glTestFenceNV', (GLuint, ))
GL_PROC('GL_NV_fence', None, 'glGetFenceivNV', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_fence', None, 'glFinishFenceNV', (GLuint, ))
GL_PROC('GL_NV_fence', None, 'glSetFenceNV', (GLuint, GLenum, ))
GL_PROC('GL_NV_fragment_program', None, 'glProgramNamedParameter4fNV', (GLuint, GLsizei, ctypes.POINTER(GLubyte), GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_NV_fragment_program', None, 'glProgramNamedParameter4dNV', (GLuint, GLsizei, ctypes.POINTER(GLubyte), GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_NV_fragment_program', None, 'glProgramNamedParameter4fvNV', (GLuint, GLsizei, ctypes.POINTER(GLubyte), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_fragment_program', None, 'glProgramNamedParameter4dvNV', (GLuint, GLsizei, ctypes.POINTER(GLubyte), ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_fragment_program', None, 'glGetProgramNamedParameterfvNV', (GLuint, GLsizei, ctypes.POINTER(GLubyte), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_fragment_program', None, 'glGetProgramNamedParameterdvNV', (GLuint, GLsizei, ctypes.POINTER(GLubyte), ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_framebuffer_multisample_coverage', None, 'glRenderbufferStorageMultisampleCoverageNV', (GLenum, GLsizei, GLsizei, GLenum, GLsizei, GLsizei, ))
GL_PROC('GL_NV_geometry_program4', None, 'glProgramVertexLimitNV', (GLenum, GLint, ))
GL_PROC('GL_NV_geometry_program4', None, 'glFramebufferTextureEXT', (GLenum, GLenum, GLuint, GLint, ))
GL_PROC('GL_NV_geometry_program4', None, 'glFramebufferTextureLayerEXT', (GLenum, GLenum, GLuint, GLint, GLint, ))
GL_PROC('GL_NV_geometry_program4', None, 'glFramebufferTextureFaceEXT', (GLenum, GLenum, GLuint, GLint, GLenum, ))
GL_PROC('GL_NV_gpu_program4', None, 'glProgramLocalParameterI4iNV', (GLenum, GLuint, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_NV_gpu_program4', None, 'glProgramLocalParameterI4ivNV', (GLenum, GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_gpu_program4', None, 'glProgramLocalParametersI4ivNV', (GLenum, GLuint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_gpu_program4', None, 'glProgramLocalParameterI4uiNV', (GLenum, GLuint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_NV_gpu_program4', None, 'glProgramLocalParameterI4uivNV', (GLenum, GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_gpu_program4', None, 'glProgramLocalParametersI4uivNV', (GLenum, GLuint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_gpu_program4', None, 'glProgramEnvParameterI4iNV', (GLenum, GLuint, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_NV_gpu_program4', None, 'glProgramEnvParameterI4ivNV', (GLenum, GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_gpu_program4', None, 'glProgramEnvParametersI4ivNV', (GLenum, GLuint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_gpu_program4', None, 'glProgramEnvParameterI4uiNV', (GLenum, GLuint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_NV_gpu_program4', None, 'glProgramEnvParameterI4uivNV', (GLenum, GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_gpu_program4', None, 'glProgramEnvParametersI4uivNV', (GLenum, GLuint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_gpu_program4', None, 'glGetProgramLocalParameterIivNV', (GLenum, GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_gpu_program4', None, 'glGetProgramLocalParameterIuivNV', (GLenum, GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_gpu_program4', None, 'glGetProgramEnvParameterIivNV', (GLenum, GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_gpu_program4', None, 'glGetProgramEnvParameterIuivNV', (GLenum, GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_gpu_program5', None, 'glProgramSubroutineParametersuivNV', (GLenum, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_gpu_program5', None, 'glGetProgramSubroutineParameteruivNV', (GLenum, GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform1i64NV', (GLint, GLint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform2i64NV', (GLint, GLint64EXT, GLint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform3i64NV', (GLint, GLint64EXT, GLint64EXT, GLint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform4i64NV', (GLint, GLint64EXT, GLint64EXT, GLint64EXT, GLint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform1i64vNV', (GLint, GLsizei, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform2i64vNV', (GLint, GLsizei, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform3i64vNV', (GLint, GLsizei, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform4i64vNV', (GLint, GLsizei, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform1ui64NV', (GLint, GLuint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform2ui64NV', (GLint, GLuint64EXT, GLuint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform3ui64NV', (GLint, GLuint64EXT, GLuint64EXT, GLuint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform4ui64NV', (GLint, GLuint64EXT, GLuint64EXT, GLuint64EXT, GLuint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform1ui64vNV', (GLint, GLsizei, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform2ui64vNV', (GLint, GLsizei, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform3ui64vNV', (GLint, GLsizei, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glUniform4ui64vNV', (GLint, GLsizei, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glGetUniformi64vNV', (GLuint, GLint, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform1i64NV', (GLuint, GLint, GLint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform2i64NV', (GLuint, GLint, GLint64EXT, GLint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform3i64NV', (GLuint, GLint, GLint64EXT, GLint64EXT, GLint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform4i64NV', (GLuint, GLint, GLint64EXT, GLint64EXT, GLint64EXT, GLint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform1i64vNV', (GLuint, GLint, GLsizei, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform2i64vNV', (GLuint, GLint, GLsizei, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform3i64vNV', (GLuint, GLint, GLsizei, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform4i64vNV', (GLuint, GLint, GLsizei, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform1ui64NV', (GLuint, GLint, GLuint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform2ui64NV', (GLuint, GLint, GLuint64EXT, GLuint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform3ui64NV', (GLuint, GLint, GLuint64EXT, GLuint64EXT, GLuint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform4ui64NV', (GLuint, GLint, GLuint64EXT, GLuint64EXT, GLuint64EXT, GLuint64EXT, ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform1ui64vNV', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform2ui64vNV', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform3ui64vNV', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_gpu_shader5', None, 'glProgramUniform4ui64vNV', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_half_float', None, 'glVertex2hNV', (GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glVertex2hvNV', (ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glVertex3hNV', (GLhalfNV, GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glVertex3hvNV', (ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glVertex4hNV', (GLhalfNV, GLhalfNV, GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glVertex4hvNV', (ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glNormal3hNV', (GLhalfNV, GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glNormal3hvNV', (ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glColor3hNV', (GLhalfNV, GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glColor3hvNV', (ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glColor4hNV', (GLhalfNV, GLhalfNV, GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glColor4hvNV', (ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glTexCoord1hNV', (GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glTexCoord1hvNV', (ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glTexCoord2hNV', (GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glTexCoord2hvNV', (ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glTexCoord3hNV', (GLhalfNV, GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glTexCoord3hvNV', (ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glTexCoord4hNV', (GLhalfNV, GLhalfNV, GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glTexCoord4hvNV', (ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glMultiTexCoord1hNV', (GLenum, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glMultiTexCoord1hvNV', (GLenum, ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glMultiTexCoord2hNV', (GLenum, GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glMultiTexCoord2hvNV', (GLenum, ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glMultiTexCoord3hNV', (GLenum, GLhalfNV, GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glMultiTexCoord3hvNV', (GLenum, ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glMultiTexCoord4hNV', (GLenum, GLhalfNV, GLhalfNV, GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glMultiTexCoord4hvNV', (GLenum, ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glFogCoordhNV', (GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glFogCoordhvNV', (ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glSecondaryColor3hNV', (GLhalfNV, GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glSecondaryColor3hvNV', (ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glVertexWeighthNV', (GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glVertexWeighthvNV', (ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glVertexAttrib1hNV', (GLuint, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glVertexAttrib1hvNV', (GLuint, ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glVertexAttrib2hNV', (GLuint, GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glVertexAttrib2hvNV', (GLuint, ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glVertexAttrib3hNV', (GLuint, GLhalfNV, GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glVertexAttrib3hvNV', (GLuint, ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glVertexAttrib4hNV', (GLuint, GLhalfNV, GLhalfNV, GLhalfNV, GLhalfNV, ))
GL_PROC('GL_NV_half_float', None, 'glVertexAttrib4hvNV', (GLuint, ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glVertexAttribs1hvNV', (GLuint, GLsizei, ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glVertexAttribs2hvNV', (GLuint, GLsizei, ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glVertexAttribs3hvNV', (GLuint, GLsizei, ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_half_float', None, 'glVertexAttribs4hvNV', (GLuint, GLsizei, ctypes.POINTER(GLhalfNV), ))
GL_PROC('GL_NV_occlusion_query', None, 'glGenOcclusionQueriesNV', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_occlusion_query', None, 'glDeleteOcclusionQueriesNV', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_occlusion_query', GLboolean, 'glIsOcclusionQueryNV', (GLuint, ))
GL_PROC('GL_NV_occlusion_query', None, 'glBeginOcclusionQueryNV', (GLuint, ))
GL_PROC('GL_NV_occlusion_query', None, 'glEndOcclusionQueryNV', ())
GL_PROC('GL_NV_occlusion_query', None, 'glGetOcclusionQueryivNV', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_occlusion_query', None, 'glGetOcclusionQueryuivNV', (GLuint, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_parameter_buffer_object', None, 'glProgramBufferParametersfvNV', (GLenum, GLuint, GLuint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_parameter_buffer_object', None, 'glProgramBufferParametersIivNV', (GLenum, GLuint, GLuint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_parameter_buffer_object', None, 'glProgramBufferParametersIuivNV', (GLenum, GLuint, GLuint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_path_rendering', GLuint, 'glGenPathsNV', (GLsizei, ))
GL_PROC('GL_NV_path_rendering', None, 'glDeletePathsNV', (GLuint, GLsizei, ))
GL_PROC('GL_NV_path_rendering', GLboolean, 'glIsPathNV', (GLuint, ))
GL_PROC('GL_NV_path_rendering', None, 'glPathCommandsNV', (GLuint, GLsizei, ctypes.POINTER(GLubyte), GLsizei, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_NV_path_rendering', None, 'glPathCoordsNV', (GLuint, GLsizei, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_NV_path_rendering', None, 'glPathSubCommandsNV', (GLuint, GLsizei, GLsizei, GLsizei, ctypes.POINTER(GLubyte), GLsizei, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_NV_path_rendering', None, 'glPathSubCoordsNV', (GLuint, GLsizei, GLsizei, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_NV_path_rendering', None, 'glPathStringNV', (GLuint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_NV_path_rendering', None, 'glPathGlyphsNV', (GLuint, GLenum, ctypes.c_void_p, GLbitfield, GLsizei, GLenum, ctypes.c_void_p, GLenum, GLuint, GLfloat, ))
GL_PROC('GL_NV_path_rendering', None, 'glPathGlyphRangeNV', (GLuint, GLenum, ctypes.c_void_p, GLbitfield, GLuint, GLsizei, GLenum, GLuint, GLfloat, ))
GL_PROC('GL_NV_path_rendering', None, 'glWeightPathsNV', (GLuint, GLsizei, ctypes.POINTER(GLuint), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glCopyPathNV', (GLuint, GLuint, ))
GL_PROC('GL_NV_path_rendering', None, 'glInterpolatePathsNV', (GLuint, GLuint, GLuint, GLfloat, ))
GL_PROC('GL_NV_path_rendering', None, 'glTransformPathNV', (GLuint, GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glPathParameterivNV', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_path_rendering', None, 'glPathParameteriNV', (GLuint, GLenum, GLint, ))
GL_PROC('GL_NV_path_rendering', None, 'glPathParameterfvNV', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glPathParameterfNV', (GLuint, GLenum, GLfloat, ))
GL_PROC('GL_NV_path_rendering', None, 'glPathDashArrayNV', (GLuint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glPathStencilFuncNV', (GLenum, GLint, GLuint, ))
GL_PROC('GL_NV_path_rendering', None, 'glPathStencilDepthOffsetNV', (GLfloat, GLfloat, ))
GL_PROC('GL_NV_path_rendering', None, 'glStencilFillPathNV', (GLuint, GLenum, GLuint, ))
GL_PROC('GL_NV_path_rendering', None, 'glStencilStrokePathNV', (GLuint, GLint, GLuint, ))
GL_PROC('GL_NV_path_rendering', None, 'glStencilFillPathInstancedNV', (GLsizei, GLenum, ctypes.c_void_p, GLuint, GLenum, GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glStencilStrokePathInstancedNV', (GLsizei, GLenum, ctypes.c_void_p, GLuint, GLint, GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glPathCoverDepthFuncNV', (GLenum, ))
GL_PROC('GL_NV_path_rendering', None, 'glPathColorGenNV', (GLenum, GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glPathTexGenNV', (GLenum, GLenum, GLint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glPathFogGenNV', (GLenum, ))
GL_PROC('GL_NV_path_rendering', None, 'glCoverFillPathNV', (GLuint, GLenum, ))
GL_PROC('GL_NV_path_rendering', None, 'glCoverStrokePathNV', (GLuint, GLenum, ))
GL_PROC('GL_NV_path_rendering', None, 'glCoverFillPathInstancedNV', (GLsizei, GLenum, ctypes.c_void_p, GLuint, GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glCoverStrokePathInstancedNV', (GLsizei, GLenum, ctypes.c_void_p, GLuint, GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glGetPathParameterivNV', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_path_rendering', None, 'glGetPathParameterfvNV', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glGetPathCommandsNV', (GLuint, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_NV_path_rendering', None, 'glGetPathCoordsNV', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glGetPathDashArrayNV', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glGetPathMetricsNV', (GLbitfield, GLsizei, GLenum, ctypes.c_void_p, GLuint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glGetPathMetricRangeNV', (GLbitfield, GLuint, GLsizei, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glGetPathSpacingNV', (GLenum, GLsizei, GLenum, ctypes.c_void_p, GLuint, GLfloat, GLfloat, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glGetPathColorGenivNV', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_path_rendering', None, 'glGetPathColorGenfvNV', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', None, 'glGetPathTexGenivNV', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_path_rendering', None, 'glGetPathTexGenfvNV', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_path_rendering', GLboolean, 'glIsPointInFillPathNV', (GLuint, GLuint, GLfloat, GLfloat, ))
GL_PROC('GL_NV_path_rendering', GLboolean, 'glIsPointInStrokePathNV', (GLuint, GLfloat, GLfloat, ))
GL_PROC('GL_NV_path_rendering', GLfloat, 'glGetPathLengthNV', (GLuint, GLsizei, GLsizei, ))
GL_PROC('GL_NV_path_rendering', GLboolean, 'glPointAlongPathNV', (GLuint, GLsizei, GLsizei, GLfloat, ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_pixel_data_range', None, 'glPixelDataRangeNV', (GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_NV_pixel_data_range', None, 'glFlushPixelDataRangeNV', (GLenum, ))
GL_PROC('GL_NV_point_sprite', None, 'glPointParameteriNV', (GLenum, GLint, ))
GL_PROC('GL_NV_point_sprite', None, 'glPointParameterivNV', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_present_video', None, 'glPresentFrameKeyedNV', (GLuint, GLuint64EXT, GLuint, GLuint, GLenum, GLenum, GLuint, GLuint, GLenum, GLuint, GLuint, ))
GL_PROC('GL_NV_present_video', None, 'glPresentFrameDualFillNV', (GLuint, GLuint64EXT, GLuint, GLuint, GLenum, GLenum, GLuint, GLenum, GLuint, GLenum, GLuint, GLenum, GLuint, ))
GL_PROC('GL_NV_present_video', None, 'glGetVideoivNV', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_present_video', None, 'glGetVideouivNV', (GLuint, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_present_video', None, 'glGetVideoi64vNV', (GLuint, GLenum, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_present_video', None, 'glGetVideoui64vNV', (GLuint, GLenum, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_primitive_restart', None, 'glPrimitiveRestartNV', ())
GL_PROC('GL_NV_primitive_restart', None, 'glPrimitiveRestartIndexNV', (GLuint, ))
GL_PROC('GL_NV_register_combiners', None, 'glCombinerParameterfvNV', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_register_combiners', None, 'glCombinerParameterfNV', (GLenum, GLfloat, ))
GL_PROC('GL_NV_register_combiners', None, 'glCombinerParameterivNV', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_register_combiners', None, 'glCombinerParameteriNV', (GLenum, GLint, ))
GL_PROC('GL_NV_register_combiners', None, 'glCombinerInputNV', (GLenum, GLenum, GLenum, GLenum, GLenum, GLenum, ))
GL_PROC('GL_NV_register_combiners', None, 'glCombinerOutputNV', (GLenum, GLenum, GLenum, GLenum, GLenum, GLenum, GLenum, GLboolean, GLboolean, GLboolean, ))
GL_PROC('GL_NV_register_combiners', None, 'glFinalCombinerInputNV', (GLenum, GLenum, GLenum, GLenum, ))
GL_PROC('GL_NV_register_combiners', None, 'glGetCombinerInputParameterfvNV', (GLenum, GLenum, GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_register_combiners', None, 'glGetCombinerInputParameterivNV', (GLenum, GLenum, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_register_combiners', None, 'glGetCombinerOutputParameterfvNV', (GLenum, GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_register_combiners', None, 'glGetCombinerOutputParameterivNV', (GLenum, GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_register_combiners', None, 'glGetFinalCombinerInputParameterfvNV', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_register_combiners', None, 'glGetFinalCombinerInputParameterivNV', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_register_combiners2', None, 'glCombinerStageParameterfvNV', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_register_combiners2', None, 'glGetCombinerStageParameterfvNV', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_shader_buffer_load', None, 'glMakeBufferResidentNV', (GLenum, GLenum, ))
GL_PROC('GL_NV_shader_buffer_load', None, 'glMakeBufferNonResidentNV', (GLenum, ))
GL_PROC('GL_NV_shader_buffer_load', GLboolean, 'glIsBufferResidentNV', (GLenum, ))
GL_PROC('GL_NV_shader_buffer_load', None, 'glMakeNamedBufferResidentNV', (GLuint, GLenum, ))
GL_PROC('GL_NV_shader_buffer_load', None, 'glMakeNamedBufferNonResidentNV', (GLuint, ))
GL_PROC('GL_NV_shader_buffer_load', GLboolean, 'glIsNamedBufferResidentNV', (GLuint, ))
GL_PROC('GL_NV_shader_buffer_load', None, 'glGetBufferParameterui64vNV', (GLenum, GLenum, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_shader_buffer_load', None, 'glGetNamedBufferParameterui64vNV', (GLuint, GLenum, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_shader_buffer_load', None, 'glGetIntegerui64vNV', (GLenum, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_shader_buffer_load', None, 'glUniformui64NV', (GLint, GLuint64EXT, ))
GL_PROC('GL_NV_shader_buffer_load', None, 'glUniformui64vNV', (GLint, GLsizei, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_shader_buffer_load', None, 'glGetUniformui64vNV', (GLuint, GLint, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_shader_buffer_load', None, 'glProgramUniformui64NV', (GLuint, GLint, GLuint64EXT, ))
GL_PROC('GL_NV_shader_buffer_load', None, 'glProgramUniformui64vNV', (GLuint, GLint, GLsizei, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_texture_barrier', None, 'glTextureBarrierNV', ())
GL_PROC('GL_NV_texture_multisample', None, 'glTexImage2DMultisampleCoverageNV', (GLenum, GLsizei, GLsizei, GLint, GLsizei, GLsizei, GLboolean, ))
GL_PROC('GL_NV_texture_multisample', None, 'glTexImage3DMultisampleCoverageNV', (GLenum, GLsizei, GLsizei, GLint, GLsizei, GLsizei, GLsizei, GLboolean, ))
GL_PROC('GL_NV_texture_multisample', None, 'glTextureImage2DMultisampleNV', (GLuint, GLenum, GLsizei, GLint, GLsizei, GLsizei, GLboolean, ))
GL_PROC('GL_NV_texture_multisample', None, 'glTextureImage3DMultisampleNV', (GLuint, GLenum, GLsizei, GLint, GLsizei, GLsizei, GLsizei, GLboolean, ))
GL_PROC('GL_NV_texture_multisample', None, 'glTextureImage2DMultisampleCoverageNV', (GLuint, GLenum, GLsizei, GLsizei, GLint, GLsizei, GLsizei, GLboolean, ))
GL_PROC('GL_NV_texture_multisample', None, 'glTextureImage3DMultisampleCoverageNV', (GLuint, GLenum, GLsizei, GLsizei, GLint, GLsizei, GLsizei, GLsizei, GLboolean, ))
GL_PROC('GL_NV_transform_feedback', None, 'glBeginTransformFeedbackNV', (GLenum, ))
GL_PROC('GL_NV_transform_feedback', None, 'glEndTransformFeedbackNV', ())
GL_PROC('GL_NV_transform_feedback', None, 'glTransformFeedbackAttribsNV', (GLsizei, ctypes.POINTER(GLint), GLenum, ))
GL_PROC('GL_NV_transform_feedback', None, 'glBindBufferRangeNV', (GLenum, GLuint, GLuint, GLintptr, GLsizeiptr, ))
GL_PROC('GL_NV_transform_feedback', None, 'glBindBufferOffsetNV', (GLenum, GLuint, GLuint, GLintptr, ))
GL_PROC('GL_NV_transform_feedback', None, 'glBindBufferBaseNV', (GLenum, GLuint, GLuint, ))
GL_PROC('GL_NV_transform_feedback', None, 'glTransformFeedbackVaryingsNV', (GLuint, GLsizei, ctypes.POINTER(GLint), GLenum, ))
GL_PROC('GL_NV_transform_feedback', None, 'glActiveVaryingNV', (GLuint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_NV_transform_feedback', GLint, 'glGetVaryingLocationNV', (GLuint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_NV_transform_feedback', None, 'glGetActiveVaryingNV', (GLuint, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLsizei), ctypes.POINTER(GLenum), ctypes.POINTER(GLchar), ))
GL_PROC('GL_NV_transform_feedback', None, 'glGetTransformFeedbackVaryingNV', (GLuint, GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_transform_feedback', None, 'glTransformFeedbackStreamAttribsNV', (GLsizei, ctypes.POINTER(GLint), GLsizei, ctypes.POINTER(GLint), GLenum, ))
GL_PROC('GL_NV_transform_feedback2', None, 'glBindTransformFeedbackNV', (GLenum, GLuint, ))
GL_PROC('GL_NV_transform_feedback2', None, 'glDeleteTransformFeedbacksNV', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_transform_feedback2', None, 'glGenTransformFeedbacksNV', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_transform_feedback2', GLboolean, 'glIsTransformFeedbackNV', (GLuint, ))
GL_PROC('GL_NV_transform_feedback2', None, 'glPauseTransformFeedbackNV', ())
GL_PROC('GL_NV_transform_feedback2', None, 'glResumeTransformFeedbackNV', ())
GL_PROC('GL_NV_transform_feedback2', None, 'glDrawTransformFeedbackNV', (GLenum, GLuint, ))
GL_PROC('GL_NV_vdpau_interop', None, 'glVDPAUInitNV', (ctypes.c_void_p, ctypes.c_void_p, ))
GL_PROC('GL_NV_vdpau_interop', None, 'glVDPAUFiniNV', ())
GL_PROC('GL_NV_vdpau_interop', GLvdpauSurfaceNV, 'glVDPAURegisterVideoSurfaceNV', (ctypes.c_void_p, GLenum, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_vdpau_interop', GLvdpauSurfaceNV, 'glVDPAURegisterOutputSurfaceNV', (ctypes.c_void_p, GLenum, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_vdpau_interop', None, 'glVDPAUIsSurfaceNV', (GLvdpauSurfaceNV, ))
GL_PROC('GL_NV_vdpau_interop', None, 'glVDPAUUnregisterSurfaceNV', (GLvdpauSurfaceNV, ))
GL_PROC('GL_NV_vdpau_interop', None, 'glVDPAUGetSurfaceivNV', (GLvdpauSurfaceNV, GLenum, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_vdpau_interop', None, 'glVDPAUSurfaceAccessNV', (GLvdpauSurfaceNV, GLenum, ))
GL_PROC('GL_NV_vdpau_interop', None, 'glVDPAUMapSurfacesNV', (GLsizei, ctypes.POINTER(GLvdpauSurfaceNV), ))
GL_PROC('GL_NV_vdpau_interop', None, 'glVDPAUUnmapSurfacesNV', (GLsizei, ctypes.POINTER(GLvdpauSurfaceNV), ))
GL_PROC('GL_NV_vertex_array_range', None, 'glFlushVertexArrayRangeNV', ())
GL_PROC('GL_NV_vertex_array_range', None, 'glVertexArrayRangeNV', (GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL1i64NV', (GLuint, GLint64EXT, ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL2i64NV', (GLuint, GLint64EXT, GLint64EXT, ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL3i64NV', (GLuint, GLint64EXT, GLint64EXT, GLint64EXT, ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL4i64NV', (GLuint, GLint64EXT, GLint64EXT, GLint64EXT, GLint64EXT, ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL1i64vNV', (GLuint, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL2i64vNV', (GLuint, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL3i64vNV', (GLuint, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL4i64vNV', (GLuint, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL1ui64NV', (GLuint, GLuint64EXT, ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL2ui64NV', (GLuint, GLuint64EXT, GLuint64EXT, ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL3ui64NV', (GLuint, GLuint64EXT, GLuint64EXT, GLuint64EXT, ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL4ui64NV', (GLuint, GLuint64EXT, GLuint64EXT, GLuint64EXT, GLuint64EXT, ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL1ui64vNV', (GLuint, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL2ui64vNV', (GLuint, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL3ui64vNV', (GLuint, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribL4ui64vNV', (GLuint, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glGetVertexAttribLi64vNV', (GLuint, GLenum, ctypes.POINTER(GLint64EXT), ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glGetVertexAttribLui64vNV', (GLuint, GLenum, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_vertex_attrib_integer_64bit', None, 'glVertexAttribLFormatNV', (GLuint, GLint, GLenum, GLsizei, ))
GL_PROC('GL_NV_vertex_buffer_unified_memory', None, 'glBufferAddressRangeNV', (GLenum, GLuint, GLuint64EXT, GLsizeiptr, ))
GL_PROC('GL_NV_vertex_buffer_unified_memory', None, 'glVertexFormatNV', (GLint, GLenum, GLsizei, ))
GL_PROC('GL_NV_vertex_buffer_unified_memory', None, 'glNormalFormatNV', (GLenum, GLsizei, ))
GL_PROC('GL_NV_vertex_buffer_unified_memory', None, 'glColorFormatNV', (GLint, GLenum, GLsizei, ))
GL_PROC('GL_NV_vertex_buffer_unified_memory', None, 'glIndexFormatNV', (GLenum, GLsizei, ))
GL_PROC('GL_NV_vertex_buffer_unified_memory', None, 'glTexCoordFormatNV', (GLint, GLenum, GLsizei, ))
GL_PROC('GL_NV_vertex_buffer_unified_memory', None, 'glEdgeFlagFormatNV', (GLsizei, ))
GL_PROC('GL_NV_vertex_buffer_unified_memory', None, 'glSecondaryColorFormatNV', (GLint, GLenum, GLsizei, ))
GL_PROC('GL_NV_vertex_buffer_unified_memory', None, 'glFogCoordFormatNV', (GLenum, GLsizei, ))
GL_PROC('GL_NV_vertex_buffer_unified_memory', None, 'glVertexAttribFormatNV', (GLuint, GLint, GLenum, GLboolean, GLsizei, ))
GL_PROC('GL_NV_vertex_buffer_unified_memory', None, 'glVertexAttribIFormatNV', (GLuint, GLint, GLenum, GLsizei, ))
GL_PROC('GL_NV_vertex_buffer_unified_memory', None, 'glGetIntegerui64i_vNV', (GLenum, GLuint, ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_vertex_program', GLboolean, 'glAreProgramsResidentNV', (GLsizei, ctypes.POINTER(GLuint), ctypes.POINTER(GLboolean), ))
GL_PROC('GL_NV_vertex_program', None, 'glBindProgramNV', (GLenum, GLuint, ))
GL_PROC('GL_NV_vertex_program', None, 'glDeleteProgramsNV', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_vertex_program', None, 'glExecuteProgramNV', (GLenum, GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_vertex_program', None, 'glGenProgramsNV', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_vertex_program', None, 'glGetProgramParameterdvNV', (GLenum, GLuint, GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_vertex_program', None, 'glGetProgramParameterfvNV', (GLenum, GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_vertex_program', None, 'glGetProgramivNV', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_vertex_program', None, 'glGetProgramStringNV', (GLuint, GLenum, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_NV_vertex_program', None, 'glGetTrackMatrixivNV', (GLenum, GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_vertex_program', None, 'glGetVertexAttribdvNV', (GLuint, GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_vertex_program', None, 'glGetVertexAttribfvNV', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_vertex_program', None, 'glGetVertexAttribivNV', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_vertex_program', None, 'glGetVertexAttribPointervNV', (GLuint, GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_NV_vertex_program', GLboolean, 'glIsProgramNV', (GLuint, ))
GL_PROC('GL_NV_vertex_program', None, 'glLoadProgramNV', (GLenum, GLuint, GLsizei, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_NV_vertex_program', None, 'glProgramParameter4dNV', (GLenum, GLuint, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_NV_vertex_program', None, 'glProgramParameter4dvNV', (GLenum, GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_vertex_program', None, 'glProgramParameter4fNV', (GLenum, GLuint, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_NV_vertex_program', None, 'glProgramParameter4fvNV', (GLenum, GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_vertex_program', None, 'glProgramParameters4dvNV', (GLenum, GLuint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_vertex_program', None, 'glProgramParameters4fvNV', (GLenum, GLuint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_vertex_program', None, 'glRequestResidentProgramsNV', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_vertex_program', None, 'glTrackMatrixNV', (GLenum, GLuint, GLenum, GLenum, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttribPointerNV', (GLuint, GLint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib1dNV', (GLuint, GLdouble, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib1dvNV', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib1fNV', (GLuint, GLfloat, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib1fvNV', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib1sNV', (GLuint, GLshort, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib1svNV', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib2dNV', (GLuint, GLdouble, GLdouble, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib2dvNV', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib2fNV', (GLuint, GLfloat, GLfloat, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib2fvNV', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib2sNV', (GLuint, GLshort, GLshort, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib2svNV', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib3dNV', (GLuint, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib3dvNV', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib3fNV', (GLuint, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib3fvNV', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib3sNV', (GLuint, GLshort, GLshort, GLshort, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib3svNV', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib4dNV', (GLuint, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib4dvNV', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib4fNV', (GLuint, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib4fvNV', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib4sNV', (GLuint, GLshort, GLshort, GLshort, GLshort, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib4svNV', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib4ubNV', (GLuint, GLubyte, GLubyte, GLubyte, GLubyte, ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttrib4ubvNV', (GLuint, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttribs1dvNV', (GLuint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttribs1fvNV', (GLuint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttribs1svNV', (GLuint, GLsizei, ctypes.POINTER(GLshort), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttribs2dvNV', (GLuint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttribs2fvNV', (GLuint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttribs2svNV', (GLuint, GLsizei, ctypes.POINTER(GLshort), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttribs3dvNV', (GLuint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttribs3fvNV', (GLuint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttribs3svNV', (GLuint, GLsizei, ctypes.POINTER(GLshort), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttribs4dvNV', (GLuint, GLsizei, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttribs4fvNV', (GLuint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttribs4svNV', (GLuint, GLsizei, ctypes.POINTER(GLshort), ))
GL_PROC('GL_NV_vertex_program', None, 'glVertexAttribs4ubvNV', (GLuint, GLsizei, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI1iEXT', (GLuint, GLint, ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI2iEXT', (GLuint, GLint, GLint, ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI3iEXT', (GLuint, GLint, GLint, GLint, ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI4iEXT', (GLuint, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI1uiEXT', (GLuint, GLuint, ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI2uiEXT', (GLuint, GLuint, GLuint, ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI3uiEXT', (GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI4uiEXT', (GLuint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI1ivEXT', (GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI2ivEXT', (GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI3ivEXT', (GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI4ivEXT', (GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI1uivEXT', (GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI2uivEXT', (GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI3uivEXT', (GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI4uivEXT', (GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI4bvEXT', (GLuint, ctypes.POINTER(GLbyte), ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI4svEXT', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI4ubvEXT', (GLuint, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribI4usvEXT', (GLuint, ctypes.POINTER(GLushort), ))
GL_PROC('GL_NV_vertex_program4', None, 'glVertexAttribIPointerEXT', (GLuint, GLint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_NV_vertex_program4', None, 'glGetVertexAttribIivEXT', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_vertex_program4', None, 'glGetVertexAttribIuivEXT', (GLuint, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_NV_video_capture', None, 'glBeginVideoCaptureNV', (GLuint, ))
GL_PROC('GL_NV_video_capture', None, 'glBindVideoCaptureStreamBufferNV', (GLuint, GLuint, GLenum, GLintptrARB, ))
GL_PROC('GL_NV_video_capture', None, 'glBindVideoCaptureStreamTextureNV', (GLuint, GLuint, GLenum, GLenum, GLuint, ))
GL_PROC('GL_NV_video_capture', None, 'glEndVideoCaptureNV', (GLuint, ))
GL_PROC('GL_NV_video_capture', None, 'glGetVideoCaptureivNV', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_video_capture', None, 'glGetVideoCaptureStreamivNV', (GLuint, GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_video_capture', None, 'glGetVideoCaptureStreamfvNV', (GLuint, GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_video_capture', None, 'glGetVideoCaptureStreamdvNV', (GLuint, GLuint, GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_NV_video_capture', GLenum, 'glVideoCaptureNV', (GLuint, ctypes.POINTER(GLuint), ctypes.POINTER(GLuint64EXT), ))
GL_PROC('GL_NV_video_capture', None, 'glVideoCaptureStreamParameterivNV', (GLuint, GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_NV_video_capture', None, 'glVideoCaptureStreamParameterfvNV', (GLuint, GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_NV_video_capture', None, 'glVideoCaptureStreamParameterdvNV', (GLuint, GLuint, GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_PGI_misc_hints', None, 'glHintPGI', (GLenum, GLint, ))
GL_PROC('GL_SGIS_detail_texture', None, 'glDetailTexFuncSGIS', (GLenum, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIS_detail_texture', None, 'glGetDetailTexFuncSGIS', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIS_fog_function', None, 'glFogFuncSGIS', (GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIS_fog_function', None, 'glGetFogFuncSGIS', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIS_multisample', None, 'glSampleMaskSGIS', (GLclampf, GLboolean, ))
GL_PROC('GL_SGIS_multisample', None, 'glSamplePatternSGIS', (GLenum, ))
GL_PROC('GL_SGIS_pixel_texture', None, 'glPixelTexGenParameteriSGIS', (GLenum, GLint, ))
GL_PROC('GL_SGIS_pixel_texture', None, 'glPixelTexGenParameterivSGIS', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_SGIS_pixel_texture', None, 'glPixelTexGenParameterfSGIS', (GLenum, GLfloat, ))
GL_PROC('GL_SGIS_pixel_texture', None, 'glPixelTexGenParameterfvSGIS', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIS_pixel_texture', None, 'glGetPixelTexGenParameterivSGIS', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_SGIS_pixel_texture', None, 'glGetPixelTexGenParameterfvSGIS', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIS_point_parameters', None, 'glPointParameterfSGIS', (GLenum, GLfloat, ))
GL_PROC('GL_SGIS_point_parameters', None, 'glPointParameterfvSGIS', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIS_sharpen_texture', None, 'glSharpenTexFuncSGIS', (GLenum, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIS_sharpen_texture', None, 'glGetSharpenTexFuncSGIS', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIS_texture4D', None, 'glTexImage4DSGIS', (GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_SGIS_texture4D', None, 'glTexSubImage4DSGIS', (GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_SGIS_texture_color_mask', None, 'glTextureColorMaskSGIS', (GLboolean, GLboolean, GLboolean, GLboolean, ))
GL_PROC('GL_SGIS_texture_filter4', None, 'glGetTexFilterFuncSGIS', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIS_texture_filter4', None, 'glTexFilterFuncSGIS', (GLenum, GLenum, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIX_async', None, 'glAsyncMarkerSGIX', (GLuint, ))
GL_PROC('GL_SGIX_async', GLint, 'glFinishAsyncSGIX', (ctypes.POINTER(GLuint), ))
GL_PROC('GL_SGIX_async', GLint, 'glPollAsyncSGIX', (ctypes.POINTER(GLuint), ))
GL_PROC('GL_SGIX_async', GLuint, 'glGenAsyncMarkersSGIX', (GLsizei, ))
GL_PROC('GL_SGIX_async', None, 'glDeleteAsyncMarkersSGIX', (GLuint, GLsizei, ))
GL_PROC('GL_SGIX_async', GLboolean, 'glIsAsyncMarkerSGIX', (GLuint, ))
GL_PROC('GL_SGIX_flush_raster', None, 'glFlushRasterSGIX', ())
GL_PROC('GL_SGIX_fragment_lighting', None, 'glFragmentColorMaterialSGIX', (GLenum, GLenum, ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glFragmentLightfSGIX', (GLenum, GLenum, GLfloat, ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glFragmentLightfvSGIX', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glFragmentLightiSGIX', (GLenum, GLenum, GLint, ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glFragmentLightivSGIX', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glFragmentLightModelfSGIX', (GLenum, GLfloat, ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glFragmentLightModelfvSGIX', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glFragmentLightModeliSGIX', (GLenum, GLint, ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glFragmentLightModelivSGIX', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glFragmentMaterialfSGIX', (GLenum, GLenum, GLfloat, ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glFragmentMaterialfvSGIX', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glFragmentMaterialiSGIX', (GLenum, GLenum, GLint, ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glFragmentMaterialivSGIX', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glGetFragmentLightfvSGIX', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glGetFragmentLightivSGIX', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glGetFragmentMaterialfvSGIX', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glGetFragmentMaterialivSGIX', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_SGIX_fragment_lighting', None, 'glLightEnviSGIX', (GLenum, GLint, ))
GL_PROC('GL_SGIX_framezoom', None, 'glFrameZoomSGIX', (GLint, ))
GL_PROC('GL_SGIX_instruments', GLint, 'glGetInstrumentsSGIX', ())
GL_PROC('GL_SGIX_instruments', None, 'glInstrumentsBufferSGIX', (GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_SGIX_instruments', GLint, 'glPollInstrumentsSGIX', (ctypes.POINTER(GLint), ))
GL_PROC('GL_SGIX_instruments', None, 'glReadInstrumentsSGIX', (GLint, ))
GL_PROC('GL_SGIX_instruments', None, 'glStartInstrumentsSGIX', ())
GL_PROC('GL_SGIX_instruments', None, 'glStopInstrumentsSGIX', (GLint, ))
GL_PROC('GL_SGIX_list_priority', None, 'glGetListParameterfvSGIX', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIX_list_priority', None, 'glGetListParameterivSGIX', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_SGIX_list_priority', None, 'glListParameterfSGIX', (GLuint, GLenum, GLfloat, ))
GL_PROC('GL_SGIX_list_priority', None, 'glListParameterfvSGIX', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIX_list_priority', None, 'glListParameteriSGIX', (GLuint, GLenum, GLint, ))
GL_PROC('GL_SGIX_list_priority', None, 'glListParameterivSGIX', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_SGIX_pixel_texture', None, 'glPixelTexGenSGIX', (GLenum, ))
GL_PROC('GL_SGIX_polynomial_ffd', None, 'glDeformationMap3dSGIX', (GLenum, GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble, GLint, GLint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_SGIX_polynomial_ffd', None, 'glDeformationMap3fSGIX', (GLenum, GLfloat, GLfloat, GLint, GLint, GLfloat, GLfloat, GLint, GLint, GLfloat, GLfloat, GLint, GLint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIX_polynomial_ffd', None, 'glDeformSGIX', (GLbitfield, ))
GL_PROC('GL_SGIX_polynomial_ffd', None, 'glLoadIdentityDeformationMapSGIX', (GLbitfield, ))
GL_PROC('GL_SGIX_reference_plane', None, 'glReferencePlaneSGIX', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_SGIX_sprite', None, 'glSpriteParameterfSGIX', (GLenum, GLfloat, ))
GL_PROC('GL_SGIX_sprite', None, 'glSpriteParameterfvSGIX', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGIX_sprite', None, 'glSpriteParameteriSGIX', (GLenum, GLint, ))
GL_PROC('GL_SGIX_sprite', None, 'glSpriteParameterivSGIX', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_SGIX_tag_sample_buffer', None, 'glTagSampleBufferSGIX', ())
GL_PROC('GL_SGI_color_table', None, 'glColorTableSGI', (GLenum, GLenum, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_SGI_color_table', None, 'glColorTableParameterfvSGI', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGI_color_table', None, 'glColorTableParameterivSGI', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_SGI_color_table', None, 'glCopyColorTableSGI', (GLenum, GLenum, GLint, GLint, GLsizei, ))
GL_PROC('GL_SGI_color_table', None, 'glGetColorTableSGI', (GLenum, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_SGI_color_table', None, 'glGetColorTableParameterfvSGI', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SGI_color_table', None, 'glGetColorTableParameterivSGI', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_SUNX_constant_data', None, 'glFinishTextureSUNX', ())
GL_PROC('GL_SUN_global_alpha', None, 'glGlobalAlphaFactorbSUN', (GLbyte, ))
GL_PROC('GL_SUN_global_alpha', None, 'glGlobalAlphaFactorsSUN', (GLshort, ))
GL_PROC('GL_SUN_global_alpha', None, 'glGlobalAlphaFactoriSUN', (GLint, ))
GL_PROC('GL_SUN_global_alpha', None, 'glGlobalAlphaFactorfSUN', (GLfloat, ))
GL_PROC('GL_SUN_global_alpha', None, 'glGlobalAlphaFactordSUN', (GLdouble, ))
GL_PROC('GL_SUN_global_alpha', None, 'glGlobalAlphaFactorubSUN', (GLubyte, ))
GL_PROC('GL_SUN_global_alpha', None, 'glGlobalAlphaFactorusSUN', (GLushort, ))
GL_PROC('GL_SUN_global_alpha', None, 'glGlobalAlphaFactoruiSUN', (GLuint, ))
GL_PROC('GL_SUN_mesh_array', None, 'glDrawMeshArraysSUN', (GLenum, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_SUN_triangle_list', None, 'glReplacementCodeuiSUN', (GLuint, ))
GL_PROC('GL_SUN_triangle_list', None, 'glReplacementCodeusSUN', (GLushort, ))
GL_PROC('GL_SUN_triangle_list', None, 'glReplacementCodeubSUN', (GLubyte, ))
GL_PROC('GL_SUN_triangle_list', None, 'glReplacementCodeuivSUN', (ctypes.POINTER(GLuint), ))
GL_PROC('GL_SUN_triangle_list', None, 'glReplacementCodeusvSUN', (ctypes.POINTER(GLushort), ))
GL_PROC('GL_SUN_triangle_list', None, 'glReplacementCodeubvSUN', (ctypes.POINTER(GLubyte), ))
GL_PROC('GL_SUN_triangle_list', None, 'glReplacementCodePointerSUN', (GLenum, GLsizei, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_SUN_vertex', None, 'glColor4ubVertex2fSUN', (GLubyte, GLubyte, GLubyte, GLubyte, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glColor4ubVertex2fvSUN', (ctypes.POINTER(GLubyte), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glColor4ubVertex3fSUN', (GLubyte, GLubyte, GLubyte, GLubyte, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glColor4ubVertex3fvSUN', (ctypes.POINTER(GLubyte), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glColor3fVertex3fSUN', (GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glColor3fVertex3fvSUN', (ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glNormal3fVertex3fSUN', (GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glNormal3fVertex3fvSUN', (ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glColor4fNormal3fVertex3fSUN', (GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glColor4fNormal3fVertex3fvSUN', (ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glTexCoord2fVertex3fSUN', (GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glTexCoord2fVertex3fvSUN', (ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glTexCoord4fVertex4fSUN', (GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glTexCoord4fVertex4fvSUN', (ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glTexCoord2fColor4ubVertex3fSUN', (GLfloat, GLfloat, GLubyte, GLubyte, GLubyte, GLubyte, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glTexCoord2fColor4ubVertex3fvSUN', (ctypes.POINTER(GLfloat), ctypes.POINTER(GLubyte), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glTexCoord2fColor3fVertex3fSUN', (GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glTexCoord2fColor3fVertex3fvSUN', (ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glTexCoord2fNormal3fVertex3fSUN', (GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glTexCoord2fNormal3fVertex3fvSUN', (ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glTexCoord2fColor4fNormal3fVertex3fSUN', (GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glTexCoord2fColor4fNormal3fVertex3fvSUN', (ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glTexCoord4fColor4fNormal3fVertex4fSUN', (GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glTexCoord4fColor4fNormal3fVertex4fvSUN', (ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiVertex3fSUN', (GLuint, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiVertex3fvSUN', (ctypes.POINTER(GLuint), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiColor4ubVertex3fSUN', (GLuint, GLubyte, GLubyte, GLubyte, GLubyte, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiColor4ubVertex3fvSUN', (ctypes.POINTER(GLuint), ctypes.POINTER(GLubyte), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiColor3fVertex3fSUN', (GLuint, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiColor3fVertex3fvSUN', (ctypes.POINTER(GLuint), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiNormal3fVertex3fSUN', (GLuint, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiNormal3fVertex3fvSUN', (ctypes.POINTER(GLuint), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiColor4fNormal3fVertex3fSUN', (GLuint, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiColor4fNormal3fVertex3fvSUN', (ctypes.POINTER(GLuint), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiTexCoord2fVertex3fSUN', (GLuint, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiTexCoord2fVertex3fvSUN', (ctypes.POINTER(GLuint), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiTexCoord2fNormal3fVertex3fSUN', (GLuint, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiTexCoord2fNormal3fVertex3fvSUN', (ctypes.POINTER(GLuint), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiTexCoord2fColor4fNormal3fVertex3fSUN', (GLuint, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_SUN_vertex', None, 'glReplacementCodeuiTexCoord2fColor4fNormal3fVertex3fvSUN', (ctypes.POINTER(GLuint), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1', None, 'glCullFace', (GLenum, ))
GL_PROC('GL_VERSION_1_1', None, 'glFrontFace', (GLenum, ))
GL_PROC('GL_VERSION_1_1', None, 'glHint', (GLenum, GLenum, ))
GL_PROC('GL_VERSION_1_1', None, 'glLineWidth', (GLfloat, ))
GL_PROC('GL_VERSION_1_1', None, 'glPointSize', (GLfloat, ))
GL_PROC('GL_VERSION_1_1', None, 'glPolygonMode', (GLenum, GLenum, ))
GL_PROC('GL_VERSION_1_1', None, 'glScissor', (GLint, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_VERSION_1_1', None, 'glTexParameterf', (GLenum, GLenum, GLfloat, ))
GL_PROC('GL_VERSION_1_1', None, 'glTexParameterfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1', None, 'glTexParameteri', (GLenum, GLenum, GLint, ))
GL_PROC('GL_VERSION_1_1', None, 'glTexParameteriv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1', None, 'glTexImage1D', (GLenum, GLint, GLint, GLsizei, GLint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1', None, 'glTexImage2D', (GLenum, GLint, GLint, GLsizei, GLsizei, GLint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1', None, 'glDrawBuffer', (GLenum, ))
GL_PROC('GL_VERSION_1_1', None, 'glClear', (GLbitfield, ))
GL_PROC('GL_VERSION_1_1', None, 'glClearColor', (GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1', None, 'glClearStencil', (GLint, ))
GL_PROC('GL_VERSION_1_1', None, 'glClearDepth', (GLdouble, ))
GL_PROC('GL_VERSION_1_1', None, 'glStencilMask', (GLuint, ))
GL_PROC('GL_VERSION_1_1', None, 'glColorMask', (GLboolean, GLboolean, GLboolean, GLboolean, ))
GL_PROC('GL_VERSION_1_1', None, 'glDepthMask', (GLboolean, ))
GL_PROC('GL_VERSION_1_1', None, 'glDisable', (GLenum, ))
GL_PROC('GL_VERSION_1_1', None, 'glEnable', (GLenum, ))
GL_PROC('GL_VERSION_1_1', None, 'glFinish', ())
GL_PROC('GL_VERSION_1_1', None, 'glFlush', ())
GL_PROC('GL_VERSION_1_1', None, 'glBlendFunc', (GLenum, GLenum, ))
GL_PROC('GL_VERSION_1_1', None, 'glLogicOp', (GLenum, ))
GL_PROC('GL_VERSION_1_1', None, 'glStencilFunc', (GLenum, GLint, GLuint, ))
GL_PROC('GL_VERSION_1_1', None, 'glStencilOp', (GLenum, GLenum, GLenum, ))
GL_PROC('GL_VERSION_1_1', None, 'glDepthFunc', (GLenum, ))
GL_PROC('GL_VERSION_1_1', None, 'glPixelStoref', (GLenum, GLfloat, ))
GL_PROC('GL_VERSION_1_1', None, 'glPixelStorei', (GLenum, GLint, ))
GL_PROC('GL_VERSION_1_1', None, 'glReadBuffer', (GLenum, ))
GL_PROC('GL_VERSION_1_1', None, 'glReadPixels', (GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1', None, 'glGetBooleanv', (GLenum, ctypes.POINTER(GLboolean), ))
GL_PROC('GL_VERSION_1_1', None, 'glGetDoublev', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1', GLenum, 'glGetError', ())
GL_PROC('GL_VERSION_1_1', None, 'glGetFloatv', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1', None, 'glGetIntegerv', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1', ctypes.POINTER(char), 'glGetString', (GLenum, ))
GL_PROC('GL_VERSION_1_1', None, 'glGetTexImage', (GLenum, GLint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1', None, 'glGetTexParameterfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1', None, 'glGetTexParameteriv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1', None, 'glGetTexLevelParameterfv', (GLenum, GLint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1', None, 'glGetTexLevelParameteriv', (GLenum, GLint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1', GLboolean, 'glIsEnabled', (GLenum, ))
GL_PROC('GL_VERSION_1_1', None, 'glDepthRange', (GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1', None, 'glViewport', (GLint, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_VERSION_1_1', None, 'glDrawArrays', (GLenum, GLint, GLsizei, ))
GL_PROC('GL_VERSION_1_1', None, 'glDrawElements', (GLenum, GLsizei, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1', None, 'glGetPointerv', (GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_VERSION_1_1', None, 'glPolygonOffset', (GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1', None, 'glCopyTexImage1D', (GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLint, ))
GL_PROC('GL_VERSION_1_1', None, 'glCopyTexImage2D', (GLenum, GLint, GLenum, GLint, GLint, GLsizei, GLsizei, GLint, ))
GL_PROC('GL_VERSION_1_1', None, 'glCopyTexSubImage1D', (GLenum, GLint, GLint, GLint, GLint, GLsizei, ))
GL_PROC('GL_VERSION_1_1', None, 'glCopyTexSubImage2D', (GLenum, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_VERSION_1_1', None, 'glTexSubImage1D', (GLenum, GLint, GLint, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1', None, 'glTexSubImage2D', (GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1', None, 'glBindTexture', (GLenum, GLuint, ))
GL_PROC('GL_VERSION_1_1', None, 'glDeleteTextures', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_1_1', None, 'glGenTextures', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_1_1', GLboolean, 'glIsTexture', (GLuint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glNewList', (GLuint, GLenum, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEndList', ())
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glCallList', (GLuint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glCallLists', (GLsizei, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glDeleteLists', (GLuint, GLsizei, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', GLuint, 'glGenLists', (GLsizei, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glListBase', (GLuint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glBegin', (GLenum, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glBitmap', (GLsizei, GLsizei, GLfloat, GLfloat, GLfloat, GLfloat, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3b', (GLbyte, GLbyte, GLbyte, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3bv', (ctypes.POINTER(GLbyte), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3d', (GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3f', (GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3i', (GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3s', (GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3ub', (GLubyte, GLubyte, GLubyte, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3ubv', (ctypes.POINTER(GLubyte), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3ui', (GLuint, GLuint, GLuint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3uiv', (ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3us', (GLushort, GLushort, GLushort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor3usv', (ctypes.POINTER(GLushort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4b', (GLbyte, GLbyte, GLbyte, GLbyte, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4bv', (ctypes.POINTER(GLbyte), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4d', (GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4f', (GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4i', (GLint, GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4s', (GLshort, GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4ub', (GLubyte, GLubyte, GLubyte, GLubyte, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4ubv', (ctypes.POINTER(GLubyte), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4ui', (GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4uiv', (ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4us', (GLushort, GLushort, GLushort, GLushort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColor4usv', (ctypes.POINTER(GLushort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEdgeFlag', (GLboolean, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEdgeFlagv', (ctypes.POINTER(GLboolean), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEnd', ())
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glIndexd', (GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glIndexdv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glIndexf', (GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glIndexfv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glIndexi', (GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glIndexiv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glIndexs', (GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glIndexsv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glNormal3b', (GLbyte, GLbyte, GLbyte, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glNormal3bv', (ctypes.POINTER(GLbyte), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glNormal3d', (GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glNormal3dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glNormal3f', (GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glNormal3fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glNormal3i', (GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glNormal3iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glNormal3s', (GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glNormal3sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos2d', (GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos2dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos2f', (GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos2fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos2i', (GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos2iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos2s', (GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos2sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos3d', (GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos3dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos3f', (GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos3fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos3i', (GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos3iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos3s', (GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos3sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos4d', (GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos4dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos4f', (GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos4fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos4i', (GLint, GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos4iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos4s', (GLshort, GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRasterPos4sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRectd', (GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRectdv', (ctypes.POINTER(GLdouble), ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRectf', (GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRectfv', (ctypes.POINTER(GLfloat), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRecti', (GLint, GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRectiv', (ctypes.POINTER(GLint), ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRects', (GLshort, GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRectsv', (ctypes.POINTER(GLshort), ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord1d', (GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord1dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord1f', (GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord1fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord1i', (GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord1iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord1s', (GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord1sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord2d', (GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord2dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord2f', (GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord2fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord2i', (GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord2iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord2s', (GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord2sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord3d', (GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord3dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord3f', (GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord3fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord3i', (GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord3iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord3s', (GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord3sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord4d', (GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord4dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord4f', (GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord4fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord4i', (GLint, GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord4iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord4s', (GLshort, GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoord4sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex2d', (GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex2dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex2f', (GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex2fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex2i', (GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex2iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex2s', (GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex2sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex3d', (GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex3dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex3f', (GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex3fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex3i', (GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex3iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex3s', (GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex3sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex4d', (GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex4dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex4f', (GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex4fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex4i', (GLint, GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex4iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex4s', (GLshort, GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertex4sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glClipPlane', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColorMaterial', (GLenum, GLenum, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glFogf', (GLenum, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glFogfv', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glFogi', (GLenum, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glFogiv', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glLightf', (GLenum, GLenum, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glLightfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glLighti', (GLenum, GLenum, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glLightiv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glLightModelf', (GLenum, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glLightModelfv', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glLightModeli', (GLenum, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glLightModeliv', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glLineStipple', (GLint, GLushort, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMaterialf', (GLenum, GLenum, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMaterialfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMateriali', (GLenum, GLenum, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMaterialiv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPolygonStipple', (ctypes.POINTER(GLubyte), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glShadeModel', (GLenum, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexEnvf', (GLenum, GLenum, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexEnvfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexEnvi', (GLenum, GLenum, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexEnviv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexGend', (GLenum, GLenum, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexGendv', (GLenum, GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexGenf', (GLenum, GLenum, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexGenfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexGeni', (GLenum, GLenum, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexGeniv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glFeedbackBuffer', (GLsizei, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glSelectBuffer', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', GLint, 'glRenderMode', (GLenum, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glInitNames', ())
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glLoadName', (GLuint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPassThrough', (GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPopName', ())
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPushName', (GLuint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glClearAccum', (GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glClearIndex', (GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glIndexMask', (GLuint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glAccum', (GLenum, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPopAttrib', ())
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPushAttrib', (GLbitfield, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMap1d', (GLenum, GLdouble, GLdouble, GLint, GLint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMap1f', (GLenum, GLfloat, GLfloat, GLint, GLint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMap2d', (GLenum, GLdouble, GLdouble, GLint, GLint, GLdouble, GLdouble, GLint, GLint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMap2f', (GLenum, GLfloat, GLfloat, GLint, GLint, GLfloat, GLfloat, GLint, GLint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMapGrid1d', (GLint, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMapGrid1f', (GLint, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMapGrid2d', (GLint, GLdouble, GLdouble, GLint, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMapGrid2f', (GLint, GLfloat, GLfloat, GLint, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEvalCoord1d', (GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEvalCoord1dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEvalCoord1f', (GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEvalCoord1fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEvalCoord2d', (GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEvalCoord2dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEvalCoord2f', (GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEvalCoord2fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEvalMesh1', (GLenum, GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEvalPoint1', (GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEvalMesh2', (GLenum, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEvalPoint2', (GLint, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glAlphaFunc', (GLenum, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPixelZoom', (GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPixelTransferf', (GLenum, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPixelTransferi', (GLenum, GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPixelMapfv', (GLenum, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPixelMapuiv', (GLenum, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPixelMapusv', (GLenum, GLsizei, ctypes.POINTER(GLushort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glCopyPixels', (GLint, GLint, GLsizei, GLsizei, GLenum, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glDrawPixels', (GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetClipPlane', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetLightfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetLightiv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetMapdv', (GLenum, GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetMapfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetMapiv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetMaterialfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetMaterialiv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetPixelMapfv', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetPixelMapuiv', (GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetPixelMapusv', (GLenum, ctypes.POINTER(GLushort), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetPolygonStipple', (ctypes.POINTER(GLubyte), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetTexEnvfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetTexEnviv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetTexGendv', (GLenum, GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetTexGenfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glGetTexGeniv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', GLboolean, 'glIsList', (GLuint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glFrustum', (GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glLoadIdentity', ())
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glLoadMatrixf', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glLoadMatrixd', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMatrixMode', (GLenum, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMultMatrixf', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glMultMatrixd', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glOrtho', (GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPopMatrix', ())
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPushMatrix', ())
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRotated', (GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glRotatef', (GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glScaled', (GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glScalef', (GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTranslated', (GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTranslatef', (GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glArrayElement', (GLint, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glColorPointer', (GLint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glDisableClientState', (GLenum, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEdgeFlagPointer', (GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glEnableClientState', (GLenum, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glIndexPointer', (GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glInterleavedArrays', (GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glNormalPointer', (GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glTexCoordPointer', (GLint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glVertexPointer', (GLint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', GLboolean, 'glAreTexturesResident', (GLsizei, ctypes.POINTER(GLuint), ctypes.POINTER(GLboolean), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPrioritizeTextures', (GLsizei, ctypes.POINTER(GLuint), ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glIndexub', (GLubyte, ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glIndexubv', (ctypes.POINTER(GLubyte), ))
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPopClientAttrib', ())
GL_PROC('GL_VERSION_1_1_DEPRECATED', None, 'glPushClientAttrib', (GLbitfield, ))
GL_PROC('GL_VERSION_1_2', None, 'glBlendColor', (GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_2', None, 'glBlendEquation', (GLenum, ))
GL_PROC('GL_VERSION_1_2', None, 'glDrawRangeElements', (GLenum, GLuint, GLuint, GLsizei, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_2', None, 'glTexImage3D', (GLenum, GLint, GLint, GLsizei, GLsizei, GLsizei, GLint, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_2', None, 'glTexSubImage3D', (GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_2', None, 'glCopyTexSubImage3D', (GLenum, GLint, GLint, GLint, GLint, GLint, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glColorTable', (GLenum, GLenum, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glColorTableParameterfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glColorTableParameteriv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glCopyColorTable', (GLenum, GLenum, GLint, GLint, GLsizei, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glGetColorTable', (GLenum, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glGetColorTableParameterfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glGetColorTableParameteriv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glColorSubTable', (GLenum, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glCopyColorSubTable', (GLenum, GLsizei, GLint, GLint, GLsizei, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glConvolutionFilter1D', (GLenum, GLenum, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glConvolutionFilter2D', (GLenum, GLenum, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glConvolutionParameterf', (GLenum, GLenum, GLfloat, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glConvolutionParameterfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glConvolutionParameteri', (GLenum, GLenum, GLint, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glConvolutionParameteriv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glCopyConvolutionFilter1D', (GLenum, GLenum, GLint, GLint, GLsizei, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glCopyConvolutionFilter2D', (GLenum, GLenum, GLint, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glGetConvolutionFilter', (GLenum, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glGetConvolutionParameterfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glGetConvolutionParameteriv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glGetSeparableFilter', (GLenum, GLenum, GLenum, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glSeparableFilter2D', (GLenum, GLenum, GLsizei, GLsizei, GLenum, GLenum, ctypes.c_void_p, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glGetHistogram', (GLenum, GLboolean, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glGetHistogramParameterfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glGetHistogramParameteriv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glGetMinmax', (GLenum, GLboolean, GLenum, GLenum, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glGetMinmaxParameterfv', (GLenum, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glGetMinmaxParameteriv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glHistogram', (GLenum, GLsizei, GLenum, GLboolean, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glMinmax', (GLenum, GLenum, GLboolean, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glResetHistogram', (GLenum, ))
GL_PROC('GL_VERSION_1_2_DEPRECATED', None, 'glResetMinmax', (GLenum, ))
GL_PROC('GL_VERSION_1_3', None, 'glActiveTexture', (GLenum, ))
GL_PROC('GL_VERSION_1_3', None, 'glSampleCoverage', (GLfloat, GLboolean, ))
GL_PROC('GL_VERSION_1_3', None, 'glCompressedTexImage3D', (GLenum, GLint, GLenum, GLsizei, GLsizei, GLsizei, GLint, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_3', None, 'glCompressedTexImage2D', (GLenum, GLint, GLenum, GLsizei, GLsizei, GLint, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_3', None, 'glCompressedTexImage1D', (GLenum, GLint, GLenum, GLsizei, GLint, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_3', None, 'glCompressedTexSubImage3D', (GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_3', None, 'glCompressedTexSubImage2D', (GLenum, GLint, GLint, GLint, GLsizei, GLsizei, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_3', None, 'glCompressedTexSubImage1D', (GLenum, GLint, GLint, GLsizei, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_3', None, 'glGetCompressedTexImage', (GLenum, GLint, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glClientActiveTexture', (GLenum, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord1d', (GLenum, GLdouble, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord1dv', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord1f', (GLenum, GLfloat, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord1fv', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord1i', (GLenum, GLint, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord1iv', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord1s', (GLenum, GLshort, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord1sv', (GLenum, ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord2d', (GLenum, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord2dv', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord2f', (GLenum, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord2fv', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord2i', (GLenum, GLint, GLint, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord2iv', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord2s', (GLenum, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord2sv', (GLenum, ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord3d', (GLenum, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord3dv', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord3f', (GLenum, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord3fv', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord3i', (GLenum, GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord3iv', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord3s', (GLenum, GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord3sv', (GLenum, ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord4d', (GLenum, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord4dv', (GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord4f', (GLenum, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord4fv', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord4i', (GLenum, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord4iv', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord4s', (GLenum, GLshort, GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultiTexCoord4sv', (GLenum, ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glLoadTransposeMatrixf', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glLoadTransposeMatrixd', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultTransposeMatrixf', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_3_DEPRECATED', None, 'glMultTransposeMatrixd', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_4', None, 'glBlendFuncSeparate', (GLenum, GLenum, GLenum, GLenum, ))
GL_PROC('GL_VERSION_1_4', None, 'glMultiDrawArrays', (GLenum, ctypes.POINTER(GLint), ctypes.POINTER(GLsizei), GLsizei, ))
GL_PROC('GL_VERSION_1_4', None, 'glMultiDrawElements', (GLenum, ctypes.POINTER(GLsizei), GLenum, ctypes.POINTER(ctypes.c_void_p), GLsizei, ))
GL_PROC('GL_VERSION_1_4', None, 'glPointParameterf', (GLenum, GLfloat, ))
GL_PROC('GL_VERSION_1_4', None, 'glPointParameterfv', (GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_4', None, 'glPointParameteri', (GLenum, GLint, ))
GL_PROC('GL_VERSION_1_4', None, 'glPointParameteriv', (GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glFogCoordf', (GLfloat, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glFogCoordfv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glFogCoordd', (GLdouble, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glFogCoorddv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glFogCoordPointer', (GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3b', (GLbyte, GLbyte, GLbyte, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3bv', (ctypes.POINTER(GLbyte), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3d', (GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3f', (GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3i', (GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3s', (GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3ub', (GLubyte, GLubyte, GLubyte, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3ubv', (ctypes.POINTER(GLubyte), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3ui', (GLuint, GLuint, GLuint, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3uiv', (ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3us', (GLushort, GLushort, GLushort, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColor3usv', (ctypes.POINTER(GLushort), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glSecondaryColorPointer', (GLint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos2d', (GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos2dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos2f', (GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos2fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos2i', (GLint, GLint, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos2iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos2s', (GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos2sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos3d', (GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos3dv', (ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos3f', (GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos3fv', (ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos3i', (GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos3iv', (ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos3s', (GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_1_4_DEPRECATED', None, 'glWindowPos3sv', (ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_1_5', None, 'glGenQueries', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_1_5', None, 'glDeleteQueries', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_1_5', GLboolean, 'glIsQuery', (GLuint, ))
GL_PROC('GL_VERSION_1_5', None, 'glBeginQuery', (GLenum, GLuint, ))
GL_PROC('GL_VERSION_1_5', None, 'glEndQuery', (GLenum, ))
GL_PROC('GL_VERSION_1_5', None, 'glGetQueryiv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_5', None, 'glGetQueryObjectiv', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_5', None, 'glGetQueryObjectuiv', (GLuint, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_1_5', None, 'glBindBuffer', (GLenum, GLuint, ))
GL_PROC('GL_VERSION_1_5', None, 'glDeleteBuffers', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_1_5', None, 'glGenBuffers', (GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_1_5', GLboolean, 'glIsBuffer', (GLuint, ))
GL_PROC('GL_VERSION_1_5', None, 'glBufferData', (GLenum, GLsizeiptr, ctypes.c_void_p, GLenum, ))
GL_PROC('GL_VERSION_1_5', None, 'glBufferSubData', (GLenum, GLintptr, GLsizeiptr, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_5', None, 'glGetBufferSubData', (GLenum, GLintptr, GLsizeiptr, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_1_5', ctypes.c_void_p, 'glMapBuffer', (GLenum, GLenum, ))
GL_PROC('GL_VERSION_1_5', GLboolean, 'glUnmapBuffer', (GLenum, ))
GL_PROC('GL_VERSION_1_5', None, 'glGetBufferParameteriv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_1_5', None, 'glGetBufferPointerv', (GLenum, GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_VERSION_2_0', None, 'glBlendEquationSeparate', (GLenum, GLenum, ))
GL_PROC('GL_VERSION_2_0', None, 'glDrawBuffers', (GLsizei, ctypes.POINTER(GLenum), ))
GL_PROC('GL_VERSION_2_0', None, 'glStencilOpSeparate', (GLenum, GLenum, GLenum, GLenum, ))
GL_PROC('GL_VERSION_2_0', None, 'glStencilFuncSeparate', (GLenum, GLenum, GLint, GLuint, ))
GL_PROC('GL_VERSION_2_0', None, 'glStencilMaskSeparate', (GLenum, GLuint, ))
GL_PROC('GL_VERSION_2_0', None, 'glAttachShader', (GLuint, GLuint, ))
GL_PROC('GL_VERSION_2_0', None, 'glBindAttribLocation', (GLuint, GLuint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_VERSION_2_0', None, 'glCompileShader', (GLuint, ))
GL_PROC('GL_VERSION_2_0', GLuint, 'glCreateProgram', ())
GL_PROC('GL_VERSION_2_0', GLuint, 'glCreateShader', (GLenum, ))
GL_PROC('GL_VERSION_2_0', None, 'glDeleteProgram', (GLuint, ))
GL_PROC('GL_VERSION_2_0', None, 'glDeleteShader', (GLuint, ))
GL_PROC('GL_VERSION_2_0', None, 'glDetachShader', (GLuint, GLuint, ))
GL_PROC('GL_VERSION_2_0', None, 'glDisableVertexAttribArray', (GLuint, ))
GL_PROC('GL_VERSION_2_0', None, 'glEnableVertexAttribArray', (GLuint, ))
GL_PROC('GL_VERSION_2_0', None, 'glGetActiveAttrib', (GLuint, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLint), ctypes.POINTER(GLenum), ctypes.POINTER(GLchar), ))
GL_PROC('GL_VERSION_2_0', None, 'glGetActiveUniform', (GLuint, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLint), ctypes.POINTER(GLenum), ctypes.POINTER(GLchar), ))
GL_PROC('GL_VERSION_2_0', None, 'glGetAttachedShaders', (GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_2_0', GLint, 'glGetAttribLocation', (GLuint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_VERSION_2_0', None, 'glGetProgramiv', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_2_0', None, 'glGetProgramInfoLog', (GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_VERSION_2_0', None, 'glGetShaderiv', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_2_0', None, 'glGetShaderInfoLog', (GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_VERSION_2_0', None, 'glGetShaderSource', (GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLchar), ))
GL_PROC('GL_VERSION_2_0', GLint, 'glGetUniformLocation', (GLuint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_VERSION_2_0', None, 'glGetUniformfv', (GLuint, GLint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_0', None, 'glGetUniformiv', (GLuint, GLint, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_2_0', None, 'glGetVertexAttribdv', (GLuint, GLenum, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_2_0', None, 'glGetVertexAttribfv', (GLuint, GLenum, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_0', None, 'glGetVertexAttribiv', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_2_0', None, 'glGetVertexAttribPointerv', (GLuint, GLenum, ctypes.POINTER(ctypes.c_void_p), ))
GL_PROC('GL_VERSION_2_0', GLboolean, 'glIsProgram', (GLuint, ))
GL_PROC('GL_VERSION_2_0', GLboolean, 'glIsShader', (GLuint, ))
GL_PROC('GL_VERSION_2_0', None, 'glLinkProgram', (GLuint, ))
GL_PROC('GL_VERSION_2_0', None, 'glShaderSource', (GLuint, GLsizei, ctypes.POINTER(ctypes.POINTER(GLchar)), ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_2_0', None, 'glUseProgram', (GLuint, ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform1f', (GLint, GLfloat, ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform2f', (GLint, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform3f', (GLint, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform4f', (GLint, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform1i', (GLint, GLint, ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform2i', (GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform3i', (GLint, GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform4i', (GLint, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform1fv', (GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform2fv', (GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform3fv', (GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform4fv', (GLint, GLsizei, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform1iv', (GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform2iv', (GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform3iv', (GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_2_0', None, 'glUniform4iv', (GLint, GLsizei, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_2_0', None, 'glUniformMatrix2fv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_0', None, 'glUniformMatrix3fv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_0', None, 'glUniformMatrix4fv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_0', None, 'glValidateProgram', (GLuint, ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib1d', (GLuint, GLdouble, ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib1dv', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib1f', (GLuint, GLfloat, ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib1fv', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib1s', (GLuint, GLshort, ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib1sv', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib2d', (GLuint, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib2dv', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib2f', (GLuint, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib2fv', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib2s', (GLuint, GLshort, GLshort, ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib2sv', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib3d', (GLuint, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib3dv', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib3f', (GLuint, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib3fv', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib3s', (GLuint, GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib3sv', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4Nbv', (GLuint, ctypes.POINTER(GLbyte), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4Niv', (GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4Nsv', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4Nub', (GLuint, GLubyte, GLubyte, GLubyte, GLubyte, ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4Nubv', (GLuint, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4Nuiv', (GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4Nusv', (GLuint, ctypes.POINTER(GLushort), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4bv', (GLuint, ctypes.POINTER(GLbyte), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4d', (GLuint, GLdouble, GLdouble, GLdouble, GLdouble, ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4dv', (GLuint, ctypes.POINTER(GLdouble), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4f', (GLuint, GLfloat, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4fv', (GLuint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4iv', (GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4s', (GLuint, GLshort, GLshort, GLshort, GLshort, ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4sv', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4ubv', (GLuint, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4uiv', (GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttrib4usv', (GLuint, ctypes.POINTER(GLushort), ))
GL_PROC('GL_VERSION_2_0', None, 'glVertexAttribPointer', (GLuint, GLint, GLenum, GLboolean, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_2_1', None, 'glUniformMatrix2x3fv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_1', None, 'glUniformMatrix3x2fv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_1', None, 'glUniformMatrix2x4fv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_1', None, 'glUniformMatrix4x2fv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_1', None, 'glUniformMatrix3x4fv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_2_1', None, 'glUniformMatrix4x3fv', (GLint, GLsizei, GLboolean, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_3_0', None, 'glColorMaski', (GLuint, GLboolean, GLboolean, GLboolean, GLboolean, ))
GL_PROC('GL_VERSION_3_0', None, 'glGetBooleani_v', (GLenum, GLuint, ctypes.POINTER(GLboolean), ))
GL_PROC('GL_VERSION_3_0', None, 'glGetIntegeri_v', (GLenum, GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_3_0', None, 'glEnablei', (GLenum, GLuint, ))
GL_PROC('GL_VERSION_3_0', None, 'glDisablei', (GLenum, GLuint, ))
GL_PROC('GL_VERSION_3_0', GLboolean, 'glIsEnabledi', (GLenum, GLuint, ))
GL_PROC('GL_VERSION_3_0', None, 'glBeginTransformFeedback', (GLenum, ))
GL_PROC('GL_VERSION_3_0', None, 'glEndTransformFeedback', ())
GL_PROC('GL_VERSION_3_0', None, 'glBindBufferRange', (GLenum, GLuint, GLuint, GLintptr, GLsizeiptr, ))
GL_PROC('GL_VERSION_3_0', None, 'glBindBufferBase', (GLenum, GLuint, GLuint, ))
GL_PROC('GL_VERSION_3_0', None, 'glTransformFeedbackVaryings', (GLuint, GLsizei, ctypes.POINTER(ctypes.POINTER(GLchar)), GLenum, ))
GL_PROC('GL_VERSION_3_0', None, 'glGetTransformFeedbackVarying', (GLuint, GLuint, GLsizei, ctypes.POINTER(GLsizei), ctypes.POINTER(GLsizei), ctypes.POINTER(GLenum), ctypes.POINTER(GLchar), ))
GL_PROC('GL_VERSION_3_0', None, 'glClampColor', (GLenum, GLenum, ))
GL_PROC('GL_VERSION_3_0', None, 'glBeginConditionalRender', (GLuint, GLenum, ))
GL_PROC('GL_VERSION_3_0', None, 'glEndConditionalRender', ())
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribIPointer', (GLuint, GLint, GLenum, GLsizei, ctypes.c_void_p, ))
GL_PROC('GL_VERSION_3_0', None, 'glGetVertexAttribIiv', (GLuint, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_3_0', None, 'glGetVertexAttribIuiv', (GLuint, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI1i', (GLuint, GLint, ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI2i', (GLuint, GLint, GLint, ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI3i', (GLuint, GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI4i', (GLuint, GLint, GLint, GLint, GLint, ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI1ui', (GLuint, GLuint, ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI2ui', (GLuint, GLuint, GLuint, ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI3ui', (GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI4ui', (GLuint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI1iv', (GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI2iv', (GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI3iv', (GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI4iv', (GLuint, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI1uiv', (GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI2uiv', (GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI3uiv', (GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI4uiv', (GLuint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI4bv', (GLuint, ctypes.POINTER(GLbyte), ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI4sv', (GLuint, ctypes.POINTER(GLshort), ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI4ubv', (GLuint, ctypes.POINTER(GLubyte), ))
GL_PROC('GL_VERSION_3_0', None, 'glVertexAttribI4usv', (GLuint, ctypes.POINTER(GLushort), ))
GL_PROC('GL_VERSION_3_0', None, 'glGetUniformuiv', (GLuint, GLint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_3_0', None, 'glBindFragDataLocation', (GLuint, GLuint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_VERSION_3_0', GLint, 'glGetFragDataLocation', (GLuint, ctypes.POINTER(GLchar), ))
GL_PROC('GL_VERSION_3_0', None, 'glUniform1ui', (GLint, GLuint, ))
GL_PROC('GL_VERSION_3_0', None, 'glUniform2ui', (GLint, GLuint, GLuint, ))
GL_PROC('GL_VERSION_3_0', None, 'glUniform3ui', (GLint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_VERSION_3_0', None, 'glUniform4ui', (GLint, GLuint, GLuint, GLuint, GLuint, ))
GL_PROC('GL_VERSION_3_0', None, 'glUniform1uiv', (GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_3_0', None, 'glUniform2uiv', (GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_3_0', None, 'glUniform3uiv', (GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_3_0', None, 'glUniform4uiv', (GLint, GLsizei, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_3_0', None, 'glTexParameterIiv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_3_0', None, 'glTexParameterIuiv', (GLenum, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_3_0', None, 'glGetTexParameterIiv', (GLenum, GLenum, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_3_0', None, 'glGetTexParameterIuiv', (GLenum, GLenum, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_3_0', None, 'glClearBufferiv', (GLenum, GLint, ctypes.POINTER(GLint), ))
GL_PROC('GL_VERSION_3_0', None, 'glClearBufferuiv', (GLenum, GLint, ctypes.POINTER(GLuint), ))
GL_PROC('GL_VERSION_3_0', None, 'glClearBufferfv', (GLenum, GLint, ctypes.POINTER(GLfloat), ))
GL_PROC('GL_VERSION_3_0', None, 'glClearBufferfi', (GLenum, GLint, GLfloat, GLint, ))
GL_PROC('GL_VERSION_3_0', ctypes.POINTER(char), 'glGetStringi', (GLenum, GLuint, ))
GL_PROC('GL_VERSION_3_1', None, 'glDrawArraysInstanced', (GLenum, GLint, GLsizei, GLsizei, ))
GL_PROC('GL_VERSION_3_1', None, 'glDrawElementsInstanced', (GLenum, GLsizei, GLenum, ctypes.c_void_p, GLsizei, ))
GL_PROC('GL_VERSION_3_1', None, 'glTexBuffer', (GLenum, GLenum, GLuint, ))
GL_PROC('GL_VERSION_3_1', None, 'glPrimitiveRestartIndex', (GLuint, ))
GL_PROC('GL_VERSION_3_2', None, 'glGetInteger64i_v', (GLenum, GLuint, ctypes.POINTER(GLint64), ))
GL_PROC('GL_VERSION_3_2', None, 'glGetBufferParameteri64v', (GLenum, GLenum, ctypes.POINTER(GLint64), ))
GL_PROC('GL_VERSION_3_2', None, 'glFramebufferTexture', (GLenum, GLenum, GLuint, GLint, ))
GL_PROC('GL_VERSION_3_3', None, 'glVertexAttribDivisor', (GLuint, GLuint, ))
GL_PROC('GL_VERSION_4_0', None, 'glMinSampleShading', (GLfloat, ))
GL_PROC('GL_VERSION_4_0', None, 'glBlendEquationi', (GLuint, GLenum, ))
GL_PROC('GL_VERSION_4_0', None, 'glBlendEquationSeparatei', (GLuint, GLenum, GLenum, ))
GL_PROC('GL_VERSION_4_0', None, 'glBlendFunci', (GLuint, GLenum, GLenum, ))
GL_PROC('GL_VERSION_4_0', None, 'glBlendFuncSeparatei', (GLuint, GLenum, GLenum, GLenum, GLenum, ))

"""
GL_PROC('GL_NV_copy_image', BOOL, 'wglCopyImageSubDataNV', (HGLRC, GLuint, GLenum, GLint, GLint, GLint, GLint, HGLRC, GLuint, GLenum, GLint, GLint, GLint, GLint, GLsizei, GLsizei, GLsizei, ))
GL_PROC('GL_NV_present_video', int, 'wglEnumerateVideoDevicesNV', (HDC, ctypes.POINTER(HVIDEOOUTPUTDEVICENV), ))
GL_PROC('GL_NV_present_video', BOOL, 'wglBindVideoDeviceNV', (HDC, unsigned int, HVIDEOOUTPUTDEVICENV, ctypes.POINTER(int), ))
GL_PROC('GL_NV_present_video', BOOL, 'wglQueryCurrentContextNV', (int, ctypes.POINTER(int), ))
GL_PROC('GL_NV_vertex_array_range', ctypes.c_void_p, 'wglAllocateMemoryNV', (GLsizei, GLfloat, GLfloat, GLfloat, ))
GL_PROC('GL_NV_vertex_array_range', None, 'wglFreeMemoryNV', (ctypes.c_void_p, ))
GL_PROC('GL_NV_video_capture', BOOL, 'wglBindVideoCaptureDeviceNV', (UINT, HVIDEOINPUTDEVICENV, ))
GL_PROC('GL_NV_video_capture', UINT, 'wglEnumerateVideoCaptureDevicesNV', (HDC, ctypes.POINTER(HVIDEOINPUTDEVICENV), ))
GL_PROC('GL_NV_video_capture', BOOL, 'wglLockVideoCaptureDeviceNV', (HDC, HVIDEOINPUTDEVICENV, ))
GL_PROC('GL_NV_video_capture', BOOL, 'wglQueryVideoCaptureDeviceNV', (HDC, HVIDEOINPUTDEVICENV, int, ctypes.POINTER(int), ))
GL_PROC('GL_NV_video_capture', BOOL, 'wglReleaseVideoCaptureDeviceNV', (HDC, HVIDEOINPUTDEVICENV, ))
GL_PROC('WGL_3DL_stereo_control', BOOL, 'wglSetStereoEmitterState3DL', (HDC, UINT, ))
GL_PROC('WGL_AMD_gpu_association', UINT, 'wglGetGPUIDsAMD', (UINT, ctypes.POINTER(UINT), ))
GL_PROC('WGL_AMD_gpu_association', INT, 'wglGetGPUInfoAMD', (UINT, int, GLenum, UINT, ctypes.c_void_p, ))
GL_PROC('WGL_AMD_gpu_association', UINT, 'wglGetContextGPUIDAMD', (HGLRC, ))
GL_PROC('WGL_AMD_gpu_association', HGLRC, 'wglCreateAssociatedContextAMD', (UINT, ))
GL_PROC('WGL_AMD_gpu_association', HGLRC, 'wglCreateAssociatedContextAttribsAMD', (UINT, HGLRC, ctypes.POINTER(int), ))
GL_PROC('WGL_AMD_gpu_association', BOOL, 'wglDeleteAssociatedContextAMD', (HGLRC, ))
GL_PROC('WGL_AMD_gpu_association', BOOL, 'wglMakeAssociatedContextCurrentAMD', (HGLRC, ))
GL_PROC('WGL_AMD_gpu_association', HGLRC, 'wglGetCurrentAssociatedContextAMD', ())
GL_PROC('WGL_AMD_gpu_association', VOID, 'wglBlitContextFramebufferAMD', (HGLRC, GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLint, GLbitfield, GLenum, ))
GL_PROC('WGL_ARB_buffer_region', HANDLE, 'wglCreateBufferRegionARB', (HDC, int, UINT, ))
GL_PROC('WGL_ARB_buffer_region', VOID, 'wglDeleteBufferRegionARB', (HANDLE, ))
GL_PROC('WGL_ARB_buffer_region', BOOL, 'wglSaveBufferRegionARB', (HANDLE, int, int, int, int, ))
GL_PROC('WGL_ARB_buffer_region', BOOL, 'wglRestoreBufferRegionARB', (HANDLE, int, int, int, int, int, int, ))
GL_PROC('WGL_ARB_create_context', HGLRC, 'wglCreateContextAttribsARB', (HDC, HGLRC, ctypes.POINTER(int), ))
GL_PROC('WGL_ARB_extensions_string', ctypes.POINTER(char), 'wglGetExtensionsStringARB', (HDC, ))
GL_PROC('WGL_ARB_make_current_read', BOOL, 'wglMakeContextCurrentARB', (HDC, HDC, HGLRC, ))
GL_PROC('WGL_ARB_make_current_read', HDC, 'wglGetCurrentReadDCARB', ())
GL_PROC('WGL_ARB_pbuffer', HPBUFFERARB, 'wglCreatePbufferARB', (HDC, int, int, int, ctypes.POINTER(int), ))
GL_PROC('WGL_ARB_pbuffer', HDC, 'wglGetPbufferDCARB', (HPBUFFERARB, ))
GL_PROC('WGL_ARB_pbuffer', int, 'wglReleasePbufferDCARB', (HPBUFFERARB, HDC, ))
GL_PROC('WGL_ARB_pbuffer', BOOL, 'wglDestroyPbufferARB', (HPBUFFERARB, ))
GL_PROC('WGL_ARB_pbuffer', BOOL, 'wglQueryPbufferARB', (HPBUFFERARB, int, ctypes.POINTER(int), ))
GL_PROC('WGL_ARB_pixel_format', BOOL, 'wglGetPixelFormatAttribivARB', (HDC, int, int, UINT, ctypes.POINTER(int), ctypes.POINTER(int), ))
GL_PROC('WGL_ARB_pixel_format', BOOL, 'wglGetPixelFormatAttribfvARB', (HDC, int, int, UINT, ctypes.POINTER(int), ctypes.POINTER(FLOAT), ))
GL_PROC('WGL_ARB_pixel_format', BOOL, 'wglChoosePixelFormatARB', (HDC, ctypes.POINTER(int), ctypes.POINTER(FLOAT), UINT, ctypes.POINTER(int), ctypes.POINTER(UINT), ))
GL_PROC('WGL_ARB_render_texture', BOOL, 'wglBindTexImageARB', (HPBUFFERARB, int, ))
GL_PROC('WGL_ARB_render_texture', BOOL, 'wglReleaseTexImageARB', (HPBUFFERARB, int, ))
GL_PROC('WGL_ARB_render_texture', BOOL, 'wglSetPbufferAttribARB', (HPBUFFERARB, ctypes.POINTER(int), ))
GL_PROC('WGL_EXT_display_color_table', GLboolean, 'wglCreateDisplayColorTableEXT', (GLushort, ))
GL_PROC('WGL_EXT_display_color_table', GLboolean, 'wglLoadDisplayColorTableEXT', (ctypes.POINTER(GLushort), GLuint, ))
GL_PROC('WGL_EXT_display_color_table', GLboolean, 'wglBindDisplayColorTableEXT', (GLushort, ))
GL_PROC('WGL_EXT_display_color_table', VOID, 'wglDestroyDisplayColorTableEXT', (GLushort, ))
GL_PROC('WGL_EXT_extensions_string', ctypes.POINTER(char), 'wglGetExtensionsStringEXT', ())
GL_PROC('WGL_EXT_make_current_read', BOOL, 'wglMakeContextCurrentEXT', (HDC, HDC, HGLRC, ))
GL_PROC('WGL_EXT_make_current_read', HDC, 'wglGetCurrentReadDCEXT', ())
GL_PROC('WGL_EXT_pbuffer', HPBUFFEREXT, 'wglCreatePbufferEXT', (HDC, int, int, int, ctypes.POINTER(int), ))
GL_PROC('WGL_EXT_pbuffer', HDC, 'wglGetPbufferDCEXT', (HPBUFFEREXT, ))
GL_PROC('WGL_EXT_pbuffer', int, 'wglReleasePbufferDCEXT', (HPBUFFEREXT, HDC, ))
GL_PROC('WGL_EXT_pbuffer', BOOL, 'wglDestroyPbufferEXT', (HPBUFFEREXT, ))
GL_PROC('WGL_EXT_pbuffer', BOOL, 'wglQueryPbufferEXT', (HPBUFFEREXT, int, ctypes.POINTER(int), ))
GL_PROC('WGL_EXT_pixel_format', BOOL, 'wglGetPixelFormatAttribivEXT', (HDC, int, int, UINT, ctypes.POINTER(int), ctypes.POINTER(int), ))
GL_PROC('WGL_EXT_pixel_format', BOOL, 'wglGetPixelFormatAttribfvEXT', (HDC, int, int, UINT, ctypes.POINTER(int), ctypes.POINTER(FLOAT), ))
GL_PROC('WGL_EXT_pixel_format', BOOL, 'wglChoosePixelFormatEXT', (HDC, ctypes.POINTER(int), ctypes.POINTER(FLOAT), UINT, ctypes.POINTER(int), ctypes.POINTER(UINT), ))
GL_PROC('WGL_EXT_swap_control', BOOL, 'wglSwapIntervalEXT', (int, ))
GL_PROC('WGL_EXT_swap_control', int, 'wglGetSwapIntervalEXT', ())
GL_PROC('WGL_I3D_digital_video_control', BOOL, 'wglGetDigitalVideoParametersI3D', (HDC, int, ctypes.POINTER(int), ))
GL_PROC('WGL_I3D_digital_video_control', BOOL, 'wglSetDigitalVideoParametersI3D', (HDC, int, ctypes.POINTER(int), ))
GL_PROC('WGL_I3D_gamma', BOOL, 'wglGetGammaTableParametersI3D', (HDC, int, ctypes.POINTER(int), ))
GL_PROC('WGL_I3D_gamma', BOOL, 'wglSetGammaTableParametersI3D', (HDC, int, ctypes.POINTER(int), ))
GL_PROC('WGL_I3D_gamma', BOOL, 'wglGetGammaTableI3D', (HDC, int, ctypes.POINTER(USHORT), ctypes.POINTER(USHORT), ctypes.POINTER(USHORT), ))
GL_PROC('WGL_I3D_gamma', BOOL, 'wglSetGammaTableI3D', (HDC, int, ctypes.POINTER(USHORT), ctypes.POINTER(USHORT), ctypes.POINTER(USHORT), ))
GL_PROC('WGL_I3D_genlock', BOOL, 'wglEnableGenlockI3D', (HDC, ))
GL_PROC('WGL_I3D_genlock', BOOL, 'wglDisableGenlockI3D', (HDC, ))
GL_PROC('WGL_I3D_genlock', BOOL, 'wglIsEnabledGenlockI3D', (HDC, ctypes.POINTER(BOOL), ))
GL_PROC('WGL_I3D_genlock', BOOL, 'wglGenlockSourceI3D', (HDC, UINT, ))
GL_PROC('WGL_I3D_genlock', BOOL, 'wglGetGenlockSourceI3D', (HDC, ctypes.POINTER(UINT), ))
GL_PROC('WGL_I3D_genlock', BOOL, 'wglGenlockSourceEdgeI3D', (HDC, UINT, ))
GL_PROC('WGL_I3D_genlock', BOOL, 'wglGetGenlockSourceEdgeI3D', (HDC, ctypes.POINTER(UINT), ))
GL_PROC('WGL_I3D_genlock', BOOL, 'wglGenlockSampleRateI3D', (HDC, UINT, ))
GL_PROC('WGL_I3D_genlock', BOOL, 'wglGetGenlockSampleRateI3D', (HDC, ctypes.POINTER(UINT), ))
GL_PROC('WGL_I3D_genlock', BOOL, 'wglGenlockSourceDelayI3D', (HDC, UINT, ))
GL_PROC('WGL_I3D_genlock', BOOL, 'wglGetGenlockSourceDelayI3D', (HDC, ctypes.POINTER(UINT), ))
GL_PROC('WGL_I3D_genlock', BOOL, 'wglQueryGenlockMaxSourceDelayI3D', (HDC, ctypes.POINTER(UINT), ctypes.POINTER(UINT), ))
GL_PROC('WGL_I3D_image_buffer', LPVOID, 'wglCreateImageBufferI3D', (HDC, DWORD, UINT, ))
GL_PROC('WGL_I3D_image_buffer', BOOL, 'wglDestroyImageBufferI3D', (HDC, LPVOID, ))
GL_PROC('WGL_I3D_image_buffer', BOOL, 'wglAssociateImageBufferEventsI3D', (HDC, ctypes.POINTER(HANDLE), ctypes.POINTER(LPVOID), ctypes.POINTER(DWORD), UINT, ))
GL_PROC('WGL_I3D_image_buffer', BOOL, 'wglReleaseImageBufferEventsI3D', (HDC, ctypes.POINTER(LPVOID), UINT, ))
GL_PROC('WGL_I3D_swap_frame_lock', BOOL, 'wglEnableFrameLockI3D', ())
GL_PROC('WGL_I3D_swap_frame_lock', BOOL, 'wglDisableFrameLockI3D', ())
GL_PROC('WGL_I3D_swap_frame_lock', BOOL, 'wglIsEnabledFrameLockI3D', (ctypes.POINTER(BOOL), ))
GL_PROC('WGL_I3D_swap_frame_lock', BOOL, 'wglQueryFrameLockMasterI3D', (ctypes.POINTER(BOOL), ))
GL_PROC('WGL_I3D_swap_frame_usage', BOOL, 'wglGetFrameUsageI3D', (ctypes.POINTER(float), ))
GL_PROC('WGL_I3D_swap_frame_usage', BOOL, 'wglBeginFrameTrackingI3D', ())
GL_PROC('WGL_I3D_swap_frame_usage', BOOL, 'wglEndFrameTrackingI3D', ())
GL_PROC('WGL_I3D_swap_frame_usage', BOOL, 'wglQueryFrameTrackingI3D', (ctypes.POINTER(DWORD), ctypes.POINTER(DWORD), ctypes.POINTER(float), ))
GL_PROC('WGL_NV_DX_interop', BOOL, 'wglDXSetResourceShareHandleNV', (ctypes.c_void_p, HANDLE, ))
GL_PROC('WGL_NV_DX_interop', HANDLE, 'wglDXOpenDeviceNV', (ctypes.c_void_p, ))
GL_PROC('WGL_NV_DX_interop', BOOL, 'wglDXCloseDeviceNV', (HANDLE, ))
GL_PROC('WGL_NV_DX_interop', HANDLE, 'wglDXRegisterObjectNV', (HANDLE, ctypes.c_void_p, GLuint, GLenum, GLenum, ))
GL_PROC('WGL_NV_DX_interop', BOOL, 'wglDXUnregisterObjectNV', (HANDLE, HANDLE, ))
GL_PROC('WGL_NV_DX_interop', BOOL, 'wglDXObjectAccessNV', (HANDLE, GLenum, ))
GL_PROC('WGL_NV_DX_interop', BOOL, 'wglDXLockObjectsNV', (HANDLE, GLint, ctypes.POINTER(HANDLE), ))
GL_PROC('WGL_NV_gpu_affinity', BOOL, 'wglEnumGpusNV', (UINT, ctypes.POINTER(HGPUNV), ))
GL_PROC('WGL_NV_gpu_affinity', BOOL, 'wglEnumGpuDevicesNV', (HGPUNV, UINT, PGPU_DEVICE, ))
GL_PROC('WGL_NV_gpu_affinity', HDC, 'wglCreateAffinityDCNV', (ctypes.POINTER(HGPUNV), ))
GL_PROC('WGL_NV_gpu_affinity', BOOL, 'wglEnumGpusFromAffinityDCNV', (HDC, UINT, ctypes.POINTER(HGPUNV), ))
GL_PROC('WGL_NV_gpu_affinity', BOOL, 'wglDeleteDCNV', (HDC, ))
GL_PROC('WGL_NV_swap_group', BOOL, 'wglJoinSwapGroupNV', (HDC, GLuint, ))
GL_PROC('WGL_NV_swap_group', BOOL, 'wglBindSwapBarrierNV', (GLuint, GLuint, ))
GL_PROC('WGL_NV_swap_group', BOOL, 'wglQuerySwapGroupNV', (HDC, ctypes.POINTER(GLuint), ctypes.POINTER(GLuint), ))
GL_PROC('WGL_NV_swap_group', BOOL, 'wglQueryMaxSwapGroupsNV', (HDC, ctypes.POINTER(GLuint), ctypes.POINTER(GLuint), ))
GL_PROC('WGL_NV_swap_group', BOOL, 'wglQueryFrameCountNV', (HDC, ctypes.POINTER(GLuint), ))
GL_PROC('WGL_NV_swap_group', BOOL, 'wglResetFrameCountNV', (HDC, ))
GL_PROC('WGL_NV_video_output', BOOL, 'wglGetVideoDeviceNV', (HDC, int, ctypes.POINTER(HPVIDEODEV), ))
GL_PROC('WGL_NV_video_output', BOOL, 'wglReleaseVideoDeviceNV', (HPVIDEODEV, ))
GL_PROC('WGL_NV_video_output', BOOL, 'wglBindVideoImageNV', (HPVIDEODEV, HPBUFFERARB, int, ))
GL_PROC('WGL_NV_video_output', BOOL, 'wglReleaseVideoImageNV', (HPBUFFERARB, int, ))
GL_PROC('WGL_NV_video_output', BOOL, 'wglSendPbufferToVideoNV', (HPBUFFERARB, int, ctypes.POINTER(unsigned long), BOOL, ))
GL_PROC('WGL_NV_video_output', BOOL, 'wglGetVideoInfoNV', (HPVIDEODEV, ctypes.POINTER(unsigned long), ctypes.POINTER(unsigned long), ))
GL_PROC('WGL_OML_sync_control', BOOL, 'wglGetSyncValuesOML', (HDC, ctypes.POINTER(INT64), ctypes.POINTER(INT64), ctypes.POINTER(INT64), ))
GL_PROC('WGL_OML_sync_control', BOOL, 'wglGetMscRateOML', (HDC, ctypes.POINTER(INT32), ctypes.POINTER(INT32), ))
GL_PROC('WGL_OML_sync_control', INT64, 'wglSwapBuffersMscOML', (HDC, INT64, INT64, INT64, ))
GL_PROC('WGL_OML_sync_control', INT64, 'wglSwapLayerBuffersMscOML', (HDC, int, INT64, INT64, INT64, ))
GL_PROC('WGL_OML_sync_control', BOOL, 'wglWaitForMscOML', (HDC, INT64, INT64, INT64, ctypes.POINTER(INT64), ctypes.POINTER(INT64), ctypes.POINTER(INT64), ))
GL_PROC('WGL_OML_sync_control', BOOL, 'wglWaitForSbcOML', (HDC, INT64, ctypes.POINTER(INT64), ctypes.POINTER(INT64), ctypes.POINTER(INT64), ))
"""

#

for n in dir():
  if n.startswith("SUPP"):
    print n, globals()[n]


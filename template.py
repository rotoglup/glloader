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

%(GL_categories)s

"""
%(WGL_categories)s
"""

%(GL_enums)s

"""
%(WGL_enums)s
"""

%(GL_commands)s

"""
%(WGL_commands)s
"""

#

for n in dir():
  if n.startswith("SUPP"):
    print n, globals()[n]


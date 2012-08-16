/*

To get a header file to include, #define GLLOADER_HEADER_ONLY and #include this file
afterwards.

Call 'glLoaderInit()' to load GL core & extensions function pointers. This requires
a current GL context, created using core wgl functions provided by GDI. Meaning that
you have to link with opengl32.lib to get these functions.

Extension support is provided through variables named with the following
convention :
    
    int GLLOADER_SUPPORTS_<extension_name>

*/
/* begin header file **********************************************************/

#pragma comment(lib, "opengl32.lib")

#ifndef GLLOADER_THIS_FILE_IS_INCLUDED

#define GLLOADER_THIS_FILE "glloader.c"
#define GLLOADER_THIS_FILE_IS_INCLUDED

#ifndef GLLOADER_DECLARE_EXTS
# define GLLOADER_DECLARE_EXTS 1
#endif
#ifndef GLLOADER_DECLARE_ENUMS
# define GLLOADER_DECLARE_ENUMS 1
#endif
#ifndef GLLOADER_DECLARE_COMMANDS
# define GLLOADER_DECLARE_COMMANDS 1
#endif
#ifndef GLLOADER_SUPPORTS_NAME
# define GLLOADER_SUPPORTS_NAME(x) SUPPORTS_##x
#endif
#ifndef GLAPI
# define GLAPI extern
#endif

// TODO
#define NOMINMAX          // Macros min(a,b) and max(a,b)
#include <windows.h>
#undef NOMINMAX

/* typedef, manually taken from spec files */

typedef unsigned int GLenum;
typedef unsigned int GLbitfield;
typedef unsigned int GLuint;
typedef int GLint;
typedef int GLsizei;
typedef unsigned char GLboolean;
typedef signed char GLbyte;
typedef short GLshort;
typedef unsigned char GLubyte;
typedef unsigned short GLushort;
typedef unsigned long GLulong;
typedef float GLfloat;
typedef float GLclampf;
typedef double GLdouble;
typedef double GLclampd;
typedef void GLvoid;

#include <stddef.h>

/* GL type for program/shader text */
typedef char GLchar;

/* GL types for handling large vertex buffer objects */
typedef ptrdiff_t GLintptr;
typedef ptrdiff_t GLsizeiptr;

/* GL types for handling large vertex buffer objects */
typedef ptrdiff_t GLintptrARB;
typedef ptrdiff_t GLsizeiptrARB;

/* GL types for program/shader text and shader object handles */
typedef char GLcharARB;
typedef unsigned int GLhandleARB;

/* GL type for "half" precision (s10e5) float data in host memory */
typedef unsigned short GLhalfARB;

typedef unsigned short GLhalfNV;

#ifndef GLEXT_64_TYPES_DEFINED
/* This code block is duplicated in glxext.h, so must be protected */
#define GLEXT_64_TYPES_DEFINED
/* Define int32_t, int64_t, and uint64_t types for UST/MSC */
/* (as used in the GL_EXT_timer_query extension). */
#if defined(__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
#include <inttypes.h>
#elif defined(__sun__) || defined(__digital__)
#include <inttypes.h>
#if defined(__STDC__)
#if defined(__arch64__) || defined(_LP64)
typedef long int int64_t;
typedef unsigned long int uint64_t;
#else
typedef long long int int64_t;
typedef unsigned long long int uint64_t;
#endif /* __arch64__ */
#endif /* __STDC__ */
#elif defined( __VMS ) || defined(__sgi)
#include <inttypes.h>
#elif defined(__SCO__) || defined(__USLC__)
#include <stdint.h>
#elif defined(__UNIXOS2__) || defined(__SOL64__)
typedef long int int32_t;
typedef long long int int64_t;
typedef unsigned long long int uint64_t;
#elif defined(_WIN32) && defined(__GNUC__)
#include <stdint.h>
#elif defined(_WIN32)
typedef __int32 int32_t;
typedef __int64 int64_t;
typedef unsigned __int64 uint64_t;
#else
/* Fallback if nothing above works */
#include <inttypes.h>
#endif
#endif

typedef int64_t GLint64EXT;
typedef uint64_t GLuint64EXT;

typedef int64_t GLint64;
typedef uint64_t GLuint64;
typedef struct __GLsync *GLsync;

/* These incomplete types let us declare types compatible with OpenCL's cl_context and cl_event */
struct _cl_context;
struct _cl_event;

typedef void (APIENTRY *GLDEBUGPROCARB)(GLenum source,GLenum type,GLuint id,GLenum severity,GLsizei length,const GLchar *message,GLvoid *userParam);

typedef void (APIENTRY *GLDEBUGPROCAMD)(GLuint id,GLenum category,GLenum severity,GLsizei length,const GLchar *message,GLvoid *userParam);

typedef void (APIENTRY *GLDEBUGPROC)(GLenum source,GLenum type,GLuint id,GLenum severity,GLsizei length,const GLchar *message,GLvoid *userParam);

typedef GLintptr GLvdpauSurfaceNV;

#ifdef _WIN32 /* WGL types */

DECLARE_HANDLE(HPBUFFERARB);
DECLARE_HANDLE(HPBUFFEREXT);
DECLARE_HANDLE(HVIDEOOUTPUTDEVICENV);
DECLARE_HANDLE(HPVIDEODEV);
DECLARE_HANDLE(HPGPUNV);
DECLARE_HANDLE(HGPUNV);

typedef struct _GPU_DEVICE {
    DWORD  cb;
    CHAR   DeviceName[32];
    CHAR   DeviceString[128];
    DWORD  Flags;
    RECT   rcVirtualScreen;
} GPU_DEVICE, *PGPU_DEVICE;

DECLARE_HANDLE(HVIDEOINPUTDEVICENV);

#endif /* #ifdef _WIN32 */

/* create declarations */

#ifdef __cplusplus
extern "C" {
#endif

int glLoaderInit();

#define GL_EXT(name) GLAPI int GLLOADER_SUPPORTS_NAME(name);
#define GL_PROC(cat, rtype, name, params) GLAPI rtype (APIENTRY *name)params;
#include GLLOADER_THIS_FILE
#undef GL_EXT
#undef GL_PROC

#ifdef __cplusplus
} /* extern "C" */
#endif

#undef GLLOADER_DECLARE_ENUMS

/* end header file **********************************************************/

#ifndef GLLOADER_HEADER_ONLY

/* create definitions */

#define GLLOADER_DECLARE_ENUMS 0

#define GL_EXT(name) int GLLOADER_SUPPORTS_NAME(name);
#define GL_PROC(cat, rtype, name, params) rtype (APIENTRY *name)params;
#include GLLOADER_THIS_FILE
#undef GL_EXT
#undef GL_PROC

/* function loading */

static HMODULE libgl;

static void* glLoaderGetProc(const char *name)
{
  void *result = wglGetProcAddress(name);
  if (result == NULL)
		result = GetProcAddress(libgl, name);
	return result;
}

static int glLoaderFindGLExt(const char *name)
{
  const GLubyte * (APIENTRY *glGetString)(GLenum name) = glLoaderGetProc("glGetString");
  const char *extensions;
  const char *current;
  size_t name_length;

  if (strstr(name, "GL_VERSION_") == name)
    return 1;

  if (glGetString == NULL)
    return 0;

  name_length = strlen(name);

  extensions = (const char*)glGetString(GL_EXTENSIONS);
  current = extensions;
  while (current)
  {
    current = strstr(current, name);
    if (current)
    {
      char supposed_end_char;

      current += name_length;

      supposed_end_char = *current;
      if (supposed_end_char == 0 || supposed_end_char == ' ')
        return 1;
    }
  }

  return 0;
}

#ifdef _WIN32

static int glLoaderFindWGLExt(const char *name)
{
  const char * (APIENTRY *wglGetExtensionsStringARB)(HDC hdc) = glLoaderGetProc("wglGetExtensionsStringARB");
  const char *extensions;
  const char *current;
  size_t name_length;

  if (wglGetExtensionsStringARB == NULL)
    return 0;

  name_length = strlen(name);

  extensions = wglGetExtensionsStringARB( wglGetCurrentDC() );
  current = extensions;
  while (current)
  {
    current = strstr(current, name);
    if (current)
    {
      char supposed_end_char;

      current += name_length;

      supposed_end_char = *current;
      if (supposed_end_char == 0 || supposed_end_char == ' ')
        return 1;
    }
  }

  return 0;
}

#endif

static int glLoaderFindExt(const char *name)
{
  if (strstr(name, "GL_") == name)
    return glLoaderFindGLExt(name);

#ifdef _WIN32

  if (strstr(name, "WGL_") == name)
    return glLoaderFindWGLExt(name);

#endif

  return 0;
}

int glLoaderInit()
{
	libgl = LoadLibraryA("opengl32.dll");

#define GL_EXT(name) GLLOADER_SUPPORTS_NAME(name) = glLoaderFindExt(#name);
#define GL_PROC(cat, rtype, name, params) name = (rtype (APIENTRY *)params)glLoaderGetProc(#name); GLLOADER_SUPPORTS_NAME(cat) = GLLOADER_SUPPORTS_NAME(cat) && (name != NULL);
#include GLLOADER_THIS_FILE
#undef GL_EXT
#undef GL_PROC

  FreeLibrary(libgl);

  return GLLOADER_SUPPORTS_NAME(GL_VERSION_1_1);
}

#undef GLLOADER_THIS_FILE

#endif /* #ifndef GLLOADER_HEADER_ONLY */

#else /* #ifdef GLLOADER_THIS_FILE_IS_INCLUDED */

/* generated declarations */

#if (GLLOADER_DECLARE_EXTS == 1)

%(GL_categories)s

#ifdef _WIN32

%(WGL_categories)s

#endif /* #ifdef _WIN32 */

#endif /* #if (GLLOADER_DECLARE_EXTS == 1) */

#if (GLLOADER_DECLARE_ENUMS == 1)

%(GL_enums)s

#ifdef _WIN32

%(WGL_enums)s

#endif /* #ifdef _WIN32 */

#endif /*#if (GLLOADER_DECLARE_ENUMS == 1)*/

#if (GLLOADER_DECLARE_COMMANDS == 1)

%(GL_commands)s

#ifdef _WIN32

%(WGL_commands)s

#endif /* #ifdef _WIN32 */

#endif /* #if (GLLOADER_DECLARE_COMMANDS == 1) */

#endif /* #ifdef GLLOADER_THIS_FILE_IS_INCLUDED */

import os

#-----------------------------------------------------------------------------

def formatIdentifier(glid, namespace):
  name = glid
  if not name.upper().startswith("WGL"):
    name = "%s_%s" % (namespace.upper(), name)
  return name

def formatTypeName(typemap, typename):
  assert typename is not None
  return typemap.get(typename, typename)


def formatCommandArguments(typemap, cmd):
  argument_string = ""
  arg_count = 0
  for argument in cmd.arguments:
    if (arg_count > 0):
      argument_string += ", "
    type_string = formatTypeName(typemap, argument.type)
    if (not argument.is_value() and argument.is_in()):
      type_string = "const " + type_string
    if (not argument.is_value()):
      type_string += " *" 
    argument_string += "%s %s" % (type_string, argument.name)
    arg_count += 1
  return argument_string


def formatCommand(category_name, spec, typemap, cmd):
  
  if cmd.is_reuse_from_extension():
    return None
  return "GL_PROC(%s, %s, %s%s, (%s))" % (category_name, formatTypeName(typemap, cmd.returnType), cmd.namespace, cmd.name, formatCommandArguments(typemap, cmd))


def formatEnum(spec, enum):
  
  name = formatIdentifier(enum.enum_id, enum.namespace)
  
  if enum.is_reference():
    return None # "/*  %s (from '%s') */" % (name, enum.reference_category_id)
  
  # this is a (name, value) enum, value can be an alias to another value
  value_comment = ""
  
  # resolve alias
  value, value_alias = spec.resolve_enum_value(enum)
  if value_alias is not None:
    value_comment = " /* %s */" % value_alias
  
  # write actual value  
  return "#define %s %s%s" % (name, value, value_comment)


def outputKey(category, basekey):
  return "%s_%s" % (category.namespace.upper(), basekey)

def formatGL(spec, typemap):

  result = dict()

  def categoryName(cat):
    return "%s_%s" % (cat.namespace.upper(), cat.id)

  def section(cat):
    name = categoryName(cat)
    if name.startswith("VERSION_"):
      # core GL comes first as we'll need its functions to look for extensions
      return 0
    elif name.upper().startswith("WGL"):
      return 2
    else:
      return 1
  
  def sort_categories(a, b):
    sa = section(a)
    sb = section(b)
    if sa == sb:
      return cmp(a.id, b.id)
    else:
      return cmp(sa, sb)

  categories = spec.categories.values()
  categories = sorted(categories, cmp=sort_categories)
  
  for category in categories:
    
    if category.id == "wgl":
      # core wgl is provided by windows since Windows 2000, suppose it is provided
      continue
    
    output = result.setdefault( outputKey(category, "categories"), [] )
    
    name = formatIdentifier(category.id, category.namespace)
    output.append( "GL_EXT(%s)" % name )
    
  for category in categories:
    
    if category.id == "wgl":
      # core wgl is provided by windows since Windows 2000, suppose it is provided
      continue
    
    output = result.setdefault( outputKey(category, "enums"), [] )
    
    output.append("/* %s */" % category.id)

    enums = category.enums
    for enu in enums:
      enustr = formatEnum(spec, enu)
      if enustr is not None:
        output.append( "%s" % enustr )

  for category in categories:
    
    if category.id == "wgl":
      # core wgl is provided by windows since Windows 2000, suppose it is provided
      continue
    
    # in a given category (extension), there may be GL_ commands _and_ WGL_ commands.
    
    category_name = formatIdentifier(category.id, category.namespace)
    
    commands = category.commands
    for cmd in commands:
      
      cmdstr = formatCommand(category_name, spec, typemap, cmd)
      
      if cmdstr is not None:
        output = result.setdefault( outputKey(cmd, "commands"), [] )
        output.append( "%s" % cmdstr )

  for key in result:
    result[key] = "\n".join(result[key])

  return result

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
if __name__ == "__main__":

  from glparser.spec import Specification
  from glparser import parse_gl
  from glparser.enum_spec import SpecParserCallback

  specification = Specification()

  callback = SpecParserCallback(specification)

  # parse the enumext spec, which defines all OpenGL (core and extensions)
  # parse the additional enumext_unofficial spec, which defines ghosts extensions
  
  parse_gl(specification, "gl", ["registry/gl.spec"], ["registry/enumext.spec", "enumext_unofficial.spec"], callback)
  parse_gl(specification, "wgl", ["registry/wgl.spec", "registry/wglext.spec"], ["registry/wglenumext.spec"], callback)

  import glparser.typemap
  typemap = glparser.typemap.parse_typemap( file("registry/gl.tm", "r") )
  typemap = glparser.typemap.parse_typemap( file("registry/wgl.tm", "r"), typemap=typemap )

  #

  with file("template.c", "r") as template:
    templatestr = template.read()
    
  formattedGL = formatGL(specification, typemap)

  templatestr = templatestr % formattedGL
  
  out_folder = "glloader"
  out_filename = "glloader.c"
  
  if not os.path.isdir(out_folder):
    os.makedirs(out_folder)
    
  output_path = os.path.join(out_folder, out_filename)

  with file(output_path, "w") as output: 
    output.write(templatestr)

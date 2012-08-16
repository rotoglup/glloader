"""
Parse 'enum*.spec' file
Generates information related to OpenGL enumeration values
"""
import glparser.config
import glparser.helpers

from glparser.spec import Enum

#---------------------------------------------------------------------------

def __parse_enum_section(line):
  m = glparser.helpers.RE_ENUM_SECTION.match(line)
  if m == None:
    raise RuntimeError("Unsupported file format in line '%s'" % line)
  name = m.group(1)
  if name.startswith("WGL_"):
    # strip the leading WGL_ to be homogenous with GL_ that is not set
    name = name[4:]
  return name

#---------------------------------------------------------------------------

def __parse_enum_value(line):
  result = Enum()
  match_value = glparser.helpers.RE_ENUM_VALUE.match(line)
  if match_value:
    result.set_declaration(match_value.group(1), match_value.group(2))
  else:
    match_use = glparser.helpers.RE_ENUM_USE_VALUE.match(line)
    if match_use:
      extension = match_use.group(1)
      enum_id = match_use.group(2)
      result.set_reference(extension, enum_id)
    else:
      raise RuntimeError("Unsupported file format in line '%s'" % line)
  return result

#---------------------------------------------------------------------------

class IParserCallback:
  
  def begin_category(self, category_id, namespace):
    pass
  
  def use_enum(self, enum):
    pass

  def define_enum(self, enum):
    pass

#---------------------------------------------------------------------------

class SpecParserCallback(IParserCallback):
  
  def __init__(self, specification, ignore_names=None):
    
    self.global_values = dict()
    self.local_values = dict()

    self.ignore_names = dict() if ignore_names is None else ignore_names
    
    self.specification = specification
    self._current_category = None
    
  #
  
  def begin_category(self, category, namespace):
    
    self._current_category = None
    
    if category in glparser.config.IGNORE_EXTENSIONS:
      return False
    
    category_id = category
    category_description = category
    
    category = self.specification.add_category( category_id, namespace )
    category.description = category_description
    
    self._current_category = category    
    
    return True
    
  def use_enum(self, enum):
    
    if self._current_category == None:
      raise RuntimeError("ERROR: incoherent specification file, trying to use an enum outside a category")
    
    assert enum.is_reference()
    
    skip_name = (enum.enum_id in self.ignore_names)
    if not skip_name:
      self._current_category.add_enum(enum)

  def define_enum(self, enum):
    
    if self._current_category == None:
      raise RuntimeError("ERROR: incoherent specification file, trying to define an enum outside a category")
    
    assert not enum.is_reference()
    
    enum_id = enum.enum_id
    
    skip_name = (enum_id in self.ignore_names)
    if not skip_name:
      
      previous_definition = self.global_values.get(enum_id, None)
      stored_enum = enum
      
      if previous_definition is None:
        self.global_values[ enum_id ] = enum
        self.local_values[ enum_id ] = enum
      else:
        if previous_definition.value != enum.value:
          raise RuntimeError("ERROR: incoherent specification file, multiple values for '%s': %s & %s" % (enum_id, previous_definition.value, enum.value))
        stored_enum = Enum()
        stored_enum.namespace = enum.namespace
        stored_enum.set_reference(previous_definition.category_id, enum_id)
      
      self._current_category.add_enum(stored_enum)
      
#---------------------------------------------------------------------------

def parse_enum_spec(f, namespace, callback):
  
  with glparser.helpers.spec_read_lines(f) as line_consumer:
  
    current_section = line_consumer.__iter__().next()
    
    while (current_section.startswith("passthru:")):
      current_section = line_consumer.__iter__().next()
  
    # skip first section (for 'enum.spec') (could be cleaner)
    
    if (current_section == "Extensions define:"):
    
      current_section = None
      
      for line in line_consumer:
        if glparser.helpers.RE_SECTION.match(line) != None:
          current_section = line
          break
      
      if current_section == None:
        raise RuntimeError("Unexpected end of file")
    
    # parse following sections (enums grouped by function)
    
    current_section = __parse_enum_section(current_section)
    consider_section = callback.begin_category( current_section, namespace )
    
    for line in line_consumer:
      if (line.startswith("passthru:")):
        continue
      if (line.startswith("ARB_future_use:")):
        continue
      if (glparser.helpers.RE_SECTION.match(line)):
        current_section = __parse_enum_section(line)
        consider_section = callback.begin_category( current_section, namespace )
      else:
        if consider_section:
          enum_entry = __parse_enum_value(line)
          enum_entry.namespace = namespace
          if enum_entry.is_reference():
            callback.use_enum( enum_entry )
          else:
            callback.define_enum( enum_entry )

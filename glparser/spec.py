#---------------------------------------------------------------------------

class Specification:
  
  def __init__(self):
    
    self.categories = dict()
    self.ordered_categories = []
    self._all_enums = dict()
    self._all_enum_refs = dict()
    
  def add_category(self, category_id, namespace):
    
    category = self.categories.get(category_id, None)
    if category is None:
      category = Category(category_id, namespace)
      category._specification = self
      self.categories[category_id] = category
      self.ordered_categories.append( category_id )
    return category
    
  def _add_enum(self, enum):
    
    if enum.is_reference():
      self._all_enum_refs.setdefault(enum.enum_id, []).append(enum)
    else:
      if enum.enum_id in self._all_enums:
        raise RuntimeError("Incoherent specification: multiple values defined for '%s' (new value is '%s')" % (enum.enum_id, str(enum.value)))
      self._all_enums[enum.enum_id] = enum
    
  
  def resolve_enum_value(self, enum):
    
    # this is a (name, value) enum, value can be an alias to another value
    name, value = (enum.enum_id, enum.value)
    value_alias = None
    
    # resolve alias
    while (value.startswith("GL_")):
      if value_alias is None:
        value_alias = value
      value = value[3:] # strip GL_
      aliased_enum = self._all_enums.get(value, None)
      if aliased_enum is None:
        raise RuntimeError("ERROR: incoherent specification file, '%s' is an alias to an undefined value '%s'" % (name, value))
      value = aliased_enum.value
      
    return value, value_alias
  
  
#---------------------------------------------------------------------------

class Category:
  """
  A Category is a kind of namespace. Categories are either versions of OpenGL or extensions.
  """
  def __init__(self, category_id, namespace):
    
    self.id = category_id
    self.namespace = namespace
    self.description = None
    self.enums = []
    self.commands = []
    
    self._specification = None
    
  def add_enum(self, enum):
    
    enum.category_id = self.id
    self.enums.append(enum)
    
    self._specification._add_enum(enum)
    
  def add_command(self, command):
    
    self.commands.append(command)

#---------------------------------------------------------------------------

class Enum:
  
  def __init__(self):
    self.enum_id = None
    self.value = None
    self.reference_category_id = None
    self.category_id = None
    self.namespace = None
  
  def set_declaration(self, enum_id, value):
    self.enum_id = enum_id
    self.value = value
    
  def set_reference(self, category_id, enum_id):
    self.reference_category_id = category_id
    self.enum_id = enum_id
    
  def is_reference(self):
    return self.value is None

#---------------------------------------------------------------------------

class Command:
  
  def __init__(self):
    
    self.returnType = None
    self.name = None
    self.arguments = []
    self.category_id = None
    self.version = None
    self.reuse_from = None
    self.namespace = None
    
  def is_reuse_from_extension(self):
    return self.reuse_from is not None
    
  def set_reuse_from(self, category_id):
    self.reuse_from = category_id

  def add_argument(self, argument):
    self.arguments.append(argument)
      
#---------------------------------------------------------------------------

class Argument:
  
  INOUT_TYPE_IN = 0
  INOUT_TYPE_OUT = 1
  
  def __init__(self):
    self.type = None
    self.name = None
    self.inout = None
    self.sequence = None
    self.moreinfo = None

  def is_in(self):
    return self.inout == Argument.INOUT_TYPE_IN

  def is_out(self):
    return self.inout == Argument.INOUT_TYPE_OUT
  
  def is_value(self):
    return self.sequence == "value" 

  def is_array(self):
    return self.sequence == "array" 

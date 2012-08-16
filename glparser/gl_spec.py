"""
Corner cases, spec revision 10796

* GL3+ 'silently' references ARB extensions promoted to core in 'passthru' statements, for example :
passthru: /* OpenGL 3.2 also reuses entry points from these extensions: */
passthru: /* ARB_draw_elements_base_vertex */
passthru: /* ARB_provoking_vertex */
passthru: /* ARB_sync */
passthru: /* ARB_texture_multisample */

* TODO GL3.2 has a comment defining a command:
# FramebufferTextureLayer already declared in ARB_framebuffer_object
# FramebufferTextureLayer(target, attachment, texture, level, layer)
"""

import re

from glparser.config import IGNORE_EXTENSIONS
from glparser.helpers import RE_EMPTY, spec_read_lines

from glparser.spec import Command, Argument

#---------------------------------------------------------------------------

RE_PROPERTY_LINE = re.compile("^[^\:\#]+\:")
RE_COMMAND = re.compile("^(\w+)\((.*?)\)")
RE_COMMAND_PROPERTY = re.compile("^\t(\w+)\s*(.*?)\s*(?:\#.*)?$")

RE_COMMAND_REUSE = re.compile("^passthru\:\s*\/\*\s*OpenGL\s+(\d+)\.(\d+)\s+also reuses entry points from these extensions.*")
RE_COMMAND_REUSE_EXTENSION = re.compile("^passthru\:\s*\/\*\s*([\w]+).*")

RE_SINGLE_COMMAND_REUSE = re.compile("^\#\s*(\w+)\s+already declared in\s+(\w+)")

RE_PROP_PARAM_VALUE = re.compile("([^\s]+)\s+(.*?)$")
RE_PROP_PARAM_VALUE_TYPE = re.compile("^([^\s]+)\s([^\s]+)\s([^\s]+)(?:\s(.*?))?\s*$")

PARAM_MODIFIER_TYPES = { "in": Argument.INOUT_TYPE_IN, "out": Argument.INOUT_TYPE_OUT }

#---------------------------------------------------------------------------

class ParserCallback:
  
  def __init__(self, namespace, specification):
    self.currentCommand = None
    self.namespace = namespace
    self.spec = specification
    
  #
  
  def property_line(self, line, line_consumer):
    
    match = RE_COMMAND_REUSE.match(line) 
    if match is not None:
      gl_version = (match.group(1), match.group(2))
      line_consumer.allow_comments_and_empty(True)
      for line in line_consumer:
        if RE_EMPTY.match(line):
          break
        match = RE_COMMAND_REUSE_EXTENSION.match(line)
        if match is None:
          raise RuntimeError("Unable to parse specification: reused extensions could not be found")
        category_id = match.group(1)
        self.__emit_command()
        self.currentCommand = Command()
        self.currentCommand.set_reuse_from(category_id)
        self.currentCommand.category_id = "VERSION_%s_%s" % gl_version
        self.__emit_command()
      line_consumer.allow_comments_and_empty(False)
      return
      
  def command_line(self, line):
    self.__emit_command()
    self.currentCommand = Command()
    match = RE_COMMAND.match(line)
    self.currentCommand.name = match.group(1)
  
  def command_property_line(self, line):
    match = RE_COMMAND_PROPERTY.match(line)
    property_name = match.group(1)
    
    if (property_name == "return"):
      self.currentCommand.returnType = match.group(2)
    
    elif (property_name == "param"):
      param_value_string = match.group(2)
      param_value_match = RE_PROP_PARAM_VALUE.match(param_value_string)
      param_name = param_value_match.group(1)
      param_type_string = param_value_match.group(2)
      param_type_match = RE_PROP_PARAM_VALUE_TYPE.match(param_type_string)
      if param_type_match == None:
        raise RuntimeError("Unable to parse 'param' type in '%s' (type string = '%s')" % (line, param_type_string))
      param_basetype = param_type_match.group(1)
      param_inout = param_type_match.group(2)
      param_sequence = param_type_match.group(3)
      param_moreinfo = param_type_match.group(4)
      self.__emit_parameter( param_name, param_basetype, param_inout, param_sequence, param_moreinfo )
      
    elif (property_name == "category"):
      category_id = match.group(2)
      category_id = self.__category_id(category_id)
      self.currentCommand.category_id = category_id
      
    elif (property_name == "version"):
      version = match.group(2)
      self.currentCommand.version = version
      
  #
  
  def __emit_command(self):
    if self.currentCommand != None:
      self.currentCommand.namespace = self.namespace
      category_id = self.currentCommand.category_id
      if category_id is None:
        category_id = self.__category_id("wgl")   # workaround problem in wgl spec
        self.currentCommand.category_id = category_id
      consider_command = not category_id in IGNORE_EXTENSIONS
      if consider_command:
        category = self.spec.add_category( category_id, self.namespace )
        category.add_command(self.currentCommand)
    self.currentCommand = None
    
  def __category_id(self, category_id):
    # OpenGL v1.0 does not exist in enums, remove it also from functions
    if (category_id.startswith("VERSION_1_0")): category_id = category_id.replace("VERSION_1_0", "VERSION_1_1")
    ## old 'hack' when categories were not consistent for opengl 1.0
    #is_core_1_1_category = (-1 == category_id.find("_"))
    #return category_id if (not is_core_1_1_category) else "VERSION_1_1"
    return category_id
    
  def __emit_parameter(self, param_name, param_basetype, param_inout, param_sequence, param_moreinfo):
    
    argument = Argument()
    
    if not param_inout in PARAM_MODIFIER_TYPES:
      raise RuntimeError("Unsupported parameter type modifier '%s'" % param_inout)
    else:
      param_inout = PARAM_MODIFIER_TYPES[param_inout]
    
    argument.type = param_basetype
    argument.name = param_name
    argument.inout = param_inout
    argument.sequence = param_sequence
    argument.moreinfo = param_moreinfo
    
    self.currentCommand.add_argument(argument)
    
#---------------------------------------------------------------------------

def parse_commands(f, namespace, specification):
  
  callback = ParserCallback(namespace, specification)
  with spec_read_lines(f) as line_consumer:
  
    for line in line_consumer:
      
      if (RE_PROPERTY_LINE.match(line) != None):
        callback.property_line(line, line_consumer)
      
      elif (RE_COMMAND.match(line) != None):
        callback.command_line(line)
      
      elif (RE_COMMAND_PROPERTY.match(line) != None):
        callback.command_property_line(line)
      
      elif line.startswith("#"):
        # HACK, corner case
        callback.property_line(line, line_consumer)
      
      else:
        raise RuntimeError("Unsupported line format in '%s'" % line)


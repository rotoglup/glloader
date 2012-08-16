import glparser.gl_spec
import glparser.enum_spec

#-----------------------------------------------------------------------------

def parse_gl(specification, namespace, cmd_spec_filenames, enum_spec_filenames, callback):

  # parse enums

  for filename in enum_spec_filenames:
    
    with file(filename, "r") as f:
      glparser.enum_spec.parse_enum_spec( f, namespace, callback )

  # parse commands

  for filename in cmd_spec_filenames:
    
    with file(filename, "r") as f: 
      glparser.gl_spec.parse_commands( f, namespace, specification )
  

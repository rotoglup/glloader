"""
Parse 'gl.tm' type map file, allowing to define OpenGL data types
"""

import re

from glparser.helpers import spec_read_lines

#---------------------------------------------------------------------------

RE_TYPE_DEFINITION = re.compile("^(\w+)\,\*\,\*\,\s*([^\,]+)\,\*\,\*")

#---------------------------------------------------------------------------

def parse_typemap(f, typemap=None):
  
  with spec_read_lines(f) as line_consumer:
  
    result = dict() if typemap is None else typemap
  
    for line in line_consumer:
      match = RE_TYPE_DEFINITION.match(line)
      if (match == None):
        raise RuntimeError("Unsupported line format for '%s'" % line)
      spec_type = match.group(1)
      impl_type = match.group(2)
      if impl_type != "*":
        result[spec_type] = impl_type
      
    return result

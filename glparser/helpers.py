import contextlib
import re

#---------------------------------------------------------------------------

RE_COMMENT = re.compile("^(\#|\@)")

RE_EMPTY   = re.compile("^\s*$")
RE_SECTION = re.compile("^[^\s]")

RE_ENUM_SECTION = re.compile("^(.+?)(\senum)?\:")

RE_ENUM_VALUE = re.compile("^\s+([^\s]+)\s+\=\s+([^\s,]+)")
RE_ENUM_USE_VALUE = re.compile("^\s+use\s+([^\s]+)\s+([^\s]+)")

# TODO see if core special case is still useful for glparser.enum_spec
#---------------------------------------------------------------------------

@contextlib.contextmanager
def spec_read_lines(f):
  """
  Generator yielding content lines of the given file object (removes comments and empty lines)
  """
  
  done = False
  
  class LineCounter:
    def __init__(self):
      self.linenum = -1
  
  class Reader:
    def __init__(self, lineCounter):
      self.lineCounter = lineCounter
      self._allow_comments_and_empty = False
      self._lines = f.readlines()
    
    def allow_comments_and_empty(self, value):
      self._allow_comments_and_empty = value
    
    def __iter__(self):
      """
      Designed to be reentrant
      """
      while self._lines != []:

        lineCounter.linenum += 1
        
        line = self._lines[0]
        del self._lines[0]

        valid = True
        if not self._allow_comments_and_empty:
          valid = (RE_COMMENT.match(line) == None and RE_EMPTY.match(line) == None)
        if valid:
          yield line.rstrip()
  
  lineCounter = LineCounter()
  
  try:
    yield Reader(lineCounter)
    done = True
  
  finally:
    if not done:
      print "An error occured while parsing line %d" % (lineCounter.linenum+1)
    

#---------------------------------------------------------------------------

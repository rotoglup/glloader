import os
import urllib

# official spec files from Khronos, they have problems/bugs such as missing functions
#baseurl = "http://www.opengl.org/registry/api/"

# unofficial spec files maintained independently
baseurl = "https://bitbucket.org/alfonse/gl-xml-specs/raw/default/glspecs/"

files = ['gl.spec', 'gl.tm', 'enum.spec', 'enumext.spec']
files += ['wglenum.spec', 'wglenumext.spec', 'wgl.spec', 'wglext.spec', 'wgl.tm']

outdir = "registry"
if not os.path.isdir(outdir):
  os.makedirs(outdir)

for f in files:
  
  source_url = baseurl + f
  destination_path = os.path.join(outdir, f)
  
  print "downloading from '%s'" % source_url
  mysock = urllib.urlopen(source_url)
  fileToSave = mysock.read()
  
  print "writing '%s'" % destination_path
  oFile = open(destination_path, 'wb')
  oFile.write(fileToSave)
  oFile.close

print "done."

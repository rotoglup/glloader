> OpenGL *spec* files are now obsolete, replaced by `xml files <https://github.com/KhronosGroup/OpenGL-Registry>`_ for some time

**glloader** is a generated code snippet that allows to load OpenGL and extensions with a single file, see ``glloader\glloader.c``.

The ``glparser`` folder contains python code used to parse the gl *spec* files, while ``build_glloader.py`` contains the backend that generates ``glloader.c``.

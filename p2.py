import numpy
from stl import mesh
import stl

# Using an existing stl file:
your_mesh = mesh.Mesh.from_file('cilindro3.stl')


puntos = your_mesh.vectors

for x in puntos:
    for elemento in x:
        if elemento[2] != 0:
            elemento[2] = 0





your_mesh.save('cilindro3.stl', mode =stl.Mode.ASCII)

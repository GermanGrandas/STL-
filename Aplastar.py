import numpy
from stl import mesh
import stl

# Using an existing stl file:
Datos = mesh.Mesh.from_file('p1.stl')
lista = []

puntos = Datos.vectors
vec2 = Datos.v2
for x in puntos:
    cont = 0
    for elemento in x:
        if elemento[2] <= 0:
            cont+=1
    if cont == 3:
        lista.append(x)

l = mesh.Mesh(numpy.zeros(len(lista),  dtype = mesh.Mesh.dtype))
for y,p in enumerate(lista):
    l.vectors[y] = lista[y]
    l.vectors[y][0][2] = 0
    l.vectors[y][1][2] = 0
    l.vectors[y][2][2] = 0
#Formula de minima distancia


l.save('p2.stl', mode =stl.Mode.ASCII)

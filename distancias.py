# aqui ingresamos coordenadas
x1 = int(input("Ingresa x1: "))
y1 = int(input("Ingresa y1: "))
x2 = int(input("Ingresa x2: "))
y2 = int(input("Ingresa y2: "))

# estas son las operaciones para la distancia Euclidiana
from math import sqrt
dx=x2-x1
dy=y2-y1
de = sqrt(((dx)**2)+((dy)**2))

# estas son las operaciones para la distancia Manhattan
dx=x2-x1
dy=y2-y1
dm = dx+dy

print("Distancia Euclidiana:", de)
print("Distancia Manhattan:", dm)

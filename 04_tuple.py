#Las tuplas no se pueden modificar
my_tuple = ()

print(type(my_tuple))

# función que asigna los valores de la tupla
def coordenadas():
    return (5, 4)

coordenada = coordenadas()
print(coordenada)

# desempaquetar una tupla
x, y = coordenadas()
print(x)
print(y)

my_list = [1, 2, 3]
print(my_list)

my_list.append(4) # agrega un valor al final de la lista
print(my_list)

my_list[0] = 0
print(my_list) # asigna un nuevo valor a la posición 0

my_list.pop() # borra el último elemento de la lista
print(my_list)

for elem in my_list: # itera una lista
    print(elem)


lista_a = [1, 2, 3]
lista_b = lista_a # asigna otro alias a la misma lista
# si modificamos lista_a también se modifica lista_b (y biceversa) porque son la misma lista
print(id(lista_a))
print(id(lista_b))

lista_c = [lista_a, lista_b]
print(lista_c)

lista_a.append(4)
print(lista_a)
print(lista_b)
print(lista_c) # también se modifica lista_c

# Clonar una lista
a = [2,4,6]
print(a)
print(id(a))

b = a
print(id(b))

c = list(a) # crea una lista nueva (c) con el mismo contenido de a
print(id(a))
print(id(c)) # son dos listas distintas

my_list = list(range(100))
print(my_list)

doble = [i + 2 for i in my_list] # genera una lista con los valores de my_list multiplicados por 2
print(doble)

pares = [i for i in my_list if i % 2 == 0] # genera una lista con los números pares de my_list
print(pares)






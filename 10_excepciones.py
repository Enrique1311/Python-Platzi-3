def divide_elem_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as error:
        print(error)
        return lista

lista = list(range(10))
divisor = 0

print(divide_elem_de_lista(lista, divisor))

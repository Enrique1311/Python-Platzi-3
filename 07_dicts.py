my_dict = {
    'Santiago': 6,
    'Martina': 14,
    'Carolina': 42
}
print(my_dict["Santiago"])

print(my_dict.get('Mart', 'Nombre inexistente')) # Si la llave que solicitamos no existe, imprime el otro valor

my_dict['Carolina'] = 40 # reasigna un valor
print(my_dict)

my_dict['Enrique'] = 46 # agrega una nueva llave al dict
print(my_dict)

del my_dict["Enrique"] # borra una llave
print(my_dict)

for key in my_dict.keys(): # itera e imprime las llaves
    print(key) 

for key in my_dict.keys(): # itera e imprime las llaves con sus valores
    print(key, my_dict[key]) 

for value in my_dict.values(): # itera e imprime los valores
    print(value) 

for key, value in my_dict.items(): # itera e imprime llaves y valores
    print(key, value)

print('Martina' in my_dict) # devuelve True or False dependiendo de si está o no la llave

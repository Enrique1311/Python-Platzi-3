# # ¿Quién es mayor?
# nombre1  = input('Ingresa el nombre de la primera persona: ')
# edad1 = int(input(f'Ingresa la edad de {nombre1}: '))

# nombre2  = input('Ingresa el nombre de la primera persona: ')
# edad2 = int(input(f'Ingresa la edad de {nombre2}: '))

# if edad1 > edad2:
#     print(f'{nombre1} tiene {edad1} años y es mayor que {nombre2} que tiene {edad2} años.')
# elif edad1 < edad2:
#     print(f'{nombre2} tiene {edad2} años y es mayor que {nombre1} que tiene {edad1} años.')
# else:
#     print(f'{nombre1} y {nombre2} tienen la misma edad.')

# # Averiguar si un número tiene raíz cuadrada
# number = int(input('Ingresa un número: '))
# resp = 0
# while resp**2 < number:
#     resp += 1

# if resp**2 == number:
#     print(f'La raíz cuadrada de {number} es {resp}')
# else:
#     print(f'{number} no tiene como raíz cuadrada a un número entero')

# # Raíz cuadrada aproximada
# number = int(input('Ingresa un número: '))
# epsilon = 0.01
# step = epsilon**2
# resp = 0.0

# # El método "abs" devuelve el valor absoluto de un cálculo
# while abs(resp**2 - number) >= epsilon and resp <= number:
#     resp += step
 
# if abs(resp**2 - number) >= epsilon:
#     print(f'No se encontró la raíz cuadrada de {number}.')
# else:
#     print(f'La raíz cuadrada de {number} es {resp}.')

# Búsqueda binaria
number = int(input('Ingresa un número: '))
epsilon = 0.01 # margen de error
bajo = 0 # valor minimo para calcular largo del conjunto
alto = max(1.0, number) # valor maximo para calcular largo de conjunto. Función max() >> elegirá el valor máximo de los parámetros que le demos; colocamos 1.0 como valor mínimo aceptado (así nos cubrimos de que, por ejemplo, el usuario coloque un valor negativo), y objetivo (valor que nos dará el usuario)
resp = (alto + bajo) / 2

while abs(resp**2 - number) >= epsilon:
    if resp**2 < number:
        bajo = resp
    else:
        alto = resp

    resp = (alto + bajo) / 2

print(f'La raíz cuadrada de {number} es {resp}')


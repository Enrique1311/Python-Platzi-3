# Averiguar si un número tiene raíz cuadrada
def raizCuadradaClasica(number):
    resp = 0
    while resp**2 < number:
        resp += 1

    if resp**2 == number:
        print(f'La raíz cuadrada de {number} es {resp}')
    else:
        print(f'{number} no tiene como raíz cuadrada a un número entero')
def raizCuadradaAprox(number):
    epsilon = 0.01
    step = epsilon**2
    resp = 0.0

    while abs(resp**2 - number) >= epsilon and resp <= number: # El método "abs" devuelve el valor absoluto de un cálculo
        resp += step
    
    if abs(resp**2 - number) >= epsilon:
        print(f'No se encontró la raíz cuadrada de {number}.')
    else:
        print(f'La raíz cuadrada de {number} es {resp}.')
    return resp


# Búsqueda binaria
def raizCuadradaBinaria(number):
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
    return resp
        
number = int(input('Ingresa un número para calcular su raíz cuadrada: '))
print('1 - Raíz cuadrada tradicional')
print('2 - Raíz cuadrada por aproximación')
print('3 - Raíz cuadrada binaria')
option = input('Elige el método para buscar la raíz cuadrada de un número: ')

if option == "1":
    raizCuadradaClasica(number)
elif option == "2":
    raizCuadradaAprox(number)
elif option == "3":
    raizCuadradaBinaria(number)
else:
    print('¡Opción incorrecta!')


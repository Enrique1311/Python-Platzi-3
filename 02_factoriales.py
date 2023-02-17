def factorial(n):
    # calcula el factorial de n
    if n == 1:
        return 1

    return n * factorial(n - 1)

n = int(input('Ingresa un número entero: '))
print(f'El factorial de {n} es {factorial(n)}')
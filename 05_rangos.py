# range(comienzo, fin, pasos)
my_range = range(1, 5)
print(type(my_range))

for i in my_range:
    print(i)

my_range_2 = range(0, 7, 2)
my_range_3 = range(0, 8, 2)

for i in my_range_2:
    print(i)

for i in my_range_3:
    print(i)

print(f'Generan el mismo resultado?: {my_range_2 == my_range_3}') # ambos rangos generan el mismo resultado

print(f'Son los mismos rangos?: {my_range_2 is my_range_3}') # is compara si son los mismos rangos

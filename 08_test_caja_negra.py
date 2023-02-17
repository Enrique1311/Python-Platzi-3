import unittest # importa un módula para generar pruebas

def suma(num_1, num_2):
    return num_1 + num_2


class BlackBoxTest(unittest.TestCase): # realiza la prueba de una porción de código
    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 20

        result = suma(num_1, num_2)

        self.assertEqual(result, 30) # el resultado debe ser igual al segundo parámetro 

    # otra función para testear
    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -5

        result = suma(num_1, num_2)

        self.assertEqual(result, -15)

if __name__ == '__main__': # para ejecutar ésta módulo como principal
    unittest.main() # ejecuta el módulo dentro de la función unittest


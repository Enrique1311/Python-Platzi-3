import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    def test_es_mayor_de_edad(self):
        edad = 20
        result  = es_mayor_de_edad(edad)
        self.assertEqual(result, True)

    def test_es_menor_de_edad(self):
        edad = 15
        result = es_mayor_de_edad(edad)
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
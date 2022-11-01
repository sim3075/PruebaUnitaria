import unittest
from ejercicio import suma_numeros

class Testsuma(unittest.TestCase):

    def test_numeros_default(self):
        self.assertEqual(suma_numeros(), 5050)

    def test_numeros_various_inputs(self):

        self.assertEqual(suma_numeros(range(1, 11)), 55)
        self.assertEqual(suma_numeros([1, 2, 3]), 6)
        self.assertEqual(suma_numeros((1, 2, 3)), 6)
        self.assertEqual(suma_numeros([]), 0)


if __name__ == '__main__':
    unittest.main()
import unittest

from complejos import suma, resta, product, division, modulo, conjugado


class TestComplejos(unittest.TestCase):

    # 1. Prueba de Suma

    def test_suma_1(self):
        resultado = suma((5, -4), (1, 2))
        esperado = (6, -2)

        self.assertEqual(resultado, esperado)

    def test_suma_2(self):
        resultado = suma((3, 2), (4, 5))
        esperado = (7, 7)

        self.assertEqual(resultado, esperado)


    # 2. Prueba de resta

    def test_resta_1(self):
        resultado = resta((5, -4), (1, 2))
        esperado = (4, -6)

        self.assertEqual(resultado, esperado)

    def test_resta_2(self):
        resultado = resta((8, 5), (3, 2))
        esperado = (5, 3)

        self.assertEqual(resultado, esperado)


    # 3. Prueba de multiplicación

    def test_multiplicacion_1(self):
        resultado = product((5, -4), (1, 2))
        esperado = (13, 6)

        self.assertEqual(resultado, esperado)

    def test_multiplicacion_2(self):
        resultado = product((3, 2), (4, 5))
        esperado = (2, 23)

        self.assertEqual(resultado, esperado)


    # 4. Prueba de división

    def test_division_1(self):
        resultado = division((5, -4), (1, 2))
        esperado = (-0.6, -2.8)

        self.assertEqual(resultado, esperado)

    def test_division_2(self):
        resultado = division((4, 2), (1, 1))
        esperado = (3, -1)

        self.assertEqual(resultado, esperado)


    # 5. Pruebas de módulo

    def test_modulo_1(self):
        resultado = modulo((3, 4))
        esperado = 5

        self.assertEqual(resultado, esperado)

    def test_modulo_2(self):
        resultado = modulo((5, 12))
        esperado = 13

        self.assertEqual(resultado, esperado)


    # 6. Prueba de conjugado

    def test_conjugado_1(self):
        resultado = conjugado((3, 2))
        esperado = (3, -2)

        self.assertEqual(resultado, esperado)

    def test_conjugado_2(self):
        resultado = conjugado((5, -4))
        esperado = (5, 4)

        self.assertEqual(resultado, esperado)


if __name__ == '__main__':
    unittest.main()
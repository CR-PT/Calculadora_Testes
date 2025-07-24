import unittest
import math
from main import calculadora, calculadora_v2, calculadora_v3, calculadora_v4

class TestCalculadora(unittest.TestCase):

    def teste_operacoes_basicas(self):
        # Teste operaciones básicas para calculadora
        self.assertEqual(calculadora(2, 3, '+'), 5)
        self.assertEqual(calculadora(5, 3, '-'), 2)
        self.assertEqual(calculadora(4, 3, '*'), 12)
        self.assertEqual(calculadora(10, 2, '/'), 5.0)
        self.assertEqual(calculadora(10, 3, '%'), 1)
        self.assertEqual(calculadora(2, 3, '^'), 8)

    def teste_v2_operacoes(self):
        # Teste operaciones básicas para calculadora_v2
        self.assertEqual(calculadora_v2(2, 3, '+'), 5)
        self.assertEqual(calculadora_v2(5, 3, '-'), 2)
        self.assertEqual(calculadora_v2(4, 3, '*'), 12)
        self.assertEqual(calculadora_v2(10, 2, '/'), 5.0)
        self.assertEqual(calculadora_v2(10, 3, '%'), 1)
        self.assertEqual(calculadora_v2(2, 3, '^'), 8)

    def teste_v3_operacoes(self):
        # Teste operaciones básicas para calculadora_v3
        self.assertEqual(calculadora_v3(2, 3, '+'), 5)
        self.assertEqual(calculadora_v3(5, 3, '-'), 2)
        self.assertEqual(calculadora_v3(4, 3, '*'), 12)
        self.assertEqual(calculadora_v3(10, 2, '/'), 5.0)
        self.assertEqual(calculadora_v3(10, 3, '%'), 1)
        self.assertEqual(calculadora_v3(2, 3, '^'), 8)

    def teste_v4_operacoes(self):
        # Teste operaciones básicas para calculadora_v4
        self.assertEqual(calculadora_v4(2, 3, '+'), 5)
        self.assertEqual(calculadora_v4(5, 3, '-'), 2)
        self.assertEqual(calculadora_v4(4, 3, '*'), 12)
        self.assertEqual(calculadora_v4(10, 2, '/'), 5.0)
        self.assertEqual(calculadora_v4(10, 3, '%'), 1)
        self.assertEqual(calculadora_v4(2, 3, '^'), 8)

    def teste_operacoes_diversas(self):
        # Teste división por cero para todas las versiones
        for calc in [calculadora, calculadora_v2, calculadora_v3, calculadora_v4]:
            self.assertTrue(math.isnan(calc(5, 0, '/')))
            self.assertTrue(math.isnan(calc(5, 0, '%')))

        # Teste operadores inválidos - tres pruebas para todas las versiones
        for calc in [calculadora, calculadora_v2, calculadora_v3, calculadora_v4]:
            self.assertTrue(math.isnan(calc(2, 3, '$')))
            self.assertTrue(math.isnan(calc(2, 5, '#')))
            self.assertTrue(math.isnan(calc(0, 2, 'qwe')))

        # Teste números decimales - tres pruebas para todas las versiones
        for calc in [calculadora, calculadora_v2, calculadora_v3, calculadora_v4]:
            self.assertAlmostEqual(calc(2.5, 1.5, '+'), 4.0)
            self.assertAlmostEqual(calc(4.5, 1.5, '-'), 3.0)
            self.assertAlmostEqual(calc(5.5, 1.5, '*'), 8.25)

        # Teste números negativos - tres pruebas para todas las versiones
        for calc in [calculadora, calculadora_v2, calculadora_v3, calculadora_v4]:
            self.assertEqual(calc(-2, 3, '*'), -6)
            self.assertEqual(calc(-5, -2, '+'), -7)
            self.assertEqual(calc(-10, 2, '/'), -5.0)

        # Teste división y módulo con números negativos
        for calc in [calculadora, calculadora_v2, calculadora_v3, calculadora_v4]:
            self.assertEqual(calc(-6, 3, '/'), -2.0)
            self.assertEqual(calc(-7, 3, '%'), 2)


        # Teste exponenciación con números negativos
        for calc in [calculadora, calculadora_v2, calculadora_v3, calculadora_v4]:
            self.assertEqual(calc(-2, 3, '^'), -8)

        # Teste exponenciación con base cero
        for calc in [calculadora, calculadora_v2, calculadora_v3, calculadora_v4]:
            self.assertEqual(calc(0, 3, '^'), 0)

if __name__ == '__main__':
    unittest.main()

# Para correr los tests: python -m unittest -v testes_main_alunos.py
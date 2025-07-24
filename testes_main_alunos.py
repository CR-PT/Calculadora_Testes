import unittest
import math
from main import calculadora, calculadora_v2, calculadora_v3, calculadora_v4

class TesteCalculadora(unittest.TestCase):

    def teste_operacoes_diversas(self):
        self.assertTrue(math.isnan(calculadora(5, 0, '/')))
        self.assertEqual(calculadora(5, 5, '+'), 10)
        self.assertEqual(calculadora(5, 5, '-'), 0)
        self.assertEqual(calculadora(5, 5, '*'), 25)
        self.assertEqual(calculadora(5, 5, '/'), 1)
        self.assertEqual(calculadora(5, 2, '**'), 25)

    def teste_operacoes_diversas_v2(self):
        self.assertTrue(math.isnan(calculadora_v2(5, 0, '/')))
        self.assertEqual(calculadora_v2(5, 5, '+'), 10)
        self.assertEqual(calculadora_v2(5, 5, '-'), 0)
        self.assertEqual(calculadora_v2(5, 5, '*'), 25)
        self.assertEqual(calculadora_v2(5, 5, '/'), 1)
        self.assertEqual(calculadora_v2(5, 2, '**'), 25)

    def teste_operacoes_diversas_v3(self):
        self.assertTrue(math.isnan(calculadora_v3(5, 0, '/')))
        self.assertEqual(calculadora_v3(5, 5, '+'), 10)
        self.assertEqual(calculadora_v3(5, 5, '-'), 0)
        self.assertEqual(calculadora_v3(5, 5, '*'), 25)
        self.assertEqual(calculadora_v3(5, 5, '/'), 1)
        self.assertEqual(calculadora_v3(5, 2, '**'), 25)

    def teste_operacoes_diversas_v4(self):
        self.assertTrue(math.isnan(calculadora_v4(5, 0, '/')))
        self.assertEqual(calculadora_v4(5, 5, '+'), 10)
        self.assertEqual(calculadora_v4(5, 5, '-'), 0)
        self.assertEqual(calculadora_v4(5, 5, '*'), 25)
        self.assertEqual(calculadora_v4(5, 5, '/'), 1)
        self.assertEqual(calculadora_v4(5, 2, '**'), 25)

if __name__ == '__main__':
    unittest.main()

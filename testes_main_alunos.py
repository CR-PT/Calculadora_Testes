import unittest
import math
from main import calculadora, calculadora_v2, calculadora_v3, calculadora_v4

class TesteCalculadora(unittest.TestCase):

    def test_operacoes_diversas(self):
        # Testar divisão por zero
        self.assertTrue(math.isnan(calculadora(5, 0, '/')))
        # Testar adição
        self.assertEqual(calculadora(5, 5, '+'), 10)
        # Testar subtração
        self.assertEqual(calculadora(5, 5, '-'), 0)
        # Testar multiplicação
        self.assertEqual(calculadora(5, 5, '*'), 25)
        # Testar divisão
        self.assertEqual(calculadora(5, 5, '/'), 1)
        # Testar módulo
        self.assertEqual(calculadora(5, 2, '%'), 1)  # 5 % 2 = 1
        # Testar potência (corrigido para usar '^')
        self.assertEqual(calculadora(5, 2, '^'), 25)  # 5 ^ 2 = 25
        # Testar operador inválido
        self.assertTrue(math.isnan(calculadora(5, 5, '#')))

    def test_operacoes_diversas_v2(self):
        # Testar divisão por zero
        self.assertTrue(math.isnan(calculadora_v2(5, 0, '/')))
        # Testar adição
        self.assertEqual(calculadora_v2(5, 5, '+'), 10)
        # Testar subtração
        self.assertEqual(calculadora_v2(5, 5, '-'), 0)
        # Testar multiplicação
        self.assertEqual(calculadora_v2(5, 5, '*'), 25)
        # Testar divisão
        self.assertEqual(calculadora_v2(5, 5, '/'), 1)
        # Testar módulo
        self.assertEqual(calculadora_v2(5, 2, '%'), 1)  # 5 % 2 = 1
        # Testar potência (corrigido para usar '^')
        self.assertEqual(calculadora_v2(5, 2, '^'), 25)  # 5 ^ 2 = 25
        # Testar operador inválido
        self.assertTrue(math.isnan(calculadora_v2(5, 5, '#')))

    def test_operacoes_diversas_v3(self):
        # Testar divisão por zero
        self.assertTrue(math.isnan(calculadora_v3(5, 0, '/')))
        # Testar adição
        self.assertEqual(calculadora_v3(5, 5, '+'), 10)
        # Testar subtração
        self.assertEqual(calculadora_v3(5, 5, '-'), 0)
        # Testar multiplicação
        self.assertEqual(calculadora_v3(5, 5, '*'), 25)
        # Testar divisão
        self.assertEqual(calculadora_v3(5, 5, '/'), 1)
        # Testar módulo
        self.assertEqual(calculadora_v3(5, 2, '%'), 1)  # 5 % 2 = 1
        # Testar potência (corrigido para usar '^')
        self.assertEqual(calculadora_v3(5, 2, '^'), 25)  # 5 ^ 2 = 25
        # Testar operador inválido
        self.assertTrue(math.isnan(calculadora_v3(5, 5, '#')))

    def test_operacoes_diversas_v4(self):
        # Testar divisão por zero
        self.assertTrue(math.isnan(calculadora_v4(5, 0, '/')))
        # Testar adição
        self.assertEqual(calculadora_v4(5, 5, '+'), 10)
        # Testar subtração
        self.assertEqual(calculadora_v4(5, 5, '-'), 0)
        # Testar multiplicação
        self.assertEqual(calculadora_v4(5, 5, '*'), 25)
        # Testar divisão
        self.assertEqual(calculadora_v4(5, 5, '/'), 1)
        # Testar módulo
        self.assertEqual(calculadora_v4(5, 2, '%'), 1)  # 5 % 2 = 1
        # Testar potência (corrigido para usar '^')
        self.assertEqual(calculadora_v4(5, 2, '^'), 25)  # 5 ^ 2 = 25
        # Testar operador inválido
        self.assertTrue(math.isnan(calculadora_v4(5, 5, '#')))

if __name__ == '__main__':
    unittest.main()

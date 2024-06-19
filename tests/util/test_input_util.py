'''
Testes do módulo input_util.py
pytest tests/util/test_input_util.py -vv
python -m unittest -v tests.util.test_input_util.Test -v
'''
from unittest.mock import patch, call
from unittest import TestCase
from util.input_util import input_int, input_float, input_opcoes

class Test(TestCase):
    '''
    Classe de teste para inputs.
    '''
    @patch('util.input_util.get_input')
    def test_input_int_valido(self, get_input):
        '''
        Teste para input de numero inteiro válido.  
        python -m unittest -v tests.util.test_input_util.Test.test_input_int_valido -v
        '''
        msg = 'Entre com um número inteiro'
        get_input.return_value = '1'
        x = input_int(msg)
        self.assertEqual(x, 1)
        get_input.assert_has_calls([
            call(msg)
        ])

    @patch('util.input_util.get_input')
    def test_input_int_invalido(self, get_input):
        '''
        Teste para input de numero inteiro inválido.
        python -m unittest -v tests.util.test_input_util.Test.test_input_int_invalido -v
        '''
        msg = 'Entre com um número inteiro'
        get_input.side_effect = ['X', '2']
        x = input_int(msg)
        self.assertEqual(x, 2)
        get_input.assert_has_calls([
            call(msg),
            call(msg),
        ])

    @patch('util.input_util.get_input')
    def test_input_float_valido(self, get_input):
        '''
        Teste para input de numero float válido.  
        python -m unittest -v tests.util.test_input_util.Test.test_input_float_valido -v
        '''
        msg = 'Entre com um número float'
        get_input.return_value = '1.7'
        x = input_float(msg)
        self.assertEqual(x, 1.7)
        get_input.assert_has_calls([
            call(msg)
        ])

    @patch('util.input_util.get_input')
    def test_input_float_invalido(self, get_input):
        '''
        Teste para input de numero float inválido.
        python -m unittest -v tests.util.test_input_util.Test.test_input_float_invalido -v
        '''
        msg = 'Entre com um número float'
        get_input.side_effect = ['X', '2.8']
        x = input_float(msg)
        self.assertEqual(x, 2.8)
        get_input.assert_has_calls([
            call(msg),
            call(msg),
        ])

    @patch('util.input_util.get_input')
    def test_input_opcoes_valido(self, get_input):
        '''
        Teste para input de opções válido.  
        python -m unittest -v tests.util.test_input_util.Test.test_input_opcoes_valido -v
        '''
        msg = 'Entre com um opção'
        get_input.return_value = 'A'
        x = input_opcoes(msg, ['A', 'B', 'C'])
        self.assertEqual(x, 'A')
        get_input.assert_has_calls([
            call(msg)
        ])

    @patch('util.input_util.get_input')
    def test_input_opcoes_invalido(self, get_input):
        '''
        Teste para input de opções inválido.  
        python -m unittest -v tests.util.test_input_util.Test.test_input_opcoes_invalido -v
        '''
        msg = 'Entre com um opção'
        get_input.side_effect = ['X', 'B']
        x = input_opcoes(msg, ['A', 'B', 'C'])
        self.assertEqual(x, 'B')
        get_input.assert_has_calls([
            call(msg),
            call(msg),
        ])

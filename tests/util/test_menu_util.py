'''
Testes do módulo menu_util.py
pytest tests/util/test_menu_util.py -vv
'''
from unittest.mock import patch, call
from unittest import TestCase
from src.util.menu_util import exibir_menu, escolher_uma_opcao_do_menu_entrada

def test_exibir_menu():
    '''
    Testa a exibição de menu.
    pytest tests/util/test_menu_util.py::test_exibir_menu -vv
    '''
    opcoes = {
        'A': 'A TESTE',
        'C': 'C TESTE',
        'D': 'D TESTE'
    }
    exibir_menu(opcoes)
    assert True

class Test(TestCase):
    '''
    Classe de teste para inputs.
    '''

    @patch('src.util.menu_util.input_opcoes')
    def test_escolher_uma_opcao_do_menu_entrada_valido(self, input_opcoes):
        '''
        Teste para input das opções do menu: ['E', D', 'S', 'F'] OPÇÃO-VÁLIDA.
        python -m unittest -v tests.util.test_menu_util.Test.test_escolher_uma_opcao_do_menu_entrada_valido -v
        '''
        opcoes_do_menu_entrada = {
        'E': 'Extrato',
        'D': 'Depósito',
        'S': 'Saque', 
        'F': 'Finalizar e sair da conta.',
        }
        exibir_menu(opcoes_do_menu_entrada)
        siglas: list[str] = list(opcoes_do_menu_entrada)
        msg = 'Entre com a opção desejada: '
        input_opcoes.return_value = 'E'
        opcao_escolhida = 'E'
        escolher_opcao = escolher_uma_opcao_do_menu_entrada(opcoes_do_menu_entrada)
        self.assertEqual(escolher_opcao, opcao_escolhida)
        input_opcoes.assert_has_calls([
            call(msg, siglas),
        ])

    @patch('src.util.menu_util.input_opcoes')
    def test_escolher_uma_opcao_do_menu_entrada_invalido(self, input_opcoes):
        '''
        Teste para input das opções do menu: ['E', D', 'S', 'F'] OPÇÃO-INVÁLIDA.
        python -m unittest -v tests.util.test_menu_util.Test.test_escolher_uma_opcao_do_menu_entrada_invalido -v
        '''
        opcoes_do_menu_entrada = {
        'E': 'Extrato',
        'D': 'Depósito',
        'S': 'Saque', 
        'F': 'Finalizar e sair da conta.',
        }
        exibir_menu(opcoes_do_menu_entrada)
        siglas: list[str] = list(opcoes_do_menu_entrada)
        msg = 'Entre com a opção desejada: '
        opcao_escolhida = 'E'
        input_opcoes.side_effect = ['OPÇÃO INVÁLIDA', opcao_escolhida]
        escolher_opcao = escolher_uma_opcao_do_menu_entrada(opcoes_do_menu_entrada)
        self.assertEqual(escolher_opcao, opcao_escolhida)
        input_opcoes.assert_has_calls([
            call(msg, siglas),
            call(msg, siglas),
        ])
# pylint: disable=line-too-long
'''
Testes do fluxo principal main.py
pytest tests/test_main.py -vv
'''

from unittest.mock import patch, call
from unittest import TestCase
from datetime import datetime
from main import (
    get_login_na_conta,
    escolher_uma_opcao_do_menu_entrada,
    siglas_das_opcoes_menu_entrada,
    exibir_mensagem_de_boas_vindas,
    main
)


class Test(TestCase):
    '''
    Classe de teste para inputs.
    '''
    ################################################
     # TESTES USUÁRIO #
    ################################################

    @patch('main.input_int')
    @patch('main.get_senha')
    def test_obter_usuario_valido(self, get_senha, input_int):
        '''
        Teste para input das credenciais do usuario (nome e senha).  NOME_E_SENHA-INVÁLIDOS 
        python -m unittest -v tests.test_main.Test.test_obter_usuario_valido -v
        '''
        msg_nome = "\n Conta Corrente: "
        msg_senha = " Senha: "
        get_senha.return_value = '123'
        conta_usuario = 555555
        input_int.return_value = conta_usuario
        login = get_login_na_conta()
        self.assertIsNotNone(login, 'Úsuario esperado não é CONTA')
        self.assertEqual(login['conta_numero'], conta_usuario)
        input_int.assert_has_calls([
            call(msg_nome)
        ])
        get_senha.assert_has_calls([
            call(msg_senha)
        ])

    ########################################################
    # TESTES  ESCOLHER OPÇÃO DA OPERAÇÃO/E OU MOVIMENTÇÃO #
    #######################################################

    @patch('main.input_opcoes')
    def test_escolher_uma_opcao_do_menu_entrada_valido(self, input_opcoes):
        '''
        Teste para input das opções do menu: ['E', D', 'S', 'F'] OPÇÃO-VÁLIDA.
        python -m unittest -v tests.test_main.Test.test_escolher_uma_opcao_do_menu_entrada_valido -v
        '''
        msg = 'Entre com a opção desejada: '
        input_opcoes.return_value = 'E'
        opcao_escolhida = 'E'
        escolher_opcao = escolher_uma_opcao_do_menu_entrada()
        self.assertEqual(escolher_opcao, opcao_escolhida)
        input_opcoes.assert_has_calls([
            call(msg, siglas_das_opcoes_menu_entrada),
        ])

    @patch('main.input_opcoes')
    def test_escolher_uma_opcao_do_menu_entrada_invalido(self, input_opcoes):
        '''
        Teste para input das opções do menu: ['E', D', 'S', 'F'] OPÇÃO-INVÁLIDA.
        python -m unittest -v tests.test_main.Test.test_escolher_uma_opcao_do_menu_entrada_invalido -v
        '''
        msg = 'Entre com a opção desejada: '
        opcao_escolhida = 'E'
        input_opcoes.side_effect = ['OPÇÃO INVÁLIDA', opcao_escolhida]
        escolher_opcao = escolher_uma_opcao_do_menu_entrada()
        self.assertEqual(escolher_opcao, opcao_escolhida)
        input_opcoes.assert_has_calls([
            call(msg, siglas_das_opcoes_menu_entrada),
            call(msg, siglas_das_opcoes_menu_entrada),
        ])

    ################################################
     # TESTES DO FLUXO PRINCIPAL -> MAIN #
    ################################################
    @patch('main.exibir_extrato')
    @patch('main.depositar')
    @patch('main.sacar')
    @patch('main.escolher_uma_opcao_do_menu_entrada')
    # @patch('main.exibir_mensagem_de_boas_vindas')
    @patch('main.get_login_na_conta')
    def test_main_opcao( # pylint: disable=too-many-arguments
        self,
        get_login_na_conta_mock,
        escolher_uma_opcao_do_menu_entrada_mock,
        sacar_mock,
        depositar_mock,
        exibir_extrato_mock,
    ):
        '''
        Teste do fluxo principal - main() 
        python -m unittest -v tests.test_main.Test.test_main_opcao -v
        '''
        get_login_na_conta_mock.return_value =  {
            'conta_numero': 555555,
            'usuario_nome': 'test'
        }
        escolher_uma_opcao_do_menu_entrada_mock.side_effect = ['D', 'E', 'S', 'F']
        exibir_extrato_mock.return_value = None
        depositar_mock.return_value = None
        sacar_mock.return_value = None
        main()


###############################################
    # TESTES SAUDAÇÃO USUÁRIO #
###############################################

def test_mensagem_boas_vindas_bom_dia():
    '''
    Teste para mensagem de boas vindas com bom dia.
    pytest tests/test_main.py::test_mensagem_boas_vindas_bom_dia -vv
    '''
    nome_usuario = 'test'
    hora_manha= datetime(2021, 6, 10, 6, 10, 00)
    exibir_mensagem_de_boas_vindas(nome_usuario, hora_manha)
    assert True

def test_mensagem_boas_vindas_boa_tarde():
    '''
    Teste para mensagem de boas vindas com boa tarde.
    pytest tests/test_main.py::test_mensagem_boas_vindas_boa_tarde -vv
    '''
    nome_usuario = 'test'
    hora_tarde= datetime(2021, 6, 10, 16, 10, 00)
    exibir_mensagem_de_boas_vindas(nome_usuario, hora_tarde)
    assert True

def test_mensagem_boas_vindas_boa_noite():
    '''
    Teste para mensagem de boas vindas com boa noite.
    pytest tests/test_main.py::test_mensagem_boas_vindas_boa_noite -vv
    '''
    nome_usuario = 'test'
    hora_noite= datetime(2021, 6, 10, 22, 10, 00)
    exibir_mensagem_de_boas_vindas(nome_usuario, hora_noite)
    assert True


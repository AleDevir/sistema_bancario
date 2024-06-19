# pylint: disable=line-too-long
'''
Testes do artefato operacoes_bancarias.py
pytest tests/test_operacoes_bancarias.py -vv
'''

from unittest.mock import patch, call
from unittest import TestCase
from datetime import datetime
from operacoes_bancarias import (
    obter_usuario,
    escolher_uma_opcao_do_menu_entrada,
    siglas_das_opcoes_menu_entrada,
    obter_movimentacao_financeira_do_usuario,
    exibir_mensagem_de_boas_vindas,
    exibir_extrato,
    calcular_saldo_do_usuario,
    pode_sacar_hoje,
    validar_saque,
    sacar,
    depositar,
    main,
)


class Test(TestCase):
    '''
    Classe de teste para inputs.
    '''

    ################################################
     # TESTES USUÁRIO #
    ################################################

    @patch('operacoes_bancarias.get_input')
    @patch('operacoes_bancarias.get_senha')
    def test_obter_usuario_valido(self, get_senha, get_input):
        '''
        Teste para input das credenciais do usuario (nome e senha).  NOME_E_SENHA-INVÁLIDOS 
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_obter_usuario_valido -v
        '''
        msg_nome = 'Nome'
        msg_senha = 'Senha'
        get_senha.return_value = '123'
        nome_usuario = 'ale'
        get_input.return_value = nome_usuario
        usuario = obter_usuario()
        self.assertIsNotNone(usuario, 'Úsuario esperado não é NONE')
        self.assertEqual(usuario['nome'], nome_usuario)
        get_input.assert_has_calls([
            call(f'\n {msg_nome}: ')
        ])
        get_senha.assert_has_calls([
            call(f' {msg_senha}: ')
        ])

    @patch('operacoes_bancarias.get_input')
    @patch('operacoes_bancarias.get_senha')
    def test_obter_usuario_senha_invalida(self, get_senha, get_input):
        '''
        Teste para input das credencial senha inválida do usuario (nome e senha).  SENHA-INVÁLIDA 
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_obter_usuario_senha_invalida -v
        '''
        msg_nome = 'Nome'
        msg_senha = 'Senha'
        get_senha.side_effect = ['SENHA INVÁLIDA', '123']
        nome_usuario = 'ale'
        get_input.return_value = nome_usuario
        usuario = obter_usuario()
        self.assertIsNotNone(usuario, 'Usuário esperado não é NONE')
        self.assertEqual(usuario['nome'], nome_usuario)
        get_input.assert_has_calls([
            call(f'\n {msg_nome}: '),
            call(f'\n {msg_nome}: '),
        ])
        get_senha.assert_has_calls([
            call(f' {msg_senha}: '),
            call(f' {msg_senha}: '),
        ])

    @patch('operacoes_bancarias.get_input')
    @patch('operacoes_bancarias.get_senha')
    def test_obter_usuario_nome_invalido(self, get_senha, get_input):
        '''
        Teste para input das credencial nome inválido do usuario (nome e senha). NOME-INVÁLIDO 
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_obter_usuario_nome_invalido -v
        '''
        msg_nome = 'Nome'
        msg_senha = 'Senha'
        get_senha.return_value = '123'
        nome_usuario = 'ale'
        get_input.side_effect = ['NOME INVÁLIDO', nome_usuario]
        usuario = obter_usuario()
        self.assertIsNotNone(usuario, 'Usuário esperado não é NONE')
        self.assertEqual(usuario['nome'], nome_usuario)
        get_input.assert_has_calls([
            call(f'\n {msg_nome}: '),
            call(f'\n {msg_nome}: '),
        ])
        get_senha.assert_has_calls([
            call(f' {msg_senha}: '),
            call(f' {msg_senha}: '),
        ])

    ########################################################
    # TESTES  ESCOLHER OPÇÃO DA OPERAÇÃO/E OU MOVIMENTÇÃO #
    #######################################################

    @patch('operacoes_bancarias.input_opcoes')
    def test_escolher_uma_opcao_do_menu_entrada_valido(self, input_opcoes):
        '''
        Teste para input das opções do menu: ['E', D', 'S', 'F'] OPÇÃO-VÁLIDA.
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_escolher_uma_opcao_do_menu_entrada_valido -v
        '''
        msg = 'Entre com a opção desejada: '
        input_opcoes.return_value = 'E'
        opcao_escolhida = 'E'
        escolher_opcao = escolher_uma_opcao_do_menu_entrada()
        self.assertEqual(escolher_opcao, opcao_escolhida)
        input_opcoes.assert_has_calls([
            call(msg, siglas_das_opcoes_menu_entrada),
        ])

    @patch('operacoes_bancarias.input_opcoes')
    def test_escolher_uma_opcao_do_menu_entrada_invalido(self, input_opcoes):
        '''
        Teste para input das opções do menu: ['E', D', 'S', 'F'] OPÇÃO-INVÁLIDA.
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_escolher_uma_opcao_do_menu_entrada_invalido -v
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

    ##################################################
     # TESTES DAS VALIDAÇÕES DAS OPERAÇÕES #
    ##################################################

    def test_pode_sacar_hoje_valido(self):
        '''
        Teste do metodo pode_sacar_hoje() - OPÇÃO VÁLIDA
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_pode_sacar_hoje_valido -v
        '''
        usuario = {
            'id': 4,
            'nome': 'test'
        }
        self.assertTrue(pode_sacar_hoje(usuario))

    def test_pode_sacar_hoje_invalido(self):
        '''
        Teste do metodo pode_sacar_hoje() - OPÇÃO INVÁLIDA
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_pode_sacar_hoje_invalido -v
        '''
        usuario = {
            'id': 3,
            'nome': 'testes'
        }
        self.assertFalse(pode_sacar_hoje(usuario))

    def test_validar_saque_valido(self):
        '''
        Teste do metodo validar_saque() - OPÇÃO VÁLIDA
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_validar_saque_valido -v
        '''
        saque = 20.5
        saldo = 122
        saque_valido = validar_saque(saque, saldo)
        self.assertEqual(saque_valido, '')

    def test_validar_saque_salo_invalido(self):
        '''
        Teste do metodo validar_saque() - SALDO INSUFICIENTE
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_validar_saque_salo_invalido -v
        '''
        saque = 20.5
        saldo = 12
        msg_saque_esperada = f"O valor {saque} excede o seu saldo atual R$ {saldo}."
        msg_saque_invalido = validar_saque(saque, saldo)
        self.assertEqual(msg_saque_invalido, msg_saque_esperada)

    def test_validar_saque_valor_invalido(self):
        '''
        Teste do metodo validar_saque() - VALOR  INVÁLIDO
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_validar_saque_valor_invalido -v
        '''
        saque = -3
        saldo = 12
        msg_saque_esperada = f"O valor do saque {saque} é inválido! O valor deve ser um número positivo." 
        msg_saque_invalido = validar_saque(saque, saldo)
        self.assertEqual(msg_saque_invalido, msg_saque_esperada)

    def test_validar_saque_limite_invalido(self):
        '''
        Teste do metodo validar_saque() - VALOR ACIMA DO LIMITE 
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_validar_saque_limite_invalido -v
        '''
        saque = 501
        saldo = 600
        msg_saque_esperada = f"O valor {saque} excede o limite de saque diário (R$500,00)."
        msg_saque_invalido = validar_saque(saque, saldo)
        self.assertEqual(msg_saque_invalido, msg_saque_esperada)

    @patch('operacoes_bancarias.input_float')
    def test_sacar_valido(self, input_float):
        '''
        Teste do metodo sacar() - OPÇÃO VÁLIDA
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_sacar_valido -v
        '''
        usuario = {
            'id': 4,
            'nome': 'tests'
        }

        msg = "Entre com o valor do saque R$: "
        saque = 50
        input_float.return_value = saque
        input_float.side_effect = [saque]
        sacar(usuario)
        input_float.assert_has_calls([
            call(msg)
        ])

    @patch('operacoes_bancarias.input_float')
    def test_sacar_valor_invalido(self, input_float):
        '''
        Teste do metodo sacar() - OPÇÃO INVÁLIDA
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_sacar_valor_invalido -v
        '''
        usuario = {
            'id': 5,
            'nome': 'tests'
        }
        msg = "Entre com o valor do saque R$: "
        saque = 150
        input_float.return_value = saque
        input_float.side_effect = [-1, saque]
        sacar(usuario)
        input_float.assert_has_calls([
            call(msg),
            call(msg),
        ])

    def test_nao_pode_sacar(self):
        '''
        Teste do metodo sacar() - OPÇÃO INVÁLIDA
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_nao_pode_sacar -v
        '''
        usuario = {
            'id': 3,
            'nome': 'tests'
        }

        sacar(usuario)
        assert True # Você já atingiu o limite de saques por dia!

    @patch('operacoes_bancarias.input_float')
    def test_depositar_valido(self, input_float):
        '''
        Teste do metodo depositar() - OPÇÃO VÁLIDA
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_depositar_valido -v
        '''
        usuario = {
            'id': 2,
            'nome': 'ale'
        }

        msg = "\nEntre com o valor do depósito R$: "
        deposito = 50
        input_float.return_value = deposito
        input_float.side_effect = [deposito]
        depositar(usuario)
        input_float.assert_has_calls([
            call(msg)
        ])

    @patch('operacoes_bancarias.input_float')
    def test_depositar_invalido(self, input_float):
        '''
        Teste do metodo depositar() - OPÇÃO INVÁLIDA
        python -m unittest -v tests.test_operacoes_bancarias.Test.test_depositar_invalido -v
        '''
        usuario = {
            'id': 2,
            'nome': 'ale'
        }

        msg = "\nEntre com o valor do depósito R$: "
        deposito = 50
        input_float.return_value = deposito
        input_float.side_effect = [-1, deposito]
        depositar(usuario)
        input_float.assert_has_calls([
            call(msg)
        ])

    ################################################
     # TESTES DO FLUXO PRINCIPAL -> MAIN #
    ################################################
    @patch('operacoes_bancarias.exibir_extrato')
    @patch('operacoes_bancarias.depositar')
    @patch('operacoes_bancarias.sacar')
    @patch('operacoes_bancarias.escolher_uma_opcao_do_menu_entrada')
    # @patch('operacoes_bancarias.exibir_mensagem_de_boas_vindas')
    @patch('operacoes_bancarias.obter_usuario')
    def test_main_opcao( # pylint: disable=too-many-arguments
        self,
        obter_usuario_mock,
        escolher_uma_opcao_do_menu_entrada_mock,
        sacar_mock,
        depositar_mock,
        exibir_extrato_mock,
    ):
        '''
        Teste do fluxo principal - main() 
        python -m unittest -v tests.test_operacoes_bancarias_main.Test.test_main_opcao -v
        '''
        obter_usuario_mock.return_value =  {
            'id': 5,
            'nome': 'testes'
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
    pytest tests/test_operacoes_bancarias.py::test_mensagem_boas_vindas_bom_dia -vv
    '''
    nome_usuario = 'teste'
    hora_manha= datetime(2021, 6, 10, 6, 10, 00)
    exibir_mensagem_de_boas_vindas(nome_usuario, hora_manha)
    assert True

def test_mensagem_boas_vindas_boa_tarde():
    '''
    Teste para mensagem de boas vindas com boa tarde.
    pytest tests/test_operacoes_bancarias.py::test_mensagem_boas_vindas_boa_tarde -vv
    '''
    nome_usuario = 'teste'
    hora_tarde= datetime(2021, 6, 10, 16, 10, 00)
    exibir_mensagem_de_boas_vindas(nome_usuario, hora_tarde)
    assert True

def test_mensagem_boas_vindas_boa_noite():
    '''
    Teste para mensagem de boas vindas com boa noite.
    pytest tests/test_operacoes_bancarias.py::test_mensagem_boas_vindas_boa_noite -vv
    '''
    nome_usuario = 'teste'
    hora_noite= datetime(2021, 6, 10, 22, 10, 00)
    exibir_mensagem_de_boas_vindas(nome_usuario, hora_noite)
    assert True

###############################################
    # TESTES  DAS MOVIMENTAÇÕES #
###############################################
def test_obter_movimentacao_financeira_do_usuario_valida():
    '''
    Teste do metodo obter_movimentacao_financeira_do_usuario - VÁLIDO
    pytest tests/test_operacoes_bancarias.py::test_obter_movimentacao_financeira_do_usuario_valida -vv
    '''
    usuario = {
        'id': 2
    }
    movimentacao_do_usuario = obter_movimentacao_financeira_do_usuario(usuario)
    assert movimentacao_do_usuario
    assert movimentacao_do_usuario == [m for m in movimentacao_do_usuario if m['usuario_id'] == usuario['id']]

def test_obter_movimentacao_financeira_do_usuario_invalida():
    '''
    Teste do metodo obter_movimentacao_financeira_do_usuario - INVÁLIDO
    pytest tests/test_operacoes_bancarias.py::test_obter_movimentacao_financeira_do_usuario_valida -vv
    '''
    usuario = {
        'id': 999
    }
    movimentacao_do_usuario = obter_movimentacao_financeira_do_usuario(usuario)
    assert not movimentacao_do_usuario
    assert movimentacao_do_usuario == []

def test_exibir_extrato_valida():
    '''
    Teste do metodo exibir_extrato - VÁLIDO
    pytest tests/test_operacoes_bancarias.py::test_exibir_extrato_valida -vv
    '''
    usuario = {
        'id': 2,
        'nome': 'ale'
    }
    exibir_extrato(usuario)
    assert True

def test_calcular_saldo_do_usuario():
    '''
    Teste do metodo calcular_saldo() - EXERCITANDO CÓDIGO
    pytest tests/test_operacoes_bancarias.py::test_calcular_saldo_do_usuario -vv
    '''
    usuario = {
        'id': 4,
        'nome': 'tests'
    }
    saldo = calcular_saldo_do_usuario(usuario)
    assert saldo == 450

##################################################
     # TESTES DAS VALIDAÇÕES DAS OPERAÇÕES #
##################################################

def test_pode_sacar_hoje():
    '''
    Teste do metodo pode_sacar_hoje() - OPÇÃO VÁLIDA
    pytest tests/test_operacoes_bancarias.py::test_pode_sacar_hoje -vv
    '''
    usuario = {
        'id': 4,
        'nome': 'tests'
    }
    pode_sacar_hoje(usuario)
    assert True

def test_pode_sacar_hoje_invalido():
    '''
    Teste do metodo pode_sacar_hoje() - OPÇÃO INVÁLIDA
    pytest tests/test_operacoes_bancarias.py::test_pode_sacar_hoje_invalido -vv
    '''
    usuario = {
        'id': 3,
        'nome': 'tests'
    }
    pode_sacar = pode_sacar_hoje(usuario)
    assert not pode_sacar

def test_validar_saque_valido():
    '''
    Teste do metodo validar_saque() VÁLIDO
    pytest tests/test_operacoes_bancarias.py::test_validar_saque_valido -vv
    '''
    saque = 23
    saldo = 123
    resposta = ''
    saque_valido = validar_saque(saque, saldo)
    assert saque_valido == resposta

def test_validar_saque_saldo_insuficiente():
    '''
    Teste do metodo validar_saque() SALDO INSUFICIENTE
    pytest tests/test_operacoes_bancarias.py::test_validar_saque_saldo_insuficiente -vv
    '''
    saque = 23
    saldo = 12
    resposta = f"O valor {saque} excede o seu saldo atual R$ {saldo}."
    saque_valido = validar_saque(saque, saldo)
    assert saque_valido == resposta

def test_validar_saque_limite_de_saques_invalido():
    '''
    Teste do metodo validar_saque() LIMITE DE SAQUE DIÁRIO INVÁLIDO
    pytest tests/test_operacoes_bancarias.py::test_validar_saque_limite_de_saques_invalido -vv
    '''
    saque = 1000
    saldo = 12
    resposta = f"O valor {saque} excede o limite de saque diário (R$500,00)."
    saque_valido = validar_saque(saque, saldo)
    assert saque_valido == resposta

def test_validar_saque_valor_de_saques_invalido():
    '''
    Teste do metodo validar_saque() VALOR DE SAQUE DIÁRIO INVÁLIDO
    pytest tests/test_operacoes_bancarias.py::test_validar_saque_valor_de_saques_invalido -vv
    '''
    saque = -2
    saldo = 12
    resposta = f"O valor do saque {saque} é inválido! O valor deve ser um número positivo."
    saque_valido = validar_saque(saque, saldo)
    assert saque_valido == resposta

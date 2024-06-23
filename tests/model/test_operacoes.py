# pylint: disable=line-too-long
'''
Testes do model operacoes.py
pytest tests/model/test_operacoes.py -vv
'''

from unittest.mock import patch, call
from unittest import TestCase
from src.model.operacoes import (
   get_movimentacao_financeira_do_usuario,
   exibir_extrato,
   calcular_saldo_do_usuario,
   calcular_saldo_das_movimentacoes,
   pode_sacar_hoje,
   validar_saque,
   sacar,
   depositar
)

###########################################################
    # TESTES  DAS MOVIMENTAÇÕES #
##########################################################
def test_get_movimentacao_financeira_do_usuario_valida():
    '''
    Teste do metodo get_movimentacao_financeira_do_usuario - VÁLIDO
    pytest tests/model/test_operacoes.py::test_get_movimentacao_financeira_do_usuario_valida -vv
    '''
    login = {
        'usuario_id': 1
    }
    movimentacao_do_usuario = get_movimentacao_financeira_do_usuario(login)
    assert movimentacao_do_usuario
    assert movimentacao_do_usuario == [m for m in movimentacao_do_usuario if m['usuario_id'] == login['usuario_id']]

def test_get_movimentacao_financeira_do_usuario_invalida():
    '''
    Teste do metodo get_movimentacao_financeira_do_usuario - INVÁLIDO
    pytest tests/model/test_operacoes.py::test_get_movimentacao_financeira_do_usuario_invalida -vv
    '''
    login = {
        'usuario_id': 999
    }
    movimentacao_do_usuario = get_movimentacao_financeira_do_usuario(login)
    assert not movimentacao_do_usuario
    assert movimentacao_do_usuario == []

def test_exibir_extrato():
    '''
    Teste do metodo exibir_extrato 
    pytest tests/model/test_operacoes.py::test_exibir_extrato -vv
    '''
    login = {
        'usuario_id': 1,
        'usuario_nome': 'rinaldo benevies'

    }
    exibir_extrato(login)
    assert True

def test_calcular_saldo_das_movimentacoes():
    '''
    Teste do metodo calcular_saldo_das_movimentacoes() - EXERCITANDO CÓDIGO
    pytest tests/model/test_operacoes.py::test_calcular_saldo_das_movimentacoes -vv
    '''

    movimentacoes = [{'valor': 330.90},{'valor': 500}]
    saldo = calcular_saldo_das_movimentacoes(movimentacoes)
    assert saldo == 830.90

def test_calcular_saldo_do_usuario():
    '''
    Teste do metodo calcular_saldo_do_usuario - EXERCITANDO CÓDIGO
    pytest tests/model/test_operacoes.py::test_calcular_saldo_do_usuario -vv
    '''
    login = {
        'usuario_id': 5,
        'usuario_nome': 'test'

    }
    saldo = calcular_saldo_do_usuario(login)
    assert saldo == 500

##################################################
     # TESTES DAS VALIDAÇÕES DAS OPERAÇÕES #
##################################################

def test_pode_sacar_hoje():
    '''
    Teste do metodo pode_sacar_hoje() - OPÇÃO VÁLIDA
    pytest tests/model/test_operacoes.py::test_pode_sacar_hoje -vv
    '''
    login = {
        'usuario_id': 5,
        'usuario_nome': 'test'

    }
    pode_sacar_hoje(login)
    assert True

def test_pode_sacar_hoje_invalido():
    '''
    Teste do metodo pode_sacar_hoje() - OPÇÃO INVÁLIDA
    pytest tests/model/test_operacoes.py::test_pode_sacar_hoje_invalido -vv
    '''
    login = {
        'usuario_id': 3,
        'usuario_nome': 'test'

    }
    pode_sacar = pode_sacar_hoje(login)
    assert not pode_sacar

def test_validar_saque_valido():
    '''
    Teste do metodo validar_saque() VÁLIDO
    pytest tests/model/test_operacoes.py::test_validar_saque_valido -vv
    '''
    saque = 23
    saldo = 123
    resposta = ''
    saque_valido = validar_saque(saque, saldo)
    assert saque_valido == resposta

def test_validar_saque_saldo_insuficiente():
    '''
    Teste do metodo validar_saque() SALDO INSUFICIENTE
    pytest tests/model/test_operacoes.py::test_validar_saque_saldo_insuficiente -vv
    '''
    saque = 23
    saldo = 12
    resposta = f"O valor {saque} excede o seu saldo atual R$ {saldo}."
    saque_valido = validar_saque(saque, saldo)
    assert saque_valido == resposta

def test_validar_saque_limite_de_saques_invalido():
    '''
    Teste do metodo validar_saque() LIMITE DE SAQUE DIÁRIO INVÁLIDO
    pytest tests/model/test_operacoes.py::test_validar_saque_limite_de_saques_invalido -vv
    '''
    saque = 1000
    saldo = 12
    resposta = f"O valor {saque} excede o limite de saque diário (R$500,00)."
    saque_valido = validar_saque(saque, saldo)
    assert saque_valido == resposta

def test_validar_saque_valor_de_saques_invalido():
    '''
    Teste do metodo validar_saque() VALOR DE SAQUE DIÁRIO INVÁLIDO
    pytest tests/model/test_operacoes.py::test_validar_saque_valor_de_saques_invalido -vv
    '''
    saque = -2
    saldo = 12
    resposta = f"O valor do saque {saque} é inválido! O valor deve ser um número positivo."
    saque_valido = validar_saque(saque, saldo)
    assert saque_valido == resposta

##############################################################################
                #TESTES UNITÁRIOS#
##############################################################################

class Test(TestCase):
    '''
    Classe de teste para inputs.
    '''
    ##################################################
     # TESTES DAS VALIDAÇÕES DAS OPERAÇÕES #
    ##################################################

    def test_pode_sacar_hoje_valido(self):
        '''
        Teste do metodo pode_sacar_hoje() - OPÇÃO VÁLIDA
        python -m unittest -v tests.model.test_operacoes.Test.test_pode_sacar_hoje_valido -v
        '''
        login = {
        'usuario_id': 5,
        'usuario_nome': 'test'
        }
        self.assertTrue(pode_sacar_hoje(login))

    def test_pode_sacar_hoje_invalido(self):
        '''
        Teste do metodo pode_sacar_hoje() - OPÇÃO INVÁLIDA
        python -m unittest -v tests.model.test_operacoes.Test.test_pode_sacar_hoje_invalido -v
        '''
        login = {
        'usuario_id': 3,
        'usuario_nome': 'test'
        }
        self.assertFalse(pode_sacar_hoje(login))

    def test_validar_saque_valido(self):
        '''
        Teste do metodo validar_saque() - OPÇÃO VÁLIDA
        python -m unittest -v tests.model.test_operacoes.Test.test_validar_saque_valido -v
        '''
        saque = 20.5
        saldo = 122
        saque_valido = validar_saque(saque, saldo)
        self.assertEqual(saque_valido, '')

    def test_validar_saque_salo_invalido(self):
        '''
        Teste do metodo validar_saque() - SALDO INSUFICIENTE
        python -m unittest -v tests.model.test_operacoes.Test.test_validar_saque_salo_invalido -v
        '''
        saque = 20.5
        saldo = 12
        msg_saque_esperada = f"O valor {saque} excede o seu saldo atual R$ {saldo}."
        msg_saque_invalido = validar_saque(saque, saldo)
        self.assertEqual(msg_saque_invalido, msg_saque_esperada)

    def test_validar_saque_valor_invalido(self):
        '''
        Teste do metodo validar_saque() - VALOR  INVÁLIDO
        python -m unittest -v tests.model.test_operacoes.Test.test_validar_saque_valor_invalido -v
        '''
        saque = -3
        saldo = 12
        msg_saque_esperada = f"O valor do saque {saque} é inválido! O valor deve ser um número positivo." 
        msg_saque_invalido = validar_saque(saque, saldo)
        self.assertEqual(msg_saque_invalido, msg_saque_esperada)

    def test_validar_saque_limite_invalido(self):
        '''
        Teste do metodo validar_saque() - VALOR ACIMA DO LIMITE 
        python -m unittest -v tests.model.test_operacoes.Test.test_validar_saque_limite_invalido -v
        '''
        saque = 501
        saldo = 600
        msg_saque_esperada = f"O valor {saque} excede o limite de saque diário (R$500,00)."
        msg_saque_invalido = validar_saque(saque, saldo)
        self.assertEqual(msg_saque_invalido, msg_saque_esperada)

    @patch('src.model.operacoes.input_float')
    def test_sacar_valido(self, input_float):
        '''
        Teste do metodo sacar() - OPÇÃO VÁLIDA
        python -m unittest -v tests.model.test_operacoes.Test.test_sacar_valido -v
        '''
        login = {
        'usuario_id': 4,
        'usuario_nome': 'test'
        }

        msg = "Entre com o valor do saque R$: "
        saque = 50
        input_float.return_value = saque
        input_float.side_effect = [saque]
        sacar(login)
        input_float.assert_has_calls([
            call(msg)
        ])

    @patch('src.model.operacoes.input_float')
    def test_sacar_valor_invalido(self, input_float):
        '''
        Teste do metodo sacar() - OPÇÃO INVÁLIDA
        python -m unittest -v tests.model.test_operacoes.Test.test_sacar_valor_invalido -v
        '''
        login = {
        'usuario_id': 5,
        'usuario_nome': 'test'
        }
        msg = "Entre com o valor do saque R$: "
        saque = 150
        input_float.return_value = saque
        input_float.side_effect = [-1, saque]
        sacar(login)
        input_float.assert_has_calls([
            call(msg),
            call(msg),
        ])

    def test_nao_pode_sacar(self):
        '''
        Teste do metodo sacar() - OPÇÃO INVÁLIDA
        python -m unittest -v tests.model.test_operacoes.Test.test_nao_pode_sacar -v
        '''
        login = {
        'usuario_id':3,
        'usuario_nome': 'test'
        }

        sacar(login)
        assert True # Você já atingiu o limite de saques por dia!

    @patch('src.model.operacoes.input_float')
    def test_depositar_valido(self, input_float):
        '''
        Teste do metodo depositar() - OPÇÃO VÁLIDA
        python -m unittest -v tests.model.test_operacoes.Test.test_depositar_valido -v
        '''
        login = {
        'usuario_id': 2,
        'usuario_nome': 'test'
        }

        msg = "\nEntre com o valor do depósito R$: "
        deposito = 50
        input_float.return_value = deposito
        input_float.side_effect = [deposito]
        depositar(login)
        input_float.assert_has_calls([
            call(msg)
        ])

    @patch('src.model.operacoes.input_float')
    def test_depositar_invalido(self, input_float):
        '''
        Teste do metodo depositar() - OPÇÃO INVÁLIDA
        python -m unittest -v tests.model.test_operacoes.Test.test_depositar_invalido -v
        '''
        login = {
        'usuario_id': 2,
        'usuario_nome': 'test'
        }

        msg = "\nEntre com o valor do depósito R$: "
        deposito = 50
        input_float.return_value = deposito
        input_float.side_effect = [-1, deposito]
        depositar(login)
        input_float.assert_has_calls([
            call(msg)
        ])
# pylint: disable=line-too-long
'''
Testes de negocio transacoes.py
pytest tests/negocio/test_transacao.py -vv
'''

from unittest import TestCase
from src.negocio.transacao import pode_sacar_hoje, validar_saque

##################################################
     # TESTES DAS VALIDAÇÕES DAS OPERAÇÕES #
##################################################

def test_pode_sacar_hoje():
    '''
    Teste do metodo pode_sacar_hoje() - OPÇÃO VÁLIDA
    pytest tests/negocio/test_transacao.py::test_pode_sacar_hoje -vv
    '''
    conta_id =  1
    pode_sacar_hoje(conta_id)
    assert True

def test_pode_sacar_hoje_invalido():
    '''
    Teste do metodo pode_sacar_hoje() - OPÇÃO INVÁLIDA
    pytest tests/negocio/test_transacao.py::test_pode_sacar_hoje_invalido -vv
    '''
    conta_id = 4
    pode_sacar = pode_sacar_hoje(conta_id)
    assert not pode_sacar

def test_validar_saque_valido():
    '''
    Teste do metodo validar_saque() VÁLIDO
    pytest tests/negocio/test_transacao.py::test_validar_saque_valido -vv
    '''
    saque = 23
    saldo = 123
    resposta = ''
    saque_valido = validar_saque(saque, saldo)
    assert saque_valido == resposta

def test_validar_saque_saldo_insuficiente():
    '''
    Teste do metodo validar_saque() SALDO INSUFICIENTE
    pytest tests/negocio/test_transacao.py::test_validar_saque_saldo_insuficiente -vv
    '''
    saque = 23
    saldo = 12
    resposta = f"O valor {saque} excede o seu saldo atual R$ {saldo}."
    saque_valido = validar_saque(saque, saldo)
    assert saque_valido == resposta

def test_validar_saque_limite_de_saques_invalido():
    '''
    Teste do metodo validar_saque() LIMITE DE SAQUE DIÁRIO INVÁLIDO
    pytest tests/negocio/test_transacao.py::test_validar_saque_limite_de_saques_invalido -vv
    '''
    saque = 1000
    saldo = 12
    resposta = f"O valor {saque} excede o limite de saque diário (R$500,00)."
    saque_valido = validar_saque(saque, saldo)
    assert saque_valido == resposta

def test_validar_saque_valor_de_saques_invalido():
    '''
    Teste do metodo validar_saque() VALOR DE SAQUE DIÁRIO INVÁLIDO
    pytest tests/negocio/test_transacao.py::test_validar_saque_valor_de_saques_invalido -vv
    '''
    saque = -2
    saldo = 12
    resposta = f"O valor do saque {saque} é inválido! O valor deve ser um número positivo."
    saque_valido = validar_saque(saque, saldo)
    assert saque_valido == resposta



##############################################################################
                # TESTES UNITÁRIOS #
##############################################################################

class Test(TestCase):
    '''
    Classe de teste para inputs.
    python -m unittest -v tests.negocio.test_transacao.Test -v
    '''
    ##################################################
     # TESTES DAS VALIDAÇÕES DAS OPERAÇÕES #
    ##################################################

    def test_pode_sacar_hoje_valido(self):
        '''
        Teste do metodo pode_sacar_hoje() - OPÇÃO VÁLIDA
        python -m unittest -v tests.negocio.test_transacao.Test.test_pode_sacar_hoje_valido -v
        '''
        conta_id = 5
        self.assertTrue(pode_sacar_hoje(conta_id))

    def test_pode_sacar_hoje_invalido(self):
        '''
        Teste do metodo pode_sacar_hoje() - OPÇÃO INVÁLIDA
        python -m unittest -v tests.negocio.test_transacao.Test.test_pode_sacar_hoje_invalido -v
        '''
        conta_id = 4
        self.assertFalse(pode_sacar_hoje(conta_id))

    def test_validar_saque_valido(self):
        '''
        Teste do metodo validar_saque() - OPÇÃO VÁLIDA
        python -m unittest -v tests.negocio.test_transacao.Test.test_validar_saque_valido -v
        '''
        saque = 20.5
        saldo = 122
        saque_valido = validar_saque(saque, saldo)
        self.assertEqual(saque_valido, '')

    def test_validar_saque_saldo_invalido(self):
        '''
        Teste do metodo validar_saque() - SALDO INSUFICIENTE
        python -m unittest -v tests.negocio.test_transacao.Test.test_validar_saque_salo_invalido -v
        '''
        saque = 20.5
        saldo = 12
        msg_saque_esperada = f"O valor {saque} excede o seu saldo atual R$ {saldo}."
        msg_saque_invalido = validar_saque(saque, saldo)
        self.assertEqual(msg_saque_invalido, msg_saque_esperada)

    def test_validar_saque_valor_invalido(self):
        '''
        Teste do metodo validar_saque() - VALOR  INVÁLIDO
        python -m unittest -v tests.negocio.test_transacao.Test.test_validar_saque_valor_invalido -v
        '''
        saque = -3
        saldo = 12
        msg_saque_esperada = f"O valor do saque {saque} é inválido! O valor deve ser um número positivo." 
        msg_saque_invalido = validar_saque(saque, saldo)
        self.assertEqual(msg_saque_invalido, msg_saque_esperada)

    def test_validar_saque_limite_invalido(self):
        '''
        Teste do metodo validar_saque() - VALOR ACIMA DO LIMITE 
        python -m unittest -v tests.negocio.test_transacao.Test.test_validar_saque_limite_invalido -v
        '''
        saque = 501
        saldo = 600
        msg_saque_esperada = f"O valor {saque} excede o limite de saque diário (R$500,00)."
        msg_saque_invalido = validar_saque(saque, saldo)
        self.assertEqual(msg_saque_invalido, msg_saque_esperada)

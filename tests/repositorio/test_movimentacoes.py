# pylint: disable=line-too-long
'''
Testes do repositorio movimentacoes_repositorio.py
pytest testsrepositorio/test_movimentacoes.py -vv
'''

from src.repositorio.movimentacoes_repositorio import (
   get_movimentacao_financeira_do_cliente,

)

###########################################################
    # TESTES  DAS MOVIMENTAÇÕES #
##########################################################
def test_get_movimentacao_financeira_do_cliente_valida():
    '''
    Teste do metodo get_movimentacao_financeira_do_cliente - VÁLIDO
    pytest tests/repositorio/test_movimentacoes.py::test_get_movimentacao_financeira_do_cliente_valida -vv
    '''
    conta_id = 1
    movimentacoes = get_movimentacao_financeira_do_cliente(conta_id)
    assert movimentacoes
    for movimentacao in movimentacoes:
        assert movimentacao.conta_id == conta_id
    

def test_get_movimentacao_financeira_do_cliente_invalida():
    '''
    Teste do metodo get_movimentacao_financeira_do_cliente - INVÁLIDO
    pytest tests/repositorio/test_movimentacoes.py::test_get_movimentacao_financeira_do_cliente_invalida -vv
    '''
    conta_id = 10
    movimentacao_do_cliente = get_movimentacao_financeira_do_cliente(conta_id)
    assert not movimentacao_do_cliente
    assert movimentacao_do_cliente == []

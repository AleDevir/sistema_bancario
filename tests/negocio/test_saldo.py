# pylint: disable=line-too-long
'''
Testes de negocio saldo.py
pytest tests/negocio/test_saldo.py -vv
'''
from datetime import datetime
from src.negocio.saldo import(
    calcular_saldo_das_movimentacoes,
    calcular_saldo_do_cliente
 
)
from src.model.movimentacoes import Movimentacoes

###########################################################
    # TESTES  DAS MOVIMENTAÇÕES #
##########################################################


def test_calcular_saldo_das_movimentacoes():
    '''
    Teste do metodo calcular_saldo_das_movimentacoes() - EXERCITANDO CÓDIGO
    pytest tests/negocio/test_saldo.py::test_calcular_saldo_das_movimentacoes -vv
    '''

    movimentacoes = [
        Movimentacoes(
            idt=1,
            valor=500,
            date=datetime(1900, 1, 1, 00, 00, 00),
            conta_id=2,
            cliente_id=3,
        ),
        Movimentacoes(
            idt=2,
            valor=330.90,
            date=datetime(1900, 1, 2, 00, 00, 00),
            conta_id=2,
            cliente_id=3,
        )
    ]
    saldo = calcular_saldo_das_movimentacoes(movimentacoes)
    assert saldo == 830.90

def test_calcular_saldo_do_cliente():
    '''
    Teste do metodo calcular_saldo_do_usuario - EXERCITANDO CÓDIGO
    pytest tests/negocio/test_saldo.py::test_calcular_saldo_do_cliente -vv
    '''
    conta_id = 6
    saldo = calcular_saldo_do_cliente(conta_id)
    assert saldo == 500

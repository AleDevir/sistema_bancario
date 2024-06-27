'''
Model das movimentações finaceiras
'''

from datetime import datetime
from src.model.movimentacoes import Movimentacoes, movimentacao_from_dict

MOVIMENTACOES: list[dict[str, str | datetime | float]] = [

    {
        'valor': 215.2,
        'date': datetime(2019, 2, 12, 12, 14, 00),
        'usuario_id': 1,
        'conta_id': 1,

    },
    {
        'valor': 25.0,
        'date': datetime(2020, 5, 10, 23, 10, 00),
        'usuario_id': 1,
        'conta_id': 2,   
    },
    {
        'valor': 100.0,
        'date': datetime(2020, 4, 17, 15, 10, 00),
        'usuario_id': 2,   
        'conta_id': 3,
    },
    {
        'valor': -10.0,
        'date': datetime.now(),
        'usuario_id': 2,
        'conta_id': 3,
    },
    {
        'valor': -15.00,
        'date': datetime.now(),
        'usuario_id': 2,
        'conta_id': 3,  
    },
    {
        'valor': -10.50,
        'date': datetime(2021, 6, 11, 18, 10, 00),
        'usuario_id': 1,
        'conta_id': 1,
    },
    {
        'valor': -30.55,
        'date': datetime.now(),
        'usuario_id': 3,
        'conta_id': 4,
    },
    {
        'valor': -15.50,
        'date': datetime.now(),
        'usuario_id': 3,
        'conta_id': 4,
    },
    {
        'valor': -35.00,
        'date': datetime.now(),
        'usuario_id': 3,
        'conta_id': 4,
    },
    {
        'valor': -53.00,
        'date': datetime(2021, 6, 10, 15, 10, 00),
        'usuario_id': 3,
        'conta_id': 4,
    },
    {
        'valor': 330.90,
        'date': datetime(2021, 6, 12, 12, 10, 00),
        'usuario_id': 3,
        'conta_id': 4,
    },
    {
        'valor': 500,
        'date': datetime(2021, 6, 9, 23, 10, 00),
        'usuario_id': 4,
        'conta_id': 6,
    },
    {
        'valor': 500,
        'date': datetime(2021, 8, 11, 18, 10, 00),
        'usuario_id': 5,
        'conta_id': 7,
    },
]

def add_movimentacao(valor: float, usuario_id: int) -> None:
    '''
    Add Movimentação
    '''
    MOVIMENTACOES.append({
        'valor': valor,
        'date': datetime.now(),
        'usuario_id': usuario_id,         
    })

def get_movimentacao_financeira() -> list[Movimentacoes]:
    '''
    Obtem dados da movimentação financeira do usuario(depósitos, saques e saldo)
    Retorna a movimentação.
    '''
    result: list[Movimentacoes] = []
    for data in MOVIMENTACOES:
        result.append(
            movimentacao_from_dict(data)
        )
    return result


def get_movimentacao_financeira_do_usuario(usuario_id: int) -> list[Movimentacoes]:
    '''
    Obtem dados da movimentação financeira do usuario(depósitos, saques e saldo)
    Retorna a movimentação.
    '''

    movimentacoes_do_usuario = [m for m in MOVIMENTACOES if m['usuario_id'] == usuario_id]
    result: list[Movimentacoes] = []
    for data in movimentacoes_do_usuario:
        result.append(
            movimentacao_from_dict(data)
        )
    return result

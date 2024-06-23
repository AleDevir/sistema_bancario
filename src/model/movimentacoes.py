'''
Model das movimentações finaceiras
'''

from datetime import datetime

movimentacoes_finaceiras: list[dict[str, str | datetime | float]] = [

    {
        'valor': 215.2,
        'data': datetime(2019, 2, 12, 12, 14, 00),
        'usuario_id': 1,
        'conta_id': 1,

    },
    {
        'valor': 25.0,
        'data': datetime(2020, 5, 10, 23, 10, 00),
        'usuario_id': 1,
        'conta_id': 2,   
    },
    {
        'valor': 100.0,
        'data': datetime(2020, 4, 17, 15, 10, 00),
        'usuario_id': 2,   
        'conta_id': 3,
    },
    {
        'valor': -10.0,
        'data': datetime.now(),
        'usuario_id': 2,
        'conta_id': 3,
    },
    {
        'valor': -15.00,
        'data': datetime.now(),
        'usuario_id': 2,
        'conta_id': 3,  
    },
    {
        'valor': -10.50,
        'data': datetime(2021, 6, 11, 18, 10, 00),
        'usuario_id': 1,
        'conta_id': 1,
    },
    {
        'valor': -30.55,
        'data': datetime.now(),
        'usuario_id': 3,
        'conta_id': 4,
    },
    {
        'valor': -15.50,
        'data': datetime.now(),
        'usuario_id': 3,
        'conta_id': 4,
    },
    {
        'valor': -35.00,
        'data': datetime.now(),
        'usuario_id': 3,
        'conta_id': 4,
    },
    {
        'valor': -53.00,
        'data': datetime(2021, 6, 10, 15, 10, 00),
        'usuario_id': 3,
        'conta_id': 4,
    },
    {
        'valor': 330.90,
        'data': datetime(2021, 6, 12, 12, 10, 00),
        'usuario_id': 3,
        'conta_id': 4,
    },
    {
        'valor': 500,
        'data': datetime(2021, 6, 9, 23, 10, 00),
        'usuario_id': 4,
        'onta_id': 6,
    },
    {
        'valor': 500,
        'data': datetime(2021, 8, 11, 18, 10, 00),
        'usuario_id': 5,
        'conta_id': 7,
    },
]

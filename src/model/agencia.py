'''
Model Agência

'id'    = PK - Primary Key: Chave Primária
'numero'= AK - Alternate Key: Chave Alternativa
'''

agencias: list[dict[str, int]] = [
    {
        'id': 1,
        'numero': 111,
        'digito': 1,
    },
    {
        'id': 2,
        'numero': 222,
        'digito': 2,
    },
    {
        'id': 3,
        'numero': 333,
        'digito': 3,
    },
]

def get_agencia_by_id(agencia_id: int) -> dict[str, int]:
    '''
    Obter uma agência pelo ID.
    '''
    return next((a for a in agencias if a['id'] == agencia_id), {})

def get_agencia_by_numero(agencia_numero: int) -> dict[str, int]:
    '''
    Obter uma agência pelo NÚMERO.
    '''
    return next((a for a in agencias if a['numero'] == agencia_numero), {})

def get_agencias() -> list[dict[str, int]]:
    '''
    Obter TODAS as agências.
    '''
    return agencias.copy()

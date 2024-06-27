'''
Model Agência

'id'    = PK - Primary Key: Chave Primária
'numero'= AK - Alternate Key: Chave Alternativa
'''

from src.model.agencia import Agencia, agencia_from_dict

AGENCIAS: list[dict[str, int]] = [
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

def get_agencia_by_id(agencia_id: int) -> Agencia:
    '''
    Obter uma agência pelo ID.
    '''
    data: dict[str, int] = next((a for a in AGENCIAS if a['id'] == agencia_id), {})
    return agencia_from_dict(data)

def get_agencia_by_numero(agencia_numero: int) -> Agencia:
    '''
    Obter uma agência pelo NÚMERO.
    '''
    data: dict[str, int] = next((a for a in AGENCIAS if a['numero'] == agencia_numero), {})
    return agencia_from_dict(data)

def get_agencias() -> list[Agencia]:
    '''
    Obter TODAS as agências.
    '''
    result: list[Agencia] = []
    for data in AGENCIAS:
        result.append(
            agencia_from_dict(data)
        )
    return result

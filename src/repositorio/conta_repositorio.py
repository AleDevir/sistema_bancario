'''
Model Conta
'id'    = PK - Primary Key: Chave Primária
'numero'= AK - Alternate Key: Chave Alternativa
'''
from typing import Optional
from src.model.conta import Conta, conta_from_dict

CONTAS: list[dict[str, int]] = [
    {
        'id': 1,
        'numero': 111111, 
        'digito': 11,
        'tipo': 1, # Conta Corrente
        'agencia_id': 1, 
        'usuario_id': 1, 
    },
    {
        'id': 2,
        'numero': 222222, 
        'digito': 22,
        'tipo': 2, # Conta Poupança
        'agencia_id': 1, 
        'usuario_id': 1, 
    },
    {
        'id': 3,
        'numero': 333333, 
        'digito': 33,
        'tipo': 1, # Conta Corrente
        'agencia_id': 2,
        'usuario_id': 2,
    },
    {
        'id': 4,
        'numero': 444444, 
        'digito': 44,
        'tipo': 1, # Conta Corrente
        'agencia_id': 1,
        'usuario_id': 3,
    },
    {
        'id': 5,
        'numero': 555555, 
        'digito': 55,
        'tipo': 2, # Conta Corrente
        'agencia_id': 2,
        'usuario_id': 4,
    },
    {
        'id': 6,
        'numero': 666666, 
        'digito': 66,
        'tipo': 2, # Conta Corrente
        'agencia_id': 3,
        'usuario_id': 5,
    },
    {
        'id': 7,
        'numero': 777777, 
        'digito': 77,
        'tipo': 2, # Conta Poupança
        'agencia_id': 1, 
        'usuario_id': 2, 
    },
]

def get_conta_by_id(conta_id: int) -> Optional[Conta]:
    '''
    Obter uma Conta pelo ID.
    '''
    data: dict[str, int] = next((c for c in CONTAS if c['id'] == conta_id), {})
    return conta_from_dict(data)

def get_conta_by_numero(conta_numero: int) -> Optional[Conta]:
    '''
    Obter uma Conta pelo NÚMERO.
    '''
    data: dict[str, int] = next((c for c in CONTAS if c['numero'] == conta_numero), {})
    return conta_from_dict(data)

def get_contas() -> list[Conta]:
    '''
    Obter TODAS as Contas.
    '''
    result: list[Conta] = []
    for data in CONTAS:
        result.append(
            conta_from_dict(data) # type: ignore[arg-type]
        )
    return result

def get_contas_da_agencia(agencia_id: int) -> list[Conta]:
    '''
    Obter Contas da Agência informada.
    '''
    contas_da_agencia = [c for c in CONTAS if c['agencia_id'] == agencia_id]
    return list(map(conta_from_dict, contas_da_agencia))  # type: ignore[arg-type]

def get_contas_do_usuario(usuario_id: int) -> list[Conta]:
    '''
    Obter Contas da Agência informada.
    '''
    contas_do_usuario = [c for c in CONTAS if c['usuario_id'] == usuario_id]
    result: list[Conta] = []
    for data in contas_do_usuario:
        result.append(
            conta_from_dict(data)  # type: ignore[arg-type]
        )
    return result

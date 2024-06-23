'''
Model Conta
'id'    = PK - Primary Key: Chave Primária
'numero'= AK - Alternate Key: Chave Alternativa
'''

contas: list[dict[str, int]] = [
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

def get_conta_by_id(conta_id: int) -> dict[str, int]:
    '''
    Obter uma Conta pelo ID.
    '''
    return next((c for c in contas if c['id'] == conta_id), {})

def get_conta_by_numero(conta_numero: int) -> dict[str, int]:
    '''
    Obter uma Conta pelo NÚMERO.
    '''
    return next((c for c in contas if c['numero'] == conta_numero), {})

def get_contas() -> list[dict[str, int]]:
    '''
    Obter TODAS as Contas.
    '''
    return contas.copy()

def get_contas_da_agencia(agencia_id: int) -> list[dict[str, int]]:
    '''
    Obter Contas da Agência informada.
    '''
    return [c for c in contas if c['agencia_id'] == agencia_id]

def get_contas_do_usuario(usuario_id: int) -> list[dict[str, int]]:
    '''
    Obter Contas da Agência informada.
    '''
    return [c for c in contas if c['usuario_id'] == usuario_id]

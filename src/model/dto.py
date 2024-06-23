'''
DTO - DATA TRANSFER OBJECT
'''

def new_dto(
    conta: dict[str, int],
    agencia: dict[str, int],
    usuario: dict[str, str | int]
) -> dict[str, str | int]:
    '''
    b
    '''
    return {
        # Conta
        'conta_id': conta['id'],
        'conta_numero': conta['numero'],
        'conta_digito': conta['digito'],
        # Agência
        'agencia_id': agencia['id'],
        'agencia_numero': agencia['numero'],
        'agencia_digito': agencia['digito'],
        # Usuário
        'usuario_id': usuario['id'],
        'usuario_nome': usuario['nome'],
    }

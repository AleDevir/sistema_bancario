'''
DTO - DATA TRANSFER OBJECT
'''

from src.model.agencia import Agencia
from src.model.conta import Conta
from src.model.usuario import Usuario

def new_dto(
    conta: Conta,
    agencia: Agencia,
    usuario: Usuario
) -> dict[str, str | int]:
    '''
    DTO = Data Transfer Object
    '''
    return {
        # Conta
        'conta_id': conta.id,
        'conta_numero': conta.numero,
        'conta_digito': conta.digito,
        # Agência
        'agencia_id': agencia.id,
        'agencia_numero': agencia.numero,
        'agencia_digito': agencia.digito,
        # Usuário
        'usuario_id': usuario.id,
        'usuario_nome': usuario.nome,
    }

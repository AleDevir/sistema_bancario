'''
DTO - DATA TRANSFER OBJECT
'''

from src.model.agencia import Agencia
from src.model.conta import Conta
from src.model.cliente import Cliente

def new_dto(
    conta: Conta,
    agencia: Agencia,
    cliente: Cliente
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
        # Cliente
        'cliente_id': cliente.id,
        'cliente_nome': cliente.nome,
    }

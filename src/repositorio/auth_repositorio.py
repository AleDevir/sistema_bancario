'''
Model Login
'''

from src.repositorio.agencia_repositorio import get_agencia_by_id
from src.repositorio.conta_repositorio import get_conta_by_numero
from src.repositorio.usuario_repositorio import get_usuario_by_id, senha_valida
from src.repositorio.dto import new_dto


def get_auth(conta_numero: int, senha: str) -> dict[str, int | str]:
    '''
    Obter Contas com sua Agência
    '''
    conta = get_conta_by_numero(conta_numero)

    if not conta:
        raise ValueError(f"Não foi possível obter a conta de número {conta_numero}!")
    # Esse tipo de consulta não deve ser feito em acesso à Base de Dados
    agencia = get_agencia_by_id(conta.agencia_id)
    if not agencia:
        raise ValueError(f"Não foi possível obter a agência da Conta de número {conta.numero} (ID={conta.id})!") # pylint: disable=line-too-long

    usuario = get_usuario_by_id(conta.usuario_id)
    if not usuario:
        raise ValueError(f"Não foi possível obter o usuário da Conta de número {conta.numero} (ID={conta.id})!") # pylint: disable=line-too-long

    if not senha_valida(int(usuario.id), senha):
        return {}
    return new_dto(conta, agencia, usuario)

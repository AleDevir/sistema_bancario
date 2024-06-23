'''
Model Login
'''

from src.model.agencia import get_agencia_by_id
from src.model.conta import get_conta_by_numero
from src.model.usuario import get_usuario_by_id, senha_valida
from src.model.dto import new_dto

def get_login(conta_numero: int, senha: str) -> dict[str, int | str]:
    '''
    Obter Contas com sua Agência
    '''
    conta = get_conta_by_numero(conta_numero)

    if not conta:
        raise ValueError(f"Não foi possível obter a conta de número {conta_numero}!")
    # Esse tipo de consulta não deve ser feito em acesso à Base de Dados
    agencia = get_agencia_by_id(conta.get('agencia_id', 0))
    if not agencia:
        raise ValueError(f"Não foi possível obter a agência da Conta de número {conta['numero']} (ID={conta['id']})!") # pylint: disable=line-too-long

    usuario = get_usuario_by_id(conta.get('usuario_id', 0))
    if not usuario:
        raise ValueError(f"Não foi possível obter o usuário da Conta de número {conta['numero']} (ID={conta['id']})!") # pylint: disable=line-too-long

    if not senha_valida(int(usuario['id']), senha):
        return {}
    return new_dto(conta, agencia, usuario)

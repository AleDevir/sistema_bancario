'''
Model Agência + Conta
'''

from src.model.agencia import get_agencia_by_id
from src.model.conta import get_contas_do_usuario
from src.model.usuario import get_usuario_by_id
from src.model.dto import new_dto

def get_contas_agencias_do_usuario(usuario_id: int) -> list[dict[str, str | int]]:
    '''
    Obter Contas com sua Agência
    '''
    result: list[dict[str, str | int]] = []
    contas = get_contas_do_usuario(usuario_id)
    for conta in contas:
        # Esse tipo de consulta não deve ser feito em acesso à Base de Dados
        agencia = get_agencia_by_id(conta.get('agencia_id', 0))
        if not agencia:
            raise ValueError(f"Não foi possível obter a agência da Conta de número {conta['numero']} (ID={conta['id']})!") # pylint: disable=line-too-long

        usuario = get_usuario_by_id(conta.get('usuario_id', 0))
        if not usuario:
            raise ValueError(f"Não foi possível obter o usuário da Conta de número {conta['numero']} (ID={conta['id']})!") # pylint: disable=line-too-long

        result.append(new_dto(conta, agencia, usuario))
        # result.append({
        #     # Conta
        #     'conta_id': conta['id'],
        #     'conta_numero': conta['numero'],
        #     'conta_digito': conta['digito'],
        #     # Agência
        #     'agencia_id': agencia['id'],
        #     'agencia_numero': agencia['numero'],
        #     'agencia_digito': agencia['digito'],
        #     # Usuário
        #     'usuario_id': usuario['id'],
        #     'usuario_nome': usuario['nome'],
        # })

    return result

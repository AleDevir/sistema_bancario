
'''
Regras de negócio - calculos de saldo
'''

from src.model.movimentacoes import Movimentacoes
from src.repositorio.movimentacoes_repositorio import get_movimentacao_financeira_do_usuario

##################################################
                     # SALDO  #
##################################################


def calcular_saldo_das_movimentacoes(movimentacoes: list[Movimentacoes]) -> float: # pylint: disable=line-too-long
    '''
    Calula o saldo de todas as movimentações.
    Retorna o saldo.
    '''
    saldo:list[float] = []
    for operacao in movimentacoes:
        valor:float = operacao.valor
        saldo.append(valor)
    return round(sum(saldo), 2)

def calcular_saldo_do_usuario(usuario_id: int ) -> float:
    '''
    Calcula o saldo do usuário.
    Retorna o saldo.
    '''
    movimentacoes_do_usuario = get_movimentacao_financeira_do_usuario(usuario_id)
    return calcular_saldo_das_movimentacoes(movimentacoes_do_usuario)

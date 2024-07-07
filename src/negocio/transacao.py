'''
Regras de negócio - para saque
'''

from datetime import datetime, date

from src.repositorio.movimentacoes_repositorio import(
    get_movimentacao_financeira_do_cliente
)

##################################################
     # VALIDAÇÕES DAS OPERAÇÕES DE SAQUE #
##################################################

def pode_sacar_hoje(conta_id: int) -> bool:
    '''
    Valida o limite de  três saques permitidos para o dia.
    '''
    inicio = datetime(date.today().year, date.today().month, date.today().day, 0, 0, 0)
    fim = datetime(date.today().year, date.today().month, date.today().day, 23, 59, 59)
    movimentacao_cliente = get_movimentacao_financeira_do_cliente(conta_id)
    saques = [m for m in movimentacao_cliente if m.valor < 0]
    saques_hoje = [s for s in saques if inicio <= s.date <= fim ]
    if len(saques_hoje) >= 3:
        return False
    return True

def validar_saque(saque: float, saldo: float) -> str:
    '''
    Recebe o saque e saldo para validar as ação de sacar. 
    Retorna a mensagem de erro para cada caso.
    '''
    if saque <= 0:
        return f"O valor do saque {saque} é inválido! O valor deve ser um número positivo."
    if saque > 500:
        return f"O valor {saque} excede o limite de saque diário (R$500,00)."
    if saque > saldo:
        return f"O valor {saque} excede o seu saldo atual R$ {saldo}."
    return ''

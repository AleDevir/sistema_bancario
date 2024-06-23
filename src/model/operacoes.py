'''
model das operções: saque, depósito, saldo e extrato.
'''
from typing import Final
from datetime import datetime, date
from src.model.movimentacoes import movimentacoes_finaceiras
from src.util.input_util import input_float
from src.util.console_util import (
    verde,
    vermelho,
    print_left,
)

LINHA_TRACEJADA: Final[str] = '-' * 71


##################################################
     # MOVIMENTAÇÃO  #
##################################################

def get_movimentacao_financeira_do_usuario(login: dict[str, str | int ]) -> list[dict]:
    '''
    Obtem dados da movimentação financeira do usuario(depósitos, saques e saldo)
    Retorna a movimentação.
    '''
    movimentacoes_do_usuario = [m for m in movimentacoes_finaceiras if m['usuario_id'] == login['usuario_id']] # pylint: disable=line-too-long
    return movimentacoes_do_usuario


def exibir_extrato(login: dict[str, str | int ]) -> None:
    '''
    Exibe toda a movimentação financeira(depósitos, saques e saldo atual) do usúario logado. 
    '''
    extrato = get_movimentacao_financeira_do_usuario(login)
    print(f"\n{LINHA_TRACEJADA}")
    print_left(f" Olá {str(login['usuario_nome']).title()}! Seu extrato ({datetime.now().strftime("%m-%d-%Y %H:%M:%S")}): \n\n") # pylint: disable=line-too-long
    for operacao in extrato:
        valor:float = operacao['valor']
        data: float = operacao['data']
        if valor < 0:
            print_left(f"Saque {vermelho(f'R${valor}')} Em: {data}\n")
        elif valor > 0:
            print_left(f"Depósito {verde(f'R${valor}')} Em: {data}\n")
    print(f"{LINHA_TRACEJADA}")
    print_left(f"Saldo R$ {calcular_saldo_do_usuario(login)}")
    print(f"{LINHA_TRACEJADA} \n")

def calcular_saldo_das_movimentacoes(movimentacoes: list[dict[str, str | datetime | float]]) -> float: # pylint: disable=line-too-long
    '''
    Calula o saldo de todas as movimentações.
    Retorna o saldo.
    '''
    saldo:list[float] = []
    for operacao in movimentacoes:
        valor:float = operacao['valor'] # type: ignore[assignment]
        saldo.append(valor)
    return round(sum(saldo), 2)

def calcular_saldo_do_usuario(login: dict[str, str | int ]) -> float:
    '''
    Calula o saldo do usuário.
    Retorna o saldo.
    '''
    movimentacoes_do_usuario = get_movimentacao_financeira_do_usuario(login)
    return calcular_saldo_das_movimentacoes(movimentacoes_do_usuario)


##################################################
     # VALIDAÇÕES DAS OPERAÇÕES #
##################################################

def pode_sacar_hoje(login: dict[str, str | int ]) -> bool:
    '''
    Valida o limite de  três saques permitidos para o dia.
    '''

    inicio = datetime(date.today().year, date.today().month, date.today().day, 0, 0, 0)
    fim = datetime(date.today().year, date.today().month, date.today().day, 23, 59, 59)
    movimentacao_usuario = get_movimentacao_financeira_do_usuario(login)
    saques = [m for m in movimentacao_usuario if m['valor'] < 0]
    saques_hoje = [s for s in saques if inicio <= s['data'] <= fim ]
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


##################################################
     # OPERAÇÕES FINANCEIRAS #
##################################################

def sacar(login: dict[str, str | int ]) -> None:
    '''
    Obtem o valor de saque inserido pelo usuário.
    Inseri o resultado na estrutura de dados.
    '''
    if not pode_sacar_hoje(login):
        print(vermelho('\n Você já atingiu o limite de saques por dia!\n')) # pylint: disable=line-too-long
        return

    saldo = calcular_saldo_do_usuario(login)
    while True:
        saque = input_float("Entre com o valor do saque R$: ")
        saque_invalido = validar_saque(saque, saldo)
        if saque_invalido:
            print(f"\n{vermelho(saque_invalido)}\n")
        else:
            movimentacoes_finaceiras.append({
                'valor': -saque,
                'data': datetime.now(),
                'usuario_id': int(login['usuario_id']),         
            })
            saldo = calcular_saldo_do_usuario(login)
            print(f"Saldo R$ {saldo}")
            break

def depositar(login: dict[str, str | int ]) -> None:
    '''
    Deposita valores positivos na conta.
    '''
    while True:
        deposito = input_float("\nEntre com o valor do depósito R$: ")
        if deposito <= 0:
            print(vermelho(f'\nValor {deposito} inválido! Por favor tente novamente.\n')) # pylint: disable=line-too-long
        else:
            if deposito:
                movimentacoes_finaceiras.append({
                    'valor': deposito,
                    'data': datetime.now(),
                    'usuario_id': int(login['usuario_id'])
                })
            saldo = calcular_saldo_do_usuario(login)
            print(f"Saldo R$ {saldo}")
            break

'''
A princípio TUDO da main vem pra cá.

O def main será renomeado para caixa_eletronico
'''

import getpass
from datetime import datetime
from typing import Final
from src.util.console_util import (
    verde,
    vermelho,
    bright_amarelo,
    print_left,
    print_center,
    limpar_console
)
from src.util.menu_util import exibir_menu
from src.util.input_util import input_opcoes, input_int
from src.repositorio.auth_repositorio import get_auth
from src.repositorio.movimentacoes_repositorio import (
    add_movimentacao,
    get_movimentacao_financeira_do_usuario,
)
from src.negocio.saldo import  calcular_saldo_do_usuario
from src.negocio.transacao import pode_sacar_hoje, validar_saque
from src.util.input_util import input_float



LINHA_TRACEJADA: Final[str] = '-' * 71
#################################################
    # INFRAESTRUTURA #
#################################################

def get_input(msg: str) -> str:
    '''
    Encapsula as chamadas dos inputs.
    Confeccionada para poder mokar os testes.
    '''
    return input(msg)

def get_senha(msg: str) -> str:
    '''
    Encapsula a chamada do getpass.
    Confeccionada para poder mokar os testes.
    '''
    return getpass.getpass(msg)

##################################################
        # CREDENCIAS - ENTRADA NO SISTEMA #
##################################################

def get_auth_na_conta() -> dict[str, str | int]:
    '''
    Obtem um usuário cadastrado.
    Retorna o usuário.
    '''
    auth: dict[str, str | int ] = {}
    while not auth:
        conta_numero = input_int("\n Conta Corrente: ")
        senha_informada = get_senha(" Senha: " )
        print(f"conta: {conta_numero} e senha: {senha_informada}")
        auth = get_auth(conta_numero, senha_informada)
        print(f"auth: {auth} ")
        if not auth:
            print(vermelho('\n Credênciais inválidas! Por favor tente novamente.')) # pylint: disable=line-too-long
    return auth

def exibir_mensagem_de_boas_vindas(
    nome_do_usuario: str,
    hora_atual: datetime = datetime.now()
) -> None:
    '''
    Exibe uma mensagem de boas-vindas para o usuário da conta.
    '''
    print_center(bright_amarelo("Banco Feliz :)"), 40)
    if hora_atual.hour < 12:
        print_left(bright_amarelo(f"\n Bom dia, {nome_do_usuario.title()}! \n"))
    elif 12 <= hora_atual.hour < 18:
        print_left(bright_amarelo(f"\n Boa tarde, {nome_do_usuario.title()}! \n"))
    else:
        print_left(bright_amarelo(f"\n Bom noite, {nome_do_usuario.title()}! \n"))

##################################################
                  # EXTRATO  #
##################################################

def exibir_extrato(usuario_id: int) -> None:
    '''
    Exibe toda a movimentação financeira(depósitos, saques e saldo atual) do usúario logado. 
    '''
    extrato = get_movimentacao_financeira_do_usuario(usuario_id)
    print(f"\n{LINHA_TRACEJADA}")
    for operacao in extrato:
        valor:float = operacao.valor
        data: datetime = operacao.date
        if valor < 0:
            print_left(f"Saque {vermelho(f'R${valor}')} Em: {data}\n")
        elif valor > 0:
            print_left(f"Depósito {verde(f'R${valor}')} Em: {data}\n")
    print(f"{LINHA_TRACEJADA}")
    print_left(f"Saldo R$ {calcular_saldo_do_usuario(usuario_id)}")
    print(f"{LINHA_TRACEJADA} \n")

##################################################
     # OPÇOES DO MENU #
##################################################

opcoes_do_menu_entrada:  dict[str, str ] = {
        'E': 'Extrato',
        'D': 'Depósito',
        'S': 'Saque', 
        'F': 'Finalizar e sair da conta.',
}

siglas_das_opcoes_menu_entrada: list[str] = list(opcoes_do_menu_entrada)

def escolher_uma_opcao_do_menu_entrada() -> str:
    '''
    Escolhe uma opção do menu.
    Retorna uma das opções do menu: ['E', D', 'S', 'F'].
    '''
    exibir_menu(opcoes_do_menu_entrada)
    escolher_opcao = input_opcoes('Entre com a opção desejada: ', siglas_das_opcoes_menu_entrada).upper() # pylint: disable=line-too-long
    while escolher_opcao not in siglas_das_opcoes_menu_entrada:
        print(f"\n Opção '{vermelho(escolher_opcao)}' inválida! As opções válidas são: {verde(', '.join(siglas_das_opcoes_menu_entrada))} \n") # pylint: disable=line-too-long
        escolher_opcao = input_opcoes(
            'Entre com a opção desejada: ',
             siglas_das_opcoes_menu_entrada
        ).upper()
    return escolher_opcao

##################################################
     # OPERAÇÕES FINANCEIRAS #
##################################################

def sacar(usuario_id: int) -> None:
    '''
    Obtem o valor de saque inserido pelo usuário.
    Inseri o resultado na estrutura de dados.
    '''
    if not pode_sacar_hoje(usuario_id):
        print(vermelho('\n Você já atingiu o limite de saques por dia!\n')) # pylint: disable=line-too-long
        return

    saldo = calcular_saldo_do_usuario(usuario_id)
    while True:
        saque = input_float("Entre com o valor do saque R$: ")
        saque_invalido = validar_saque(saque, saldo)
        if saque_invalido:
            print(f"\n{vermelho(saque_invalido)}\n")
        else:
            add_movimentacao(-saque, usuario_id)
            saldo = calcular_saldo_do_usuario(usuario_id)
            print(f"Saldo R$ {saldo}")
            break

def depositar(usuario_id: int) -> None:
    '''
    Deposita valores positivos na conta.
    '''
    while True:
        deposito = input_float("\nEntre com o valor do depósito R$: ")
        if deposito <= 0:
            print(vermelho(f'\nValor {deposito} inválido! Por favor tente novamente.\n')) # pylint: disable=line-too-long
        else:
            if deposito:
                add_movimentacao(deposito, usuario_id)
            saldo = calcular_saldo_do_usuario(usuario_id)
            print(f"Saldo R$ {saldo}")
            break

##################################################
     # FLUXO PRINCIPAL DA APP #
##################################################

def caixa_eletronico() -> None:
    '''
    Fluxo Principal do Programa.
    '''
    limpar_console()
    auth = get_auth_na_conta()
    limpar_console()
    exibir_mensagem_de_boas_vindas(str(auth['usuario_nome']))
    while True:
        opcao = escolher_uma_opcao_do_menu_entrada()
        if opcao == "E":
            exibir_extrato(int(auth['usuario_id']))
        if opcao == "D":
            depositar(int(auth['usuario_id']))
        if opcao == "S":
            sacar(int(auth['usuario_id']))
        if opcao == "F":
            print_center(bright_amarelo(" Banco Feliz :)\n"), 40)
            print_center(bright_amarelo(f"Até breve {str(auth['usuario_nome']).title()}."), 30)
            break
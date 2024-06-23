'''
Módulo com fluxo principal do programa.
  
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
from src.model.operacoes import sacar, depositar, exibir_extrato
from src.model.login import get_login

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

def get_login_na_conta() -> dict[str, str | int]:
    '''
    Obtem um usuário cadastrado.
    Retorna o usuário.
    '''
    login: dict[str, str | int ] = {}
    while not login:
        conta_numero = input_int("\n Conta Corrente: ")
        senha_informada = get_senha(" Senha: " )
        login = get_login(conta_numero, senha_informada)
        if not login:
            print(vermelho('\n Credênciais inválidas! Por favor tente novamente.')) # pylint: disable=line-too-long
    return login

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
     # OPÇOES DE CONTA E OPERAÇÕES #
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

def main() -> None:
    '''
    Fluxo Principal do Programa.
    '''
    limpar_console()
    login = get_login_na_conta()
    limpar_console()
    exibir_mensagem_de_boas_vindas(str(login['usuario_nome']))
    while True:
        opcao = escolher_uma_opcao_do_menu_entrada()
        if opcao == "E":
            exibir_extrato(login)
        if opcao == "D":
            depositar(login)
        if opcao == "S":
            sacar(login)
        if opcao == "F":
            print_center(bright_amarelo(" Banco Feliz :)\n"), 40)
            print_center(bright_amarelo(f"Até breve, {str(login['usuario_nome']).title()}."), 30)
            break

if __name__ == "__main__":
    main()

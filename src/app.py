'''
Aplicação do sistema bancário
'''

import getpass
from datetime import datetime
from typing import Final
import locale
from src.util.console_util import (
    verde,
    vermelho,
    bright_amarelo,
    print_left,
    print_center,
    limpar_console
)
from src.util.menu_util import escolher_uma_opcao_do_menu_entrada
from src.util.input_util import input_int, input_float
from src.auth.authentication import get_auth
from src.repositorio.movimentacoes_repositorio import (
    add_movimentacao,
    get_movimentacao_financeira_do_cliente,
)
from src.negocio.saldo import  calcular_saldo_do_cliente
from src.negocio.transacao import pode_sacar_hoje, validar_saque
from src.util.execptions import AuthException
from src.util.data_e_hora_util import exibir_data_e_hora, formatar_data_e_hora



LINHA_TRACEJADA: Final[str] = '-' * 51
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

def timestamp(funcao):
    '''
    Função decoradora para exibir a data e a hora.
    '''
    def envelope(*args, **kwargs) -> None:
        '''
        Função envelope
        '''
        funcao(*args, **kwargs)

        # Pegar cliente_id tanto argumento posicional como argumento nomeado.
        cliente_id: int = kwargs.get('cliente_id', 0) if 'cliente_id' in kwargs else args[0]
        saldo = calcular_saldo_do_cliente(cliente_id)
        print(f"Saldo {formatar_valor_monetario(saldo)}")
        exibir_data_e_hora()

    return envelope


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def formatar_valor_monetario(valor:float) -> str:
    '''
    Formata um valor para  moeda corrente.
    '''
    moeda_formatada = locale.currency(valor, grouping=True)
    return moeda_formatada
   
##################################################
        # CREDENCIAS - ENTRADA NO SISTEMA #
##################################################

def get_auth_na_conta() -> dict[str, str | int]:
    '''
    Obtem uma conta cadastrada.
    Retorna a conta.
    '''
    auth: dict[str, str | int ] = {}
    while not auth:
        conta_numero = input_int("\n Conta Corrente: ")
        senha_informada = get_senha(" Senha: " )
        try:
            auth = get_auth(conta_numero, senha_informada)
        except AuthException:
            print(vermelho('\nCredênciais inválidas! Por favor tente novamente.')) # pylint: disable=line-too-long

    return auth

def exibir_mensagem_de_boas_vindas(
    nome_do_cliente: str,
    hora_atual: datetime = datetime.now()
) -> None:
    '''
    Exibe uma mensagem de boas-vindas para o usuário da conta.
    '''
    print_center(bright_amarelo("Banco Feliz :)"), 40)
    if hora_atual.hour < 12:
        print_left(bright_amarelo(f"\n Bom dia, {nome_do_cliente.title()}! \n"))
    elif 12 <= hora_atual.hour < 18:
        print_left(bright_amarelo(f"\n Boa tarde, {nome_do_cliente.title()}! \n"))
    else:
        print_left(bright_amarelo(f"\n Bom noite, {nome_do_cliente.title()}! \n"))

##################################################
                  # EXTRATO  #
##################################################

@timestamp
def exibir_extrato(cliente_id: int) -> None:
    '''
    Exibe toda a movimentação financeira(depósitos, saques e saldo atual) do usúario logado. 
    '''
    extrato = get_movimentacao_financeira_do_cliente(cliente_id)
    print(f"\n{LINHA_TRACEJADA}")
    for operacao in extrato:
        valor:float = operacao.valor
        data: datetime = operacao.date
        if valor < 0:
            print_left(f"Saque {vermelho(f'{formatar_valor_monetario(valor)}')} Em: {formatar_data_e_hora(data)}\n") # pylint: disable=line-too-long
        elif valor > 0:
            print_left(f"Depósito {verde(f'{formatar_valor_monetario(valor)}')} Em: {formatar_data_e_hora(data)}\n") # pylint: disable=line-too-long
    print(f"{LINHA_TRACEJADA}")


##################################################
     # OPÇOES DO MENU CLIENTE #
##################################################

opcoes_do_menu_entrada:  dict[str, str ] = {
        'E': 'Extrato',
        'D': 'Depósito',
        'S': 'Saque', 
        'F': 'Finalizar e sair da conta.',
}

##################################################
     # OPERAÇÕES FINANCEIRAS #
##################################################

@timestamp
def sacar(conta_id: int) -> None:
    '''
    Obtem o valor de saque inserido pelo cliente.
    Inseri o resultado na estrutura de dados.
    '''
    if not pode_sacar_hoje(conta_id):
        print(vermelho('\n Você já atingiu o limite de saques por dia!\n')) # pylint: disable=line-too-long
        return

    saldo = calcular_saldo_do_cliente(conta_id)
    while True:
        saque = input_float("Entre com o valor do saque R$: ")
        saque_invalido = validar_saque(saque, saldo)
        if saque_invalido:
            print(f"\n{vermelho(saque_invalido)}\n")
        else:
            add_movimentacao(-saque, conta_id)
            break

@timestamp
def depositar(conta_id: int) -> None:
    '''
    Deposita valores positivos na conta.
    '''
    while True:
        deposito = input_float("\nEntre com o valor do depósito R$: ")
        if deposito <= 0:
            print(vermelho(f'\nValor {deposito} inválido! Por favor tente novamente.\n')) # pylint: disable=line-too-long
        else:
            if deposito:
                add_movimentacao(deposito, conta_id)
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
    exibir_mensagem_de_boas_vindas(str(auth['cliente_nome']))
    while True:
        opcao = escolher_uma_opcao_do_menu_entrada(opcoes_do_menu_entrada)
        if opcao == "E":
            exibir_extrato(int(auth['conta_id']))
        if opcao == "D":
            depositar(int(auth['conta_id']))
        if opcao == "S":
            sacar(int(auth['conta_id']))
        if opcao == "F":
            print_center(bright_amarelo(" Banco Feliz :)\n"), 40)
            print_center(bright_amarelo(f"Até breve {str(auth['cliente_nome']).title()}."), 30)
            break

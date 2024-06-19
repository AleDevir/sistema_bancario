'''
    - Operação de Depósito -> Realizar depósitos para conta bancária. 
        O programa nesta versão só possui um usuário.
    - Operação de Saque -> Possibilidade de realizar três saques diários, com limite 
        máximo de R$ 500,00 por saque.
        Caso não possui limite, uma mensagem deve ser exibida avisando a falta de saldo.
    - Operação de Extrato -> listar todos os depósitos e saques realizados na conta. 
        o final informa o saldo atual.
'''

import getpass
from datetime import datetime, date
from typing import Final
import bcrypt
from util.console_util import (
    verde,
    vermelho,
    bright_amarelo,
    print_left,
    print_center,
    limpar_console
)
from util.menu_util import exibir_menu
from util.input_util import input_opcoes, input_float

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
     # ESTRUTURA DE DADOS #
##################################################

usuarios:  list[dict[str, str | int | bytes ]] = [
    {
        'nome': 'ri',
        'id': 1,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()),    
    },
    {
        'nome': 'ale',
        'id': 2,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()), 
    },
    {
        'nome': 'test',
        'id': 3,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()), 
    },
    {
        'nome': 'test',
        'id': 4,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()), 
    },
    {
        'nome': 'test',
        'id': 5,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()), 
    },
]

movimentacoes_finaceiras: list[dict[str, str | datetime | float]] = [
    {
        'valor': 15.2,
        'data': datetime(2019, 2, 12, 12, 14, 00),
        'usuario_id': 1,
    },
    {
        'valor': 25.0,
        'data': datetime(2020, 5, 10, 23, 10, 00),
        'usuario_id': 1,   
    },
    {
        'valor': 100.0,
        'data': datetime(2020, 4, 17, 15, 10, 00),
        'usuario_id': 2,   
    },
    {
        'valor': -10.0,
        'data': datetime.now(),
        'usuario_id': 2,
    },
    {
        'valor': -15.00,
        'data': datetime.now(),
        'usuario_id': 2,  
    },
    {
        'valor': -10.50,
        'data': datetime(2021, 6, 11, 18, 10, 00),
        'usuario_id': 1,
    },
    {
        'valor': -30.55,
        'data': datetime.now(),
        'usuario_id': 3,
    },
    {
        'valor': -15.50,
        'data': datetime.now(),
        'usuario_id': 3,
    },
    {
        'valor': -35.00,
        'data': datetime.now(),
        'usuario_id': 3,
    },
    {
        'valor': -53.00,
        'data': datetime(2021, 6, 10, 15, 10, 00),
        'usuario_id': 3,
    },
    {
        'valor': 330.90,
        'data': datetime(2021, 6, 12, 12, 10, 00),
        'usuario_id': 3,
    },
    {
        'valor': 500,
        'data': datetime(2021, 6, 9, 23, 10, 00),
        'usuario_id': 4,
    },
    {
        'valor': 500,
        'data': datetime(2021, 8, 11, 18, 10, 00),
        'usuario_id': 5,
    },
]

##################################################
     # USUÁRIO #
##################################################

def obter_usuario() -> dict[str, str | int | bytes ]:
    '''
    Obtem um usuário cadastrado.
    Retorna o usuário.
    '''
    usuario: dict[str, str | int | bytes ] = {}
    while not usuario:
        nome_informado = get_input("\n Nome: ")
        senha_informada = get_senha(" Senha: " )
        usuario = next((u for u in usuarios if str(u['nome']).lower() ==  nome_informado.lower()), {}) # pylint: disable=line-too-long
        if not usuario:
            print(vermelho('\n Credênciais inválidas! Por favor tente novamente.')) # pylint: disable=line-too-long
        elif not bcrypt.checkpw(senha_informada.encode(), usuario['senha']): # type: ignore[arg-type] # pylint: disable=line-too-long
            usuario = {}
            print(vermelho('\n Credênciais inválidas! Por favor tente novamente.')) # pylint: disable=line-too-long
    return usuario

def exibir_mensagem_de_boas_vindas(
    nome_do_usuario: str,
    hora_atual: datetime = datetime.now()
) -> None:
    '''
    Exibe uma mensagem de boas-vindas para o usuário da conta.
    '''
    if hora_atual.hour < 12:
        print_left(f"\n Bom dia :) {nome_do_usuario.capitalize()}! \n")
    elif 12 <= hora_atual.hour < 18:
        print_left(f"\n Boa tarde :) {nome_do_usuario.capitalize()}! \n")
    else:
        print_left(f"\n Boa noite :) {nome_do_usuario.capitalize()}! \n")

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


##################################################
     # MOVIMENTAÇÃO  #
##################################################

def obter_movimentacao_financeira_do_usuario(usuario: dict[str, str | int | bytes ]) -> list[dict]:
    '''
    Obtem dados da movimentação financeira do usuario(depósitos, saques e saldo)
    Retorna a movimentação.
    '''
    movimentacoes_do_usuario = [m for m in movimentacoes_finaceiras if m['usuario_id'] == usuario['id']] # pylint: disable=line-too-long
    return movimentacoes_do_usuario

def exibir_extrato(usuario: dict[str, str | int | bytes ]) -> None:
    '''
    Exibe toda a movimentação financeira(depósitos, saques e saldo atual) do usúario logado. 
    '''
    extrato = obter_movimentacao_financeira_do_usuario(usuario)
    print(f"\n{LINHA_TRACEJADA}")
    print_left(f" Olá {str(usuario['nome']).capitalize()}! Seu extrato ({datetime.now().strftime("%m-%d-%Y %H:%M:%S")}): \n\n") # pylint: disable=line-too-long
    for operacao in extrato:
        valor:float = operacao['valor']
        data: float = operacao['data']
        if valor < 0:
            print_left(f"Saque {vermelho(f'R${valor}')} Em: {data}\n")
        elif valor > 0:
            print_left(f"Depósito {verde(f'R${valor}')} Em: {data}\n")
    print(f"{LINHA_TRACEJADA}")
    print_left(f"Saldo R$ {calcular_saldo_do_usuario(usuario)}")
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

def calcular_saldo_do_usuario(usuario: dict[str, str | int | bytes ]) -> float:
    '''
    Calula o saldo do usuário.
    Retorna o saldo.
    '''
    movimentacoes_do_usuario = obter_movimentacao_financeira_do_usuario(usuario)
    return calcular_saldo_das_movimentacoes(movimentacoes_do_usuario)


##################################################
     # VALIDAÇÕES DAS OPERAÇÕES #
##################################################

def pode_sacar_hoje(usuario: dict[str, str | int | bytes ]) -> bool:
    '''
    Valida o limite de  três saques permitidos para o dia.
    '''

    inicio = datetime(date.today().year, date.today().month, date.today().day, 0, 0, 0)
    fim = datetime(date.today().year, date.today().month, date.today().day, 23, 59, 59)
    movimentacao_usuario = obter_movimentacao_financeira_do_usuario(usuario)
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

def sacar(usuario: dict[str, str | int | bytes ]) -> None:
    '''
    Obtem o valor de saque inserido pelo usuário.
    Inseri o resultado na estrutura de dados.
    '''
    if not pode_sacar_hoje(usuario):
        print(vermelho('\n Você já atingiu o limite de saques por dia!\n')) # pylint: disable=line-too-long
        return

    saldo = calcular_saldo_do_usuario(usuario)
    while True:
        saque = input_float("Entre com o valor do saque R$: ")
        saque_invalido: float = validar_saque(saque, saldo)
        if saque_invalido:
            print(f"\n{vermelho(saque_invalido)}\n")
        else:
            movimentacoes_finaceiras.append({
                'valor': -saque,
                'data': datetime.now(),
                'usuario_id': int(usuario['id']),         
            })
            saldo = calcular_saldo_do_usuario(usuario)
            print(f"Saldo R$ {saldo}")
            break

def depositar(usuario: dict[str, str | int | bytes ]) -> None:
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
                    'usuario_id': int(usuario['id'])
                })
            saldo = calcular_saldo_do_usuario(usuario)
            print(f"Saldo R$ {saldo}")
            break

def main() -> None:
    '''
    Fluxo Principal do Programa.
    '''
    limpar_console()
    usuario = obter_usuario()
    limpar_console()
    exibir_mensagem_de_boas_vindas(str(usuario['nome']))
    while True:
        opcao = escolher_uma_opcao_do_menu_entrada()
        if opcao == "E":
            exibir_extrato(usuario)
        if opcao == "D":
            depositar(usuario)
        if opcao == "S":
            sacar(usuario)
        if opcao == "F":
            print_center(bright_amarelo(f"Até breve, {str(usuario['nome']).capitalize()} :)"), 40)
            break

if __name__ == "__main__":
    main()

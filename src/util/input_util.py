'''
Módulo Utilitário das operações de input do console.
'''
from src.util.console_util import vermelho, verde

def get_input(msg: str) -> str:
    '''
    Encapsula as chamadas dos inputs.
    Confecionda para poder testar os inputs.
    '''
    return input(msg)


def input_opcoes(msg: str, opcoes: list[str]) -> str:
    '''
    Obtem a opção válida.
    Retorna a opção.
    '''
    while True:
        opcao = get_input(msg).upper()
        if opcao in opcoes:
            return opcao
        print(f"'{vermelho(opcao)}' Opção inválida! As opções válidas são: {verde(', '.join(opcoes))}") # pylint: disable=line-too-long

def input_int(msg: str) -> int:
    '''
    Obtem número inteiro informado pelo usuário.
    Retorna o número.
    '''
    while True:
        try:
            return int(get_input(msg))
        except ValueError:
            print(vermelho('Apenas números inteiros são aceitos. Por favor, tente novamente.\n'))

def input_float(msg: str) -> float:
    '''
    Obtem número inteiro informado pelo usuário.
    Retorna o número.
    '''
    while True:
        try:
            return float(get_input(msg))
        except ValueError:
            print(vermelho('Apenas números são aceitos. Por favor, tente novamente.\n'))

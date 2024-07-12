'''
Módulo Utilitário de menu.
'''
from typing import Final
from src.util.console_util import verde, vermelho, print_left
from src.util.input_util import input_opcoes

LINHA_TRACEJADA: Final[str] = '-' * 51


def exibir_menu(opcoes: dict[str, str]) -> None:
    '''
    Exibi o menu de opções.
    '''
    print('')
    print(verde(LINHA_TRACEJADA))
    menu = 'MENU DE OPÇÕES \n'
    print(verde(menu.center(50)))

    for key, value in opcoes.items():
        opcao = '|' + key + '|' + "  "  + value
        print_left(f"{verde(opcao)} ")
    print(verde(LINHA_TRACEJADA))


def escolher_uma_opcao_do_menu_entrada(opcoes_menu_dict: dict[str, str]) -> str:
    '''
    Escolhe uma opção do menu.
    Retorna uma das opções do menu.
    '''
    exibir_menu(opcoes_menu_dict)
    siglas: list[str] = list(opcoes_menu_dict)
    escolher_opcao = input_opcoes('Entre com a opção desejada: ', siglas).upper() # pylint: disable=line-too-long
    while escolher_opcao not in siglas:
        print(f"\n Opção '{vermelho(escolher_opcao)}' inválida! As opções válidas são: {verde(', '.join(siglas))} \n") # pylint: disable=line-too-long
        escolher_opcao = input_opcoes(
            'Entre com a opção desejada: ',
             siglas
        ).upper()
    return escolher_opcao

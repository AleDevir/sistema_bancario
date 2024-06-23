'''
Módulo Utilitário de menu.
'''
from typing import Final
from src.util.console_util import verde, print_left

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

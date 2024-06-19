'''
Módulo Utilitário das operações de console.

Links úteis:
. Cores no console:
https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
. Limpar console (clear_output):
https://notebook.community/CestDiego/emacs-ipython-notebook/tests/notebook/nbformat4/Animations%20Using%20clear_output
'''

import os
import platform
from typing import Final
from typing import Any


COR_BRANCA: Final[str] = '\033[0;0m'
COR_BRIGHT_AMARELA: Final[str] = '\033[93m'
COR_VERDE: Final[str] = '\033[32m'
COR_VERMELHA: Final[str] = '\033[31m'


# Habilita os caracteres ANSI escape no terminal Windows.
os.system("")

def bright_amarelo(conteudo: Any) -> Any:
    '''
    Colore o texto informado em amarelo brilhante.
    Retorna o texto colorido.
    '''
    return f"{COR_BRIGHT_AMARELA}{conteudo}{COR_BRANCA}"

def verde(conteudo: Any) -> Any:
    '''
    Colore o texto informado em verde.
    Retorna o texto colorido.
    '''
    return f"{COR_VERDE}{conteudo}{COR_BRANCA}"

def vermelho(conteudo: Any) -> Any:
    '''
    Colore o texto informado em vermelho.
    Retorna o texto colorido.
    '''
    return f"{COR_VERMELHA}{conteudo}{COR_BRANCA}"

def limpar_console():
    '''
    Limpa o console de acordo com a plataforma.
    '''
    if platform.system() == 'Windows':
        os.system('cls')
    if platform.system() == 'Linux':
        os.system('clear')

def print_left(conteudo: str, justificado: int = 2) -> None:
    '''
    Recebe a posição do alinhamento e o tamanho do mesmo.
    '''
    espassos = " ".ljust(justificado)
    print(espassos, conteudo)

def print_center(conteudo: str, justificado: int) -> None:
    '''
    Recebe a posição do alinhamento e o tamanho do mesmo.
    '''
    espassos = " ".center(justificado)
    print(espassos, conteudo)

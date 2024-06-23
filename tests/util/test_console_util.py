'''
Testes do módulo console_util.py
pytest tests/util/test_console_util.py -vv
'''
from src.util.console_util import(
    limpar_console,
    verde,
    bright_amarelo,
    vermelho,
    COR_BRANCA,
    COR_VERDE,
    COR_BRIGHT_AMARELA,
    COR_VERMELHA,
    print_center,
    print_left
)

def test_limpar_console():
    '''
    Testa a exibição de menu.
    pytest tests/util/test_console_util.py::test_limpar_console -vv
    '''
    limpar_console()
    assert True

def test_conteudo_verde():
    '''
    Testa a função de colorir conteudo.
    pytest tests/util/test_console_util.py::test_conteudo_verde -vv
    '''
    text = 'texto'
    resposta = f"{COR_VERDE}{text}{COR_BRANCA}"
    coloracao_valida = verde(text)
    assert coloracao_valida == resposta

def test_conteudo_bright_amarelo():
    '''
    Testa a função de colorir conteudo.
    pytest tests/util/test_console_util.py::test_conteudo_bright_amarelo -vv
    '''
    text = 'texto'
    resposta = f"{COR_BRIGHT_AMARELA}{text}{COR_BRANCA}"
    coloracao_valida = bright_amarelo(text)
    assert coloracao_valida == resposta

def test_conteudo_vermelho():
    '''
    Testa a função de colorir conteudo.
    pytest tests/util/test_console_util.py::test_conteudo_vermelho -vv
    '''
    text = 'texto'
    resposta = f"{COR_VERMELHA}{text}{COR_BRANCA}"
    coloracao_valida = vermelho(text)
    assert coloracao_valida == resposta

def test_print_center():
    '''
    Testa a função de imprimir conteúdo no centro.
    pytest tests/util/test_console_util.py::test_print_center -vv
    '''
    texto = 'texto'
    print_center(texto, 10)
    assert True

def test_print_left():
    '''
    Testa a função de imprimir conteúdo com espaços a esquerda.
    pytest tests/util/test_console_util.py::test_print_left -vv
    '''
    texto = 'texto'
    print_left(texto, 10)
    assert True

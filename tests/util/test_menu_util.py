'''
Testes do módulo menu_util.py
pytest tests/util/test_menu_util.py -vv
'''
from util.menu_util import exibir_menu

def test_exibir_menu():
    '''
    Testa a exibição de menu.
    pytest tests/util/test_menu_util.py::test_exibir_menu -vv
    '''
    opcoes = {
        'A': 'A TESTE',
        'C': 'C TESTE',
        'D': 'D TESTE'
    }
    exibir_menu(opcoes)
    assert True

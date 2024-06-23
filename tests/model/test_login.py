# pylint: disable=line-too-long
'''
Testes do model login.py
pytest tests/model/test_login.py -vv
'''

from src.model.login import(
    get_login
)

def test_login():
    '''
    Teste do metodo get_usuario_by_id
    pytest tests/model/test_login.py::test_login -vv
    '''
    
    senha = '123'
    conta_numero = 777777
    login = get_login(conta_numero, senha)
    assert login
    assert 'conta_numero' in login
    assert login['conta_numero'] == conta_numero

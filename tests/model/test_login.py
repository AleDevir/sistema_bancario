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
    usuario = {
        'senha': '123'
    }
    conta = {
        'numero': 777777,
    }
    login = get_login(conta['numero'], usuario['senha'])
    assert login

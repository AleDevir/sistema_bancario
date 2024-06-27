# pylint: disable=line-too-long
'''
Testes do repositorio login.py
pytest tests/repositorio/test_auth.py -vv
'''
import pytest
from src.repositorio.auth_repositorio import(
    get_auth
)

def test_auth():
    '''
    Teste do metodo get_auth
    pytest tests/repositorio/test_auth.py::test_auth -vv
    '''
    senha = '123'
    conta_numero = 777777
    auth = get_auth(conta_numero, senha)
    assert auth
    assert 'conta_numero' in auth
    assert auth['conta_numero'] == conta_numero

def test_auth_error():
    '''
    Teste do metodo get_auth
    pytest tests/repositorio/test_auth.py::test_auth_error -vv
    '''
    senha = '123'
    conta_numero = 8577777
    erro = f"Não foi possível obter a conta de número {conta_numero}!"
    with pytest.raises(ValueError, match=erro):
        get_auth(conta_numero, senha)


def test_auth_error_manual():
    '''
    Teste do metodo get_auth
    pytest tests/repositorio/test_auth.py::test_auth_error_manual -vv
    '''
    senha = '123'
    conta_numero = 8577777
    try:
        get_auth(conta_numero, senha)
        assert False
    except ValueError as error:
        assert True
        assert str(error) ==f"Não foi possível obter a conta de número {conta_numero}!"

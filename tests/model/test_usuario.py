# pylint: disable=line-too-long
'''
Testes do model usuario.py
pytest tests/model/test_usuario.py -vv
'''

from src.model.usuario import(
    get_usuario_by_id,
    get_usuario_by_nome,
    get_usuarios,
    senha_valida
)

def test_get_usuario_by_id():
    '''
    Teste do metodo get_usuario_by_id
    pytest tests/test_usuario.py::test_get_usuario_by_id -vv
    '''
    usuario = {
        'id': 1
    }
    usuario = get_usuario_by_id(usuario['id'])
    assert usuario

def test_get_usuario_by_nome():
    '''
    Teste do metodo get_usuario_by_nome
    pytest tests/test_usuario.py::test_get_usuario_by_id -vv
    '''
    usuario = {
        'nome': 'rinaldo benevies'
    }
    usuario = get_usuario_by_nome(usuario['nome'])
    assert usuario

def test_get_usuarios():
    '''
    Teste do metodo get_usuarios
    pytest tests/test_usuario.py::test_get_usuarios -vv
    '''
    get_usuarios()
    assert True

def test_senha_valida():
    '''
    Teste do metodo senha_valida
    pytest tests/test_usuario.py::test_senha_valida -vv
    '''
    usuario = {
        'id':1,
        'senha': '123'
    }
    teste_de_senha_valida = senha_valida(usuario['id'], usuario['senha'])
    assert teste_de_senha_valida

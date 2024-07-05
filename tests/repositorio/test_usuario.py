# pylint: disable=line-too-long
'''
Testes do repositorio usuario.py
pytest tests/repositorio/test_usuario.py -vv
'''

from src.repositorio.cliente_repositorio import(
    get_usuario_by_id,
    get_usuario_by_nome,
    get_usuarios,
    senha_valida
)

def test_get_usuario_by_id():
    '''
    Teste do metodo get_usuario_by_id
    pytest tests/repositorio/test_usuario.py::test_get_usuario_by_id -vv
    '''
    usuario_id = 1
    usuario = get_usuario_by_id(usuario_id)
    assert usuario.id == usuario_id

def test_get_usuario_by_nome():
    '''
    Teste do metodo get_usuario_by_nome
    pytest tests/repositorio/test_usuario.py::test_get_usuario_by_nome -vv
    '''
    usuario_nome = 'test'
    usuario = get_usuario_by_nome(usuario_nome)
    assert usuario.nome == usuario_nome

def test_get_usuarios():
    '''
    Teste do metodo get_usuarios
    pytest tests/repositorio/test_usuario.py::test_get_usuarios -vv
    '''
    usuarios = get_usuarios()
    assert usuarios

def test_senha_valida():
    '''
    Teste do metodo senha_valida
    pytest tests/repositorio/test_usuario.py::test_senha_valida -vv
    '''
    usuario_id = 1
    usuario_senha = '123'
    senha_informada_valida = senha_valida(usuario_id, usuario_senha)
    assert senha_informada_valida

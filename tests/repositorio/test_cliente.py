# pylint: disable=line-too-long
'''
Testes do repositorio usuario.py
pytest tests/repositorio/test_cliente.py -vv
'''

from src.repositorio.cliente_repositorio import(
    get_cliente_by_id,
    get_cliente_by_nome,
    get_clientes,
    senha_valida
)

def test_get_cliente_by_id():
    '''
    Teste do metodo get_usuario_by_id
    pytest tests/repositorio/test_cliente.py::test_get_cliente_by_id -vv
    '''
    cliente_id = 1
    cliente = get_cliente_by_id(cliente_id)
    assert cliente.id == cliente_id

def test_get_cliente_by_nome():
    '''
    Teste do metodo get_usuario_by_nome
    pytest tests/repositorio/test_cliente.py::test_get_cliente_by_nome -vv
    '''
    cliente_nome = 'test'
    cliente = get_cliente_by_nome(cliente_nome)
    assert cliente.nome == cliente_nome

def test_get_clientes():
    '''
    Teste do metodo get_usuarios
    pytest tests/repositorio/test_cliente.py::test_get_clientes -vv
    '''
    clientes = get_clientes()
    assert clientes

def test_senha_valida():
    '''
    Teste do metodo senha_valida
    pytest tests/repositorio/test_usuario.py::test_senha_valida -vv
    '''
    usuario_id = 1
    usuario_senha = '123'
    senha_informada_valida = senha_valida(usuario_id, usuario_senha)
    assert senha_informada_valida

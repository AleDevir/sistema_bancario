# pylint: disable=line-too-long
'''
Testes do repositorio agencia_conta.py
pytest tests/repositorio/test_agencia_conta.py -vv
'''

from src.repositorio.agencia_conta_repositorio import get_contas_agencias_do_usuario

def test_get_contas_agencias_do_usuario():
    '''
    Teste do metodo otest_get_contas_agencias_do_usuario 
    pytest tests/repositorio/test_agencia_conta.py::test_get_contas_agencias_do_usuario -vv
    '''
    usuario = {
        'id': 4
    }
    contas_agencias_do_usuario = get_contas_agencias_do_usuario(usuario['id'])
    assert contas_agencias_do_usuario
    for conta in contas_agencias_do_usuario:
        assert conta['usuario_id'] == usuario['id']

def test_get_contas_agencias_do_usuario_invalido():
    '''
    Teste do metodo otest_get_contas_agencias_do_usuario - ID INVÁLIDO
    pytest tests/repositorio/test_agencia_conta.py::test_get_contas_agencias_do_usuario_invalido -vv
    '''
    usuario = {
        'id': 4333
    }
    contas_agencias_do_usuario = get_contas_agencias_do_usuario(usuario['id'])
    assert not contas_agencias_do_usuario
    assert contas_agencias_do_usuario == []

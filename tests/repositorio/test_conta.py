# pylint: disable=line-too-long
'''
Testes do repositorio conta.py
pytest tests/repositorio/test_conta.py -vv
'''

from src.repositorio.conta_repositorio import(
    get_conta_by_id,
    get_conta_by_numero,
    get_contas,
    get_contas_do_cliente,
)

def test_get_conta_by_id():
    '''
    Teste do metodo get_conta_by_id
    pytest tests/repositorio/test_conta.py::test_get_conta_by_id -vv
    '''
    conta_id = 1
    conta = get_conta_by_id(conta_id)
    assert conta
    assert conta.id == conta_id

def test_get_conta_by_numero():
    '''
    Teste do metodo get_conta_by_numero
    pytest tests/repositorio/test_conta.py::test_get_conta_by_numero -vv
    '''
    conta_numero =  7777
    conta = get_conta_by_numero(conta_numero)
    assert conta.numero == conta_numero

def test_get_contas():
    '''
    Teste do metodo get_contas
    pytest tests/repositorio/test_conta.py::test_get_contas -vv
    '''
    contas = get_contas()
    assert contas

def test_get_contas_do_cliente():
    '''
    Teste do metodo get_contas_do_usuario
    pytest tests/repositorio/test_conta.py::test_get_contas_do_cliente -vv
    '''
    cliente_id = 1
    contas = get_contas_do_cliente(cliente_id)
    for conta in contas:
        assert conta.cliente_id == cliente_id

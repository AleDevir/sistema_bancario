# pylint: disable=line-too-long
'''
Testes do model conta.py
pytest tests/model/test_conta.py -vv
'''

from src.model.conta import(
    get_conta_by_id,
    get_conta_by_numero,
    get_contas 
)

def test_get_conta_by_id():
    '''
    Teste do metodo get_conta_by_id
    pytest tests/model/test_conta.py::test_get_conta_by_id -vv
    '''
    conta_id = 1
    conta = get_conta_by_id(conta_id)
    assert conta
    assert conta['id'] == conta_id

def test_get_conta_by_numero():
    '''
    Teste do metodo get_conta_by_numero
    pytest tests/model/test_conta.py::test_get_conta_by_numero -vv
    '''
    conta_numero =  777777
    conta = get_conta_by_numero(conta_numero)
    assert conta['numero'] == conta_numero

def test_get_contas():
    '''
    Teste do metodo get_contas
    pytest tests/model/test_conta.py::test_get_contas -vv
    '''
    contas = get_contas()
    assert contas

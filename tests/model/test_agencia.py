# pylint: disable=line-too-long
'''
Testes do model agencia.py
pytest tests/model/test_agencia.py -vv
'''

from src.model.agencia import(
    get_agencia_by_id,
    get_agencia_by_numero,
    get_agencias
)

def test_get_agencia_by_id():
    '''
    Teste do metodo test_get_agencia_by_id
    pytest tests/model/test_agencia.py::test_get_agencia_by_id -vv
    '''
    agencia = {
        'id': 3
    }
    agencia = get_agencia_by_id(agencia['id'])
    assert agencia

def test_get_agencia_by_numero():
    '''
    Teste do metodo test_get_agencia_by_numero
    pytest tests/model/test_agencia.py::test_get_agencia_by_numero -vv
    '''
    agencia = {
        'numero': 333,
    }
    agencia = get_agencia_by_numero(agencia['numero'])
    assert agencia

def test_get_agencia():
    '''
    Teste do metodo test_get_agencia
    pytest tests/model/test_agencia.py::test_get_agencia -vv
    '''
    get_agencias()
    assert True

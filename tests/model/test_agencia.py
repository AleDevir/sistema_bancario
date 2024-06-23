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
    agencia_id = 3
    agencia = get_agencia_by_id(agencia_id)
    assert agencia['id'] == agencia_id

def test_get_agencia_by_numero():
    '''
    Teste do metodo test_get_agencia_by_numero
    pytest tests/model/test_agencia.py::test_get_agencia_by_numero -vv
    '''
    agencia_numero = 333
    agencia = get_agencia_by_numero(agencia_numero)
    assert agencia['numero'] == agencia_numero

def test_get_agenciaS():
    '''
    Teste do metodo test_get_agencia
    pytest tests/model/test_agencia.py::test_get_agencias -vv
    '''
    agencias = get_agencias()
    assert agencias 


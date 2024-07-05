'''
Repositório Agência
'''

from sqlite3 import connect, Cursor
from src.model.agencia import Agencia, agencia_from_dict

conexao_agencia = connect('C:\\Estudos_python\\operacoes_bancarias_basicas\\src\\db\\banco_de_dados.db')
cursor: Cursor = conexao_agencia.cursor()

def criar_tabela_agencias():
    '''
    Cria a tabela agencias
    '''
    cursor.execute(''' CREATE TABLE IF NOT EXISTS agencias(
                    id integer primary key autoincrement,
                    numero integer NOT NULL,
                    digito integer NOT NULL)''')

def inserir_agencia(numero: int, digito: int ):
    '''
    Inseri agencia na tabela.
    '''
    dados =  (numero, digito)
    cursor.execute('INSERT INTO agencias(numero, digito) VALUES(?, ?)', dados) # pylint: disable=line-too-long
    conexao_agencia.commit()
#################################################
    # INFRAESTRUTURA #
#################################################

def agencia_tuple_to_dict(data: tuple) -> dict[str, int]:
    '''
    Transforma um elemento (tuple) do banco de dados em uma estrutura de dicionário.
    Retorna o dicionário com dados da conta.
    '''
    idt, numero, digito =  data
    return {
        'id': idt,
        'numero': numero,
        'digito': digito
    }

#################################################
    # GET - AGENCIA #
#################################################
def get_agencia_by_id(agencia_id: int) -> Agencia:
    '''
    Obter uma agência pelo ID.
    '''
    cursor.execute(f"SELECT * FROM agencias WHERE id = {agencia_id} ")
    data = cursor.fetchone()
    data_dict = agencia_tuple_to_dict(data)
    return agencia_from_dict(data_dict)

def get_agencia_by_numero(agencia_numero: int) -> Agencia:
    '''
    Obter uma agência pelo NÚMERO.
    '''
    cursor.execute(f"SELECT * FROM agencias WHERE numero = {agencia_numero} ")
    data = cursor.fetchone()
    data_dict = agencia_tuple_to_dict(data)
    return agencia_from_dict(data_dict)

def get_agencias() -> list[Agencia]:
    '''
    Obter TODAS as agências.
    '''
    cursor.execute('SELECT * FROM agencias')
    agencias_db = cursor.fetchall()
    result: list[Agencia] = []
    for data in agencias_db:
        agencia_dict = agencia_tuple_to_dict(data)
        result.append(
            agencia_from_dict(agencia_dict)
        )
    return result

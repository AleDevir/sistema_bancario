'''
Repositório Agência
'''

from sqlite3 import connect, Cursor
from src.model.agencia import Agencia

conexao_agencia = connect('.\\src\\db\\banco_de_dados.db') # pylint: disable=line-too-long
cursor: Cursor = conexao_agencia.cursor()

def drop_table_agencias() -> None:
    '''
    Apaga a tabela se ela já exixtir.
    '''
    cursor.execute("DROP TABLE  IF EXISTS agencias")

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

def delete_rows_agencia() -> None:
    '''
    Deleta as linhas da tabela.
    '''
    cursor.execute("DELETE FROM agencias")
    conexao_agencia.commit()

#################################################
    # INFRAESTRUTURA #
#################################################

def tuple_to_agencia(data: tuple) -> Agencia:
    '''
    Transforma um elemento (tuple) do banco de dados em uma estrutura de dicionário.
    Retorna o dicionário com dados da conta.
    '''
    if not data:
        return None
    idt, numero, digito =  data
    return Agencia.agencia(
        idt=idt,
        numero=numero,
        digito=digito
    )

#################################################
    # GET - AGENCIA #
#################################################
def get_agencia_by_id(agencia_id: int) -> Agencia:
    '''
    Obter uma agência pelo ID.
    '''
    cursor.execute(f"SELECT * FROM agencias WHERE id = {agencia_id} ")
    data = cursor.fetchone()
    return tuple_to_agencia(data)

def get_agencia_by_numero(agencia_numero: int) -> Agencia:
    '''
    Obter uma agência pelo NÚMERO.
    '''
    cursor.execute(f"SELECT * FROM agencias WHERE numero = {agencia_numero} ")
    data = cursor.fetchone()
    return tuple_to_agencia(data)

def get_agencias() -> list[Agencia]:
    '''
    Obter TODAS as agências.
    '''
    cursor.execute('SELECT * FROM agencias')
    agencias_db = cursor.fetchall()
    result: list[Agencia] = []
    for data in agencias_db:
        agencia = tuple_to_agencia(data)
        result.append(agencia)
    return result

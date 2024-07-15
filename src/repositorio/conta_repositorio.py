'''
Model Conta
'id'    = PK - Primary Key: Chave Primária
'numero'= AK - Alternate Key: Chave Alternativa
'''

from sqlite3 import connect, Cursor
from typing import Optional
from src.model.conta import Conta

conexao_conta = connect('.\\src\\db\\banco_de_dados.db')
cursor: Cursor = conexao_conta.cursor()


def drop_table_contas() -> None:
    '''
    Apaga a tabela se ela já exixtir.
    '''
    cursor.execute("DROP TABLE IF EXISTS contas")

def criar_tabela_contas():
    '''
    Cria a tabela contas
    '''
    cursor.execute(''' CREATE TABLE IF NOT EXISTS contas(
                    id integer primary key autoincrement,
                    numero integer NOT NULL,
                    digito integer NOT NULL,
                    tipo integer NOT NULL,
                    agencia_id integer  NOT NULL,
                    cliente_id integer NOT NULL,
                    FOREIGN KEY(cliente_id) REFERENCES clientes(id))''')

def inserir_conta(numero: int, digito: int, tipo: int, agencia_id: int, cliente_id: int, ):
    '''
    Inseri conta na tabela.
    '''
    dados =  (numero, digito, tipo, agencia_id, cliente_id)
    cursor.execute('INSERT INTO contas(numero, digito, tipo, agencia_id, cliente_id) VALUES(?, ?,  ?, ?, ?)', dados) # pylint: disable=line-too-long
    conexao_conta.commit()

def delete_rows_conta() -> None:
    '''
    Deleta as linhas da tabela.
    '''
    cursor.execute("DELETE FROM contas")
    conexao_conta.commit()

#################################################
    # INFRAESTRUTURA #
#################################################


def tuple_to_conta(data: tuple) -> Optional[Conta]:
    '''
    Transforma um elemento (tuple) do banco de dados em uma estrutura de dicionário.
    Retorna o dicionário com dados da conta.
    '''
    if not data:
        return None
    idt, numero, digito, tipo, agencia_id, cliente_id =  data
    return Conta.conta(
        idt=idt,
        numero=numero,
        digito=digito,
        tipo=tipo,
        agencia_id=agencia_id,
        cliente_id=cliente_id
    )

#################################################
    # GET - CONTA #
#################################################

def get_conta_by_id(conta_id: int) -> Optional[Conta]:
    '''
    Obter uma Conta pelo ID.
    '''
    cursor.execute(f"SELECT * FROM contas WHERE id = {conta_id} ")
    data = cursor.fetchone()
    return tuple_to_conta(data)

def get_conta_by_numero(conta_numero: int) -> Optional[Conta]:
    '''
    Obter uma Conta pelo NÚMERO.
    '''
    cursor.execute(f"SELECT * FROM contas WHERE numero = {conta_numero} ")
    data = cursor.fetchone()
    return tuple_to_conta(data)


def get_contas() -> list[Conta]:
    '''
    Obter TODAS as Contas.
    '''
    cursor.execute('SELECT * FROM contas')
    contas_db = cursor.fetchall()
    result: list[Conta] = []
    for data in contas_db:
        conta = tuple_to_conta(data)
        if conta:
            result.append(conta)
    return result

def get_contas_do_cliente(cliente_id: int) -> list[Conta]:
    '''
    Obter Contas da Agência informada.
    '''
    cursor.execute(f"SELECT * FROM contas WHERE id = {cliente_id} ")
    contas_db = cursor.fetchall()

    result: list[Conta] = []
    for data in contas_db:
        conta = tuple_to_conta(data)
        if conta:
            result.append(conta)
    return result

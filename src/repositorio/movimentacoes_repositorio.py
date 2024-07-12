'''
Model das movimentações finaceiras
'''
from sqlite3 import connect, Cursor
from datetime import datetime
from src.model.movimentacoes import Movimentacoes, movimentacao_from_dict

conexao_movimentacoes = connect('.\\src\\db\\banco_de_dados.db')
cursor: Cursor = conexao_movimentacoes.cursor()

def drop_table_movimentacoes() -> None:
    '''
    Apaga a tabela se ela já exixtir.
    '''
    cursor.execute("DROP TABLE IF EXISTS movimentacoes")

def criar_tabela_movimentacoes():
    '''
    Cria a tabela contas
    '''
    cursor.execute(''' CREATE TABLE IF NOT EXISTS movimentacoes(
                    id integer primary key autoincrement,
                    valor real NOT NULL,
                    date int NOT NULL,
                    conta_id integer NOT NULL,
                    FOREIGN KEY(conta_id) REFERENCES contas(id))''')



def inserir_movimentacoes(valor: float, date: datetime, conta_id: int ):
    '''
    Inseri conta na tabela.
    '''
    dados =  (valor, date, conta_id)
    cursor.execute('INSERT INTO movimentacoes(valor, date, conta_id) VALUES(?, ?, ?)', dados) # pylint: disable=line-too-long
    conexao_movimentacoes.commit()

def delete_rows_movimentacao() -> None:
    '''
    Deleta as linhas da tabela.
    '''
    cursor.execute("DELETE FROM movimentacoes")
    conexao_movimentacoes.commit()


#################################################
    # INFRAESTRUTURA #
#################################################

def movimentacao_tuple_to_dict(data: tuple) -> dict[str, int]:
    '''
    Transforma um elemento (tuple) do banco de dados em uma estrutura de dicionário.
    Retorna o dicionário com dados da conta.
    '''
    idt, valor, date, conta_id = data
    return {
        'id': idt,
        'valor': valor,
        'date': date,
        'conta_id': conta_id    
    }

#################################################
    # ADD - MOVIMENTAÇÃO #
#################################################

def add_movimentacao(valor: float, conta_id: int) -> None:
    '''
    Add Movimentação
    '''
    agora = datetime.now()
    data_hora = datetime(agora.year, agora.month, agora.day, agora.hour, agora.minute, agora.second)
    inserir_movimentacoes(valor, data_hora, conta_id)

#################################################
    # GET - MOVIMENTAÇÃO #
#################################################

def get_movimentacoes_financeiras() -> list[Movimentacoes]:
    '''
    Obtem dados daa movimentações financeira
    Retorna aa movimentações.
    '''
    cursor.execute('SELECT * FROM movimentacoes')
    movimentacoes_db = cursor.fetchall()
    result: list[Movimentacoes] = []
    for data in movimentacoes_db:
        mov_dict = movimentacao_tuple_to_dict(data)
        mov = movimentacao_from_dict(mov_dict)
        if mov:
            result.append(mov)
    return result

def get_movimentacao_financeira_do_cliente(conta_id: int) -> list[Movimentacoes]:
    '''
    Obtem dados da movimentação financeira do cliente(depósitos, saques e saldo)
    Retorna a movimentação.
    '''
    cursor.execute(f"SELECT * FROM movimentacoes WHERE conta_id = {conta_id} ")
    movimentacoes_db = cursor.fetchall()
    result: list[Movimentacoes] = []
    for data in movimentacoes_db:
        mov_dict = movimentacao_tuple_to_dict(data)
        mov = movimentacao_from_dict(mov_dict)
        if mov:
            result.append(mov)
    return result

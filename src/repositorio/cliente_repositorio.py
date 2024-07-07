'''
Repositório cliente
'''
from sqlite3 import connect, Cursor
import bcrypt
from src.model.cliente import Cliente, cliente_from_dict

conexao_cliente = connect('.\\src\\db\\banco_de_dados.db') # pylint: disable=line-too-long
cursor: Cursor = conexao_cliente.cursor()

def drop_table_clientes() -> None:
    '''
    Apaga a tabela se ela já exixtir.
    '''
    cursor.execute("DROP TABLE IF EXISTS clientes")

def criar_tabela_clientes()-> None:
    '''
    Cria a tabela clientes
    '''
    cursor.execute(''' CREATE TABLE IF NOT EXISTS clientes(
                    id integer primary key autoincrement,
                    nome text NOT NULL,
                    sobrenome text NOT NULL,
                    senha text  NOT NULL,
                    cpf text UNIQUE NOT NULL)''')



def inserir_cliente(nome: str, sobrenome: str, senha_hash: str, cpf: str) -> None:
    '''
    Inseri cliente na tabela.
    '''
    dados =  (nome, sobrenome, senha_hash, cpf)
    cursor.execute('INSERT INTO clientes(nome, sobrenome, senha, cpf) VALUES(?, ?, ?, ?)', dados)
    conexao_cliente.commit()

def delete_rows_cliente() -> None:
    '''
    Deleta as linhas da tabela.
    '''
    cursor.execute("DELETE FROM clientes")
    conexao_cliente.commit()

#################################################
    # INFRAESTRUTURA #
#################################################

def cliente_tuple_to_dict(data: tuple) -> dict[str, int]:
    '''
    Transforma um elemento (tuple) do banco de dados em uma estrutura de dicionário.
    Retorna o dicionário com dados da conta.
    '''
    idt, nome, sobrenome, senha, cpf =  data
    return {
        'id': idt,
        'nome': nome,
        'sobrenome': sobrenome,
        'senha': senha,
        'cpf': cpf
    }

#################################################
    # GET - CLIENTE #
#################################################

def get_cliente_by_id(cliente_id: int) -> Cliente:
    '''
    Obter um cliente pelo ID.
    '''
    cursor.execute(f"SELECT * FROM clientes WHERE id = {cliente_id} ")
    data = cursor.fetchone()
    data_dict = cliente_tuple_to_dict(data)
    return cliente_from_dict(data_dict)


def get_cliente_by_nome(cliente_nome: str) -> Cliente:
    '''
    Obter um Usuário pelo NOME.
    '''
    print(f"cliente nome: {cliente_nome} ############################")
    cursor.execute(f"SELECT * FROM clientes WHERE nome = '{cliente_nome}' ")
    data = cursor.fetchone()
    print(f"data: {data} ############################")
    data_dict = cliente_tuple_to_dict(data)
    print(f"data_dict: {data_dict} ############################")
    return cliente_from_dict(data_dict)

def get_clientes() -> list[Cliente]:
    '''
    Obter TODOS os clientes
    '''
    cursor.execute('SELECT * FROM clientes')
    clientes_db = cursor.fetchall()
    result: list[Cliente] = []
    for data in clientes_db:
        cliente_dict = cliente_tuple_to_dict(data)
        result.append(
            cliente_from_dict(cliente_dict)
        )
    return result

def senha_valida(cliente_id: int, senha: str) -> bool:
    '''
    Valida a senha do cliente.
    '''
    cliente = get_cliente_by_id(cliente_id)

    if not cliente:
        return False

    return bcrypt.checkpw(senha.encode(), cliente.senha) # type: ignore[arg-type]

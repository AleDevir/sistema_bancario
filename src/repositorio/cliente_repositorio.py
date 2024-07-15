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

# def atualizar_cliente(cursor: Cursor, nome: str, cliente_id: int):
#     cursor.execute(f"UPDATE clientes SET nome = '{nome}' WHERE id = {cliente_id}")
#     conexao_cliente.commit()

# def deletar_cliente(cursor: Cursor, id: int):
#     cursor.execute(f"DELETE FROM clientes WHERE id={id}")
#     conexao_cliente.commit()

def delete_rows_cliente() -> None:
    '''
    Deleta as linhas da tabela.
    '''
    cursor.execute("DELETE FROM clientes")
    conexao_cliente.commit()

#################################################
    # INFRAESTRUTURA #
#################################################


def tuple_to_cliente(data: tuple) -> Cliente:
    '''
    Transforma um elemento (tuple) do banco de dados em uma estrutura de dicionário.
    Retorna o dicionário com dados da conta.
    '''
    idt, nome, sobrenome, senha, cpf =  data
    return Cliente.cliente(
        idt=idt,
        nome=nome,
        sobrenome=sobrenome,
        senha=senha,
        cpf=cpf
    )


#################################################
    # GET - CLIENTE #
#################################################

def get_cliente_by_id(cliente_id: int) -> Cliente:
    '''
    Obter um cliente pelo ID.
    '''
    cursor.execute(f"SELECT * FROM clientes WHERE id = {cliente_id} ")
    data = cursor.fetchone()
    return tuple_to_cliente(data)


def get_cliente_by_nome(cliente_nome: str) -> Cliente:
    '''
    Obter um Usuário pelo NOME.
    '''
    cursor.execute(f"SELECT * FROM clientes WHERE nome = '{cliente_nome}' ")
    data = cursor.fetchone()
    return tuple_to_cliente(data)

def get_clientes() -> list[Cliente]:
    '''
    Obter TODOS os clientes
    '''
    cursor.execute('SELECT * FROM clientes')
    clientes_db = cursor.fetchall()
    result: list[Cliente] = []
    for data in clientes_db:
        cliente = tuple_to_cliente(data)
        result.append(cliente)
    return result

def senha_valida(cliente_id: int, senha: str) -> bool:
    '''
    Valida a senha do cliente.
    '''
    cliente = get_cliente_by_id(cliente_id)

    if not cliente:
        return False

    return bcrypt.checkpw(senha.encode(), cliente.senha) # type: ignore[arg-type]

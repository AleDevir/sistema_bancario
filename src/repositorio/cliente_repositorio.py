'''
Repositório cliente
'''
from sqlite3 import connect, Cursor
import bcrypt
from src.model.cliente import Cliente

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
    # CRIAR - CLIENTE #
#################################################

def inserir_cliente(nome: str, sobrenome: str, senha_hash: str, cpf: str) -> None:
    '''
    Inseri cliente na tabela.
    '''
    dados =  (nome, sobrenome, senha_hash, cpf)
    # cursor.execute('INSERT INTO clientes(nome, sobrenome, senha, cpf) VALUES(?, ?, ?, ?)', dados) # pylint: disable=line-too-long
    cursor.execute('INSERT INTO clientes(nome, sobrenome, senha, cpf) VALUES(?, ?, ?, ?)', dados) # pylint: disable=line-too-long
    conexao_cliente.commit()


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

def get_cliente_by_cpf(cliente_cpf: str) -> Cliente | None:
    '''
    Obter um Usuário pelo CPF.
    '''
    cursor.execute(f"SELECT * FROM clientes WHERE cpf = '{cliente_cpf}' ")
    data = cursor.fetchone()
    if not data:
        return None
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

#################################################
    # UPDATE - CLIENTE #
#################################################

def update_cliente(nome: str, sobrenome: str, cliente_cpf: str, cliente_id: int) -> None:
    '''
    Atualiza dados do cliente na tabela.
    '''
    cursor.execute("UPDATE clientes SET nome = ?, sobrenome = ?, cpf = ? WHERE id = ?", (nome, sobrenome, cliente_cpf, cliente_id)) # pylint: disable=line-too-long
    conexao_cliente.commit()

#################################################
    # SENHA - CLIENTE #
#################################################

def senha_valida(cliente_id: int, senha: str) -> bool:
    '''
    Valida a senha do cliente.
    '''
    cliente = get_cliente_by_id(cliente_id)

    if not cliente:
        return False

    return bcrypt.checkpw(senha.encode(), cliente.senha) # type: ignore[arg-type]


#################################################
    # DELETE - CLIENTE #
#################################################
def delete_cliente(idt: int):
    '''
    Deleta um cliente de id informado.
    '''
    cursor.execute("DELETE FROM clientes WHERE id= ?", (str(idt)))
    conexao_cliente.commit()

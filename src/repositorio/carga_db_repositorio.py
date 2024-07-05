'''
Carga DB - criação de tabelas e inserção de dados.
'''

from datetime import datetime
import bcrypt
from src.repositorio.cliente_repositorio import(
    criar_tabela_clientes,
    inserir_cliente,
    drop_table_clientes
)
from src.repositorio.conta_repositorio import(
    criar_tabela_contas,
    inserir_conta,
    drop_table_contas
)
from src.repositorio.agencia_repositorio import(
    criar_tabela_agencias,
    inserir_agencia,
    drop_table_agencias
)
from src.repositorio.movimentacoes_repositorio import(
    criar_tabela_movimentacoes,
    inserir_movimentacoes,
    drop_table_movimentacoes
)

def carregar_banco_de_dados() -> None:
    '''
    Fluxo principal
    '''
    drop_table_movimentacoes()
    drop_table_contas()
    drop_table_agencias()
    drop_table_clientes()

    criar_tabela_clientes()
    criar_tabela_agencias()
    criar_tabela_contas()
    criar_tabela_movimentacoes()

    # Cliente
    senha_hash = bcrypt.hashpw('123'.encode(), bcrypt.gensalt())
    inserir_cliente('rinaldo', 'benevides', senha_hash, 45559920088)
    inserir_cliente('alessandra', 'guimarães', senha_hash, 95282507005)
    inserir_cliente('test', 'test', senha_hash, 87315683003)
    inserir_cliente('test', 'test', senha_hash, 23447087072)
    inserir_cliente('test', 'test', senha_hash, 82160212083)

    # Agência
    inserir_agencia(111, 1)
    inserir_agencia(222, 2)
    inserir_agencia(333, 3)

    # Conta
    inserir_conta(1111, 11, 1, 1, 1)
    inserir_conta(2222, 22, 2, 1, 1)
    inserir_conta(3333, 33, 1, 2, 2)
    inserir_conta(4444, 44, 1, 1, 3)
    inserir_conta(5555, 55, 2, 2, 4)
    inserir_conta(6666, 66, 2, 3, 5)
    inserir_conta(7777, 77, 2, 1, 2)

    agora = datetime.now()
    data_hora = datetime(agora.year, agora.month, agora.day, agora.hour, agora.minute, agora.second)

    # Movimentação
    inserir_movimentacoes(215.20, datetime(2019, 2, 12, 12, 14, 00), 1)
    inserir_movimentacoes(25.00, datetime(2020, 5, 10, 23, 10, 00), 2)
    inserir_movimentacoes(100.00, datetime(2020, 4, 17, 15, 10, 00), 3)
    inserir_movimentacoes(-10.00, data_hora, 3)
    inserir_movimentacoes(-15.00, data_hora, 3)
    inserir_movimentacoes(-10.50, data_hora, 1)
    inserir_movimentacoes(-15.50, data_hora, 4)
    inserir_movimentacoes(-35.00, data_hora, 4)
    inserir_movimentacoes(-53.00, datetime(2021, 6, 10, 15, 10, 00), 4)
    inserir_movimentacoes(330.90, datetime(2021, 6, 12, 12, 10, 00), 4)
    inserir_movimentacoes(500.00, datetime(2021, 6, 9, 23, 10, 00), 6)
    inserir_movimentacoes(500.00, datetime(2021, 8, 11, 18, 10, 00), 7)

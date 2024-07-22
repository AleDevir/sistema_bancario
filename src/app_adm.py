# pylint: disable=line-too-long
'''
Aplicação do administrador.
    Carregar o DB.
    RUD no DB - Sqlite
'''

from typing import Final
import bcrypt
from src.util.console_util import (
    bright_amarelo,
    vermelho,
    verde,
    print_center,
    limpar_console
)
from src.util.menu_util import escolher_uma_opcao_do_menu_entrada
from src.util.input_util import  input_int
from src.app import get_input, get_senha
from src.repositorio.carga_db_repositorio import carregar_banco_de_dados
from src.repositorio.cliente_repositorio import(
    inserir_cliente,
    get_cliente_by_cpf,
    delete_cliente,
    update_cliente
)
from src.repositorio.conta_repositorio import (
    inserir_conta,
    update_conta,
    get_conta_by_numero,
    delete_conta
)
from src.repositorio.agencia_repositorio import (
    inserir_agencia,
    get_agencia_by_numero,
    update_agencia,
    delete_agencia
)

LINHA_ASTERISCO: Final[str] = '*' * 83

def get_dados_da_conta_para_inserir_na_tabela() -> list[int]:
    '''
    Obter dados da conta para inserir na tabela
    '''
    dados: list[int] = []
    while True:
        numero = input_int('Numero da conta: ')
        digito = input_int('Digito: ')
        tipo = input_int('Tipo (1: conta-corrente | 2: poupança): ')
        agencia_id = input_int('Agencia_id: ')
        cliente_id = input_int('Cliente_id: ')
        break
    return dados.append(numero, digito, tipo, agencia_id, cliente_id)



##################################################
     # OPÇOES DO MENU ADMIN#
##################################################

menu_admin:  dict[str, str ] = {
        'CB': 'Carregar a Base de Dados',
        'CL': 'Cliente',
        'CO': 'Conta',
        'AG': 'Agência', 
        'SA': 'Sair',
}
menu_crud:  dict[str, str ] = {
        'A': 'Adicionar',
        'C': 'Consultar',
        'D': 'Deletar',
        'U': 'Update', 
        'S': 'Sair',
}


##################################################
     # FLUXO PRINCIPAL DA APP_ADMIN #
##################################################

def admin() -> None:
    '''
    Fluxo Principal do Administrador.
    '''
    limpar_console()

    while True:
        opcao_administrativa = escolher_uma_opcao_do_menu_entrada(menu_admin)
        match opcao_administrativa:
            case "CB":
                carregar_banco_de_dados()
                print(verde('Carregada com sucesso! :)'))
                break
            case "CL":
                opcao_crud = escolher_uma_opcao_do_menu_entrada(menu_crud)
                match opcao_crud:
                    case "A":
                        nome = get_input('Nome: ')
                        sobrenome = get_input('Sobrenome: ')
                        senha = get_senha('Senha: ')
                        senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
                        cpf = get_input('CPF: ')
                        inserir_cliente(nome, sobrenome, senha_hash, cpf)
                    case "C":
                        cpf= get_input("Insira o CPF: ")
                        cliente = get_cliente_by_cpf(cpf)
                        if not cliente:
                            print(vermelho(f'Cliente de cpf: {cpf} não encontrado na Base de Dados.'))
                        else:
                            print(f"\n{LINHA_ASTERISCO}\n")
                            print(bright_amarelo(f"\nCliente: nome: {cliente.nome} {cliente.sobrenome} - CPF: {cliente.cpf}\n"))
                            print(f"\n{LINHA_ASTERISCO}\n")
                    case "D":
                        cpf= get_input("Insira o CPF: ")
                        cliente = get_cliente_by_cpf(cpf)
                        if not cliente:
                            print(vermelho(f'Cliente de cpf: {cpf} não encontrado na Base de dados.'))
                        else:
                            print(f"Cliente: nome: {cliente.nome} sobrenome: {cliente.sobrenome} CPF: {cliente.cpf} ID: {cliente.id}")
                            confirmar = get_input("Deseja excluir o cliente (S ou N): ").upper()
                            if confirmar == "S":
                                delete_cliente(cliente.id)
                                print(bright_amarelo(f"\nCliente do cpf {cliente.cpf} excluído com sucesso"))
                            else:
                                return
                    case "U":
                        cpf= get_input("Insira o CPF: ")
                        cliente = get_cliente_by_cpf(cpf)
                        if not cliente:
                            print(vermelho(f'Cliente de cpf: {cpf} não encontrado na Base de Dados.'))
                        else:
                            print(f"\n{LINHA_ASTERISCO}\n")
                            print(f"Cliente: nome: {cliente.nome} sobrenome: {cliente.sobrenome} CPF: {cliente.cpf} ID: {cliente.id}") # pylint: disable=line-too-long
                            print(f"\n{LINHA_ASTERISCO}\n")
                            print_center('Inserir os novos dados', 34)
                            nome = get_input('Novo nome: ')
                            sobrenome = get_input('Novo sobrenome: ')
                            novo_cpf = get_input('Novo cpf: ')
                            update_cliente(nome, sobrenome, novo_cpf, cliente.id)

                    case "S":
                        print_center(bright_amarelo(" SAIR :)\n"), 40)
                        break
            case "CO":
                opcao_crud = escolher_uma_opcao_do_menu_entrada(menu_crud)
                match opcao_crud:
                    case "A":
                        numero = input_int('Numero da conta: ')
                        digito = input_int('Digito: ')
                        tipo = input_int('Tipo (1: conta-corrente | 2: poupança): ')
                        agencia_id = input_int('Agencia_id: ')
                        cliente_id = input_int('Cliente_id: ')
                        inserir_conta(numero, digito, tipo, agencia_id, cliente_id)

                    case "C":
                        numero= input_int("Insira o número da conta: ")
                        conta = get_conta_by_numero(numero)
                        if not conta:
                            print(vermelho(f'Conta de númerof: {numero} não encontrada na Base de Dados.'))
                        else:
                            print(f"\n{LINHA_ASTERISCO}\n")
                            print(bright_amarelo(f"Conta: número: {conta.numero} | digito: {conta.digito} | tipo: {conta.tipo} | agência_id: {conta.agencia_id} | cliente_id: {conta.cliente_id} | ID: {conta.id}")) # pylint: disable=line-too-long
                            print(f"\n{LINHA_ASTERISCO}\n")
                    case "D":
                        numero= get_input("Insira o número da conta: ")
                        conta = get_conta_by_numero(numero)
                        if not conta:
                            print(vermelho(f'Conta de número: {numero} não encontrada na Base de Dados.'))
                        else:
                            print(f"\nConta: número: {conta.numero} | digito: {conta.digito} | tipo: {conta.tipo} | agência_id: {conta.agencia_id} | cliente_id: {conta.cliente_id} | ID: {conta.id}") # pylint: disable=line-too-long
                            confirmar = get_input("Deseja excluir a conta (S ou N): ").upper()
                            if confirmar == "S":
                                delete_conta(conta.id)
                                print(bright_amarelo(f"\nConta do número {conta.numero} excluída com sucesso"))
                            else:
                                return
                    case "U":
                        numero= input_int("Insira o número da conta: ")
                        conta = get_conta_by_numero(numero)
                        if not conta:
                            print(vermelho(f'Conta de númerof: {numero} não encontrada na Base de Dados.'))
                        else:
                            print(f"\n{LINHA_ASTERISCO}\n")
                            print(f"Conta: número: {conta.numero} | digito: {conta.digito} | tipo: {conta.tipo} | agência_id: {conta.agencia_id} | cliente_id: {conta.cliente_id} | ID: {conta.id}") # pylint: disable=line-too-long
                            print(f"\n{LINHA_ASTERISCO}\n")
                            print_center('Inserir os novos dados', 34)
                            numero = input_int('Número da conta: ')
                            digito = input_int('Digito: ')
                            tipo = input_int('Tipo (1: conta-corrente | 2: poupança): ')
                            agencia_id = input_int('Agencia_id: ')
                            cliente_id = input_int('Cliente_id: ')
                            update_conta(numero, digito, tipo, agencia_id, cliente_id, conta.id)
                    case "S":
                        print_center(bright_amarelo(" SAIR :)\n"), 40)
                        break
            case "AG":
                opcao_crud = escolher_uma_opcao_do_menu_entrada(menu_crud)
                match opcao_crud:
                    case "A":
                        numero = input_int('Numero da agência: ')
                        digito = input_int('Digito: ')
                        inserir_agencia(numero, digito)
                    case "C":
                        numero= input_int("Insira o número da conta: ")
                        agencia = get_conta_by_numero(numero)
                        if not conta:
                            print(vermelho(f'Agência de númerof: {numero} não encontrada na Base de Dados.'))
                        else:
                            print(f"\n{LINHA_ASTERISCO}\n")
                            print(bright_amarelo(f"Agência: número: {agencia.numero} | digito: {agencia.digito} | ID: {agencia.id}")) # pylint: disable=line-too-long
                            print(f"\n{LINHA_ASTERISCO}\n")
                    case "D":
                        numero= input_int("Insira o número da conta: ")
                        agencia = get_agencia_by_numero(numero)
                        if not agencia:
                            print(vermelho(f'Agência de número: {numero} não encontrada na Base de Dados.'))
                        else:
                            print(f"\nConta: número: {agencia.numero} | digito: {agencia.digito} | ID: {agencia.id}") # pylint: disable=line-too-long
                            confirmar = get_input("Deseja excluir a agência (S ou N): ").upper()
                            if confirmar == "S":
                                delete_agencia(agencia.id)
                                print(bright_amarelo(f"\nAgência de número {agencia.numero} excluída com sucesso"))
                            else:
                                return
                    case "U":
                        numero= input_int("Insira o número da conta: ")
                        agencia = get_agencia_by_numero(numero)
                        if not agencia:
                            print(vermelho(f'Agência de número: {numero} não encontrada na Base de Dados.'))
                        else:
                            print(f"\n{LINHA_ASTERISCO}\n")
                            print(f"Conta: número: {agencia.numero} | digito: {agencia.digito} | ID: {conta.id}")
                            print(f"\n{LINHA_ASTERISCO}\n")
                            print_center('Inserir os novos dados', 34)
                            numero = input_int('Número da agência: ')
                            digito = input_int('Digito: ')
                            update_agencia(numero, digito, agencia.id)
                    case "S":
                        print_center(bright_amarelo(" SAIR :)\n"), 40)
                        break
            case "SA":
                print_center(bright_amarelo(" SAIR :)\n"), 40)
                break

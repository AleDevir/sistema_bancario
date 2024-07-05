'''
Módulo com fluxo principal do programa Administrativo.
'''
from src.repositorio.carga_db_repositorio import carregar_banco_de_dados

if __name__ == "__main__":
    carregar_banco_de_dados()

'''
model Cliente() 
'''

from src.model.base_model import BaseModel

class Cliente(BaseModel):
    '''
    Dados do cliente
    '''
    # pylint: disable=too-few-public-methods
    def __init__(
        # pylint: disable=too-many-arguments
        self,
        nome: str,
        sobrenome: str,
        idt: int,
        senha: str,
        cpf: str
    ) -> None:
        '''
        Inicialização da classe Cliente
        '''
        super().__init__(idt)
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.senha: str = senha
        self.cpf: str = cpf

    @classmethod
    def cliente(
         # pylint: disable=too-many-arguments
        cls,
        *,
        nome: str,
        sobrenome: str,
        idt: int,
        senha: str,
        cpf: str
        ) -> dict[str, str | int | bytes ]:
        '''
        Recebe os dados e retorna o Cliente(id, nome, sobrenome, cpf, senha)
        '''
        return cls(nome, sobrenome, idt, senha, cpf)

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
        cpf: int
    ) -> None:
        '''
        Inicialização da classe Cliente
        '''
        super().__init__(idt)
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.senha: str = senha
        self.cpf: int = cpf

def cliente_from_dict(data: dict[str, str | int | bytes ]) -> Cliente:
    '''
    Recebe os dados e retorna o Cliente(id, nome, sobrenome, cpf, senha)
    '''
    return Cliente(
        nome=data.get('nome', ''), # type: ignore[arg-type]
        sobrenome=data.get('sobrenome', ''), # type: ignore[arg-type]
        idt=data.get('id', 0), # type: ignore[arg-type]
        senha=data.get('senha', '123'), # type: ignore[arg-type]
        cpf=data.get('cpf', 0) # type: ignore[arg-type]
    )

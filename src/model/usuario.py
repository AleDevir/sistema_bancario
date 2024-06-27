'''
model Usuario() 
'''

from src.model.base_model import BaseModel

class Usuario(BaseModel):
    '''
    Dados do usuário
    '''
    # pylint: disable=too-few-public-methods
    def __init__(
        # pylint: disable=too-many-arguments
        self,
        nome: str,
        sobrenome: str,
        idt: int,
        senha: str,
        endereco: str,
        cpf: int
    ) -> None:
        '''
        Inicialização da classe Usuário
        '''
        super().__init__(idt)
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.senha: str = senha
        self.endereco: str = endereco
        self.cpf: int = cpf

def usuario_from_dict(data: dict[str, str | int | bytes ]) -> Usuario:
    '''
    Recebe os dados e retorna o Usuario(id, nome, sobrenome, cpf, endereco, senha)
    '''
    return Usuario(
        nome=data.get('nome', ''), # type: ignore[arg-type]
        sobrenome=data.get('sobrenome', ''), # type: ignore[arg-type]
        idt=data.get('id', 0), # type: ignore[arg-type]
        senha=data.get('senha', '123'), # type: ignore[arg-type]
        endereco=data.get('endereco', 'x'), # type: ignore[arg-type]
        cpf=data.get('cpf', 0) # type: ignore[arg-type]
    )

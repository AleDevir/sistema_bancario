'''
model Agencia()
'''

from src.model.base_model import BaseModel

class Agencia(BaseModel):
    '''
    Dados da agencia
    '''
    # pylint: disable=too-few-public-methods
    def __init__(
        self,
        idt: int,
        numero: int,
        digito: int
    ) -> None:
        '''
        Inicialização da classe Agencia
        '''
        super().__init__(idt)
        self.numero: int = numero
        self.digito: int = digito


def agencia_from_dict(data: dict[str, int]) -> Agencia:
    '''
    Recebe os dados e retorna Agencia(id, numero e digito)
    '''
    return Agencia(
        idt=data.get('id', 0),
        numero=data.get('numero', 0),
        digito=data.get('digito', 0),
    )

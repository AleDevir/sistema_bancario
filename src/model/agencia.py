'''
model Agencia()
'''
from typing import Self
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

    @classmethod
    def agencia(
         # pylint: disable=too-many-arguments
        cls,
        *,
        idt: int,
        numero: int,
        digito: int

        ) -> Self:
        '''
        Recebe os dados e retorna Agencia(id, numero, digito)
        '''
        return cls(idt, numero, digito)

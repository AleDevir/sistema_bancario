'''
model Contas()
'''
from typing import Self
from src.model.base_model import BaseModel

class Conta(BaseModel):
    '''
    Dados da conta
    tipo 1 Conta Corrente | tipo 2 Conta Poupança
    '''
    # pylint: disable=too-few-public-methods
    def __init__( # pylint: disable=too-many-arguments
        self,
        idt: int,
        numero: int,
        digito: int,
        tipo: int,
        agencia_id: int,
        cliente_id: int
    ) -> None:
        '''
        Inicialização da classe Conta
        '''
        super().__init__(idt)
        self.numero: int = numero
        self.digito: int = digito
        self.tipo: int = tipo
        self.agencia_id: int =  agencia_id
        self.cliente_id: int = cliente_id

    @classmethod
    def conta(
         # pylint: disable=too-many-arguments
        cls,
        *,
        idt: int,
        numero: int,
        digito: int,
        tipo: int,
        agencia_id: int,
        cliente_id: int

        ) -> Self:
        '''
        Recebe os dados e retorna Conta(id, numero, tipo, agencia_id, cliente_id e digito)
        '''
        return cls(idt, numero, digito, tipo, agencia_id, cliente_id)

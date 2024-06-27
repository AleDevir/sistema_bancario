'''
model Contas()
'''
from typing import Optional
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
        usuario_id: int
    ) -> None:
        '''
        Inicialização da classe Conta
        '''
        super().__init__(idt)
        self.numero: int = numero
        self.digito: int = digito
        self.tipo: int = tipo
        self.agencia_id: int =  agencia_id
        self.usuario_id: int = usuario_id

def conta_from_dict(data: dict[str, int]) -> Optional[Conta]:
    '''
    Recebe os dados e retorna Conta(id, numero, tipo, agencia_id, usuario_id e digito)
    '''
    if not data:
        return None
    return Conta(
        idt=data.get('id', 0),
        numero=data.get('numero', 0),
        digito=data.get('digito', 0),
        tipo=data.get('tipo', 0),
        agencia_id=data.get('agencia_id', 0),
        usuario_id=data.get('usuario_id', 0),
    )

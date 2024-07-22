'''
model Transacoes()
'''
from typing import Self
from datetime import datetime
from src.model.base_model import BaseModel
from src.util.data_e_hora_util import (
    converter_timestamp_to_datetime
)

class Movimentacoes(BaseModel):
    '''
    Dados da movimentação bancária de uma determinada conta do correntista.
    '''
    # pylint: disable=too-few-public-methods
    def __init__(
        # pylint: disable=too-many-arguments
        self,
        idt: int,
        valor: float,
        date: datetime,
        conta_id: int
    ) -> None:
        '''
        Inicialização da classe Transacoes
        '''
        super().__init__(idt)
        self.valor: float = valor
        self.date: datetime = date
        self.conta_id: int = conta_id

    @classmethod
    def movimentacao(
         # pylint: disable=too-many-arguments
        cls,
        *,
        idt: int,
        valor: float,
        date: int,
        conta_id: int,

        ) -> Self:
        '''
        Recebe os dados e retorna Movimentacao(id, valor, date, conta-id)
        '''
        data_hora = converter_timestamp_to_datetime(date)
        return cls(idt, valor, data_hora, conta_id)

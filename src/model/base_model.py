'''
Base Model
'''


class BaseModel():
    '''
    Classe Base dos Models
    '''
    def __init__(self, idt: int) -> None:
        '''
        Inicialização da classe
        '''
        self.id: int = idt


    def __repr__(self) -> str:
        '''
        Repr
        '''
        return f"{self.__class__.__name__}({', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])})" # pylint: disable=line-too-long


    def __str__(self) -> str:
        '''
        To String
        '''
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}" # pylint: disable=line-too-long

'''
Model Usuário

'id'    = PK - Primary Key: Chave Primária
'nome'  = AK - Alternate Key: Chave Alternativa
'''

import bcrypt
from src.model.usuario import Usuario, usuario_from_dict

USUARIOS: list[dict[str, str | int | bytes ]] = [
    {
        'nome': 'rinaldo',
        'sobrenome': 'benevides',
        'id': 1,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()),
        'endereco': 'Rua: Carvalho, n. 34 Rio de Janeiro/RJ',    
        'CPF': 45559920088
    },
    {
        'nome': 'alessandra',
        'sobrenome': 'guimarães',
        'id': 2,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()),
        'endereco': 'Rua: Raiz Forte, n. 71 Guapimirim/RJ',    
        'CPF': 95282507005 
    },
    {
        'nome': 'test',
        'sobrenome': 'test',
        'id': 3,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()), 
        'endereco': 'Rua: Teste, n. 1 teste/TE',    
        'CPF': 87315683003 
    },
    {
        'nome': 'test',
        'sobrenome': 'test',
        'id': 4,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()), 
        'endereco': 'Rua: Teste, n. 1 teste/TE', 
        'CPF': 23447087072
    },
    {
        'nome': 'test',
        'sobrenome': 'test',
        'id': 5,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()),
        'endereco': 'Rua: Teste, n. 1 teste/TE', 
        'CPF': 82160212083 
    },
]

def get_usuario_by_id(usuario_id: int) -> Usuario:
    '''
    Obter um Usuário pelo ID.
    '''
    data: dict[str, str | int | bytes ] = next((u for u in USUARIOS if u['id'] == usuario_id), {})
    return usuario_from_dict(data)

def get_usuario_by_nome(usuario_nome: str) -> Usuario:
    '''
    Obter um Usuário pelo NOME.
    '''
    data: dict[str, str | int | bytes ] =  next((u for u in USUARIOS if u['nome'] == usuario_nome), {}) # pylint: disable=line-too-long
    return usuario_from_dict(data)

def get_usuarios() -> list[Usuario]:
    '''
    Obter TODOS os Usuários.
    '''
    result: list[Usuario] = []
    for data in USUARIOS:
        result.append(
            usuario_from_dict(data)
        )
    return result

def senha_valida(usuario_id: int, senha: str) -> bool:
    '''
    Valida a senha do usuário.
    '''
    usuario = get_usuario_by_id(usuario_id)

    if not usuario:
        return False

    return bcrypt.checkpw(senha.encode(), usuario.senha.encode())

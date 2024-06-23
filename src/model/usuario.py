'''
Model Usuário

'id'    = PK - Primary Key: Chave Primária
'nome'  = AK - Alternate Key: Chave Alternativa
'''
import bcrypt

usuarios: list[dict[str, str | int | bytes ]] = [
    {
        'nome': 'rinaldo benevies',
        'id': 1,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()),
        'endereco': 'Rua: Carvalho, n. 34 Rio de Janeiro/RJ',    
        'CPF': 45559920088
    },
    {
        'nome': 'alessandra guimarães',
        'id': 2,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()),
        'endereco': 'Rua: Raiz Forte, n. 71 Guapimirim/RJ',    
        'CPF': 95282507005 
    },
    {
        'nome': 'test',
        'id': 3,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()), 
        'endereco': 'Rua: Teste, n. 1 teste/TE',    
        'CPF': 87315683003 
    },
    {
        'nome': 'test',
        'id': 4,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()), 
        'endereco': 'Rua: Teste, n. 1 teste/TE', 
        'CPF': 23447087072
    },
    {
        'nome': 'test',
        'id': 5,
        'senha': bcrypt.hashpw(b'123', bcrypt.gensalt()),
        'endereco': 'Rua: Teste, n. 1 teste/TE', 
        'CPF': 82160212083 
    },
]

def get_usuario_by_id(usuario_id: int) -> dict[str, int | str]:
    '''
    Obter um Usuário pelo ID.
    '''
    return next((u for u in usuarios if u['id'] == usuario_id), {}) # type: ignore[misc]

def get_usuario_by_nome(usuario_nome: str) -> dict[str, int | str]:
    '''
    Obter um Usuário pelo NOME.
    '''
    return next((u for u in usuarios if u['nome'] == usuario_nome), {}) # type: ignore[misc]

def get_usuarios() -> list[dict[str, str | int | bytes ]]:
    '''
    Obter TODOS os Usuários.
    '''
    return usuarios.copy()


def senha_valida(usuario_id: int, senha: str) -> bool:
    '''
    Valida a senha do usuário.
    '''
    usuario = get_usuario_by_id(usuario_id)

    if not usuario:
        return False

    return bcrypt.checkpw(senha.encode(), usuario['senha']) # type: ignore[arg-type]

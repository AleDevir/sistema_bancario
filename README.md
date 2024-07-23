
<img src="https://cdn-icons-png.flaticon.com/512/1052/1052854.png" width='40'/>  Repositório desenvolvido com Python 3.12 para fins de aprendizado, contendo estrutura de testes e checagem estática de código utilizando Pytest e Mypy.
## [![Sistema Bancario](https://img.shields.io/badge/Sistema_Bancario-gold)](https://github.com/AleDevir/sistema_bancario)

### Links Úteis:
+ [![Python](https://img.shields.io/badge/Python-blue)](https://www.python.org/downloads/)
+ [![Pylint](https://img.shields.io/badge/Pylint-yellowgreen)](https://pypi.org/project/pylint/)
+ [![Mypy](https://img.shields.io/badge/Mypy-darkblue)](https://mypy.readthedocs.io/en/stable/)
+ [![Pytest](https://img.shields.io/badge/Pytest-orange)](https://pypi.org/project/pytest/)
+ [![Bcrypt](https://img.shields.io/badge/Bcrypt-ligthbluee)](https://pypi.org/project/bcrypt/)
+ [![Python-sqlite3](https://img.shields.io/badge/Python-sqlite3-violet)](https://docs.python.org/3/library/sqlite3.html)
+ [![Tutorial-SQL](https://img.shields.io/badge/Tutorial-SQL-yellow)](https://www.sqltutorial.org/)
+ [![DB Browser for SQLite](https://img.shields.io/badge/DBBrowser-SQLite-darkgreen)](https://github.com/sqlitebrowser/sqlitebrowser/wiki)


### Diagrama Entidade Relacionamento (DER)
![DER](https://github.com/AleDevir/operacoes_bancarias_basicas/blob/main/img/der.png)

 ### Instalações:
```
# Para verificar a qualidade de código fonte.
pip install pylint --user

# Para verificar os tipos estáticos. 
pip install mypy --user

# Para testes parametrizados, acessórios e reescrita assertiva.
pip install pytest --user

# Para criptografia do tipo hash para senhas.
pip install bcrypt

#Para total de cobertura de testes.
pip install pytest-cov

```
#### Download - Visualização sqlite
[![DB4S 3.12.2](https://img.shields.io/badge/DB4S-blue)](https://www.python.org/downloads/)

### Comandos para Verificação Estática de Código (pylint e mypy):
```
# Para testar todos:
pylint *

#Para testar cada arquivo:
pylint <nome_do_arquivo.py> util

#Para testar um ou mais arquivos
mypy --show-error-codes --check-untyped-defs <nome_do_arquivo.py>  <nome_da_pasta>

# Testes com relatório de cobertura para o sonar (coverage.xml).
pytest tests/ -vv --cov=src --cov-report=xml

# Testes com relatório de cobertura exibido no console.
pytest tests/ -vv --cov=src

```

### Exemplo do relatório utilizando o pytest:
```
pytest tests/ -vv --cov=src
```
![Relatório dos testes>](https://github.com/AleDevir/operacoes_bancarias_basicas/blob/main/img/resultado_do_relatorio_cobertura_de_teste.png)






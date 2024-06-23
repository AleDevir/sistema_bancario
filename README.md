# ${\color{#b3903f} Operações Bancárias}$  
<img src="https://cdn-icons-png.flaticon.com/512/1052/1052854.png" width='40'/>  Repositório desenvolvido com Python 3.12 para fins de aprendizado, contendo estrutura de testes e checagem estática de código utilizando Pytest e Mypy.
 [Operações Bancárias](https://github.com/AleDevir/operacoes_bancarias_basicas)
 


### Links Úteis:
+ [![Python](https://img.shields.io/badge/Python-blue)](https://www.python.org/downloads/)
+ [![Pylint](https://img.shields.io/badge/Pylint-yellowgreen)](https://pypi.org/project/pylint/)
+ [![Mypy](https://img.shields.io/badge/Mypy-darkblue)](https://mypy.readthedocs.io/en/stable/)
+ [![Pytest](https://img.shields.io/badge/Pytest-orange)](https://pypi.org/project/pytest/)
+ [![Bcrypt](https://img.shields.io/badge/Bcrypt-ligthbluee)](https://pypi.org/project/bcrypt/)




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

### Comandos para Verificação Estática de Código (pylint e mypy):
```
# Para testar todos:
pylint *

#Para testar cada arquivo:
pylint <nome_do_arquivo.py> util

#Para testar um ou mais arquivos
mypy --show-error-codes --check-untyped-defs <nome_do_arquivo.py>  <nome_da_pasta>

# Testes com relatório de cobertura para o sonar (coverage.xml).
pytest tests/ -vv --cov=. --cov-report=xml

# Testes com relatório de cobertura exibido no console.
pytest tests/ -vv --cov=.

```

### Exemplo do relatório utilizando o pytest:
```
pytest tests/ -vv --cov=.
```
![Relatório dos testes>](https://github.com/AleDevir/operacoes_bancarias_basicas/blob/main/img/resultado_do_relatorio_cobertura_de_teste.png)

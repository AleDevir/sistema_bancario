# ${\color{#b3903f} Operações Bancárias}$  
<img src="https://cdn-icons-png.flaticon.com/512/1052/1052854.png" width='40'/>  Repositório desenvolvido para fins de aprendizado, com estrutura de testes e checagem estática de código utilizando Pytest e Mypy.
 [Operações Bancárias](https://github.com/AleDevir/operacoes_bancarias_basicas)


<sub>Repositório criado com Python 3.12 </sub><img src="https://docs.python.org/pt-br/3/_static/py.svg" alt="imagem logo python" width="20"/> 

### Links Úteis:
+ [Python Pages](https://www.python.org/downloads/)
  
+ [![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
+ [Mypy Pages](https://mypy.readthedocs.io/en/stable/getting_started.html) 
+ [Pytest Pages](https://pypi.org/project/pytest/) 



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

### Exemplo teste com relaório do pytest:
```
pytest tests/ -vv --cov=.
```
![Relatório dos testes>](https://github.com/AleDevir/operacoes_bancarias_basicas/blob/main/img/resultado_do_relatorio_cobertura_de_teste.png)

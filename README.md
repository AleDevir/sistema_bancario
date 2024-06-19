 


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

### Comando para Verificação Estática de Código (pylint e mypy):
```
# Para testar todos:
pylint *

#Para testar cada arquivo:
pylint operacoes_bancarias.py util

#Para testar um ou mais arquivos
mypy --show-error-codes --check-untyped-defs operacoes_bancarias.py  util

# Testes com relatório de cobertura para o sonar (coverage.xml).
pytest tests/ -vv --cov=. --cov-report=xml

# Testes com relatório de cobertura exibido no console.
pytest tests/ -vv --cov=.

```
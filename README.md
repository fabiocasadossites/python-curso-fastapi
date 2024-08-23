# Curso de FastAPI
Curso de Fastapi com python, feito no canal do youtube Eduardo


Material em texto: https://fastapidozero.dunossauro.com/
Repositório no GIT: https://github.com/dunossauro/fastapi-do-zero
Grupo no Telegram do curso: https://t.me/fastapicomdunossauro

### Ferramentas

- pyenv - https://github.com/pyenv/pyenv
- pipx - https://github.com/pypa/pipx
- poetry - https://python-poetry.org/
- ignr - https://github.com/Antrikshy/ignr.py
- gh - https://github.com/cli/cli#installation

### Versão

- python = "3.12.*"
- fastapi = "^0.112.1"

- Criação de variáveis e commits em inglês

### Criando ambiente virtual

Dentro da pasta do projeto execute no mesmo local que está o arquivo pyproject.toml.
````
poetry install
````

Para ativar o venv o ambiente virtual, faça isso dentro da raiz do projeto, utilize:
````
poetry shell
````

### Comando de execução
Estas configurações estão dentro do arquivo pyproject.toml

Para executar o fastapi
````
task run
````

Rodar o linter
````
task lint
````

Rodar a formatação do código
````
task format
````

Rodar o pré-teste
````
task pre_test
````

Rodar os testes
````
task test
````

Criar o arquivo em html dos testes
````
task post_test
````

### Dependências

Fastapi - https://fastapi.tiangolo.com/
````
poetry add fastapi
````

Ruff linter de código - https://docs.astral.sh/ruff/
````
poetry add --group dev ruff
````

Pytest, framework de teste em python - https://docs.pytest.org/en/stable/
````
poetry add --group dev pytest pytest-cov
````

Taskipy, framework de criação de comandos - https://github.com/taskipy/taskipy
````
poetry add --group dev taskipy
````

Sqlalchemy, ORM banco de dados - https://www.sqlalchemy.org/
````
poetry add sqlalchemy
````

Pydantic, configurações de banco de dados - https://docs.pydantic.dev/latest/
````
poetry add pydantic-settings
````

Alembic, migration de banco de dados - https://alembic.sqlalchemy.org/en/latest/
````
poetry add alembic
````
 - Iniciando o local das migrações(só precisa rodar uma única vez):
````
alembic init migrations
````
 - Gerar os comandos para criar uma migração
````
alembic revision --autogenerate -m "create table"
````
 - Gerar uma migração depois que atualizar o comando acima para atualizar o códigos das tabelas.
````
alembic upgrade head
````
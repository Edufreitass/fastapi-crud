# Criando o primeiro CRUD com FastAPI

## Criando o projeto

    mkdir fastapi-crud
    cd fastapi-crud

Uma vez dentro do diretório do projeto nós vamos criar e ativar um ambiente virtual com os seguintes comandos:
- No Linux e MacOS
```
python3 -m venv .venv
source .venv/bin/activate
```
- No Windows
```
python -m venv .venv
.\.venv\Scripts\activate
```
Agora que estamos com o nosso ambiente virtual ativo podemos realizar a instalação das bibliotecas necessárias utilizando o PIP.
```
pip install fastapi uvicorn[standard] sqlalchemy
```
Ou podemos optar por criar um arquivo `requirements.txt` na pasta raiz do projeto e inserir as dependências neste arquivo
```
fastapi
uvicorn[standard]
sqlalchemy
```

Após a execução do comando acima teremos feito a instalação das seguintes bibliotecas:

    FastAPI: Microframework voltada para o desenvolvimento de Web APIs;
    Uvicorn: Web server ASGI implementado em Python, necessário para a execução do nosso projeto;
    SQLAlchemy: ORM bastante popular dentro do ecossistema Python.

Agora nós já estamos com o nosso ambiente preparado e podemos dar prosseguimento com o desenvolvimento de nossa API.

## Para executar o projeto

```bash
$ (venv) PS D:\workspace\fastapi-crud> uvicorn app.main:app --reload

INFO:     Will watch for changes in these directories: ['D:\\workspace\\fastapi-crud']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [26692] using WatchFiles
INFO:     Started server process [30120]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

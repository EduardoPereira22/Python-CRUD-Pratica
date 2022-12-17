#imprortando o flask para uasrs
from flask import Flask
from db import database

app = Flask(__name__)
#definindo a rota e a função com o return
@app.route("/")
def teste():
    return "opa,pegou"
#definindo a rota e fazer um objeto
@app.route("/teste1")
def nome():
    return{"nome":"eduardo", "cidade":"recife"}
#usando o nome para carregar o nome que for dito na url e tb inserindo o dado que for passado na url depois do bv ,no banco de dados
@app.route("/bv/<string:nome>")
def bv(nome):
    database.append(nome)
    return f"bem vindo {nome}"
#essa rota vai imprimir o nome das pessoas citadas na rota de cima
@app.route("/listar")
def listar():
    return "\n" .join(database)

if __name__ == "__main__":
    app.run(debug=True)



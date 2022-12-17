from flask import  Flask, abort, request

app = Flask(__name__)


database = {}


#usando o metodo get
@app.route("/")
def home():
    return "Olá Amigo!"


#usando o metodo post para adicionar dados ao database , se executar ele retorna Ola você, atraves do request do flask e ela obtém as informações envidas atraves do http
#cessa o campo nome e guarda ele no banco de dados como sendo o registro do usuario

@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    name = data.pop("nome")
    database [name] = data
    return "Olá Você"
#obtendo os dados salvos no codigo de cima, caso o nome não esteja no banco de dados ele retorna o erro 404, caso contrario obtem-se a informação e retorna elas
@app.route("/user/<string:name>")
def get_user(name):
   if not name in database:
       abort(404)

   data = database[name]
   return data

#usando o put para atualizar as informações caso o name não exista no banco de dados ele retorna o erro 404, caso exista obtem-se os dados atraves do request e sobrescreve
#a informação
@app.route("/user/<string:name>", methods=["PUT"])
def update_user(name):
   if name not in database:
       abort(404)
 
   data = request.json
   database[name] = data
   return data

#usando o delete para deletar o nome
@app.route("/user/<string:name>", methods=["DELETE"])
def remover_usuario(name):
 if name not in database:
    abort(404)
 del database[name]
 return "Úsuario excluido"

    
    

if __name__ == "__main__":
    app.run(debug=True)

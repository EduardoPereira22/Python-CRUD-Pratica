from flask import Blueprint, request
from config.database import connection, cursor
import bcrypt

users_bp = Blueprint(name="users", import_name=__name__, url_prefix="/users")

def _hash_password(password):
  byte_password = password.encode("utf-8")
  return bcrypt.hashpw(byte_password, bcrypt.gensalt())

# localhost:5000/users/
# usuario que tenha: nome, email, senha e data de criacao
@users_bp.route("/", methods=["POST"])
def create():
  body = request.json
  email = body.get("email")
  senha = body.get("senha")
  # SUPER INSEGURO
  # "str1" + "str2"
  # "str".format()
  # sql = f"INSERT INTO users(password, email) VALUES('{senha}', '{email}')"
  sql = "INSERT INTO users(password, email) VALUES(%s, %s)"
  create_tuple = (_hash_password(senha), email)
  cursor.execute(sql, create_tuple)
  connection.commit()
  return {"message": "usuário criado com sucesso", "data" : { "email": email, "senha": senha}}, 201


# Precisamos de paginação!
@users_bp.route("/")
def read_all():
  sql = "select * from users;"
  cursor.execute(sql)
  users = cursor.fetchall()
  return users


@users_bp.route("/<id>")
def read_one(id):
  sql = "select * from users u WHERE u.id = %s"
  read_tuple = (id,)
  cursor.execute(sql, read_tuple)
  user = cursor.fetchone()
  response = { "email": user[2], "senha": user[1]}
  return response, 200


@users_bp.route("/<id>", methods=["PUT"])
def update(id):
  body = request.json
  nova_senha = body.get("senha") # body["senha"]
  sql = "UPDATE users SET password = %s WHERE id = %s"

  try:
    cursor.execute(sql, (_hash_password(nova_senha), id))
    connection.commit()
  except:
    print("faça alguma coisa")

  return {"message": "usuário atualizado com sucesso!", "nova_senha": nova_senha }, 200


@users_bp.route("/<id>", methods=["DELETE"])
def delete(id):
  sql = "DELETE FROM users WHERE id = %s"
  cursor.execute(sql, (id,))
  connection.commit()
  connection.close()
  cursor.close()
  return {}, 200

from flask import Blueprint, request
from config.database import connection, cursor
import bcrypt

users_bp = Blueprint(name="users", import_name=__name__, url_prefix="/users")

def _hash_password(password):
  byte_password = password.encode("utf-8")
  return bcrypt.hashpw(byte_password, bcrypt.gensalt())


@users_bp.route("/", methods=["POST"])
def create():
  body = request.json
  email = body.get("email")
  senha = body.get("senha")
  username = body.get("username")
  aten = body.get("aten")
  dinheiro = body.get("dinheiro")
  npedidos = body.get("npedidos")
  vip = body.get("vip")

  sql = "INSERT INTO accounts (password, email, username, aten, dinheiro, npedidos, vip) VALUES(%s, %s, %s , %s, %s , %s, %s)"
  create_tuple = (_hash_password(senha), email, username, aten, dinheiro, npedidos, vip)
  cursor.execute(sql, create_tuple)
  connection.commit()
  connection.close()
  cursor.close()
  return {"message": "usuário criado com sucesso", "data" : {"email": email, "numero de bairros atendidos": aten}}, 201



@users_bp.route("/")
def read_all():
  sql = "select * from accounts;"
  cursor.execute(sql)
  users = cursor.fetchall()
  connection.close()
  cursor.close()
  return users


@users_bp.route("/<id>")
def read_one(id):
  sql = "select * from accounts WHERE user_id = %s"
  read_tuple = (id,)
  cursor.execute(sql, read_tuple)
  user = cursor.fetchone()
  response = { "userid":user[0], "username":user[1],"email":user[3], "created_on":user[4],"aten":user[5],"dinheiro":user[6],"npedidos":user[7],"NºclientesVip":user[8]}
  return response, 200


@users_bp.route("/<id>", methods=["PUT"])
def update(id):
  body = request.json
  nova_senha = body.get("senha") 
  sql = "UPDATE accounts SET password = %s WHERE user_id = %s"

  try:
    cursor.execute(sql, (_hash_password(nova_senha), id))
    connection.commit()
  except:
    print("faça alguma coisa")

  return {"message": "usuário atualizado com sucesso!", "nova_senha": nova_senha }, 200


@users_bp.route("/<id>", methods=["DELETE"])
def delete(id):
  sql = "DELETE FROM accounts WHERE user_id = %s"
  cursor.execute(sql, (id,))
  connection.commit()
  connection.close()
  cursor.close()
  return {}, 200

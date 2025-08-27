from flask import Flask
from .controllers.task_controller import TaskController
from .controllers.user_controller import UserController
from .config import Config
from models.task import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db= SQLAlchemy()

app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.add_url_rule('/tasks',TaskController.list_tasks,methods=['GET'])
app.add_url_rule('/tasks/new',TaskController.create_task,methods=['GET','POST'])
app.add_url_rule('/tasks/update/<int:id>',TaskController.update_task_status,methods=['POST'])
app.add_url_rule('/tasks/delete/<int:id>',TaskController.delete_task,methods=['DELETE'])

app.add_url_rule('/','index',UserController.index,methods=['GET'])
app.add_url_rule('/contact','contact',UserController.contact,methods=['GET','POST'])

if __name__ == "__main__":
    app.run(debug=True)


'''users = {}
id = 1

@app.route("/users", methods=["POST"])
def criar_usuario():
    global id
    dict = request.json
    user = {"id": id, "nome": dict["nome"], "email": dict["email"]}
    users[id] = user
    id += 1
    return jsonify(user),201

@app.route("/users", methods =["GET"])
def listar_usuarios():
    return jsonify (list(users.values())), 200

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "Usuário não encontrado"}), 404

@app.route("/users/<int:user_id>", methods=["PUT"])
def atulizar_usuario(user_id):
    data = request.json
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404
    user["nome"] = data.get("nome", user["nome"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user), 200

@app.route("/users/<int:user_id>", methods=["DELETE"])
def deletar_usuario(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "Usuário excluído com sucesso"}), 200
    return jsonify({"error": "Usuário não encontrado"}), 404'''



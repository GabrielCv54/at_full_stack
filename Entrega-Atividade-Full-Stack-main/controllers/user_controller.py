from flask import request,Blueprint,jsonify
from models.user import UserNotFound,create_new_user,delete_user,get_all_users,update_user
from config import db

user_blueprint = Blueprint('users_routes',__name__)

@user_blueprint.route('/users',methods=['GET'])
def show_all():
    return get_all_users(),200

@user_blueprint.route('/users',methods=['POST'])
def create_new():
    data = request.get_json()
    create_new_user(data)
    return jsonify({'Sucesso':'Usuário criado com sucesso!'}),201

@user_blueprint.route('/users/<int:id>',methods=['PUT'])
def updating(id):
    try:
        user = request.json
        update_user(id,user)
        return jsonify({'Sucesso':'Usuário atualizado!!!'}),201
    except UserNotFound:
        return jsonify({'Erro':'Usuário não encontrado!!'}),404


@user_blueprint.route('/users/<int:id>',methods=['DELETE'])   
def delete(id):
    try:
      delete_user(id)
      return jsonify({'Sucesso':'Usuário deletado!!'})
    except UserNotFound:
        return jsonify({'Erro':'Usuário não encontrado'}),404


'''class UserController:
    @staticmethod
    def index():
        users = User.query.all()
        return render_template('index.html',users=users)
    
    @staticmethod
    def contact():
        if request.method == 'POST':
            id = request.form['id']
            nome = request.form['nome']
            email = request.form['email']
            
            user = User(id=id,nome=nome,email=email)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('index'))
        return render_template('contact.html')'''

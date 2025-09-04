from flask import request,Blueprint,jsonify
from models.user import UserNotFound,create_new_user,delete_user,get_all_users,update_user

user_blueprint = Blueprint('users_routes',__name__)

@user_blueprint.route('/users',methods=['GET'])
def show_all():
    """
    Lista de Usuários
    ---
    tags:
       - Usuários
    description: Retorna todos os usuários
    responses:
      200:
         description: Todos os usuários.

    """
    #...
    return get_all_users(),200

@user_blueprint.route('/users',methods=['POST'])
def create_new():
    """
    Cria um novo usuário
    ---
    tags:
      - Usuários
    parameters:
      - in: body
        name: body
        schema:
          id : User
          required:
          - id
          - nome
          properties:
           id:
            type: integer
            description: Id do usuário
           nome:
            type: string
            description: Nome do usuário
           email:
             type: string
             description: Email do usuário
    responses:
      201:
        description: Usuário criado!!
        schema:
        id: UserResponse
        properties:
            id:
                type: integer
            nome:
                type: string
            email:
                type: string
             
    """
    #...

    data = request.get_json()
    create_new_user(data)
    return jsonify({'Sucesso':'Usuário criado com sucesso!'}),201

@user_blueprint.route('/users/<int:id>',methods=['PUT'])
def updating(id):
    """
    Atualizar um usuário
    ---
    tags: 
     - Usuários
    parameters:
     - in: path
       name: id
       type: integer
       required: true
       description: id do usuário
     - in: body
       name: body
       schema: 
        id: UserUpdate
        properties:
         id:
           description: id do usuário
           type: integer
         nome:
           description: nome do usuário
           type: string
         email:
           description: email do usuário
           type: string

    responses:
      201:
        description: Usuário atualizado!
      404:
        description: Usuário não encontrado!
         
    """
    #...

    try:
        user = request.json
        update_user(id,user)
        return jsonify({'Sucesso':'Usuário atualizado!!!'}),201
    except UserNotFound:
        return jsonify({'Erro':'Usuário não encontrado!!'}),404


@user_blueprint.route('/users/<int:id>',methods=['DELETE'])   
def delete(id):
    """
    Deletar um usuário
    ---
    tags:
     - Usuários
    parameters:
     - in: path
       name: id
       type: integer
       required: true
       description: id do usuário

    responses:
      204:
       description: Usuário deletado!!
      404:
       description: Usuário não encontrado
        
    
    """
    #...

    try:
      delete_user(id)
      return jsonify({'Sucesso':'Usuário deletado!!'}),204
    except UserNotFound:
        return jsonify({'Erro':'Usuário não encontrado'}), 404



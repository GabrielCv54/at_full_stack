from flask import jsonify,request,Blueprint
from models.task import create_one_task,del_task,get_all_tasks,update_task,TaskNotFound

task_blueprint = Blueprint('tasks_routes',__name__)

@task_blueprint.route('/tasks',methods=['GET'])
def get_tasks():
    """
    Listar todas as tarefas
    ---
    tags:
        - Tarefas
    description: Retorna todas as tarefas.
    responses:
        200 :
            description: Um objeto json com as tarefas.
    """
    #...

    return jsonify(get_all_tasks()),200


@task_blueprint.route('/tasks',methods=['POST'])
def create():
    """
    Criar uma nova tarefa
    ---
    tags:
        - Tarefas
    parameters:
        - in: body
          name: body
          schema:
             id: Task
             required:
             - title
             - user_id
             properties:
              id:
                type: integer
                description: Id da tarefa
              title:
                type : string
                description : título da tarefa
              description:
                type: string
                description : Descrição sobre a tarefa
              status:
                type : string
                description : status da tarefa
              user_id:
                type: integer
                description : Usuário responsável
    responses:
        201 :
            description: Tarefa criada!!.
            schema:
            id: TaskResponse
            properties:
                id:
                  type: integer
                title:
                  type: string
                description:
                    type: string
                status:
                    type: string
                user_id:
                   type: integer

    """
    #...

    data = request.get_json()
    create_one_task(data)
    return jsonify({'Sucesso':'Tarefa criada com sucesso!'}),201


@task_blueprint.route('/tasks/<int:id>',methods=['PUT'])
def update(id):
    """
   Atualizar tarefa
    ---
    tags:
        - Tarefas
    parameters:
      - in: path
        name: id
        type: integer
        required: true
        description: id da tarefa.
      - in: body
        name: body
        schema:
         id: TaskUpdate
         properties:
           title:
             type: string
             description: título da tarefa
           status:
             type: string
             description: status da tarefa 
           description:
             type: string
             description: descrição da tarefa 
           user_id:
             type: integer
             description : id do usuário responsável

    responses:
        201:
            description: Tarefa Atualizada com sucesso!!
        404:
            description:  tarefa com id não encontrado.
    """
    #...

    try:
        data_ = request.json
        update_task(id,data_)
        return jsonify({'Sucesso':'Tarefa atualizada com sucesso!'}),201
    except TaskNotFound:
        return jsonify({'Erro':'Tarefa não encontrada'}),404


@task_blueprint.route('/tasks/<int:id>',methods=['DELETE'])
def delete(id):
    """
    Deletar uma tarefa
    ---
    tags:
        - Tarefas
    parameters:
      - in: path
        name: id 
        type: integer
        required: true
        description: id da tarefa a ser excluída
        
    responses:
        204:
            description: Tarefa excluída com sucesso!!.
        404:
            description: tarefa com id não encontrado.
    """
    #...
    try:
        del_task(id)
        return jsonify({'Sucesso':'Tarefa excluída com sucesso!'}),200
    except TaskNotFound:
        return jsonify({'Erro':'Tarefa não encontrada'}),404


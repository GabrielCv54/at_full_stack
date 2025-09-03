from flask import jsonify,request,Blueprint
from models.task import create_one_task,del_task,get_all_tasks,update_task,TaskNotFound
from config import db

task_blueprint = Blueprint('tasks_routes',__name__)

@task_blueprint.route('/tasks',methods=['GET'])
def get_tasks():
    """
    Listar todas as tarefas
    ---
    tags:
        -tasks
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
        -tasks
    description: Cria uma nova tarefa
    responses:
        201 :
            description: O objeto json original ,com a nova tarefa já inserida.
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
        -tasks
    description: Atualiza uma tarefa, pegando o id
    responses:
        201:
            description: Um json de sucesso.
        404:
            description: um json de erro, tarefa com id não encontrado.
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
        -tasks
    description: Deleta uma tarefa pelo id
    responses:
        200 :
            description: Um json de sucesso.
        404:
            description: Um json de tarefa com id não encontrado.
    """
    #...
    try:
        del_task(id)
        return jsonify({'Sucesso':'Tarefa excluída com sucesso!'}),200
    except TaskNotFound:
        return jsonify({'Erro':'Tarefa não encontrada'}),404


'''class TaskController:
    @staticmethod
    def list_tasks():
            tasks = Task.query.all()
            return render_template('tasks.html',tasks=tasks)
    
    @staticmethod
    def create_task():
           if request.method == 'POST':
              data = request.form
              task = Task(id=data['id'],title=data['title'],description=data['description'],status=data['status'],user_id=data['user_id'])
              db.session.add(task)
              db.session.commit()          
              return redirect(url_for('list_tasks'))
           
           users = User.query.all()
           return render_template('create_task.html',users=users)
    
    @staticmethod
    def update_task_status(id):
                task = Task.query.get(id)
                if task:
                        task.status = 'Concluído'                 
                        db.session.commit()
                        return redirect(url_for('list_tasks'))
                
                tasks = Task.query.all()
                return render_template('tasks.html',tasks=tasks)
           
    @staticmethod
    def delete_task(id):
            task = Task.query.get(id)
            if task:
                db.session.delete(task)
                db.session.commit()
                return redirect(url_for('list_tasks'))
            return render_template('tasks.html')
     '''
          

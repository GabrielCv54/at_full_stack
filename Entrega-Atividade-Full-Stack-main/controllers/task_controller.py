from flask import jsonify,request,Blueprint
from models.task import create_one_task,del_task,get_all_tasks,get_task,update_task,TaskNotFound
from models.user import User
from config import db

task_blueprint = Blueprint(__name__)

@task_blueprint.route('/tasks',methods=['GET'])
def get_tasks():
    return jsonify(get_all_tasks()),200


@task_blueprint.route('/tasks',methods=['POST'])
def create():
    data = request.get_json()
    create_one_task(data)
    return jsonify({'Sucesso':'Tarefa criada com sucesso!'}),201

@task_blueprint.route('/tasks/<int:id>',methods=['PUT'])
def update(id):
    try:
        data_ = request.json
        update_task(id,data_)
        return jsonify({'Sucesso':'Tarefa atualizada com sucesso!'}),201
    except TaskNotFound:
        return jsonify({'Erro':'Tarefa não encontrada'}),404

@task_blueprint.route('tasks/<int:id>',methods=['DELETE'])
def delete(id):
    try:
        del_task(id)
        return jsonify({'Sucesso':'Tarefa excluída com sucesso!'}),204
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
          

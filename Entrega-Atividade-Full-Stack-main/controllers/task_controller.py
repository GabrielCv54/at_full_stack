from App import app,request,jsonify
from flask import render_template,redirect,url_for
from models.task import (create_one_task,del_task,get_all_tasks,update_task,TaskNotFound)

class Controller:
    @staticmethod
    def list_tasks():
        try:
            tasks = get_all_tasks()
            return jsonify(tasks),200
        except TaskNotFound:
            return jsonify({'Erro':'Tarefa não cadastrada!'}),404
        
    @staticmethod
    def create_task(data):
        data = request.get_json()
        create_one_task(data)
        return jsonify({'Sucesso':'Tarefa criada!!'}),201
    
    @staticmethod
    def update_task_status(id):
        try:
            update = request.json
            update_task(id,update)
            return jsonify({'Sucesso':'Tarefa atualizada!!'}),201
        except TaskNotFound:
            return jsonify({'Erro':'Tarefa não encontrada!!'}),404
    
    @staticmethod
    def delete_task(id):
        try:
            del_task(id)
            return jsonify({'Sucesso':'Tarefa Excluída!!'}),204
        except TaskNotFound:
            return jsonify({'Erro':'tarefa não encontrada'}),404

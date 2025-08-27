from flask import render_template,redirect,url_for,jsonify,request
from models.task import Task
from models.user import User
from config import db

class TaskController:
    @staticmethod
    def list_tasks():
            tasks = Task.query.all()
            return render_template('tasks.html',tasks=tasks)
    
    @staticmethod
    def create_task():
           if request.method == 'POST':
              data = request.form
              task = Task(title=data['title'],description=data['description'],status=data['status'],user_id=data['user_id'])
              db.session.add(task)
              db.session.commit()          
              return redirect(url_for('list_tasks'))
           
           users = User.query.all()
           return render_template('new_task.html',users=users)
    @staticmethod
    def update_task_status(id):
            task = Task.query.get(id)
            if task:
                  task.status = 'concluído'                  
                  db.session.commit()
                  return redirect(url_for('list_tasks'))
            return render_template('tasks.html')
           
    @staticmethod
    def delete_task(id):
            task = Task.query.get(id)
            db.session.delete(task)
            db.session.commit()
            return redirect(url_for('list_tasks') )
     
          

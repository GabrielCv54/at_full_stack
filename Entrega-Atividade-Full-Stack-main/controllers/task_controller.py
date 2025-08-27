from flask import render_template,redirect,url_for,jsonify,request
from models.task import Task,db

class TaskController:
    @staticmethod
    def list_tasks():
            tasks = Task.query.all()
            return render_template('tasks.html',tasks=tasks)
    
    @staticmethod
    def create_task():
           if request.method =='POST':
              title =  request.form['title']  
              description = request.form['description']
              status = request.form['status']
              user_id = request.form['user_id']

              task = Task(title=title,description=description,status=status,user_id=user_id)
              db.session.add(task)
              db.session.commit()

         
           return render_template('tasks.html')
    
    @staticmethod
    def update_task_status():
            if request.method == 'POST':
                  request.form['status'] = 'Concluído'
                  db.session.commit()

            return render_template('create_task.html')
           
    @staticmethod
    def delete_task(id):
            task = Task.query.get(id)
            db.session.delete(task)
            db.session.commit()
            return render_template('tasks.html') 
     
          

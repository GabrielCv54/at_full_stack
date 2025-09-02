from config import db

class Task(db.Model):
   __tablename__ ='tasks'

   id = db.Column(db.Integer,primary_key=True,nullable=False,auto_increment=True)
   title = db.Column(db.String,nullable=False)
   description = db.Column(db.String(150))
   status = db.Column(db.String,default='Pendente',nullable=False)
   user_id = db.Column(db.ForeignKey('users.id'))

   def __init__(self,id,title,description,status,user_id):
      self.id = id
      self.title = title
      self.description = description
      self.status = status
      self.user_id = user_id

   def dictionary(self):
      return {
         'id':self.id,
         'title':self.title,
         'description':self.description,
         'status':self.status,
         'user_id':self.user_id
         }
   
class TaskNotFound(Exception):
   pass

def get_all_tasks():
   tasks = Task.query.all()
   return [task.dictionary() for task in tasks]
   
def create_one_task(data):
   data = Task(id=data['id'],title=data['title'],description=data['description'],status=data['status'],user_id=data['user_id'])
   db.session.add(data)
   db.session.commit()

def update_task(id,data):
   task_updated = Task.query.get(id)
   if not task_updated:
      raise TaskNotFound
   task_updated.id = data['id']
   task_updated.title = data['title']
   task_updated.description = data['description']
   task_updated.status = data['status']
   task_updated.user_id = data['user_id']
   db.session.commit()

def del_task(id):
   deleted = Task.query.get(id)
   if not deleted:
      raise TaskNotFound
   db.session.delete(deleted)
   db.session.commit()
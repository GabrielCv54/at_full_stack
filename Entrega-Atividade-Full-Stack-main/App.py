from controllers.task_controller import task_blueprint
from controllers.user_controller import user_blueprint
from config import Config,app,db


app.config.from_object(Config)

db.init_app(app)


app.register_blueprint(task_blueprint)
app.register_blueprint(user_blueprint)


with app.app_context():
    db.create_all()
'''app.add_url_rule('/tasks',endpoint='list_tasks',view_func=TaskController.list_tasks,methods=['GET'])
app.add_url_rule('/tasks/new',endpoint='create_task',view_func=TaskController.create_task,methods=['GET','POST'])
app.add_url_rule('/tasks/update/<int:id>',endpoint='update_task_status',view_func=TaskController.update_task_status,methods=['GET','POST'])
app.add_url_rule('/tasks/delete/<int:id>',endpoint='delete_task',view_func=TaskController.delete_task,methods=['GET','POST'])

app.add_url_rule('/',endpoint='index',view_func=UserController.index,methods=['GET'])
app.add_url_rule('/contact',endpoint='contact',view_func=UserController.contact,methods=['GET','POST'])'''

if __name__ == "__main__":
    app.run(debug=True)
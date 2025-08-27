from App import app
from flask import request,render_template,redirect,url_for
from models.user import User,db

'''users = {}
id = 1'''

class UserController:
    @staticmethod
    def index():
        users = User.query.all()
        return render_template('index.html',users=users)
    
    @staticmethod
    def contact():
        if request.method == 'POST':
            name = request.form['nome']
            email = request.form['email']
            
            user = User(name=name,email=email)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('index'))
        return render_template('contact.html')

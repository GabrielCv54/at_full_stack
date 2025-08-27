from flask import request,render_template,redirect,url_for,make_response
from models.user import User
from config import db

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
            id = request.form['id']
            nome = request.form['nome']
            email = request.form['email']
            
            user = User(id=id,nome=nome,email=email)
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('index'))
        return render_template('contact.html')

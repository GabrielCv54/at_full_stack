from config import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    nome = db.Column(db.String,nullable=False)
    email = db.Column(db.String)

    def __init__(self,id,nome,email):
        self.id = id
        self.nome = nome
        self.email = email
'''
    def dici(self):
        return {'id':self.id,'nome':self.nome,'email':self.email}
    
class UserNotFound(Exception):
    pass

def get_all_users():
    users = User.query.all()
    return [us.nome for us in users]

def get_one_user(id):
    user = User.query.get(id)
    if not user:
        raise UserNotFound
    return user.dici

def create_new_user(dados):
    user = User(id=dados['id'],nome=dados['nome'],email=dados['email'])
    db.session.add(user)
    db.session.commit()

def update_user(id,dados):
    user = User.query.get(id)
    if not user:
        raise UserNotFound
    user.id = dados['id']
    user.nome = dados['nome']
    user.email = dados['email']
    db.session.commit()

def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()'''
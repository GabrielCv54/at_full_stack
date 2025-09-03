from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger


app = Flask(__name__)
swagger = Swagger(app,template={
            "info":{
             "title":'API Tarefas',
            "description":"Api de gerencimento de tarefas",
            "version":'1.0'
                }
                 })


db = SQLAlchemy()


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = 'database.db'

def create_app():
  app = Flask(__name__)
  app.config['SECRETE_KEY'] = '12345678'
  
  app.config['SQL_ALCHEMY_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)

  from .views import views

  app.register_blueprint(views, url_prefix='/')

  from .models import Notes 

  return app

def create_databse(app):
  if not path.exists('website/'+ DB_NAME):
    db.create_all(app = app)
    print("Database Created")
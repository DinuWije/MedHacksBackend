import os
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = 'sqlite:///{}'.format(os.path.join(project_dir, "userdatabase.db"))


app = Flask(__name__)
app.config['SECRET_KEY'] = '7651628nyh0r13ht0c676dgedw345grwe424'
app.config['SQLALCHEMY_DATABASE_URI'] = database_file

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

engine = db.create_engine(database_file, {})
connection = engine.connect()

from app import routes
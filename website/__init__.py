from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY']= 'qwerty'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'

db = SQLAlchemy(app)
from website import routes

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_wtf import Form
app = Flask(__name__)

#Secret Key
app.config['SECRET_KEY'] = '0a907654f51cb16237bd4881a661fc5a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

db.create_all()

#Avoid circular imports
from droid import Routes

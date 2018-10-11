import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

#creating instance of LoginManager
login_manager = LoginManager()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'flask_login.sqlite') 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#create db
db = SQLAlchemy(app)
#perform Migrations
Migrate(app,db)

#pass in application to LoginManager, configure management of login users
login_manager.init_app(app)

# Tell users what view to go to when they need to login.
login_manager.login_view = 'login'







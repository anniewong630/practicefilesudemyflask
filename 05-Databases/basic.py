import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#gets the directory name
basedir = os.path.abspath(os.path.dirname(__file__))
#print(basedir)

app = Flask(__name__)

#Connects Flask app to DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#allows Flask to talk to SQLAlchemy so we can use Python instead of SQL syntax
db = SQLAlchemy(app)

Migrate(app,db)
#########################################################

class Puppy(db.Model):

    #Manual table name choice
    __tablename__ = 'puppies'

    #Primary Key Column 
    id = db.Column(db.Integer, primary_key = True)
    #Puppy name column
    name = db.Column(db.Text)
    #Puppy age Column
    age = db.Column(db.Integer)
    #Breed
    breed = db.Column(db.Text)


    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed
    
    def __repr__(self):
        return f"Puppy {self.name} is {self.age} years old"


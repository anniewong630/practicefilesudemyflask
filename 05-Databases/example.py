import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'datasqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app,db)

##################################

class Puppy(db.Model):
    #tablename
    __tablename__ = 'puppies'

    #PRIMARY KEY ID (column)
    id = db.Column(db.Integer,primary_key=True)

    #column name NAME
    name = db.Column(db.Text)

    #one to many relationship 
    #toys is connected to Toy Model class 
    #backreference in the other model, related to Toy model and Puppy model 
    toys = db.relationship('Toy', backref='puppy', lazy='dynamic')

    #One to one relationship
    #one puppy to one owner
    #by default it is true, one to many it is true, list of possible toys 
    #no need for a list of owners 
    owner = db.relationship('Owner', backref='puppy', uselist=False)

    #METHOD - to create and instance of Puppy - has one parameter (name)
    def __init__ (self, name):
        self.name = name
    
    #representation when you print out puppy 
    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner name is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and puppy has no owner yet."

    #method how many toys puppy has
    #since uselist is default by true, toys is a list
    def report_toys(self):
        print("Here are a list of toys: ")
        for toy in self.toys:
            print(toy.item_name) 


class Toy(db.Model):
    __tablename__ = 'toys'

    #Primarykey ID
    id = db.Column(db.Integer,primary_key=True)

    #column name: Item Name (name of toy)
    item_name = db.Column(db.Text)

    #connect puppy to toy (FK)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))


    #to create a toy
    def __init__(self,item_name, puppy_id):
        self.item_name = item_name
        self.puppy_id = puppy_id


class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key=True)

    name = db.Column(db.Text)

    #connect owner to puppy
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))


    def __init__(self, name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id






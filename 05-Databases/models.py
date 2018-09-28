import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#gets directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


class Puppy(db.Model):
    #tablename - puppies
    __tablename__ = 'puppies'

    #Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    #one to many relationship (one puppy can have many toys)
    toys = db.relationship('Toy',backref='puppy',lazy='dynamic')

    #one to one relationship (one puppy per owner)
    owner = db.relationship('Owner',backref='owner',uselist=False)

    #creating puppy object
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Puppy name is {self.name} and owner is {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and no owner is assigned yet."

    def report_toys(self):
        print('Here are my toys.')
        for toy in self.toys:
            print(toy.item_name)

    
class Toy(db.Model):
    __tablename__ = 'toys'

    id = db.Column(db.Integer,primary_key=True)
    item_name = db.Column(db.Text)
    #connect toy with puppy by using foreign key
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies_id'))

    #creating toy object
    def __init__(self,name, puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    
class Owner(db.Model):
    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    #puppies<--name of table (FK)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies_id'))

    #creating owner object
    def __init__(self, name,puppy_id):
        self.name = name    
        self.puppy_id = puppy_id

        






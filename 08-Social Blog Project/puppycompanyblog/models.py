#models.py
from puppycompanyblog import db, login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin 
#allow us to have functionality- is_authenticate, is_activate, etc.
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    #link to image file that user uploads, nullable- can't get rid of user's profile_image
    profile_image = db.Column(db.String(64), nullable=False, default='default_profile.png') 
    #must be unique email (unique=True), index-sets up index (sql)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)

    #password
    password_hash = db.Column(db.String(128))

    #connect blogpost to user
    posts = db.relationship('BlogPost',backref='author',lazy=True)

    #make instance of user
    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash, password)


    #string representation
    def __repr__(self):
        return f"Username: {self.username}"


class BlogPost(db.Model):
    
    #each blogpost is connected to the user
    users = db.relationship(User)


    id = db.Column(db.Integer, primary_key=True)
    #attribute that connects blogpost to user, (nullable)-every blogpost must be associated to user id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)   #tablename: users, attribute: id
    
    #every blogpost has to have a publish date
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    #each blogpost has a title, (nullable)-must provide title
    title = db.Column(db.String(140), nullable=False)

    text = db.Column(db.Text, nullable=False)



    #make instance of blogpost
    def __init__(self,title,text,user_id):
        self.title = title
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f"Post ID: {self.id} -- Date: {self.date} -- {self.title}"
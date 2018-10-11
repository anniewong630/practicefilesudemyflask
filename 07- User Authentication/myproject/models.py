from myproject import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
#UserMixin has builtin attributes: is_authenticated(), is_active(),is_anonymous(),get_id()

#user_loader decorator allows flask to load user and get id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True) #limit 64 characters, unique=True so no two users have the same email
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        #save password_hash not actual password
        self.password_hash = generate_password_hash(password)

    #checks to see if the user's password is the correct password
    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    









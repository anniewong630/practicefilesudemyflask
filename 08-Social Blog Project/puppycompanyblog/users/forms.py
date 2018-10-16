from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
#Let user update a jpeg, png file in order to have profile displayed
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from puppycompanyblog.models import User

class LoginForm(FlaskForm):

    email = StringField('Email: ',validators=[DataRequired(),Email()])
    password = PasswordField('Password: ',validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):

    email = StringField('Email: ', validators=[DataRequired(),Email()])
    username = StringField('Username: ',validators=[DataRequired()])
    password = PasswordField('Password: ',validators=[DataRequired(),EqualTo('pass_confirm', message='Passwords must match')])
    pass_confirm = PasswordField('Confirm Password: ', validators=[DataRequired()])
    submit = SubmitField('Register')

    #check email 
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            return ValidationError('Your email has been registered already.')


    #check username
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            return ValidationError('Your username has been registered already.')


class UpdateUserForm(FlaskForm):

    email = StringField('Email: ',validators=[DataRequired(),Email()])
    username = StringField('Username: ',validators=[DataRequired()])
    picture = FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')


    #check email 
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            return ValidationError('Your email has been registered already.')

    #check username
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            return ValidationError('Your username has been registered already.')






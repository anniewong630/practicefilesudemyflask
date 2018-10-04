#owners/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Owner\'s name: ')
    pup_id = IntegerField('Puppy ID: ')
    submit = SubmitField('Add Owner')
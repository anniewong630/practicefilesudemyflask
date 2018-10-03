from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):

    name = StringField('Name of Puppy: ')
    submit = SubmitField('Add Puppy')


class DelForm(FlaskForm):

    id = IntegerField('Puppy ID: ')
    submit = SubmitField('Remove Puppy')


class AddOwnerForm(FlaskForm):

    name = StringField('Owner\'s name: ')
    pup_id = IntegerField('Puppy ID: ')
    submit = SubmitField('Add Owner')
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

#create application
app = Flask(__name__)

#configure secret key
app.config['SECRET_KEY'] = 'mysecretkey'

#inherits from FlaskForm 
class InfoForm(FlaskForm):
    #attributes
    breed = StringField("What breed are you?")
    submit = SubmitField("Submit")


@app.route('/', methods = ['GET', 'POST'])
def index():

    #variable breed different from breed attribute above, used in if statement in HTML
    breed = False

    #creating an instance of Form
    form = InfoForm()

    if form.validate_on_submit():
        breed = form.breed.data #data that was submitted for that field
        form.breed.data = '' #reset variable
    return render_template('index.html', form=form, breed=breed)


if __name__ == '__main__':
    app.run(debug=True)

    
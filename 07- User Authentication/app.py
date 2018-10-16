from myproject import db, app
from flask import render_template, redirect, request, url_for, flash, abort
from flask_login import login_user, login_required, logout_user
from myproject.models import User
from myproject.forms import LoginForm, RegistrationForm

@app.route('/')
def home():
    return render_template('home.html')

#welcomes user after logging in
@app.route('/welcome')
@login_required  #makes sure the user is logged in to see the page
def welcome_user():
    return render_template('welcome_user.html')

#LOGOUT VIEW
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You logged out.')
    return redirect(url_for('home'))

#LOGIN VIEW
@app.route('/login', methods=['GET','POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        #user was supplied and password is correct
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Logged in successfully')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('welcome_user')

            return redirect(next)
    return render_template('login.html',form=form)


#REGISTER VIEW 
@app.route('/register',methods=['GET','POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,     
                    password=form.password.data)
    
        db.session.add(user)
        db.session.commit()
        flash('Thank you for registering.')
        return redirect(url_for('login'))

    return render_template('register.html',form=form)



if __name__ == '__main__':
    app.run()







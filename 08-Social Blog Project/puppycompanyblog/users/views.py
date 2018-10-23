#user/view.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user,current_user,logout_user, login_required
#reference database, registering user and update or create it
from puppycompanyblog import db
from puppycompanyblog.models import User, BlogPost
from puppycompanyblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from puppycompanyblog.users.picture_handler import add_profile_pic


#register blueprint
users = Blueprint('users', __name__)

#REGISTER USER VIEW
@users.route('/register',methods=['GET','POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        #create user object
        user = User(email = form.email.data,
                    username = form.username.data,
                    password = form.password.data)

        #add user to db
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('users.login'))

    return render_template('register.html',form=form)


#LOGIN USER VIEW
@users.route('/login',methods=['GET','POST'])
def login():
    
    form = LoginForm()

    if form.validate_on_submit():
        #query user that already exists
        user = User.query.filter_by(email=form.email.data).first()
        #check password
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash('Log In Success')

            #grabs the information the user was trying to access 
            next = request.args.get('next')

            if next == None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('login.html',form=form)


#LOGOUT USER VIEW
@users.route('/logout')
def logout():
    logout_user()
    #once user is logged out, redirect to home page
    return redirect(url_for('core.index'))


#ACCOUNT VIEW - update user information
@users.route('/account',methods=['GET','POST'])
@login_required
def account():

    form = UpdateUserForm()

    if form.validate_on_submit():

        #if user uploaded a picture
        if form.picture.data:
            #grab current username
            username = current_user.username

            #(grab data from picture and username) pass it to the add_profile_pic function
            pic = add_profile_pic(form.picture.data,username)

            #default is changed to user's picture 
            current_user.profile_image = pic
        
        current_user.username = form.username.data
        current_user.email = form.email.data

        db.session.commit()
        flash('User Account Updated')
        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        #not submitting anything, just getting current username ******
        form.username.data = current_user.username
        form.email.data = current_user.email
    #goes to static folder under profile_pics get the current user's profile image
    profile_image = url_for('static',filename='profile_pics/'+current_user.profile_image)

    return render_template('account.html',profile_image=profile_image,form=form)



#USER'S LIST OF BLOGPOST VIEW
@users.route('/<username>')
def user_posts(username):
    #later on will use this page variable to cycle through user post 
    page = request.args.get('page',1,type=int)
    #will return 404 error if username does not exist
    user = User.query.filter_by(username=username).first_or_404()
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)

    return render_template('user_blog_post.html',blog_posts=blog_posts,user=user)


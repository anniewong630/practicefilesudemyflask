#os.environ[] - used locally for testing
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

from flask import Flask, render_template, redirect, url_for
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

blueprint = make_google_blueprint(client_id='113654048914-jt1av6j3civ4mc9c95qhf25fnutd42cc.apps.googleusercontent.com',
                                  client_secret='0ukboFY3iAEefvM5Anc7FGti',
                                  offline=True,scope=['profile','email'])

#when user wants to login, will open up a new separate login page
app.register_blueprint(blueprint,url_prefix='/login')

#home page
@app.route('/')
def index():
    return render_template('home.html')


#welcome page
@app.route('/welcome')
def welcome():
    #will return an error if user did not log in
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    email = resp.json()['email']
    return render_template('welcome.html',email=email)

#google login page
@app.route('/login/google')
def login():
    if not google.authorized:
        #automated call from flask dance, takes you to google login page
        return render_template(url_for('google.login'))

    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    #grab user's email 
    email = resp.json()['email']

    return render_template('welcome.html',email=email)

if __name__ == '__main__':
    app.run()


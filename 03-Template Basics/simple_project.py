#Second version of Simple-Project

# Set up your imports and your flask app.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indexp.html')

# This page will be the page after the form
@app.route('/report')
def report():
     #get username from submission form
    username  = request.args.get('username')

    upper_char = False
    lower_char = False
    last_char = False

    upper_char = any(item.isupper() for item in username)
    lower_char = any(item.islower() for item in username)
    last_char = username[-1].isdigit()

    report = upper_char and lower_char and last_char

    return render_template('reportp.html', report=report
                            ,upper=upper_char,lower=lower_char,last=last_char)



if __name__ == '__main__':
    app.run(debug=True)

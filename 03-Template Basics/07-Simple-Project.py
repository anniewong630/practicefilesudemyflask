# Set up your imports and your flask app.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index7.html')


# This page will be the page after the form
@app.route('/report')
def report():
    # Check the user name for the 3 requirements.
    username = request.args.get('username')

    last_number = username[-1].isdigit() #returns True/False
    lowercase = any(c.islower() for c in username)
    uppercase = any(c.isupper() for c in username)

    requirements_list = [last_number,lowercase,uppercase]
    failure_messages = ['<li>You did not end with a number</li>',
                        '<li>You do not have a lowercase letter</li>', 
                        '<li>You do not have an uppercase letter</li>']

    output = '' #will contain error messages

    for index, requirement in enumerate(requirements_list):
        # if this requirement failed, output its error message
        if not requirement:
            output+=failure_messages[index] + '\n'
    
    #if/else block checks to see if output is empty (passes all requirements) 
    if output == '':
        message = "<p>You satisfy all the requirements</p"
        return render_template('report7.html',message=message)
    else:
        message = "<p>Here are the requirements you failed:\n<p>" + output
        return render_template('report7.html',message=message)



if __name__ == '__main__':
    app.run(debug=True)

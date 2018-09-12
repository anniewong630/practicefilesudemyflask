# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    return '<h1>Welcome to Puppy Latin page</h1>'
    # Welcome Page
    # Create a generic welcome page.
    

@app.route('/puppylatin/<name>') # Fill this in!
def puppylatin(name):
    last_letter = name[-1]
    if last_letter == 'y':
        name_without_y = name[:-1]
        new_name = name_without_y + 'iful'
    else:
        new_name = name + 'y'
        print(new_name) #output to the console
    return '<h1>Hi ' + name + '! Your puppylatin name is ' + new_name + '</h1>'
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"

if __name__ == '__main__':
    # Fill me in!
    app.run(debug = True)

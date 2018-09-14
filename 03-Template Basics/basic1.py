from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    my_name = "Spongebob"
    letters = list(my_name)
    s_dictionary = {'name':'patrick'}
    return render_template('basic.html',my_name=my_name,letters=letters,s_dictionary=s_dictionary)

if __name__ == '__main__':
    app.run(debug = True)
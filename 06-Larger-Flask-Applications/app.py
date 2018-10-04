#app.py
from myproject import app
from flask import render_template

#set up homepage
@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

    
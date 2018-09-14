from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    my_list=['Spongebob','Patrick','Mr. Krabs','Sandy']
    return render_template('basic2.html', my_list=my_list)


if __name__ == '__main__':
    app.run(debug = True)


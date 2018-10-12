from flask import render_template, request, Blueprint

core = Blueprint('core', __name__)

@core.route('/')
def index():
    #more to come (list of all available blog posts)
    return render_template('index.html')


@core.route('/info')
def info():
    #general information about the company
    return render_template('info.html')
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

@app.route('/test', methods=['GET'])
def test():
    return '<h1>This is a test page!</h1>'

@app.route('/test', methods=['POST'])
def test_post():
    return '<h1>This is a test page via a POST request!</h1>'

if __name__ == '__main__':
    app.run()

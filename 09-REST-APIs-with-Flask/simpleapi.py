from flask import Flask
from flask_restful import Resource, Api

#Resource - creates a resource to connect to 
#Api- wrapper around entire app that allows resource to connect

app = Flask(__name__)

api = Api(app)

#Resource class has different methods- get, put, delete, post
class HelloWorld(Resource):

    def get(self):
        return {'hello':'world'}

api.add_resource(HelloWorld,'/')

if __name__ == '__main__':
    app.run(debug=True)
    
from flask import Flask, request
from flask_restful import Resource, Api
from secure_check import authenticate,identity
from flask_jwt import JWT,jwt_required

app = Flask(__name__)
app.config['SECRETKEY'] = 'mysecretkey'
api = Api(app)

jwt = JWT(app,authenticate,identity)

# puppies = [{'name':'Rufus'},{name:'Frankie'},......]
# its in memory, it clears with every restart
puppies = []

class PuppyNames(Resource):
    def get(self,name):

        # Cycle through list for puppies
        for pup in puppies:
            if pup['name'] == name:
                return pup

        # If you request a puppy not yet in the puppies list
        return {'name':None},404

    def post(self, name):
        # Add  the dictionary to list
        pup = {'name':name}
        puppies.append(pup)
        # Then return it back
        return pup

    def delete(self,name):

        # Cycle through list for puppies
        for ind,pup in enumerate(puppies):
            if pup['name'] == name:
                # don't really need to save this
                delted_pup = puppies.pop(ind)
                return {'note':'delete successful'}


class AllNames(Resource):
    @jwt_required()
    def get(self):
        # return all the puppies :)
        return {'puppies': puppies}


api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames,'/puppies')

if __name__ == '__main__':
    app.run(debug=True)
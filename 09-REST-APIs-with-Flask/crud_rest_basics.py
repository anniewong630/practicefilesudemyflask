from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#list of dictionaries 
#[{'name': 'rufus}, {'name': 'frankie'}]
puppies = []

class PuppyNames(Resource):

    #to get puppy we need to cycle through list
    def get(self,name):
        print(puppies)

        for pup in puppies:
            if pup['name'] == name:
                return pup
            
        return {'name':None}

    def post(self,name):
        
        pup = {'name':name}
        puppies.append(pup)
        print(puppies)
        return pup

    def delete(self,name):
        for ind,pup in enumerate(puppies):
            if pup['name'] == name:
                deleted_pup = puppies.pop(ind)
                #print(deleted_puppy)
                return {'note':'delete success'}

#get a list of all puppies        
class AllNames(Resource):

    def get(self):
        return {'puppies':puppies}

#register resources
api.add_resource(PuppyNames,'/puppy/<string:name>')
api.add_resource(AllNames,'/puppies')        

if __name__ == '__main__':
    app.run()
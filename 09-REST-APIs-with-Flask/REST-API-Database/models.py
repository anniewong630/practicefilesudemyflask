from auth_api import db

class Puppy(db.Model):
    name = db.Column(db.String(80),primary_key=True)

    def __init__ (self,name):
        self.name = name
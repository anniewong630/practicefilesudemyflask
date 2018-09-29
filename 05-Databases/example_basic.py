#create entries into tables
from example import db, Puppy, Toy, Owner

#create two puppy object
jane = Puppy('Jane')
dot = Puppy('Dot')

#add puppy to db
db.session.add_all([jane,dot])
db.session.commit()

#check
print(Puppy.query.all())

#first puppy name that is jane .all() will return a list
jane = Puppy.query.filter_by(name='Jane').first()
print(jane) #jane has no owner

#create owner for jane
michelle = Owner('Michelle', jane.id)

#give toys to jane
toy1 = Toy('Chew Toy', jane.id)
toy2 = Toy('Ball', jane.id)
toy3 = Toy('Stick', dot.id)


db.session.add_all([michelle,toy1,toy2,toy3])
db.session.commit()

#get jane after additions, jane will have an owner
jane = Puppy.query.filter_by(name='Jane').first()
print(jane)

jane.report_toys()






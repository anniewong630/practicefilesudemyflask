#Create, Read, Update, Delete 
from basic import db, Puppy 

#CREATE new puppy object
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()

#READ 
#List of all puppy objects in table
all_puppies = Puppy.query.all()
print(all_puppies)
print('\n')

#Select by ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)
print(puppy_one.age)
print('\n')

#Filter
puppy_frankie = Puppy.query.filter_by(name = 'Frankie')
print(puppy_frankie.all()) 
print('\n')

#UPDATE - get data, modify and save changes
first_puppy = Puppy.query.get(1)
first_puppy.age = 15
db.session.add(first_puppy)
db.session.commit()

#DELETE
#delete second puppy
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

#Print all puppies
all_puppies = Puppy.query.all()
print(all_puppies)


from basic import db, Puppy

#creates all tables
db.create_all()

#creating puppy objects
sam = Puppy('Sammy', 7)
frank = Puppy('Frankie', 2)

#Prints none because it has not been added to the DB
print(sam.id)
print(frank.id)

#id are created once we add these entries to the DB
db.session.add_all([sam,frank])

#save info to DB
db.session.commit()

#check id
print(sam.id)
print(frank.id)
"""Example using Bcrypt """
from flask_bcrypt import Bcrypt

#create hashing object, instance of hasher
bcrypt = Bcrypt()

#we do not want to save this, instead we want to save the hashed_version
password = 'secretpassword'

#want to store this on servers
hashed_password = bcrypt.generate_password_hash(password)
print (hashed_password)

#check to see if the password is correct with new value user provided 
check_password = bcrypt.check_password_hash(hashed_password, 'wrong')
print(check_password) 
#print false because 'wrong' is not the correct password





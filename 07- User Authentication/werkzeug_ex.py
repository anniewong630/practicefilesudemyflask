from werkzeug.security import generate_password_hash, check_password_hash

hashed_pass = generate_password_hash('mypassword')
print(hashed_pass)

check = check_password_hash(hashed_pass,'wrongpassword')
print(check) #returns false 

check = check_password_hash(hashed_pass,'mypassword')
print(check) #returns true
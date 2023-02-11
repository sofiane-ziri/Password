import random
import string
import bcrypt

def store_passwords_in_txt(passwords, file_path):
    with open(file_path, "a") as file:
        for password in passwords:
            file.write(password)
        file.write("\n")
            
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(chars, k=length))

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)

password = generate_password()
hashed_password = hash_password(password)

# Check the password
assert check_password(password, hashed_password) == True

store_passwords_in_txt(password, "password.txt")
print ("mot de passe", password)



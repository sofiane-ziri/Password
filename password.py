import hashlib
import re


def check_lenght_psw(password):
    if len(password) < 8:
        return "Le mot de passe doit comporter au moins 8 caractères."


def check_uppercase_psw(password):
    if not re.search("[A-Z]", password):
        return "Le mot de passe doit contenir au moins une lettre majuscule."


def check_lowercase_psw(password):
    if not re.search("[a-z]", password):
        return "Le mot de passe doit contenir au moins une lettre minuscule."


def check_number_psw(password):
    if not re.search("[0-9]", password):
        return "Le mot de passe doit contenir au moins un chiffre."


def check_specialchart_psw(password):
    if re.search("[!@#$%^&*]", password) is None:
        return "Le mot de passe doit contenir au moins un caractère spécial."


    return True


def get_hash_password(password):
    objet_hash = hashlib.sha256(password.encode())
    dig_hex = objet_hash.hexdigest()
    return dig_hex


def get_password():
    while True:
        password = input("Entrez un mot de passe : ")
        error_message = ""
        if check_lenght_psw(password):
            error_message = check_lenght_psw(password)
        elif check_lowercase_psw(password):
            error_message = check_lowercase_psw(password)
        elif check_uppercase_psw(password):
            error_message = check_uppercase_psw(password)
        elif check_number_psw(password):
            error_message = check_number_psw(password)
        elif check_specialchart_psw(password) != True:
            error_message = check_specialchart_psw(password)
        if error_message == "":
            break
        print(error_message)
    return password


password = get_password()
hashed_password = get_hash_password(password)
print("Hachage du mot de passe :", hashed_password)

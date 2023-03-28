import hashlib
import json

PASSWORD_FILE = "passwords.json"

def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file)

def load_passwords():
    try:
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_password():
    while True:
        password = input("Veuillez entrer un nouveau mot de passe : ")
        if len(password) < 8:
            print("Erreur : le mot de passe doit contenir au moins 8 caractères.")
        elif not any(char.isupper() for char in password):
            print("Erreur : le mot de passe doit contenir au moins une lettre majuscule.")
        elif not any(char.islower() for char in password):
            print("Erreur : le mot de passe doit contenir au moins une lettre minuscule.")
        elif not any(char.isdigit() for char in password):
            print("Erreur : le mot de passe doit contenir au moins un chiffre.")
        elif not any(char in '!@#$%^&*' for char in password):
            print("Erreur : le mot de passe doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).")
        else:
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            passwords.append(hashed_password)
            save_passwords(passwords)
            print("Le mot de passe a été enregistré avec succès.")
            break

def view_passwords():
    if len(passwords) == 0:
        print("Il n'y a aucun mot de passe enregistré.")
    else:
        print("Voici la liste des mots de passe enregistrés :")
        for password in passwords:
            print("-", password)

passwords = load_passwords()

while True:
    print("\nQue souhaitez-vous faire ?")
    print("1. Ajouter un nouveau mot de passe")
    print("2. Afficher les mots de passe enregistrés")
    print("3. Quitter le programme")
    choice = input("Entrez le numéro de l'option choisie : ")
    if choice == "1":
        add_password()
    elif choice == "2":
        view_passwords()
    elif choice == "3":
        break
    else:
        print("Option invalide.")

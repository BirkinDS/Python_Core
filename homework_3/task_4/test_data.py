# solution
import random
import string

def generate_login():
    letters = string.ascii_lowercase
    login = ""
    for i in range(6):
        login = login + random.choice(letters)
    return login

def generate_age():
    return random.randint(18, 65)

def generate_status():
    return random.choice(["ACTIVE", "BLOCKED", "INACTIVE"])

def generate_user():
    user = {
        "login": generate_login(),
        "age": generate_age(),
        "status": generate_status()
    }
    return user
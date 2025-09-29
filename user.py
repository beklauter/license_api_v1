import uuid
import json

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.licenses = []

    def create_license(self):
        license_key = str(uuid.uuid4()).replace('-', '').upper()[:16]
        api_key = str(uuid.uuid4())
        license_obj = {
            "license_key": license_key,
            "api_key": api_key,
            "activated": False
        }
        self.licenses.append(license_obj)
        return license_obj

users = {}

def add_user(username, password):
    user = User(username, password)
    users[username] = user
    return user

def save_users():
    with open('users.json', 'w') as file:
        json.dump({u: vars(user) for u, user in users.items()}, file, default=str)
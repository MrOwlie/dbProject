import uuid
from User import User

class UserHandler:
    def __init__(self, db):
        self.db = db;
        self.users = dict()

    def newUser(self, name, email, password, zipCode, city, address, phone, ssn):
        ID = currentID
        user = User(self.db, email, password, name, ID, zipCode, city, address, phone, ssn);
        user.handler = self;
        self.users[ID] = user

    def returningUser(self, email, password):
        user = User(self.db, email, password)
        self.users[user.ID] = user

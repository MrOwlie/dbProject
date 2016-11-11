import uuid
from User import User

class UserHandler:
    def __init__(self, db):
        self.db = db;
        self.users = dict()

    def newUser(self, name, email, password, zipCode, address, phone, ssn):
        ID = uuid.uuid4();
        user = User(self.db, ID, name, email, password, zipCode, address, phone, ssn);
        user.handler = self;
        self.users[ID] = user

    def returningUser(self, name, password):
        user = User(self.db, name, password)
        self.users[user.ID] = user

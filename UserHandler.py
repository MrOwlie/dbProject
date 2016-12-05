import uuid
from User import User

class UserHandler:
    def __init__(self, db):
        self.db = db;
        self.users = dict()

    def newUser(self, name, email, password, zipCode, city, address, phone, ssn):
        seshID = uuid.uuid4
        user = User(self.db, seshID, email, password, name, zipCode, city, address, phone, ssn);
        user.handler = self
        self.users[seshID] = user

    def returningUser(self, email, password):
        validated = self.db.validatePassword(email,password)
        if not validated:
            return "Invalid email or password"
        user = User(self.db, email, password)
        self.users[user.ID] = user
        return None

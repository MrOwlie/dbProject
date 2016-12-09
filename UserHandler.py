import uuid
from User import User

class UserHandler:
    def __init__(self, db):
        self.db = db;
        self.users = dict()

    def newUser(self, name, email, password, zipCode, city, address, phone, ssn):
        ID = db.runQuery("SELECT MAX(uid) FROM users").fetchone()
        seshID = uuid.uuid4
        user = User.register(self.db, seshID, email, password, name, zipCode, city, address, phone, ssn)
        user.handler = self
        self.users[seshID] = user
        return seshID

    def returningUser(self, email, password):
        seshID = uuid.uuid4
        validated = self.db.validatePassword(email,password)
        if not validated:
            return "ERROR: Invalid email or password"
        user = User.login(self.db, seshID, email)
        self.users[seshID] = user
        return seshID

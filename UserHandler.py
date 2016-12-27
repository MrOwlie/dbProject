import uuid
from User import User
from Cart import Cart

class UserHandler:
    def __init__(self, db):
        self.db = db;
        self.users = dict()

    def newUser(self, name, email, password, zipCode, city, address, phone, ssn):
        ID = (self.db.runQuery("SELECT MAX(uid) FROM users").fetchone()[0]) + 1
        seshID = str(uuid.uuid4().hex)
        user = User.register(self.db, seshID, email, password, name, zipCode, city, address, phone, ssn)
        user.handler = self
        self.users[seshID] = user
        cart = Cart(self.db)
        cart.new(ID)
        return seshID

    def returningUser(self, email, password):
        seshID = str(uuid.uuid4().hex)
        print("returningUser() -> seshID: " + seshID)
        validated = self.db.validatePassword(email,password)
        if not validated:
            return "ERROR: Invalid email or password"
        user = User.login(self.db, seshID, email)
        self.users[seshID] = user
        print("returningUser() -> users: " + str(self.users))
        return seshID

    def isSessionActive(self, seshID):
        try:
            if(self.users[seshID] != None):
                return True
            else:
                return False
        except KeyError:
            return False

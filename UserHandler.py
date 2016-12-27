import uuid
from User import User
from Cart import Cart

class UserHandler:
    def __init__(self, db):
        self.db = db;
        self.users = dict()
        self.seshIDs = dict()

    def banUser(self, email):
        if(self.db.runQuery("SELECT banned FROM users WHERE email = '" + email + "'").fetchone()[0] == 0):
            banFlag = "1"
        else:
            banFlag = "0"
        query = "UPDATE users SET banned = '" + banFlag + "' where email = '" + email + "'"
        self.db.runQuery(query);
        try:
            del self.users[self.seshIDs[email]]
        except(KeyError):
            pass

    def newUser(self, name, email, password, zipCode, city, address, phone, ssn):
        seshID = str(uuid.uuid4().hex)
        user = User.register(self.db, seshID, email, password, name, zipCode, city, address, phone, ssn)
        user.handler = self
        self.users[seshID] = user
        self.seshIDs[user.email] = seshID
        cart = Cart(self.db)
        cart.new(email)
        return seshID

    def returningUser(self, email, password):
        seshID = str(uuid.uuid4().hex)
        print("returningUser() -> seshID: " + seshID)
        validated = self.db.validatePassword(email,password)
        if not validated:
            return "ERROR: Invalid email or password"
        user = User.login(self.db, seshID, email)
        self.users[seshID] = user
        self.seshIDs[email] = seshID
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

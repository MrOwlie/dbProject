class User:

    def __init__(self, db, ID, password):
        #This constructor will fetch a user from the DB
        #It can be used to attempt a login.
        self.ID = ID
        self.db = db
        if(self.validate()):
            self.update();

    def __init__(self, db, name, email, password, zipCode, address, cart):
        self.name = name
        self.ssn = ssn
        self.address = address
        self.email = email
        self.zipCode = zipCode
        self.phone = phone
        self.password = password
        #This constructor will create a user object and save to DB

        save(self);

    def validate(self):
        realPassword = self.db.runQuery("SELECT password FROM users WHERE uid = " + ID)
        return (password == realPassword)

    def update(self):
        #This function will update the user object from DB
        data = self.db.runQuery("SELECT * FROM users WHERE uid = " + ID)
        data = data.fetchone()
        self.password = data.pop()
        self.phone = data.pop()
        self.zipCode = data.pop()
        self.email = data.pop()
        self.address = data.pop()
        self.ssn = data.pop()
        self.name = data.pop()

    def save(self):
        #This function will save the user object to DB
        self.db.runQuery("UPDATE users SET name = " + self.name + ", ssn = " + self.ssn + ", address = " + self.address + ", email = " + self.email + ", zipCode = " + zipCode + ", phone = " + phone + ", password = " + password + " WHERE uid = " + ID)

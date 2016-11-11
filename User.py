class User:

    def __init__(self, db, name, password):
        #This constructor will fetch a user from the DB
        #It can be used to attempt a login.
        self.name = name
        self.db = db
        self.password = password
        if(self.validate()):
            self.update(self.name);

    def __init__(self, db, ID, name, email, password, zipCode, address, phone, ssn):
        self.db = db
        self.name = name
        self.ssn = ssn
        self.address = address
        self.email = email
        self.zipCode = zipCode
        self.phone = phone
        self.password = password
        self.ID = ID

        print(self.db)
        print(self.name)
        print(self.ssn)
        print(self.address)
        print(self.email)
        print(self.zipCode)
        print(self.phone)
        print(self.password)
        print(self.ID)
        #This constructor will create a user object and save to DB

        self.save();

    def validate(self):
        #checks if the password entered in the frontend matches our DB records
        realPassword = self.db.runQuery("SELECT password FROM users WHERE name = " + name)
        return (self.password == realPassword)

    def update(self, ID):
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
        self.ID = data.pop()

    def update(self, name):
        data = self.db.runQuery("SELECT * FROM users WHERE name = " + name)
        data = data.fetchone()
        self.password = data.pop()
        self.phone = data.pop()
        self.zipCode = data.pop()
        self.email = data.pop()
        self.address = data.pop()
        self.ssn = data.pop()
        self.name = data.pop()
        self.ID = data.pop()


    def save(self):
        #This function will save the user object to DB
        ##WIP : Need to check if the user exists in the db, if it doesn't we should insert instead of update.

        print "UPDATE users SET name = '" + self.name + "', ssn = '" + self.ssn + "', adress = '" + self.address + "', email = '" + self.email + "', zip_code = '" + self.zipCode + "', phone = '" + self.phone + "', password = '" + self.password + "' WHERE uid = '13'"
        self.db.runQuery("UPDATE users SET name = '" + self.name + "', ssn = '" + self.ssn + "', adress = '" + self.address + "', email = '" + self.email + "', zip_code = '" + self.zipCode + "', phone = '" + self.phone + "', password = '" + self.password + "' WHERE uid = '13'")

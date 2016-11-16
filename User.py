from flask import flash
from flask import render_template
class User:

    '''def __init__(self, db, name, password):
        #This constructor will fetch a user from the DB
        #It can be used to attempt a login.
        self.name = name
        self.db = db
        self.password = password
        if(self.validate()):
            self.update(self.name);'''

    def __init__(self, db, email = None, password = None, name = None, ID = None, zipCode = None, city = None, address = None, phone = None, ssn = None):
        self.db = db
        self.name = name
        self.ssn = ssn
        self.address = address
        self.email = email
        self.zipCode = zipCode
        self.city = city
        self.phone = phone
        self.password = password
        self.ID = ID

        print(self.db)
        print(self.name)
        print(self.ssn)
        print(self.address)
        print(self.email)
        print(self.zipCode)
        print(self.city)
        print(self.phone)
        print(self.password)
        print(self.ID)
        #This constructor will create a user object and save to DB
        if(ID == None):
            if(self.validate()):
                self.update(self.name)
            else:
                #WRONG PASSWORD MADDAFAKKA
                render_template('index.html', loginError = "Invalid Email or password!")
        else:
            self.save();

    def validate(self):
        #checks if the password entered in the frontend matches our DB records
        realPassword = self.db.runQuery("SELECT password FROM users WHERE email = '{}'".format(self.email))
        realPassword = realPassword.fetchone()
        print ("passwords: {}, {}, {}".format(self.password, realPassword, self.password == realPassword))
        return (self.password == realPassword)


    def update(self, ID = None, name = None):
        #This function will update the user object from DB
        if(ID == None):
            queryEnd = ("email = " + email)
        else:
            queryEnd = ("uid = " + ID)

        data = self.db.runQuery("SELECT uid, name, ssn, address, email, city, zipCode, phone, password FROM users WHERE " + queryEnd)
        data = data.fetchone()
        self.password = data.pop()
        self.phone = data.pop()
        self.zipCode = data.pop()
        self.city = data.pop()
        self.email = data.pop()
        self.address = data.pop()
        self.ssn = data.pop()
        self.name = data.pop()
        self.ID = data.pop()


    def save(self):
        #This function will save the user object to DB
        ##WIP : Need to check if the user exists in the db, if it doesn't we should insert instead of update.

        queryStart = "UPDATE users SET name = '{}', ssn = '{}', adress = '{}', email = '{}', zip_code = '{}', city = '{}' phone = '{}', password = '{}' WHERE uid = '{}'"
        query = queryStart.format(self.name, self.ssn, self.address, self.email, self.zipCode, self.city, self.phone, self.password, self.ID)
        #query = "INSERT INTO users (name,ssn,adress,email,zip_code,phone,password) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(self.name, self.ssn, self.address, self.email, self.zipCode, self.phone, self.password)
        print (query)
        self.db.runQuery(query)

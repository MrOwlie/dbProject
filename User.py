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

    @staticmethod
    def register(db, seshID, email, password, name, zipCode, city, address, phone, ssn):
        user = User(db, seshID, email, password, name, zipCode, city, address, phone, ssn)
        user.registerDB()
        user.update()
        return user

    @staticmethod
    def login(db, seshID, email):
        user = User(db, seshID, email, "", "", "", "", "", "", "")
        user.update()
        return user


    def __init__(self, db, seshID, email, password, name, zipCode, city, address, phone, ssn):
        self.db = db
        self.name = name
        self.ssn = ssn
        self.address = address
        self.email = email
        self.zipCode = zipCode
        self.city = city
        self.phone = phone
        self.password = password
        self.seshID = seshID

        print(self.db)
        print(self.name)
        print(self.ssn)
        print(self.address)
        print(self.email)
        print(self.zipCode)
        print(self.city)
        print(self.phone)
        print(self.password)
        print(self.seshID)



    def validate(self):
        #checks if the password entered in the frontend matches our DB records

        realPassword = self.db.runQuery("SELECT password FROM users WHERE email = '{}'".format(self.email))
        realPassword = realPassword.fetchone()
        print ("passwords: {}, {}, {}".format(self.password, realPassword, self.password == realPassword))
        return (self.password == realPassword)


    def update(self):
        #This function will update the user object from DB
        print("update: " + self.email)
        data = self.db.runQuery('SELECT uid, name, ssn, address, email, city, zipCode, phone, password FROM users WHERE email = ' + "'" + self.email + "'")
        data = data.fetchone()
        print(data)
        self.password = data[8]
        self.phone = data[7]
        self.zipCode = data[6]
        self.city = data[5]
        self.email = data[4]
        self.address = data[3]
        self.ssn = data[2]
        self.name = data[1]
        self.ID = data[0]

    def registerDB(self):
        #This function will insert the user object in DB
        query = "INSERT INTO users (name, ssn, address, email, zipCode, city, phone, password) VALUES ('{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}' , '{}' ) "
        query = query.format(self.name, self.ssn, self.address, self.email, self.zipCode, self.city, self.phone, self.password)
        print(query)
        self.db.runQuery(query)

    def save(self):
        #This function will update the user object in DB
        ##WIP : THIS SHOULD ONLY UPDATE THE RECORDS IN THE DATABASE
        ## ---> Use .register() to add new entries.

        query = "UPDATE users SET name = '{}', ssn = '{}', adress = '{}', email = '{}', zip_code = '{}', city = '{}' phone = '{}', password = '{}' WHERE uid = '{}'"
        query = query.format(self.name, self.ssn, self.address, self.email, self.zipCode, self.city, self.phone, self.password, self.ID)
        #query = "INSERT INTO users (name,ssn,adress,email,zip_code,phone,password) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(self.name, self.ssn, self.address, self.email, self.zipCode, self.phone, self.password)
        print (query)
        self.db.runQuery(query)

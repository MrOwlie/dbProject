

class User:



    def __init__(self, ID):
        #This constructor will fetch a user from the DB

    def __init__(self, name, email, password, zipCode, address, cart):
        self.name = name
        self.email = email
        self.password = password
        self.zipCode = zipCode
        self.address = address
        self.cart = cart
        #This constructor will create a user object and save to DB

        save(self);

    def update(self):
        #This function will update the user object from DB

    def save(self):
        #This function will save the user object to DB

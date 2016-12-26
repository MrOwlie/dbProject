import uuid

class Order:

    def __init__(self, db):
        self.db = db;

    def place(self, cartID, address, zip, city):
        query = "INSERT INTO orders (delivery_address, delivery_zip, delivery_city, cart_uid) VALUES ('{}', '{}', '{}', '{}')".format(address, zip, city, cartID)
        print(query)
        self.db.runQuery(query)
        return

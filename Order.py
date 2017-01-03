import uuid

class Order:

    def __init__(self, db):
        self.db = db;

    def place(self, cartID, address, zip, city):
        query = "INSERT INTO orders (delivery_address, delivery_zip, delivery_city, cart_uid) VALUES ('{}', '{}', '{}', '{}')".format(address, zip, city, cartID)
        self.db.runQuery(query)
        return

    def getOrders(self):
        query = "SELECT * FROM orders"
        orders = self.db.runQuery(query).fetchall()
        print(orders)
        return orders

    def setStatus(self,status,ID):
        query = "UPDATE orders SET sent = '{}' WHERE uid = '{}'".format(status,ID)
        self.db.runQuery(query)

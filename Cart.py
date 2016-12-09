import uuid

class Cart:

    def __init__(self, db):
        self.db = db;


    def newCart(self, userID):
        self.products = []
        self.userID = userID
        self.db.runQuery("INSERT INTO carts (customer) VALUES ('{}')".format(userID))
        self.cartID = self.db.runQuery("SELECT uid FROM carts WHERE customer = '{}'".format(userID)).fetchone()
        return self.cartID

    def getCart(self, userID):
        self.userID = userID
        self.cartID = self.db.runQuery("SELECT uid FROM carts WHERE customer='{}'".format(userID)).fetchone()
        self.products = self.db.runQuery("SELECT details FROM products WHERE cart = '{}'".format(self.cartID)).fetchall()
        print (self.products)
        return self.cartID

    def getProducts(self):
        return self.products

    def getDetails(self):
        products = []
        tmp = []
        for detail in self.products:
            if(detail not in tmp):
                tmp.append(detail)
                details = [self.products.count(detail)]
                details = details + self.db.runQuery("SELECT name, description, price, stock FROM product_details WHERE uid = '{}'".format(detail)).fetchone()
                products.append(details)
        #count, name, description, price, stock
        return details

    def getPrice(self):
        price = 0
        for product in self.products:
            price = price + self.db.runQuery("SELECT price FROM product_details WHERE uid = '{}'".format(product)).fetchone()
        return price

    def add(self, detailsID):
        self.products.append(detailsID)
        self.db.runQuery("INSERT INTO products (cart, details) VALUES ('{}','{}')".format(self.cartID, detailsID))
        return True

    def remove(self, detailsID):
        self.products.remove(detailsID)
        self.db.runQuery("DELETE FROM products WHERE cart = {} && details = {} LIMIT 1;".format(self.cartID, detailsID))
        return True

    def removeAll(self, detailsID):
        while detailsID in self.products:
            self.products.remove(detailsID)
        self.db.runQuery("DELETE FROM products WHERE cart = {} && details = {}".format(self.cartID, detailsID))
        return True

    def clear(self):
        self.products = []
        self.db.runQuery("DELETE FROM products WHERE cart = {}".format(self.cartID))
        return True

    def deleteCart(self):
        self.db.runQuery("DELETE FROM carts WHERE uid = {}".format(self.cartID))
        return True

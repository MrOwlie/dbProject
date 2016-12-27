import uuid

class Cart:

    def __init__(self, db):
        self.db = db;


    def new(self, userMail):
        self.products = []
        self.userMail = userMail
        self.db.runQuery("INSERT INTO carts (customer) VALUES ('{}')".format(userMail))
        self.cartID = self.db.runQuery("SELECT uid FROM carts WHERE customer = '{}'".format(userMail)).fetchone()
        return self.cartID

    def get(self, userMail):
        self.userMail = userMail
        cartID = self.db.runQuery("SELECT uid FROM carts WHERE customer='{}' && locked = '0'".format(userMail))
        self.cartID = cartID.fetchone()[0]
        query = "SELECT details FROM products WHERE cart = '{}'".format(self.cartID)
        products = self.db.runQuery(query).fetchall()
        array = []
        for i in range(0,len(products)):
            array.append (products[i][0])
        self.products = array
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
                detail = self.db.runQuery("SELECT uid, name, description, price, stock FROM product_details WHERE uid = '{}'".format(detail)).fetchall()[0]
                for item in detail:
                    details.append(item)
                #details = details +
                products.append(details)
        #count, uid, name, description, price, stock
        print(products)
        return products

    def getPrice(self):
        price = 0
        for product in self.products:
            price = price + self.db.runQuery("SELECT price FROM product_details WHERE uid = '{}'".format(product)).fetchone()
        return price

    def add(self, detailsID, amount):
        for _i in range(0,amount):
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

    def lock(self):
        self.db.runQuery("UPDATE carts SET locked = 1 WHERE uid = '{}'".format(self.cartID))

    def clear(self):
        self.products = []
        self.db.runQuery("DELETE FROM products WHERE cart = {}".format(self.cartID))
        return True

    def deleteCart(self):
        self.db.runQuery("DELETE FROM carts WHERE uid = {}".format(self.cartID))
        return True

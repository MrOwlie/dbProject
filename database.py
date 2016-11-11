

def runQuery(cursor,query):
    cursor.execute(query)
    return cursor.fetchone()


#USERS:
def createUser(cursor,name,ssn,adress,email,zipCode,phone,password):
    query = "INSERT INTO users (name,ssn,adress,email,zip_code,phone,password) VALUES (" + name + "," + ssn + "," + adress + "," + email + "," + zipCode + "," + phone + "," + password + ");"
    runQuery(cursor,query)


def validateUser (cursor,userid,password):
    query = "SELECT password FROM users WHERE uid = " + userid
    realPassword = runQuery(cursor,query)
    return (password == realPassword)


#ORDERS:
def insertOrder (cursor,customer,adress,cart,price):
    query = "INSERT INTO orders (customer,delivery_adress,cart_uid,price) VALUES ({}, {}, {}, {})".format(customer,adress,cart,price)
    runQuery(cursor,query)


#CARTS:
def insertCart (cursor,customer,item,price):
    query = "INSERT INTO carts (customer,items,price) VALUES ({}, {}, {})".format(customer,[item],price)
    runQuery(cursor,query)


def modifyCart (cursor,cart,bool,product):
    query = "SELECT items FROM carts WHERE uid = {}".format(cart)
    items = runQuery(cursor,query)

    if(bool):
        items.append(product)
    else:
        items.remove(product)

    query = "UPDATE carts SET items = {} WHERE uid = {}".format(items,cart)
    runQuery(cursor,query)

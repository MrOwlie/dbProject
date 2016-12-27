from flask import Flask
from flask import render_template
from flask import redirect
from flask import make_response
from flask import url_for
from flask import session
from flask import request
from flask import flash
from flask_restful import Resource, Api
from flask_jsonrpc import JSONRPC
from flask_cors import CORS
from Database import Database
from UserHandler import UserHandler
from Cart import Cart
from Order import Order



#initialize the app and add extensionsA
app = Flask(__name__)
#CORS(app)#
db = Database(app)
userHandler = UserHandler(db)


#initialize the MySQL connection

#Static files
#url_for('static', filename = 'style.css')

#route the website

#index



@app.route('/', methods=['GET', 'POST'])
def root():
    if(request.cookies.get('seshID') in userHandler.users):
        response = make_response(render_template('account.html', headerTitle = "Account", content=["account"], user = userHandler.users[request.cookies.get('seshID')]))
        return response
    errors = []
    switch = request.form.get("submit")
    if(switch == "Login"):
        loginString = userHandler.returningUser(request.form.get("email"), request.form.get("password"))
        if('ERROR:' in str(loginString)):
            return render_template("account.html", content = ["login"], loginError = loginString, headerTitle = "Login")
        else:
            response = make_response(redirect(url_for('products')))
            response.set_cookie('seshID', loginString)
            return response

    elif(switch == "Register"):
        if(request.form.get("password") == request.form.get("passwordConfirm")):
            userHandler.newUser(request.form.get("name"), request.form.get("email"), request.form.get("password"), request.form.get("zipCode"), request.form.get("city"), request.form.get("address"), request.form.get("phone"), request.form.get("ssn"))
            response = make_response(redirect(url_for('products')))
            response.set_cookie('seshID', loginString)
            return response
        else:
            request.form.clear
            return make_response("<p style='color:red; font-size:3em;'>Error: Passwords do not match!</p>", 1337)

    elif(switch == "Account"):
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        passwordConfirm = request.form.get("passwordConfirm")
        zipCode = request.form.get("zipCode")
        city = request.form.get("city")

    return render_template('account.html', content = ["login", "register"], headerTitle = "Login or Register")




@app.route('/products', methods=['GET', 'POST'])
def products():
    if(request.cookies.get('seshID') is None or request.cookies.get('seshID') not in userHandler.users):
        return redirect(url_for('root'))
    if(request.form.get('reviewSubmit') is not None):
        query = "INSERT INTO feedback (product, rating, comment) VALUES ('{}' , '{}' , '{}')".format(request.form.get('productIDReview'), request.form.get('score'), request.form.get('comment'))
        db.runQuery(query)
    products = db.runQuery("SELECT * FROM product_details")
    products = products.fetchall()
    cart = Cart(db)
    cart.get(userHandler.users[request.cookies.get('seshID')].email)
    cartItems = cart.getDetails()
    return render_template('productContainer.html', products = products, cartitems = cartItems)

@app.route('/order', methods=['GET', 'POST'])
def order():
    switch = request.form.get("submit")
    address = request.form.get("address")
    if(address != None):

        zip = request.form.get("zipCode")
        city = request.form.get("city")
        cart = Cart(db)
        cartID = cart.get(userHandler.users[request.cookies.get('seshID')].email)
        order = Order(db)

        order.place(cartID, address, zip, city)
        cart.lock()
        cart.new(userHandler.users[request.cookies.get('seshID')].email)
        return redirect(url_for('products'))

    cart = Cart(db)
    cart.get(userHandler.users[request.cookies.get('seshID')].email)
    cartItems = cart.getDetails()
    return render_template('orderContainer.html', cartitems = cartItems)

@app.route('/product', methods = ['GET', 'POST'])
def productView():
    if(request.cookies.get('seshID') is None or request.cookies.get('seshID') not in userHandler.users):
        return redirect(url_for('root'))
    productID = request.form.get("product")
    if(productID is None):
        redirect(url_for('products'))

    product = db.runQuery("SELECT * FROM product_details WHERE uid='{}'".format(productID)).fetchone()
    reviews = db.runQuery("SELECT * FROM feedback WHERE product='{}'".format(productID)).fetchall()
    score = list()
    for review in reviews:
        score.append(float(review[2]))
    if(len(score) != 0):
        score = sum(score)/float(len(score))
        score = "{0:.2f}".format(score) + "/5"
    else:
        score = "unrated"
    return render_template('productView.html', product = product, reviews = reviews, score = score)




@app.route('/register', methods=['GET', 'POST'])
def register():
    if(request.form.get('submit')):
        error = ""
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        passwordConfirm = request.form.get('passwordConfirm')
        phone = request.form.get('phone')
        ssn = request.form.get('ssn')
        address = request.form.get('address')
        zipCode = request.form.get('zipCode')
        city = request.form.get('city')

        #Check if passwords match
        if(password != passwordConfirm):
            error += "<body style='background-color: LightBlue'><p style = 'font-size: 30px; color: DodgerBlue'> Passwords did not match. " + password != passwordConfirm + " </p></body><br/>"
        #Check if username is valid (nothing to check here)

        #Check if email is valid
        if('@' not in email and '.' not in email):
            error += "<body style='background-color: LightBlue'><p style = 'font-size: 30px; color: DodgerBlue'> E-mail was not valid. </p></body><br/>"

        #Check if phone is valid
        if(not phone.isdigit()):
            error += "<body style='background-color: LightBlue'><p style = 'font-size: 30px; color: DodgerBlue'> Phone was not valid. </p></body><br/>"

        #check if ssn is valid
        if(not ssn.isdigit()):
            error += "<body style='background-color: LightBlue'><p style = 'font-size: 30px; color: DodgerBlue'> SSN was not valid. </p></body><br/>"

        #check if address is valid (nothing to check here)

        #check if zipCode is valid
        if(not zipCode.isdigit()):
            error += "<body style='background-color: LightBlue'><p style = 'font-size: 30px; color: DodgerBlue'> zipCode was not valid </p></body><br/>"

        if (error != ""):
            error += "name:" + name + "</br>"
            error += "email:" + email + "</br>"
            error += "password:" + password + "</br>"
            error += "passwordConfirm:" + passwordConfirm + "</br>"
            error += "phone:" + phone + "</br>"
            error += "ssn:" + ssn + "</br>"
            error += "address:" + address + "</br>"
            error += "zipCode:" + zipCode + "</br>"
            error += "city:" + city + "</br>"
            return error
        else:
            userHandler.newUser(name, email, password, zipCode, city, address, phone, ssn)
            return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    return render_template('reset.html', data = 'Did not confirm yet')

@app.route('/addToCart', methods=['GET', 'POST'])
def addToCart():
    value = int(request.form.get('amount'))
    productID = int(request.form.get('product'))
    cart = Cart(db)
    cartID = cart.get(userHandler.users[request.cookies.get('seshID')].email)
    cart.add(productID,value)
    return redirect(url_for('products'))

@app.route('/removeFromCart', methods=['GET', 'POST'])
def removeFromCart():
    productID = int(request.form.get('product'))
    cart = Cart(db)
    cartID = cart.get(userHandler.users[request.cookies.get('seshID')].email)
    cart.remove(productID)
    return redirect(url_for('products'))

@app.route('/account', methods=['GET', 'POST'])
def account():
    return render_template('AccountWidget.html', headerTitle = "Account")

@app.route('/resetConfirmed', methods=['GET','POST'])
def resetConfirmed():
    f = open('/SQL_setup.sql','r')
    data = f.read()
    data = data.replace("\n", "")
    db.runQuery(data)
    return render_template('resetConfirmed.html', data = "The database has been reset!")

@app.route('/banUser', methods=['GET', 'POST'])
def banUser():
    if(request.cookies.get('seshID') in userHandler.users):
        if(userHandler.users[request.cookies.get('seshID')].adminlevel >= 2):
            userHandler.banUser(request.form.get('email'))
    return redirect(url_for('root'))


#Run the server
if __name__ == '__main__':
    app.run()
    while True:
        time.sleep(10)

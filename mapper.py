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
    print(userHandler.users)
    if(request.cookies.get('seshID') in userHandler.users):
        response = make_response(render_template('account.html', content=["account"], user = userHandler.users[request.cookies.get('seshID')]))
        return response
    errors = []
    switch = request.form.get("submit")
    if(switch == "Login"):
        loginString = userHandler.returningUser(request.form.get("email"), request.form.get("password"))
        if('ERROR:' in str(loginString)):
            print(loginString)
            return render_template("account.html", content = ["login"], loginError = loginString, headerTitle = "Login")
        else:
            print("uuid: " + str(loginString))
            response = make_response(redirect(url_for('products')))
            response.set_cookie('seshID', loginString)
            return response

    elif(switch == "Register"):
        if(request.form.get("password") == request.form.get("passwordConfirm")):
            userHandler.newUser(request.form.get("name"), request.form.get("email"), request.form.get("password"), request.form.get("zipCode"), request.form.get("city"), request.form.get("address"), request.form.get("phone"), request.form.get("ssn"))
            return render_template('account.html', content = ["register"], headerTitle = "Register")
        else:
            request.form.clear
            return make_response("<p style='color:red; font-size:3em;'>Error: Passwords do not match!</p>", 1337)

    elif(switch == "Account"):
        pass

    return render_template('account.html', content = ["login", "register"], headerTitle = "Login or Register")





@app.route('/indsadex', methods=['GET', 'POST'])
def test(name="", password=""):
    name = request.form["name"]
    password = request.form["password"]

    return render_template('test.html', name = name, password = password)


@app.route('/products')
def products():
    products = db.runQuery("SELECT * FROM product_details")
    products = products.fetchall();
    return render_template('productContainer.html', products = products)

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

@app.route('/account', methods=['GET', 'POST'])
def account():
    return render_template('AccountWidget.html', headerTitle = "Account", )

@app.route('/resetConfirmed', methods=['GET','POST'])
def resetConfirmed():
    f = open('SQL_setup.sql','r')
    data = f.read();
    data = data.replace("\n", "")
    db.runQuery(data)
    return render_template('resetConfirmed.html', data = "The database has been reset!")


#Run the server
if __name__ == '__main__':
    app.run()
    while True:
        time.sleep(10)
        print(userHandler.users);

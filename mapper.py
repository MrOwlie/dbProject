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

def getHighestID ():
    query = "SELECT MAX(uid) FROM users"
    global currentID
    currentID = db.runQuery(query)
getHighestID()

@app.route('/', methods=['GET', 'POST'])
def root():
    errors = []
    switch = request.form.get("submit")
    if(switch == "Login"):
        errors = userHandler.returningUser(request.form.get("email"), request.form.get("password"))
        if(errors != None):
            return render_template("index.html",loginError = errors, headerTitle = "Login")
        else:
            return render_template("index.html", headerTitle = "Login")

    elif(switch == "Register"):
        if(request.form.get("password") == request.form.get("passwordConfirm")):
            userHandler.newUser(request.form.get("name"), request.form.get("email"), request.form.get("password"), request.form.get("zipCode"), request.form.get("city"), request.form.get("address"), request.form.get("phone"), request.form.get("ssn"))
            return render_template('index.html', headerTitle = "Register")
        else:
            request.form.clear
            return make_response("<p style='color:red; font-size:3em;'>Error: Passwords do not match!</p>", 1337)

    return render_template('index.html', headerTitle = "Register")


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # next_is_valid should check if the user has valid
        # permission to access the `next` url
        if not next_is_valid(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)


@app.route('/index', methods=['GET', 'POST'])
def test(name="", password=""):
    name = request.form["name"]
    password = request.form["password"]

    return render_template('test.html', name = name, password = password)

@app.route('/register', methods=['GET', 'POST'])
def register():
    #name = request.form['name']
    #email = request.form['email']
    #password = request.form['password']
    db.runQuery("UPDATE users SET ssn = '12414' WHERE uid = '12'")
    return redirect(make_response("<p>Query send</p>"))

@app.route('/reset', methods=['GET', 'POST'])
def reset():
    return render_template('reset.html', data = 'Did not confirm yet')

@app.route('/account', methods=['GET', 'POST'])
def account():
    return render_template('AccountWidget.html')

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

from flask import Flask
from flask import render_template
from flask import redirect
from flask import make_response
from flask import url_for
from flask import session
from flask import request
from flask_restful import Resource, Api
from flask_jsonrpc import JSONRPC
from flask_cors import CORS
from Database import Database
from UserHandler import UserHandler



#initialize the app and add extensions
app = Flask(__name__)
CORS(app)
db = Database(app)
userHandler = UserHandler(db)
#initialize the MySQL connection


#Static files
#url_for('static', filename = 'style.css')

#route the website

#index


@app.route('/', methods=['GET', 'POST'])
def root():
    switch = request.form.get("submit")
    if(switch == "Login"):
        userHandler.returningUser(request.form.get("name"), request.form.get("password"))
    elif(switch == "Register"):
        if(request.form.get("password") == request.form.get("passwordConfirm")):
            userHandler.newUser(request.form.get("name"), request.form.get("email"), request.form.get("password"), request.form.get("zipCode"), request.form.get("address"), request.form.get("phone"), request.form.get("ssn"))
            return render_template('index.html')
        else:
            request.form.clear
            return make_response("<p style='color:red; font-size:3em;'>Error: Passwords do not match!</p>", 1337)

    return render_template('index.html')



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


#Run the server
if __name__ == '__main__':
    app.run()
    while True:
        time.sleep(10)
        print(userHandler.users);

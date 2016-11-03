from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flaskext.mysql import MySQL
import database

#initialize the app and add extensions
app = Flask(__name__)

#initialize the MySQL connection
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'python'
app.config['MYSQL_DATABASE_PASSWORD'] = 'pythonpesswerd'
app.config['MYSQL_DATABASE_DB'] = 'dbproject'
app.config['MYSQL_DATABASE_HOST'] = 'arma.publiclir.se'
mysql.init_app(app)

#Static files
#url_for('static', filename = 'style.css')

#route the website

#index
@app.route('/')
def root():

    return render_template('index.html')

@app.route('/contact')
def contact():
    return "fredrik.uvgard@gmail.com <br/> johan.kannel@gmail.com"

@app.route('/about')
def about():
    return "made by Kannel and Fredrik"

@app.route('/register', methods=['GET', 'POST'])
def register():
    #name = request.form['name']
    #email = request.form['email']
    #password = request.form['password']
    return render_template('register.html')


#Run the server
if __name__ == '__main__':
    app.run()

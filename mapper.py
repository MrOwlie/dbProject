from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from database.py import Database

#initialize the app and add extensions
app = Flask(__name__)
db = new Database(app)
#initialize the MySQL connection


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

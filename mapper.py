from flask import Flask
from flask import render_template
from flask import url_for
from flaskext.mysql import MySQL
import pyjade

#initialize the app and add extensions
app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

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
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT name from products where uid=12")
    return cursor.fetchone()
    #return render_template('index.jade')




#Run the server
if __name__ == '__main__':
    app.run()

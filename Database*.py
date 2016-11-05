from flaskext.mysql import MySQL
from jsonrpc import ServiceMethod


class Database:

    __init__(self, app):
        #MYSQL init
        self.mysql = MySQL()
        app.config['MYSQL_DATABASE_USER'] = 'python'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'pythonpesswerd'
        app.config['MYSQL_DATABASE_DB'] = 'dbproject'
        app.config['MYSQL_DATABASE_HOST'] = 'arma.publiclir.se'
        self.mysql.init_app(app)


    def getCursor(self):
        #Creates cursor
        return self.mysql.get_db().cursor();

    def runQuery(self, query):
        #Creates cursor, executes query and returns the cursor
        cursor = getCursor(self)
        cursor.execute(query)
        return cursor

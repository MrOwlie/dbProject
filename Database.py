from flaskext.mysql import MySQL


class Database:

    def __init__(self, app):
        #MYSQL init
        self.mysql = MySQL()
        app.config['MYSQL_DATABASE_USER'] = 'python'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'pythonpesswerd'
        app.config['MYSQL_DATABASE_DB'] = 'dbproject'
        app.config['MYSQL_DATABASE_HOST'] = 'arma.publiclir.se'
        self.mysql.init_app(app)
        self.conn = self.mysql.connect()


    def getCursor(self):
        #Creates cursor
        return self.conn.cursor();

    def runQuery(self, query):
        #Creates cursor, executes query and returns the cursor
        cursor = self.getCursor()
        #query = "SELECT apahej HEJ"
        #query = "INSERT INTO users "
        print("asdasd " + query)
        cursor.execute(query)
        self.conn.commit()
        return cursor

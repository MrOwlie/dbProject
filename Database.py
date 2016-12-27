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
        try:
            cursor = self.getCursor()
            cursor.execute(query)
            self.conn.commit()
        except(UnicodeEncodeError):
            print ("UNICORNS EXIST")
        return cursor

    def validatePassword(self, email, password):
        #checks if the password entered in the frontend matches our DB records

        try:
            realPassword = self.runQuery("SELECT password FROM users WHERE email = '{}'".format(email))
            realPassword = realPassword.fetchone()[0]
        except (TypeError):
            return False
        return (password == realPassword)



def runQuery(cursor,query):
    cursor.execute(query)
    return cursor.fetchone()

def createUser(cursor,name,ssn,adress,email,zipCode,phone,password,adminlevel):
    query = "INSERT INTO users (name,ssn,adress,email,zip_code,phone,password,adminlevel) VALUES (" + name + "," + ssn "," + adress "," + email "," + zipCode "," + phone "," + password "," + adminlevel + ");"
    runQuery(cursor,query)

def validateUser (password):
    password = runQuery()

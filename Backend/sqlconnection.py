import mysql.connector
__cnx=None

def get_sql_connection():
    global __cnx
    print("SQL is starting... ")
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root',password='root',host='127.0.0.1',
                                        database='grocer_management_system')
    return __cnx

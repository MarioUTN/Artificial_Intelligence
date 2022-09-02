import pyodbc as conn
import psycopg2 as psy
import mysql.connector as mysql

host = '127.0.0.1'
dbname = 'mario'
username = 'usermarioutn'
password = 'password-sqlserver'


def Show(vector):
    resp = ""
    for i in range(len(vector)):
        resp = resp + str(vector[i]) + "\t"
    return resp


def connect_mysql(hostname, dbname, username, password):
    try:
        connect = mysql.connect(host=hostname, user=username, password=password, db=dbname)
        print('Database connect successfully to MySQL', connect)
        query = "select*from cliente"
        cursor=connect.cursor()
        cursor.execute(query)
        for tabla in cursor:
            print(tabla)
        #cursor.close()
        return connect
    except Exception as e:
        print('Ocurrio un error al conectar a MySQL')


cursor = connect_mysql("127.0.0.1", "mariosalazar", "root", "password-mysql").cursor()
print(cursor.execute('show tables'))



def connect_postgresql(hostname, dbname, username, password):
    try:
        conn_query = "host = '" + hostname + "' dbname = '" + dbname + "' user= '" + username + "' password= '" + password + "'"
        conn_post = psy.connect(conn_query)
        cursor = conn_post.cursor()
        print("Database connect successfully to PostgreSQL")
        return cursor
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)


print(connect_postgresql("172.20.142.85", "proyecto", "usermario", "password-usermario"))


def connect_sqlserver(hostname, dbname, username, password):
    try:
        conexion = conn.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                hostname + ';DATABASE=' + dbname + ';UID=' + username + ';PWD=' + password)
        cursor = conexion.cursor()
        print("Database connect successfully to SQL Server")
        return cursor
    except Exception as e:
        # Atrapar error
        print("Ocurrió un error al conectar a SQL Server: ", e)


print(connect_sqlserver("172.20.142.85", "mariosalazar", "sa", "password-sqlserver"))

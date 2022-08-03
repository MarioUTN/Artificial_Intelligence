import connect as connect
import pandas as pd
import sqlite3 as sql
import pyodbc as conn
import psycopg2 as psy
import matplotlib.pyplot as plt


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

cur = connect_sqlserver("127.0.0.1", "mario", "usermarioutn", "password-sqlserver")
cur.execute("SELECT*FROM view_invoice_byidcustomers")
resp = cur.fetchall()
# print(resp)
l = pd.array(resp)

titles = ["A", "B", "C", "D", "E", "F", "G", "H"]


def add(lista, index):
    a = []
    for dato in lista:
        a.append(dato[index])
    return a



a1 = add(l, 0)
a2 = add(l, 1)
a3 = add(l, 2)
a4 = add(l, 3)
a5 = add(l, 4)
a6 = add(l, 5)
a7 = add(l, 6)
a8 = add(l, 7)
a9 = add(l, 8)
a10 = add(l, 9)
a11 = add(l, 10)
a12 = add(l, 11)
a13 = add(l, 12)
a14 = add(l, 13)
a15 = add(l, 14)
a16 = add(l, 15)
a17 = add(l, 16)
a18 = add(l, 17)
a19 = add(l, 18)
a20 = add(l, 19)
a21 = add(l, 20)
a22 = add(l, 21)
a23 = add(l, 22)
a24 = add(l, 23)
a25 = add(l, 24)
a26 = add(l, 25)
a27 = add(l, 26)
a28 = add(l, 27)
a29 = add(l, 28)
a30 = add(l, 29)
a31 = add(l, 30)
a32 = add(l, 31)
a33 = add(l, 32)


a=[]
for i in range(32):
    resp = str('Title{0}'.format(i))
    resp1 = str('a{0}'.format(i))
    z = format(resp)+format(resp1)
    a.append(z)

a = {'Title 1': a1, 'Title 2': a2, 'Title 3': a3, 'Title 4': a4, 'Title 5': a5, 'Title 6': a6, 'Title 7': a7, 'Title 8': a8, 'Title 9': a9, 'Title 10': a10, 'Title 11': a11, 'Title 12': a12, 'Title 13': a13, 'Title 14': a14, 'Title 15': a15, 'Title 16': a16, 'Title 17': a17, 'Title 18': a18, 'Title 19': a19, 'Title 20': a20, 'Title 21': a21, 'Title 22': a22, 'Title 23': a23, 'Title 24': a24, 'Title 25': a25, 'Title 26': a26, 'Title 27': a27, 'Title 28': a28, 'Title 29': a29, 'Title 30': a30, 'Title 31': a31, 'Title 32': a32, 'Title 33': a33}

print(a)
df = pd.DataFrame(a)
#df.to_excel("mario.xlsx")

print(df.head(10))
print()
print(df.tail())
print()
print(df.shape)
print()
print(df.describe())
print()
print(df.dtypes)
print()
print(df['Title 7'].describe())

plt.figure()

plt.subplot(121)
plt.boxplot(df["Title 7"])
plt.ylabel("Overall")
plt.title("Real Madrid")
plt.grid(True)

plt.subplot(122)
plt.boxplot(df["Title 7"])
plt.title("Barcelona")
plt.grid(True)

"""
pd.DataFrame(view).to_excel('sample.xlsx', header=False, index=False)
print(type(view))


a = pd.DataFrame(view)
pd.DataFrame(a[0]).to_excel('sample1.xlsx', header=False, index=False)
print(a)
"""
"""
df = pd.read_excel("sample.xlsx")
print("Columns")
print(df.columns)

for item in view:
    print(connect.Show(item))
        # OK! conexión exitosa
"""

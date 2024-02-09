import cx_Oracle

dsn = cx_Oracle.makedsn('localhost', 1521, service_name='XE')
connection = cx_Oracle.connect(user='C##JSORTO', password='72776400', dsn=dsn)

cursor = connection.cursor()

sql = '''SELECT * FROM compras'''

cursor.execute(sql)
datos = cursor.fetchall()

for x in datos:
    print(x)

connection.close()

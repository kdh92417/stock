import pymysql

connection = pymysql.connect(host='localhost', port=3306, db='INVESTAR',
                             user='root', password='durwltkwl12', autocommit=True)

cursor = connection.cursor()
cursor.execute("SELECT VERSION();")
result = cursor.fetchone()

print("MariaDB version : {}".format(result))

connection.close()

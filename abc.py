import pymysql

dave_db = pymysql.connect(
        user='root',
        passwd='',
        host='127.0.0.1',
        db='ad',
        charset='utf8'
        )

cursor = dave_db.cursor(pymysql.cursors.DictCursor)
sql = """SELECT * FROM accounts;"""
cursor.execute(sql)
result = cursor.fetchall()
print(result)


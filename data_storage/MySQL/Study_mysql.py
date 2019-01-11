import pymysql
# 通过pymysql对象的connect()方法声明一个Mysql连接对象,用于连接mysql
db = pymysql.connect(host='localhost',user='root',password='zhiaini1314',port=3306,db='spiders')
# 调用cursor()方法获得Mysql的游标对象，可以利用游标来执行SQL语句
cursor = db.cursor()
# 调用execute()执行SQL语句
cursor.execute('select version()')
# 调用fetchone()方法获得第一条数据。
data = cursor.fetchone()
print("Database version: %s"%data)
# 关闭数据库连接
db.close()






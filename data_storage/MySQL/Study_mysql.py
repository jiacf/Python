import pymysql
# 通过pymysql对象的connect()方法声明一个Mysql连接对象,用于连接mysql
db = pymysql.connect(host='localhost',user='root',password='zhiaini1314',port=3306,db='spiders')
# 调用cursor()方法获得Mysql的游标对象，可以利用游标来执行SQL语句
cursor = db.cursor()
# 调用execute()执行SQL语句
cursor.execute('select version()')
# 调用fetchone()方法获得第一条数据。
data = cursor.fetchone()
data1 = {'id':'20121121',
       'name':'贾朝峰',
       'age':20
}
table = 'students'
key = ','.join(data1.keys())
values = ','.join(['%s']*len(data1))
sql = 'INSERT INTO {table} ({keys}) VALUES ({values})'.format(table=table,keys=key,values=values)
print(sql)
try:
    if cursor.execute(sql,tuple(data1.values())):
        print('成功')
        # 提交表单
        db.commit()
except:
    print('失败')
    # 提交失败，事件回滚
    db.rollback()
# 关闭数据库连接
db.close()



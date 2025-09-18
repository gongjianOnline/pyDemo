"""
    pymysql
        操作步骤
            1. 获取连接对象. python 连接 MySQL 的对象
            2. 获取游标对象  可以执行 SQL 语句的对象


"""


import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='gong93692',
    database='world',
    charset='utf8'
)

#  游标对象
cus = conn.cursor()

# 执行SQL
sql = 'select * from city'
cus.execute(sql)

# 操作结果集
data = cus.fetchall()
print(data)

cus.close()
conn.close()

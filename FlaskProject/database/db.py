# # db.py
# import pymysql
# from dbutils.pooled_db import PooledDB
# from pymysql.cursors import DictCursor
#
# pool = PooledDB(
#     creator=pymysql,
#     maxconnections=20,     # 连接池最大连接数
#     mincached=2,           # 启动时创建的空闲连接
#     maxcached=10,          # 连接池最多空闲连接数
#     blocking=True,         # 池满后阻塞等待
#     ping=5,                # 0=从不，1=默认:每次请求前ping，避免MySQL断开
#     host="127.0.0.1",
#     port=3307,
#     user="root",
#     password="",
#     database="vote",
#     charset="utf8mb4",
#     cursorclass=DictCursor # 返回字典
# )
#
# def fetch_one(sql):
#     conn = pool.connection()
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return result


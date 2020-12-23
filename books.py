from pymysql import connect
from pymysql.cursors import  DictCursor
from settings import MYSQL_HOST, MYSQL_PORT, MYSQL_PASSWORD, MYSQL_DATABASE, MYSQL_USER

class Book(object):
    def __init__(self):  # 双下划线 -- 魔法方法， 创建对象的同时要执行的代码
        self.conn = connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            charset='utf8'
            )
        self.cursor = self.conn.cursor(DictCursor)  # 返回字典的形式

    def __del__(self):  # 释放对象时要执行的代码
        self.cursor.close()
        self.conn.close()

    def get_books_infos_limit(self):
        sql = 'select * from book_infos limit 3'
        result = self.cursor.execute(sql)  # 3
        data = []
        for temp in self.cursor.fetchall():
            print(temp)
            data.append(temp)
        return data
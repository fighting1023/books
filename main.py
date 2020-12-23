# 用flask起一个服务

from flask import Flask, jsonify
from books import Book
"""
接口说明：
    1. 返回的是json数据
    2. 结构如下
        {
            resCode: 0, # 非0即错误
            data:  # 数据位置，一般是数组
            message: # 对本次请求的说明
        }
"""
app = Flask(__name__)

# 1. 直接执行这个文件
# 2. __name__ = 当前文件的名字

app.config['JSON_AS_ASCII'] = False  # 将文字重新编码


@app.route('/', methods=['GET'])
def hello_world():
    book = Book()
    arrData = book.get_books_infos_limit()
    return jsonify(arrData)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

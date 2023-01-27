# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hi():
    return 'HI'
    
# 문자 입력
@app.route('/greet/<name>')
def greeting(name):
    return f'안녕 {name}'

# 숫자 입력
@app.route('/myblog/<int:num>')
def myblog(num):
    # print(type(num))
    return f'나의 블로그 - {num}'

# 수정 번호 0.1, 실수형
@app.route('/float/<float:num>')
def float(num):
    print(type(num))
    return f'수정 번호 - {num}'

if __name__ == '__main__':
    app.run(debug=True)
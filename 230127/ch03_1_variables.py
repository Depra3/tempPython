# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hi():
    return 'HI'
    
@app.route('/greet/<name>')
def greeting(name):
    return f'안녕 {name}'

if __name__ == '__main__':
    app.run(debug=True)
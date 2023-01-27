# redirect
# 원래 페이지로 돌아가기

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hi():
    return 'Hi'

# 3개의 페이지 만들기 - Admin / Guest / 사용자 페이지
@app.route('/admin')
def admin():
    return 'Admin 페이지 입니다.'

@app.route('/guest/<guest>')
def guest(guest):
    return f'안녕 {guest}님은 게스트 입니다.'

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest = name))
    

if __name__ == "__main__":
    app.run(debug=True)
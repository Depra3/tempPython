from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def hi():
    return 'HI'

@app.route('/success/<name>')
def success(name):
    return f'{name}을 환영합니다.' # f없으면 그대로 출력

@app.route('/submit', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, jsonify, request, render_template

app = Flask(__name__, static_url_path='/templates')

# @app.route('/')
# def ():
#     return render_template('.html')
@app.route('/login')
def login():
    username = request.args.get('user_name')
    password = request.args.get('pw')

    if username == 'dave':
        return_data = {'auth' : 'success'}
    else:
        return_data = {'auth' : 'failed'}
    return jsonify(return_data)

@app.route('/html_test')
def hellow_html():
    return render_template('login.html')

@app.route('/html_test1')
def hello_html1():
    return render_template('login_raw.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')
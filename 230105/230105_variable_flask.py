from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('variable.html',name1=user, name2=2)

@app.route('/hello2/<user1>/<user2>')
def hello_name2(user1, user2):
    return render_template('variable.html',name1=user1, name2=user2)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello_if1')
def hello_name():
    value = 27
    return render_template('condition.html', data=value)

@app.route('/hello_if2/<value>')
def hello_name1(value):
    return render_template('condition.html', data=int(value))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')
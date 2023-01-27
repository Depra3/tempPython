from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/hello/<user>')
def hello(user):
    return render_template('hello.html', name=user)

if __name__ == "__main__":
    app.run(debug=True)
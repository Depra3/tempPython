from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return '첫번째 페이지'

@app.route('/he')
def he():
    return 'Hello'

@app.route('/greet')
def greeting():
    return 'Hello World!!'

if __name__ == "__main__":
    app.run(debug=True)
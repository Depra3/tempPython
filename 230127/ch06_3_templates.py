from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hi():
    return 'HI'

@app.route('/score/<int:score>')
def a_test(score):
    return render_template('score.html', marks=score)

if __name__ == '__main__':
    app.run(debug=True)
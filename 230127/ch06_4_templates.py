from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hi():
    return 'HI'

@app.route('/result')
def result():
    data_dict = {'수학':50, '국어':90, '영어':100}
    return render_template('result.html', result=data_dict)

if __name__ == '__main__':
    app.run(debug=True)
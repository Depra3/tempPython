from flask import Flask, render_template

app = Flask(__name__)

@app.route('/helloloop')
def hello_name():
    value_list = ['list1', 'list2', 'list3']
    return render_template('loop.html', values=value_list)

@app.route('/helloloop1/<list>')
def hello_name1(list):
    # value_list1 = eval(list)
    return render_template('loop.html', values=list)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')
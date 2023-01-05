from flask import Flask, jsonify, request, render_template

app = Flask(__name__, static_url_path='/templates')

@app.route('/checkout')
def hello_html():
    return render_template('checkout.html')

@app.route('/')
def hello_html1():
    return render_template('blog_index.html')

@app.route('/blog')
def hello_html2():
    return render_template('blog_html.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')
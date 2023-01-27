from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    message = "Hello, World"
    return render_template('hello.html', 
                           message=message)

@app.route("/css")
def hello_css():
    message = "Hello, World"
    return render_template('hello2.html', 
                           message=message)

@app.route("/js")
def hello_js():
    message = "Hello, World"
    return render_template('hello3.html', 
                           message=message)

@app.route("/image")
def serve_image():
    message = "Image Route"
    return render_template('images.html', message=message)

@app.route("/video")
def serve_video():
    message = "Video Route"
    return render_template('video.html', message=message)

@app.route("/audio")
def serve_audio():
    message = "Audio Route"
    return render_template('audio.html', message=message)

if __name__ == '__main__':
   app.run(debug = True)
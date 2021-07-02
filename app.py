from flask import Flask, render_template, request
from flooddetection import get
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html");   
@app.route("/", methods = ['POST'])
def final():
    text = request.form['text']
    labe = get(text)
    return render_template('final.html', url = text, stat = labe)

if __name__ == "__main__":
    app.run()

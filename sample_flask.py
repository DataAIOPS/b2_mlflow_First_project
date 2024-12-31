from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/home")
def home():
    return "Welcome to flask"


@app.route("/contact")
def contact():
    return "Welcome to contact page"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)
# import flask
from flask import request
from flask.templating import render_template
from flask import Flask

#initiate flask
app = Flask(__name__)

# Define routes first of all default route is/
@app.route('/')
def home():
    return "Web development in Python updated 123"

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"{a} + {b} = {a + b}"

@app.route("/sub/<int:a>/<int:b>")
def sub(a, b):
    return f"{a} - {b} = {a - b}"

@app.route("/template")
def template():
    return render_template("index.html", name="Hello Cosmos")

@app.route("/newtemplate")
def newtemplate():
    return render_template("page.html")

# run the app
if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
from flask import request

app = Flask (__name__)
@app.route('/')
def home():
    return'Hello World!'
@app.route('/greet/<name>')
def greet (name):
    return f'helllo, {name }!'
@app.route("/add/<int:a>/<int:b>")
def add (a,b):
    return f'{a} + {b}= {a+b}'
@app.route('/sub/<int:a>/<int:b>')
def sub(a,b):
    return f'{a} - {b} = {a-b}'
@app.route('/mul/<int:a>/<int:b>')
def div(a,b):
    return f'{a} * {b} = {a*b}'
@app.route('/template')
def template():
    return render_template('index.html', name='anita')



@app.route("/submit", methods =["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}, whats up?!"
    return render_template ("form.html")

@app.route("/page-form")
def page_form():
    return render_template("page-form.html")

if __name__== "__main__":

    app.run(host = "0.0.0.0",port=5001)

if __name__=='__main__':
    app.run(debug = True)

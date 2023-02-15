#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    return "C {}".format(text.replace("_", " "))

@app.route("/python", defaults={'text': 'is_cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    return "Python {}".format(text.replace("_", " "))

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n):
    return render_template('5-num.html', num=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def num_type(n):
    return render_template('6-num_type.html', num=n)



if __name__ == "__main__":
    app.run(host='0.0.0.0')

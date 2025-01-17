#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ Hello """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ HBNB """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ c text """
    return "C {}".format(text.replace("_", " "))

@app.route("/python", defaults={'text': 'is_cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """ python text """
    return "Python {}".format(text.replace("_", " "))

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ nos text """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

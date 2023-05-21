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
    """ C TEXTS """
    return "C {}".format(text.replace("_", " "))

@app.route("/python", defaults={'text': 'is_cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """ PYTHON TEXT """
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0')

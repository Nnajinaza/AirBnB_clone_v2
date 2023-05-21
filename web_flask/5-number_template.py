#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ HELLO """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ HBNB """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ C TEXT """
    return "C {}".format(text.replace("_", " "))

@app.route("/python", defaults={'text': 'is_cool'})
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """PYTHON TEXT """
    return "Python {}".format(text.replace("_", " "))

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Nos text """
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n):
    """ Num template """
    return render_template('5-number.html', num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

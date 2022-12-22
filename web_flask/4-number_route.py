#!/usr/bin/python3
"""
Mini Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """
    Route to home page
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route to hbnb page
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route for c page
    """
    res = text.replace('_', " ")
    return "C {}".format(res)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """
    Route for python page
    """
    res = text.replace('_', " ")
    return "Python {}".format(res)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route for number page
    """
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

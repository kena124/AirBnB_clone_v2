#!/usr/bin/python3
"""
Mini Flask web application
"""
from flask import Flask, render_template
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Rout for number template
    """
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """
    Route for parity page
    """
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

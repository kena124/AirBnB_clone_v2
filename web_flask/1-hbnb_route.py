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


if __name__ == "__main__":
    app.run(host='0.0.0.0')

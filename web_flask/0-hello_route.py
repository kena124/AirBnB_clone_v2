#!/usr/bin/python3
"""
Mini Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Home page
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0')

#!/usr/bin/python3
"""
 a script that starts a Flask web application
"""
from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """function to return text"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """function to return text"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """function to return texT"""
    return f"C {escape(text).replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """function to return text"""
    return f"Python {escape(text).replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

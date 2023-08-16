#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHBNB():
    """Displays a string to stdout"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hBNB():
    """Displays a string to stdout"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """Displays a string to stdout"""
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    """Displays a string to stdout"""
    text = text.replace('_', ' ')
    return f'Python {escape(text)}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

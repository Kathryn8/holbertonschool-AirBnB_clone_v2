#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays a string to stdout"""
    return f'{escape(n)} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a string to stdout"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """Displays a string to stdout"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

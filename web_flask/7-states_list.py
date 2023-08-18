#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_objects():
    """Displays a HTML page"""
    return render_template('7-states_list.html', states=storage.all(State))


@app.teardown_appcontext
def teardown_db(exception):
    """ remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

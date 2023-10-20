#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
import os


app = Flask(__name__)
db = os.environ.get("HBNB_TYPE_STORAGE")


@app.teardown_appcontext
def remove_session(e):
    """closes session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def show_cities_by_states():
    """
    renders a page with all cities in states
    """
    states = list(storage.all(State).values())
    return render_template('8-cities_by_states.html', states=states, db=db)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

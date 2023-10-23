#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
import os


app = Flask(__name__)


@app.teardown_appcontext
def remove_session(e):
    """closes session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    renders hbnb filters
    """
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

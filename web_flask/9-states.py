#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
import os


app = Flask(__name__)


@app.teardown_appcontext
def remove_session(e):
    """closes session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """
    renders a page with all states
    """
    db_type = os.environ.get('HBNB_TYPE_STORAGE')
    states = list(storage.all(State).values())
    return render_template('9-states.html', states=states, id=id, db=db_type)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

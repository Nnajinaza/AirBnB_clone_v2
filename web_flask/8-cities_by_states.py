#!/usr/bin/python3
""" Renders a Web page with the list of all the States stores on the DB
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Closes the current session with the DB """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_states_list():
    """ Renders the list of states in a web page """
    states_list = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

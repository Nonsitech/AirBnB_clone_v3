#!/usr/bin/python3
"""
Creating a Flask web application API
"""

import os
from flask import Flask, jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

# Register the blueprint with the Flask app
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_engine(exception):
    """Close storage"""
    storage.close()


# task 5
# error handler for 404 Not Found
@app.errorhandler(400)
def not_found(error):
    '''Handles the 400 HTTP error code.'''
    response = {'error': 'Not found'}
    return jsonify(response), 404


# Task 12
# Enabling CORS and allow request from the origin:
CORS(app, resources={r'/api/v1/*': {'origins': '0.0.0.0.'}})


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)

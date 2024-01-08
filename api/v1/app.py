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
app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
app_port = int(os.getenv('HBNB_API_PORT', '5000'))
# Task 12
# Enabling CORS and allow request from the origin:
CORS(app, resources={'/*': {'origins': app_host}})


@app.teardown_appcontext
def teardown_engine(exception):
    """Close storage"""
    storage.close()


# task 5
# error handler for 404 Not Found
@app.errorhandler(400)
def not_found(error):
    """Handling the 400 HTTP error code"""
    response = {'error': 'Not found'}
    return jsonify(response), 404

@app.errorhandler(400)
def error_400(error):
    """Handling the 400 HTTP error code"""
    msg = 'Bad request'
    if isinstance(error, Exception) and hasattr(error, 'description'):
        msg = error.description
    return jsonify(error=msg), 400


if __name__ == "__main__":
    app_host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    app_port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=app_host, port=app_port, threaded=True)

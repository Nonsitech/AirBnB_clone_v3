#!/usr/bin/python3
"""Create a route "/status" on the object app_views"""

from flask import jsonify
from models import storage
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def api_status():
    """
    Status of API
    """
    responce = {'status': 'OK'}
    return jsonify(responce)

# task 4
@app_views.route('/stats', methods=['GET'])
def get_stats():
    """Retrieves the number of each objects by type"""
    stats {
        'aminities': storage.count('Aminity'),
        'cities': storage.count('City'),
        'palaces': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('Usuer')
    }
    return jsonify(stats)
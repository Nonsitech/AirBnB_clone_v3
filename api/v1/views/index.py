#!/usr/bin/python3
"""Create a route "/status" on the object app_views"""

from flask import jsonify
from models import storage
from api.v1.views import app_views
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


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
    atats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)

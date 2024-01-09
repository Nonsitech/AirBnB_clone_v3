#!/usr/bin/python3
"""Create a route "/status" on the object app_views"""
from flask import jsonify

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route('/status')
def api_status():
    """
    Status of API
    """
    responce = {'status': 'OK'}
    return jsonify(responce)


# task 4
@app_views.route('/stats')
def get_stats():
    """Retrieves the number of each objects by type"""
    objects = {
        'amenities': Amenity,
        'cities': City,
        'places': Place,
        'reviews': Review,
        'states': State,
        'users': User
    }
    for key, value in objects.items():
        objects[key] = storage.count(value)
    return jsonify(objects)

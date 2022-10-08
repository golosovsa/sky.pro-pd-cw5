"""
    flask initialization module with create_app function
"""

from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException
from app.setup.api import api
from app.views import equipment_ns, weapon_ns, armor_ns, unit_class_ns
from app.game_container import Equipment


def base_service_error_handler(exception: HTTPException):
    return jsonify({'error': str(exception)}), exception.code


def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    api.init_app(app)
    api.add_namespace(equipment_ns)
    api.add_namespace(weapon_ns)
    api.add_namespace(armor_ns)
    api.add_namespace(unit_class_ns)
    app.register_error_handler(HTTPException, base_service_error_handler)
    Equipment(app.config["EQUIPMENT_DATA"])
    return app

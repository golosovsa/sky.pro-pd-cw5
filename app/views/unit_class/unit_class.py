"""
    UnitClass view
"""

from flask_restx import Namespace, Resource  # type: ignore
from werkzeug.exceptions import NotFound

from app.service_container import unit_class_service
from app.setup.api.models import unit_class_names_schema, unit_class_schema

api = Namespace("unit-class", description="Unit class handler")


@api.route("/")
class UnitClassesView(Resource):
    @api.marshal_with(unit_class_names_schema, code=200, description="Ok")
    def get(self):
        data = {
            "unit_class_names": unit_class_service.get_names()
        }
        return data


@api.route("/<name>")
class UnitClassView(Resource):

    @api.response(404, "Not Found")
    @api.marshal_with(unit_class_schema, code=200, description="OK")
    def get(self, name: str):
        model = unit_class_service.get_by_name(name)
        if model is None:
            raise NotFound()
        return unit_class_service.get_by_name(name)

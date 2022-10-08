"""
    Equipment view
"""

from flask_restx import Namespace, Resource  # type: ignore

from app.service_container import weapon_service, armor_service
from app.setup.api.models import equipment_names_schema

api = Namespace("equipment", description="Equipment handle")


@api.route("/")
class EquipmentView(Resource):
    @api.marshal_with(equipment_names_schema, code=200, description="Ok")
    def get(self):
        data = {
            "weapon": weapon_service.get_names(),
            "armor": armor_service.get_names(),
        }
        return data

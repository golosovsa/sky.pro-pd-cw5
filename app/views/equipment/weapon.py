"""
    Equipment/weapon view
"""

from flask_restx import Resource, Namespace  # type: ignore
from werkzeug.exceptions import NotFound

from app.service_container import weapon_service
from app.setup.api.models import weapon_schema


api = Namespace(name="weapon", description="Weapon handle", path="/equipment/weapon")


@api.route("/<name>")
class WeaponView(Resource):

    @api.response(404, "Not Found")
    @api.marshal_with(weapon_schema, code=200, description="OK")
    def get(self, name: str):
        model = weapon_service.get_by_name(name)
        if model is None:
            raise NotFound()
        return weapon_service.get_by_name(name)

"""
    Equipment/weapon view
"""

from flask_restx import Resource, Namespace  # type: ignore
from werkzeug.exceptions import NotFound

from app.service_container import armor_service
from app.setup.api.models import armor_schema


api = Namespace(name="armor", description="Armor handle", path="/equipment/armor")


@api.route("/<name>")
class ArmorView(Resource):

    @api.response(404, "Not Found")
    @api.marshal_with(armor_schema, code=200, description="OK")
    def get(self, name: str):
        model = armor_service.get_by_name(name)
        if model is None:
            raise NotFound()
        return model

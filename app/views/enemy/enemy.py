"""
    Enemy view
"""

from flask_restx import Namespace, Resource  # type: ignore
from werkzeug.exceptions import BadRequest

from app.service_container import enemy_service
from app.setup.api.models import unit_schema

api = Namespace("enemy", description="Enemy handle")


@api.route("/")
class EnemyView(Resource):
    @api.response(400, "Bad request")
    @api.marshal_with(unit_schema, code=200, description="Ok")
    def get(self):
        enemy = enemy_service.get_item(0)
        if enemy is None:
            raise BadRequest
        return enemy

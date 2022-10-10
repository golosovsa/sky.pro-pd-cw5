"""
    Enemy view
"""

from flask_restx import Namespace, Resource  # type: ignore
from werkzeug.exceptions import BadRequest

from app.service_container import enemy_service
from app.setup.api.models import unit_schema
from app.setup.api.parsers import create_unit_args_parser

api = Namespace("enemy", description="Enemy handle")


@api.route("/")
class EnemyView(Resource):
    @api.response(400, "Bad request")
    @api.marshal_with(unit_schema, code=200, description="Ok")
    def get(self):
        enemy = enemy_service.get_item(0)
        if enemy is None:
            raise BadRequest()
        return enemy

    @api.response(400, "Bad request")
    @api.expect(create_unit_args_parser)
    def post(self):
        if not enemy_service.create_enemy(**create_unit_args_parser.parse_args()):
            raise BadRequest()
        return "OK", 201, {"Location": "/enemy/"}

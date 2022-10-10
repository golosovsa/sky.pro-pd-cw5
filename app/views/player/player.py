"""
    Player view
"""

from flask_restx import Namespace, Resource  # type: ignore
from werkzeug.exceptions import BadRequest

from app.service_container import player_service
from app.setup.api.models import unit_schema
from app.setup.api.parsers import create_unit_args_parser

api = Namespace("player", description="player handle")


@api.route("/")
class PlayerView(Resource):
    @api.response(400, "Bad request")
    @api.marshal_with(unit_schema, code=200, description="Ok")
    def get(self):
        player = player_service.get_item(0)
        if player is None:
            raise BadRequest()
        return player

    @api.response(400, "Bad request")
    @api.expect(create_unit_args_parser)
    def post(self):
        if not player_service.create_player(**create_unit_args_parser.parse_args()):
            raise BadRequest()
        return "OK", 201, {"Location": "/player/"}

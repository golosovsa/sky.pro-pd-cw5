"""
    Fight view
"""

from flask_restx import Namespace, Resource  # type: ignore
from werkzeug.exceptions import BadRequest

from app.service_container import fight_service
from app.setup.api.parsers import fight_args_parser

api = Namespace("fight", description="Fight handle")


@api.route("/")
class StartGameView(Resource):

    @api.response(400, "Bad request")
    @api.expect(fight_args_parser)
    def post(self):
        if not fight_service.fight(**fight_args_parser.parse_args()):
            raise BadRequest()
        return "OK", 201, {"Location": "/status/"}

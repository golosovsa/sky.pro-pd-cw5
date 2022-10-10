"""
    StartGame view
"""

from flask_restx import Namespace, Resource  # type: ignore
from werkzeug.exceptions import BadRequest

from app.service_container import game_service

api = Namespace("start-game", description="Start game handle")


@api.route("/")
class StartGameView(Resource):

    @api.response(400, "Bad request")
    def post(self):
        if not game_service.start_game():
            raise BadRequest()
        return "OK", 201, {"Location": "/status/"}

"""
    BattleLog view
"""

from flask_restx import Namespace, Resource  # type: ignore

from app.service_container import battle_log_service
from app.setup.api.models import battle_log_schema

api = Namespace("battle-log", description="Battle log handler")


@api.route("/")
class BattleLogView(Resource):

    @api.marshal_with(battle_log_schema, code=200, description="Ok")
    def get(self):
        return battle_log_service.get_item(0)

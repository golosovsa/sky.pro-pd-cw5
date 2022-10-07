"""
    Status view
"""

from flask_restx import Namespace, Resource  # type: ignore

api = Namespace('status', description="game status")


@api.route('/')
class StatusView(Resource):
    def get(self):
        return

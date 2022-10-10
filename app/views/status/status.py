"""
    Status view
"""

from flask_restx import Namespace, Resource  # type: ignore

from app.service_container import status_service
from app.setup.api.models import status_schema

api = Namespace('status', description="game status")


@api.route('/')
class StatusView(Resource):

    @api.marshal_with(status_schema, code=200, description="Ok")
    def get(self):
        return status_service.get_item(0)

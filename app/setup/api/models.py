"""
    App answer models for restx api
"""

from flask_restx import fields, Model  # type: ignore

from app.setup.api import api

status_schema: Model = api.model(
    name="Status",
    model={
        "server_status": fields.String,
        "current_screen": fields.String,
    }
)

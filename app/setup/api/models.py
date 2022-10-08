"""
    App answer models for restx api
"""

from flask_restx import fields, Model  # type: ignore

from app.setup.api import api

status_schema: Model = api.model(
    name="Status",
    model={
        "server_status": fields.String(description="Server status, always 'online' if the server is available"),
        "current_screen": fields.String(description="Screen Name for Single Page Server Application"),
    }
)

weapon_schema: Model = api.model(
    name="Weapon",
    model={
        "name": fields.String(description="Weapon name"),
        "min_damage": fields.Float(description="Weapon min damage"),
        "max_damage": fields.Float(description="Weapon max damage"),
        "stamina_per_hit": fields.Float(description="Stamina consumption"),
    }
)

armor_schema: Model = api.model(
    name="Armor",
    model={
        "name": fields.String(description="Armor name"),
        "defence": fields.Float(description="Armor defence"),
        "stamina_per_turn": fields.Float(description="Stamina consumption"),
    }
)

equipment_names_schema: Model = api.model(
    name="Equipment names",
    model={
        "weapon": fields.List(fields.String, description="List of weapon names"),
        "armor": fields.List(fields.String, description="List of armor names"),
    }
)

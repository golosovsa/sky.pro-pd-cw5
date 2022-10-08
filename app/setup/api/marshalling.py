"""
    Custom app data marshalling classes for restx api
"""

from flask_restx import fields  # type: ignore


class SkillField(fields.Raw):
    def format(self, value):
        return {
            "name": value.name,
            "stamina": value.stamina,
            "damage": value.damage,
        }

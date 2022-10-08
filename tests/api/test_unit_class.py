"""
    Api testing
    route unit-class
"""

from flask import Response
from app.game_container import unit_classes


class TestUnitClassRoute:

    def test_get_all_request(self, client):
        response: Response = client.get("/unit-class/")

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert response.is_json

        data = response.json

        assert "unit_class_names" in data
        assert len(data["unit_class_names"]) == len(unit_classes)

    def test_get_by_name_request(self, client):
        for name in unit_classes:
            response: Response = client.get(f"/unit-class/{name}")
            assert response.status_code == 200
            assert response.headers["Content-Type"] == "application/json"
            assert response.is_json
            data = response.json
            print(data)

            assert "name" in data
            assert "max_health" in data
            assert "max_stamina" in data
            assert "attack" in data
            assert "stamina" in data
            assert "skill" in data

            skill = data["skill"]

            assert "name" in skill
            assert "stamina" in skill
            assert "damage" in skill

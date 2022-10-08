"""
    Api testing
    route equipment
"""

from flask import Response


class TestEquipmentRoute:

    def test_get_all_request(self, client, equipment_data):
        response: Response = client.get("/equipment/")

        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert response.is_json

        data = response.json

        assert "weapon" in data
        assert "armor" in data

        assert len(data["weapon"]) == len(equipment_data["weapons"])
        for weapon in equipment_data["weapons"]:
            assert weapon["name"] in data["weapon"]

        assert len(data["armor"]) == len(equipment_data["armors"])
        for weapon in equipment_data["armors"]:
            assert weapon["name"] in data["armor"]


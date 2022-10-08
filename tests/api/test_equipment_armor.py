"""
    Api testing
    route equipment/weapon/<name>
"""

from pytest import fixture
from flask import Response


@fixture
def armor_names(client):
    response: Response = client.get("/equipment/")
    data = response.json
    return data["armor"]


class TestArmorRoute:

    def test_armor_request(self, client, armor_names, equipment_data):
        for name in armor_names:
            response: Response = client.get(f"/equipment/armor/{name}")
            assert response.status_code == 200
            assert response.headers["Content-Type"] == "application/json"
            assert response.is_json
            data = response.json

            for armor in equipment_data["armors"]:
                if name == armor["name"]:
                    assert data["defence"] == armor["defence"]
                    assert data["stamina_per_turn"] == armor["stamina_per_turn"]
                    break
            else:
                assert False

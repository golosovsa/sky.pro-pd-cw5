"""
    Api testing
    route equipment/weapon/<name>
"""

from pytest import fixture
from flask import Response


@fixture
def weapon_names(client):
    response: Response = client.get("/equipment/")
    data = response.json
    return data["weapon"]


class TestWeaponRoute:

    def test_weapon_request(self, client, weapon_names, equipment_data):
        for name in weapon_names:
            response: Response = client.get(f"/equipment/weapon/{name}")
            assert response.status_code == 200
            assert response.headers["Content-Type"] == "application/json"
            assert response.is_json
            data = response.json

            for weapon in equipment_data["weapons"]:
                if name == weapon["name"]:
                    assert data["min_damage"] == weapon["min_damage"]
                    assert data["max_damage"] == weapon["max_damage"]
                    assert data["stamina_per_hit"] == weapon["stamina_per_hit"]
                    break
            else:
                assert False

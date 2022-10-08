"""
    Api testing
    route battle-log
"""

from flask import Response


class TestBattleLog:

    def test_get_all_request(self, client):
        response: Response = client.get("/battle-log/")
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert response.is_json

        data = response.json

        assert "log" in data
        assert type(data["log"]) == list

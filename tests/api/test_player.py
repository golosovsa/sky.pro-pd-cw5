"""
    Api testing
    route player
"""

from flask import Response

from app.game_container import game, Game


class TestPlayerRoute:

    def test_get_by_id_request_before_select_player(self, client):
        assert game.screen == "start_and_results"
        response: Response = client.get(f"/player/")
        assert response.status_code == 404

        game._arena = None
        game._player = None
        game._enemy = None

    def test_get_by_id_request_after_game_start(self, client):
        assert game.screen == "start_and_results"
        game.start_game()
        assert game.screen == "create_player"
        game.select_player("Player", "Воин", "панцирь", "топорик")
        response: Response = client.get(f"/player/")
        assert response.status_code == 200
        assert response.headers["Content-Type"] == "application/json"
        assert response.is_json
        data = response.json

        assert "name" in data
        assert "health_points" in data
        assert "stamina_points" in data
        assert "unit_class" in data
        assert "weapon" in data
        assert "armor" in data
        assert data["name"] == "Player"
        assert data["unit_class"] == "Воин"
        assert data["armor"] == "панцирь"
        assert data["weapon"] == "топорик"

        game._arena = None
        game._player = None
        game._enemy = None


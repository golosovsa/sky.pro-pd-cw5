"""
    Api testing
    route enemy
"""

from flask import Response

from app.game_container import game


class TestEnemyRoute:

    def test_get_by_id_request_before_select_enemy(self, client):
        response: Response = client.get(f"/player/")
        assert response.status_code == 404

    def test_get_by_id_request_after_game_start(self, client):
        assert game.screen == "start_and_results"
        game.start_game()
        assert game.screen == "create_player"
        game.select_player("Player", "Воин", "панцирь", "топорик")
        assert game.screen == "create_enemy"
        game.select_enemy("Enemy", "Вор", "панцирь", "топорик")
        response: Response = client.get(f"/enemy/")
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
        assert data["name"] == "Enemy"
        assert data["unit_class"] == "Вор"
        assert data["armor"] == "панцирь"
        assert data["weapon"] == "топорик"
        game._player = None
        game._arena = None
        game._enemy = None



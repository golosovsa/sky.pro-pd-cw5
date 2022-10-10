"""
    Api testing
    route start-game
"""

from flask import Response

from app.game_container import game


class TestStartGame:

    def test_start_game(self, client):
        assert game.screen == "start_and_results"
        response: Response = client.post("/start-game/")
        assert response.status_code == 201

        game._arena = None
        game._player = None
        game._enemy = None

"""
    Api testing
    route fight
"""
import json

from flask import Response

from app.game_container import game


class TestFight:

    def test_fight_failed_page_start_and_results(self, client):
        assert game.screen == "start_and_results"
        response: Response = client.post("/fight/")
        assert response.status_code == 400

        game._arena = None
        game._player = None
        game._enemy = None

    def test_fight_failed_page_create_player(self, client):
        assert game.screen == "start_and_results"
        game.start_game()
        assert game.screen == "create_player"
        response: Response = client.post("/fight/")
        assert response.status_code == 400

        game._arena = None
        game._player = None
        game._enemy = None

    def test_fight_failed_page_create_enemy(self, client):
        assert game.screen == "start_and_results"
        game.start_game()
        assert game.screen == "create_player"
        game.select_player("Player", "Воин", "панцирь", "топорик")
        assert game.screen == "create_enemy"
        response: Response = client.post("/fight/")
        assert response.status_code == 400

        game._arena = None
        game._player = None
        game._enemy = None

    def test_fight(self, client):
        assert game.screen == "start_and_results"
        game.start_game()
        assert game.screen == "create_player"
        game.select_player("Player", "Воин", "панцирь", "топорик")
        assert game.screen == "create_enemy"
        game.select_enemy("Enemy", "Воин", "панцирь", "топорик")
        assert game.screen == "fight"
        response: Response = client.post("/fight/", data={"action": "hit"})
        assert response.status_code == 201
        response: Response = client.post("/fight/", data={"action": "skill"})
        assert response.status_code == 201
        response: Response = client.post("/fight/", data={"action": "skip"})
        assert response.status_code == 201

        game._arena = None
        game._player = None
        game._enemy = None

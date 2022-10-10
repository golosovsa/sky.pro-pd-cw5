import json

import pytest
import os
from app.interfaces.equipment import BaseEquipment
from app.server import create_app
from app.config import TestingConfig


os.environ["APP_ENV"] = "testing"


@pytest.fixture
def equipment_data():
    return {
        "weapons": [
            {
                "id": 1,
                "name": "топорик",
                "min_damage": 2.5,
                "max_damage": 4.1,
                "stamina_per_hit": 1.8
            },
            {
                "id": 2,
                "name": "ножик",
                "min_damage": 1.2,
                "max_damage": 2.5,
                "stamina_per_hit": 1.3
            },
            {
                "id": 3,
                "name": "ладошки",
                "max_damage": 1,
                "min_damage": 0.5,
                "stamina_per_hit": 1
            }
        ],
        "armors": [
            {
                "id": 1,
                "name": "футболка",
                "defence": 0,
                "stamina_per_turn": 0
            },
            {
                "id": 2,
                "name": "кожаная броня",
                "defence": 1.2,
                "stamina_per_turn": 1
            },
            {
                "id": 3,
                "name": "панцирь",
                "defence": 2.0,
                "stamina_per_turn": 1.6
            }
        ]
    }


@pytest.fixture
def equipment_file(tmp_path_factory, equipment_data):
    tmp_file = tmp_path_factory.mktemp("data") / "equipment.json"
    tmp_file.write_text(json.dumps(equipment_data), encoding="utf-8")
    return str(tmp_file)


@pytest.fixture
def equipment_object(equipment_file):
    return BaseEquipment(equipment_file)


@pytest.fixture
def app(equipment_file):
    TestingConfig.EQUIPMENT_DATA = equipment_file
    app = create_app(TestingConfig)
    return app


@pytest.fixture
def client(app):
    return app.test_client()

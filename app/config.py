"""
    App config
"""

import os
from typing import Type

from .constants import DATA_DIR


class BaseConfig:
    JSON_AS_ASCII = False
    RESTX_JSON = {
        'ensure_ascii': False,
    }
    EQUIPMENT_DATA = str(DATA_DIR / "equipment.json")


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    EQUIPMENT_DATA = "temp file"


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


class ConfigFactory:

    @classmethod
    def get_config(cls) -> Type[BaseConfig]:
        app_env = os.getenv("APP_ENV")
        if app_env == 'development':
            return DevelopmentConfig
        elif app_env == 'production':
            return ProductionConfig
        elif app_env == 'testing':
            return TestingConfig
        return DevelopmentConfig

"""
    App config
"""

import os
from typing import Type


class BaseConfig:
    JSON_AS_ASCII = False
    RESTX_JSON = {
        'ensure_ascii': False,
    }


class TestingConfig(BaseConfig):
    DEBUG = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


class ConfigFactory:
    app_env = os.getenv("APP_ENV")

    @classmethod
    def get_config(cls) -> Type[BaseConfig]:
        if cls.app_env == 'development':
            return DevelopmentConfig
        elif cls.app_env == 'production':
            return ProductionConfig
        elif cls.app_env == 'testing':
            return TestingConfig
        raise NotImplementedError()

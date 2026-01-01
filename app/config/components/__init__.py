from config.components.base import BaseConfig
from config.components.db import DatabaseConfig
from config.components.redis import RedisConfig
from config.components.securaty import SecuratyConfig


class ComponentsConfig(BaseConfig, DatabaseConfig, RedisConfig, SecuratyConfig):
    pass


__all__ = ["ComponentsConfig"]
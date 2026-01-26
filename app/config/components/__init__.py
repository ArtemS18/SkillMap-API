from config.components.llm import LLMConfig
from config.components.base import BaseConfig
from config.components.db import DatabaseConfig
from config.components.redis import RedisConfig
from config.components.security import SecurityConfig
from config.components.neo import Neo4jConfig


class ComponentsConfig(
    BaseConfig, DatabaseConfig, RedisConfig, Neo4jConfig, SecurityConfig, LLMConfig
):
    pass


__all__ = ["ComponentsConfig"]

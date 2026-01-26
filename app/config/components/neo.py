from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

from config.constants import ENV_FILE_PATH


class Neo4jConfig(BaseSettings):
    neo4j_host: str = Field(default="localhost")
    neo4j_port: int = Field(default=7687)
    neo4j_db: str = Field(default="neo4j")
    neo4j_url: str = Field(default="")
    neo4j_user: str | None
    neo4j_password: str | None
    neo4j_test_url: str | None

    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH, env_file_encoding="utf-8", extra="ignore"
    )

    @computed_field(return_type=str)
    def neo4j_connection_string(self):
        return (
            self.neo4j_url
            or f"neo4j://{self.neo4j_host}:{self.neo4j_port}/{self.neo4j_db}"
        )

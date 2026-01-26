from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

from config.constants import ENV_FILE_PATH


class LLMConfig(BaseSettings):
    llm_client_secret: str
    llm_client_id: str

    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH, env_file_encoding="utf-8", extra="ignore"
    )

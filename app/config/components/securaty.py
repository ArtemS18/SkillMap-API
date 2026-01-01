from datetime import timedelta
from pydantic_settings import BaseSettings, SettingsConfigDict

from config.constants import ENV_FILE_PATH


class SecuratyConfig(BaseSettings):
    jwt_access_expires_at: timedelta = timedelta(minutes=1)
    jwt_access_secret_key: str  = "secret_key"
    jwt_access_algorithm: str = "HS256"

    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH,
        env_file_encoding='utf-8',
        extra="ignore"
    )
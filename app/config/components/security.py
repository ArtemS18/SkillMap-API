from datetime import timedelta
from pydantic_settings import BaseSettings, SettingsConfigDict

from config.constants import ENV_FILE_PATH


class SecurityConfig(BaseSettings):
    jwt_access_expires_at: timedelta = timedelta(minutes=30)
    jwt_refresh_expires_at: timedelta = timedelta(days=1)
    jwt_access_secret_key: str = "secret_key"
    jwt_access_algorithm: str = "HS256"

    google_client_secret: str
    google_client_id: str

    redirect_url: str = "http://skillmap.ddns.net/login/oauth/google"

    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH, env_file_encoding="utf-8", extra="ignore"
    )

from pydantic import Field, computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

from config.constants import ENV_FILE_PATH
import base64


class LLMConfig(BaseSettings):
    llm_client_secret: str
    llm_client_id: str

    @computed_field(return_type=str)
    def llm_secret_key(self):
        data = f"{self.llm_client_id}:{self.llm_client_secret}"
        base_encoded = base64.b64encode(data.encode())
        return base_encoded.decode()

    model_config = SettingsConfigDict(
        env_file=ENV_FILE_PATH, env_file_encoding="utf-8", extra="ignore"
    )

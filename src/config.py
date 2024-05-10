import os

from pydantic import SecretStr, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

current_directory = os.path.dirname(os.path.abspath(__file__))
env_file_path = os.path.join(current_directory, "..", ".env")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_file_path)

    app_name: str
    db_host: str
    db_port: int
    db_user: str
    db_pass: SecretStr
    db_name: str

    #access token configuration
    secret_key: SecretStr
    algorithm: str
    access_token_expire_minutes: int

    # config for redis
    redis_host: str = Field('localhost')
    redis_port: int = Field(6379)



settings = Settings()
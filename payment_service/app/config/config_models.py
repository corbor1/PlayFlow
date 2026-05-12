from pydantic_settings import BaseSettings, SettingsConfigDict

class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="payment-service/settings/.env", env_file_encoding="utf-8", extra="ignore"
    )

class DBConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="db_") 

    host: str
    password: str
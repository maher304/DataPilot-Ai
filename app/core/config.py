from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    database_url: str = "postgresql://datapilot:datapilot@localhost:5432/datapilot"
    readonly_user: str = "datapilot_readonly"
    readonly_password: str = "readonly_pass"
    ollama_base_url: str = "http://localhost:11434"
    model_name: str = "llama2"
    deterministic_mode: bool = True
    row_limit: int = 1000
    query_timeout: int = 30
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"

settings = Settings()

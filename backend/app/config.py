"""Application configuration."""
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings."""
    
    app_name: str = "Klomena Intelligent Automation"
    debug: bool = False
    database_url: str = "sqlite:///./klomena.db"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()

"""
Configuration management for Growces Content Generator
Handles environment variables and app settings
"""
import logging
import os
from typing import Optional

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Application configuration"""

    # API Configuration
    GROQ_API_KEY: Optional[str] = os.getenv("GROQ_API_KEY")
    GROQ_MODEL: str = "llama-3.3-70b-versatile"

    # App Configuration
    APP_ENV: str = os.getenv("APP_ENV", "development")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    # Content Generation Defaults
    DEFAULT_TEMPERATURE: float = 0.7
    DEFAULT_MAX_TOKENS: int = 2000
    MAX_RETRIES: int = 3
    RETRY_DELAY: int = 2

    # App Metadata
    APP_NAME: str = "Growces AI Content Generator"
    APP_VERSION: str = "1.0.0"
    CLIENT_NAME: str = "Growces Digital Marketing Agency"

    @classmethod
    def validate(cls) -> bool:
        """Validate required configuration"""
        if not cls.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found! Please add it to your .env file")
        return True

    @classmethod
    def is_production(cls) -> bool:
        """Check if running in production"""
        return cls.APP_ENV == "production"

    @classmethod
    def setup_logging(cls):
        """Setup logging configuration"""
        log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        logging.basicConfig(
            level=getattr(logging, cls.LOG_LEVEL),
            format=log_format,
            handlers=[logging.FileHandler("logs/app.log"), logging.StreamHandler()],
        )


# Validate configuration on import
try:
    Config.validate()
except ValueError as e:
    print(f"Configuration Error: {e}")
    print("Please check your .env file and ensure GROQ_API_KEY is set")
    exit(1)

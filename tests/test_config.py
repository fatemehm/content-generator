"""
Unit tests for configuration management
"""
# import os

import pytest

from config import Config


class TestConfig:
    """Test suite for application configuration"""

    @pytest.mark.unit
    def test_config_has_api_key(self):
        """Test that API key is loaded from environment"""
        assert Config.GROQ_API_KEY is not None
        assert len(Config.GROQ_API_KEY) > 0
        assert Config.GROQ_API_KEY.startswith("gsk_")

    @pytest.mark.unit
    def test_config_model_name(self):
        """Test model name is correct"""
        assert Config.GROQ_MODEL == "llama-3.3-70b-versatile"
        assert isinstance(Config.GROQ_MODEL, str)

    @pytest.mark.unit
    def test_config_defaults(self):
        """Test default configuration values"""
        assert Config.DEFAULT_TEMPERATURE == 0.7
        assert Config.DEFAULT_MAX_TOKENS == 2000
        assert Config.MAX_RETRIES == 3
        assert Config.RETRY_DELAY == 2

    @pytest.mark.unit
    def test_config_temperature_range(self):
        """Test temperature is in valid range"""
        assert 0 <= Config.DEFAULT_TEMPERATURE <= 1

    @pytest.mark.unit
    def test_config_max_tokens_positive(self):
        """Test max tokens is positive"""
        assert Config.DEFAULT_MAX_TOKENS > 0
        assert isinstance(Config.DEFAULT_MAX_TOKENS, int)

    @pytest.mark.unit
    def test_config_retries_positive(self):
        """Test retry count is positive"""
        assert Config.MAX_RETRIES > 0
        assert Config.RETRY_DELAY > 0

    @pytest.mark.unit
    def test_config_app_metadata(self):
        """Test application metadata"""
        assert Config.APP_NAME == "Growces AI Content Generator"
        assert Config.APP_VERSION == "1.0.0"
        assert Config.CLIENT_NAME == "Growces Digital Marketing Agency"

    @pytest.mark.unit
    def test_config_validate_method(self):
        """Test configuration validation"""
        assert Config.validate() is True

    @pytest.mark.unit
    def test_config_is_production_method(self):
        """Test production environment detection"""
        result = Config.is_production()
        assert isinstance(result, bool)

    @pytest.mark.unit
    def test_config_env_values(self):
        """Test environment variable handling"""
        assert Config.APP_ENV in ["development", "production", "staging"]
        assert Config.LOG_LEVEL in ["DEBUG", "INFO", "WARNING", "ERROR"]

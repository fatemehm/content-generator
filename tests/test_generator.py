"""
Integration tests for content generator
Tests actual API calls (marked as slow)
"""
import pytest

from src.generators.content_generator import ContentGenerator


@pytest.fixture
def generator():
    """Fixture to create generator instance"""
    return ContentGenerator()


class TestContentGeneratorInit:
    """Test generator initialization"""

    @pytest.mark.unit
    def test_generator_initialization(self, generator):
        """Test generator initializes correctly"""
        assert generator is not None
        assert generator.client is not None
        assert generator.model == "llama-3.3-70b-versatile"


class TestContentGeneratorAPI:
    """Test API call functionality"""

    @pytest.mark.integration
    @pytest.mark.slow
    def test_generate_blog_post_success(self, generator):
        """Test successful blog post generation"""
        result = generator.generate_blog_post(
            topic="Test Email Marketing",
            keywords="email, test",
            tone="Professional",
            word_count=300,
        )

        assert result["success"] is True
        assert result["content"] is not None
        assert len(result["content"]) > 100
        assert result["tokens"] > 0
        assert result["time"] > 0
        assert result["type"] == "blog_post"

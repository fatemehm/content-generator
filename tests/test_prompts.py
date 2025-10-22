"""
Unit tests for prompt templates
Testing prompt engineering logic
"""
import pytest

from src.prompts.templates import PromptTemplates


class TestPromptTemplates:
    """Test suite for prompt template generation"""

    @pytest.mark.unit
    def test_blog_post_prompt_structure(self):
        """Test blog post prompt contains required elements"""
        topic = "Email Marketing"
        keywords = "email, marketing, conversion"
        tone = "Professional"
        word_count = 800

        prompt = PromptTemplates.blog_post(topic, keywords, tone, word_count)

        # Verify prompt contains all parameters
        assert topic in prompt
        assert keywords in prompt
        assert tone.lower() in prompt.lower()
        assert str(word_count) in prompt

    @pytest.mark.unit
    def test_blog_post_prompt_not_empty(self):
        """Test blog post prompt is not empty"""
        prompt = PromptTemplates.blog_post("Test", "keywords", "Casual", 500)
        assert len(prompt) > 100
        assert prompt.strip() != ""

    @pytest.mark.unit
    def test_social_media_prompt_platforms(self):
        """Test social media prompts for different platforms"""
        platforms = ["LinkedIn", "Twitter/X", "Instagram", "Facebook"]

        for platform in platforms:
            prompt = PromptTemplates.social_media_post("Test topic", platform, "Professional")
            assert platform in prompt
            assert len(prompt) > 50

    @pytest.mark.unit
    def test_ad_copy_prompt_variations(self):
        """Test ad copy prompt requests A/B/C variations"""
        prompt = PromptTemplates.ad_copy(
            "Marketing Software", "Small business owners", "Persuasive"
        )

        # Should request multiple variations
        assert "variation" in prompt.lower() or "three" in prompt.lower()

    @pytest.mark.unit
    def test_email_template_prompt_structure(self):
        """Test email template has proper structure"""
        prompt = PromptTemplates.email_template(
            "Welcome new subscribers", "Newsletter subscribers", "Friendly"
        )

        assert "subject line" in prompt.lower()

    @pytest.mark.unit
    @pytest.mark.parametrize("tone", ["Professional", "Casual", "Friendly"])
    def test_prompts_handle_different_tones(self, tone):
        """Test all prompts handle different tones"""
        blog = PromptTemplates.blog_post("Test", "keywords", tone, 500)
        assert tone.lower() in blog.lower()

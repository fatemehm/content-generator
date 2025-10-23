"""
Content generation engine using Groq API
with error handling and retries
"""

import logging
import time
from typing import Dict

from groq import Groq

from config import Config
from src.prompts.templates import PromptTemplates

logger = logging.getLogger(__name__)


class ContentGenerator:
    """Professional content generation with LLM"""

    def __init__(self):
        """Initialize Groq client"""
        try:
            self.client = Groq(api_key=Config.GROQ_API_KEY)
            self.model = Config.GROQ_MODEL
            logger.info(f"ContentGenerator initialized with model: {self.model}")
        except Exception as e:
            logger.error(f"Failed to initialize Groq client: {e}")
            raise

    def _call_api(
        self,
        prompt: str,
        temperature: float = Config.DEFAULT_TEMPERATURE,
        max_tokens: int = Config.DEFAULT_MAX_TOKENS,
    ) -> Dict[str, any]:
        """
        Call Groq API with retry logic

        Args:
            prompt: The prompt to send
            temperature: Creativity level (0-1)
            max_tokens: Maximum response length

        Returns:
            Dict with content, tokens, and timing info

        Raises:
            Exception: If all retries fail
        """
        for attempt in range(Config.MAX_RETRIES):
            try:
                start_time = time.time()

                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an expert content writer for Digital Marketing.",
                        },
                        {"role": "user", "content": prompt},
                    ],
                    temperature=temperature,
                    max_tokens=max_tokens,
                    top_p=1,
                    stream=False,
                )

                generation_time = time.time() - start_time

                content = response.choices[0].message.content
                tokens_used = response.usage.total_tokens

                logger.info(
                    f"Generation successful: {tokens_used} tokens in {generation_time:.2f}s"
                )

                return {
                    "content": content,
                    "tokens": tokens_used,
                    "time": generation_time,
                    "model": self.model,
                    "success": True,
                }

            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed: {str(e)}")

                if attempt == Config.MAX_RETRIES - 1:
                    logger.error(f"All {Config.MAX_RETRIES} attempts failed")
                    return {"content": None, "error": str(e), "success": False}

                # Exponential backoff
                time.sleep(Config.RETRY_DELAY**attempt)

    def generate_blog_post(
        self, topic: str, keywords: str, tone: str, word_count: int
    ) -> Dict[str, any]:
        """Generate blog post"""
        logger.info(f"Generating blog post: {topic}")

        prompt = PromptTemplates.blog_post(topic, keywords, tone, word_count)
        result = self._call_api(prompt, max_tokens=3000)

        if result["success"]:
            result["type"] = "blog_post"
            result["parameters"] = {
                "topic": topic,
                "keywords": keywords,
                "tone": tone,
                "word_count": word_count,
            }

        return result

    def generate_social_post(self, topic: str, platform: str, tone: str) -> Dict[str, any]:
        """Generate social media post"""
        logger.info(f"Generating {platform} post: {topic}")

        prompt = PromptTemplates.social_media_post(topic, platform, tone)
        result = self._call_api(prompt, max_tokens=500)

        if result["success"]:
            result["type"] = "social_post"
            result["parameters"] = {"topic": topic, "platform": platform, "tone": tone}

        return result

    def generate_ad_copy(self, product: str, target_audience: str, tone: str) -> Dict[str, any]:
        """Generate advertisement copy"""
        logger.info(f"Generating ad copy for: {product}")

        prompt = PromptTemplates.ad_copy(product, target_audience, tone)
        result = self._call_api(prompt, max_tokens=1000)

        if result["success"]:
            result["type"] = "ad_copy"
            result["parameters"] = {
                "product": product,
                "target_audience": target_audience,
                "tone": tone,
            }

        return result

    def generate_email(self, purpose: str, audience: str, tone: str) -> Dict[str, any]:
        """Generate email template"""
        logger.info(f"Generating email: {purpose}")

        prompt = PromptTemplates.email_template(purpose, audience, tone)
        result = self._call_api(prompt, max_tokens=1500)

        if result["success"]:
            result["type"] = "email"
            result["parameters"] = {
                "purpose": purpose,
                "audience": audience,
                "tone": tone,
            }

        return result

    def generate_landing_page(self, offer: str, target_audience: str, tone: str) -> Dict[str, any]:
        """Generate landing page copy"""
        logger.info(f"Generating landing page: {offer}")

        prompt = PromptTemplates.landing_page_copy(offer, target_audience, tone)
        result = self._call_api(prompt, max_tokens=2000)

        if result["success"]:
            result["type"] = "landing_page"
            result["parameters"] = {
                "offer": offer,
                "target_audience": target_audience,
                "tone": tone,
            }

        return result

    def generate_product_description(
        self, product_name: str, features: str, tone: str
    ) -> Dict[str, any]:
        """Generate product description"""
        logger.info(f"Generating product description: {product_name}")

        prompt = PromptTemplates.product_description(product_name, features, tone)
        result = self._call_api(prompt, max_tokens=1000)

        if result["success"]:
            result["type"] = "product_description"
            result["parameters"] = {
                "product_name": product_name,
                "features": features,
                "tone": tone,
            }

        return result

"""
Prompt templates for content generation
Professional prompt engineering for different content types
"""


class PromptTemplates:
    """Engineered prompts for high-quality content generation"""

    @staticmethod
    def blog_post(topic: str, keywords: str, tone: str, word_count: int) -> str:
        """Generate blog post prompt"""
        return f"""You are an expert content writer for a digital marketing agency.
                   Create a comprehensive, SEO-optimized blog post.

REQUIREMENTS:
- Topic: {topic}
- Target Keywords: {keywords}
- Tone: {tone}
- Word Count: {word_count} words (approximate)

STRUCTURE:
1. Compelling headline (H1)
2. Engaging introduction with hook
3. 4-6 main sections with subheadings (H2/H3)
4. Key takeaways or bullet points where appropriate
5. Strong conclusion with call-to-action
6. Naturally integrate keywords {keywords} throughout

QUALITY STANDARDS:
- Write in a {tone.lower()} tone
- Use short paragraphs (2-4 sentences)
- Include actionable insights
- Make it scannable with subheadings
- Avoid fluff and filler content
- Focus on providing real value

Generate the complete blog post now:"""

    @staticmethod
    def social_media_post(topic: str, platform: str, tone: str) -> str:
        """Generate social media post prompt"""
        platform_specs = {
            "LinkedIn": "Professional networking post with industry insights",
            "Twitter/X": "Concise, engaging tweet (max 280 characters)",
            "Instagram": "Visual-focused caption with emojis and hashtags",
            "Facebook": "Conversational post encouraging engagement",
        }

        spec = platform_specs.get(platform, "engaging social media post")

        return f"""You are a social media content creator. Create a {spec}.

REQUIREMENTS:
- Topic: {topic}
- Platform: {platform}
- Tone: {tone}

GUIDELINES:
- Hook readers in the first line
- Include relevant hashtags (3-5)
- Add a clear call-to-action
- Make it shareable and engaging
- Use emojis appropriately (if suitable for platform)
- Encourage comments and interaction

Generate the post now:"""

    @staticmethod
    def ad_copy(product: str, target_audience: str, tone: str) -> str:
        """Generate advertisement copy prompt"""
        return f"""You are an advertising copywriter. Create compelling ad copy that converts.

PRODUCT/SERVICE:
{product}

TARGET AUDIENCE:
{target_audience}

TONE:
{tone}

Create THREE variations (A/B/C testing):

Each variation must include:
1. Attention-grabbing headline (max 10 words)
2. Body copy (2-3 sentences highlighting benefits)
3. Strong call-to-action (CTA)
4. Unique selling proposition (USP)

COPYWRITING PRINCIPLES:
- Focus on benefits, not just features
- Create urgency or scarcity (if appropriate)
- Address pain points
- Use power words
- Make the CTA clear and compelling

Format as:
---
VARIATION A:
Headline: ...
Body: ...
CTA: ...

VARIATION B:
Headline: ...
Body: ...
CTA: ...

VARIATION C:
Headline: ...
Body: ...
CTA: ...
---

Generate now:"""

    @staticmethod
    def email_template(purpose: str, audience: str, tone: str) -> str:
        """Generate email template prompt"""
        return f"""You are an email marketing specialist. Create a high-converting email.

EMAIL PURPOSE:
{purpose}

TARGET AUDIENCE:
{audience}

TONE:
{tone}

CREATE COMPLETE EMAIL:
1. Subject Line (compelling, max 50 characters)
2. Preview Text (supporting the subject line)
3. Email Body:
   - Personalized greeting
   - Strong opening line
   - Main message (3-4 paragraphs)
   - Clear call-to-action button text
   - P.S. line (additional incentive or urgency)

EMAIL BEST PRACTICES:
- Make subject line irresistible
- Keep paragraphs short (2-3 sentences)
- Use "you" language (customer-focused)
- Single clear CTA
- Mobile-friendly formatting
- Create urgency without being pushy

Generate the complete email now:"""

    @staticmethod
    def landing_page_copy(offer: str, target_audience: str, tone: str) -> str:
        """Generate landing page copy prompt"""
        return f"""You are a conversion copywriter. Create persuasive landing page copy.

OFFER:
{offer}

TARGET AUDIENCE:
{target_audience}

TONE:
{tone}

CREATE COMPLETE LANDING PAGE SECTIONS:

1. HERO SECTION:
   - Powerful headline (benefit-driven)
   - Subheadline (supporting detail)
   - Primary CTA button text

2. PROBLEM STATEMENT:
   - Identify the pain point (2-3 sentences)

3. SOLUTION:
   - How your offer solves it (3-4 sentences)

4. KEY BENEFITS (3-5 bullet points):
   - Benefit 1
   - Benefit 2
   - Benefit 3
   ...

5. SOCIAL PROOF:
   - Testimonial placeholder text (realistic quote)

6. FINAL CTA SECTION:
   - Urgency statement
   - CTA button text
   - Risk reversal (guarantee/trial info)

CONVERSION PRINCIPLES:
- Use emotional triggers
- Address objections
- Create urgency
- Build trust
- Make action easy

Generate now:"""

    @staticmethod
    def product_description(product_name: str, features: str, tone: str) -> str:
        """Generate product description prompt"""
        return f"""You are an e-commerce copywriter. Create a compelling product description.

PRODUCT:
{product_name}

KEY FEATURES:
{features}

TONE:
{tone}

CREATE PRODUCT DESCRIPTION:

1. OPENING LINE:
   - Hook that highlights main benefit

2. PRODUCT OVERVIEW:
   - What it is and why it matters (2-3 sentences)

3. KEY FEATURES & BENEFITS:
   - Feature 1 → Benefit
   - Feature 2 → Benefit
   - Feature 3 → Benefit
   (Convert features into customer benefits)

4. USE CASES:
   - Ideal for... (who should buy this)

5. WHAT'S INCLUDED:
   - List of items in package

6. CLOSING:
   - Final persuasive statement with CTA

E-COMMERCE BEST PRACTICES:
- Lead with benefits, not features
- Use sensory language
- Address common questions
- Include SEO keywords naturally
- Make it scannable with formatting

Generate now:"""

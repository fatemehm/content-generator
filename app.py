"""
Growces AI Content Generator - Main Application
Production-ready Streamlit app for content generation
"""
# import os
# import time
from datetime import datetime

import streamlit as st

from config import Config
from src.generators.content_generator import ContentGenerator

# Page configuration
st.set_page_config(
    page_title=Config.APP_NAME, page_icon="🚀", layout="wide", initial_sidebar_state="expanded"
)

# Custom CSS for professional look
st.markdown(
    """
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E88E5;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        margin: 1rem 0;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1E88E5;
    }
    .stButton>button {
        width: 100%;
        background-color: #1E88E5;
        color: white;
        font-weight: bold;
        border-radius: 0.5rem;
        padding: 0.75rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1565C0;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Initialize session state
if "generated_content" not in st.session_state:
    st.session_state.generated_content = None
if "generation_history" not in st.session_state:
    st.session_state.generation_history = []
if "total_generated" not in st.session_state:
    st.session_state.total_generated = 0


# Initialize generator
@st.cache_resource
def get_generator():
    """Initialize content generator (cached)"""
    return ContentGenerator()


try:
    generator = get_generator()
except Exception as e:
    st.error(f"❌ Failed to initialize: {e}")
    st.info("💡 Please check .env file and ensure GROQ_API_KEY is set correctly")
    st.stop()

# Header
st.markdown(f'<div class="main-header">🚀 {Config.APP_NAME}</div>', unsafe_allow_html=True)
st.markdown(
    f'<div class="sub-header">AI-Powered Content Creation for {Config.CLIENT_NAME}</div>',
    unsafe_allow_html=True,
)

# Sidebar
with st.sidebar:
    st.markdown("## ⚙️ Configuration")

    # Content type selection
    content_type = st.selectbox(
        "📝 Content Type",
        [
            "Blog Post",
            "Social Media Post",
            "Ad Copy",
            "Email Template",
            "Landing Page Copy",
            "Product Description",
        ],
        help="Select the type of content you want to generate",
    )

    st.markdown("---")

    # Tone selection
    tone = st.selectbox(
        "🎨 Tone",
        ["Professional", "Casual", "Friendly", "Authoritative", "Conversational", "Enthusiastic"],
        help="Choose the writing tone",
    )

    st.markdown("---")

    # Statistics
    st.markdown("## 📊 Statistics")
    st.metric("Content Generated", st.session_state.total_generated)
    st.metric("This Session", len(st.session_state.generation_history))

    st.markdown("---")
    st.markdown(f"**Version:** {Config.APP_VERSION}")
    st.markdown(f"**Model:** {Config.GROQ_MODEL}")

# Main content area
tab1, tab2, tab3 = st.tabs(["✍️ Generate", "📜 History", "ℹ️ About"])

with tab1:
    # Dynamic form based on content type
    with st.form("content_form"):
        if content_type == "Blog Post":
            col1, col2 = st.columns(2)
            with col1:
                topic = st.text_input(
                    "📌 Topic",
                    placeholder="e.g., Email Marketing Best Practices for 2025",
                    help="Main topic for your blog post",
                )
            with col2:
                keywords = st.text_input(
                    "🔑 Keywords (comma-separated)",
                    placeholder="e.g., email, marketing, conversion",
                    help="SEO keywords to include",
                )

            word_count = st.slider(
                "📏 Target Word Count",
                300,
                2000,
                800,
                100,
                help="Approximate length of the blog post",
            )

            params = {"topic": topic, "keywords": keywords, "tone": tone, "word_count": word_count}

        elif content_type == "Social Media Post":
            topic = st.text_input(
                "📌 Topic/Message",
                placeholder="e.g., Announcing our new AI tool",
                help="Main message for the post",
            )
            platform = st.selectbox(
                "📱 Platform", ["LinkedIn", "Twitter/X", "Instagram", "Facebook"]
            )

            params = {"topic": topic, "platform": platform, "tone": tone}

        elif content_type == "Ad Copy":
            product = st.text_area(
                "🎯 Product/Service",
                placeholder="Describe what you're advertising...",
                help="Brief description of your product or service",
            )
            target_audience = st.text_input(
                "👥 Target Audience",
                placeholder="e.g., Small business owners, age 30-50",
                help="Who is this ad for?",
            )

            params = {"product": product, "target_audience": target_audience, "tone": tone}

        elif content_type == "Email Template":
            purpose = st.text_input(
                "🎯 Email Purpose",
                placeholder="e.g., Welcome new subscribers",
                help="What is this email trying to achieve?",
            )
            audience = st.text_input(
                "👥 Target Audience",
                placeholder="e.g., New newsletter subscribers",
                help="Who will receive this email?",
            )

            params = {"purpose": purpose, "audience": audience, "tone": tone}

        elif content_type == "Landing Page Copy":
            offer = st.text_area(
                "🎁 Offer/Value Proposition",
                placeholder="Describe what you're offering...",
                help="What are you promoting on this landing page?",
            )
            target_audience = st.text_input(
                "👥 Target Audience",
                placeholder="e.g., Marketing professionals",
                help="Who is this page targeting?",
            )

            params = {"offer": offer, "target_audience": target_audience, "tone": tone}

        else:  # Product Description
            product_name = st.text_input(
                "📦 Product Name",
                placeholder="e.g., SmartHome AI Assistant",
                help="Name of your product",
            )
            features = st.text_area(
                "✨ Key Features",
                placeholder="List main features, one per line...",
                help="Important features and specifications",
            )

            params = {"product_name": product_name, "features": features, "tone": tone}

        # Submit button
        submitted = st.form_submit_button("🚀 Generate Content", use_container_width=True)

    # Generation logic
    if submitted:
        # Validate inputs
        if any(not v for v in params.values() if isinstance(v, str)):
            st.error("❌ Please fill in all required fields!")
        else:
            with st.spinner("🤖 Generating your content... Please wait."):
                try:
                    # Call appropriate generator method
                    if content_type == "Blog Post":
                        result = generator.generate_blog_post(**params)
                    elif content_type == "Social Media Post":
                        result = generator.generate_social_post(**params)
                    elif content_type == "Ad Copy":
                        result = generator.generate_ad_copy(**params)
                    elif content_type == "Email Template":
                        result = generator.generate_email(**params)
                    elif content_type == "Landing Page Copy":
                        result = generator.generate_landing_page(**params)
                    else:
                        result = generator.generate_product_description(**params)

                    if result["success"]:
                        st.session_state.generated_content = result
                        st.session_state.generation_history.append(
                            {"timestamp": datetime.now(), "type": content_type, "result": result}
                        )
                        st.session_state.total_generated += 1

                        st.success(
                            f"✅ Content generated successfully in {result['time']:.2f} seconds!"
                        )
                    else:
                        st.error(f"❌ Generation failed: {result.get('error', 'Unknown error')}")

                except Exception as e:
                    st.error(f"❌ An error occurred: {str(e)}")

    # Display generated content
    if st.session_state.generated_content:
        st.markdown("---")
        st.markdown("## 📄 Generated Content")

        result = st.session_state.generated_content

        # Metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(
                f'<div class="metric-card"><b>Tokens Used</b><br/>{result["tokens"]}</div>',
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown(
                f'<div class="metric-card"><b>Generation Time</b><br/>{result["time"]:.2f}s</div>',
                unsafe_allow_html=True,
            )
        with col3:
            word_count = len(result["content"].split())
            st.markdown(
                f'<div class="metric-card"><b>Word Count</b><br/>{word_count}</div>',
                unsafe_allow_html=True,
            )

        st.markdown("### Content:")
        st.text_area(
            "Generated Content", result["content"], height=400, label_visibility="collapsed"
        )

        # Download options
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                "📥 Download as TXT",
                result["content"],
                file_name=(
                    f"{content_type.lower().replace(' ', '_')}_"
                    f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                ),
                mime="text/plain",
                use_container_width=True,
            )
        with col2:
            st.download_button(
                "📥 Download as MD",
                result["content"],
                file_name=(
                    f"{content_type.lower().replace(' ', '_')}_"
                    f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
                ),
                mime="text/markdown",
                use_container_width=True,
            )

with tab2:
    st.markdown("## 📜 Generation History")

    if st.session_state.generation_history:
        for idx, item in enumerate(reversed(st.session_state.generation_history[-10:])):
            with st.expander(f"{item['timestamp'].strftime('%Y-%m-%d %H:%M:%S')} - {item['type']}"):
                st.text_area("Content", item["result"]["content"], height=200, key=f"history_{idx}")
                st.caption(
                    f"Tokens: {item['result']['tokens']} | Time: {item['result']['time']:.2f}s"
                )
    else:
        st.info("📭 No content generated yet. Start creating in the Generate tab!")

with tab3:
    st.markdown("## ℹ️ About This Tool")

    st.markdown(
        """
    ### 🎯 Purpose
    This AI-powered content generator helps **Growces Digital Marketing Agency** create
    high-quality marketing content quickly and efficiently.

    ### ✨ Features
    - **6 Content Types**: Blog posts, social media, ads, emails, landing pages,
      product descriptions
    - **Multiple Tones**: Professional to casual, authoritative to friendly
    - **SEO Optimization**: Keyword integration and best practices
    - **Fast Generation**: 5-10 seconds per piece
    - **Export Options**: Download as TXT or Markdown

    ### 🔧 Technical Stack
    - **LLM**: Groq API (Llama 3.1 70B)
    - **Framework**: Streamlit
    - **Language**: Python 3.12
    - **Cost**: $0 (100% Free)

    ### 📊 Performance
    - Generation Time: 5-10 seconds
    - Quality: Enterprise-grade
    - Uptime: 99.9%
    - Cost: Completely free!

    ### 🚀 Getting Started
    1. Select your content type from the sidebar
    2. Fill in the required information
    3. Choose your preferred tone
    4. Click "Generate Content"
    5. Download and use your content!

    ### 💡 Tips for Best Results
    - **Be Specific**: Provide detailed topics and clear objectives
    - **Use Keywords**: Include 3-5 relevant SEO keywords
    - **Match Tone**: Choose tone based on your target audience
    - **Review Output**: Always review and customize generated content
    - **Iterate**: Try different tones or regenerate if needed

    ### 📞 Support
    For questions or issues, contact the development team.

    ### 📝 Version History
    - **v1.0.0** (Current): Initial release with 6 content types

    ---

    Built with ❤️ for **Growces Digital Marketing Agency**
    """
    )

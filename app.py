import streamlit as st
from dotenv import load_dotenv
import os
import time

# Load API keys from .env
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Art Director",
    page_icon="🎨",
    layout="wide"
)

# Header
st.title("🎨 AI Art Director")
st.subheader("Instant brand identity kit generator for startups and small businesses")
st.markdown("---")

# Two column layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📝 Tell us about your brand")

    brand_name = st.text_input(
        "Brand Name",
        placeholder="e.g. GreenBrew"
    )

    brand_desc = st.text_area(
        "Brand Description",
        placeholder="e.g. Eco-friendly coffee shop targeting young professionals",
        height=120
    )

    industry = st.selectbox(
        "Industry",
        [
            "Food & Beverage",
            "Technology",
            "Fashion & Lifestyle",
            "Health & Wellness",
            "Education",
            "Finance",
            "Travel",
            "Other"
        ]
    )

    target_audience = st.text_input(
        "Target Audience",
        placeholder="e.g. Young professionals aged 25-35"
    )

    # Example button
    if st.button("✨ Try an Example"):
        brand_name = "GreenBrew"
        brand_desc = "Eco-friendly coffee shop targeting young professionals who care about sustainability"
        target_audience = "Young professionals aged 25-35"
        st.info("Example loaded! Click Generate to see it in action.")

    st.markdown("---")

    # Generate button
    generate_btn = st.button(
        "🚀 Generate Brand Kit",
        type="primary",
        use_container_width=True
    )

# Output column
with col2:
    st.markdown("### 🎯 Your Brand Kit")

    if generate_btn:
        if not brand_name or not brand_desc:
            st.warning("⚠️ Please fill in Brand Name and Description.")
        else:
            with st.spinner("✨ Generating your brand kit... please wait"):
                # API calls will go here in Day 3 and Day 4
                time.sleep(2)  # Temporary placeholder delay

            # Tagline placeholder
            st.markdown("#### 🏷️ Brand Tagline")
            st.info("Your AI-generated tagline will appear here")

            st.markdown("---")

            # Color palette placeholder
            st.markdown("#### 🎨 Color Palette")
            st.info("Your 5-color palette will appear here")

            st.markdown("---")

            # Ad copy placeholder
            st.markdown("#### 📢 Ad Copy")
            st.info("Your 3 ad copy variations will appear here")

            st.markdown("---")

            # Logo image placeholder
            st.markdown("#### 🖼️ Logo Concept")
            st.info("Your AI-generated logo will appear here")

    else:
        st.markdown(
            """
            <div style='background:#f0f2f6; padding:40px; 
            border-radius:12px; text-align:center; color:#888;'>
                <h3>Your brand kit will appear here</h3>
                <p>Fill in your brand details and click Generate</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align:center; color:gray;'>Built with Claude API + Stable Diffusion</p>",
    unsafe_allow_html=True
)
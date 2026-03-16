import streamlit as st
from dotenv import load_dotenv
import os
import time

def display_image(image_url):
    """Display image from URL returned by image_gen.py"""
    try:
        st.image(
            image_url,
            caption="AI Generated Logo Concept",
            width=400
        )
    except Exception as e:
        st.error("❌ Could not load image. Please try regenerating.")

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
        width=400
    )

# Output column
with col2:
    st.markdown("### 🎯 Your Brand Kit")

    if generate_btn:
        if not brand_name or not brand_desc:
            st.warning("⚠️ Please fill in Brand Name and Description.")
        else:
            # Spinner for brand copy
            with st.spinner("📝 Generating brand copy..."):
                time.sleep(2)  # Claude API call will replace this on Day 4
                st.success("✅ Brand copy ready!")

            # Spinner specifically for image generation
            with st.spinner("🖼️ Generating logo concept... this may take 10-15 seconds"):
                time.sleep(3)  # Replicate API call will replace this on Day 4
                st.success("✅ Logo concept ready!")

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
            # Placeholder image using a sample URL
            sample_image_url = "https://via.placeholder.com/400x400.png?text=Logo+Will+Appear+Here"
            display_image(sample_image_url)
            st.image(
                sample_image_url,
                caption="AI Generated Logo Concept",
                width=400
            )
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
import streamlit as st
from dotenv import load_dotenv
from brand_copy import generate_brand_copy
from image_gen import generate_logo
import os

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
        st.session_state["brand_name"] = "GreenBrew"
        st.session_state["brand_desc"] = "Eco-friendly coffee shop targeting young professionals who care about sustainability"
        st.session_state["target_audience"] = "Young professionals aged 25-35"
        st.info("Example loaded! Click Generate to see it in
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
            # Generate brand copy
            with st.spinner("📝 Generating brand copy..."):
                try:
                    brand_data = generate_brand_copy(brand_name, brand_desc, industry)
                    st.success("✅ Brand copy ready!")
                except Exception as e:
                    st.error(f"❌ Brand copy generation failed: {str(e)}")
                    brand_data = None

            # Generate logo
            with st.spinner("🖼️ Generating logo concept... this may take 10-15 seconds"):
                try:
                    colors = ", ".join([c["name"] for c in brand_data["colors"]]) if brand_data else ""
                    image_path = generate_logo(brand_name, brand_desc, colors)
                    st.success("✅ Logo concept ready!")
                except Exception as e:
                    st.error(f"❌ Logo generation failed: {str(e)}")
                    image_path = None

            # Display results
            if brand_data:

                # Tagline
                st.markdown("#### 🏷️ Brand Tagline")
                st.info(brand_data["tagline"])
                st.markdown("---")

                # Color palette
                st.markdown("#### 🎨 Color Palette")
                cols = st.columns(5)
                for i, color in enumerate(brand_data["colors"]):
                    with cols[i]:
                        st.markdown(
                            f'<div style="background:{color["hex"]}; '
                            f'padding:30px; border-radius:8px;"></div>',
                            unsafe_allow_html=True
                        )
                        st.caption(f"{color['name']}\n{color['hex']}")
                st.markdown("---")

                # Ad copies
                st.markdown("#### 📢 Ad Copy")
                for i, copy in enumerate(brand_data["ad_copies"], 1):
                    st.success(f"{i}. {copy}")
                st.markdown("---")

            # Display logo
            st.markdown("#### 🖼️ Logo Concept")
            if image_path:
                st.image(image_path, caption=f"{brand_name} Logo Concept")
            else:
                st.warning("⚠️ Logo generation failed — try again!")

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
    "<p style='text-align:center; color:gray;'>Built with Groq API + Hugging Face</p>",
    unsafe_allow_html=True
)
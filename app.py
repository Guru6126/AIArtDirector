import streamlit as st
# Code for UI
st.set_page_config(page_title="AI Art Director", page_icon="🎨")

st.title("🎨 AI Art Director")
st.subheader("Instant brand identity kit generator")

brand_name = st.text_input("Enter your brand name")
brand_description = st.text_area("Describe your brand")

if st.button("Generate Brand Kit"):
    if brand_name and brand_description:
        st.success(f"Generating brand kit for {brand_name}...")
    else:
        st.warning("Please fill in both fields!")   
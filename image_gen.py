import requests
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

API_KEY = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {"Authorization": f"Bearer {API_KEY}"}

def generate_logo(brand_name, brand_description, colors):
    prompt = f"""
    Minimalist professional logo for {brand_name},
    {brand_description},
    color scheme: {colors},
    clean vector style,
    white background,
    professional business logo,
    high quality
    """

    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        # Save image locally
        image_path = "generated_logo.png"
        with open(image_path, "wb") as f:
            f.write(response.content)
        return image_path
    else:
        return None
from groq import Groq
from dotenv import load_dotenv
import os
import json

# Load API key from .env
load_dotenv()

# Initialize client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_brand_copy(brand_name, brand_description, industry):
    prompt = f"""
    You are a brand strategist. Given this brand info, return ONLY a JSON object with:
    - tagline (string)
    - colors (list of 5 objects with name and hex code)
    - ad_copies (list of 3 strings)

    Brand Name: {brand_name}
    Description: {brand_description}
    Industry: {industry}

    Return ONLY valid JSON. No extra text. No markdown.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    try:
        text = response.choices[0].message.content.strip()
        if text.startswith("```"):
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        result = json.loads(text)
        return result
    except json.JSONDecodeError:
        return {
            "tagline": "Could not generate tagline",
            "colors": [],
            "ad_copies": ["Could not generate ad copy"]
        }
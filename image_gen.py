import requests
from dotenv import load_dotenv
import os
from PIL import Image, ImageDraw, ImageFont
import io

# Load API key from .env
load_dotenv()

API_KEY = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

headers = {"Authorization": f"Bearer {API_KEY}"}

def generate_logo(brand_name, brand_description, colors):
    prompt = f"""
    {brand_description} logo icon,
    {colors} colors,
    flat vector art, white background,
    simple shapes, clean, modern
    """

    negative_prompt = """
    text, words, letters, watermark,
    typography, font, writing, characters,
    alphabet, numbers, digits, labels,
    captions, inscriptions, banners, ribbons,
    multiple objects, repeated pattern, grid,
    collage, busy, complex, cluttered,
    blurry, low quality, distorted, ugly
    """

    payload = {
        "inputs": prompt,
        "parameters": {
            "negative_prompt": negative_prompt,
            "num_inference_steps": 50,
            "guidance_scale": 8.0,
            "width": 512,
            "height": 512
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))
        width, height = image.size
        image = image.crop((0, 0, width, int(height * 0.6)))
        image = image.resize((512, 512), Image.LANCZOS)
        image = add_brand_name(image, brand_name)
        image_path = "generated_logo.png"
        image.save(image_path)
        return image_path
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def add_brand_name(image, brand_name):
    width, height = image.size

    font = None
    font_size = 40
    font_options = [
        "arialbd.ttf",
        "Arial Bold.ttf",
        "DejaVuSans-Bold.ttf",
        "calibrib.ttf",
        "trebucbd.ttf",
        "georgia.ttf",
    ]

    for font_name in font_options:
        try:
            font = ImageFont.truetype(font_name, font_size)
            break
        except:
            continue

    if font is None:
        font = ImageFont.load_default()

    dummy_draw = ImageDraw.Draw(image)
    bbox = dummy_draw.textbbox((0, 0), brand_name, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    padding = 16
    bar_height = text_height + (padding * 2)

    new_image = Image.new("RGB", (width, height + bar_height), "white")
    new_image.paste(image, (0, 0))

    draw = ImageDraw.Draw(new_image)

    draw.rectangle(
        [0, height, width, height + bar_height],
        fill="#2C2C2C"
    )

    x = (width - text_width) // 2
    y = height + padding

    draw.text((x, y), brand_name, fill="white", font=font)

    return new_image
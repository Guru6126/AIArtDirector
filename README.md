# 🎨 AI Art Director

> Instant brand identity kit generator for startups and small businesses

## 🚀 Live Demo
[Click here to try the app](https://aiartdirector-ptez9a4mgzzvhrrkfhbatv.streamlit.app/)

## 📌 About
AI Art Director takes a brand name and description as input and 
automatically generates a complete brand identity kit including 
tagline, color palette, ad copy, and a logo concept — all powered by AI.

## ✨ Features
- 🏷️ AI generated brand tagline
- 🎨 5 color palette with hex codes
- 📢 3 ad copy variations
- 🖼️ AI generated logo concept
- ✨ Try an Example button
- 📱 Responsive layout

## 🛠️ Tech Stack
| Tool | Purpose |
|---|---|
| Python | Core language |
| Streamlit | UI + Deployment |
| Groq API (Llama 3.3) | Brand copy generation |
| Stable Diffusion (Hugging Face) | Logo generation |
| Pillow | Image processing |

## 📁 Project Structure
```
ai-art-director/
├── app.py          → Main Streamlit UI
├── brand_copy.py   → Groq API logic
├── image_gen.py    → Hugging Face API logic
├── requirements.txt → Dependencies
└── .env            → API keys (never shared)
```

## ⚙️ Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 👥 Team
- Member 1 — Backend & AI Integration
- Member 2 — Frontend & UI Design

## 📄 License
MIT

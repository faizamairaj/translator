import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai  


# 🌍 Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 🔐 Configure Gemini API
genai.configure(api_key=api_key)

# 🌐 Supported Languages
languages = ["Urdu 🇵🇰", "French 🇫🇷","Hindi 🇮🇳", "Spanish 🇪🇸", "German 🇩🇪", "Chinese 🇨🇳", "English 🇺🇸"]

# 🖥️ Streamlit UI
st.set_page_config(page_title="🌐 AI Translator", layout="centered")
st.title("🌐✨ AI Translator")

st.markdown("👋 Welcome! Translate your English text into different languages using **Gemini AI** 🧠✨")

text = st.text_area("✍️ Enter English text:")
lang = st.selectbox("🌎 Select target language:", languages)
btn = st.button("🚀 Translate")

if btn and text:
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = f"Translate the following text to {lang.split()[0]}:\n\n{text}"
        response = model.generate_content(prompt)
        st.success(f"✅ Translated to {lang}:")
        st.markdown(f"📘 **{response.text}**")
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

purpose of the code:
yeh code ek "Translator Agent" banata hai jo English se multiple 
languages mein translate karta hai using Gemini API (by Google)
Iska output AI-generated translated paragraph hota hai.


uv init .
uv venv
uv add openai-agents
uv add dotenv
python -m pip install google-generativeai
 streamlit run main.py
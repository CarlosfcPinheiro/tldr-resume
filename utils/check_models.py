import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

try:
    models = genai.list_models()
    print("Available models:")
    for model in models:
        if 'generateContent' in model.supported_generation_methods:
            print(f"- {model.name}")
            print(f"  Display name: {model.display_name}")
            print(f"  Supported methods: {model.supported_generation_methods}")
            print()
except Exception as e:
    print(f"Error listing models: {e}")
import os
from google import genai
from dotenv import load_dotenv

# Loading environment variables from .env file
load_dotenv()

class Summarizer:
    def summarize_dialogue(self, dialogue: str) -> str:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        result = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=f"Summarize the following dialogue in a concise manner:\n\n{dialogue}"
        )
        print(result)

        return result.text
import os
import json

# json_repair is used to fix malformed JSON responses
from json_repair import repair_json
import google.generativeai as genai

from dotenv import load_dotenv

# Loading environment variables from .env file
load_dotenv()

# Summarizer class to handle text summarization using Gemini API
class Summarizer:
    model = genai.GenerativeModel('gemini-2.5-pro')

    def __init__(self):
        if not os.getenv("GEMINI_API_KEY"):
            raise ValueError("GEMINI_API_KEY environment variable not set")
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    def summarize_dialogue(self, text: str) -> str:
        if (len(text.split()) < 30):
            raise ValueError("Input text must be at least 30 words long")
        
        result = self.model.generate_content(
            f"""Summarize the following text in a concise manner. You need to return ONLY  a JSON in this form: 
                {{
                    "summary": "Concise summary of the text",
                    "title": "A short and catchy title for the summary",
                    "content_classification": "only use capitalized single words"
                }}
            
            This is the text: \n\n{text}"""
        )
        repaired_json = repair_json(result.text)
        summary = json.loads(repaired_json)

        words_count_before = len(text.split())
        words_count_after = len(summary['summary'].split())

        print(result)

        return {"result": summary, "words_count_before": words_count_before, "words_count_after": words_count_after}

    def entity_extraction(self, text: str) -> str:
        if (len(text.split()) < 30):
            raise ValueError("Input text must be at least 30 words long")
        result = self.model.generate_content(
            f"""Extract key entities from the following text, you need to return ONLY a JSON array of entities in this form:
            [
                {{
                    "entity": "Entity Name",
                    "type": "Entity Type, ONLY capitalized",
                    "count": Number of times the entity appears in the text
                }},
                ...
            ]

            This is the text: \n\n{text}"""
        )
        print("Raw response:", result.text)

        repaired_json_string = repair_json(result.text)
        entities = json.loads(repaired_json_string)

        return {"entities": entities}
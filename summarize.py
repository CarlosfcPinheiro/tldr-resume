import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Loading environment variables from .env file
load_dotenv()

class Summarizer:
    def summarize_dialogue(self, dialogue: str) -> str:
        client = InferenceClient(token=os.getenv("HF_TOKEN"))
        result = client.summarization(dialogue, model="facebook/bart-large-cnn")

        return result.summary_text
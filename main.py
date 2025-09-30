from fastapi import FastAPI
from pydantic import BaseModel

from summarize import Summarizer

# Instance fastAPI application
app = FastAPI()

# Pydantic model for request body, extending from BaseModel
class Dialogue(BaseModel):
    text: str

@app.get("/")
async def root():
    return "Welcome to Dialogue Resume API"

@app.post("/summarize")
async def summarize(dialogue_data: Dialogue):
    summarizer = Summarizer()
    summary = summarizer.summarize_dialogue(dialogue_data.text)
    return {"summary": summary}
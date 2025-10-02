from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from summarize import Summarizer

# Instance fastAPI application
app = FastAPI(swagger_ui_parameters={"syntaxHighlight": {"theme": "obsidian"}})

# Pydantic models for request body, extending from BaseModel
class Text(BaseModel):
    text: str

@app.get("/")
async def root():
    return "Welcome to Dialogue Resume API"

@app.post("/summarize")
async def summarize(text_data: Text):
    try:
        summarizer = Summarizer()
        data = summarizer.summarize_dialogue(text_data.text)
        return {"data": data, "success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/extract_entities")
async def extract_entities(text_data: Text):
    try:
        summarizer = Summarizer()
        data = summarizer.entity_extraction(text_data.text)

        return {"data": data, "success": True}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
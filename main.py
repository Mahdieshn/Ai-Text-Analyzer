from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import spacy
from fastapi.middleware.cors import CORSMiddleware 

# 1. Initialize FastAPI app and Load the NLP model (CPU-friendly)
app = FastAPI(title="AI Text Insights API", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # در محیط واقعی باید محدود شود
    allow_methods=["*"],
    allow_headers=["*"],
)
nlp = spacy.load("en_core_web_sm")

# 2. Define Request Schema
class TextRequest(BaseModel):
    content: str

# 3. API Endpoints
@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Text Analyzer API! Go to /docs for Swagger UI."}

@app.post("/analyze")
async def analyze_text(request: TextRequest):
    if not request.content.strip():
        raise HTTPException(status_code=400, detail="Text content cannot be empty")
    
    # Process text using SpaCy
    doc = nlp(request.content)
    
    # Extract entities (like Names, Dates, Organizations)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    
    # Simple logic to count words and sentences
    analysis = {
        "word_count": len(doc),
        "sentence_count": len(list(doc.sents)),
        "entities": entities,
        "summary_hint": request.content[:50] + "..." if len(request.content) > 50 else request.content
    }
    
    return {"status": "success", "data": analysis}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
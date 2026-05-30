from fastapi import FastAPI, HTTPException
from app.models import TransformRequest, TransformResponse
from app.ai import transform_text

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.post("/transform", response_model=TransformResponse)
def transform(request: TransformRequest):
    try:
        result = transform_text(request.text)
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc))

    return {
        "original_text": request.text,
        "sentiment": result["sentiment"],
        "keywords": result["keywords"],
        "summary": result["summary"]
    }
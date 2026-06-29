import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.models import TransformRequest, TransformResponse
from app.ai import transform_text

app = FastAPI(
    title="AI Data Transformation Pipeline",
    description="Transform unstructured data into structured insights using AI",
    version="1.0.0"
)


class FetchAndTransformRequest(BaseModel):
    url: str
    extract_field: str = "body"


class FetchAndTransformResponse(TransformResponse):
    source_url: str


@app.get("/")
def home():
    return {
        "message": "AI Data Transformation Pipeline",
        "endpoints": [
            "/transform - Transform manual text",
            "/fetch-and-transform - Fetch from API and transform",
            "/docs - Interactive API documentation"
        ]
    }


@app.post("/transform", response_model=TransformResponse)
def transform(request: TransformRequest):
    """Transform manually provided text into structured insights."""
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


@app.post("/fetch-and-transform", response_model=FetchAndTransformResponse)
def fetch_and_transform(request: FetchAndTransformRequest):
    """Fetch data from external API and transform it into structured insights."""
    try:
        # Fetch data from external API
        response = requests.get(request.url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        # Extract the specified field
        text_to_transform = data.get(request.extract_field, "")
        if not text_to_transform:
            raise ValueError(f"Field '{request.extract_field}' not found in API response")
        
        # Transform using AI
        result = transform_text(text_to_transform)
        
    except requests.RequestException as exc:
        raise HTTPException(status_code=502, detail=f"Failed to fetch from API: {str(exc)}")
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc))
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    return {
        "source_url": request.url,
        "original_text": text_to_transform,
        "sentiment": result["sentiment"],
        "keywords": result["keywords"],
        "summary": result["summary"]
    }
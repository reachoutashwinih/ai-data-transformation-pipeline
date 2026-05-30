# AI Data Transformation Pipeline

AI-powered backend service that transforms unstructured text into structured insights using OpenAI and FastAPI.

## Problem

Many applications receive large amounts of unstructured text data such as customer feedback, reviews, support tickets, and survey responses.

This project demonstrates how AI can automatically extract meaningful insights from raw text and return structured JSON data that can be consumed by downstream applications.

## Architecture

Client → FastAPI → OpenAI API → Structured JSON Response

## Tech Stack

* Python
* FastAPI
* OpenAI API
* Pydantic
* Uvicorn
* Python Dotenv

## Features

* Sentiment Analysis
* Keyword Extraction
* Automatic Text Summarization
* JSON Response Validation
* Error Handling
* Environment-Based Configuration

## API Endpoint

### POST /transform

Request:

```json
{
  "text": "The customer support was excellent and resolved my issue quickly."
}
```

Response:

```json
{
  "original_text": "The customer support was excellent and resolved my issue quickly.",
  "sentiment": "positive",
  "keywords": [
    "customer support",
    "issue resolution"
  ],
  "summary": "Customer is satisfied with the support experience."
}
```

## Run Locally

```bash
pip install -r requirements.txt

uvicorn app.main:app --reload
```

Swagger UI:

http://127.0.0.1:8000/docs

## Key Learnings

* Prompt Engineering
* FastAPI Development
* OpenAI API Integration
* JSON Data Transformation
* Backend Service Design
from pydantic import BaseModel


class TransformRequest(BaseModel):
    text: str


class TransformResponse(BaseModel):
    original_text: str
    sentiment: str
    keywords: list[str]
    summary: str
import os
import json
from pathlib import Path
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv

dotenv_path = Path(__file__).resolve().parent.parent / "properties.env"
load_dotenv(dotenv_path=dotenv_path)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise RuntimeError(
        "Missing OPENAI_API_KEY. Set the OPENAI_API_KEY environment variable or add it to properties.env."
    )

client = OpenAI(api_key=api_key)


def transform_text(user_text: str):

    prompt = f"""
    Analyze the following text and return ONLY valid JSON.

    Required JSON format:
    {{
        "sentiment": "positive/negative/neutral",
        "keywords": ["keyword1", "keyword2"],
        "summary": "short summary"
    }}

    Text:
    {user_text}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0
        )
    except OpenAIError as exc:
        raise RuntimeError(f"OpenAI API error: {exc}") from exc

    ai_output = response.choices[0].message.content

    print("RAW AI OUTPUT:", flush=True)
    print(ai_output, flush=True)

    try:
        return json.loads(ai_output)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            "Failed to parse AI response as JSON. Check the AI response format and prompt instructions."
        ) from exc
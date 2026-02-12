import os
from dotenv import load_dotenv
import openai
from typing import List  # Needed for Python 3.8 type hints

# Load environment variables from .env
load_dotenv()

# Set the API key for openai
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text:str) -> str:

    prompt = f"Summarize the following medical abstract.\n\n{text}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a medical research summarizer"},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract and return the assistant's message
    return response.choices[0].message["content"].strip()
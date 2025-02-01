import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get API key
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key or len(openai_api_key.strip()) == 0:
    raise ValueError(
        "API key is missing or empty. Please ensure OPENAI_API_KEY is set in .env")

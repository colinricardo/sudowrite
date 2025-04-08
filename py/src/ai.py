from openai import AsyncOpenAI

from src.config import OPENAI_API_KEY

ai = AsyncOpenAI(api_key=OPENAI_API_KEY)

MODEL_PROSE = "gpt-4o"
MODEL_STITCH = "gpt-4o"

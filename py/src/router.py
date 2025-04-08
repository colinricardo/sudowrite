from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel

from src.prose import Character, ProseData, loop_parallel

router = APIRouter(prefix="/api")


class GenerateRequest(BaseModel):
    beats: List[str]
    characters: List[Character]
    setting: str
    genre: str
    style: str
    length: Optional[int] = None


class GenerateResponse(BaseModel):
    prose: str
    word_count: int


@router.post("/generate", response_model=GenerateResponse)
async def generate_prose(request: GenerateRequest) -> GenerateResponse:
    data: ProseData = {
        "beats": request.beats,
        "characters": request.characters,
        "setting": request.setting,
        "genre": request.genre,
        "style": request.style,
        "length": request.length,
    }

    print("request received. generating prose...")

    result = await loop_parallel(data=data)

    return GenerateResponse(prose=result["prose"], word_count=result["word_count"])

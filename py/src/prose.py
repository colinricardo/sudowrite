import asyncio
import json
from typing import Any, Dict, List, Optional, TypedDict

from pydantic import BaseModel

from src.ai import MODEL_PROSE, MODEL_STITCH, ai
from src.prose_prompt import get_prose_prompt, get_stitch_prompt
from src.utils import Message, new_assistant_message, new_user_message


class Character(TypedDict):
    name: str
    details: str


class ProseData(TypedDict):
    beats: List[str]
    characters: List[Character]
    setting: str
    genre: str
    style: str
    length: Optional[int]


class ProseResponse(BaseModel):
    prose: str
    word_count: int


async def get_prose_response(
    *,
    data: ProseData,
    history: List[Message],
    new_message: Optional[Message] = None,
    do_stitch: bool = False,
) -> Dict[str, Any]:
    input_data = history.copy()

    if new_message:
        input_data.append(new_message)

    default_length = 1500 if do_stitch else 150
    length = data.get("length", default_length) or default_length

    prompt_fn = get_stitch_prompt if do_stitch else get_prose_prompt

    # generate instructions using prompt function
    instructions = prompt_fn(
        characters=data["characters"],
        setting=data["setting"],
        genre=data["genre"],
        style=data["style"],
        length=length,
    )

    response = await ai.responses.create(
        model=MODEL_STITCH if do_stitch else MODEL_PROSE,
        instructions=instructions,
        input=input_data,  # type: ignore (not bothered typing this insane object, i know it works
        text={
            "format": {
                "type": "json_schema",
                "name": "prose_response",
                "schema": {
                    "type": "object",
                    "name": "prose_response_schema",
                    "additionalProperties": False,
                    "properties": {
                        "prose": {
                            "type": "string",
                            "description": "The generated prose",
                        },
                        "wordCount": {
                            "type": "number",
                            "description": "The total word count of the generated prose",
                        },
                    },
                    "required": ["prose", "wordCount"],
                },
            }
        },
    )

    output_text = response.output_text
    parsed_json = json.loads(output_text)
    json_response = ProseResponse(
        prose=parsed_json["prose"], word_count=parsed_json["wordCount"]
    )

    return {"json": json_response}


async def loop_parallel(*, data: ProseData) -> Dict[str, Any]:
    async def process_beat(beat: str) -> Message:
        new_msg = new_user_message(message=beat)

        # reset history for each beat since we're doing them in parallel anyway
        prose_response = await get_prose_response(
            data=data, history=[], new_message=new_msg
        )

        return new_assistant_message(message=prose_response["json"].prose)

    prose_tasks = [process_beat(beat) for beat in data["beats"]]
    prose_history = await asyncio.gather(*prose_tasks)

    final_response = await get_prose_response(
        data=data,
        history=prose_history,
        do_stitch=True,
        new_message=new_user_message(
            message="Thanks. Now stitch all of the paragraphs together."
        ),
    )

    return {
        "prose": final_response["json"].prose,
        "word_count": final_response["json"].word_count,
    }

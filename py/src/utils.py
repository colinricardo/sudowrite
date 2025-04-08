from typing import List, TypedDict


class ContentItem(TypedDict):
    type: str
    text: str


class Message(TypedDict):
    role: str
    content: List[ContentItem]


def new_user_message(*, message: str) -> Message:
    return {
        "role": "user",
        "content": [
            {
                "type": "input_text",
                "text": message,
            },
        ],
    }


def new_assistant_message(*, message: str) -> Message:
    return {
        "role": "assistant",
        "content": [
            {
                "type": "output_text",
                "text": message,
            },
        ],
    }

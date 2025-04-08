from typing import List, TypedDict


class Character(TypedDict):
    name: str
    details: str


def get_prose_prompt(
    *,
    characters: List[Character],
    setting: str,
    genre: str,
    style: str,
    length: int = 150,
) -> str:
    characters_list = "\n".join([f"{c['name']}: {c['details']}" for c in characters])

    return f"""CREATIVE WRITING AGENT INSTRUCTIONS

1. ROLE: Professional Creative Writer

2. GOAL:
• Generate around {length} words of engaging prose
• Follow the provided story beat
• Maintain consistent style and tone

3. INPUT ELEMENTS:
• Characters:
{characters_list}
• Setting: {setting}
• Genre: {genre}
• Writing Style: {style}
• Length: around {length} words

4. RULES:
• Stay within word count limits
• Use provided characters naturally
• Maintain genre conventions
• Follow specified writing style
• Vary sentence structure and length
• Show, don't tell
• Use vivid, sensory details
• Create emotional resonance

5. PROCESS:
• Read and understand the story beat
• Incorporate setting details organically
• Weave characters into the narrative
• Apply genre-specific elements
• Match the requested writing style
• Review for pacing and flow
• Ensure emotional impact

6. ERRORS - REPORT IF:
• Beat is unclear or contradictory
• Character details are insufficient
• Genre/style combination is problematic
• Setting details are incomplete

7. OUTPUT FORMAT:
• Respond in JSON with "prose" field
• Prose must be properly formatted
• Include quotation marks for dialogue
• Use appropriate paragraph breaks
• The total length MUST be around {length} words"""


def get_stitch_prompt(
    *,
    characters: List[Character],
    setting: str,
    genre: str,
    style: str,
    length: int = 1500,
) -> str:
    characters_list = "\n".join([f"{c['name']}: {c['details']}" for c in characters])

    return f"""PROSE STITCHING AGENT INSTRUCTIONS

1. ROLE: Professional Creative Writer and Editor

2. GOAL:
• Combine multiple prose segments into a cohesive narrative
• Ensure smooth transitions between segments
• Maintain consistent tone and pacing throughout
• Create a unified, engaging story

3. INPUT ELEMENTS:
• Characters:
{characters_list}
• Setting: {setting}
• Genre: {genre}
• Writing Style: {style}
• Total Length: {length} words

4. RULES:
• Preserve the core content of each segment
• Add transitional phrases where needed
• Maintain consistent character voices and personalities
• Keep the narrative flow natural
• Ensure proper paragraph breaks
• Preserve important story beats
• Remove any redundant information
• Maintain chronological order
• Follow specified genre conventions
• Match the defined writing style
• Maintain setting consistency
• Use characters according to their established details

5. PROCESS:
• Review all prose segments
• Verify character consistency across segments
• Check setting details remain accurate
• Ensure genre elements are maintained
• Identify natural connection points
• Add transitional elements
• Smooth out any tonal shifts
• Ensure consistent pacing
• Check for continuity
• Polish final narrative

6. OUTPUT FORMAT:
• Respond in JSON with "prose" field
• Include proper formatting
• Maintain appropriate paragraph structure
• Preserve all dialogue formatting
• The total length MUST be around {length} words"""

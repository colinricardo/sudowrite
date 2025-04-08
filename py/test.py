import asyncio
import time
from typing import List

from src.prose import Character, ProseData, loop_parallel

BEATS: List[str] = [
    "Begin the chapter with Jack and Xander continuing their excavation on the lunar surface, creating a sense of tension and anticipation.",
    "Describe the barren landscape of the moon, emphasizing its desolation and the isolation felt by Jack and Xander.",
    "Use vivid and descriptive language to portray the moment when Jack and Xander uncover an alien artifact, highlighting its mysterious and otherworldly appearance.",
    "Convey Jack's excitement and trepidation as he realizes the significance of the discovery and the potential implications it holds for humanity.",
    "Show Jack immediately contacting Dr. Selene Thorne, emphasizing his trust in her and the urgency of the situation.",
    "Include dialogue between Jack and Dr. Thorne, showcasing their professional relationship and the gravity of the situation.",
    "Highlight the importance of the discovery and the potential consequences it could have on Earth and the lunar mining project.",
    "Show Jack and Xander waiting anxiously for further instructions from Dr. Thorne, creating a sense of anticipation and uncertainty.",
    "Emphasize the isolation and vastness of the lunar landscape, reinforcing the challenges and dangers that Jack and Xander face.",
    "Use sensory details to immerse the reader in the lunar environment, such as the crunch of lunar soil beneath their boots and the cold, airless atmosphere.",
    "Portray Jack's determination and resolve to protect the discovery, even in the face of potential conflict with rival miners.",
    "Hint at the potential dangers and obstacles that Jack and Xander may encounter as they navigate through a world of corporate greed and betrayal.",
    "Foreshadow the secrets and mysteries that the alien artifact holds, building intrigue and anticipation for future chapters.",
    "End the chapter with a cliffhanger or unresolved tension, leaving the reader eager to continue reading and discover what happens next.",
]

CHARACTERS: List[Character] = [
    {
        "name": "Jack",
        "details": "A young man in his early 20s, with a strong sense of adventure and a knack for survival.",
    },
    {
        "name": "Xander",
        "details": "A young woman in her early 20s, with a strong sense of adventure and a knack for survival.",
    },
    {
        "name": "Dr. Selene Thorne",
        "details": "A middle-aged woman in her 40s, with a strong sense of duty and a knack for science.",
    },
]

DATA: ProseData = {
    "beats": BEATS,
    "characters": CHARACTERS,
    "setting": "The moon",
    "genre": "Science Fiction",
    "style": "Fast-paced and action-packed",
    "length": None,
}


async def test() -> None:
    print("starting parallel test...")
    start = time.time()

    result = await loop_parallel(data=DATA)
    prose = result["prose"]
    word_count = result["word_count"]

    end = time.time()
    duration = (end - start) * 1000  # convert to milliseconds

    print(f"parallel execution took {duration}ms")
    print(f"word count: {word_count}")
    print()
    print(f"prose: {prose}")


if __name__ == "__main__":
    asyncio.run(test())

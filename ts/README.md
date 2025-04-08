# ts

## install bun
```
curl -fsSL https://bun.sh/install | bash

```

# how to run code

## clone repo
```
git clone https://github.com/_colinricardo/sudowrite.git
```

## go to ts folder
```
cd sudowrite/ts
```

## make .env file and add openai key
```
OPENAI_API_KEY=sk...
```

## install stuff and run server
```
bun install && bun run main.ts
```

## run with sample beats
```
curl -X POST http://localhost:8000/api/generate \
-H "Content-Type: application/json" \
-d $'{
  "beats": [
    "Begin the chapter with Jack and Xander continuing their excavation on the lunar surface, creating a sense of tension and anticipation.",
    "Describe the barren landscape of the moon, emphasizing its desolation and the isolation felt by Jack and Xander.",
    "Use vivid and descriptive language to portray the moment when Jack and Xander uncover an alien artifact, highlighting its mysterious and otherworldly appearance.",
    "Convey Jack\'s excitement and trepidation as he realizes the significance of the discovery and the potential implications it holds for humanity.",
    "Show Jack immediately contacting Dr. Selene Thorne, emphasizing his trust in her and the urgency of the situation.",
    "Include dialogue between Jack and Dr. Thorne, showcasing their professional relationship and the gravity of the situation.",
    "Highlight the importance of the discovery and the potential consequences it could have on Earth and the lunar mining project.",
    "Show Jack and Xander waiting anxiously for further instructions from Dr. Thorne, creating a sense of anticipation and uncertainty.",
    "Emphasize the isolation and vastness of the lunar landscape, reinforcing the challenges and dangers that Jack and Xander face.",
    "Use sensory details to immerse the reader in the lunar environment, such as the crunch of lunar soil beneath their boots and the cold, airless atmosphere.",
    "Portray Jack\'s determination and resolve to protect the discovery, even in the face of potential conflict with rival miners.",
    "Hint at the potential dangers and obstacles that Jack and Xander may encounter as they navigate through a world of corporate greed and betrayal.",
    "Foreshadow the secrets and mysteries that the alien artifact holds, building intrigue and anticipation for future chapters.",
    "End the chapter with a cliffhanger or unresolved tension, leaving the reader eager to continue reading and discover what happens next."
  ],
  "characters": [
    {
      "name": "Jack",
      "details": "A young man in his early 20s, with a strong sense of adventure and a knack for survival."
    },
    {
      "name": "Xander",
      "details": "A young woman in her early 20s, with a strong sense of adventure and a knack for survival."
    }
  ],
  "setting": "The moon",
  "genre": "Science Fiction",
  "style": "Fast-paced and action-packed",
  "length": 1500
}'
```

## run test file

```
bun run src/test.ts
```

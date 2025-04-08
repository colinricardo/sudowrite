# sudowrite

- [python version](./py/README.md)
- [typescript version](./ts/README.md)
- [colab link](https://colab.research.google.com/drive/1EVnHfyRE9i10QYSAZxzkI7eR1xZnWYMb?usp=sharing)

# approach
- i first wrote this in typescript
- then just rewrote it in python
- i did this cause usually python environments and types are a nightmare, and it's just easier to do quick scripts in typescript (bun)
- i didnt use the python notebook cause i hate them, theyre very finnicky and not used in real life deployments (only for tinkering)

# time taken 
2h 23mins

# task 1: generating prose
- we can generate prose sequentially and then stitch together, which gives marginally better results, but takes way more time
- we could also get the model to generate all proses in one lump using the beats and some reasoning, but this also has not-great results, and is actually slower
- instead, we generate the prose in parallel and then stitch together once we have them all 

# task 2: incorporating metadata
- i did this from the beginning

## discussion 
- we use 4o for both generation and stitching. 4o-mini is too dumb to generate good prose, and 4o is quick enough
- experimented with using 4o-mini for the prose generation, and it's much faster, but the output is much worse
- could experiment with claude here for prose generation here, or gemini flash for stitching
- we can look at user's previous writing, use nltk (or just llm) to parse out the characters, setting, genre that theyre already using
- we can prepare it by putting it into the structure our code/api expects
- generally we can produce code that matches parameters through thorough and precise prompting. using json outputs helps. we could take it a step further by having a supervisor model check outputs, and put it in a loop until we are sure all criteria are satisfied. however this uses a LOT of tokens, and takes much longer, so it's probably not worth it here
- the parallel approach significantly reduces latency, and still produces good outputs. in testing, it was about 3-4x faster than sequential generation
- we could implement a caching layer for common character/setting combinations to further improve performance, but openai already caches static parts of prompts now

# task 3: api server
- for python, i used fastapi
- for typescript, i used fastify
- theyre both simple servers with one endpoint
- in real life you'd have a queue, proper logging, error handling, and input validation on the server

# other stuff
- we could do some proper check to make sure no new characters are hallucinated, or characters are left out, etc.
- we could also just pull the characters from the beats directly  
- we could make a prose generation dsl, but thats probably overkill
- we could add another supervisor model at the end to check if the final output prose properly conforms to everything we want 
- adding style consistency checks could help maintain the same voice throughout different sections
- we could implement a "tone slider" that adjusts how closely the prose adheres to the specified genre/style
- adding support for different languages would expand the tool's usefulness
- implementing a "save drafts" feature would allow users to compare different generations
- we could add a feature to generate alternative versions of specific paragraphs without regenerating the entire piece
- could adjust temperature based on the genre -- e.g. higher for creative/fantasy, lower for technical/realistic

# screenshot
- it should be this easy to run:
![CleanShot 2025-04-08 at 15 20 29@2x](https://github.com/user-attachments/assets/abe21491-5515-468b-9a53-87592b1a67bb)


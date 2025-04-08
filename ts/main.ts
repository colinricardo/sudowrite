import Fastify from "fastify";
import { Character, loopParallel, ProseData } from "./src/prose";

const fastify = Fastify({
  logger: true,
});

type GenerateRequest = {
  beats: string[];
  characters: Character[];
  setting: string;
  genre: string;
  style: string;
  length?: number;
};

// define our simple route
fastify.post<{ Body: GenerateRequest }>(
  "/api/generate",
  async (request, reply) => {
    try {
      const { beats, characters, setting, genre, style, length } = request.body;

      const data: ProseData = {
        beats,
        characters,
        setting,
        genre,
        style,
        length,
      };

      const result = await loopParallel({ data });

      return result;
    } catch (error) {
      console.error("Error processing request:", error);
      reply.status(500);
      return { error: "Failed to process request" };
    }
  }
);

// start server
const start = async () => {
  try {
    await fastify.listen({ port: 8000, host: "0.0.0.0" });
  } catch (err) {
    fastify.log.error(err);
    process.exit(1);
  }
};

start();

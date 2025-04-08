import { z } from "zod";
import { MODEL_PROSE, MODEL_STITCH, ai } from "./ai";
import { getProsePrompt, getStitchPrompt } from "./prose-prompt";
import { newAssistantMessage, newUserMessage } from "./utils";

export type Character = {
  name: string;
  details: string;
};

export type ProseData = {
  beats: string[];
  characters: Character[];
  setting: string;
  genre: string;
  style: string;
  length?: number;
};

const ProseResponse = z.object({
  prose: z.string(),
  wordCount: z.number(),
});

export const getProseResponse = async ({
  data,
  history,
  newMessage,
  doStitch = false,
}: {
  data: ProseData;
  history: any[];
  newMessage?: object;
  doStitch?: boolean;
}) => {
  const input = history;

  if (newMessage) {
    input.push(newMessage);
  }
  const response = await ai.responses.create({
    model: doStitch ? MODEL_STITCH : MODEL_PROSE,
    instructions: doStitch ? getStitchPrompt(data) : getProsePrompt(data),
    input,
    text: {
      format: {
        type: "json_schema",
        name: "prose_response",
        schema: {
          type: "object",
          name: "prose_response_format",
          additionalProperties: false,
          properties: {
            prose: {
              type: "string",
              description: "The generated prose",
            },
            wordCount: {
              type: "number",
              description: "The total word count of the generated prose",
            },
          },
          required: ["prose", "wordCount"],
        },
      },
    },
  });

  const { output_text } = response;
  const parsedJson = JSON.parse(output_text);
  const json = ProseResponse.parse(parsedJson);
  return { json };
};

export const loopParallel = async ({ data }: { data: ProseData }) => {
  const prosePromises = data.beats.map(async (beat) => {
    const newMessage = newUserMessage({ message: beat });

    // reset history for each beat since we're doing them in parallel anyway
    const proseResponse = await getProseResponse({
      data,
      history: [],
      newMessage,
    });

    return newAssistantMessage({ message: proseResponse.json.prose });
  });

  const proseHistory = await Promise.all(prosePromises);

  const finalResponse = await getProseResponse({
    data,
    history: proseHistory,
    doStitch: true,
    newMessage: newUserMessage({
      message: "Thanks. Now stitch all of the paragraphs together.",
    }),
  });

  return {
    prose: finalResponse.json.prose,
    wordCount: finalResponse.json.wordCount,
  };
};

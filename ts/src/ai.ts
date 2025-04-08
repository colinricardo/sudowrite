import OpenAI from "openai";
import { OPENAI_API_KEY } from "./config";

export const ai = new OpenAI({
  apiKey: OPENAI_API_KEY,
});

export const MODEL_PROSE = "gpt-4o";
export const MODEL_STITCH = "gpt-4o";

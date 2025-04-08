export const newUserMessage = ({ message }: { message: string }) => {
  return {
    role: "user",
    content: [
      {
        type: "input_text",
        text: message,
      },
    ],
  };
};

export const newAssistantMessage = ({ message }: { message: string }) => {
  return {
    role: "assistant",
    content: [
      {
        type: "output_text",
        text: message,
      },
    ],
  };
};

import openai
import groq
from agent.logger import logger


class LLMAgent:
    def __init__(self, name, tools=None, llm_provider='openai'):
        self.name = name
        self.tools = tools or []
        self.llm_provider = llm_provider

    def run(self, input_text):
        # Check if any tool can handle this input
        # If local tools can handle the query, there is no need for an LLM call
        for tool in self.tools:
            if tool.can_handle(input_text):
                return tool.handle(input_text)

        # All other queries are sent to the LLM
        logger.info(f"Sending to {self.llm_provider}: {input_text}")

        # LLM Call to OpenAI
        if self.llm_provider=="openai":
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": input_text}]
            )
            return response.choices[0].message["content"]


        # LLM Call to GROQ
        if self.llm_provider=="groq":
            client = groq.Groq()
            response = client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=[{"role":"user", 
                        "content":input_text
                        }],
                temperature=1,
                max_completion_tokens=1024,
                top_p=1,
                # stream=True,
                stop=None,
            )
            return response.choices[0].message.content



import os
import openai
import groq
from dotenv import load_dotenv

load_dotenv()

def run_config(llm_provider='openai'):
  if llm_provider=="openai":
    openai.api_key = os.environ["OPENAI_API_KEY"]
  if llm_provider=="groq":
    groq.api_key = os.environ["GROQ_API_KEY"] 

  print("\nAll set to go...\n" )

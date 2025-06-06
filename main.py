from agent.base import LLMAgent
from agent.tools import CalculatorTool
from config import run_config

# --------------------------------------------------------------------------------------
if __name__ == "__main__":
# --------------------------------------------------------------------------------------
    llm_provider="groq"
    run_config(llm_provider=llm_provider)

    tools = [CalculatorTool()]
    agent = LLMAgent(name="SimpleGPTAgent", tools=tools, llm_provider=llm_provider)
    print("--------------------------------------------\n")

# --------------------------------------------------------------------------------------
    # query1 = "What is the capital of France?"
    query1 = "Briefly tell me about the Italian movie Malena."
    print("User:", query1)
    print("Agent:", agent.run(query1))
    print("--------------------------------------------\n")

# --------------------------------------------------------------------------------------
    # query2 = "What is 12 * 9?"
    query2 = "What is 2 ^ 9**55%5?"
    print("\nUser:", query2)
    print("Agent:", agent.run(query2))
    print("--------------------------------------------\n")

# --------------------------------------------------------------------------------------
    query3 = "What is the statement for Newton's the second law of motion?"
    print("\nUser:", query3)
    print("Agent:", agent.run(query3))
    print("--------------------------------------------\n")

# --------------------------------------------------------------------------------------

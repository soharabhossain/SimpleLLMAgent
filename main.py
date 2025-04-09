from agent.base import LLMAgent
from agent.tools import CalculatorTool

if __name__ == "__main__":
    tools = [CalculatorTool()]
    agent = LLMAgent(name="SimpleGPTAgent", tools=tools)

    query1 = "What is the capital of France?"
    query2 = "What is 12 * 9?"

    print("User:", query1)
    print("Agent:", agent.run(query1))

    print("\nUser:", query2)
    print("Agent:", agent.run(query2))

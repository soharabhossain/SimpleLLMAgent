from agent.base import LLMAgent

def test_agent_response():
    agent = LLMAgent(name="TestAgent")
    reply = agent.run("Say hello!")
    print(reply)
    assert isinstance(reply, str), "assert fails!"


test_agent_response()

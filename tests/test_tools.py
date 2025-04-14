from agent.tools import CalculatorTool

def test_calculator_tool():
    tool = CalculatorTool()
    assert tool.can_handle("What is 5 + 3?"), "assert fails!"
    assert "8" in tool.handle("5 + 3"), "assert fails!"

#test_calculator_tool()

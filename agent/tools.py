import re

class CalculatorTool:
    def can_handle(self, text):
        return bool(re.match(r'.*\d+\s*[\+\-\*\/]\s*\d+.*', text))

    def handle(self, text):
        match = re.search(r'(\d+)\s*([\+\-\*\/])\s*(\d+)', text)
        if match:
            a, op, b = int(match[1]), match[2], int(match[3])
            result = eval(f"{a}{op}{b}")
            return f"The answer is {result}"
        return "Sorry, I couldn't parse the math problem."

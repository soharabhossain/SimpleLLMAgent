# 🧠 SimpleLLMAgent

An open-source project on LLM-based AI agents. 
A toy Python project demonstrating a simple LLM-based agent using OpenAI API. Includes modular structure, a basic tool (calculator) use with logging.

# 🔍 Key Features

- 🧠 **AI Agents**: Create simple LLM-based Agents.
- 📈 **Modular Design:** Definition of agents, logger, tools separated out alighed with modular design for better debugging and meintainability.
- 🖼️ **Flexibility**: Select the LLM providers you would like to use by setting up the confi file.
- ⚙️ **Extensible Design**: Add more tools and LLM providers as you please.

---

## 🗂️ Project Structure

```
simplellmagent/
├── agent/
│   ├── base.py                 # Definition of the Agent class
│   ├── logger.py               # Logger function
│   ├── tools.py                # Definition of tools (Only one Calculator tool defined as of now)
├── tests/
│   ├── test_agent.py           # Testing logic for agents
│   ├── test_tools.py           # Testing logic for tools
├── main.py                     # Script to run the application
├── config.py                   # Module containing the Configuration information
├── requirements.txt            # Required Python packages


## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/soharabhossain/simplellmagent.git
cd simplellmagent
```
### 2. Create and Activate a Virtual Environment
```bash
 python -m venv simplellmagent
 simplellmagent/Sctipts/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
### 3. (Optionally) Run the Setup
 ```bash
pip install -e .
```
### 4. Run the Applications

  ```bash
  python main.py
  ```


   

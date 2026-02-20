# Web Search Agent using Bright Data MCP + LangGraph + Gemini

## What this project does
This is an AI-powered web search agent that uses:
- **Bright Data MCP** to fetch live, real-time web data
- **LangGraph** to create a ReAct agent
- **Google Gemini 2.5 Flash** as the LLM
- **LangChain MCP Adapters** to connect MCP tools with LangChain

The agent searches the web for current information instead of relying on the model's memory.

---

## Project Structure
```
my-project/
  ├── main.py
  ├── .env.example
  ├── requirements.txt
  └── README.md
```

---

## Requirements
- Python 3.10+
- Node.js (required for Bright Data MCP via npx)
- A Bright Data account and API Token
- A Google Gemini API Key

---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Install Python dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```
Then fill in your actual API keys inside `.env`

### 4. Run the project
```bash
python main.py
```

---

## Environment Variables
| Variable | Description |
|---|---|
| `BRIGHT_DATA_API_TOKEN` | Your Bright Data API Token |
| `GOOGLE_API_KEY` | Your Google Gemini API Key |

---

## Example Output
The agent will search the web and return live results. For example:
```
"The IPL 2025 was won by..."
```

---

## Dependencies
- `python-dotenv`
- `langchain`
- `langgraph`
- `langchain-mcp-adapters`
- `langchain-google-genai`
- `langgraph_supervisor`
```

---

## Your `.env.example` should look like:
```
BRIGHT_DATA_API_TOKEN=your_bright_data_token_here
GOOGLE_API_KEY=your_google_api_key_here

import os
import sys
from dotenv import load_dotenv

# Fix Windows console encoding for Unicode
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
import asyncio


async def run_agent():
    client = MultiServerMCPClient(
        {
            "Bright Data": {
                "command": "npx",
                "args": ["@brightdata/mcp"],
                "env": {
                    "API_TOKEN": os.getenv("BRIGHT_DATA_API_TOKEN")
                },
                "transport": "stdio",  
            }
        }
    )
    
    tools = await client.get_tools()
    model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")
    
    agent = create_react_agent(
        model, 
        tools,
        prompt="You are a web search agent.  use the Bright Data tools to search the web and fetch current, up-to-date information for every query. Never answer from memory alone. use the tools to get live data."
    )
    
    agent_response = await agent.ainvoke({
        "messages": "Use web search to find who won IPL 2025 cricket tournament"
    })
    
    print(agent_response["messages"][-1].content)


if __name__ == "__main__":
    asyncio.run(run_agent())

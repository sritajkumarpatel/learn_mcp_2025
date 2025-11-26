from mcp.server.fastmcp import FastMCP
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI()

# Initialize the MCP server for managing local notes
mcp = FastMCP("Local Notes")

@mcp.tool()
def get_web_search_results(query: str) -> str:
    """
    Perform a web search and return the top results.
    
    Args:
        query: The search query string. 
    Returns:
        A string containing the top search results.
    """
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            # No system role - just user and assistant
            {"role": "user", "content": query}
        ],
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    # Start the MCP server and listen for requests
    mcp.run()
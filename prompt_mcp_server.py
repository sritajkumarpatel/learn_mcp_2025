from mcp.server.fastmcp import FastMCP

# Initialize the MCP server for prompting an MCP client
mcp = FastMCP("Prompt MCP Client")

@mcp.prompt()
def get_prompt(prompt: str) -> str:
    """
    Send a prompt to the MCP client and return the response.
    
    Args:
        prompt: The prompt string to send to the MCP client.    
    Returns:
        A string containing the MCP client's response.
    """
    return f"Describe about this and add a funny emoji at end: {prompt}"

@mcp.prompt()
def get_historical_prompt(topic: str) -> str:
    """
    Send a prompt to the MCP client with historical context and return the response.
    
    Args:
        topic: The topic string to send to the MCP client.    
    Returns:
        A string containing the MCP client's response with historical context.
    """
    prompt = "You are a historian. You need to summarize the topic: " + topic + " and tell me in 5 paragraphs about what happened historically."
    return f"Provide historical context for: {prompt}"

if __name__ == "__main__":
    mcp.run()
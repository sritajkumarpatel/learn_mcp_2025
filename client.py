"""
MCP Client for Weather Service

A Python client that connects to the Weather Service MCP server and calls
its tools programmatically. Demonstrates how to interact with MCP servers
using the MCP Python SDK.

Usage:
    python client.py
    
Requirements:
    - weather.py server must be available
    - mcp package with client support
"""

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

# Configure the MCP server connection parameters
# This tells the client how to start and communicate with the server
server_params = StdioServerParameters(
    command="uv",  # Use UV to run the server
    args=["run", "weather.py"],  # Server script to execute
)

async def run(location: str):
    """
    Connect to the Weather Service MCP server and call the get_weather tool.
    
    Args:
        location: The city or location to get weather information for
        
    Example:
        await run("New York")
    """
    # Establish stdio connection to the MCP server
    async with stdio_client(server_params) as (read, write):
        # Create a client session for communication
        async with ClientSession(read, write) as session:
            # Initialize the MCP session (handshake)
            await session.initialize()
            
            try:
                # Call the get_weather tool with location argument
                weather: str = await session.call_tool(
                    "get_weather", 
                    arguments={"location": location}
                )
                print(f"Weather in {location}: {weather}")
                
            except types.ToolCallError as e:
                print("An error occurred while calling the tool:")
                traceback.print_exception(type(e), e, e.__traceback__)
            except Exception as e:
                print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Run the async client with a sample location
    asyncio.run(run(location="Sunnyvale"))
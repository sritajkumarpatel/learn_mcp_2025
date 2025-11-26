"""
MCP Client for Airbnb Service

A Python client that connects to the Airbnb MCP server (Node.js-based)
and discovers available tools. Demonstrates cross-language MCP integration
where a Python client connects to a Node.js server via npx.

Usage:
    python client_airbnb.py
    
Requirements:
    - Node.js and npx installed
    - @openbnb/mcp-server-airbnb package (auto-installed via npx -y)
    - mcp package with client support
    
Note:
    The -y flag in npx automatically installs the package if not present.
"""

from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import asyncio
import traceback

async def main():
    """
    Connect to the Airbnb MCP server and list available tools.
    
    This demonstrates how to:
    - Connect to Node.js MCP servers from Python
    - Use npx to run servers without prior installation
    - Discover available tools dynamically
    """
    
    # Configure connection to Node.js-based Airbnb MCP server
    # npx will download and run the server automatically with -y flag
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@openbnb/mcp-server-airbnb"]
    )

    # Establish stdio connection to the MCP server
    async with stdio_client(server_params) as (read, write):
        # Create a client session for communication
        async with ClientSession(read, write) as session:
            # Initialize the MCP session (handshake)
            await session.initialize()
            
            try:
                # List all available tools provided by the Airbnb server
                print("Available tools:")
                tools = await session.list_tools()
                print(tools)
                
            except Exception as e:
                print(f"Unexpected error: {e}")
                traceback.print_exc()

if __name__ == "__main__":
    # Run the async client to discover Airbnb MCP tools
    asyncio.run(main())
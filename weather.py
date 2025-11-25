"""
Weather Service MCP Server

A simple MCP server that provides weather information tools.
This demonstrates basic MCP server implementation using FastMCP.

Usage:
    As MCP Server: python weather.py
    With Inspector: npx @modelcontextprotocol/inspector uv run weather.py
    With Client: python client.py
"""

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server with a descriptive name
mcp = FastMCP("Weather Service")

@mcp.tool()
def get_weather(location: str) -> str:
    """
    Get the current weather for a given location.
    
    Args:
        location: The name of the city or location to get weather for
        
    Returns:
        A string describing the current weather conditions
        
    Note:
        This is a mock implementation. In production, integrate with a real
        weather API like OpenWeatherMap, WeatherAPI, or similar services.
    """
    # In a real implementation, this function would call a weather API.
    return f"The current weather in {location} is sunny with a temperature of 25°C."

if __name__ == "__main__":
    # Start the MCP server and listen for requests
    mcp.run()
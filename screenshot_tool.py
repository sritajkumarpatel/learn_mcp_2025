from mcp.server.fastmcp import FastMCP

import os

# Initialize the MCP server for managing local notes
mcp = FastMCP("Screenshot")

@mcp.tool()
def take_screenshot() -> str:
    """
    Take a screenshot and save it as screenshot.png.
    
    Returns:
        A confirmation message indicating the screenshot was taken
    """
    try:
        from PIL import ImageGrab
    except ImportError:
        return "PIL module not found. Please install Pillow to use this feature."
    
    screenshot = ImageGrab.grab()
    screenshot.save("screenshot.png")
    
    return "Screenshot taken and saved as screenshot.png"

if __name__ == "__main__":
    # Start the MCP server and listen for requests
    mcp.run()
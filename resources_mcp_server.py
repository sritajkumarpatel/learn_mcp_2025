from mcp.server.fastmcp import FastMCP

# Initialize the MCP server for prompting an MCP client
mcp = FastMCP("Resources MCP Client")

@mcp.resource("inventory://overview")
def get_inventory_overview() -> str:
    """
    Send a resource request to the MCP client and return the response.
    
    Args:
        resource_name: The name of the resource to request from the MCP client.
    Returns:
        A string containing the MCP client's response.
    """

    overview = """Inventory Overview: 
    - Item A: 100 units
    - Item B: 250 units
    - Item C: 75 units"
    """

    return overview.strip()

if __name__ == "__main__":
    mcp.run()
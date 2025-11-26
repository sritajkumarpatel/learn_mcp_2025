from mcp.server.fastmcp import FastMCP
import requests


# Initialize the MCP server for managing local notes
mcp = FastMCP("Local Notes")

@mcp.tool()
def get_cryptocurrency_price(crypto: str) -> str:
    """
    Get the current price of a specified cryptocurrency.
    
    Args:
        crypto: The cryptocurrency name (e.g., 'bitcoin', 'ethereum')
        
    Returns:
        A string with the current price of the cryptocurrency
    """
    

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd"
    response = requests.get(url)
    
    if response.status_code != 200:
        return f"Error fetching price for {crypto}."
    
    data = response.json()
    
    if crypto not in data:
        return f"Cryptocurrency '{crypto}' not found."
    
    price = data[crypto]['usd']
    return f"The current price of {crypto} is ${price} USD."


if __name__ == "__main__":
    # Start the MCP server and listen for requests
    mcp.run()
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio

async def main():
    server_params = StdioServerParameters(
        command="uv",
        args=["run", "resources_mcp_server.py"]
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # List all resources
            resources = await session.list_resources()
            print(resources)
            
            # Read a specific resource
            resource = await session.read_resource("inventory://overview")
            for r in resources.resources:
              print(f"\n📦 {r.name}")
              print(f"   URI: {r.uri}")
              print(f"   Description: {r.description}")

            print("\n📄 Resource Contents:")
            print(resource.contents[0].text)

asyncio.run(main())
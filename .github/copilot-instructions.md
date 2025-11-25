# AI Agent Instructions for MCP Learning Project

## Project Overview

Educational MCP (Model Context Protocol) server implementation project demonstrating custom tool creation, cross-language integration, and AI assistant connectivity using Python 3.13+ and FastMCP framework.

## Architecture Pattern: MCP Server + Client Model

### Server Implementation Pattern

All MCP servers follow this structure (`weather.py`, `local_notes.py`, `screenshot_tool.py`):

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Server Name")

@mcp.tool()
def tool_name(param: str) -> str:
    """Docstring becomes tool description in MCP protocol"""
    return result

if __name__ == "__main__":
    mcp.run()  # Starts stdio-based MCP server
```

**Key Convention**: Tool docstrings are exposed via MCP protocol - write them for AI consumers, not just developers.

### Client Pattern

MCP clients use async/await with stdio communication (`client.py`, `client_airbnb.py`):

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="uv",  # or "npx" for Node.js servers
    args=["run", "weather.py"]
)

async with stdio_client(server_params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        result = await session.call_tool("tool_name", arguments={...})
```

## Development Workflows

### UV-First Environment (Primary)

```powershell
# Add dependencies - updates pyproject.toml + uv.lock
uv add "package-name"

# Run any command in project venv
uv run python script.py
uv run pytest
```

**Critical**: Always use `uv run` prefix for execution - direct `python` calls won't use project environment.

### Testing MCP Servers (4 Methods)

1. **Direct Function Test** (fastest iteration):

   ```powershell
   uv run python -c "from weather import get_weather; print(get_weather('Tokyo'))"
   ```

2. **MCP Inspector** (recommended for debugging):

   ```powershell
   npx @modelcontextprotocol/inspector uv run weather.py
   # Opens http://localhost:5173 with interactive UI
   ```

3. **Python Client** (programmatic access):

   ```powershell
   uv run python client.py
   ```

4. **VS Code Integration** (production): Configure in `.vscode/mcp.json`

### Configuration Management

**MCP Server Registry**: `.vscode/mcp.json` maps server names to commands:

- **Python servers**: `"command": "uv", "args": ["run", "script.py"]`
- **Node.js servers**: `"command": "npx", "args": ["-y", "@package/name"]`
- **Pre-built binaries**: `"command": "path\\to\\executable.exe", "type": "stdio"`

Example from project:

```json
{
  "servers": {
    "weather-service": {
      "command": "uv",
      "args": ["run", "weather.py"]
    },
    "airbnb": {
      "command": "npx",
      "args": ["-y", "@openbnb/mcp-server-airbnb"]
    }
  }
}
```

## Cross-Language Integration

**Python ↔ Node.js**: MCP protocol enables language-agnostic communication. See `client_airbnb.py` connecting to Node.js `@openbnb/mcp-server-airbnb` server via npx.

**Pattern**: Use `npx -y` for zero-install Node.js server execution from Python clients.

## Project-Specific Conventions

### Error Handling

- Import errors return descriptive messages (see `screenshot_tool.py`): `"PIL module not found. Please install Pillow"`
- Use `try/except` with `traceback.print_exception` for tool call failures (pattern in `client.py`)

### File-Based State

`local_notes.py` demonstrates stateful MCP tools using filesystem (`notes.txt`). Check file existence before operations:

```python
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File '{file_path}' does not exist")
```

### Dependencies

- **Core**: `mcp[cli]>=1.22.0` (includes client/server + CLI tools)
- **Optional**: Platform-specific packages (e.g., `pywin32==311` for Windows, `pillow` for screenshots)

## Common Pitfalls

1. **Running without UV**: Direct `python weather.py` may use wrong interpreter/packages. Always use `uv run`.
2. **Missing MCP CLI tools**: Use `mcp[cli]` not just `mcp` package.
3. **Forgetting async/await**: All MCP client operations are async - use `asyncio.run()` at entry point.
4. **Tool naming**: MCP exposes Python function names directly as tool names (snake_case preserved).

## Testing & Validation

**Quick Server Validation**:

```powershell
# List tools in server
uv run python -c "from weather import mcp; print(mcp.list_tools())"

# Verify imports
uv run python -c "from weather import mcp; print('OK')"
```

**Inspector for Integration Testing**: Use MCP Inspector (`npx @modelcontextprotocol/inspector`) to visually test request/response flow before writing client code.

## When Adding New Features

1. **New Tool**: Add `@mcp.tool()` decorated function to existing server file
2. **New Server**: Copy `weather.py` template, update server name and tools, add to `.vscode/mcp.json`
3. **New Dependency**: Use `uv add package-name` (updates `pyproject.toml` + `uv.lock`)
4. **External API Integration**: Follow mock pattern in `weather.py` - document in docstring that it's educational/mock implementation

## Key Files

- `weather.py` - Canonical MCP server example (minimal, well-documented)
- `client.py` - Reference Python client implementation
- `client_airbnb.py` - Cross-language integration example
- `.vscode/mcp.json` - Server registry for VS Code/Claude Desktop
- `pyproject.toml` - Single source of truth for dependencies (UV managed)

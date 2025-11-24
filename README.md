# MCP Learning Project 2025

A hands-on project to demonstrate building and deploying **Model Context Protocol (MCP)** servers. This project showcases how to create custom MCP tools, configure them for AI assistants, and integrate them with various clients like Claude Desktop, Continue, and other MCP-compatible applications.

## Tech Stack

| Category | Technology | Purpose |
|----------|------------|---------|
| **Language** | Python 3.13+ | Core programming language |
| **Protocol** | MCP (Model Context Protocol) | Standardized AI-tool communication |
| **Framework** | FastMCP | Rapid MCP server development |
| **Package Manager** | UV or pip + venv | Dependency management |
| **Validation** | Pydantic | Data validation and type safety |
| **Server** | Uvicorn | ASGI server for MCP |

## Prerequisites

- **Python 3.13+** installed on your system
- **UV** (recommended) or **pip + venv** for package management
- **VS Code** (optional but recommended for MCP configuration)
- **Git** for version control

## Installation

<table>
<tr>
<th width="50%">Using UV (Recommended)</th>
<th width="50%">Using pip + venv</th>
</tr>
<tr>
<td>

**1. Install UV:**
```bash
# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**2. Initialize project:**
```bash
# Create new project
uv init learn-mcp-2025
cd learn-mcp-2025

# Or in existing directory
uv init
```

**3. Add MCP dependencies:**
```bash
# Add MCP with CLI tools
uv add "mcp[cli]"

# This creates/updates:
# - pyproject.toml
# - uv.lock
```

**4. Install all dependencies:**
```bash
uv sync
```

</td>
<td>

**1. Navigate to project:**
```bash
cd learn-mcp-2025
```

**2. Create virtual environment:**
```bash
python -m venv .venv
```

**3. Activate virtual environment:**
```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (CMD)
.venv\Scripts\activate.bat
```

**4. Install dependencies:**
```bash
# From requirements.txt
pip install -r requirements.txt

# Or install package in editable mode
pip install -e .
```

</td>
</tr>
</table>

### Generated Files

| UV | pip + venv |
|----|------------|
| `pyproject.toml` - Project metadata and dependencies | `requirements.txt` - Pinned dependencies |
| `uv.lock` - Locked dependency versions | `.venv/` - Virtual environment directory |

## MCP Server Configuration

To integrate your MCP server with AI clients (like Claude Desktop), create a configuration file:

### Create `.vscode/mcp.json`

```json
{
    "servers": {
        "weather-service": {
            "command": "python",
            "args": ["weather.py"],
            "env": {}
        }
    }
}
```

### Multi-Server Configuration

```json
{
    "servers": {
        "weather-service": {
            "command": "python",
            "args": ["weather.py"],
            "env": {}
        },
        "winget-mcp": {
            "type": "stdio",
            "command": "C:\\Users\\YourUser\\AppData\\Local\\Microsoft\\WindowsApps\\...\\WindowsPackageManagerMCPServer.exe"
        }
    }
}
```

### Configuration Options

| Field | Description | Example |
|-------|-------------|---------|
| `command` | Executable to run | `python`, `node`, `uv` |
| `args` | Arguments passed to command | `["weather.py"]`, `["run", "server.py"]` |
| `env` | Environment variables | `{"API_KEY": "value"}` |
| `type` | Communication type | `stdio` (default) |

## Running the MCP Server

### Method 1: Quick Testing (Direct Function Call)

Test individual functions without starting the full MCP server:

<table>
<tr>
<th width="50%">Using UV</th>
<th width="50%">Using pip + venv</th>
</tr>
<tr>
<td>

```bash
uv run python -c "from weather import get_weather; print(get_weather('London'))"
```

**Output:**
```
The current weather in London is sunny with a temperature of 25°C.
```

</td>
<td>

```bash
# Activate venv first
.venv\Scripts\Activate.ps1

# Then run
python -c "from weather import get_weather; print(get_weather('London'))"
```

**Output:**
```
The current weather in London is sunny with a temperature of 25°C.
```

</td>
</tr>
</table>

**When to use:**
- ✅ Fast iteration during development
- ✅ Unit testing individual tools
- ✅ Debugging function logic
- ❌ Won't work with MCP clients

### Method 2: Production Mode (Full MCP Server)

Run as a complete MCP server for AI assistant integration:

<table>
<tr>
<th width="50%">Using UV</th>
<th width="50%">Using pip + venv</th>
</tr>
<tr>
<td>

```bash
# Start MCP server
uv run python weather.py

# The server will start and listen for MCP requests
```

</td>
<td>

```bash
# Activate venv first
.venv\Scripts\Activate.ps1

# Start MCP server
python weather.py
```

</td>
</tr>
</table>

**When to use:**
- ✅ Integration with AI assistants (Claude, Continue, etc.)
- ✅ Production deployments
- ✅ Multi-tool servers
- ✅ Standardized MCP protocol communication

### Method 3: MCP Inspector (Development & Debugging)

Use the MCP Inspector to interactively test your server:

<table>
<tr>
<th width="50%">Using UV</th>
<th width="50%">Using pip + venv</th>
</tr>
<tr>
<td>

```bash
# Install MCP inspector (if not installed)
uv add mcp-inspector

# Start inspector
uv run mcp dev weather.py
```

</td>
<td>

```bash
# Install MCP inspector
pip install mcp-inspector

# Activate venv
.venv\Scripts\Activate.ps1

# Start inspector
mcp dev weather.py
```

</td>
</tr>
</table>

**MCP Inspector Features:**
- 🔍 Interactive tool testing
- 📊 Request/response inspection
- 🐛 Real-time debugging
- 📝 Schema validation
- 🔄 Live reload on file changes

**Access Inspector:**
```
Open browser: http://localhost:5173
```

## Project Structure

```
learn-mcp-2025/
├── .vscode/
│   └── mcp.json              # MCP server configuration for VS Code
├── .venv/                    # Virtual environment (pip only)
├── weather.py                # Main MCP server implementation
├── pyproject.toml            # Project metadata & dependencies (UV)
├── requirements.txt          # Pinned dependencies (pip)
├── uv.lock                   # Locked dependency versions (UV)
├── .python-version           # Python version specification
├── .gitignore               # Git ignore rules
└── README.md                # This file
```

### Key Files Explained

| File | Purpose |
|------|---------|
| `weather.py` | MCP server with tools decorated with `@mcp.tool()` |
| `pyproject.toml` | Modern Python project configuration (PEP 621) |
| `requirements.txt` | Traditional pip dependency list |
| `uv.lock` | UV's deterministic dependency lock file |
| `.vscode/mcp.json` | MCP client configuration for VS Code |

## Quick Command Reference

### UV Commands

| Command | Description |
|---------|-------------|
| `uv init` | Initialize new Python project |
| `uv add <package>` | Add dependency to project |
| `uv remove <package>` | Remove dependency |
| `uv sync` | Install/sync all dependencies |
| `uv run <command>` | Run command in project environment |
| `uv pip list` | List installed packages |
| `uv pip show <package>` | Show package details |
| `uv lock` | Update lock file |
| `uv python install <ver>` | Install Python version |
| `uv python list` | List available Python versions |

### pip + venv Commands

| Command | Description |
|---------|-------------|
| `python -m venv .venv` | Create virtual environment |
| `.venv\Scripts\Activate.ps1` | Activate venv (PowerShell) |
| `.venv\Scripts\activate.bat` | Activate venv (CMD) |
| `pip install -r requirements.txt` | Install dependencies |
| `pip install -e .` | Install package in editable mode |
| `pip install <package>` | Install single package |
| `pip uninstall <package>` | Remove package |
| `pip list` | List installed packages |
| `pip show <package>` | Show package details |
| `pip freeze > requirements.txt` | Export dependencies |
| `deactivate` | Deactivate virtual environment |

### MCP Commands

| Command | Description |
|---------|-------------|
| `mcp dev <file>` | Start MCP Inspector for development |
| `mcp --version` | Check MCP CLI version |
| `python <file>.py` | Start MCP server in production |

## Development Examples

### Example 1: Adding a New Weather Tool

Edit `weather.py`:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather Service")

@mcp.tool()
def get_weather(location: str) -> str:
    """Get current weather for a location."""
    return f"The current weather in {location} is sunny with a temperature of 25°C."

@mcp.tool()
def get_forecast(location: str, days: int = 7) -> str:
    """Get weather forecast for the next N days."""
    return f"Forecast for {location} for the next {days} days: Mostly sunny"

@mcp.tool()
def get_temperature(location: str, unit: str = "celsius") -> str:
    """Get current temperature in specified unit."""
    temp = 25 if unit == "celsius" else 77
    return f"Temperature in {location}: {temp}°{unit[0].upper()}"

if __name__ == "__main__":
    mcp.run()
```

### Example 2: Testing New Tools

```bash
# Test with UV
uv run python -c "from weather import get_forecast; print(get_forecast('Paris', 5))"

# Test with pip/venv
python -c "from weather import get_forecast; print(get_forecast('Paris', 5))"
```

### Example 3: Adding Type Safety

```python
from typing import Literal
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather Service")

@mcp.tool()
def get_temperature(
    location: str, 
    unit: Literal["celsius", "fahrenheit"] = "celsius"
) -> str:
    """Get temperature with validated unit parameter."""
    temp = 25 if unit == "celsius" else 77
    return f"Temperature in {location}: {temp}°{unit[0].upper()}"
```

### Example 4: Debugging & Verification

```bash
# List all tools in your server
uv run python -c "from weather import mcp; print(mcp.list_tools())"

# Check Python version
uv run python --version

# Verify MCP package
uv pip show mcp

# Test imports
uv run python -c "from weather import mcp; print('MCP initialized successfully')"
```

## License

This project is for learning purposes.

# MCP Learning Project 2025 🚀

![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-Protocol-orange?style=for-the-badge)
![FastMCP](https://img.shields.io/badge/FastMCP-Server-blue?style=for-the-badge)
![UV](https://img.shields.io/badge/UV-Package_Manager-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-Learning-green?style=for-the-badge)

> A hands-on project to demonstrate building and deploying **Model Context Protocol (MCP)** servers. Learn how to create custom MCP tools, configure them for AI assistants, and integrate them with Claude Desktop, Continue, and other MCP-compatible applications.

## 🎯 What You'll Learn

- 🛠️ Build custom MCP servers from scratch
- 🔌 Integrate MCP tools with AI assistants
- 🧪 Test and debug using MCP Inspector
- 📦 Manage dependencies with UV or pip
- 🚀 Deploy production-ready MCP servers
- 🎨 Create type-safe tools with Pydantic

## 🏗️ Tech Stack

| Category | Technology | Purpose |
|----------|------------|---------|
| **Language** | Python 3.13+ | Core programming language |
| **Protocol** | MCP (Model Context Protocol) | Standardized AI-tool communication |
| **Framework** | FastMCP | Rapid MCP server development |
| **Package Manager** | UV or pip + venv | Dependency management |
| **Validation** | Pydantic | Data validation and type safety |
| **Server** | Uvicorn | ASGI server for MCP |

## 📋 Prerequisites

Before diving in, make sure you have:

- ✅ **Python 3.13+** installed on your system
- ✅ **UV** (recommended) or **pip + venv** for package management
- ✅ **VS Code** (optional but recommended for MCP configuration)
- ✅ **Git** for version control
- ✅ **Terminal** access (PowerShell, CMD, or Bash)

## 🚀 Installation

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

## ⚙️ MCP Server Configuration

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

## 🎮 Running the MCP Server

### Method 1: Quick Testing ⚡ (Direct Function Call)

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

### Method 2: Production Mode 🚀 (Full MCP Server)

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

### Method 3: MCP Inspector 🔍 (Development & Debugging)

Use the MCP Inspector to interactively test your server with a web UI:

<table>
<tr>
<th width="50%">Using Python MCP CLI</th>
<th width="50%">Using Node.js npx (Recommended)</th>
</tr>
<tr>
<td>

**With UV:**
```bash
# Start MCP dev mode
uv run mcp dev <your-server.py>
```

**With pip + venv:**
```bash
# Activate venv first
.venv\Scripts\Activate.ps1

# Start MCP dev mode
mcp dev <your-server.py>
```

**Features:**
- Terminal-based debugging
- Log output in console
- Quick server validation
- ❌ No web UI

</td>
<td>

**With UV:**
```bash
# No installation needed - npx downloads temporarily
npx @modelcontextprotocol/inspector uv run <your-server.py>
```

**With pip + venv:**
```bash
# Activate venv first
.venv\Scripts\Activate.ps1

# Run inspector with Python
npx @modelcontextprotocol/inspector python <your-server.py>
```

**Features:**
- ✅ Interactive web UI
- ✅ Visual tool explorer
- ✅ Request/response inspection
- ✅ Real-time testing
- ✅ Always latest version

</td>
</tr>
</table>

**MCP Inspector Features:**
- 🔍 Interactive tool testing in browser
- 📊 Request/response inspection
- 🐛 Real-time debugging
- 📝 Schema validation
- 🎨 Visual interface for all MCP tools

**Access Inspector:**
```
Open browser: http://localhost:5173
```

**Example with weather.py:**
```bash
$ npx @modelcontextprotocol/inspector uv run weather.py
MCP Inspector running at http://localhost:5173
Server: Weather Service
Tools available: get_weather
```

### Method 4: Python Client 🐍 (Programmatic Access)

Use Python code to connect to MCP servers programmatically:

**Example 1: Connect to Weather Service (Python Server)**

```bash
# Run the weather client
python client.py
```

**Example 2: Connect to Airbnb Service (Node.js Server)**

```bash
# Run the Airbnb client (connects to Node.js server via npx)
python client_airbnb.py
```

**Client Features:**
- 📡 Programmatic MCP server connections
- 🔄 Async/await communication patterns
- 🌐 Cross-language support (Python ↔ Node.js)
- 🛠️ Direct tool invocation from code
- 📋 Dynamic tool discovery with `list_tools()`

**When to use:**
- ✅ Building MCP-powered applications
- ✅ Automating tool calls in scripts
- ✅ Testing server integrations
- ✅ Creating custom MCP workflows
- ✅ Connecting to third-party MCP servers

## 📁 Project Structure

```
learn-mcp-2025/
├── .github/
│   ├── copilot-instructions.md    # AI agent development guidelines
│   └── prompts/                   # Reusable prompt templates
├── .vscode/
│   └── mcp.json                   # MCP server configuration for VS Code/AI assistants
├── .venv/                         # Virtual environment (pip only)
│
├── MCP Servers (Tools for AI Assistants)
├── weather__mcp_server.py         # 🔧 Weather service tools
├── crypto_mcp_server.py           # 🔧 Cryptocurrency price tools
├── local_notes_mcp_server.py      # 🔧 Local notes management tools
├── screenshot_tool.py             # 🔧 Screenshot capture tool
│
├── MCP Clients (Test & Integration)
├── weather_mcp_client.py          # 🔌 Client for weather server
├── airbnb_mcp_client.py           # 🔌 Client for Airbnb server (Node.js)
│
├── Configuration & Dependencies
├── pyproject.toml                 # Project metadata & dependencies (UV)
├── requirements.txt               # Pinned dependencies (pip)
├── uv.lock                        # Locked dependency versions (UV)
├── .python-version                # Python version specification
├── .gitignore                     # Git ignore rules
├── notes.txt                      # Data file for local_notes_mcp_server
└── README.md                      # This file
```

### Key Files Explained

| File | Type | Purpose |
|------|------|---------|
| `weather__mcp_server.py` | **MCP Server** | Weather service with mock weather data tools |
| `crypto_mcp_server.py` | **MCP Server** | Cryptocurrency price lookup tools |
| `local_notes_mcp_server.py` | **MCP Server** | File-based notes management (add/get) |
| `screenshot_tool.py` | **MCP Server** | Screenshot capture using Pillow |
| `weather_mcp_client.py` | **MCP Client** | Python client connecting to weather server |
| `airbnb_mcp_client.py` | **MCP Client** | Python client connecting to Node.js Airbnb server |
| `pyproject.toml` | Config | Modern Python project configuration (PEP 621) |
| `requirements.txt` | Config | Traditional pip dependency list (auto-generated) |
| `uv.lock` | Config | UV's deterministic dependency lock file |
| `.vscode/mcp.json` | Config | MCP server registry for VS Code/Claude Desktop |

## 📚 Quick Command Reference

### UV Commands 🔮

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

### pip + venv Commands 🐍

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

### MCP Commands 🔧

| Command | Description |
|---------|-------------|
| `mcp dev <file>` | Start MCP Inspector for development |
| `mcp --version` | Check MCP CLI version |
| `python <file>.py` | Start MCP server in production |

## 💡 Development Examples

### Example 1: Adding a New Weather Tool 🌤️

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

### Example 2: Testing New Tools ✅

```bash
# Test with UV
uv run python -c "from weather import get_forecast; print(get_forecast('Paris', 5))"

# Test with pip/venv
python -c "from weather import get_forecast; print(get_forecast('Paris', 5))"
```

### Example 3: Adding Type Safety 🔒

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

### Example 4: Building a Python MCP Client 🔌

```python
# client.py
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import asyncio

server_params = StdioServerParameters(
    command="uv",
    args=["run", "weather.py"]
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # Call a tool
            result = await session.call_tool(
                "get_weather", 
                arguments={"location": "Tokyo"}
            )
            print(result)
            
            # List all available tools
            tools = await session.list_tools()
            print(f"Available tools: {tools}")

if __name__ == "__main__":
    asyncio.run(main())
```

### Example 5: Cross-Language MCP Integration 🌐

Connect Python client to Node.js MCP server:

```python
# client_airbnb.py
server_params = StdioServerParameters(
    command="npx",
    args=["-y", "@openbnb/mcp-server-airbnb"]
)

async def main():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # Discover tools from Node.js server
            tools = await session.list_tools()
            print(f"Airbnb MCP Tools: {tools}")
```

### Example 6: Debugging & Verification 🐛

```bash
# List all tools in your server
uv run python -c "from weather import mcp; print(mcp.list_tools())"

# Check Python version
uv run python --version

# Verify MCP package
uv pip show mcp

# Test imports
uv run python -c "from weather import mcp; print('MCP initialized successfully')"

# Run client tests
python client.py
python client_airbnb.py
```

## 🤝 Contributing

This is a learning project! Feel free to:
- 🐛 Report bugs or issues
- 💡 Suggest new MCP tools
- 📝 Improve documentation
- 🔀 Submit pull requests

## 📄 License

This project is for learning purposes.

---

<div align="center">

**Built with ❤️ for learning MCP**

⭐ Star this repo if you found it helpful!

[🐙 GitHub](https://github.com/sritajkumarpatel/learn_mcp_2025) • [📚 MCP Docs](https://modelcontextprotocol.io) • [🔧 FastMCP](https://github.com/jlowin/fastmcp)

</div>

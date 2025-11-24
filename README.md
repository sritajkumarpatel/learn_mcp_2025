# MCP Weather Service

A Model Context Protocol (MCP) server project that provides weather information through a standardized interface.

## Tech Stack

- **Python 3.13+** - Core programming language
- **MCP (Model Context Protocol)** - Communication protocol for AI model interactions
- **FastMCP** - Fast MCP server implementation
- **UV** or **pip + venv** - Python package management
- **Pydantic** - Data validation using Python type annotations

## Prerequisites

- **Python 3.13+** - Programming language runtime
- **[UV](https://docs.astral.sh/uv/)** (recommended) or **pip + venv** - Package manager
- **VS Code** (optional) - For MCP configuration

## Installation

### Option 1: Using UV (Recommended)

1. **Install UV:**
   ```bash
   # Windows (PowerShell)
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. **Navigate to project directory:**
   ```bash
   cd C:\AI\learn_mcp_2025
   ```

3. **Install dependencies:**
   ```bash
   uv sync
   ```

### Option 2: Using pip and venv

1. **Navigate to project directory:**
   ```bash
   cd C:\AI\learn_mcp_2025
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment:**
   ```bash
   # Windows (PowerShell)
   .venv\Scripts\Activate.ps1
   
   # Windows (CMD)
   .venv\Scripts\activate.bat
   ```

4. **Install dependencies:**
   ```bash
   pip install -e .
   ```

## Running the Weather Service

### Method 1: Direct Function Call (Quick Testing)

Test the weather function directly without starting an MCP server:

**Using UV:**
```bash
uv run python -c "from weather import get_weather; print(get_weather('Biona'))"
```

**Using pip/venv:**
```bash
# Activate venv first, then:
python -c "from weather import get_weather; print(get_weather('Biona'))"
```

**Output:**
```
The current weather in Biona is sunny with a temperature of 25°C.
```

**When to use:**
- ✅ Fast and simple for testing
- ✅ No server startup required
- ✅ Good for development and debugging

### Method 2: MCP Server Mode (Production Use)

Run as a full MCP server that can be accessed by AI assistants and other MCP clients:

**Using UV:**
```bash
uv run python weather.py
```

**Using pip/venv:**
```bash
# Activate venv first, then:
python weather.py
```

**When to use:**
- ✅ Standardized MCP protocol
- ✅ Works with Claude Desktop, Continue, and other MCP clients
- ✅ Supports multiple tools in one server
- ✅ Professional integration

## MCP Server Configuration

To use the weather service with MCP clients (like Claude Desktop):

### Step 1: Create Configuration File

Create `.vscode/mcp.json` in your project root:

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

### Step 2: (Optional) Add Multiple MCP Servers

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

### Step 3: Connect from MCP Clients

Once configured, MCP clients can automatically discover and use your weather service.

## System Verification

Before running the weather service, verify your setup:

### 1. Check Python Installation

```bash
python --version
# Should show Python 3.13 or higher
```

### 2. Verify MCP Package

**Using UV:**
```bash
uv pip show mcp
```

**Using pip/venv:**
```bash
pip show mcp
```

### 3. Test Module Import

**Using UV:**
```bash
uv run python -c "from weather import mcp; print('MCP initialized successfully')"
```

**Using pip/venv:**
```bash
python -c "from weather import mcp; print('MCP initialized successfully')"
```

### 4. List Available Tools

**Using UV:**
```bash
uv run python -c "from weather import mcp; print(mcp.list_tools())"
```

**Using pip/venv:**
```bash
python -c "from weather import mcp; print(mcp.list_tools())"
```

### 5. Verify Configuration File

```bash
# Check if mcp.json exists
ls .vscode/mcp.json

# View contents (Windows PowerShell)
Get-Content .vscode/mcp.json
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named 'mcp'` | **UV:** Run `uv sync` <br> **pip:** Run `pip install -e .` |
| `Python version mismatch` | Check `.python-version` file <br> **UV:** `uv python install 3.13` <br> **pip:** Install Python 3.13+ |
| `Access is denied (os error 5)` | Run PowerShell as Administrator or use `uv run python` / `python` directly |
| Virtual environment not activated (pip users) | Run `.venv\Scripts\Activate.ps1` |

## Command Reference

### UV Commands

| Command | Description |
|---------|-------------|
| `uv sync` | Install/sync project dependencies |
| `uv add <package>` | Add a new dependency |
| `uv remove <package>` | Remove a dependency |
| `uv run <command>` | Run command in project environment |
| `uv pip list` | List installed packages |
| `uv lock` | Update lock file |
| `uv python install <version>` | Install Python version |

### pip + venv Commands

| Command | Description |
|---------|-------------|
| `python -m venv .venv` | Create virtual environment |
| `.venv\Scripts\Activate.ps1` | Activate venv (PowerShell) |
| `pip install -e .` | Install project in editable mode |
| `pip install <package>` | Install a package |
| `pip uninstall <package>` | Remove a package |
| `pip list` | List installed packages |
| `pip freeze > requirements.txt` | Export dependencies |
| `deactivate` | Deactivate virtual environment |

## Development

### Adding New Tools

Edit `weather.py` to add new MCP tools:

```python
@mcp.tool()
def get_forecast(location: str, days: int = 7) -> str:
    """Get weather forecast for the next N days."""
    return f"Forecast for {location} for the next {days} days: Mostly sunny"

@mcp.tool()
def get_temperature(location: str, unit: str = "celsius") -> str:
    """Get current temperature in specified unit."""
    return f"Temperature in {location}: 25°{unit[0].upper()}"
```

### Testing Changes

**Using UV:**
```bash
# Quick test
uv run python -c "from weather import get_forecast; print(get_forecast('Mumbai', 5))"

# Start MCP server
uv run python weather.py
```

**Using pip/venv:**
```bash
# Quick test
python -c "from weather import get_forecast; print(get_forecast('Mumbai', 5))"

# Start MCP server
python weather.py
```

### Debugging Tips

1. **List installed packages:**
   - UV: `uv pip list`
   - pip: `pip list`

2. **Check Python version:**
   - UV: `uv run python --version`
   - pip: `python --version`

3. **Test imports:**
   - UV: `uv run python -c "from weather import mcp; print(mcp)"`
   - pip: `python -c "from weather import mcp; print(mcp)"`

## Project Structure

```
.
├── .vscode/
│   └── mcp.json          # MCP server configuration
├── .venv/                # Virtual environment (if using pip)
├── weather.py            # Weather MCP server implementation
├── pyproject.toml        # Project dependencies and metadata
├── uv.lock               # Locked dependency versions (UV)
└── README.md             # This file
```

## License

This project is for learning purposes.

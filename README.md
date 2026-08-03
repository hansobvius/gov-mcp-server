*On Progress Project.*

# Government MCP Server

A Model Context Protocol (MCP) server that provides access to Brazilian government open data APIs, specifically focused on congressional deputy and proposition information from the Chamber of Deputies (Câmara dos Deputados).

## Overview

This project implements an MCP server that allows AI assistants (Claude Desktop, Google Antigravity, etc.) and other applications to query Brazilian government databases through a standardized protocol. The server provides tools to search for information about federal deputies and legislative propositions using the official open data API from the Chamber of Deputies.

## Features

- **Deputy Search & Details**: Search for federal deputies by name and query their detailed information.
- **Proposition Queries**: Search for legislative proposals and details related to deputies.
- **Dual Transport (stdio & SSE)**: Run locally via standard input/output (`stdio`) or as a networked HTTP/SSE service (`sse`).
- **Docker Ready**: Includes `Dockerfile` and `docker-compose.yml` for quick containerized deployment.
- **Open Data Integration**: Connects to the official Brazilian government open data API.
- **Async Operations**: Built with `async`/`await` and `httpx` for optimal performance.

## Project Structure

```
gov-mcp-server/
├── Dockerfile                  # Docker image definition
├── docker-compose.yml          # Docker compose configuration
├── .dockerignore               # Docker ignore rules
├── requirements.txt            # Python dependencies
├── main.py                     # Main application entry point (stdio / SSE)
├── manifest.json               # MCP server metadata
└── src/
    ├── config.py               # FastMCP instance & configuration
    ├── api/
    │   ├── api.py              # Central API export module
    │   ├── deputies/           # Deputies API integration
    │   └── propositions/       # Propositions API integration
    └── tools/
        ├── deputies_tools.py   # Deputy MCP tools
        └── proposition_tools.py # Proposition MCP tools
```

## Installation & Setup

### Prerequisites

- Python 3.10+ (or Docker)
- pip (Python package installer)

### Local Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd gov-mcp-server
```

2. (Optional) Create and activate a virtual environment:
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

---

## Running the Server

### 1. Standard stdio Mode (Default for Local AI Assistants)

```bash
python main.py
```

### 2. HTTP Mode (Streamable HTTP / SSE)

Run directly with Python:
```bash
# Using CLI flag:
python main.py --http

# Or using environment variables:
MCP_TRANSPORT=http HOST=0.0.0.0 PORT=8000 python main.py
```

### 3. Docker Container (Localhost / Remote PoC)

**Using Docker Compose:**
```bash
docker compose up --build
```

**Using Docker CLI:**
```bash
docker build -t gov-mcp-server .
docker run -p 8000:8000 --name gov-mcp-server gov-mcp-server
```

The Streamable HTTP endpoint will be available at: `http://localhost:8000/mcp` (or `http://localhost:8000/sse` for SSE).

---

## Client Configuration

### Google Antigravity & Claude Desktop

#### Option A: Local `stdio` Mode

Add to your `mcp_config.json` (`~/.gemini/config/mcp_config.json` in Antigravity or `claude_desktop_config.json` in Claude Desktop):

```json
{
  "mcpServers": {
    "gov-mcp-server": {
      "command": "python",
      "args": [
        "C:/Users/thiag/Projetos/MCP_Projects/gov-mcp-server/main.py"
      ],
      "env": {
        "PYTHONPATH": "C:/Users/thiag/Projetos/MCP_Projects/gov-mcp-server"
      }
    }
  }
}
```

#### Option B: Docker / Remote `HTTP` Mode

```json
{
  "mcpServers": {
    "gov-mcp-server": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

---

## Available Tools

### `get_deputies_by_names_tool`
Search for federal deputies by name.

- **Parameters:**
  - `name` (*string*): Name or partial name of the deputy (e.g., `"eduardo"`).

### `get_propositions_by_id_tools`
Search for propositions related to a deputy ID.

- **Parameters:**
  - `proposition_id` (*string*): Deputy or proposition ID (e.g., `"220589"`).

---

## API Integration

The server integrates with the Brazilian Chamber of Deputies open data API:

- **Base URL**: `https://dadosabertos.camara.leg.br/api/v2`
- **Data Source**: Official Brazilian government open data
- **Update Frequency**: Real-time data from government systems

## Dependencies

- `mcp`: Model Context Protocol SDK (`FastMCP`)
- `httpx`: Async HTTP client for API requests
- `uvicorn`: ASGI server for SSE transport
- `typing-extensions`: Type hints support

## License

This project is licensed under the MIT License.

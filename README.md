*On Progress Project.*

# Government MCP Server

A Model Context Protocol (MCP) server that provides access to Brazilian government open data APIs, specifically focused on congressional deputy information from the Chamber of Deputies (Câmara dos Deputados).

## Overview

This project implements an MCP server that allows AI assistants and other applications to query Brazilian government databases through a standardized protocol. The server currently provides tools to search for information about federal deputies using the official open data API from the Chamber of Deputies.

## Features

- **Deputy Search**: Search for federal deputies by name
- **Open Data Integration**: Connects to the official Brazilian government open data API
- **MCP Protocol**: Implements the Model Context Protocol for seamless AI assistant integration
- **Async Operations**: Built with async/await for optimal performance

## Project Structure

```
src/
├── main.py                 # Main application entry point
├── config.py              # Configuration and MCP server initialization
├── api/
│   ├── api.py            # API module imports
│   └── deputados/
│       └── deputados_api.py  # Deputy API implementation
└── mcp/
    ├── tools.py          # MCP tool definitions
    └── project_tools/
        └── deputados_tools.py  # Deputy-specific tools
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd gov-mcp-server
```

2. Install dependencies:
```bash
pip install mcp httpx
```

3. Run the server:
```bash
python src/main.py
```

## Usage

### Running the MCP Server

The server runs in stdio mode and can be integrated with MCP-compatible clients:

```bash
python src/main.py
```

### Available Tools

#### `get_deputados_por_nome`

Search for federal deputies by name.

**Parameters:**
- `nome` (string): Name or partial name of the deputy (e.g., "eduardo")

**Example:**
```python
# Search for deputies with "eduardo" in their name
result = await get_deputados_por_nome("eduardo")
```

## API Integration

The server integrates with the Brazilian Chamber of Deputies open data API:

- **Base URL**: `https://dadosabertos.camara.leg.br/api/v2`
- **Data Source**: Official Brazilian government open data
- **Update Frequency**: Real-time data from government systems

## Configuration

The server configuration is managed in `src/config.py`:

```python
URL_BASE_API = "https://dadosabertos.camara.leg.br/api/v2"
```

## Development

### Adding New Tools

1. Create API functions in the appropriate `src/api/` subdirectory
2. Define MCP tools in `src/mcp/tools.py`
3. Import and register tools in the main configuration

### Project Architecture

- **API Layer** (`src/api/`): Handles external API calls and data processing
- **MCP Layer** (`src/mcp/`): Defines MCP tools and protocol implementation
- **Configuration** (`src/config.py`): Server setup and constants

## Dependencies

- `mcp`: Model Context Protocol implementation
- `httpx`: Async HTTP client for API requests

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Support

For issues and questions:
1. Check existing issues in the repository
2. Create a new issue with detailed information
3. Provide logs and error messages when reporting bugs

## Future Enhancements

- Support for additional government APIs (Senate, ministries, etc.)
- Enhanced search capabilities
- Data caching and optimization
- Authentication support for premium APIs
- Additional data export formats

## Related Projects

- [Model Context Protocol](https://github.com/modelcontextprotocol): Official MCP specification
- [Brazilian Government Open Data](https://dados.gov.br/): Official open data portal
- [Chamber of Deputies API](https://dadosabertos.camara.leg.br/swagger/api.html): Official API documentation

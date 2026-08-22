#!/usr/bin/env python3
"""
MCP Server para buscar informações sobre o congresso brasileiro
Main entry point - imports from src modules
"""

import os
import sys

# Use package imports; ensure `src` is a proper package (has __init__.py)
from src.config import mcp

# Import all tool modules to register their @mcp.tool() decorators
import src.tools.deputies_tools
import src.tools.proposition_tools
import src.tools.votacoes_tools
import src.tools.orgaos_tools
import src.tools.partidos_blocos_tools
import src.tools.eventos_tools
import src.tools.frentes_grupos_tools
import src.tools.legislaturas_tools
import src.tools.referencias_tools


if __name__ == '__main__':
    transport = os.getenv("MCP_TRANSPORT", "stdio").lower()
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))

    if transport in ("http", "sse", "streamable-http") or "--http" in sys.argv or "--sse" in sys.argv:
        t = "sse" if ("--sse" in sys.argv or transport == "sse") else "http"
        print(f"Starting MCP server with transport='{t}' on {host}:{port}...", file=sys.stderr)
        mcp.run(transport=t, host=host, port=port)
    else:
        mcp.run(transport="stdio")

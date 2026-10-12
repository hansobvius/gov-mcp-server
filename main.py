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
import src.tools.camara.deputies_tools
import src.tools.camara.proposition_tools
import src.tools.camara.votacoes_tools
import src.tools.camara.orgaos_tools
import src.tools.camara.partidos_blocos_tools
import src.tools.camara.eventos_tools
import src.tools.camara.frentes_grupos_tools
import src.tools.camara.legislaturas_tools
import src.tools.camara.referencias_tools
import src.tools.senado.senadores_tools
import src.tools.senado.comissoes_tools
import src.tools.senado.composicao_tools
import src.tools.senado.processos_tools
import src.tools.senado.plenario_votacoes_tools
import src.tools.senado.discursos_tools
import src.tools.senado.legislacao_orcamento_tools


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

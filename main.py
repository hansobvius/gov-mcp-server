#!/usr/bin/env python3
"""
MCP Server para buscar informações sobre o congresso brasileiro
Main entry point - imports from src modules
"""

# Use package imports; ensure `src` is a proper package (has __init__.py)
from src.config import mcp
import src.tools.deputies_tools  # import module to register its tools with `mcp`


if __name__ == '__main__':
    mcp.run(transport='stdio')

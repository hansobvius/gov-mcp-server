#!/usr/bin/env python3
"""
MCP Server para buscar informações sobre o congresso brasileiro
Main entry point - imports from src modules
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import from src modules
from config import mcp
from tools.deputies_tools import get_deputies_by_names_tool


if __name__ == '__main__':
    mcp.run(transport='stdio')

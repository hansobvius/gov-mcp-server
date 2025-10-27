import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

from config import mcp

# Import tools to register them with the MCP server
import src.mcp.tools

if __name__ == '__main__':
    mcp.run(transport='stdio')
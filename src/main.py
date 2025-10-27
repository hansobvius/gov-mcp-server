import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Ensure the project root is in the Python path for MCP imports
project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from config import mcp

# Import tools to register them with the MCP server
# Import the local mcp_tools module (not the installed mcp package)
import mcp_tools.tools

if __name__ == '__main__':
    mcp.run(transport='stdio')
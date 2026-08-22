import pytest
import json
from src.config import mcp
import src.tools.deputies_tools as deputies_tools
import main


@pytest.mark.asyncio
async def test_mcp_tool_execution():
    result = await deputies_tools.get_deputies_by_names_tool("eduardo")
    assert result is not None
    assert isinstance(result, str)
    parsed = json.loads(result)
    assert "dados" in parsed


@pytest.mark.asyncio
async def test_mcp_server_initialization():
    assert mcp.name == "gov-mcp-server"
    tools = await mcp.list_tools()
    assert len(tools) == 70

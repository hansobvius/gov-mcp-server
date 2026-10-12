import pytest
from src.config import mcp
import src.tools as tools
from src.tools.senado import SENADO_TOOL_DESCRIPTIONS
import main


@pytest.mark.asyncio
async def test_senado_tools_registration():
    tools_list = await mcp.list_tools()
    registered_tools = {t.name: t for t in tools_list}

    print(f"\nTotal Senate tools in catalog: {len(SENADO_TOOL_DESCRIPTIONS)}")
    assert len(SENADO_TOOL_DESCRIPTIONS) == 56

    for tool_name, desc in SENADO_TOOL_DESCRIPTIONS.items():
        assert tool_name in registered_tools, f"Ferramenta do Senado '{tool_name}' não foi registrada no FastMCP!"
        assert tool_name in tools.TOOL_DESCRIPTIONS, f"Descrição de '{tool_name}' ausente em TOOL_DESCRIPTIONS!"
        assert len(tools.TOOL_DESCRIPTIONS[tool_name]) > 10, f"Descrição de '{tool_name}' muito curta!"

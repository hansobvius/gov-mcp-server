import json

from src.config import mcp
from src.api.api import get_deputados_by_name


@mcp.tool()
async def get_deputies_by_names_tool(name: str) -> str:
    """Busca deputies pelo nome.
    Args:
        name: Nome ou parte do nome do deputado (ex: eduardo)
    """
    data = await get_deputados_by_name(name=name)
    if data:
        # Return as JSON string
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "No deputies found", "dados": []})
import json

from src.config import mcp
from src.api.api import get_propositions_by_id


@mcp.tool()
async def get_propositions_by_id_tools(proposition_id: str) -> str:
    """Busca proposições pelo id de um deputado.

    Args:
        proposition_id: ID de um deputado (ex: 220589)

    Returns:
        JSON string contendo os dados da proposição ou um objeto de erro
        ``{"error": "No propositions found", "dados": []}`` caso não exista.
    """
    data = await get_propositions_by_id(proposition_id=proposition_id)
    if data:
        # Return as JSON string
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "No propositions found", "dados": []})

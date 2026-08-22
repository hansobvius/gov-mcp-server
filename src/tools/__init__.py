# Tools package

from .deputies_tools import get_deputies_by_names_tool
from .proposition_tools import get_propositions_by_id_tools

# Export the tools that should be publicly available
__all__ = [
    "get_deputies_by_names_tool",
    "get_propositions_by_id_tools",
]

# Centralized descriptions for agents / UI help
TOOL_DESCRIPTIONS = {
    "get_deputies_by_names_tool": "Busca deputados pelo nome ou parte dele e devolve JSON com os resultados.",
    "get_propositions_by_id_tools": "Recupera detalhes de uma proposição a partir do seu ID e devolve JSON com os dados ou erro.",
}

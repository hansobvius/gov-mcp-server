import mcp

from src.api.deputados import deputados_api

@mcp.tool()
async def get_deputados_por_nome(nome: str) -> str:
    """Busca deputados pelo nome.
    Args:
        nome: Nome ou parte do nome do deputado (ex: eduardo)
    """
    data = await deputados_api(nome=nome)
    if not data:
        return data
    return 'Result not generated'
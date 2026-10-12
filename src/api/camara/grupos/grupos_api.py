from typing import Any, Dict, List, Optional, Union
from src.api.client import get_request


async def get_grupos(
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15,
    ordem: str = "ASC",
    ordenarPor: str = "id"
) -> Optional[Dict[str, Any]]:
    """Consulta e lista os grupos parlamentares de cooperação internacional."""
    params = {
        "pagina": pagina,
        "itens": itens,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request("/grupos", params=params)


async def get_grupo_details(grupo_id: int) -> Optional[Dict[str, Any]]:
    """Retorna dados detalhados sobre um determinado grupo interparlamentar."""
    return await get_request(f"/grupos/{grupo_id}")


async def get_grupo_historico(grupo_id: int) -> Optional[Dict[str, Any]]:
    """Retorna o histórico de alterações e variações de estado de um grupo parlamentar."""
    return await get_request(f"/grupos/{grupo_id}/historico")


async def get_grupo_membros(
    grupo_id: int,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None,
    ordem: str = "ASC",
    ordenarPor: str = "id"
) -> Optional[Dict[str, Any]]:
    """Retorna a lista de parlamentares integrantes de um grupo interparlamentar."""
    params = {
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request(f"/grupos/{grupo_id}/membros", params=params)

from typing import Any, Dict, List, Optional, Union
from src.api.client import get_request


async def get_frentes(
    idLegislatura: Optional[Union[int, List[int], str]] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15
) -> Optional[Dict[str, Any]]:
    """Consulta e lista frentes parlamentares registradas na Câmara."""
    params = {
        "idLegislatura": idLegislatura,
        "pagina": pagina,
        "itens": itens
    }
    return await get_request("/frentes", params=params)


async def get_frente_details(frente_id: int) -> Optional[Dict[str, Any]]:
    """Retorna detalhes e coordenação de uma frente parlamentar."""
    return await get_request(f"/frentes/{frente_id}")


async def get_frente_membros(frente_id: int) -> Optional[Dict[str, Any]]:
    """Retorna os deputados que participam como membros da frente parlamentar."""
    return await get_request(f"/frentes/{frente_id}/membros")

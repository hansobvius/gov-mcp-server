from typing import Any, Dict, List, Optional, Union
from src.api.client import get_request


async def get_blocos(
    id: Optional[Union[int, List[int], str]] = None,
    idLegislatura: Optional[Union[int, List[int], str]] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15,
    ordem: str = "ASC",
    ordenarPor: str = "nome"
) -> Optional[Dict[str, Any]]:
    """Consulta e lista blocos partidários formados em uma ou mais legislaturas."""
    params = {
        "id": id,
        "idLegislatura": idLegislatura,
        "pagina": pagina,
        "itens": itens,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request("/blocos", params=params)


async def get_bloco_details(bloco_id: int) -> Optional[Dict[str, Any]]:
    """Retorna dados detalhados sobre um bloco partidário específico."""
    return await get_request(f"/blocos/{bloco_id}")


async def get_bloco_partidos(
    bloco_id: int,
    data: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """Retorna os partidos que integram o bloco em uma data específica ou atualmente."""
    params = {
        "data": data
    }
    return await get_request(f"/blocos/{bloco_id}/partidos", params=params)

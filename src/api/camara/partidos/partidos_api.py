from typing import Any, Dict, List, Optional, Union
from src.api.client import get_request


async def get_partidos(
    sigla: Optional[Union[str, List[str]]] = None,
    idLegislatura: Optional[Union[int, List[int], str]] = None,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15,
    ordem: str = "ASC",
    ordenarPor: str = "sigla"
) -> Optional[Dict[str, Any]]:
    """Consulta e lista partidos políticos com parlamentares em exercício na Câmara."""
    params = {
        "sigla": sigla,
        "idLegislatura": idLegislatura,
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "pagina": pagina,
        "itens": itens,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request("/partidos", params=params)


async def get_partido_details(partido_id: int) -> Optional[Dict[str, Any]]:
    """Retorna dados detalhados sobre um partido político."""
    return await get_request(f"/partidos/{partido_id}")


async def get_partido_lideres(
    partido_id: int,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15
) -> Optional[Dict[str, Any]]:
    """Retorna a lista de deputados que são ou foram líderes de um partido."""
    params = {
        "pagina": pagina,
        "itens": itens
    }
    return await get_request(f"/partidos/{partido_id}/lideres", params=params)


async def get_partido_membros(
    partido_id: int,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None,
    idLegislatura: Optional[Union[int, List[int], str]] = None,
    ordenarPor: str = "nome",
    ordem: str = "ASC",
    itens: Optional[int] = 15,
    pagina: Optional[int] = 1
) -> Optional[Dict[str, Any]]:
    """Retorna a lista de parlamentares filiados ao partido em determinado período."""
    params = {
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "idLegislatura": idLegislatura,
        "ordenarPor": ordenarPor,
        "ordem": ordem,
        "itens": itens,
        "pagina": pagina
    }
    return await get_request(f"/partidos/{partido_id}/membros", params=params)

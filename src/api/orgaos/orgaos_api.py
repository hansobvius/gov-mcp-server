from typing import Any, Dict, List, Optional, Union
from src.api.client import get_request


async def get_orgaos(
    id: Optional[Union[int, List[int], str]] = None,
    sigla: Optional[Union[str, List[str]]] = None,
    codTipoOrgao: Optional[Union[int, List[int], str]] = None,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15,
    ordem: str = "ASC",
    ordenarPor: str = "nome"
) -> Optional[Dict[str, Any]]:
    """Consulta e lista comissões e outros órgãos da Câmara dos Deputados."""
    params = {
        "id": id,
        "sigla": sigla,
        "codTipoOrgao": codTipoOrgao,
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "pagina": pagina,
        "itens": itens,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request("/orgaos", params=params)


async def get_orgao_details(orgao_id: int) -> Optional[Dict[str, Any]]:
    """Retorna dados detalhados sobre um órgão específico da Câmara."""
    return await get_request(f"/orgaos/{orgao_id}")


async def get_orgao_events(
    orgao_id: int,
    idTipoEvento: Optional[Union[int, List[int], str]] = None,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15,
    ordem: str = "ASC",
    ordenarPor: str = "dataHoraInicio"
) -> Optional[Dict[str, Any]]:
    """Retorna a lista de eventos realizados ou previstos em um órgão legislativo."""
    params = {
        "idTipoEvento": idTipoEvento,
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "pagina": pagina,
        "itens": itens,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request(f"/orgaos/{orgao_id}/eventos", params=params)


async def get_orgao_members(
    orgao_id: int,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15
) -> Optional[Dict[str, Any]]:
    """Retorna os parlamentares membros e cargos ocupados no órgão."""
    params = {
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "pagina": pagina,
        "itens": itens
    }
    return await get_request(f"/orgaos/{orgao_id}/membros", params=params)


async def get_orgao_votings(
    orgao_id: int,
    idProposicao: Optional[Union[int, List[int], str]] = None,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15,
    ordem: str = "DESC",
    ordenarPor: str = "dataHoraRegistro"
) -> Optional[Dict[str, Any]]:
    """Retorna informações detalhadas sobre votações ocorridas em um órgão."""
    params = {
        "idProposicao": idProposicao,
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "pagina": pagina,
        "itens": itens,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request(f"/orgaos/{orgao_id}/votacoes", params=params)

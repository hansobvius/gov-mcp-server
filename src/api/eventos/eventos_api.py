from typing import Any, Dict, List, Optional, Union
from src.api.client import get_request


async def get_eventos(
    id: Optional[Union[int, List[int], str]] = None,
    codTipoEvento: Optional[Union[int, List[int], str]] = None,
    codSituacao: Optional[Union[int, List[int], str]] = None,
    codTipoOrgao: Optional[Union[int, List[int], str]] = None,
    idOrgao: Optional[Union[int, List[int], str]] = None,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None,
    horaInicio: Optional[str] = None,
    horaFim: Optional[str] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15,
    ordem: str = "ASC",
    ordenarPor: str = "dataHoraInicio"
) -> Optional[Dict[str, Any]]:
    """Consulta e lista eventos ocorridos ou previstos nos órgãos da Câmara."""
    params = {
        "id": id,
        "codTipoEvento": codTipoEvento,
        "codSituacao": codSituacao,
        "codTipoOrgao": codTipoOrgao,
        "idOrgao": idOrgao,
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "horaInicio": horaInicio,
        "horaFim": horaFim,
        "pagina": pagina,
        "itens": itens,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request("/eventos", params=params)


async def get_evento_details(evento_id: int) -> Optional[Dict[str, Any]]:
    """Retorna dados detalhados sobre um evento específico."""
    return await get_request(f"/eventos/{evento_id}")


async def get_evento_deputados(evento_id: int) -> Optional[Dict[str, Any]]:
    """Retorna os deputados participantes ou convidados para um evento."""
    return await get_request(f"/eventos/{evento_id}/deputados")


async def get_evento_orgaos(evento_id: int) -> Optional[Dict[str, Any]]:
    """Retorna os órgãos organizadores responsáveis pelo evento."""
    return await get_request(f"/eventos/{evento_id}/orgaos")


async def get_evento_pauta(evento_id: int) -> Optional[Dict[str, Any]]:
    """Retorna a pauta de proposições para deliberação em um evento."""
    return await get_request(f"/eventos/{evento_id}/pauta")


async def get_evento_votacoes(evento_id: int) -> Optional[Dict[str, Any]]:
    """Retorna as votações ocorridas durante o evento."""
    return await get_request(f"/eventos/{evento_id}/votacoes")

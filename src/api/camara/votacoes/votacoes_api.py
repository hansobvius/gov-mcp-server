from typing import Any, Dict, List, Optional, Union
from src.api.client import get_request


async def get_votacoes(
    id: Optional[Union[int, List[int], str]] = None,
    idProposicao: Optional[Union[int, List[int], str]] = None,
    idEvento: Optional[Union[int, List[int], str]] = None,
    idOrgao: Optional[Union[int, List[int], str]] = None,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15,
    ordem: str = "DESC",
    ordenarPor: str = "dataHoraRegistro"
) -> Optional[Dict[str, Any]]:
    """Consulta e lista votações realizadas na Câmara dos Deputados."""
    params = {
        "id": id,
        "idProposicao": idProposicao,
        "idEvento": idEvento,
        "idOrgao": idOrgao,
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "pagina": pagina,
        "itens": itens,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request("/votacoes", params=params)


async def get_votacao_details(votacao_id: str) -> Optional[Dict[str, Any]]:
    """Retorna detalhes e resultado de uma votação específica."""
    return await get_request(f"/votacoes/{votacao_id}")


async def get_votacao_orientacoes(votacao_id: str) -> Optional[Dict[str, Any]]:
    """Retorna as orientações de bancada e liderança para uma votação."""
    return await get_request(f"/votacoes/{votacao_id}/orientacoes")


async def get_votacao_votos(votacao_id: str) -> Optional[Dict[str, Any]]:
    """Retorna o voto nominal de cada parlamentar em uma votação."""
    return await get_request(f"/votacoes/{votacao_id}/votos")

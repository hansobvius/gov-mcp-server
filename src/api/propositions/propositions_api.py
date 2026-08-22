from typing import Any, Dict, List, Optional, Union
from src.api.client import get_request


async def get_proposicoes(
    id: Optional[Union[int, List[int], str]] = None,
    siglaTipo: Optional[Union[str, List[str]]] = None,
    numero: Optional[Union[int, List[int], str]] = None,
    ano: Optional[Union[int, List[int], str]] = None,
    codTipo: Optional[Union[int, List[int], str]] = None,
    idDeputadoAutor: Optional[Union[int, List[int], str]] = None,
    autor: Optional[str] = None,
    siglaPartidoAutor: Optional[Union[str, List[str]]] = None,
    idPartidoAutor: Optional[Union[int, List[int], str]] = None,
    siglaUfAutor: Optional[Union[str, List[str]]] = None,
    keywords: Optional[str] = None,
    tramitacaoSenado: Optional[bool] = None,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None,
    dataApresentacaoInicio: Optional[str] = None,
    dataApresentacaoFim: Optional[str] = None,
    codSituacao: Optional[Union[int, List[int], str]] = None,
    codTema: Optional[Union[int, List[int], str]] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15,
    ordem: str = "ASC",
    ordenarPor: str = "id"
) -> Optional[Dict[str, Any]]:
    """Busca e lista proposições na Câmara dos Deputados segundo critérios avançados."""
    params = {
        "id": id,
        "siglaTipo": siglaTipo,
        "numero": numero,
        "ano": ano,
        "codTipo": codTipo,
        "idDeputadoAutor": idDeputadoAutor,
        "autor": autor,
        "siglaPartidoAutor": siglaPartidoAutor,
        "idPartidoAutor": idPartidoAutor,
        "siglaUfAutor": siglaUfAutor,
        "keywords": keywords,
        "tramitacaoSenado": tramitacaoSenado,
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "dataApresentacaoInicio": dataApresentacaoInicio,
        "dataApresentacaoFim": dataApresentacaoFim,
        "codSituacao": codSituacao,
        "codTema": codTema,
        "pagina": pagina,
        "itens": itens,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request("/proposicoes", params=params)


async def get_propositions_by_id(proposition_id: Union[int, str]) -> Optional[Dict[str, Any]]:
    """Busca proposições associadas a um ID de autor (mantém compatibilidade)."""
    data = await get_proposicoes(idDeputadoAutor=proposition_id)
    if not data:
        return None

    proposition_list = []
    propositions_list = data.get("dados", [])
    if propositions_list:
        for proposition in propositions_list:
            prop_id = proposition.get("id")
            if prop_id:
                try:
                    proposition_detail = await get_proposition_details(prop_id)
                    if proposition_detail and "dados" in proposition_detail:
                        proposition_list.append(proposition_detail["dados"])
                except Exception:
                    proposition_list.append(proposition)

    return {
        "dados": proposition_list,
        "links": data.get("links", []),
    }


async def get_proposition_details(proposition_id: Union[int, str]) -> Optional[Dict[str, Any]]:
    """Busca detalhes completos de uma proposição específica pelo seu ID."""
    return await get_request(f"/proposicoes/{proposition_id}")


async def get_proposition_authors(proposition_id: Union[int, str]) -> Optional[Dict[str, Any]]:
    """Lista as pessoas e/ou entidades autoras de uma proposição."""
    return await get_request(f"/proposicoes/{proposition_id}/autores")


async def get_proposition_related(proposition_id: Union[int, str]) -> Optional[Dict[str, Any]]:
    """Lista proposições relacionadas a uma em especial."""
    return await get_request(f"/proposicoes/{proposition_id}/relacionadas")


async def get_proposition_themes(proposition_id: Union[int, str]) -> Optional[Dict[str, Any]]:
    """Lista áreas temáticas vinculadas a uma proposição."""
    return await get_request(f"/proposicoes/{proposition_id}/temas")


async def get_proposition_tramitations(
    proposition_id: Union[int, str],
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """Retorna o histórico de passos na tramitação de uma proposição."""
    params = {
        "dataInicio": dataInicio,
        "dataFim": dataFim
    }
    return await get_request(f"/proposicoes/{proposition_id}/tramitacoes", params=params)


async def get_proposition_votings(
    proposition_id: Union[int, str],
    ordem: str = "DESC",
    ordenarPor: str = "dataHoraRegistro"
) -> Optional[Dict[str, Any]]:
    """Retorna as votações ocorridas sobre uma proposição específica."""
    params = {
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request(f"/proposicoes/{proposition_id}/votacoes", params=params)
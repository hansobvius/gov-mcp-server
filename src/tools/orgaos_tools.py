import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.orgaos.orgaos_api import (
    get_orgaos,
    get_orgao_details,
    get_orgao_events,
    get_orgao_members,
    get_orgao_votings,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_orgaos_tool(
    sigla: Optional[str] = None,
    cod_tipo_orgao: Optional[int] = None,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "ASC",
    ordenar_por: str = "nome"
) -> str:
    """Consulta e lista comissões permanentes, especiais, CPIs e outros órgãos da Câmara.

    Args:
        sigla: Sigla do órgão (ex.: "CCJC", "CFT", "PLEN").
        cod_tipo_orgao: Código do tipo de órgão (ex.: 2 para Comissão Permanente).
        data_inicio: Data de início (AAAA-MM-DD).
        data_fim: Data de término (AAAA-MM-DD).
        pagina: Número da página (padrão: 1).
        itens: Quantidade de itens por página (máximo: 100, padrão: 15).
        ordem: Ordenação ("ASC" ou "DESC").
        ordenar_por: Campo de ordenação ("id", "sigla", "nome", "apelido").
    """
    data = await get_orgaos(
        sigla=sigla,
        codTipoOrgao=cod_tipo_orgao,
        dataInicio=data_inicio,
        dataFim=data_fim,
        pagina=pagina,
        itens=itens,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)


@mcp.tool()
async def get_orgao_details_tool(orgao_id: int) -> str:
    """Retorna detalhes cadastrais, competência e informações completas de um órgão da Câmara.

    Args:
        orgao_id: Identificador numérico do órgão (ex.: 2003 para CCJC).
    """
    data = await get_orgao_details(orgao_id=orgao_id)
    return _json_response(data)


@mcp.tool()
async def get_orgao_events_tool(
    orgao_id: int,
    id_tipo_evento: Optional[int] = None,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "ASC",
    ordenar_por: str = "dataHoraInicio"
) -> str:
    """Retorna os eventos, audiências públicas e reuniões de um órgão legislativo.

    Args:
        orgao_id: Identificador numérico do órgão.
        id_tipo_evento: ID do tipo de evento.
        data_inicio: Data de início (AAAA-MM-DD).
        data_fim: Data de término (AAAA-MM-DD).
        pagina: Página de resultados.
        itens: Quantidade de itens.
        ordem: Ordenação.
        ordenar_por: Campo de ordenação.
    """
    data = await get_orgao_events(
        orgao_id=orgao_id,
        idTipoEvento=id_tipo_evento,
        dataInicio=data_inicio,
        dataFim=data_fim,
        pagina=pagina,
        itens=itens,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)


@mcp.tool()
async def get_orgao_members_tool(
    orgao_id: int,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    pagina: int = 1,
    itens: int = 15
) -> str:
    """Retorna a lista de deputados membros titulares, suplentes e diretoria de um órgão.

    Args:
        orgao_id: Identificador numérico do órgão.
        data_inicio: Data de início (AAAA-MM-DD).
        data_fim: Data de término (AAAA-MM-DD).
        pagina: Página de resultados.
        itens: Quantidade de itens.
    """
    data = await get_orgao_members(
        orgao_id=orgao_id,
        dataInicio=data_inicio,
        dataFim=data_fim,
        pagina=pagina,
        itens=itens
    )
    return _json_response(data)


@mcp.tool()
async def get_orgao_votings_tool(
    orgao_id: int,
    id_proposicao: Optional[int] = None,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "DESC",
    ordenar_por: str = "dataHoraRegistro"
) -> str:
    """Retorna as votações ocorridas em um determinado órgão ou comissão.

    Args:
        orgao_id: Identificador numérico do órgão.
        id_proposicao: ID da proposição legislativa votada.
        data_inicio: Data de início (AAAA-MM-DD).
        data_fim: Data de término (AAAA-MM-DD).
        pagina: Página de resultados.
        itens: Quantidade de itens.
        ordem: Ordenação.
        ordenar_por: Campo de ordenação.
    """
    data = await get_orgao_votings(
        orgao_id=orgao_id,
        idProposicao=id_proposicao,
        dataInicio=data_inicio,
        dataFim=data_fim,
        pagina=pagina,
        itens=itens,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)

import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.partidos.partidos_api import (
    get_partidos,
    get_partido_details,
    get_partido_lideres,
    get_partido_membros,
)
from src.api.blocos.blocos_api import (
    get_blocos,
    get_bloco_details,
    get_bloco_partidos,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_partidos_tool(
    sigla: Optional[str] = None,
    id_legislatura: Optional[int] = None,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "ASC",
    ordenar_por: str = "sigla"
) -> str:
    """Consulta e lista partidos políticos com deputados em exercício na Câmara.

    Args:
        sigla: Sigla do partido (ex.: "PL", "PT", "MDB", "UNIÃO").
        id_legislatura: ID da legislatura.
        data_inicio: Data inicial (AAAA-MM-DD).
        data_fim: Data final (AAAA-MM-DD).
        pagina: Número da página (padrão: 1).
        itens: Quantidade de itens (máximo: 100, padrão: 15).
        ordem: Ordenação ("ASC" ou "DESC").
        ordenar_por: Campo de ordenação ("sigla", "nome", "id").
    """
    data = await get_partidos(
        sigla=sigla,
        idLegislatura=id_legislatura,
        dataInicio=data_inicio,
        dataFim=data_fim,
        pagina=pagina,
        itens=itens,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)


@mcp.tool()
async def get_partido_details_tool(partido_id: int) -> str:
    """Retorna detalhes cadastrais, status e informações completas de um partido político.

    Args:
        partido_id: Identificador numérico do partido (ex.: 36898).
    """
    data = await get_partido_details(partido_id=partido_id)
    return _json_response(data)


@mcp.tool()
async def get_partido_lideres_tool(partido_id: int, pagina: int = 1, itens: int = 15) -> str:
    """Retorna a lista de deputados que são ou foram líderes de um partido político.

    Args:
        partido_id: Identificador numérico do partido.
        pagina: Página de resultados.
        itens: Quantidade de itens.
    """
    data = await get_partido_lideres(partido_id=partido_id, pagina=pagina, itens=itens)
    return _json_response(data)


@mcp.tool()
async def get_partido_membros_tool(
    partido_id: int,
    id_legislatura: Optional[int] = None,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "ASC",
    ordenar_por: str = "nome"
) -> str:
    """Retorna a lista de deputados filiados ao partido em determinado período ou legislatura.

    Args:
        partido_id: Identificador numérico do partido.
        id_legislatura: ID da legislatura.
        data_inicio: Data inicial (AAAA-MM-DD).
        data_fim: Data final (AAAA-MM-DD).
        pagina: Página de resultados.
        itens: Quantidade de itens.
        ordem: Ordenação.
        ordenar_por: Campo de ordenação ("nome", "idLegislatura").
    """
    data = await get_partido_membros(
        partido_id=partido_id,
        idLegislatura=id_legislatura,
        dataInicio=data_inicio,
        dataFim=data_fim,
        pagina=pagina,
        itens=itens,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)


@mcp.tool()
async def get_blocos_tool(
    id_legislatura: Optional[int] = None,
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "ASC",
    ordenar_por: str = "nome"
) -> str:
    """Consulta e lista os blocos partidários formados na Câmara dos Deputados.

    Args:
        id_legislatura: ID da legislatura (ex.: 57).
        pagina: Página de resultados.
        itens: Quantidade de itens por página.
        ordem: Ordenação ("ASC" ou "DESC").
        ordenar_por: Campo de ordenação ("nome", "id", "idLegislatura").
    """
    data = await get_blocos(
        idLegislatura=id_legislatura,
        pagina=pagina,
        itens=itens,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)


@mcp.tool()
async def get_bloco_details_tool(bloco_id: int) -> str:
    """Retorna informações detalhadas sobre um bloco partidário específico.

    Args:
        bloco_id: Identificador numérico do bloco partidário (ex.: 582).
    """
    data = await get_bloco_details(bloco_id=bloco_id)
    return _json_response(data)


@mcp.tool()
async def get_bloco_partidos_tool(bloco_id: int, data: Optional[str] = None) -> str:
    """Retorna os partidos políticos integrantes de um bloco partidário em uma data (AAAA-MM-DDTHH:mm) ou atualmente.

    Args:
        bloco_id: Identificador numérico do bloco partidário.
        data: Data e hora no formato AAAA-MM-DDTHH:mm (opcional).
    """
    data_res = await get_bloco_partidos(bloco_id=bloco_id, data=data)
    return _json_response(data_res)

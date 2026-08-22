import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.frentes.frentes_api import (
    get_frentes,
    get_frente_details,
    get_frente_membros,
)
from src.api.grupos.grupos_api import (
    get_grupos,
    get_grupo_details,
    get_grupo_historico,
    get_grupo_membros,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_frentes_tool(
    id_legislatura: Optional[int] = None,
    pagina: int = 1,
    itens: int = 15
) -> str:
    """Consulta e lista frentes parlamentares registradas na Câmara dos Deputados.

    Args:
        id_legislatura: ID da legislatura (ex.: 57).
        pagina: Página de resultados (padrão: 1).
        itens: Quantidade de itens por página (máximo: 100, padrão: 15).
    """
    data = await get_frentes(idLegislatura=id_legislatura, pagina=pagina, itens=itens)
    return _json_response(data)


@mcp.tool()
async def get_frente_details_tool(frente_id: int) -> str:
    """Retorna dados detalhados, coordenador e documento de criação de uma frente parlamentar.

    Args:
        frente_id: Identificador numérico da frente parlamentar (ex.: 54000).
    """
    data = await get_frente_details(frente_id=frente_id)
    return _json_response(data)


@mcp.tool()
async def get_frente_membros_tool(frente_id: int) -> str:
    """Retorna os deputados signatários e participantes de uma frente parlamentar.

    Args:
        frente_id: Identificador numérico da frente parlamentar.
    """
    data = await get_frente_membros(frente_id=frente_id)
    return _json_response(data)


@mcp.tool()
async def get_grupos_tool(
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "ASC",
    ordenar_por: str = "id"
) -> str:
    """Consulta e lista os grupos parlamentares de cooperação internacional e amizade entre países.

    Args:
        pagina: Página de resultados.
        itens: Itens por página.
        ordem: Ordenação ("ASC" ou "DESC").
        ordenar_por: Campo de ordenação ("id").
    """
    data = await get_grupos(pagina=pagina, itens=itens, ordem=ordem, ordenarPor=ordenar_por)
    return _json_response(data)


@mcp.tool()
async def get_grupo_details_tool(grupo_id: int) -> str:
    """Retorna detalhes sobre um grupo parlamentar interparlamentar específico.

    Args:
        grupo_id: Identificador numérico do grupo (ex.: 10).
    """
    data = await get_grupo_details(grupo_id=grupo_id)
    return _json_response(data)


@mcp.tool()
async def get_grupo_historico_tool(grupo_id: int) -> str:
    """Retorna o histórico de alterações e variações de estado de um grupo parlamentar ao longo do tempo.

    Args:
        grupo_id: Identificador numérico do grupo.
    """
    data = await get_grupo_historico(grupo_id=grupo_id)
    return _json_response(data)


@mcp.tool()
async def get_grupo_membros_tool(
    grupo_id: int,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    ordem: str = "ASC",
    ordenar_por: str = "id"
) -> str:
    """Retorna a lista de parlamentares integrantes de um grupo interparlamentar.

    Args:
        grupo_id: Identificador numérico do grupo.
        data_inicio: Data de início (AAAA-MM-DD).
        data_fim: Data de término (AAAA-MM-DD).
        ordem: Ordenação.
        ordenar_por: Campo de ordenação.
    """
    data = await get_grupo_membros(
        grupo_id=grupo_id,
        dataInicio=data_inicio,
        dataFim=data_fim,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)

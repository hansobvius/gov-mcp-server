import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.votacoes.votacoes_api import (
    get_votacoes,
    get_votacao_details,
    get_votacao_orientacoes,
    get_votacao_votos,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_votacoes_tool(
    id_proposicao: Optional[int] = None,
    id_evento: Optional[int] = None,
    id_orgao: Optional[int] = None,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "DESC",
    ordenar_por: str = "dataHoraRegistro"
) -> str:
    """Consulta e lista votações realizadas na Câmara dos Deputados.

    Args:
        id_proposicao: ID da proposição votada.
        id_evento: ID do evento ou sessão em que ocorreu a votação.
        id_orgao: ID do órgão (comissão ou plenário) onde ocorreu a votação.
        data_inicio: Data de início do período (AAAA-MM-DD).
        data_fim: Data de término do período (AAAA-MM-DD).
        pagina: Página de resultados (padrão: 1).
        itens: Quantidade de itens por página (máximo: 100, padrão: 15).
        ordem: Ordenação ("ASC" ou "DESC").
        ordenar_por: Campo de ordenação ("dataHoraRegistro").
    """
    data = await get_votacoes(
        idProposicao=id_proposicao,
        idEvento=id_evento,
        idOrgao=id_orgao,
        dataInicio=data_inicio,
        dataFim=data_fim,
        pagina=pagina,
        itens=itens,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)


@mcp.tool()
async def get_votacao_details_tool(votacao_id: str) -> str:
    """Retorna detalhes completos, ementa e resultado de uma votação específica.

    Args:
        votacao_id: Identificador único da votação (ex.: "2415840-52" ou string ID de votação).
    """
    data = await get_votacao_details(votacao_id=votacao_id)
    return _json_response(data)


@mcp.tool()
async def get_votacao_orientacoes_tool(votacao_id: str) -> str:
    """Retorna as orientações de voto emitidas pelas bancadas e lideranças partidárias para a votação.

    Args:
        votacao_id: Identificador único da votação.
    """
    data = await get_votacao_orientacoes(votacao_id=votacao_id)
    return _json_response(data)


@mcp.tool()
async def get_votacao_votos_tool(votacao_id: str) -> str:
    """Retorna o voto nominal de cada parlamentar (Sim, Não, Abstenção, Obstrução) em uma votação aberta.

    Args:
        votacao_id: Identificador único da votação.
    """
    data = await get_votacao_votos(votacao_id=votacao_id)
    return _json_response(data)

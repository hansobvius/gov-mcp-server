import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.eventos.eventos_api import (
    get_eventos,
    get_evento_details,
    get_evento_deputados,
    get_evento_orgaos,
    get_evento_pauta,
    get_evento_votacoes,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_eventos_tool(
    cod_tipo_evento: Optional[int] = None,
    cod_situacao: Optional[int] = None,
    id_orgao: Optional[int] = None,
    cod_tipo_orgao: Optional[int] = None,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    hora_inicio: Optional[str] = None,
    hora_fim: Optional[str] = None,
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "ASC",
    ordenar_por: str = "dataHoraInicio"
) -> str:
    """Consulta e lista eventos ocorridos ou previstos nos órgãos e comissões da Câmara.

    Args:
        cod_tipo_evento: Código do tipo de evento (reunião deliberativa, audiência pública, etc.).
        cod_situacao: Código da situação do evento (convocada, realizada, cancelada).
        id_orgao: Identificador numérico do órgão organizador.
        cod_tipo_orgao: Código do tipo do órgão organizador.
        data_inicio: Data de início (AAAA-MM-DD).
        data_fim: Data de término (AAAA-MM-DD).
        hora_inicio: Hora de início (HH:MM).
        hora_fim: Hora de término (HH:MM).
        pagina: Página de resultados (padrão: 1).
        itens: Quantidade de itens por página (máximo: 100, padrão: 15).
        ordem: Ordenação ("ASC" ou "DESC").
        ordenar_por: Campo de ordenação ("dataHoraInicio", "id", "titulo").
    """
    data = await get_eventos(
        codTipoEvento=cod_tipo_evento,
        codSituacao=cod_situacao,
        idOrgao=id_orgao,
        codTipoOrgao=cod_tipo_orgao,
        dataInicio=data_inicio,
        dataFim=data_fim,
        horaInicio=hora_inicio,
        horaFim=hora_fim,
        pagina=pagina,
        itens=itens,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)


@mcp.tool()
async def get_evento_details_tool(evento_id: int) -> str:
    """Retorna informações detalhadas sobre um evento específico (pauta, local, horário).

    Args:
        evento_id: Identificador numérico do evento na Câmara (ex.: 72345).
    """
    data = await get_evento_details(evento_id=evento_id)
    return _json_response(data)


@mcp.tool()
async def get_evento_deputados_tool(evento_id: int) -> str:
    """Retorna os deputados participantes ou convidados para um evento.

    Args:
        evento_id: Identificador numérico do evento.
    """
    data = await get_evento_deputados(evento_id=evento_id)
    return _json_response(data)


@mcp.tool()
async def get_evento_orgaos_tool(evento_id: int) -> str:
    """Retorna a lista de órgãos organizadores responsáveis pelo evento.

    Args:
        evento_id: Identificador numérico do evento.
    """
    data = await get_evento_orgaos(evento_id=evento_id)
    return _json_response(data)


@mcp.tool()
async def get_evento_pauta_tool(evento_id: int) -> str:
    """Retorna a lista de proposições pautadas para deliberação no evento.

    Args:
        evento_id: Identificador numérico do evento.
    """
    data = await get_evento_pauta(evento_id=evento_id)
    return _json_response(data)


@mcp.tool()
async def get_evento_votacoes_tool(evento_id: int) -> str:
    """Retorna detalhes de votações ocorridas em um evento específico.

    Args:
        evento_id: Identificador numérico do evento.
    """
    data = await get_evento_votacoes(evento_id=evento_id)
    return _json_response(data)

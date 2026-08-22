import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.referencias.referencias_api import (
    get_referencias_deputados,
    get_referencias_situacoes_deputado,
    get_referencias_tipos_profissao,
    get_referencias_ufs,
    get_referencias_tipos_despesa,
    get_referencias_eventos,
    get_referencias_situacoes_evento,
    get_referencias_tipos_evento,
    get_referencias_orgaos,
    get_referencias_situacoes_orgao,
    get_referencias_tipos_orgao,
    get_referencias_proposicoes,
    get_referencias_situacoes_proposicao,
    get_referencias_temas_proposicao,
    get_referencias_tipos_autor,
    get_referencias_tipos_tramitacao,
    get_referencias_tipos_proposicao,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_referencias_ufs_tool() -> str:
    """Retorna a lista oficial de siglas e nomes das Unidades da Federação (estados e DF)."""
    data = await get_referencias_ufs()
    return _json_response(data)


@mcp.tool()
async def get_referencias_deputados_tool() -> str:
    """Retorna os valores válidos e metadados para busca de deputados."""
    data = await get_referencias_deputados()
    return _json_response(data)


@mcp.tool()
async def get_referencias_situacoes_deputado_tool() -> str:
    """Retorna os códigos e descrições das situações de exercício parlamentar de um deputado."""
    data = await get_referencias_situacoes_deputado()
    return _json_response(data)


@mcp.tool()
async def get_referencias_tipos_profissao_tool() -> str:
    """Retorna os códigos e títulos de atividades profissionais catalogadas na Câmara."""
    data = await get_referencias_tipos_profissao()
    return _json_response(data)


@mcp.tool()
async def get_referencias_tipos_despesa_tool() -> str:
    """Retorna os tipos de despesas reembolsáveis pela cota parlamentar (CEAP)."""
    data = await get_referencias_tipos_despesa()
    return _json_response(data)


@mcp.tool()
async def get_referencias_proposicoes_tool() -> str:
    """Retorna valores válidos para parâmetros do endpoint de proposições."""
    data = await get_referencias_proposicoes()
    return _json_response(data)


@mcp.tool()
async def get_referencias_tipos_proposicao_tool() -> str:
    """Retorna os tipos e siglas de proposições existentes (PL, PEC, MPV, REQ, etc.)."""
    data = await get_referencias_tipos_proposicao()
    return _json_response(data)


@mcp.tool()
async def get_referencias_situacoes_proposicao_tool() -> str:
    """Retorna os possíveis códigos e estados de situação de tramitação de uma proposição."""
    data = await get_referencias_situacoes_proposicao()
    return _json_response(data)


@mcp.tool()
async def get_referencias_temas_proposicao_tool() -> str:
    """Retorna as áreas temáticas e códigos associados às proposições (Economia, Saúde, Educação, etc.)."""
    data = await get_referencias_temas_proposicao()
    return _json_response(data)


@mcp.tool()
async def get_referencias_tipos_autor_tool() -> str:
    """Retorna os tipos de entidades e parlamentares que podem ser autores de proposições."""
    data = await get_referencias_tipos_autor()
    return _json_response(data)


@mcp.tool()
async def get_referencias_tipos_tramitacao_tool() -> str:
    """Retorna os tipos de tramitação e passos regimentais de proposições."""
    data = await get_referencias_tipos_tramitacao()
    return _json_response(data)


@mcp.tool()
async def get_referencias_eventos_tool() -> str:
    """Retorna valores válidos para parâmetros do endpoint de eventos."""
    data = await get_referencias_eventos()
    return _json_response(data)


@mcp.tool()
async def get_referencias_tipos_evento_tool() -> str:
    """Retorna os tipos de eventos legislativos realizados na Câmara."""
    data = await get_referencias_tipos_evento()
    return _json_response(data)


@mcp.tool()
async def get_referencias_situacoes_evento_tool() -> str:
    """Retorna os códigos e descrições das situações de eventos (Convocada, Realizada, Cancelada)."""
    data = await get_referencias_situacoes_evento()
    return _json_response(data)


@mcp.tool()
async def get_referencias_orgaos_tool() -> str:
    """Retorna valores válidos para parâmetros do endpoint de órgãos."""
    data = await get_referencias_orgaos()
    return _json_response(data)


@mcp.tool()
async def get_referencias_tipos_orgao_tool() -> str:
    """Retorna os tipos de órgãos que existem na estrutura da Câmara dos Deputados."""
    data = await get_referencias_tipos_orgao()
    return _json_response(data)


@mcp.tool()
async def get_referencias_situacoes_orgao_tool() -> str:
    """Retorna as possíveis situações em que órgãos da Câmara podem se encontrar (Em funcionamento, Extinta)."""
    data = await get_referencias_situacoes_orgao()
    return _json_response(data)

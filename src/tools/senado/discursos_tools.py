import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.senado.discursos_api import (
    get_senador_discursos,
    get_senador_apartes,
    get_discurso_texto_integral,
    get_plenario_discursos_periodo,
    get_taquigrafia_notas,
    get_taquigrafia_videos,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_senador_discursos_tool(codigo: int) -> str:
    """Lista todos os discursos e pronunciamentos oficiais proferidos por um senador.

    Args:
        codigo: Código numérico identificador do senador.
    """
    res = await get_senador_discursos(codigo=codigo)
    return _json_response(res)


@mcp.tool()
async def get_senador_apartes_tool(codigo: int) -> str:
    """Lista intervenções e apartes concedidos e realizados por um senador em plenário.

    Args:
        codigo: Código numérico identificador do senador.
    """
    res = await get_senador_apartes(codigo=codigo)
    return _json_response(res)


@mcp.tool()
async def get_discurso_texto_integral_tool(codigo_pronunciamento: int) -> str:
    """Obtém o conteúdo textual integral e transcrito de um pronunciamento no Senado.

    Args:
        codigo_pronunciamento: Código numérico identificador do pronunciamento.
    """
    res = await get_discurso_texto_integral(codigo_pronunciamento=codigo_pronunciamento)
    return _json_response(res)


@mcp.tool()
async def get_plenario_discursos_periodo_tool(data_inicio: str, data_fim: str) -> str:
    """Lista os pronunciamentos em plenário realizados por todos os parlamentares em um intervalo de datas.

    Args:
        data_inicio: Data de início (AAAA-MM-DD).
        data_fim: Data de término (AAAA-MM-DD).
    """
    res = await get_plenario_discursos_periodo(data_inicio=data_inicio, data_fim=data_fim)
    return _json_response(res)


@mcp.tool()
async def get_taquigrafia_notas_tool(
    id_origem: int,
    tipo: str = "sessao"
) -> str:
    """Obtém as notas e transcrições taquigráficas oficiais de uma sessão ou reunião.

    Args:
        id_origem: Identificador numérico da sessão ou reunião.
        tipo: Tipo da origem ('sessao' ou 'reuniao'). Padrão: 'sessao'.
    """
    res = await get_taquigrafia_notas(id_origem=id_origem, tipo=tipo)
    return _json_response(res)


@mcp.tool()
async def get_taquigrafia_videos_tool(
    id_origem: int,
    tipo: str = "sessao"
) -> str:
    """Obtém os índices, minutagem e referências dos vídeos gravados de uma sessão ou reunião.

    Args:
        id_origem: Identificador numérico da sessão ou reunião.
        tipo: Tipo da origem ('sessao' ou 'reuniao'). Padrão: 'sessao'.
    """
    res = await get_taquigrafia_videos(id_origem=id_origem, tipo=tipo)
    return _json_response(res)

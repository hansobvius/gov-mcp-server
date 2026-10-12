import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.senado.composicao_api import (
    get_composicao_mesa_sf,
    get_composicao_mesa_cn,
    get_liderancas_tipos,
    get_liderancas_tipos_unidade,
    get_liderancas,
    get_partidos_senado,
    get_blocos_senado,
    get_bloco_senado_detalhes,
    get_composicao_comissao,
    get_composicao_comissao_mista_atual,
    get_composicao_comissao_mista_historica,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_composicao_mesa_sf_tool() -> str:
    """Obtém os membros da Mesa Diretora do Senado Federal (Presidente, Vice-Presidentes e Secretários)."""
    data = await get_composicao_mesa_sf()
    return _json_response(data)


@mcp.tool()
async def get_composicao_mesa_cn_tool() -> str:
    """Obtém os membros da Mesa Diretora do Congresso Nacional."""
    data = await get_composicao_mesa_cn()
    return _json_response(data)


@mcp.tool()
async def get_liderancas_tool() -> str:
    """Obtém as lideranças partidárias, de blocos e de governo em exercício no Senado e Congresso."""
    data = await get_liderancas()
    return _json_response(data)


@mcp.tool()
async def get_liderancas_tipos_tool() -> str:
    """Lista as definições e tipos de lideranças do Congresso e Senado."""
    data = await get_liderancas_tipos()
    return _json_response(data)


@mcp.tool()
async def get_partidos_senado_tool() -> str:
    """Lista os partidos políticos com representação no Senado Federal (em atividade ou extintos)."""
    data = await get_partidos_senado()
    return _json_response(data)


@mcp.tool()
async def get_blocos_senado_tool() -> str:
    """Lista os blocos partidários atualmente formados no Senado Federal."""
    data = await get_blocos_senado()
    return _json_response(data)


@mcp.tool()
async def get_bloco_senado_detalhes_tool(codigo: int) -> str:
    """Obtém detalhes de um bloco parlamentar do Senado e a lista de senadores integrantes.

    Args:
        codigo: Código numérico identificador do bloco.
    """
    data = await get_bloco_senado_detalhes(codigo=codigo)
    return _json_response(data)


@mcp.tool()
async def get_composicao_comissao_tool(codigo: Union[int, str]) -> str:
    """Obtém a composição atual de uma comissão do Senado com titulares, suplentes e cargos.

    Args:
        codigo: Código ou sigla da comissão (ex.: 'CCJ', 'CAE').
    """
    data = await get_composicao_comissao(codigo=codigo)
    return _json_response(data)


@mcp.tool()
async def get_composicao_comissao_mista_atual_tool(codigo: Union[int, str]) -> str:
    """Obtém a lista de senadores e deputados vinculados atualmente a uma comissão mista do Congresso.

    Args:
        codigo: Código identificador da comissão mista.
    """
    data = await get_composicao_comissao_mista_atual(codigo=codigo)
    return _json_response(data)


@mcp.tool()
async def get_composicao_comissao_mista_historica_tool(
    codigo: Union[int, str],
    data_inicio: str,
    data_fim: str
) -> str:
    """Obtém a composição histórica resumida de uma comissão mista em um intervalo de datas.

    Args:
        codigo: Código da comissão mista.
        data_inicio: Data de início (AAAA-MM-DD).
        data_fim: Data de término (AAAA-MM-DD).
    """
    data = await get_composicao_comissao_mista_historica(
        codigo=codigo,
        data_inicio=data_inicio,
        data_fim=data_fim
    )
    return _json_response(data)

import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.senado.senadores_api import (
    get_senadores_atuais,
    get_senadores_afastados,
    get_senadores_legislatura,
    get_senador_detalhes,
    get_senador_cargos,
    get_senador_comissoes,
    get_senador_filiacoes,
    get_senador_historico_academico,
    get_senador_licencas,
    get_senador_mandatos,
    get_senador_profissoes,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_senadores_atuais_tool() -> str:
    """Obtém a lista de senadores em exercício no Senado Federal com dados de contato, partido e UF."""
    data = await get_senadores_atuais()
    return _json_response(data)


@mcp.tool()
async def get_senadores_afastados_tool() -> str:
    """Obtém a lista de senadores atualmente afastados do exercício do mandato e o respectivo motivo."""
    data = await get_senadores_afastados()
    return _json_response(data)


@mcp.tool()
async def get_senadores_legislatura_tool(
    legislatura: int,
    legislatura_fim: Optional[int] = None
) -> str:
    """Lista senadores que atuaram em uma determinada legislatura ou intervalo de legislaturas.

    Args:
        legislatura: Número da legislatura inicial (ex.: 57 para o período 2023-2027).
        legislatura_fim: Número da legislatura final para consulta por intervalo (opcional).
    """
    data = await get_senadores_legislatura(legislatura=legislatura, legislatura_fim=legislatura_fim)
    return _json_response(data)


@mcp.tool()
async def get_senador_detalhes_tool(codigo: int) -> str:
    """Obtém a ficha completa de dados cadastrais, biografia e mandato de um senador.

    Args:
        codigo: Código numérico de identificação do senador (ex.: 5988).
    """
    data = await get_senador_detalhes(codigo=codigo)
    return _json_response(data)


@mcp.tool()
async def get_senador_cargos_tool(codigo: int) -> str:
    """Lista todos os cargos ocupados por um senador em comissões, mesas e colegiados.

    Args:
        codigo: Código numérico de identificação do senador.
    """
    data = await get_senador_cargos(codigo=codigo)
    return _json_response(data)


@mcp.tool()
async def get_senador_comissoes_tool(codigo: int) -> str:
    """Lista as comissões e colegiados dos quais o senador é ou já foi integrante.

    Args:
        codigo: Código numérico de identificação do senador.
    """
    data = await get_senador_comissoes(codigo=codigo)
    return _json_response(data)


@mcp.tool()
async def get_senador_filiacoes_tool(codigo: int) -> str:
    """Consulta o histórico de filiações partidárias do senador ao longo da carreira política.

    Args:
        codigo: Código numérico de identificação do senador.
    """
    data = await get_senador_filiacoes(codigo=codigo)
    return _json_response(data)


@mcp.tool()
async def get_senador_historico_academico_tool(codigo: int) -> str:
    """Consulta os cursos, graduações e formação acadêmica declarada pelo senador.

    Args:
        codigo: Código numérico de identificação do senador.
    """
    data = await get_senador_historico_academico(codigo=codigo)
    return _json_response(data)


@mcp.tool()
async def get_senador_licencas_tool(codigo: int) -> str:
    """Lista as licenças médicas, particulares ou de interesse pessoal solicitadas pelo senador.

    Args:
        codigo: Código numérico de identificação do senador.
    """
    data = await get_senador_licencas(codigo=codigo)
    return _json_response(data)


@mcp.tool()
async def get_senador_mandatos_tool(codigo: int) -> str:
    """Lista mandatos e períodos de exercício parlamentar e suplências do senador.

    Args:
        codigo: Código numérico de identificação do senador.
    """
    data = await get_senador_mandatos(codigo=codigo)
    return _json_response(data)


@mcp.tool()
async def get_senador_profissoes_tool(codigo: int) -> str:
    """Lista as profissões declaradas pelo senador no cadastro legislativo.

    Args:
        codigo: Código numérico de identificação do senador.
    """
    data = await get_senador_profissoes(codigo=codigo)
    return _json_response(data)

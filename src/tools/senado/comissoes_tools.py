import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.senado.comissoes_api import (
    get_comissoes_tipos_colegiado,
    get_comissoes_por_tipo,
    get_colegiados_atividade,
    get_comissoes_mistas,
    get_comissao_detalhes,
    get_comissao_agenda,
    get_comissao_cpi_requerimentos,
    get_comissao_reuniao_detalhes,
    get_comissao_documento_ultima_reuniao,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_comissoes_tipos_colegiado_tool() -> str:
    """Lista os tipos de colegiado e comissões existentes no Senado Federal e Congresso Nacional."""
    data = await get_comissoes_tipos_colegiado()
    return _json_response(data)


@mcp.tool()
async def get_comissoes_por_tipo_tool(tipo: str) -> str:
    """Lista comissões e colegiados do Senado Federal filtrados por tipo.

    Args:
        tipo: Tipo do colegiado (ex.: 'Permanente', 'Temporaria').
    """
    data = await get_comissoes_por_tipo(tipo=tipo)
    return _json_response(data)


@mcp.tool()
async def get_colegiados_atividade_tool() -> str:
    """Obtém a lista geral de todas as comissões e colegiados atualmente em atividade no Congresso Nacional."""
    data = await get_colegiados_atividade()
    return _json_response(data)


@mcp.tool()
async def get_comissoes_mistas_tool() -> str:
    """Lista as Comissões Mistas atuais constituídas no Congresso Nacional (Senado e Câmara)."""
    data = await get_comissoes_mistas()
    return _json_response(data)


@mcp.tool()
async def get_comissao_detalhes_tool(codigo: Union[int, str]) -> str:
    """Obtém informações detalhadas, competência, contato e finalidade de uma comissão do Senado.

    Args:
        codigo: Código numérico ou sigla da comissão (ex.: 'CCJ', 'CAE', 2003).
    """
    data = await get_comissao_detalhes(codigo=codigo)
    return _json_response(data)


@mcp.tool()
async def get_comissao_agenda_tool(
    data_referencia: Optional[str] = None,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    mes_referencia: Optional[str] = None
) -> str:
    """Consulta a agenda de reuniões e audiências de comissões do Senado por dia, período ou mês.

    Args:
        data_referencia: Data específica no formato AAAA-MM-DD.
        data_inicio: Data de início do período no formato AAAA-MM-DD.
        data_fim: Data de término do período no formato AAAA-MM-DD.
        mes_referencia: Mês de referência no formato AAAA-MM.
    """
    data = await get_comissao_agenda(
        data_referencia=data_referencia,
        data_inicio=data_inicio,
        data_fim=data_fim,
        mes_referencia=mes_referencia
    )
    return _json_response(data)


@mcp.tool()
async def get_comissao_cpi_requerimentos_tool(comissao: Union[int, str]) -> str:
    """Lista os requerimentos apresentados no âmbito de uma CPI (Comissão Parlamentar de Inquérito).

    Args:
        comissao: Sigla ou código da CPI (ex.: 'CPIPAND', 'CPICPMI').
    """
    data = await get_comissao_cpi_requerimentos(comissao=comissao)
    return _json_response(data)


@mcp.tool()
async def get_comissao_reuniao_detalhes_tool(codigo_reuniao: int) -> str:
    """Obtém os detalhes completos, pauta, horário e local de uma reunião de comissão.

    Args:
        codigo_reuniao: Identificador numérico da reunião.
    """
    data = await get_comissao_reuniao_detalhes(codigo_reuniao=codigo_reuniao)
    return _json_response(data)


@mcp.tool()
async def get_comissao_documento_ultima_reuniao_tool(sigla: str, tipo_documento: str) -> str:
    """Obtém o link direto para um documento da última reunião realizada por uma comissão.

    Args:
        sigla: Sigla da comissão (ex.: 'CCJ').
        tipo_documento: Tipo do documento desejado.
    """
    data = await get_comissao_documento_ultima_reuniao(sigla=sigla, tipo_documento=tipo_documento)
    return _json_response(data)

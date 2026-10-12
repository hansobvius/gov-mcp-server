import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.senado.plenario_api import (
    get_plenario_agenda_dia,
    get_plenario_agenda_mes,
    get_plenario_agenda_cn,
    get_plenario_encontro_detalhes,
    get_plenario_resultado,
    get_plenario_resultado_cn,
    get_plenario_resultado_veto,
    get_plenario_orientacao_bancada,
)
from src.api.senado.votacoes_api import (
    get_votacoes_nominais,
    get_votacao_comissao_materia,
    get_votacao_comissao_parlamentar,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_plenario_agenda_dia_tool(data: str) -> str:
    """Consulta a agenda do Plenário do Senado Federal para um dia específico.

    Args:
        data: Data da sessão no formato AAAA-MM-DD.
    """
    res = await get_plenario_agenda_dia(data=data)
    return _json_response(res)


@mcp.tool()
async def get_plenario_agenda_cn_tool(data: str) -> str:
    """Consulta a agenda do Plenário do Congresso Nacional (sessão conjunta SF e CD) para um dia específico.

    Args:
        data: Data da sessão no formato AAAA-MM-DD.
    """
    res = await get_plenario_agenda_cn(data=data)
    return _json_response(res)


@mcp.tool()
async def get_plenario_encontro_detalhes_tool(
    codigo: int,
    subrecurso: Optional[str] = None
) -> str:
    """Obtém detalhes, pauta, resultado ou resumo de uma sessão plenária (encontro) do Senado.

    Args:
        codigo: Código numérico identificador do encontro/sessão.
        subrecurso: Sub-recurso opcional ('pauta', 'resultado', 'resumo').
    """
    res = await get_plenario_encontro_detalhes(codigo=codigo, subrecurso=subrecurso)
    return _json_response(res)


@mcp.tool()
async def get_plenario_resultado_tool(data: str) -> str:
    """Obtém os resultados consolidados das deliberações da Sessão Plenária do Senado por data.

    Args:
        data: Data da sessão (AAAA-MM-DD).
    """
    res = await get_plenario_resultado(data=data)
    return _json_response(res)


@mcp.tool()
async def get_plenario_resultado_veto_tool(
    codigo: int,
    tipo: str = "veto"
) -> str:
    """Obtém a apuração e resultado de votação nominal sobre Vetos Presidenciais no Congresso Nacional.

    Args:
        codigo: Código identificador numérico.
        tipo: Tipo da consulta ('veto', 'dispositivo', 'materia'). Padrão: 'veto'.
    """
    res = await get_plenario_resultado_veto(codigo=codigo, tipo=tipo)
    return _json_response(res)


@mcp.tool()
async def get_plenario_orientacao_bancada_tool(
    data_sessao: str,
    data_fim: Optional[str] = None
) -> str:
    """Obtém a orientação de bancada e lideranças partidárias para votações em plenário.

    Args:
        data_sessao: Data da sessão (AAAA-MM-DD).
        data_fim: Data de término para pesquisa por período (opcional).
    """
    res = await get_plenario_orientacao_bancada(data_sessao=data_sessao, data_fim=data_fim)
    return _json_response(res)


@mcp.tool()
async def get_votacoes_nominais_senado_tool(
    id_sessao: Optional[int] = None,
    codigo_materia: Optional[int] = None,
    codigo_parlamentar: Optional[int] = None,
    sigla_partido: Optional[str] = None
) -> str:
    """Consulta votos nominais individuais de senadores registrados no painel eletrônico do Plenário.

    Args:
        id_sessao: Identificador da sessão plenária.
        codigo_materia: Código da matéria votada.
        codigo_parlamentar: Código do senador.
        sigla_partido: Sigla do partido político.
    """
    res = await get_votacoes_nominais(
        id_sessao=id_sessao,
        codigo_materia=codigo_materia,
        codigo_parlamentar=codigo_parlamentar,
        sigla_partido=sigla_partido
    )
    return _json_response(res)


@mcp.tool()
async def get_votacao_comissao_materia_tool(
    sigla: str,
    numero: int,
    ano: int
) -> str:
    """Consulta o resultado de votações conclusivas de matérias deliberadas no âmbito das comissões.

    Args:
        sigla: Sigla do tipo de proposição (ex.: 'PL', 'PDL').
        numero: Número da matéria.
        ano: Ano da matéria.
    """
    res = await get_votacao_comissao_materia(sigla=sigla, numero=numero, ano=ano)
    return _json_response(res)


@mcp.tool()
async def get_votacao_comissao_parlamentar_tool(codigo_parlamentar: int) -> str:
    """Consulta os votos proferidos por um parlamentar específico nas reuniões de comissões.

    Args:
        codigo_parlamentar: Código identificador do parlamentar.
    """
    res = await get_votacao_comissao_parlamentar(codigo_parlamentar=codigo_parlamentar)
    return _json_response(res)

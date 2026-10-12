import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.senado.processos_api import (
    get_processos,
    get_processo_detalhes,
    get_processo_documentos,
    get_processo_emendas,
    get_processo_referencias,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_processos_senado_tool(
    sigla: Optional[str] = None,
    numero: Optional[int] = None,
    ano: Optional[int] = None,
    autor: Optional[str] = None,
    tipo_autor: Optional[str] = None,
    situacao: Optional[str] = None,
    assunto: Optional[str] = None,
    classe: Optional[str] = None,
    itens: Optional[int] = 20
) -> str:
    """Pesquisa e lista processos legislativos no Senado Federal (rotas modernas /processo/).

    Args:
        sigla: Sigla da proposição/processo (ex.: 'PL', 'PEC', 'PDL', 'PLS').
        numero: Número da matéria legislativa.
        ano: Ano de apresentação da matéria.
        autor: Nome do autor ou parlamentar.
        tipo_autor: Tipo de autor (ex.: Senador, Deputado, Comissão).
        situacao: Situação atual de tramitação.
        assunto: Termo temático ou assunto de busca.
        classe: Classe processual da matéria.
        itens: Quantidade de itens retornados (padrão: 20).
    """
    data = await get_processos(
        sigla=sigla,
        numero=numero,
        ano=ano,
        autor=autor,
        tipo_autor=tipo_autor,
        situacao=situacao,
        assunto=assunto,
        classe=classe,
        itens=itens
    )
    return _json_response(data)


@mcp.tool()
async def get_processo_detalhes_senado_tool(processo_id: int) -> str:
    """Obtém detalhes completos de um processo legislativo do Senado (ementa, autores, relatorias, tramitações).

    Args:
        processo_id: Identificador numérico do processo (ex.: 158932).
    """
    data = await get_processo_detalhes(processo_id=processo_id)
    return _json_response(data)


@mcp.tool()
async def get_processo_documentos_senado_tool(
    processo_id: Optional[int] = None,
    tipo_documento: Optional[str] = None
) -> str:
    """Lista documentos oficiais (pareceres, relatórios, textos originais) vinculados a processos legislativos.

    Args:
        processo_id: Identificador numérico do processo.
        tipo_documento: Tipo específico do documento (opcional).
    """
    data = await get_processo_documentos(processo_id=processo_id, tipo_documento=tipo_documento)
    return _json_response(data)


@mcp.tool()
async def get_processo_emendas_senado_tool(
    processo_id: Optional[int] = None,
    autor: Optional[str] = None
) -> str:
    """Lista emendas apresentadas por parlamentares a processos legislativos no Senado.

    Args:
        processo_id: Identificador numérico do processo.
        autor: Nome ou identificação do parlamentar autor da emenda.
    """
    data = await get_processo_emendas(processo_id=processo_id, autor=autor)
    return _json_response(data)


@mcp.tool()
async def get_processo_referencias_senado_tool(tabela: str) -> str:
    """Consulta tabelas de domínio do processo legislativo do Senado.

    Args:
        tabela: Nome da tabela ('assuntos', 'classes', 'destinos', 'entes', 'siglas', 'tipos-autor', 'tipos-situacao', 'prazo/tipos').
    """
    data = await get_processo_referencias(tabela=tabela)
    return _json_response(data)

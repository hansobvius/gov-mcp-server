import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.senado.legislacao_api import (
    get_legislacao_lista,
    get_legislacao_detalhes,
    get_legislacao_tipos_norma,
    get_legislacao_termos,
    get_legislacao_classes,
)
from src.api.senado.orcamento_api import (
    get_orcamento_emendas,
    get_orcamento_oficios,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_legislacao_lista_senado_tool(
    tipo: Optional[str] = None,
    numero: Optional[int] = None,
    ano: Optional[int] = None,
    termo: Optional[str] = None
) -> str:
    """Pesquisa normas jurídicas federais brasileiras (leis, medidas provisórias, decretos, etc.).

    Args:
        tipo: Sigla do tipo da norma (ex.: 'LEI', 'LCP', 'DEC', 'MPV').
        numero: Número da norma jurídica.
        ano: Ano de publicação da norma.
        termo: Termo ou assunto para busca na ementa.
    """
    res = await get_legislacao_lista(tipo=tipo, numero=numero, ano=ano, termo=termo)
    return _json_response(res)


@mcp.tool()
async def get_legislacao_detalhes_senado_tool(codigo: Union[int, str]) -> str:
    """Obtém detalhes completos, ementa e texto integral de uma norma jurídica federal.

    Args:
        codigo: Código identificador numérico ou URN LexML da norma jurídica.
    """
    res = await get_legislacao_detalhes(codigo=codigo)
    return _json_response(res)


@mcp.tool()
async def get_legislacao_tipos_norma_tool() -> str:
    """Lista a tabela oficial de tipos de normas jurídicas catalogadas no Senado Federal."""
    res = await get_legislacao_tipos_norma()
    return _json_response(res)


@mcp.tool()
async def get_legislacao_termos_tool() -> str:
    """Lista o vocabulário controlado e termos de indexação jurídica utilizados na legislação."""
    res = await get_legislacao_termos()
    return _json_response(res)


@mcp.tool()
async def get_orcamento_emendas_senado_tool(
    ano: Optional[int] = None,
    autor: Optional[str] = None,
    tipo_emenda: Optional[str] = None
) -> str:
    """Consulta lotes de emendas parlamentares apresentadas ao Orçamento Geral da União (OGU).

    Args:
        ano: Ano orçamentário (ex.: 2024).
        autor: Nome do parlamentar ou comissão autora da emenda.
        tipo_emenda: Tipo da emenda (Individual, Bancada, Comissão).
    """
    res = await get_orcamento_emendas(ano=ano, autor=autor, tipo_emenda=tipo_emenda)
    return _json_response(res)


@mcp.tool()
async def get_orcamento_oficios_senado_tool(numero_sedol: Optional[str] = None) -> str:
    """Consulta ofícios de apoio e indicação de emendas orçamentárias (SEDOL).

    Args:
        numero_sedol: Número identificador SEDOL do ofício (opcional).
    """
    res = await get_orcamento_oficios(numero_sedol=numero_sedol)
    return _json_response(res)

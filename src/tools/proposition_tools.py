import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.propositions.propositions_api import (
    get_proposicoes,
    get_propositions_by_id,
    get_proposition_details,
    get_proposition_authors,
    get_proposition_related,
    get_proposition_themes,
    get_proposition_tramitations,
    get_proposition_votings,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_propositions_by_id_tools(proposition_id: str) -> str:
    """Busca proposições pelo ID de um deputado autor.

    Args:
        proposition_id: ID de um deputado (ex.: "220589").

    Returns:
        JSON string contendo os dados das proposições do deputado.
    """
    data = await get_propositions_by_id(proposition_id=proposition_id)
    return _json_response(data)


@mcp.tool()
async def get_propositions_tool(
    sigla_tipo: Optional[str] = None,
    numero: Optional[int] = None,
    ano: Optional[int] = None,
    autor: Optional[str] = None,
    id_deputado_autor: Optional[int] = None,
    sigla_partido_autor: Optional[str] = None,
    sigla_uf_autor: Optional[str] = None,
    keywords: Optional[str] = None,
    cod_situacao: Optional[int] = None,
    cod_tema: Optional[int] = None,
    data_apresentacao_inicio: Optional[str] = None,
    data_apresentacao_fim: Optional[str] = None,
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "DESC",
    ordenar_por: str = "ano"
) -> str:
    """Busca proposições legislativas (PL, PEC, MPV, etc.) por múltiplos filtros.

    Args:
        sigla_tipo: Tipo da proposição (ex.: "PL", "PEC", "MPV", "PLP").
        numero: Número da proposição (ex.: 1024).
        ano: Ano de apresentação da proposição (ex.: 2024).
        autor: Nome ou parte do nome do autor da proposição.
        id_deputado_autor: ID do deputado autor da proposição.
        sigla_partido_autor: Sigla do partido do autor (ex.: "PT", "PL").
        sigla_uf_autor: UF do autor (ex.: "SP", "RJ").
        keywords: Palavras-chave ou termos contidos na ementa.
        cod_situacao: Código da situação de tramitação da proposição.
        cod_tema: Código da área temática da proposição.
        data_apresentacao_inicio: Data inicial de apresentação (AAAA-MM-DD).
        data_apresentacao_fim: Data final de apresentação (AAAA-MM-DD).
        pagina: Número da página (padrão: 1).
        itens: Quantidade de itens por página (máximo: 100, padrão: 15).
        ordem: Sentido da ordenação ("ASC" ou "DESC").
        ordenar_por: Campo de ordenação ("id", "ano", "dataApresentacao").
    """
    data = await get_proposicoes(
        siglaTipo=sigla_tipo,
        numero=numero,
        ano=ano,
        autor=autor,
        idDeputadoAutor=id_deputado_autor,
        siglaPartidoAutor=sigla_partido_autor,
        siglaUfAutor=sigla_uf_autor,
        keywords=keywords,
        codSituacao=cod_situacao,
        codTema=cod_tema,
        dataApresentacaoInicio=data_apresentacao_inicio,
        dataApresentacaoFim=data_apresentacao_fim,
        pagina=pagina,
        itens=itens,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)


@mcp.tool()
async def get_proposition_details_tool(proposition_id: int) -> str:
    """Retorna informações detalhadas sobre uma proposição específica pelo seu ID.

    Args:
        proposition_id: ID numérico da proposição na Câmara (ex.: 2415840).
    """
    data = await get_proposition_details(proposition_id=proposition_id)
    return _json_response(data)


@mcp.tool()
async def get_proposition_authors_tool(proposition_id: int) -> str:
    """Lista autores e signatários de uma proposição legislativa.

    Args:
        proposition_id: ID numérico da proposição.
    """
    data = await get_proposition_authors(proposition_id=proposition_id)
    return _json_response(data)


@mcp.tool()
async def get_proposition_related_tool(proposition_id: int) -> str:
    """Lista proposições relacionadas ou apensadas a uma proposição específica.

    Args:
        proposition_id: ID numérico da proposição.
    """
    data = await get_proposition_related(proposition_id=proposition_id)
    return _json_response(data)


@mcp.tool()
async def get_proposition_themes_tool(proposition_id: int) -> str:
    """Lista as áreas temáticas associadas a uma proposição.

    Args:
        proposition_id: ID numérico da proposição.
    """
    data = await get_proposition_themes(proposition_id=proposition_id)
    return _json_response(data)


@mcp.tool()
async def get_proposition_tramitations_tool(
    proposition_id: int,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None
) -> str:
    """Retorna o histórico completo de tramitação e passos de uma proposta na Câmara.

    Args:
        proposition_id: ID numérico da proposição.
        data_inicio: Data de início (AAAA-MM-DD).
        data_fim: Data final (AAAA-MM-DD).
    """
    data = await get_proposition_tramitations(
        proposition_id=proposition_id,
        dataInicio=data_inicio,
        dataFim=data_fim
    )
    return _json_response(data)


@mcp.tool()
async def get_proposition_votings_tool(
    proposition_id: int,
    ordem: str = "DESC",
    ordenar_por: str = "dataHoraRegistro"
) -> str:
    """Retorna todas as votações que ocorreram para uma proposição específica.

    Args:
        proposition_id: ID numérico da proposição.
        ordem: Sentido da ordenação ("ASC" ou "DESC").
        ordenar_por: Campo de ordenação ("dataHoraRegistro").
    """
    data = await get_proposition_votings(
        proposition_id=proposition_id,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)

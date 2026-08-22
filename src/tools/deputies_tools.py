import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.deputies.deputies_api import (
    get_deputados,
    get_deputados_by_name,
    get_deputy_details,
    get_deputy_raw_details,
    get_deputy_expenses,
    get_deputy_speeches,
    get_deputy_events,
    get_deputy_fronts,
    get_deputy_history,
    get_deputy_external_mandates,
    get_deputy_occupations,
    get_deputy_organs,
    get_deputy_professions,
    get_legislature_leaders,
    get_legislature_board,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_deputies_by_names_tool(name: str) -> str:
    """Busca deputados pelo nome ou parte dele.

    Args:
        name: Nome ou fragmento do nome do deputado (ex.: "eduardo").

    Returns:
        JSON string contendo a lista de deputados encontrados e enriquecidos com detalhes.
    """
    data = await get_deputados_by_name(name=name)
    return _json_response(data)


@mcp.tool()
async def get_deputies_tool(
    nome: Optional[str] = None,
    id_legislatura: Optional[int] = None,
    sigla_uf: Optional[str] = None,
    sigla_partido: Optional[str] = None,
    sigla_sexo: Optional[str] = None,
    pagina: int = 1,
    itens: int = 15,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    ordem: str = "ASC",
    ordenar_por: str = "nome"
) -> str:
    """Busca e lista deputados federais segundo critérios de filtro (nome, partido, UF, etc.).

    Args:
        nome: Nome ou parte do nome parlamentar.
        id_legislatura: Identificador da legislatura (ex.: 57 para 2023-2027).
        sigla_uf: Sigla do estado (ex.: "SP", "RJ", "MG").
        sigla_partido: Sigla do partido político (ex.: "PL", "PT", "MDB").
        sigla_sexo: Sexo parlamentar ("M" ou "F").
        pagina: Número da página de resultados (padrão: 1).
        itens: Quantidade de itens por página (máximo: 100, padrão: 15).
        data_inicio: Data de início do exercício (AAAA-MM-DD).
        data_fim: Data de fim do exercício (AAAA-MM-DD).
        ordem: Ordenação dos resultados ("ASC" ou "DESC").
        ordenar_por: Campo de ordenação ("nome", "id", "siglaUf", "siglaPartido").
    """
    data = await get_deputados(
        nome=nome,
        idLegislatura=id_legislatura,
        siglaUf=sigla_uf,
        siglaPartido=sigla_partido,
        siglaSexo=sigla_sexo,
        pagina=pagina,
        itens=itens,
        dataInicio=data_inicio,
        dataFim=data_fim,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)


@mcp.tool()
async def get_deputy_details_tool(deputy_id: int) -> str:
    """Retorna os dados cadastrais completos e detalhados de um deputado específico pelo ID.

    Args:
        deputy_id: Identificador numérico do deputado (ex.: 220589).
    """
    data = await get_deputy_details(deputy_id=deputy_id)
    return _json_response(data)


@mcp.tool()
async def get_deputy_expenses_tool(
    deputy_id: int,
    ano: Optional[int] = None,
    mes: Optional[int] = None,
    id_legislatura: Optional[int] = None,
    cnpj_cpf_fornecedor: Optional[str] = None,
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "ASC",
    ordenar_por: str = "ano"
) -> str:
    """Consulta os gastos da Cota para Exercício da Atividade Parlamentar (CEAP) de um deputado.

    Args:
        deputy_id: Identificador numérico do deputado.
        ano: Ano de ocorrência da despesa (ex.: 2024).
        mes: Mês de ocorrência da despesa (1 a 12).
        id_legislatura: ID da legislatura.
        cnpj_cpf_fornecedor: CPF ou CNPJ do fornecedor beneficiário (apenas dígitos).
        pagina: Número da página (padrão: 1).
        itens: Itens por página (máximo: 100, padrão: 15).
        ordem: Sentido da ordenação ("ASC" ou "DESC").
        ordenar_por: Campo de ordenação (ex.: "ano", "mes", "valorDocumento").
    """
    data = await get_deputy_expenses(
        deputy_id=deputy_id,
        idLegislatura=id_legislatura,
        ano=ano,
        mes=mes,
        cnpjCpfFornecedor=cnpj_cpf_fornecedor,
        pagina=pagina,
        itens=itens,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)


@mcp.tool()
async def get_deputy_speeches_tool(
    deputy_id: int,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    id_legislatura: Optional[int] = None,
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "DESC",
    ordenar_por: str = "dataHoraInicio"
) -> str:
    """Consulta os pronunciamentos e discursos oficiais feitos por um deputado.

    Args:
        deputy_id: Identificador numérico do deputado.
        data_inicio: Data de início (AAAA-MM-DD).
        data_fim: Data de término (AAAA-MM-DD).
        id_legislatura: Número da legislatura.
        pagina: Página de resultados.
        itens: Quantidade de itens por página.
        ordem: Ordenação ("ASC" ou "DESC").
        ordenar_por: Campo de ordenação ("dataHoraInicio").
    """
    data = await get_deputy_speeches(
        deputy_id=deputy_id,
        idLegislatura=id_legislatura,
        dataInicio=data_inicio,
        dataFim=data_fim,
        ordenarPor=ordenar_por,
        ordem=ordem,
        itens=itens,
        pagina=pagina
    )
    return _json_response(data)


@mcp.tool()
async def get_deputy_events_tool(
    deputy_id: int,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "ASC",
    ordenar_por: str = "dataHoraInicio"
) -> str:
    """Consulta a lista de eventos e audiências com a participação do deputado.

    Args:
        deputy_id: Identificador numérico do deputado.
        data_inicio: Data inicial (AAAA-MM-DD).
        data_fim: Data final (AAAA-MM-DD).
        pagina: Página de resultados.
        itens: Quantidade de itens por página.
        ordem: Ordenação ("ASC" ou "DESC").
        ordenar_por: Campo de ordenação.
    """
    data = await get_deputy_events(
        deputy_id=deputy_id,
        dataInicio=data_inicio,
        dataFim=data_fim,
        pagina=pagina,
        itens=itens,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)


@mcp.tool()
async def get_deputy_fronts_tool(deputy_id: int) -> str:
    """Consulta as frentes parlamentares das quais o deputado é integrante.

    Args:
        deputy_id: Identificador numérico do deputado.
    """
    data = await get_deputy_fronts(deputy_id=deputy_id)
    return _json_response(data)


@mcp.tool()
async def get_deputy_history_tool(deputy_id: int) -> str:
    """Retorna o histórico de mudanças no exercício parlamentar de um deputado (licenças, trocas de partido, etc.).

    Args:
        deputy_id: Identificador numérico do deputado.
    """
    data = await get_deputy_history(deputy_id=deputy_id)
    return _json_response(data)


@mcp.tool()
async def get_deputy_external_mandates_tool(deputy_id: int) -> str:
    """Retorna outros cargos eletivos exercidos pelo parlamentar fora da Câmara (dados TSE).

    Args:
        deputy_id: Identificador numérico do deputado.
    """
    data = await get_deputy_external_mandates(deputy_id=deputy_id)
    return _json_response(data)


@mcp.tool()
async def get_deputy_occupations_tool(deputy_id: int) -> str:
    """Retorna as ocupações profissionais e empregos declarados pelo deputado.

    Args:
        deputy_id: Identificador numérico do deputado.
    """
    data = await get_deputy_occupations(deputy_id=deputy_id)
    return _json_response(data)


@mcp.tool()
async def get_deputy_organs_tool(
    deputy_id: int,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "ASC",
    ordenar_por: str = "dataInicio"
) -> str:
    """Retorna os órgãos, comissões e cargos que o deputado integra ou integrou.

    Args:
        deputy_id: Identificador numérico do deputado.
        data_inicio: Data inicial (AAAA-MM-DD).
        data_fim: Data final (AAAA-MM-DD).
        pagina: Página de resultados.
        itens: Quantidade de itens.
        ordem: Ordenação.
        ordenar_por: Campo de ordenação.
    """
    data = await get_deputy_organs(
        deputy_id=deputy_id,
        dataInicio=data_inicio,
        dataFim=data_fim,
        pagina=pagina,
        itens=itens,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data)


@mcp.tool()
async def get_deputy_professions_tool(deputy_id: int) -> str:
    """Retorna as profissões declaradas pelo deputado.

    Args:
        deputy_id: Identificador numérico do deputado.
    """
    data = await get_deputy_professions(deputy_id=deputy_id)
    return _json_response(data)


@mcp.tool()
async def get_legislature_leaders_tool(legislatura_id: int, pagina: int = 1, itens: int = 15) -> str:
    """Retorna líderes, vice-líderes e representantes partidários em uma determinada legislatura.

    Args:
        legislatura_id: Identificador da legislatura (ex.: 57).
        pagina: Página de resultados.
        itens: Itens por página.
    """
    data = await get_legislature_leaders(legislatura_id=legislatura_id, pagina=pagina, itens=itens)
    return _json_response(data)


@mcp.tool()
async def get_legislature_board_tool(
    legislatura_id: int,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None
) -> str:
    """Retorna os deputados que integraram a Mesa Diretora da Câmara em uma legislatura.

    Args:
        legislatura_id: Identificador da legislatura (ex.: 57).
        data_inicio: Data inicial (AAAA-MM-DD).
        data_fim: Data final (AAAA-MM-DD).
    """
    data = await get_legislature_board(legislatura_id=legislatura_id, dataInicio=data_inicio, dataFim=data_fim)
    return _json_response(data)

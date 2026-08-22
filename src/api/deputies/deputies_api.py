from typing import Any, Dict, List, Optional, Union
from src.api.client import get_request
from src.api.deputies.deputy_front_line import get_front_line_by_deputy


async def get_deputados(
    id: Optional[Union[int, List[int], str]] = None,
    nome: Optional[str] = None,
    idLegislatura: Optional[Union[int, List[int], str]] = None,
    siglaUf: Optional[Union[str, List[str]]] = None,
    siglaPartido: Optional[Union[str, List[str]]] = None,
    siglaSexo: Optional[str] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None,
    ordem: str = "ASC",
    ordenarPor: str = "nome"
) -> Optional[Dict[str, Any]]:
    """Busca e lista deputados segundo critérios de filtro."""
    params = {
        "id": id,
        "nome": nome,
        "idLegislatura": idLegislatura,
        "siglaUf": siglaUf,
        "siglaPartido": siglaPartido,
        "siglaSexo": siglaSexo,
        "pagina": pagina,
        "itens": itens,
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request("/deputados", params=params)


async def get_deputados_by_name(name: str) -> Optional[Dict[str, Any]]:
    """Busca deputados pelo nome e enriquece com detalhes adicionais (mantém compatibilidade)."""
    data = await get_deputados(nome=name)
    if not data:
        return None

    deputies_list = data.get("dados", [])
    if not deputies_list:
        return None

    deputies_details = []
    for deputy in deputies_list:
        deputy_id = deputy.get("id")
        if deputy_id:
            try:
                deputy_details = await get_deputy_details(deputy_id)
                if deputy_details and "dados" in deputy_details:
                    deputies_details.append(deputy_details["dados"])
                else:
                    deputies_details.append(deputy)
            except Exception:
                deputies_details.append(deputy)

    return {
        "dados": deputies_details,
        "links": data.get("links", []),
        "metadados": data.get("metadados", {})
    }


async def get_deputy_details(deputy_id: int) -> Optional[Dict[str, Any]]:
    """Busca detalhes de um deputado específico pelo ID."""
    response = await get_request(f"/deputados/{deputy_id}")
    if not response:
        return None

    front_line_response = await get_front_line_by_deputy(deputy_id)
    front_line_response_data = front_line_response.get("dados", []) if front_line_response else []

    deputies_front_line_list = []
    for front_line in front_line_response_data:
        deputies_front_line_list.append({
            "id": front_line.get("id"),
            "uri": front_line.get("uri"),
            "titulo": front_line.get("titulo"),
            "idLegislatura": front_line.get("idLegislatura"),
        })

    return {
        "dados": {
            "details": response.get("dados", {}),
            "deputy_front_lines": deputies_front_line_list
        }
    }


async def get_deputy_raw_details(deputy_id: int) -> Optional[Dict[str, Any]]:
    """Retorna os dados cadastrais diretos de um parlamentar identificado por ID."""
    return await get_request(f"/deputados/{deputy_id}")


async def get_deputy_expenses(
    deputy_id: int,
    idLegislatura: Optional[Union[int, List[int], str]] = None,
    ano: Optional[Union[int, List[int], str]] = None,
    mes: Optional[Union[int, List[int], str]] = None,
    cnpjCpfFornecedor: Optional[str] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15,
    ordem: str = "ASC",
    ordenarPor: str = "ano"
) -> Optional[Dict[str, Any]]:
    """Consulta as despesas da cota parlamentar (CEAP) de um deputado."""
    params = {
        "idLegislatura": idLegislatura,
        "ano": ano,
        "mes": mes,
        "cnpjCpfFornecedor": cnpjCpfFornecedor,
        "pagina": pagina,
        "itens": itens,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request(f"/deputados/{deputy_id}/despesas", params=params)


async def get_deputy_speeches(
    deputy_id: int,
    idLegislatura: Optional[Union[int, List[int], str]] = None,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None,
    ordenarPor: str = "dataHoraInicio",
    ordem: str = "DESC",
    itens: Optional[int] = 15,
    pagina: Optional[int] = 1
) -> Optional[Dict[str, Any]]:
    """Consulta os pronunciamentos/discursos feitos pelo deputado."""
    params = {
        "idLegislatura": idLegislatura,
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "ordenarPor": ordenarPor,
        "ordem": ordem,
        "itens": itens,
        "pagina": pagina
    }
    return await get_request(f"/deputados/{deputy_id}/discursos", params=params)


async def get_deputy_events(
    deputy_id: int,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15,
    ordem: str = "ASC",
    ordenarPor: str = "dataHoraInicio"
) -> Optional[Dict[str, Any]]:
    """Consulta eventos com a participação prevista ou realizada do deputado."""
    params = {
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "pagina": pagina,
        "itens": itens,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request(f"/deputados/{deputy_id}/eventos", params=params)


async def get_deputy_fronts(deputy_id: int) -> Optional[Dict[str, Any]]:
    """Consulta as frentes parlamentares das quais o deputado é integrante."""
    return await get_request(f"/deputados/{deputy_id}/frentes")


async def get_deputy_history(deputy_id: int) -> Optional[Dict[str, Any]]:
    """Retorna o histórico de mudanças no exercício parlamentar (versão otimizada)."""
    return await get_request(f"/deputados/{deputy_id}/historico")


async def get_deputy_history_old(deputy_id: int) -> Optional[Dict[str, Any]]:
    """Retorna o histórico de mudanças no exercício parlamentar (versão padrão)."""
    return await get_request(f"/deputados/{deputy_id}/historico-old")


async def get_deputy_external_mandates(deputy_id: int) -> Optional[Dict[str, Any]]:
    """Retorna outros cargos eletivos exercidos pelo parlamentar fora da Câmara (TSE)."""
    return await get_request(f"/deputados/{deputy_id}/mandatosExternos")


async def get_deputy_occupations(deputy_id: int) -> Optional[Dict[str, Any]]:
    """Retorna atividades profissionais/ocupações declaradas pelo parlamentar."""
    return await get_request(f"/deputados/{deputy_id}/ocupacoes")


async def get_deputy_organs(
    deputy_id: int,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15,
    ordem: str = "ASC",
    ordenarPor: str = "dataInicio"
) -> Optional[Dict[str, Any]]:
    """Retorna os órgãos e comissões que o parlamentar integra ou integrou."""
    params = {
        "dataInicio": dataInicio,
        "dataFim": dataFim,
        "pagina": pagina,
        "itens": itens,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request(f"/deputados/{deputy_id}/orgaos", params=params)


async def get_deputy_professions(deputy_id: int) -> Optional[Dict[str, Any]]:
    """Retorna profissões declaradas pelo parlamentar."""
    return await get_request(f"/deputados/{deputy_id}/profissoes")


async def get_legislature_leaders(
    legislatura_id: int,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15
) -> Optional[Dict[str, Any]]:
    """Retorna a lista de líderes, vice-líderes e representantes em uma legislatura."""
    params = {
        "pagina": pagina,
        "itens": itens
    }
    return await get_request(f"/legislaturas/{legislatura_id}/lideres", params=params)


async def get_legislature_board(
    legislatura_id: int,
    dataInicio: Optional[str] = None,
    dataFim: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """Retorna os deputados que fizeram parte da Mesa Diretora em uma legislatura."""
    params = {
        "dataInicio": dataInicio,
        "dataFim": dataFim
    }
    return await get_request(f"/legislaturas/{legislatura_id}/mesa", params=params)

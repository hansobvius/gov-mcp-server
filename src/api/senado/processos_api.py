from typing import Any, Dict, List, Optional, Union
from src.api.client import get_senado_request


async def get_processos(
    sigla: Optional[str] = None,
    numero: Optional[int] = None,
    ano: Optional[int] = None,
    autor: Optional[str] = None,
    tipo_autor: Optional[str] = None,
    situacao: Optional[str] = None,
    assunto: Optional[str] = None,
    classe: Optional[str] = None,
    itens: Optional[int] = None
) -> Optional[Dict[str, Any]]:
    """Pesquisa e lista processos legislativos no Senado Federal (rotas modernas /processo/).
    
    Args:
        sigla: Sigla do tipo do processo (ex.: PL, PEC, PDL).
        numero: Número do processo legislativo.
        ano: Ano de apresentação.
        autor: Nome ou identificação do autor.
        tipo_autor: Tipo do autor.
        situacao: Situação atual do processo.
        assunto: Assunto ou palavra-chave.
        classe: Classe processual.
        itens: Quantidade de itens retornados.
    """
    params = {
        "sigla": sigla,
        "numero": numero,
        "ano": ano,
        "autor": autor,
        "tipoAutor": tipo_autor,
        "situacao": situacao,
        "assunto": assunto,
        "classe": classe,
        "itens": itens,
    }
    return await get_senado_request("/processo", params=params)


async def get_processo_detalhes(processo_id: int) -> Optional[Dict[str, Any]]:
    """Obtém detalhes completos de um processo legislativo (ementa, autores, tramitações, relatorias).
    
    Args:
        processo_id: Identificador numérico do processo.
    """
    return await get_senado_request(f"/processo/{processo_id}")


async def get_processo_documentos(
    processo_id: Optional[int] = None,
    tipo_documento: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """Lista documentos associados a processos legislativos.
    
    Args:
        processo_id: Identificador do processo.
        tipo_documento: Tipo do documento desejado.
    """
    params = {
        "idProcesso": processo_id,
        "tipoDocumento": tipo_documento,
    }
    return await get_senado_request("/processo/documento", params=params)


async def get_processo_emendas(
    processo_id: Optional[int] = None,
    autor: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """Lista emendas apresentadas a processos legislativos.
    
    Args:
        processo_id: Identificador do processo.
        autor: Autor da emenda.
    """
    params = {
        "idProcesso": processo_id,
        "autor": autor,
    }
    return await get_senado_request("/processo/emenda", params=params)


async def get_processo_referencias(tabela: str) -> Optional[Dict[str, Any]]:
    """Consulta tabelas de referência do processo legislativo do Senado.
    
    Args:
        tabela: Nome da tabela (ex.: 'assuntos', 'classes', 'destinos', 'entes', 'siglas', 'tipos-autor', 'tipos-situacao').
    """
    clean_tabela = tabela.strip("/")
    if clean_tabela == "prazo/tipos":
        endpoint = "/processo/prazo/tipos"
    else:
        endpoint = f"/processo/{clean_tabela}"
    return await get_senado_request(endpoint)

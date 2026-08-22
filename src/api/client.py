import httpx
from typing import Any, Dict, List, Optional, Union
from src.config import URL_BASE_API

DEFAULT_TIMEOUT = 30.0
DEFAULT_HEADERS = {
    "Accept": "application/json"
}


def format_params(params: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    """Formata os parâmetros de busca para a API da Câmara.
    
    Remove valores nulos/vazios e converte listas/tuplas em strings separadas por vírgula.
    """
    if not params:
        return {}
    
    formatted = {}
    for key, value in params.items():
        if value is None:
            continue
        if isinstance(value, (list, tuple, set)):
            formatted[key] = ",".join(str(item) for item in value)
        elif isinstance(value, bool):
            formatted[key] = str(value).lower()
        else:
            formatted[key] = value
    return formatted


async def get_request(
    endpoint: str,
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: float = DEFAULT_TIMEOUT
) -> Optional[Dict[str, Any]]:
    """Executa uma requisição GET assíncrona na API de Dados Abertos da Câmara.

    Args:
        endpoint: Caminho relativo do endpoint (ex.: "/deputados" ou "deputados/123/despesas").
        params: Dicionário com parâmetros de query string.
        headers: Headers adicionais para a requisição.
        timeout: Tempo limite da requisição em segundos.

    Returns:
        Dicionário com o payload JSON de resposta, ou None em caso de falha.
    """
    clean_endpoint = endpoint.strip("/")
    url = f"{URL_BASE_API}/{clean_endpoint}"
    
    req_headers = DEFAULT_HEADERS.copy()
    if headers:
        req_headers.update(headers)
        
    formatted_params = format_params(params)

    async with httpx.AsyncClient(timeout=timeout) as client:
        try:
            response = await client.get(url, params=formatted_params, headers=req_headers)
            response.raise_for_status()
            return response.json()
        except (httpx.HTTPStatusError, httpx.RequestError, Exception):
            return None

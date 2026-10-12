from typing import Any, Dict, List, Optional, Union
from src.api.client import get_senado_request


async def get_orcamento_emendas(
    ano: Optional[int] = None,
    autor: Optional[str] = None,
    tipo_emenda: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """Consulta lotes de emendas ao Orçamento Geral da União.
    
    Args:
        ano: Ano orçamentário.
        autor: Autor da emenda parlamentar.
        tipo_emenda: Tipo da emenda (Individual, Bancada, Comissão).
    """
    params = {
        "ano": ano,
        "autor": autor,
        "tipoEmenda": tipo_emenda,
    }
    return await get_senado_request("/orcamento/lista", params=params)


async def get_orcamento_oficios(numero_sedol: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Consulta ofícios de apoio às emendas de orçamento ou detalhe de um ofício pelo número SEDOL.
    
    Args:
        numero_sedol: Número identificador SEDOL do ofício (opcional).
    """
    if numero_sedol:
        endpoint = f"/orcamento/oficios/{numero_sedol}"
    else:
        endpoint = "/orcamento/oficios"
    return await get_senado_request(endpoint)

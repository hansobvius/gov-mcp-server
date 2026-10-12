from typing import Any, Dict, List, Optional, Union
from src.api.client import get_senado_request


async def get_legislacao_lista(
    tipo: Optional[str] = None,
    numero: Optional[int] = None,
    ano: Optional[int] = None,
    termo: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """Pesquisa normas jurídicas federais (leis ordinárias, complementares, decretos, etc.).
    
    Args:
        tipo: Sigla do tipo da norma (ex.: LEI, LCP, DEC).
        numero: Número da norma.
        ano: Ano da norma.
        termo: Termo ou assunto de busca.
    """
    params = {
        "tipo": tipo,
        "numero": numero,
        "ano": ano,
        "termo": termo,
    }
    return await get_senado_request("/legislacao/lista", params=params)


async def get_legislacao_detalhes(codigo: Union[int, str]) -> Optional[Dict[str, Any]]:
    """Obtém detalhes, ementa e texto integral de uma norma jurídica.
    
    Args:
        codigo: Código ou URN identificadora da norma.
    """
    return await get_senado_request(f"/legislacao/{codigo}")


async def get_legislacao_tipos_norma() -> Optional[Dict[str, Any]]:
    """Lista a tabela de domínio dos tipos de normas jurídicas federais."""
    return await get_senado_request("/legislacao/tiposNorma")


async def get_legislacao_termos() -> Optional[Dict[str, Any]]:
    """Lista os termos e vocabulário controlado para pesquisa de normas federais."""
    return await get_senado_request("/legislacao/termos")


async def get_legislacao_classes() -> Optional[Dict[str, Any]]:
    """Lista as classes de classificação de normas legislativas."""
    return await get_senado_request("/legislacao/classes")

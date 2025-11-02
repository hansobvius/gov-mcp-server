import httpx
from typing import Any, Dict

from src.config import URL_BASE_API

async def get_propositions_by_id(proposition_id: str) -> Dict[str, Any] | None:
    """Busca proposições pelo ID na API da Câmara dos Deputados"""
    async with httpx.AsyncClient() as client:
        try:
            params = {
                "idDeputadoAutor": proposition_id,
                "ordem": "ASC",
                "ordenarPor": "id"
            }
            response = await client.get(
                f"{URL_BASE_API}/proposicoes/{proposition_id}",
                params=params,
                timeout=30.0)

            response.raise_for_status()
            data = response.json()

            return data
        except httpx.RequestError:
            return None


async def get_proposition_details(proposition_id: str) -> Dict[str, Any] | None:
    """Busca detalhes de uma proposição específica pelo ID"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{URL_BASE_API}/proposicoes/{proposition_id}/detalhes", timeout=30.0)
            response.raise_for_status()
            data = response.json()
            return data
        except httpx.RequestError:
            return None
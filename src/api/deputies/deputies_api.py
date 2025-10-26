import httpx

from typing import Any, Dict
from src.config import URL_BASE_API


async def get_deputados_by_name(name: str) -> Dict[str, Any] | None:
    async with httpx.AsyncClient() as client:
        try:
            params = {
                "nome": name,
                "ordem": "ASC",
                "ordernarPor": "nome"
            }
            response = await client.get(
                f"{URL_BASE_API}/deputados",
                params=params,
                timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError:
            return None

async def get_deputados_details(deputy_id: int) -> Dict[str, any] | None:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{URL_BASE_API}/deputados/{deputy_id}", timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError:
            return None
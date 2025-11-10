import httpx
import asyncio
from typing import Any, Dict

from src.config import URL_BASE_API

async def get_front_line_by_deputy(id: int) -> Dict[str, Any] | None:
    """Busca frentes parlamentares de um deputado específico pelo ID"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{URL_BASE_API}/deputados/{id}/frentes", timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError:
            return None